# 06 — Historique et décisions

**Date :** 2026-11-11 · **Commit :** `6f87baf`
**Sources :** `git log` (57 commits), les rapports `PHASE-0`, `A1`–`A10`, `CLOTURE-CHANTIER.md`,
`CLOTURE-DOMAINE-A.md`, `docs/decisions/`

---

## 1. Chronologie

Périodes établies d'après les dates d'auteur des commits (`git log --date=short`).

| Période | Étape | Commits | Ce qui s'est passé |
|---|---|---:|---|
| **2026-10-17** | **Ouverture** | 1→4 | premier commit `bdba473` ; **Phase 0** — rapport d'audit initial, shortlist de noms, inventaire d'accès |
| **2026-10-17 → 18** | **Nommage** | 5→8 | campagne de 242 sondes, 175 noms libres, 58 éliminés ; `A3`, `A4`, `A5` ; **inventaire structurel A2** |
| **2026-10-18** | **Décision du nom** | 9 | `mathemirum` adopté (décision 0001) ; fiche K ; ouverture du chantier de restauration |
| **2026-10-18** | **Restauration, régimes 1-2** | 10→37 | lots K, L, I, N, J — **773 restaurations** appliquées ; fiches L, D, N, I |
| **2026-10-19** | **Clôture du chantier** | 38→43 | `CLOTURE-CHANTIER.md` ; la couverture est mesurée, 18 lacunes identifiées puis comblées |
| **2026-10-19** | **Phase 2** | 44→50 | collecte, 11 fiches de plateforme, comparaison transversale, synthèse des différenciateurs, registre des licences |
| **2026-10-19** | **Étude de demande** | 51→53 | `A10` — ⚠️ **résultat défavorable** pour D1 et D2 ; proposition de licence du corpus source |
| **2026-10-20** | **Domaine A (régime 3)** | 54→61 | fiche A ; 52 propositions en 4 lots ; **6 lots appliqués, 70 substitutions** |
| **2026-11-10** | **Clôture de A, ouverture de B** | 62→63 | `CLOTURE-DOMAINE-A.md` ; inventaire des fragments de B ; **bilan exhaustif** ; lot B-1 proposé, non appliqué |
| **2026-11-11** | **Audit de connaissance** | — | le présent dossier |

⚠️ **Une interruption est visible** entre le 2026-10-20 et le 2026-11-10 : trois semaines sans
commit. Aucun document du dépôt ne l'explique.

---

## 2. Les décisions formalisées

Deux seulement ont été écrites dans `docs/decisions/`. Les autres sont consignées dans les
rapports.

### 2.1 Décision 0001 — le nom `mathemirum`

| | |
|---|---|
| **Date** | 2026-10-18 |
| **Statut** | ✅ **approuvée** (réversible) |
| **Contenu** | nom de travail, `PROJECT_CODENAME`, minuscules dans les identifiants techniques, **jamais écrit en dur** |
| **Options étudiées** | `mathauma` (choix précédent), `mathemos`, `magnificentia`, `wundermath`, `mathverse`, 58 autres |
| **Justification** | le nom ne doit pas décrire un axe technique, mais **porter la promesse** : montrer que les mathématiques sont belles, sublimes et spectaculaires |
| **Conséquences** | toute la documentation emploie `mathemirum` ou le neutre « le projet » |
| **Révision si** | antériorité de marque découverte, changement de positionnement, ou décision du porteur avant toute publication |

⚠️ **Limite assumée :** la vérification couvre npm, PyPI, GitHub et la recherche web. **Aucun
registre de marques** (INPI, EUIPO, USPTO) n'a été consulté.

### 2.2 Décision 0002 — licence du corpus source

| | |
|---|---|
| **Date** | 2026-10-19 |
| **Statut** | ⚠️ **PROPOSITION SOUMISE — en attente de décision. Rien n'a été appliqué.** |
| **Objet** | clarifier le régime juridique de `Stane316/my-own-connaissance` |
| **Constat** | dépôt **public sans licence** = tous droits réservés |
| **Pourquoi c'est bloquant** | c'est **le même défaut que le projet critique chez GeoGebra et `sadeepas`**. Un composant accompagné d'une équation du corpus reposerait sur une base juridique non établie |
| **Action requise** | le porteur se prononce |

Précision utile apportée par la décision : ❌ **les faits mathématiques ne sont pas protégeables**.
Une équation, un théorème, une valeur ne sont pas couverts par le droit d'auteur. Ce qui l'est,
c'est la **mise en forme** et le **choix d'agencement**.

---

## 3. Les décisions consignées dans les rapports

### 3.1 Phase 0 → Phase 1

| Décision | Contenu | Source |
|---|---|---|
| Périmètre de la Phase 1 | **les 29 documents**, littératie incluse | réponse d'approbation Phase 0 |
| Localisation des livrables | **à la fois** `/home/user/audit/` (brouillons) et `docs/audit/` (validés) | idem |
| Stratégie de licence | **reportée après la Phase 2** — ⚠️ aujourd'hui échue, la décision 0002 est en attente | idem |
| Nom du projet | voir décision 0001 | idem |

### 3.2 Restauration

| Décision | Contenu | Source |
|---|---|---|
| **Nature du chantier** | 🔴 **« Il ne s'agit pas d'une récupération, mais d'une reconstruction »** — le contenu détruit n'existe nulle part ailleurs | `restauration/README.md` §1 |
| Périmètre | restaurer **tout le corpus**, pas seulement ce dont les premiers composants ont besoin | porteur, 2026-10-18 |
| Validation | **lot par lot, avant application** | régle constante |
| Livraison | **branche dédiée, jamais de pull request** ; le porteur applique les diffs lui-même | porteur |
| Sauvegarde | une sauvegarde indépendante existe | porteur |
| Marquage | chaque équation reconstruite est **marquée comme reconstruction**, jamais présentée comme le texte d'origine | `README.md` §1 |
| Restructuration de A, B, C, D | ✅ **dans le périmètre de complétion** | porteur, 2026-10-18 |
| Repli « contenu perdu » | ✅ approuvé — ce qui ne peut être reconstruit est **inscrit au registre**, pas comblé | porteur |
| Entrelacement | ✅ restauration **puis** fiche, sur un document sain | porteur |

### 3.3 Phase 1 après la clôture du chantier

| Décision | Contenu | Date |
|---|---|---|
| **Reprise intégrale** (voie *b*) | ni suspension, ni réduction, ni clôture en l'état | 2026-10-19/20 |
| Ordre de traitement | **A → U**, puis les 8 documents de littératie | porteur |
| A traité en premier | pour **fixer la méthode** applicable à B, C et D | porteur |
| §9 — arbitrage | **faire les deux** | porteur |
| Mode de validation | délégué à l'agent → **par palier de confiance** | 2026-10-20 |
| **Validation en bloc des 52 propositions** | ✅ « je valide toutes tes suggestions » — les quatre points d'arbitrage sont tranchés en faveur de la recommandation | 2026-10-20 |
| Lot 5d | ❌ **définitivement non écrit** | 2026-10-19 |

### 3.4 Correction du plan A6

| Date | Correction |
|---|---|
| 2026-10-21 | **P — Cryptographie assigné au lot 3.** Le domaine P (4 120 lignes, 4ᵉ document le plus volumineux) **n'était assigné à aucun lot** : la table ne couvrait que 19 des 20 documents réels |

---

## 4. Les trois régimes de dégradation — découverte structurante

✅ Source : `restauration/README.md` §2. C'est la découverte qui a le plus influencé la méthode.

| | Régime | Documents | Ce qui subsiste | Méthode |
|---|---|---|---|---|
| 1 | Commandes LaTeX détruites **avec leurs arguments** | E à U | le bloc, son squelette, des fragments (`\_`, `_{}`, `( )`) | **reconstruction** |
| 2 | Lettres grecques détruites | E à U | idem, sans résidu | **reconstruction** |
| 3 | **Blocs `\[…\]` supprimés, formules aplaties en texte inline** | **A, B, C, D** | **les variables, l'ordre des opérations** | **recomposition** |

### Pourquoi le régime 3 est différent

Exemple vérifié, section 24 du document D :

```
R ( t ) =   O   +   td   n   ⋅   X   +   c   = 0   t   = −   n   ⋅   d n   ⋅   O   +   c
n   ⋅   d   =   0   ∥ P   −   C ∥   = 2   r 2
```

soit `R(t)=O+td`, `n·X+c=0`, `t=−(n·O+c)/(n·d)`, `n·d≠0`, `‖P−C‖²=r²`.

La barre de fraction disparaît, mais **numérateur et dénominateur restent adjacents et dans
l'ordre** : la recomposition est donc **déterministe**, et **plus sûre** que la reconstruction des
documents E à U, qui part de résidus.

Ce régime détruit en revanche les lettres grecques (sans laisser le résidu `\_`), les exposants et
indices, et quelques glyphes — **`≠` est perdu**.

### Le taux de dégradation mesuré

✅ `A7-integrite-des-equations.md`, rectifié le 2026-10-18 : **31,4 %** des 2 306 blocs qui sont de
véritables équations (48 blocs d'échappement de crochets exclus du dénominateur).

⚠️ **Rectification assumée publiée :** une affirmation antérieure (« 100 % de défauts » sur E, R, S,
U) était **fausse** — il s'agissait d'artefacts d'échappement, sans défaut structurel.

---

## 5. Les règles de méthode acquises par l'expérience

Ces règles ne sont pas des décisions formelles : elles ont été **apprises en se trompant**.

| Règle | Origine |
|---|---|
| 🔴 **Chercher une structure équivalente avant de conclure à l'impasse** | commit `5a9c382` — a permis de combler des blocs crus irrécupérables |
| 🔴 **Recalibrer le volume d'après la mesure réelle, jamais d'après l'estimation** | commit `50b06f2` |
| 🔴 **Un `git diff` incrémental par lot, testé sur worktree** | généralisé après le lot 6b |
| 🔴 **Mesurer la couverture en relisant les fichiers, jamais en recomposant un total** | `mesurer_couverture.py`, docstring |
| 🔴 **Ne pas compter les résidus par regex** | ⚠️ 3+ espaces → 425 faux positifs sur A ; le double espace intra-phrase → 1 452 |
| 🔴 **Ne pas compter les lettres grecques avec `grep -o`** | ⚠️ il compte des **octets** : 2 992 au lieu de 80 pour le document C. Utiliser `unicodedata` |
| 🔴 **Toujours vérifier `count("\n\n\n") == 0` après un essai à sec** | `retirer()`/`entre()` rendent un texte finissant déjà par `\n` |
| 🔴 **Sur les documents aplanis, seule la suite croissante des numéros donne le vrai plan** | une regex naïve de sections donne 88 candidats contaminés par ~30 listes numérotées |
| 🔴 **Tout livrable doit être commité** | sept réinitialisations du sandbox |

---

## 6. Expérimentations et pistes abandonnées

| Piste | Statut | Raison |
|---|---|---|
| **Recherche d'une version antérieure non dégradée de A, B, C, D** | ❌ abandonnée | ✅ confirmé par le porteur : **aucune version antérieure n'existe** |
| **Lot 5d** (domaine J) | ❌ définitivement non écrit | décision du porteur, 2026-10-19 |
| **Restauration du domaine D au lot 1** | ❌ sortie du périmètre clos | D relève du régime 3 → renvoyé au lot 4 avec A, B, C |
| **Réouverture du domaine A pour un lot 7** | ⏸️ **en suspens** | une correspondance **exacte** a été trouvée entre les fragments du §3.2 et sept emplacements vides du §3.1, mais la clôture était décidée avant la découverte |
| **`mathauma` comme nom** | ❌ remplacé | décision du porteur |
| **`curl` direct pour la veille web** | ❌ abandonné | bloqué par la politique réseau ; `fetch_page` utilisé à la place |
| **`git push` sur le dépôt de connaissances** | ❌ impossible | `403 — Permission denied` ; `push_via_api.py` écrit pour contourner, puis **abandonné** au profit de la livraison par diffs |
| **Comptage des défauts par heuristique composite** | ❌ écarté | `check_equations2.py` : « comptage par heuristique séparée, **pas de score composite** » |
| **Les cinq candidats du lot 6a** | ✅ **validés** | 19 candidats L/N validés et appliqués |

---

## 7. Corrections de chiffres publiés

Le projet a publiquement corrigé plusieurs de ses propres chiffres. ⚠️ **Ces corrections sont à
connaître : reprendre un ancien chiffre serait une erreur.**

| Ancien chiffre | Correction | Source |
|---|---|---|
| « 100 % de défauts » sur E, R, S, U | ❌ **faux** — artefacts d'échappement, sans défaut structurel. Taux réel mesuré : **31,4 %** | `A7` |
| « 12 emplacements vides » sur le document A | ❌ **faux** — le chiffre réel est **30** | `CLOTURE-DOMAINE-A.md` §4 |
| « 1 137 blocs » sans règle énoncée | ⚠️ exact **sous la règle `\[` en début de ligne** ; une règle plus large donne **1 146** | `CLOTURE-CHANTIER.md` §3 |
| Le test « moins de deux caractères » | ❌ **ce n'est pas une mesure** de l'état d'un bloc | `CLOTURE-CHANTIER.md` §7.3 |
| « 29 documents » | ✅ exact, **mais par un autre chemin** : 28 documents réels + la fiche d'absence de T | `CLOTURE-CHANTIER.md` §7.1 |
| P non assigné | ❌ lacune du plan A6, **corrigée** le 2026-10-21 | `A6` §4 |

**Ce que cette liste enseigne :** le projet a pour règle de **publier ses propres corrections**.
C'est cohérent avec le différenciateur D3 (limites connues) — et c'est un trait de culture à
conserver.
