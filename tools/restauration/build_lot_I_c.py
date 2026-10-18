#!/usr/bin/env python3
"""Lot 3c : domaine I, section 177 — SYNTHESE DES DOMAINES PRECEDENTS.

Neuf blocs vides consecutifs (l. 3024 a 3040 dans le fichier restaure),
introduits par : « La progression mathematique construite jusqu'ici peut
etre resumee ainsi : ».

Le document J, redige par le meme auteur, contient une section du meme type
(§155, « La progression construite jusqu'ici peut etre comprise comme : »)
qui contient DIX blocs vides suivis d'un bloc survivant : \\[ IJ \\].
L'hypothese A→…→J y a ete soumise puis VALIDEE PAR L'AUTEUR le 2026-10-18 :
les blocs sont les domaines traverses, un par bloc.

Le domaine I etant le neuvieme document du corpus et son §177 comptant
exactement NEUF blocs, la meme lecture s'applique : A, B, C, D, E, F, G, H, I.

Deux reserves sont portees :
  - aucun caractere ne subsiste dans les blocs : le residu est vide ;
  - l'argument est une analogie entre deux documents, pas une preuve
    interne au document I.
La confiance declaree est donc « moyenne ».

NOTE SUR LE PERIMETRE : ce lot ne reprend pas les blocs deja restaures par
les lots 3a et 3b. Une verification croisee a ete faite : sur les 37 blocs
encore degrades du document, 28 avaient deja ete soumis comme inconnues et
9 — ceux-ci — n'avaient jamais ete soumis.
"""

import json

SOURCE = ("Maths-vers-Informatiques/Domaine I - Calcul différentiel "
          "— Cartographie complète pour le machine learning.md")
RACINE = "/home/user/_audit/connaissance"
SORTIE = "docs/restauration/propositions/domaine-I-lot3c.patch.json"

DOMAINES = [
    ("A", "DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L’INFORMATIQUE"),
    ("B", "DOCUMENT B — THÉORIE DES NOMBRES"),
    ("C", "DOCUMENT C — ALGÈBRE LINÉAIRE"),
    ("D", "DOCUMENT D — GÉOMÉTRIE COMPUTATIONNELLE"),
    ("E", "DOCUMENT E — THÉORIE DES GRAPHES"),
    ("F", "DOCUMENT F — COMBINATOIRE ET OPTIMISATION COMBINATOIRE"),
    ("G", "Document G — Probabilités"),
    ("H", "Document H — Statistiques"),
    ("I", "Domaine I — Calcul différentiel (le présent document)"),
]

LIGNES = list(range(3024, 3041, 2))

JUSTIF = ("§177 « La progression mathématique construite jusqu'ici peut être résumée "
          "ainsi : » suivi de neuf blocs vides.")

E = []
for (lettre, titre), ligne in zip(DOMAINES, LIGNES):
    E.append((
        ligne, ligne, f"\\[ {lettre} \\]", "moyenne",
        JUSTIF,
        f"Domaine {lettre} — {titre}. Analogie avec le §155 du domaine J (même formule "
        f"d'introduction, dix blocs pour dix domaines), hypothèse A→J validée par "
        f"l'auteur le 2026-10-18. Le résidu du bloc est vide.",
    ))


def main():
    lignes = open(f"{RACINE}/{SOURCE}", encoding="utf-8").read().split("\n")
    out = [{
        "fichier": SOURCE, "ligne": deb,
        "ancien": "\n".join(lignes[deb - 1:fin]),
        "nouveau": nouv, "confiance": conf,
        "justification": just, "validation": val,
    } for deb, fin, nouv, conf, just, val in E]
    json.dump(out, open(SORTIE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(out)} entrees -> {SORTIE}")
    print("applicables :", sum(1 for e in out if e["nouveau"]))
    for e in out:
        assert e["ancien"].strip() == "\\[ \\]", (e["ligne"], e["ancien"])


if __name__ == "__main__":
    main()
