#!/usr/bin/env python3
"""Lot A-6 : emplacements vides restants et bilan du chantier A.

Deux restitutions, une recommandation non appliquee, et un etat des lieux
complet de ce qui reste — volontairement — en l'etat. Voir `domaine-A-lot6.md`.

Les deux restitutions sont des reconsiderations de decisions anterieures,
rendues possibles par deux faits nouveaux :

  1. Le §7.3 « Récursion informatique » a un emplacement « Exemple conceptuel : »
     VIDE, et ce qui le suit — « un ou plusieurs cas de base ; un appel recursif
     qui progresse vers un cas de base » — decrit exactement les deux branches
     du code factorielle. Or ce code git au §8, section des ensembles et de la
     denominabilite, dont le tas contenait deja, de facon demontree, la phrase
     de l'invariant du §7.4. Le tas du §8 etait donc un debordement de la fin
     du §7. A3-08/09 l'avait traite comme un reformatage sur place.

  2. Le §13.3 a deux emplacements vides, et `Utilisateur = (nom, email, age)`
     — un type PRODUIT — git en tas dans cette meme section.

Usage
-----
    python3 tools/restauration/build_lot_A_6.py
"""

import sys

from lot_commun import H, M, I, appliquer, entre, _lire

# Le code factorielle est RELU, pas recopie.
_DEB8 = "8. ENSEMBLES, FONCTIONS ET DÉNOMBRABILITÉ"
_FIN8 = "8.1 Ensembles et cardinalité"
_t = _lire()
_i, _j = _t.find(_DEB8), _t.find(_FIN8)
CODE = _t[_i + len(_DEB8):_j].strip("\n")

EDITS = [
    # ================================================ §7.3 <- §8 (A6-01)
    ("A6-01",
     *entre("7.3 Récursion informatique  Une fonction récursive se définit en "
            "faisant appel à elle-même, directement ou indirectement.  "
            "Exemple conceptuel :",
            "Deux éléments indispensables", "\n\n" + CODE + "\n\n"),
     H,
     "Le §7.3 est « Récursion informatique » et son emplacement « Exemple "
     "conceptuel : » est vide. Ce qui le suit nomme les deux elements "
     "indispensables — « un ou plusieurs cas de base ; un appel recursif qui "
     "progresse vers un cas de base » — et ce sont EXACTEMENT les deux "
     "branches du code : `if n = 0: return 1` (le cas de base) et "
     "`return n × factorielle(n - 1)` (l'appel recursif qui progresse). Le "
     "tas du §8 contenait par ailleurs, de facon demontree au lot 5, la phrase "
     "de l'invariant du §7.4 : ce tas etait donc un debordement de la FIN du "
     "§7. Le code en faisait partie.",
     "RECONSIDERATION DE A3-08/09, qui traitait ce code comme un simple "
     "reformatage sur place. C'etait la conclusion raisonnable tant que "
     "l'emplacement vide du §7.3 n'avait pas ete repere. Le §8 devient, apres "
     "ce deplacement, une section qui ne traite plus que de son sujet. "
     "REVERSIBLE : si le porteur prefere l'ancien montage, cette edition et "
     "A6-01b sont a annuler ensemble."),

    ("A6-01b",
     *entre(_DEB8, _FIN8, "\n\n"),
     H,
     "Retrait du bloc de code, recase au §7.3 (A6-01). Le §8 retrouve son "
     "intitule seul, suivi du §8.1.",
     None),

    # ================================================== §13.3 (A6-02)
    ("A6-02",
     *entre("13.3 Types algébriques et types somme/produit  Type produit  "
            "Regroupe plusieurs composants.  Exemple conceptuel :",
            "Type somme  Représente", " `Utilisateur = (nom, email, age)`  "),
     M,
     "`Utilisateur = (nom, email, age)` est un type PRODUIT : un enregistrement "
     "de plusieurs composantes. L'emplacement vide qui suit « Type produit — "
     "Regroupe plusieurs composants. » est l'exemple du type produit. Le "
     "fragment git en tas dans cette meme section : il est donc deplace, non "
     "invente.",
     "RESERVE MAINTE-NUE : la pile ou git le fragment se trouve APRES la "
     "description du type SOMME, ce quiDesignerait plutot le second "
     "emplacement. Mais la position d'une pile n'est pas fiable dans ce "
     "document — fait etabli des lots precedents —, et le CONTENU, lui, "
     "designer sans ambiguite le type produit. Le second emplacement reste "
     "vide : rien ne permet d'y porter quoi que ce soit sans supposer. "
     "REVERSIBLE : si le porteur juge que le fragment va au second "
     "emplacement, cette edition et A6-02b sont a permuter."),

    ("A6-02b",
     *entre("Représente une valeur choisie parmi plusieurs variantes.",
            "Exemple conceptuel :", "  "),
     H,
     "Retrait du fragment, recase en A6-02. Le second emplacement « Exemple "
     "conceptuel : » est CONSERVE — il reste vide, faute de contenu attesté.",
     None),
]


# Correction d'un lot anterieur. `build_lot_A_5.py` (A5-02b) etait montee
# avec `entre()`, qui CONSERVE son marqueur amont : la note du §6.7 s'est
# retrouvee en double, l'ancienne (avec `a` et `¬P(a)`) restant collee a la
# nouvelle. Le bon montage etait de prendre comme marqueur amont la phrase
# qui precede la note, et non la note elle-meme.
CORRECTIONS = [
    ("A5-02c (correction)",
     "*Fragments non rattachés, conservés faute de destination établie :* "
     "`∀x, P(x)` · `a` · `¬P(a)`"
     "*Fragment non rattaché, conservé faute de destination établie :* "
     "`∀x, P(x)`",
     "*Fragment non rattaché, conservé faute de destination établie :* "
     "`∀x, P(x)`",
     H,
     "La note du §6.7 etait en double depuis le lot 5 : l'ancienne mentionnait "
     "encore `a` et `¬P(a)`, recases au §6.5. Seul `∀x, P(x)` reste sans "
     "destination, la note ne doit plus citer que lui. Aucun token n'est "
     "perdu : les deux autres sont bien recases, pas supprimes.",
     None),
]


def main():
    return appliquer(
        EDITS + CORRECTIONS,
        journal="docs/restauration/propositions/domaine-A-lot6.journal.json",
    )


if __name__ == "__main__":
    sys.exit(main())
