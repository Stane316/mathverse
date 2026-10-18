#!/usr/bin/env python3
"""Lot 5c : domaine J, section 155 — LA GRANDE CARTE DES DOMAINES.

Dix blocs vides consecutifs (l. 3386 a 3404), suivis du seul bloc survivant de
la section : \\[ IJ \\], qui restitue une fleche entre deux lettres de domaines.

Hypothese soumise dans le lot 5b et VALIDEE PAR L'AUTEUR le 2026-10-18 :
les dix blocs sont les dix domaines traverses, A puis B puis ... puis J, la
transition mise en avant par le texte etant la derniere, I -> J.

Deux elements etayent cette lecture :

  1. le corpus compte exactement dix documents jusqu'a J — A, B, C, D, E, F,
     G, H, I, J — dans cet ordre ;
  2. la distinction des formes : un bloc d'une seule lettre designe un domaine,
     un bloc de deux lettres designe une transition. C'est ce que montre le
     bloc survivant, introduit par « La transition : ». Si les dix blocs
     avaient ete des transitions, le onzieme serait redondant.

Encoding retenu : une lettre par bloc, nue, comme dans \\[ IJ \\].

Confiance moyenne : l'hypothese est validee, mais le residu de chaque bloc est
vide — aucun caractere ne subsiste pour la confirmer bloc par bloc.
"""

import json

SOURCE = "Maths-vers-Informatiques/Domaine J — Optimisation.md"
RACINE = "/home/user/_audit/connaissance"
SORTIE = "docs/restauration/propositions/domaine-J-lot5c.patch.json"

DOMAINES = [
    ("A",   "DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L’INFORMATIQUE"),
    ("B",   "DOCUMENT B — THÉORIE DES NOMBRES"),
    ("C",   "DOCUMENT C — ALGÈBRE LINÉAIRE"),
    ("D",   "DOCUMENT D — GÉOMÉTRIE COMPUTATIONNELLE"),
    ("E",   "DOCUMENT E — THÉORIE DES GRAPHES"),
    ("F",   "DOCUMENT F — COMBINATOIRE ET OPTIMISATION COMBINATOIRE"),
    ("G",   "Document G — Probabilités"),
    ("H",   "Document H — Statistiques"),
    ("I",   "Domaine I — Calcul différentiel"),
    ("J",   "Domaine J — Optimisation (le présent document)"),
]

LIGNES = list(range(3386, 3405, 2))

JUSTIF = ("§155 « La progression construite jusqu'ici peut être comprise comme : » "
          "suivi de dix blocs vides, puis « La transition : [I→J] est particulièrement "
          "importante. ».")

E = []
for (lettre, titre), ligne in zip(DOMAINES, LIGNES):
    E.append((
        ligne, ligne, f"\\[ {lettre} \\]", "moyenne",
        JUSTIF,
        f"Domaine {lettre} — {titre}. Hypothèse A→J validée par l'auteur le 2026-10-18 ; "
        f"le résidu du bloc est vide, la lettre est donc restituée nue comme dans \\[ IJ \\].",
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
