#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lot B-1 — Domaine B (Theorie des nombres).

Table du §3, proprietes du §4.1, exemples des §4.3 et §4.4, propriete du §5.1,
et les trois glyphes `≠` perdus.

Ce que le lot fait
------------------
Le §3 est un tableau a trois colonnes dont la troisieme — « Formule ou
caracterisation » — est vide pour neuf lignes sur quatorze. Le §4.2 porte un
tas de formules. **Ce tas suit l'ordre du tableau**, y compris les slots de
variables de la premiere colonne : la correspondance est donc etablie par
l'ordre ET par le compte, pas par une hypothese de lecture.

Deux lignes du tableau — 9 (exponentiation modulaire) et 12 (ordre d'un
element) — ne sont PAS traitees : le segment de tas correspondant est
lacunaire et son affectation ne serait pas demonstrable. Elles restent vides
et les tokens correspondants sont conserves en note.

Le mot cle de ce lot : les piles de B debordent VERS L'AVANT. Chaque tas
recoit les formules des sections qui le precedent, et non de celle qui le
porte. C'est l'inverse du §8 de A.

Regles respectees
-----------------
1. Unicite de chaque sous-chaine source.
2. Non-perte : tout token consomme est recase ; tout token non rattache est
   conserve en note, jamais supprime.
3. Verifiabilite : le journal porte ancien, nouveau, confiance, justification.

Usage
-----
    python3 lot_commun.py build_lot_B_1.py     # diagnostic, n'ecrit rien
    python3 tools/restauration/build_lot_B_1.py   # applique et journalise
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lot_commun import H, M, entre, retirer, appliquer, FICHIER_B

# Le lot travaille sur le document B, pas sur A.
CIBLE = FICHIER_B

# ---------------------------------------------------------------------------
# B1-01 — Le tableau du §3 rendu en Markdown, colonne 3 comblee
# ---------------------------------------------------------------------------
# Le tas du §4.2, dans l'ordre :
#   a b | b = ak, k∈Z | a = bq+r, 0≤r<b | gcd(a,b) | a b
#   | ax+by=gcd(a,b) | a n | gcd(a,n)=1 | n | a≡b (mod n) | n | ax≡1 (mod n)
#   | p p
# soit, ligne a ligne : les slots de variables de la colonne 1, puis la
# formule de la colonne 3. Huit lignes, dans l'ordre, sans reste.
TABLE_3 = """| Si tu rencontres… | Pensé à… | Formule ou caractérisation |
|---|---|---|
| « `a` divise `b` », avec | Divisibilité | `b = ak`, `k ∈ Z` |
| « quotient et reste » | Division euclidienne | `a = bq + r`, `0 ≤ r < b` |
| « plus grand diviseur commun » | PGCD | `gcd(a, b)` |
| « combinaison entière de `a` et `b` » | Bézout | `ax + by = gcd(a, b)` |
| « `a` et `n` sont premiers entre eux » | Coprimalité | `gcd(a, n) = 1` |
| « même reste modulo `n` » | Congruence | `a ≡ b (mod n)` |
| « inverse modulo `n` » | Inverse modulaire | `ax ≡ 1 (mod n)` |
| « `p` est premier » | Primalité | Ses seuls diviseurs positifs sont 1 et `p` |
| « puissance modulo `n` » | Exponentiation modulaire | |
| « exposant réduit modulo… » | Fermat ou Euler | Conditions à vérifier selon le théorème |
| « système de congruences » | Restes chinois | Compatibilité et reconstruction |
| « ordre d’un élément » | Théorie des groupes | Plus petit `k` tel que |
| « résoudre `gˣ ≡ h (mod p)` » | Logarithme discret | Recherche d’un exposant |
| « produit de facteurs premiers » | Factorisation | `n = ∏ pᵢ^{eᵢ}` |

*Fragments non rattachés, conservés faute de destination établie :* `n` · `a` · `mod k` · `n` · `k > 0` · `a = k` · `e`
"""

# ---------------------------------------------------------------------------
# B1-02 — Les quatre proprietes de la divisibilite (§4.1)
# ---------------------------------------------------------------------------
# Le tas du §4.2 se poursuit, apres les huit lignes du tableau et le segment
# lacunaire, par quatre groupes :
#   a∣b  b∣c  a∣c                      -> propriete 1
#   a∣b  a∣c  a∣(ub+vc)  u, v          -> propriete 2
#   a∣b  a∣bc  c                       -> propriete 3
#   a∣b  b = <U+E020> 0  ∣a∣ ≤ ∣b∣     -> propriete 4
# Le §4.1 presente exactement quatre proprietes, avec le meme nombre de slots
# et dans le meme ordre. La troisieme se lit « Si [a∣b], alors [a∣bc] pour tout
# entier [c] » — propriete usuelle, et la seule compatible avec un seul slot
# de condition.
PROPRIETES_41 = """Pour des entiers adaptés aux hypothèses :

1. Si `a ∣ b` et `b ∣ c`, alors `a ∣ c`.
2. Si `a ∣ b` et `a ∣ c`, alors `a ∣ (ub + vc)` pour tous entiers `u, v`.
3. Si `a ∣ b`, alors `a ∣ bc` pour tout entier `c`.
4. Si `a ∣ b` et `b ≠ 0`, alors `∣a∣ ≤ ∣b∣`.

"""

# ---------------------------------------------------------------------------
# B1-03 — Le tas du §4.2 : on retire les tokens consommes
# ---------------------------------------------------------------------------
# Reste le segment lacunaire des lignes 9 et 12 du tableau, qui n'a pas de
# destination demonstrable. Il est conserve en note sur place : un token sans
# destination etablie ne sort jamais du document.
NOTE_42 = ("*Fragments non rattachés, conservés faute de destination établie :* "
           "`n` · `a` · `mod k` · `n` · `k > 0` · `a = k` · `e`")

# ---------------------------------------------------------------------------
# B1-04 — L'exemple du §4.3
# ---------------------------------------------------------------------------
# Le tas local est « 10 k  d = gcd(a, b)  gcd(18, 30) = 6 ». Le slot
# « Exemple : » est suivi de trois groupes ; seul le dernier est l'exemple.
# Les deux premiers n'ont pas de destination etablie.
EXEMPLE_43 = (
    "Exemple : `gcd(18, 30) = 6`  "
    "*Fragments non rattachés, conservés faute de destination établie :* "
    "`10 k` · `d = gcd(a, b)`"
)

# ---------------------------------------------------------------------------
# B1-06 — La propriete du §5.1 et le nettoyage de son tas
# ---------------------------------------------------------------------------
# Le tas du §5.1 porte, dans cet ordre :
#   ppcm(a, b) | a, b = <U+E020> 0 | gcd(a, b) ppcm(a, b) = ∣ab∣   -> §4.4
#   gcd(a, b) = gcd(b, a mod b) | b = <U+E020> 0                    -> §5.1
# Soit la formule de la section PRECEDENTE d'abord, puis celle de la section
# courante. C'est le meme debordement vers l'avant.
EUCLIDE_51 = (
    "Il repose sur la propriété : `gcd(a, b) = gcd(b, a mod b)` "
    "pour `b ≠ 0`, avec une convention de reste cohérente.\n\n"
    "*Fragment non rattaché, conservé faute de destination établie :* `n`"
)

EDITS = [

    # ------------------------------------------------------------- §3
    ("B1-01",
     *retirer("Si tu rencontres…", "  4. Divisibilité",
              TABLE_3 + "\n", fichier=CIBLE),
     H,
     "Le §3 est un tableau a trois colonnes dont la troisieme est vide pour "
     "neuf lignes sur quatorze. Le tas du §4.2 suit l'ordre du tableau, y "
     "compris les slots de variables de la premiere colonne : `a b` ouvre le "
     "tas et correspond a « [a] divise [b] », `b = ak, k ∈ Z` vient ensuite et "
     "correspond a la troisieme colonne de cette meme ligne. La suite est "
     "exactement celle des lignes du tableau. HUIT lignes sont ainsi pourvues, "
     "sans reste et sans inversion. Les lignes 9 et 12 restent vides : le "
     "segment de tas correspondant est lacunaire. La ligne 14 recoit "
     "`n = ∏ pᵢ^{eᵢ}`, dont les EXPOSANTS sont re-composes — les exposants "
     "sont detruits dans tout le document (0 occurrence de ² ³ ⁿ).",
     "Confiance haute pour les lignes 1 a 8 et la ligne 13. Confiance "
     "MOYENNE pour la ligne 14 (exposants re-composes) et pour la ligne 13 "
     "dont le declencheur « resoudre [ ] » est comble par `gˣ ≡ h (mod p)`, "
     "ver-batim dans le tas mais dont le rattachement a cette ligne plutot "
     "qu'au §16 (logarithme discret) reste une attribution par le contenu."),

    # ------------------------------------------------------------- §4.1
    ("B1-02",
     *retirer("Pour des entiers adaptés aux hypothèses :",
              "Ces propriétés servent", PROPRIETES_41, fichier=CIBLE),
     H,
     "Le §4.1 presente quatre proprietes, chacune avec ses slots vides. Le tas "
     "du §4.2 se poursuit, apres les huit lignes du tableau, par quatre groupes "
     "de tokens qui leur correspondent exactement, dans l'ordre et sans reste : "
     "transitivite, combinaison lineaire, `a ∣ b ⟹ a ∣ bc`, et "
     "`a ∣ b, b ≠ 0 ⟹ ∣a∣ ≤ ∣b∣`. La troisieme propriete se lit « Si [a∣b], alors "
     "[a∣bc] pour tout entier [c] » : c'est la seule lecture compatible avec un "
     "seul slot de condition, et c'est une propriete usuelle.",
     "Confiance haute : ordre, compte et contenu concordent. Le glyphe "
     "U+E020 de la quatrieme propriete est restitue en `≠` : le contexte "
     "« b =  0 » ne laisse aucune autre lecture — c'est la reparation d'une "
     "perte d'encodage, pas une invention."),

    # ------------------------------------------------------------- §4.2
    ("B1-03",
     *retirer("4.2 Critères de divisibilité usuels",
              "\n\nCes critères permettent de décider",
              "4.2 Critères de divisibilité usuels\n\n" + NOTE_42,
              fichier=CIBLE),
     H,
     "Retrait des tokens reclames par B1-01 et B1-02. Sont conserves en note "
     "les sept tokens du segment lacunaire, qui n'ont pas de destination "
     "demonstrable. Aucun token ne sort du document.",
     "Confiance haute : c'est la contrepartie mecanique des deux editions "
     "precedentes. Le §4.2 retrouve son intitule et la phrase annonçant la "
     "table des criteres de divisibilite, qui est intacte."),

    # ------------------------------------------------------------- §4.3
    ("B1-04",
     *retirer("Exemple :  10 k", "\n\nÀ quoi sert-il ?",
              EXEMPLE_43, fichier=CIBLE),
     H,
     "Le slot « Exemple : » du §4.3 est suivi de trois groupes de tokens. Le "
     "dernier, `gcd(18, 30) = 6`, est l'exemple annonce : il est immediatement "
     "apres le slot et il est le seul a etre une egalite entre nombres. Les "
     "deux premiers groupes, `10 k` et `d = gcd(a, b)`, n'ont pas de "
     "destination etablie et sont conserves en note.",
     "Confiance haute pour l'exemple, qui est verbatim et adjacent. Les deux "
     "fragments laisses en note sont signales, pas supprimes."),

    # ------------------------------------------------------------- §4.4
    ("B1-05",
     *entre("Relation importante, pour", "Cette relation permet",
            " `a, b ≠ 0` : `gcd(a, b) × ppcm(a, b) = ∣ab∣`  ", fichier=CIBLE),
     H,
     "Le §4.4 annonce une « relation importante » dont la formule est absente. "
     "Elle se trouve en tete du tas du §5.1 : `ppcm( a , b )`, `a , b = <U+E020> 0`, "
     "`gcd( a , b ) ppcm( a , b ) = ∣ ab ∣`. Les trois groupes sont la, dans "
     "l'ordre, et ils reconstituent la relation usuelle avec sa condition de "
     "validite. Le glyphe U+E020 est restitue en `≠` : « a, b =  0 » ne se lit "
     "pas autrement.",
     "Confiance haute. L'identite `pgcd × ppcm = ∣ab∣` est un resultat standard, "
     "et surtout les tokens sont presents et dans l'ordre. Le fait qu'ils "
     "resident dans le tas du §5.1 et non du §4.4 est le debordement vers "
     "l'avant decrit en tete de lot."),

    # ------------------------------------------------------------- §5.1
    ("B1-06",
     *retirer("Il repose sur la propriété :", "\n\nPrincipe  On remplace",
              EUCLIDE_51, fichier=CIBLE),
     H,
     "Le §5.1 annonce « la propriete :  pour  , avec une convention de reste "
     "coherente » — deux slots. Son tas porte d'abord les tokens du §4.4 "
     "(deja reclames par B1-05), puis `gcd( a , b ) = gcd( b , a   mod   b )` "
     "et `b = <U+E020> 0`, qui sont precisement les deux slots. Le `n` restant "
     "n'a pas de destination etablie et demeure en note.",
     "Confiance haute : l'enonce `gcd(a, b) = gcd(b, a mod b)` pour `b ≠ 0` est "
     "la propriete fondatrice de l'algorithme d'Euclide, les tokens sont la et "
     "dans l'ordre. Le glyphe U+E020 est restitue en `≠` par son contexte."),
]


def main():
    return appliquer(
        EDITS,
        journal="docs/restauration/propositions/domaine-B-lot1.journal.json",
        fichier=CIBLE,
    )


if __name__ == "__main__":
    sys.exit(main())
