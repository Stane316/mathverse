#!/usr/bin/env python3
"""Extraction compacte de tous les blocs d'affichage d'un document.

Objectif : permettre la relecture exhaustive imposee par la methode "un bloc a la
fois", sans ingerer un document entier. Pour chaque bloc \\[ ... \\], on sort :

    L<deb>-<fin> | AVANT: <derniere ligne non vide avant> >>> <contenu> <<< APRES: <ligne suivante>

Deux modes :
  --tous  (defaut) tous les blocs ;
  --defauts  uniquement les blocs degrades (vides, fragments de commande,
             parentheses vides, egalite en tete ou en queue, indice orphelin).

Options :
  --avant N   nombre de lignes de contexte avant (defaut 2)
  --apres N   nombre de lignes de contexte apres (defaut 1)
  --trunc N   troncature des contextes (defaut 150)

Aucune ecriture. Deterministe. Aucun reseau. Sortie sur stdout.

Usage :
  python3 tools/restauration/extract_blocks.py <fichier.md> [--defauts] [--avant 3]
"""

import argparse
import re
import sys

VIDE = re.compile(r"^\s*\\\[\s*(\.|,|;|:|)\s*\\\]\s*$")
FRAGMENT = re.compile(r"^\s*\\\[\s*[\\_^{}]*\s*\\\]\s*$")
PAR_VIDES = re.compile(r"^\s*\\\[\s*\\left[()]?\s*\\right[()]?\s*\\\]\s*$")
EGAL_TETE = re.compile(r"^\s*\\\[\s*=")
EGAL_QUEUE = re.compile(r"=\s*\\\]\s*$")
INDICE_ORPHELIN = re.compile(r"^\s*\\\[\s*[_^{][^\\]*\s*\\\]\s*$")


def est_degrade(contenu):
    """Vrai si le bloc porte une marque de degradation."""
    if not contenu.strip():
        return True
    for motif in (VIDE, FRAGMENT, PAR_VIDES, INDICE_ORPHELIN):
        if motif.match(contenu):
            return True
    if EGAL_TETE.match(contenu) or EGAL_QUEUE.search(contenu):
        return True
    return False


def blocs(lignes):
    """Rend (debut, fin, texte) pour chaque bloc d'affichage, en numerotation 1."""
    res = []
    i = 0
    n = len(lignes)
    while i < n:
        if "\\begin{" in lignes[i]:
            # environnement LaTeX : on le rend tel quel jusqu'a \end{...}
            deb = i
            while i < n and "\\end{" not in lignes[i]:
                i += 1
            res.append((deb, i, "\n".join(lignes[deb:i + 1])))
            i += 1
            continue
        if "\\]" in lignes[i] and "\\[" not in lignes[i]:
            # bloc fermant seul : ignore (fin de bloc multi-lignes traitee plus haut)
            i += 1
            continue
        if "\\[" in lignes[i]:
            deb = i
            if "\\]" in lignes[i][lignes[i].index("\\[") + 2:]:
                res.append((deb, i, lignes[i]))
                i += 1
                continue
            i += 1
            while i < n and "\\]" not in lignes[i]:
                i += 1
            if i < n:
                res.append((deb, i, "\n".join(lignes[deb:i + 1])))
            i += 1
            continue
        i += 1
    # passage en numerotation 1
    return [(d + 1, f + 1, t) for d, f, t in res]


def contexte(lignes, debut, fin, avant, apres, trunc):
    prec = []
    i = debut - 2
    while i >= 0 and len(prec) < avant:
        if lignes[i].strip():
            prec.insert(0, lignes[i].strip())
        i -= 1
    suiv = []
    i = fin
    while i < len(lignes) and len(suiv) < apres:
        if lignes[i].strip():
            suiv.append(lignes[i].strip())
        i += 1
    f = lambda s: (s[:trunc] + "…") if len(s) > trunc else s
    return f(" / ".join(prec)), f(" / ".join(suiv))


def main():
    ap = argparse.ArgumentParser(description="Extraction compacte des blocs d'affichage")
    ap.add_argument("fichier")
    ap.add_argument("--defauts", action="store_true", help="uniquement les blocs degrades")
    ap.add_argument("--avant", type=int, default=2)
    ap.add_argument("--apres", type=int, default=1)
    ap.add_argument("--trunc", type=int, default=150)
    a = ap.parse_args()

    texte = open(a.fichier, encoding="utf-8", errors="replace").read()
    lignes = texte.split("\n")
    liste = blocs(lignes)
    nb_def = 0
    for deb, fin, cont in liste:
        degrade = est_degrade(cont)
        if degrade:
            nb_def += 1
        if a.defauts and not degrade:
            continue
        avant, apres = contexte(lignes, deb, fin, a.avant, a.apres, a.trunc)
        marque = "  **DEGRADE**" if degrade else ""
        if deb == fin:
            print(f"L{deb}{marque} | AVANT: {avant} >>> {cont.strip()} <<< APRES: {apres}")
        else:
            print(f"L{deb}-{fin}{marque} | AVANT: {avant}")
            for k in range(deb, fin + 1):
                print(f"   {lignes[k-1]}")
            print(f"   <<< APRES: {apres}")
    print(f"\n# {len(liste)} blocs, {nb_def} degrades — {a.fichier}", file=sys.stderr)


if __name__ == "__main__":
    main()
