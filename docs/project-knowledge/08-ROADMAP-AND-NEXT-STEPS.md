# 08 — Feuille de route et prochaines étapes

**Date :** 2026-11-11 · **Commit :** `6f87baf`
⚠️ **Ce document propose.** Aucune des étapes ci-dessous n'a été validée par le porteur, à
l'exception de celles qui sont déjà engagées et marquées ✅.

---

## 1. Rappel de la situation

Le projet est en **Phase 1**, entrelacée avec le chantier de restauration. **Aucun code
d'application n'existe.** La construction (Phase 5 et au-delà) est soumise à validation explicite et
ne doit pas être engagée sans autorisation.

La feuille de route qui suit est donc celle de **l'achèvement de la connaissance**, puis
éventuellement de la construction.

---

## 2. Ce qui est déjà décidé et engagé

| Décision | Source | Statut |
|---|---|---|
| Reprise intégrale de la Phase 1 (voie *b*) | porteur, 2026-10-19 | ✅ engagée |
| Ordre **A → U**, puis les 8 documents de littératie | porteur | ✅ engagé |
| Restauration et rédaction **entrelacées** | porteur, 2026-10-18 | ✅ engagé |
| Validation **lot par lot** avant application | régle du chantier | ✅ en vigueur |
| A, B, C, D restructurés dans le périmètre | porteur, 2026-10-18 | ✅ engagé |
| Livraison par branche dédiée, **jamais de PR** | porteur | ✅ en vigueur |
| Repli « contenu perdu » approuvé | porteur | ✅ en vigueur |

---

## 3. Phase 1 — suite (en cours)

### 3.1 La boucle par document

```
1. reconstituer l'atelier   bash tools/restauration/reconstituer_atelier.sh
2. profiler                 profil_degradation.py          (mesure, jamais impression)
3. inventorier              plan reconstruit + piles + slots
4. proposer un lot          soumis, jamais appliqué sans accord
5. appliquer                sur validation, par générateur, avec journal
6. livrer                   .gitdiff + .message-commit.txt + .journal.json
7. rédiger la fiche         sur un document sain
```

### 3.2 Ordre des prochains documents

| Rang | Document | Pourquoi |
|---:|---|---|
| **1** | **B** — lot 1 appliqué, puis les lots suivants | en cours ; la méthode est rodée |
| **2** | **fiche B** | entrelacement |
| 3 | **C** — algèbre linéaire | régime 3 |
| 4 | **D** — géométrie computationnelle | régime 3, fiche déjà faite |
| 5 | puis E → U selon le plan A6 | régimes 1 et 2 |
| 6 | les 8 documents de littératie | lot 5 |

**B, puis C, puis D** : c'est l'ordre alphabétique de la directive « A → U ». Aucune priorisation
tactique n'est à plaider par-dessus.

À titre d'information, les trois documents du régime 3, mesurés le 2026-11-11 :

| Document | Caractères | Lignes | Titre/blocs/`**`/puces | Grecques | Lignes à runs |
|---|---:|---:|---|---:|---:|
| **B** — Théorie des nombres | 65 371 | 103 | **0 · 0 · 0 · 0** | 19 (toutes `φ`) | 52 |
| **C** — Algèbre linéaire | 73 453 | 123 | **0 · 0 · 0 · 0** | **80** | 62 |
| **D** — Géométrie computationnelle | 55 452 | 133 | **0 · 0 · 0 · 0** | 27 | 67 |

### 3.3 Critères de sortie par document

Un document est **traité** lorsque :

1. son plan a été reconstruit par détection, jamais par échantillonnage ;
2. chaque fragment dégradé a une proposition **ou** une décision argumentée de ne rien faire ;
3. le correctif a été vérifié à sec puis appliqué ;
4. le diff et le rapport d'application sont livrés ;
5. **les blocs non restituables sont inscrits au registre, pas laissés dans l'oubli** ;
6. la fiche est rédigée sur le document sain.

---

## 4. Les jalons proposés

### Jalon R1 — Lever les quatre points du registre des licences

| | |
|---|---|
| **Objectif** | clore la seule action restante de la Phase 2 |
| **Travaux** | obtenir une réponse écrite des éditeurs sur les quatre points |
| **Dépendance** | les éditeurs — **hors de portée de l'agent** |
| **Livrable** | le registre des licences complété |
| **Critère** | les quatre points sont clos ou déclarés clos par défaut |
| **Priorité** | 🔴 **haute** — conditionne D5 |
| **Risque** | absence de réponse des éditeurs |

### Jalon R2 — Décider de la licence du corpus source

| | |
|---|---|
| **Objectif** | établir la base juridique du projet |
| **Travaux** | le porteur se prononce sur le régime de `my-own-connaissance` |
| **Dépendance** | **le porteur seul** |
| **Livrable** | un fichier `LICENSE` sur les deux dépôts |
| **Critère** | les deux dépôts déclarent une licence |
| **Priorité** | 🔴 **haute** — c'est le point bloquant n°1 |
| **Risque** | ⚠️ publier sans avoir tranché **reproduirait le défaut critiqué chez GeoGebra** |

### Jalon R3 — Achever le domaine B

| | |
|---|---|
| **Objectif** | premier document du régime 3 mené à terme après A |
| **Travaux** | appliquer le lot 1 ; produire les lots suivants ; rédiger la fiche B |
| **Dépendance** | validation du porteur pour chaque lot |
| **Livrable** | diffs + fiche |
| **Critère** | les six critères de sortie du §3.3 |
| **Priorité** | 🟠 **courante** — c'est le travail en cours |

### Jalon R4 — Traiter C et D

| | |
|---|---|
| **Objectif** | achever les quatre documents aplanis |
| **Travaux** | inventaire, lots, fiches |
| **Dépendance** | R3 (la méthode sera éprouvée deux fois) |
| **Livrable** | 2 fiches + diffs |
| **Priorité** | 🟠 courante |

### Jalon R5 — Achever les régimes 1 et 2 (E → U)

| | |
|---|---|
| **Objectif** | 13 documents restants |
| **Travaux** | inventaire des défauts, reconstruction, fiches |
| **Volume estimé** | au moins **266 lignes à défaut** relevées par l'inventaire heuristique sur 7 documents — ⚠️ **sous-estimation certaine**, l'inventaire ne couvre que 13 documents |
| **Priorité** | 🟡 moyenne |

### Jalon R6 — Littératie technique

| | |
|---|---|
| **Objectif** | 8 documents |
| **Charge** | ⚠️ **beaucoup plus légère** : 27 075 lignes mais **32 équations affichées seulement**. Le formalisme n'y est presque pas dégradé |
| **Priorité** | 🟡 moyenne |

### Jalon R7 — L'index notion → composant

| | |
|---|---|
| **Objectif** | livrer la table qui relie le corpus au produit |
| **Travaux** | alimenter l'index prévu par `A6` §3.4 au fil des fiches |
| **Dépendance** | ⚠️ **l'achèvement des fiches** — c'est une consolidation, pas une tâche parallèle |
| **Priorité** | 🟡 moyenne ; ⚠️ **non commencé** |

### Jalon R8 — Ouvrir la construction

| | |
|---|---|
| **Objectif** | passer de la connaissance au produit |
| **Préalables** | 🔴 R1 et R2 levés · 🔴 validation explicite du porteur · 🔴 architecture cible arrêtée |
| **Priorité** | ⬜ **soumise à validation** — ne pas engager |

---

## 5. Ce qu'il ne faut **pas** faire

Cette section est aussi importante que la précédente.

### 5.1 Développements prématurés

| À ne pas faire | Pourquoi |
|---|---|
| ❌ **Écrire le moindre composant** | la construction est soumise à validation explicite ; aucune architecture n'est arrêtée |
| ❌ **Choisir un framework maintenant** | React est dominant (83 %) mais rien n'est tranché, et le choix doit suivre l'architecture, pas la précéder |
| ❌ **Créer un site de découverte** | aucun composant à montrer |
| ❌ **Mettre en place une base de données** | aucun besoin identifié à ce stade. ⚠️ Supabase/PostgreSQL était une préférence initiale du porteur, à comparer objectivement — **aucune migration, aucun service payant sans autorisation** |

### 5.2 Refactorisations sans valeur

| À ne pas faire | Pourquoi |
|---|---|
| ❌ Refactoriser les 30 scripts d'outillage | ils fonctionnent ; la mission était documentaire |
| ❌ Unifier `apply_patch.py` et `lot_commun.py` | 🔶 les deux moteurs répondent à des régimes différents ; la fusion n'a pas de valeur démontrée |
| ❌ Remplacer les chemins absolus par une configuration | souhaitable à terme, mais c'est une amélioration d'outillage, pas un jalon |

### 5.3 Expérimentations déjà faites, à ne pas refaire

| Ne pas refaire | Conclusion acquise |
|---|---|
| ❌ Chercher une version antérieure non dégradée de A, B, C, D | ✅ confirmé : **elle n'existe pas** |
| ❌ Compter les défauts par regex | ⚠️ 425 faux positifs sur A ; seule la lecture tranche |
| ❌ Compter les grecques avec `grep -o` | ⚠️ il compte des octets (2 992 au lieu de 80) |
| ❌ Une regex naïve pour les sections d'un document aplani | ⚠️ 88 candidats contaminés sur B ; seule la suite croissante donne le plan |
| ❌ Un score composite d'intégrité des équations | ❌ écarté : comptage par heuristique séparée |
| ❌ `curl` direct pour la veille | ❌ bloqué par la politique réseau |

### 5.4 Risques de dispersion

⚠️ **Ne pas rouvrir la question du nom.** `mathemirum` est décidé. La révision est conditionnée à
une antériorité de marque, un changement de positionnement, ou une décision du porteur — rien de
tel n'est survenu.

⚠️ **Ne pas relancer la veille concurrentielle sans motif.** 27 plateformes ont été étudiées. La
recommandation R7 est levée. Repartir en collecte sans question nouvelle serait du travail perdu.

⚠️ **Ne pas rejouer l'étude de demande en espérant un meilleur résultat.** `A10` a répondu, et la
réponse est défavorable sur D1 et D2. La compléter est légitime ; la refaire pour obtenir un
résultat plus agréable ne l'est pas.

---

## 6. Hiérarchie des priorités

| Rang | Action | Priorité | Dépendance |
|---:|---|---|---|
| 1 | **Décider de la licence du corpus source** | 🔴 haute | le porteur |
| 2 | **Lever les quatre points du registre des licences** | 🔴 haute | les éditeurs |
| 3 | **Valider et appliquer le lot B-1** | 🟠 courante | le porteur |
| 4 | Achever B (lots suivants + fiche) | 🟠 courante | 3 |
| 5 | Traiter C, puis D | 🟠 courante | 4 |
| 6 | Trancher l'incohérence D/J du lot 1 | 🟡 moyenne | le porteur |
| 7 | Trancher la réouverture de A (lot 7) | 🟡 moyenne | le porteur |
| 8 | Achever E → U | 🟡 moyenne | 5 |
| 9 | Littératie technique | 🟡 moyenne | 8 |
| 10 | Index notion → composant | 🟡 moyenne | 9 |
| 11 | Compléter l'étude de demande | 🟢 basse | — |
| 12 | Ouvrir la construction | ⬜ validée | 1, 2, 10 + accord |

---

## 7. Le risque de fond

⚠️ **La question posée par `A10` n'a pas été tranchée.**

Les deux différenciateurs les plus identitaires du projet — **D1** (équations, hypothèses, domaine
de validité) et **D2** (classement tripartite) — sont les deux dont **la demande n'est pas établie**.
Aucune source, sur les ~20 guides consultés, ne mentionne ces attributs comme critère de choix.

Deux voies s'ouvrent, et **le porteur doit choisir explicitement** :

| Voie | Conséquence |
|---|---|
| **A — Assumer la rigueur comme fin en soi** | la question du marché devient secondaire. C'est légitime : ces exigences viennent du cahier des charges. ⚠️ **Mais il faut le dire**, pas le supposer |
| **B — Poursuivre l'adéquation au marché** | alors D1 et D2 doivent être **présentés par leurs bénéfices observés** (débogable, mesuré, lisible par une machine), jamais comme argument premier — c'est la recommandation **R3.1**, devenue structurante |

🔶 **Tant que ce choix n'est pas fait, toute la construction repose sur une hypothèse non
vérifiée.** C'est, pour un nouvel agent, **la première chose à faire trancher avant d'écrire la
moindre ligne de code produit**.
