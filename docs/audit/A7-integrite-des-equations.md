# A7 — INTÉGRITÉ DES ÉQUATIONS DU DÉPÔT DE CONNAISSANCES

**Date :** 2026-10-18 — **Statut :** **résultat vérifié**, à portée structurante pour la Phase 1
**Source :** clone en lecture seule de `Stane316/my-own-connaissance` (commit `f0f5e2d`)
**Outils :** `tools/check_equations.py`, `tools/check_equations2.py` (déterministes, sans réseau)
**Données brutes :** `annexes/A7-integrite-equations.csv`

---

## 1. Résumé

Une analyse systématique des 2 354 équations LaTeX en mode display (`\[…\]`) du corpus montre que **724 d'entre elles, soit 30,8 %, sont structurellement incomplètes**. Les équations n'ont pas été mal rédigées : elles ont été **tronquées lors d'un export**, les commandes LaTeX (`\frac`, `\lim`, `\sum`, `\log`, `\lambda`, `\sigma`…) ayant été supprimées en emportant leur contenu.

Quatre documents (A, B, C, D) ne contiennent **plus aucune équation display** : la perte y est totale, et cohérente avec la perte simultanée de leur arborescence de titres.

**Conséquence directe pour le projet :** on ne peut pas extraire mécaniquement un catalogue d'équations fiable de ce corpus. Les équations devront être **réécrites et validées** une par une pour chaque composant, à partir de sources de référence, et non recopiées depuis le dépôt de connaissances.

## 2. Méthode

Détection par heuristiques **séparées et comptées séparément** (pas de score composite), afin qu'un résultat discutable ne contamine pas les autres :

| Heuristique | Ce qu'elle détecte | Occurrences |
|---|---|---:|
| `vide_ou_blanc` | équation réduite à du vide | **365** |
| `fragment_commande` | restes d'une commande supprimée (`\_`, `_{x}_`, `\(`) | **205** |
| `parentheses_vides` | `()` laissé par un argument supprimé | **73** |
| `finit_par_egal` | membre droit disparu | **68** |
| `commence_par_egal` | membre gauche disparu | **42** |
| `indice_orphelin` | indice sans base (`_ {`) | **8** |
| **Union (« structurellement incomplètes »)** | | **724 / 2 354 (30,8 %)** |
| `courte_ambiguë` (hors décompte) | 0 < longueur < 6 caractères | 834 |

**Ce que la méthode ne fait pas :** elle ne juge pas de l'exactitude mathématique des équations complètes, et elle ne prétend pas détecter une équation complète mais fausse. La catégorie « courte ambiguë » est **volontairement exclue** du décompte : elle contient autant d'expressions légitimes (`x(t)`, `X(f)`) que de troncatures.

## 3. Preuves directes (extraits de la source)

**Système de Lorenz** — `DOCUMENT K`, lignes 1142-1146 :

```text
\[ =(y-x) \]
\[ =x(-z)-y \]
\[ =xy-z \]

où :
- () ;
```

Les trois équations ont perdu leur membre gauche (`dx/dt`, `dy/dt`, `dz/dt`) et leurs paramètres (σ, ρ, β) ; la liste des paramètres qui suit est vide.

**Dimension de similarité** — `DOCUMENT K`, lignes 826-841 :

```text
Si une structure est composée de (N) copies réduites d'un facteur (r), alors :
\[ N=r^{-D} \]
d'où :
\[ D= \]
```

La formule `D = log N / log(1/r)` a disparu — y compris dans l'exemple du triangle de Sierpiński, où `D=` reste vide alors que `N=3` et `r=1/2` sont énoncés juste au-dessus.

**Exposant de Lyapunov** — `DOCUMENT K`, ligne 1126 :

```text
\[ _{n}_ {i=0}^{n-1} |f'(x_i)| \]
```

Reste de `λ = lim (1/n) Σ ln|f'(x_i)|` après suppression de `\lambda`, `\lim`, `\frac` et `\sum`.

## 4. Répartition par document

| Document | Éq. display | Incomplètes | % |
|---|---:|---:|---:|
| `Ai Technical Litteracy` 02 — UI/UX | 20 | 20 | **100 %** |
| H — Statistiques | 125 | 64 | 51,2 % |
| J — Optimisation | 333 | 166 | 49,8 % |
| N — Transformées | 258 | 104 | 40,3 % |
| L — Analyse numérique | 178 | 61 | 34,3 % |
| I — Calcul différentiel | 318 | 109 | 34,3 % |
| **K — Fractales, chaos, systèmes dynamiques** | **64** | **18** | **28,1 %** |
| G — Probabilités | 236 | 60 | 25,4 % |
| M — Théorie de l'information | 251 | 59 | 23,5 % |
| O — Complexité | 248 | 38 | 15,3 % |
| Q — Logique, automates | 79 | 11 | 13,9 % |
| F — Combinatoire | 118 | 12 | 10,2 % |
| P — Cryptographie | 66 | 2 | 3,0 % |
| E — Graphes · R — Algèbre abstraite · S — Topologie · U — Logique floue | 48 | 48 | **100 %** |
| **A (maître) · B · C · D** | **0** | — | **équations entièrement absentes** |

Les quatre derniers documents de mathématiques (E, R, S, U) ont un taux de 100 % sur un petit nombre d'équations (6 à 11) : dans leur cas, la quasi-totalité du formalisme a été perdue, et non une fraction.

## 5. Conséquences pour le projet

1. **L'index « notion → équations » ne peut pas être généré automatiquement.** Il devra être construit notion par notion, avec des équations réécrites et sourcées.
2. **Le critère d'acceptation « exactitude des équations » ne peut pas s'appuyer sur le corpus existant.** Chaque équation retenue pour un composant devra être validée contre une référence externe (ouvrage, article, dépôt de référence), et la référence citée.
3. **La correction du corpus est un chantier distinct**, qui ne doit pas être mené en douce pendant la Phase 1 : elle touche aux documents de l'utilisateur et suppose des choix éditoriaux (réécrire les équations ? restaurer depuis une source antérieure ? marquer les trous ?).
4. **Le produit garde sa valeur malgré ce défaut** : le corpus reste une excellente carte conceptuelle (7 240 titres, 15 388 items, vocabulaire de rigueur dense, distinctions utiles comme « fractale ≠ bruit procédural »). Ce qui manque, c'est le formalisme exécutable — précisément ce que le produit va produire.

## 6. Ce que je recommande

| # | Recommandation | Priorité | Dépendance |
|---|---|---|---|
| 1 | **Ne pas corriger le corpus maintenant.** Poursuivre l'audit avec le défaut documenté, et traiter la correction comme un chantier à part, décidé par vous | Haute | Votre accord |
| 2 | **Produire les fiches de domaine sur le fond conceptuel** (notions, définitions, enchaînements, distinctions, algorithmes décrits en prose, limites énoncées), en signalant pour chaque notion si son formalisme est exploitable ou perdu | Haute | Aucune |
| 3 | **Créer un registre des équations à réécrire**, alimenté au fil de la Phase 1 : notion, formule attendue, statut (perdue / partielle / présente), source de référence proposée | Haute | Aucune |
| 4 | **Vérifier s'il existe une version antérieure non dégradée** des documents (brouillon, export d'origine, historique d'outil) avant d'envisager une réécriture manuelle — c'est la voie la moins coûteuse | Haute | Vous seul pouvez répondre |
| 5 | Évaluer, une fois la Phase 1 terminée, si une passe de restauration automatique est envisageable (les motifs de perte sont réguliers : `\frac`, `\lim`, `\sum`, `\log`, lettres grecques) | Moyenne | Fin de Phase 1 |

## 7. Limites de cette analyse

- Heuristiques lexicales : elles ne détectent ni une équation complète mais fausse, ni une troncature qui laisse une formule syntaxiquement valide.
- Le taux de 30,8 % est un **plancher** : il ne compte pas les troncatures invisibles à ces motifs.
- Les documents A, B, C, D n'ont pas pu être analysés par cette méthode (aucune équation display détectée) ; la perte y est totale mais non chiffrable ainsi.
- Aucune vérification n'a été faite de l'exactitude des équations *complètes* : c'est un travail notion par notion, qui viendra avec les fiches.

## 8. Point exigeant votre attention

**Existe-t-il une version antérieure, non dégradée, de ces documents ?** Si oui, la restauration est immédiate et peu coûteuse. Si non, il faut décider d'une stratégie : réécriture ciblée des seules équations nécessaires aux composants, ou chantier de restauration global du corpus. Cette décision conditionne une partie du calendrier de la Phase 1.
