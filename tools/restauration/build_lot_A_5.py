#!/usr/bin/env python3
"""Lot A-5 : points laisses ouverts par les lots 1 a 4.

Six points ont ete investigates. Trois donnent lieu a une restitution ;
trois ne sont PAS appliques, et c'est la conclusion :

  - A5-05 (§13.3) : deux emplacements vides, affectation non tranchable.
  - A5-06 (§17.5) : le contenu plausible n'est pas deplace ; le deplacer
    serait une REDACTION, pas une restauration.
  - A5-07 (§9.3)  : le symbole relationnel est perdu ; retablir `x ∉ x`
    serait une INVENTION.

Voir `domaine-A-lot5.md` pour l'argumentation, et notamment la grille
empirique qui distingue un emplacement vide d'un libelle suivi de son
contenu — grille sans laquelle le §6.5 aurait ete mal compte.

Usage
-----
    python3 tools/restauration/build_lot_A_5.py
"""

import sys

from lot_commun import H, M, I, appliquer, entre, retirer

EDITS = [
    # ------------------------------------------------------------- §6.5
    ("A5-02",
     *entre("il suffit de trouver un", "tel que :", " `a` "),
     M,
     "Emplacement vide : trois espaces en pleine phrase, signature retenue par "
     "la grille. Le token `a` etait conserve comme non rattache au §6.7, "
     "section des regles d'inference ou il n'a aucune place. Le §6.5 est la "
     "section du contre-exemple, et sa phrase en decrit le schema.",
     "Ce lot ne case que DEUX tokens pour DEUX emplacements. Le troisieme "
     "orphelin, `∀x, P(x)`, n'a pas d'emplacement : il demeure conserve et "
     "signale. On ne le case pas en force."),

    ("A5-03",
     *entre("tel que :", "Réflexe :", " `¬P(a)`  "),
     M,
     "Emplacement vide : deux espaces suivis d'un autre libelle, meme signa- "
     "ture que le §10.1. La source designe elle-meme le contenu : « tel que : » "
     "appelle une propriete niee. `¬P(a)` etait orphelin au §6.7.",
     None),

    ("A5-02b",
     *entre("*Fragments non rattachés, conservés faute de destination établie :*"
            " `∀x, P(x)` · `a` · `¬P(a)`", "La distinction devient importante",
            "*Fragment non rattaché, conservé faute de destination établie :* "
            "`∀x, P(x)`  "),
     H,
     "Mise a jour de la note du §6.7 : `a` et `¬P(a)` sont desormais recases "
     "au §6.5, il n'y a plus lieu de les signaler. `∀x, P(x)` reste sans "
     "destination et reste signale. Aucun token n'est supprime.",
     None),

    # ------------------------------------------------------------- §7.4
    ("A5-01",
     *entre("Dans une recherche du maximum d’un tableau, l’invariant peut "
            "affirmer :", "Cet invariant permet de raisonner",
            " « Après avoir examiné les `i` premiers éléments, la variable max "
            "contient le maximum de ces éléments. »  "),
     H,
     "L'emplacement du §7.4 nomme exactement le contenu : une recherche du "
     "maximum d'un tableau, et un invariant. La phrase est verbatim dans la "
     "source, en tete du §8 — RIEN N'EST REDIGE. Le `i`, separe en fin de "
     "pile, revient a sa place dans « les _ premiers elements ». `max` etait "
     "deja en place et n'est pas touche.",
     "Le §7.4 relevant du lot 2, deja livre, ce point avait ete renvoye ici : "
     "on ne redefait pas un diff deja livre pour y ajouter une restitution "
     "trouvee apres coup. Ce lot la reprend, et le diff est incremental."),

    ("A5-01b",
     # Le marqueur amont doit SURVIVRE : c'est la fin du bloc de code, qui
     # reste au §8. Seule la phrase disparait, avec la pile. `entre()` est donc
     # le bon outil — a condition de prendre un marqueur amont qui ne fasse pas
     # partie de ce qu'on supprime.
     #
     # Deux erreurs ont ete commises ici avant d'y arriver, et valent d'etre
     # consignees : (1) prendre `Après avoir examiné` comme marqueur amont, que
     # `entre()` conserve — la phrase restait en tete du §8 ; (2) passer a
     # `retirer()`, qui supprime AUSSI le marqueur amont — la fin du bloc de
     # code partait avec. La zone a du etrereparee a la main. Le montage
     # ci-dessous est le bon.
     *entre("return n × factorielle(n - 1)\n```\n\n",
            "8.1 Ensembles et cardinalité", ""),
     H,
     "Retrait de la phrase egarée, recasee au §7.4 (A5-01). Le §8 est "
     "« ENSEMBLES, FONCTIONS ET DENOMBRABILITE » : une phrase sur le maximum "
     "d'un tableau n'y a rien a faire. Le bloc de code factorielle, lui, reste "
     "en place : il est bien a sa section.",
     "DEUX ERREURS COMMISES AVANT D'Y ARRIVER, consignees parce qu'elles "
     "revelent une limite de l'outillage. (1) Premier montage : marqueur amont "
     "« Après avoir examiné ». Or `entre()` CONSERVE ses deux marqueurs — la "
     "phrase restait donc en tete du §8, accolee au titre de section. (2) "
     "Second montage : passage a `retirer()`, censee supprimer l'intervalle. "
     "Elle supprime AUSSI le marqueur amont, qui etait la fin du bloc de code : "
     "le bloc a ete deregle. La zone a etereparee a la main, puis le constructeur "
     "a ete REJOUE DEBOUT depuis la sauvegarde pre-lot-5 et compare octet par "
     "octet a l'etatrepare : identiques. Le montage retenu est `entre()` avec un "
     "marqueur amont qui doit survivre."),

    # ------------------------------------------------------------ §14.2
    ("A5-04",
     *entre("d’un langage de programmation.  Exemple conceptuel :",
            "Une grammaire réelle doit aussi",
            "\n\nExpression → Expression + Terme\nExpression → Terme\n"
            "Terme → nombre\n\n"),
     H,
     "Trois raisons convergent. (1) L'emplacement est vide : « Exemple "
     "conceptuel : » est suivi d'une MISE EN GARDE (« Une grammaire reelle "
     "doit aussi preciser… »), non d'un exemple. (2) Le contenu est une "
     "grammaire : trois productions, avec terminaux et non terminaux — c'est "
     "la definition de l'exemple que le §14.2 appelle. (3) Il git dans la "
     "section des AUTOMATES FINIS, ou il coupe le paragraphe avant "
     "« Comment les reconnaitre ? ».",
     "La mise en forme une-production-par-ligne est PROPOSEE : le fragment est "
     "a plat sur une ligne, et ce rendu, usuel pour une grammaire, n'est pas "
     "atteste."),

    ("A5-04b",
     *entre("Ils servent notamment à reconnaître des langages réguliers.",
            "Comment les reconnaître ?", "\n\n"),
     H,
     "Retrait des productions grammaticales, recasees au §14.2 (A5-04). Elles "
     "coupaient le paragraphe des automates finis ; le retrait le ressoude.",
     None),
]


def main():
    return appliquer(
        EDITS,
        journal="docs/restauration/propositions/domaine-A-lot5.journal.json",
    )


if __name__ == "__main__":
    sys.exit(main())
