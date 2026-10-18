# A2 — INVENTAIRE STRUCTUREL DU DÉPÔT DE CONNAISSANCES (Phase 1, étape 1)

**Date :** 2026-10-17 — **Régénéré et validé le :** 2026-10-18
**Source :** clone local en lecture seule de `Stane316/my-own-connaissance` (commit `f0f5e2d`)
**Outil :** `tools/extract_structure.py` (déterministe, sans réseau, aucune écriture dans la source)
**Données brutes :** `annexes/A2-inventaire-structurel.csv`

> **Note de traçabilité :** ce livrable a d'abord été produit hors dépôt, puis perdu lors d'une réinitialisation du sandbox (2026-10-18). Il a été régénéré à l'identique — les totaux sont strictement les mêmes, ce qui valide la reproductibilité de la méthode. Il est désormais versionné : **les livrables validés ne doivent plus rester hors dépôt.**

---

## 1. Méthode

Comptages automatiques par document : lignes, octets, titres Markdown, équations LaTeX (`\[…\]`, `\(…\)`), blocs de code délimités par ``` , lignes de tableau, items de liste, et occurrences de 18 marqueurs de rigueur (hypothèse, limite, condition, convergence, stabilité, erreur, validation, test, exemple, algorithme, complexité, théorème, démonstration, implémentation, contre-exemple, précision, approximation, références).

**Ce que ces comptages ne prouvent pas :** un mot peut être cité sans être expliqué, une équation peut être présente mais fausse. Ils servent à **cibler** la lecture, jamais à la remplacer.

## 2. Totaux (29 documents)

| Métrique | Total |
|---|---:|
| Lignes / octets | 80 330 / 1 912 005 |
| Titres Markdown | 7 240 |
| Équations display `\[…\]` | **2 354** |
| Équations inline `\(…\)` | 5 |
| **Blocs de code ``` ** | **0** |
| Lignes de tableau | 781 |
| Items de liste | 15 388 |
| « algorithme » | 475 |
| « exemple » | 829 |
| « erreur » | 417 |
| « test » | 447 |
| « validation » | 160 |
| « hypothèse » | 211 |
| « limite » | 222 |
| « théorème » | 207 |
| « démonstration/preuve » | 227 |
| « implémentation » | 223 |
| « contre-exemple » | 20 |
| « approximation » | 137 |
| « précision » | 105 |

## 3. Constat majeur (vérifié)

**Zéro bloc de code, zéro équation inline significative, dans 80 330 lignes.** Le corpus est très riche en énoncés (2 354 équations, 7 240 titres) et dense en vocabulaire de rigueur — mais **dépourvu de tout artefact exécutable** : pas un bloc de code, pas de pseudocode formaté, pas de jeu de données, pas de script, pas de bibliographie structurée.

Conséquence directe : la chaîne « modèle → équations → algorithme → **implémentation → tests** » est documentée jusqu'à l'algorithme, jamais au-delà. C'est le chaînon que le produit devra construire — une lacune pour le dépôt de connaissances, un différenciateur pour le produit.

## 4. Répartition par domaine

| Document | Lignes | Titres | Éq. display | Hypoth. | Limites | Valid. | Err. | Algo. | Réf. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A — Logique et fondements | 119 | **0** | 0 | 22 | 24 | 8 | 8 | 34 | 7 |
| B — Théorie des nombres | 103 | **0** | 0 | 7 | 22 | 2 | 3 | 63 | 7 |
| C — Algèbre linéaire | 123 | **0** | 0 | 2 | 0 | 1 | 16 | 12 | 2 |
| D — Géométrie computationnelle | 133 | **0** | 0 | 5 | 4 | 1 | 5 | 34 | 2 |
| E — Graphes | 2 858 | 295 | 11 | 2 | 4 | 4 | 8 | 25 | 1 |
| F — Combinatoire | 2 945 | 347 | 118 | 1 | 2 | 0 | 10 | 16 | 0 |
| G — Probabilités | 3 072 | 347 | 236 | 10 | 7 | 0 | 7 | 12 | 0 |
| H — Statistiques | 2 662 | 316 | 125 | 29 | 0 | 13 | 25 | 2 | 1 |
| I — Calcul différentiel | 3 177 | 285 | **318** | 5 | 10 | 1 | 17 | 4 | 0 |
| J — Optimisation | 3 542 | 359 | **333** | 3 | 1 | 8 | 14 | 25 | 1 |
| K — Fractales, chaos, dyn. | 4 316 | 340 | 64 | **0** | 6 | 1 | 11 | 11 | **11** |
| L — Analyse numérique | 2 356 | 257 | 178 | 0 | 4 | 4 | **46** | 8 | 2 |
| M — Théorie de l'information | 4 276 | 308 | 251 | 9 | 19 | 4 | 22 | 10 | 10 |
| N — Transformées | 3 947 | 290 | 258 | 4 | 4 | 4 | 7 | 7 | 1 |
| O — Complexité | 3 618 | 275 | 248 | 2 | 4 | 0 | 15 | **69** | 1 |
| P — Cryptographie | 4 120 | 319 | 66 | 10 | 1 | 2 | 27 | 28 | 2 |
| Q — Logique, automates | 3 142 | 255 | 79 | 0 | 5 | **23** | 8 | 6 | 1 |
| R — Algèbre abstraite | 2 706 | 269 | 6 | 6 | 13 | 2 | 17 | 50 | 2 |
| S — Topologie | 2 524 | 272 | 8 | 17 | 12 | 7 | 6 | 20 | 4 |
| U — Logique floue | 2 394 | 197 | 23 | 1 | 21 | 9 | 12 | 2 | 8 |
| README (maître) | 1 122 | 130 | 0 | 17 | 27 | 6 | 5 | 27 | 5 |

## 5. Lectures provisoires (à confirmer par lecture réelle)

1. **A, B, C, D cumulent deux handicaps** : titres absents **et** très peu de lignes (103 à 133) pour 58 à 82 Kio — l'aplatissement est massif, la navigation humaine probablement très dégradée.
2. **I, J, N, G, M, O** sont les plus « équationnels » (248 à 333 équations) : candidats naturels pour des composants à modèle explicitable.
3. **Alerte sur K** (fractales, chaos, systèmes dynamiques) — le domaine le plus stratégique pour la première famille de composants : 64 équations seulement, **0 occurrence de « hypothèse », 1 de « validation »**. À vérifier en priorité en Phase 1.
4. **L** est le plus dense en vocabulaire d'erreur (46) : référence naturelle pour les critères de validation numérique.
5. **Les 8 documents de littératie technique (01–08)** ne contiennent presque aucune équation (0 à 20) : ils devront être audités sur d'autres critères.

## 6. Limites

Comptage lexical, pas analyse sémantique. Le comptage des blocs de code repère les délimiteurs ``` : un pseudocode non délimité n'est pas compté. Le contenu des documents de littératie technique n'est pas évalué à ce stade.
