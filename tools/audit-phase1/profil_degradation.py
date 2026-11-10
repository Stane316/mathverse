#!/usr/bin/env python3
"""
Profil structurel d'un ou plusieurs documents du corpus de connaissances.

Objectif : distinguer, par la mesure, les documents dont la structure markdlown
est intacte de ceux qui en ont ete depouilles (documents "aplanis"), et
caracteriser la degradation sans rien reconstruire.

Le profil ne restaure rien et ne propose rien : il mesure. Toute restitution de
contenu reste soumise a la validation lot par lot decrite dans
docs/restauration/CLOTURE-CHANTIER.md.

Usage
-----
    python3 profil_degradation.py <racine_du_clone>            # tout le corpus
    python3 profil_degradation.py <fichier.md> [<fichier.md>]  # documents donnes

Le script accepte une racine de clone : il retient alors tous les *.md situes
sous « Maths-vers-Informatiques/ ».

Sortie
------
Un tableau par document, puis un diagnostic. Le script se termine par un code
de retour 0 dans tous les cas : c'est un outil de mesure, pas un test.
"""

import os
import re
import sys
import glob
import collections

RACINE_DOCS = "Maths-vers-Informatiques"

# Vocabulaire de la couche de preuve. Les motifs couvrent pluriels et variantes
# accentuees ; ils sont volontairement larges mais non stemmatises.
VOCABULAIRE_PREUVE = {
    "hypothèse": r"hypoth[eèê]se",
    "preuve": r"preuve",
    "validation": r"validation",
    "contre-exemple": r"contre[-\s]exemple",
    "limite": r"limite",
    "erreur": r"erreur",
    "algorithme": r"algorithme",
    "complexité": r"complexité",
    "référence": r"référence",
    "test": r"\btest",
}

# Symboles logiques et mathematiques recherches dans le texte nu.
SYMBOLES = "∀∃∈∉⊂⊆∪∩∧∨¬⇒⇔→↔⊕⊢⊨≡≠≤≥×÷√∞∑∏∫∅ℕℤℚℝℂ⊤⊥"

# Balises de langage susceptibles d'avoir survecu a l'aplanissement d'un bloc
# de code : elles apparaissent alors comme un mot isole dans la prose.
BALISES_LANGAGE = ["JavaScript", "TypeScript", "Python", "Prolog", "SQL",
                   "Bash", "C++", "Java", "Go", "Rust"]


def profiler(chemin):
    """Renvoye le profil de structure d'un document."""
    with open(chemin, encoding="utf-8") as f:
        t = f.read()

    nb_car = len(t)
    nb_lig = t.count("\n") + 1
    nb_non_vides = sum(1 for l in t.split("\n") if l.strip())

    def c(pat, flags=0):
        return len(re.findall(pat, t, flags))

    symboles = collections.Counter(ch for ch in t if ch in SYMBOLES)

    vocab = {}
    for nom, motif in VOCABULAIRE_PREUVE.items():
        n = c(motif, re.I)
        # densite pour 10 000 caracteres : seule normalisation honnete ici, les
        # regimes de lignes etant incomparables d'un document a l'autre.
        vocab[nom] = (n, round(n * 10000 / nb_car, 1) if nb_car else 0.0)

    balises = {b: len(re.findall(r"(?<![\w])%s(?![\w])" % re.escape(b), t))
               for b in BALISES_LANGAGE}
    balises = {b: n for b, n in balises.items() if n}

    return {
        "chemin": chemin,
        "nom": os.path.basename(chemin),
        "caracteres": nb_car,
        "octets": os.path.getsize(chemin),
        "lignes": nb_lig,
        "non_vides": nb_non_vides,
        "car_par_ligne": nb_car // max(1, nb_non_vides),
        "titres_md": c(r"^#{1,6}\s", re.M),
        "blocs_display": c(r"\\\["),
        "gras": c(r"\*\*"),
        "pipes": t.count("|"),
        "puces": c(r"^\s*[-*+]\s", re.M),
        "backticks": t.count("`"),
        "backslahes": t.count("\\"),
        "espaces_2": len(re.findall(r" {2,}", t)),
        "run_2": c(r"(?<! ) {2}(?! )"),
        "run_3plus": c(r" {3,}"),
        "tables_verite": c(r"(?:\b[VF]\b\s+){5,}"),
        "symboles": symboles,
        "vocabulaire": vocab,
        "balises_langage": balises,
    }


def diagnostiquer(p):
    """Classe un document : structure intacte ou aplanie."""
    if p["titres_md"] >= 50 and p["blocs_display"] >= 1:
        return "structuree"
    if p["titres_md"] == 0 and p["blocs_display"] == 0 and p["puces"] == 0:
        return "aplanie"
    return "intermediaire"


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)

    fichiers = []
    for a in args:
        if os.path.isdir(a):
            motif = os.path.join(a, RACINE_DOCS, "*.md")
            fichiers += sorted(glob.glob(motif))
            if not fichiers:
                fichiers = sorted(glob.glob(os.path.join(a, "**", "*.md"),
                                            recursive=True))
        else:
            fichiers.append(a)

    if not fichiers:
        print("Aucun document .md trouve.")
        return

    profils = [profiler(f) for f in fichiers]
    profils.sort(key=lambda p: p["nom"])

    entete = "%-12s %8s %6s %7s %6s %6s %5s %5s %6s  %s"
    print(entete % ("document", "caract.", "lignes", "car/lig", "tit#",
                    "blocs", "**", "puce", "esp2+", "diagnostic"))
    print("-" * 88)
    for p in profils:
        print("%-12s %8d %6d %7d %6d %6d %5d %5d %6d  %s" % (
            p["nom"][:12], p["caracteres"], p["lignes"],
            p["car_par_ligne"], p["titres_md"], p["blocs_display"],
            p["gras"], p["puces"], p["espaces_2"], diagnostiquer(p)))
    print("-" * 88)
    print("tit# = titres markdown ^# ; blocs = \\\\[ ; ** = gras ; "
          "puce = listes ; esp2+ = runs d'espaces multiples ; "
          "car/lig = caracteres par ligne non vide")

    if len(profils) == 1:
        p = profils[0]
        print("\n=== detail : %s ===" % p["nom"])
        print("  diagnostic          : %s" % diagnostiquer(p))
        print("  octets / caracteres : %d / %d" % (p["octets"], p["caracteres"]))
        print("  lignes non vides    : %d (moyenne %d caracteres)"
              % (p["non_vides"], p["car_par_ligne"]))
        print("  backslashes / backticks / pipes : %d / %d / %d"
              % (p["backslahes"], p["backticks"], p["pipes"]))
        print("  runs de 2 espaces   : %d" % p["run_2"])
        print("  runs de 3 espaces+  : %d" % p["run_3plus"])
        print("  tables de verite    : %d sequences V/F" % p["tables_verite"])
        print("  balises de langage  : %s"
              % (", ".join("%s x%d" % (b, n)
                           for b, n in p["balises_langage"].items()) or "aucune"))
        print("  symboles presents   : %s"
              % (" ".join(sorted(p["symboles"])) or "aucun"))
        print("\n  vocabulaire de preuve (occurrences, puis pour 10 000 caracteres) :")
        for nom, (n, d) in p["vocabulaire"].items():
            print("    %-16s %4d   %5.1f" % (nom, n, d))

    ap = [p for p in profils if diagnostiquer(p) == "aplanie"]
    if ap:
        print("\n=== documents aplanis : %d ===" % len(ap))
        for p in ap:
            print("  %s" % p["nom"])


if __name__ == "__main__":
    main()
