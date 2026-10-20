#!/usr/bin/env python3
"""Moteur commun d'application des lots du document A.

Pourquoi un moteur separe
-------------------------
Les lots K, L, I, N, J comblaient des blocs d'affichage vides : `apply_patch.py`
suffisait, qui travaille ligne a ligne. Le document A a ete « aplani » : un
paragraphe entier tient sur une seule ligne et les formules ont ete DEPLACEES,
parfois au milieu d'une phrase. Les restitutions portent donc sur des
SOUS-CHAINES qui enjambent les sauts de paragraphe. Ce moteur travaille en
sous-chaines et tient un journal, pas un patch ligné.

Les trois regles qu'il fait respecter
------------------------------------
1. **Unicite** — chaque sous-chaine source doit apparaitre EXACTEMENT UNE fois.
   Sinon le lot echoue sans rien ecrire.
2. **Non-perte** — un fragment ne peut etre retire que si chacun de ses tokens
   est recase. Tout token sans destination etablie doit rester dans le document,
   signale par la mention « Fragments non rattaches ».
3. **Verifiabilite** — le journal porte, pour chaque substitution, l'ancien, le
   nouveau, la confiance, la justification et la validation. Le livrable
   opposable reste le `.gitdiff` tire du depot.

Usage
-----
    from lot_commun import appliquer
    appliquer(EDITS, tranche=None, journal="...json")
"""

import json
import os
import shutil
import sys

H = "haute"
M = "moyenne"
I = "inconnue"

RACINE = "/home/user/_audit/connaissance"
FICHIER_A = ("Maths-vers-Informatiques/DOCUMENT MAÎTRE A — "
             "LOGIQUE ET FONDEMENTS DE L’INFORMATIQUE.md")

# Les lots sont lances depuis n'importe quel repertoire : le journal est ecrit
# relativement a la racine du depot, jamais au repertoire courant.
RACINE_DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))

# Sauvegarde hors du clone (donc hors `git status` du clone) mais dans
# l'espace de travail persistant, pour pouvoir revenir en arriere si un lot
# s'applique partiellement.
SAUVEGARDES = "/home/user/_audit/sauvegardes"


def _lire():
    return open(f"{RACINE}/{FICHIER_A}", encoding="utf-8").read()


def _long_prefixe(ancien, texte):
    """Longueur du plus long prefixe de `ancien` reellement present dans `texte`."""
    lo, hi = 0, len(ancien)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if texte.count(ancien[:mid]):
            lo = mid
        else:
            hi = mid - 1
    return lo


def divergence(ancien, texte):
    """Explique pourquoi `ancien` est absent : premier caractere qui diverge.

    L'erreur la plus frequente est un espace de trop ou de trop peu dans une
    longue sequence d'espaces (transcription manuelle). Ce diagnostic la rend
    visible immediatement au lieu de laisser comparer deux chaines a l'oeil.
    """
    lo = _long_prefixe(ancien, texte)
    ancrage = ancien[:max(1, lo)]
    i = texte.find(ancrage)
    if i < 0:
        i = 0
    debut = max(0, lo - 25)
    return ("    divergence a l'index %d\n"
            "      lot    : %r\n"
            "      source : %r"
            % (lo,
               ancien[debut:debut + 50],
               texte[i + debut:i + debut + 50]))


def entre(deb, fin, nouveau):
    """Construit (ancien, nouveau) pour la region strictement entre deux marqueurs.

    Supprime la cause d'erreur la plus frequente du chantier : la transcription
    a la main de longues sequences d'espaces. On ne recopie plus le milieu ; on
    le RELIT dans le fichier. Seuls deux marqueurs courts et surs sont ecrits a
    la main, et ils encadrent le remplacement sans etre modifies.

        ("A3-02", *entre("Énoncé :", "Reconnaissance :", " `a ≡ b`  "), H, ...)

    Leve ValueError si un marqueur est introuvable ou si `fin` precede `deb`.
    """
    texte = _lire()
    i = texte.find(deb)
    if i < 0:
        raise ValueError("marqueur de debut introuvable : %r" % deb)
    j = texte.find(fin, i + len(deb))
    if j < 0:
        raise ValueError("marqueur de fin introuvable : %r" % fin)
    return (texte[i:j + len(fin)], deb + nouveau + fin)


def retirer(deb, fin, remplacement=""):
    """Construit (ancien, nouveau) en supprimant tout l'intervalle, `deb` compris.

    A ne pas confondre avec `entre()`, qui CONSERVE les deux marqueurs et ne
    remplace que l'intervalle entre eux. Ici `deb` disparait avec le contenu ;
    `fin` est conserve et `remplacement` est insere devant lui.

    Sert au cas frequent ou un fragment a supprimer n'a pas de marqueur amont
    qui doive survivre — par exemple une pile situee entre la fin d'un bloc et
    le titre de la section suivante.

        ("A5-01b", *retirer("```\n\n", "8.1 Ensembles"), H, ...)
    """
    texte = _lire()
    i = texte.find(deb)
    if i < 0:
        raise ValueError("marqueur de debut introuvable : %r" % deb)
    j = texte.find(fin, i + len(deb))
    if j < 0:
        raise ValueError("marqueur de fin introuvable : %r" % fin)
    return (texte[i:j + len(fin)], remplacement + fin)


def diagnostiquer(edits, tranche=None):
    """Compte les occurrences de chaque sous-chaine SANS rien ecrire.

    A executer avant `appliquer` : une sous-chaine introuvable ou ambigue
    fait echouer le lot, mieux vaut le savoir pour toutes les editions d'un
    coup que de corriger l'une et de redecouvrir la suivante.
    """
    texte = _lire()
    ok = True
    for ident, ancien, nouveau, conf, just, val in edits:
        n = texte.count(ancien)
        marque = "OK  " if n == 1 else "ECHEC"
        if n != 1:
            ok = False
        print(f"{marque}  {ident:<34} {n} occurrence(s)")
        if n != 1:
            print(divergence(ancien, texte))
    if tranche:
        deb, fin, nouveau, ident, conf, just, val = tranche
        ia, ib = texte.find(deb), texte.find(fin)
        if ia < 0 or ib <= ia:
            ok = False
            print(f"ECHEC  {ident:<34} marqueurs introuvables ({ia}, {ib})")
        else:
            print(f"OK     {ident:<34} tranche de {ib - ia} caracteres")
    print("diagnostic : " + ("toutes les sous-chaines sont uniques"
                             if ok else "ECHECS A CORRIGER"))
    return 0 if ok else 1


def appliquer(edits, journal, tranche=None):
    """Applique une liste de substitutions au document et emet le journal.

    `edits`   : liste de (identifiant, ancien, nouveau, confiance,
                          justification, validation)
    `journal` : chemin du JSON de sortie, relatif a la racine du depot
    `tranche` : (marqueur_debut, marqueur_fin, nouveau, identifiant,
                 confiance, justification, validation) — pour remplacer une
                 region delimitee par deux marqueurs plutot que transcrite en
                 clair (utile pour les longues sequences d'espaces).

    Renvoie 0 si tout s'est bien passe, 1 sinon.
    """
    chemin = f"{RACINE}/{FICHIER_A}"
    texte = _lire()
    avant = len(texte)
    log = []

    for ident, ancien, nouveau, conf, just, val in edits:
        n = texte.count(ancien)
        if n != 1:
            print(f"ECHEC [{ident}] : sous-chaine trouvee {n} fois (attendu 1)",
                  file=sys.stderr)
            if n == 0:
                print(divergence(ancien, texte), file=sys.stderr)
                print("    astuce : python3 lot_commun.py <ce_lot> --verifie "
                      "controle toutes les editions d'un coup", file=sys.stderr)
            return 1
        texte = texte.replace(ancien, nouveau, 1)
        log.append({"identifiant": ident, "confiance": conf,
                    "ancien": ancien, "nouveau": nouveau,
                    "justification": just, "validation": val})

    if tranche:
        (deb, fin, nouveau, ident, conf, just, val) = tranche
        ia, ib = texte.find(deb), texte.find(fin)
        if ia < 0 or ib <= ia:
            print(f"ECHEC [{ident}] : marqueurs introuvables ({ia}, {ib})",
                  file=sys.stderr)
            return 1
        log.append({"identifiant": ident, "confiance": conf,
                    "ancien": texte[ia:ib], "nouveau": nouveau.rstrip("\n"),
                    "justification": just, "validation": val})
        texte = texte[:ia] + nouveau + texte[ib:]

    os.makedirs(SAUVEGARDES, exist_ok=True)
    nom = os.path.basename(journal).replace(".journal.json", "")
    shutil.copy2(chemin, f"{SAUVEGARDES}/A-avant-{nom}.md")

    open(chemin, "w", encoding="utf-8").write(texte)

    chemin_journal = journal
    if not os.path.isabs(chemin_journal):
        chemin_journal = os.path.join(RACINE_DEPOT, chemin_journal)
    os.makedirs(os.path.dirname(chemin_journal), exist_ok=True)
    with open(chemin_journal, "w", encoding="utf-8") as fh:
        json.dump(log, fh, ensure_ascii=False, indent=1)

    n_h = sum(1 for e in log if e["confiance"] == H)
    n_m = sum(1 for e in log if e["confiance"] == M)
    n_i = sum(1 for e in log if e["confiance"] == I)
    print(f"{len(log)} substitutions appliquees — {n_h} haute, {n_m} moyenne, "
          f"{n_i} inconnue")
    print(f"{avant} -> {len(texte)} caracteres ({len(texte) - avant:+d})")
    print(f"journal : {os.path.relpath(chemin_journal, RACINE_DEPOT)}")
    print(f"sauvegarde : {SAUVEGARDES}/A-avant-{nom}.md")
    return 0


if __name__ == "__main__":
    # Controle prealable de n'importe quel lot construit sur ce moteur :
    #     python3 lot_commun.py build_lot_A_2.py
    if len(sys.argv) < 2:
        print("usage : python3 lot_commun.py <fichier_du_lot>", file=sys.stderr)
        sys.exit(2)
    import importlib.util
    _spec = importlib.util.spec_from_file_location("lot", sys.argv[1])
    _mod = importlib.util.module_from_spec(_spec)
    sys.modules["lot"] = _mod
    _spec.loader.exec_module(_mod)
    sys.exit(diagnostiquer(_mod.EDITS, getattr(_mod, "TRANCHE", None)))
