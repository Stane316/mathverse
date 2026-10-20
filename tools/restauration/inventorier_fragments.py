#!/usr/bin/env python3
"""
Inventaire des formules deplacees dans un document « aplani » du corpus.

Contexte
--------
Les documents A, B, C et D du corpus ont ete depouilles de toute structure
Markdown : plus aucun titre, plus aucune liste, plus aucun tableau, plus aucune
balise LaTeX. Leurs formules n'ont toutefois pas ete supprimees : elles ont ete
retirees de leur emplacement, concatenees, puis reinserees ailleurs — parfois au
milieu d'une phrase.

Ce script ne restaure rien. Il produit l'inventaire qui sert de matiere premiere
aux propositions de restauration, lesquelles restent soumises a la validation
lot par lot decrite dans docs/restauration/CLOTURE-CHANTIER.md.

Deux objets sont recherches :

1. les **fragments** — suites de tokens mathematiques consecutifs qui ne
   peuvent pas etre de la prose ;
2. les **emplacements vides** — points du texte ou une formule a manifestement
   ete retiree (par exemple « Initialisation : _ . »).

Usage
-----
    python3 inventorier_fragments.py <fichier.md> [--slots] [--contexte N]

Options
-------
    --slots       affiche aussi les emplacements vides detectes
    --contexte N  longueur du contexte affiche avant/apres (defaut 70)
"""

import re
import sys

# Caracteres qui ne peuvent apparaitre que dans une formule.
SYMBOLES = set("¬∧∨→↔⇒⇔⊢⊨≡⊤⊥∀∃∈∉∅⊂⊆∪∩≤≥≠±×÷∑∏∫√∞ℕℤℚℝℂ=^_|~")
SYMBOLES |= set("αβγδεθλμπρστφψωΓΔΘΛΣΦΨΩ")

# Ponctuation qui n'interrompt pas une formule si elle est encadree de tokens
# mathematiques — elle fait partie de la notation.
PONCT = set("(),;:[]{}")

# Sections : « 1. IDENTITE » (niveau 1) et « 3.1 Les connecteurs » (niveau 2).
ANC_1 = re.compile(r"(?<![\d.])(\d{1,2})\.\s+[A-ZÀ-Ÿ]{3,}")
ANC_2 = re.compile(r"(?<![\d.])(\d{1,2}\.\d{1,2})\s+[A-ZÀ-Ÿ]")


def est_math(tok):
    """Un token est mathematique s'il porte un symbole, ou s'il est reduit a
    un seul caractere (variable, chiffre, valeur de verite)."""
    if not tok:
        return False
    if any(c in SYMBOLES for c in tok):
        return True
    if len(tok) == 1 and (tok.isalnum()):
        return True
    # suites de chiffres et de ponctuation de notation, ex. « 2 » « 10 »
    if all(c.isdigit() or c in PONCT for c in tok) and any(c.isdigit() for c in tok):
        return True
    return False


def est_ponct(tok):
    return len(tok) == 1 and tok in PONCT


def ancres(texte):
    """Liste des (position, libelle) des sections du document."""
    out = []
    for m in ANC_1.finditer(texte):
        # libelle = le motif entier, prolonge jusqu'au double espace suivant
        suite = texte[m.start():m.start() + 60].split("  ")[0]
        out.append((m.start(), suite.strip()))
    for m in ANC_2.finditer(texte):
        suite = texte[m.start():m.start() + 60].split("  ")[0]
        out.append((m.start(), suite.strip()))
    out.sort()
    return out


def ancre_avant(pos, anc):
    r = [a for a in anc if a[0] <= pos]
    return r[-1][1] if r else "(debut du document)"


def fragments(texte):
    """Suites de tokens mathematiques consecutifs, separees par des blancs."""
    res = []
    courant = []
    for m in re.finditer(r"\S+", texte):
        tk = m.group(0)
        if est_math(tk) or est_ponct(tk):
            courant.append((m.start(), m.end(), tk))
        else:
            res.append(courant)
            courant = []
    res.append(courant)

    runs = []
    for seq in res:
        # ne garder que les portions contenant au moins 2 tokens vraiment
        # mathematiques et au moins un symbole : sinon c'est de la prose.
        maths = [x for x in seq if est_math(x[2])]
        if len(maths) < 2:
            continue
        if not any(any(c in SYMBOLES for c in x[2]) or len(x[2]) == 1 for x in maths):
            continue
        debut, fin = seq[0][0], seq[-1][1]
        contenu = texte[debut:fin]
        if len(contenu.strip()) < 2:
            continue
        runs.append((debut, fin, contenu))
    return runs


def emplacements_vides(texte):
    """Points ou une formule a manifestement ete retiree.

    Motifs retenus, tous verifies sur le document A :
      - « : _ . »   deux-points, blancs, point       ( « Initialisation : . » )
      - « a _ . »   preposition, blancs, point       ( « penser a . » )
      - « de _ , »  preposition, blancs, virgule
      - « : _ ; »   deux-points, blancs, point-virgule
    """
    motifs = [
        (r":\s{2,}\.", ": … ."),
        (r"\bà\s{2,}\.", "à … ."),
        (r"\bde\s{2,},", "de … ,"),
        (r":\s{2,};", ": … ;"),
        (r"\bque\s{2,}\.", "que … ."),
        (r"\bde\s{2,}\.", "de … ."),
        (r"\bsur\s{2,}\.", "sur … ."),
        (r"\bun\s{2,},", "un … ,"),
    ]
    out = []
    for pat, lab in motifs:
        for m in re.finditer(pat, texte):
            out.append((m.start(), m.end(), lab, m.group(0)))
    out.sort()
    return out


def main():
    args = [a for a in sys.argv[1:]]
    if not args:
        sys.exit(__doc__)
    chemin = args[0]
    avec_slots = "--slots" in args
    ctx = 70
    if "--contexte" in args:
        ctx = int(args[args.index("--contexte") + 1])

    with open(chemin, encoding="utf-8") as f:
        t = f.read()
    anc = ancres(t)

    frags = fragments(t)
    print("=" * 96)
    print("FRAGMENTS DE FORMULES — %s" % chemin.rsplit("/", 1)[-1])
    print("=" * 96)
    print("%d fragments detectes\n" % len(frags))
    for i, (a, b, contenu) in enumerate(frags, 1):
        av = t[max(0, a - ctx):a].replace("\n", " ")
        ap = t[b:b + ctx].replace("\n", " ")
        print("[%3d] @%d  section : %s" % (i, a, ancre_avant(a, anc)))
        print("      FRAGMENT : « %s »" % contenu.replace("\n", " "))
        print("      avant    : ...%s" % av)
        print("      apres    : %s..." % ap)
        print()

    if avec_slots:
        vides = emplacements_vides(t)
        print("=" * 96)
        print("EMPLACEMENTS VIDES — %d" % len(vides))
        print("=" * 96)
        for a, b, lab, brut in vides:
            av = t[max(0, a - ctx):a].replace("\n", " ")
            print("@%d [%s]  ...%s«%s»..." % (a, lab, av, brut))

    print("=" * 96)
    print("Rappel : cet inventaire est une matiere premiere. Aucune restitution")
    print("n'est proposee ici ; elle reste soumise a validation lot par lot.")
    print("=" * 96)


if __name__ == "__main__":
    main()
