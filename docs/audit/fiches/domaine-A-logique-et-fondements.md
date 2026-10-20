# FICHE DE DOMAINE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE

**Date :** 2026-10-20 — **Phase :** 1 (audit documentaire) — **Statut :** fiche 6/24, **partiellement vérifiée**
**Source :** `Maths-vers-Informatiques/DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE.md`
**Outils :** `tools/audit-phase1/profil_degradation.py` (déposé cette session) ; mesures complémentaires par scripts ad hoc
**Convention :** ✅ vérifié par lecture ou mesure · ⚠️ attesté par le plan mais non lu en détail · ❌ absent ou perdu
**Profondeur de lecture :** ~40 % du document (sections 0–2, 7, 10, 15, 16, 20–35 lues ; les autres attestées par le plan)

> **Avertissement de portée.** A est le premier des quatre documents dits « aplanis » (A, B, C, D). Il fixe la
> méthode appliquée ensuite à B, C et D — voir §11. Les conclusions des §5 et §11 valent pour les quatre ;
> les constats de contenu des §2, §3 et §7 valent pour A seul.

---

## 1. Identification et volume

| Métrique | Valeur |
|---|---|
| Lignes / octets / caractères | 119 / 81 681 / 77 970 |
| Lignes non vides | 60 (paragraphes de 1 299 caractères en moyenne) |
| Titres Markdown `#` | **0** |
| Blocs display `\[ … \]` | **0** |
| Gras `**` / puces de liste / backticks / backslashes | **0 / 0 / 0 / 0** |
| Pipes `\|` (tableaux) | **1** |
| Runs d'espaces multiples | **2 165** (1 410 doubles, 755 triples et plus) |
| Sections de premier niveau | **35**, de « 1. Identité » à « 35. Suite logique du parcours » |
| Sous-sections numérotées | ~100 (détection automatique, 112 entrées dont quelques faux positifs) |

A est le **document maître** du corpus : c'est lui qui définit le format que les autres suivent (§35 le dit
explicitement — « le document B suivra le même format maître »). Sa dénomination `DOCUMENT MAÎTRE A` n'est donc
pas honorifique.

### Position dans le corpus — mesure, pas impression

`profil_degradation.py` classe les 21 documents du dossier `Maths-vers-Informatiques` :

| Régime | Documents | Titres `#` | Blocs `\[` | Puces | Caractères / ligne |
|---|---|---|---|---|---|
| **Aplani** | **A, B, C, D** | 0 | 0 | 0 | 827 – 1 299 |
| Structuré | E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, U (16) | 197 – 359 | 6 – 332 | 329 – 862 | 23 – 56 |
| Intermédiaire | README (1) | 130 | 0 | 178 | 77 |

**A, B, C et D sont les quatre seuls documents du corpus dépouillés de toute structure Markdown et de tout
 LaTeX.** Le contraste est d'un facteur ~25 sur la longueur de ligne et n'admet pas d'interprétation
 intermédiaire. Ce résultat est reproductible : `python3 tools/audit-phase1/profil_degradation.py <racine_du_clone>`.

---

## 2. Objectif déclaré et couverture

Le document se présente comme une **« carte de reconnaissance »**, non comme un traité ✅. Son §0 pose quatre
questions que chaque notion doit permettre de trancher : *qu'est-ce que c'est / comment la reconnaître / à quoi
sert-elle en informatique / veux-je l'approfondir*. Son §33 porte une limite auto-déclarée, rare dans le corpus :

> « ce document constitue une cartographie pédagogique générale. Il ne contient pas encore une bibliographie
> vérifiée, référence par référence, ni les démonstrations complètes des théorèmes. » ✅

### Plan reconstruit (35 sections)

La numérotation survit intégralement en texte. Sections lues marquées ✅, attestées par le plan ⚠️.

| N° | Section | État |
|---:|---|---|
| 1 | Identité et question centrale du domaine (1.1–1.4) | ✅ |
| 2 | Vocabulaire fondamental | ✅ |
| 3 | Notations et signatures logiques à reconnaître (3.1–3.3) | ⚠️ |
| 4 | Logique propositionnelle (4.1–4.5) | ⚠️ |
| 5 | Logique des prédicats (5.1–5.4) | ⚠️ |
| 6 | Raisonnement et méthodes de démonstration (6.1–6.7) | ⚠️ |
| 7 | Induction, récursion et invariants (7.1–7.4) | ✅ |
| 8 | Ensembles (8.1–8.4) | ⚠️ |
| 9 | Paradoxes et limites du raisonnement formel (9.1–9.3) | ⚠️ |
| 10 | Théorèmes et résultats fondamentaux (10.1–10.7) | ✅ |
| 11 | Calculabilité (11.1–11.6) | ⚠️ |
| 12 | Logique des programmes et vérification formelle (12.1–12.7) | ⚠️ |
| 13 | Types et logique des langages de programmation (13.1–13.5) | ⚠️ |
| 14 | Langages formels (14.1–14.7) | ⚠️ |
| 15 | Algorithmes et méthodes phares du domaine A (15.1–15.10) | ⚠️ |
| 16 | Applications informatiques (16.1–16.8) | ✅ |
| 17 | Applications Web (17.1–17.5) | ✅ |
| 18 | Relation avec l'IA symbolique (18.1–18.4) | ⚠️ |
| 19 | Structures de données associées | ⚠️ |
| 20 | **Matrice centrale — problème → maths → algorithme → application** | ✅ |
| 21 | **Matrice — algorithme → applications** | ✅ |
| 22 | Problèmes types à reconnaître (10 réflexes) | ✅ |
| 23 | Outils et technologies à associer au domaine | ✅ |
| 24 | **Projets possibles pour le domaine A (5 + 1 portfolio)** | ✅ |
| 25 | Expérimentations personnelles (12) | ✅ |
| 26 | Ordre d'apprentissage recommandé (6 niveaux) | ✅ |
| 27 | Prérequis et dépendances (5 chaînes) | ✅ |
| 28 | **Connexions avec les autres domaines A → V** | ✅ |
| 29 | Sélection des notions à approfondir (29.1–29.6) | ⚠️ |
| 30 | Questions de maîtrise du domaine | ⚠️ |
| 31 | Challenge sans IA et challenge avec IA (31.1–31.2) | ✅ |
| 32 | Checkpoint final (17 items) | ✅ |
| 33 | Références de recherche et points à vérifier | ✅ |
| 34 | Livrable final du domaine A | ✅ |
| 35 | Suite logique du parcours | ✅ |

**Le plan est donc intégralement récupérable.** C'est le résultat le plus important de cette fiche : la
« reconstruction manuelle du plan » que le lot 4 d'A6 présentait comme une option incertaine est en réalité
**totale et mécanique**, parce que les intitulés n'ont pas été détruits — seul leur niveau hiérarchique l'a été.

---

## 3. Ce qui est remarquablement aligné avec le projet

### 3.1 Le catalogue de composants existe déjà (§24)

C'est la trouvaille la plus directe. Le §24 « Projets possibles » définit cinq projets puis un **projet
portfolio intitulé « Logic Lab — laboratoire interactif de logique et de fondements »** ✅, qui regroupe :

- un éditeur de formules ;
- un générateur de tables de vérité ;
- un visualiseur de règles d'inférence ;
- un mini-solveur SAT ;
- un éditeur d'automates ;
- un visualiseur d'AST ;
- un petit moteur de règles symboliques ;
- des explications et des expériences guidées.

Sept de ces huit modules sont des **composants visuels adossés à une notion mathématique explicite** — la
conjonction que le projet recherche. ⚠️ **Réserve obligatoire** : c'est un catalogue d'apprentissage écrit pour
une personne, pas une étude de demande. Le verdict de l'étude de demande (`A10`) s'applique : cette
convergence ne constitue pas une preuve de marché, et le §2.0 de `A9-synthese-differenciateurs` interdit de
présenter la couche de preuve comme argument d'appel.

### 3.2 Le vocabulaire de la couche de preuve est présent — contrairement à K

Mesure, occurrences et densité pour 10 000 caractères (seule normalisation honnête, les régimes de lignes
étant incomparables) :

| Mot | A | K | D |
|---|---:|---:|---:|
| « preuve » | **58** (7,4) | 0 | 0 |
| « hypothèse » | **22** (2,8) | 0 | 5 (0,9) |
| « limite » | 24 (3,1) | 6 (0,8) | 4 (0,7) |
| « contre-exemple » | **10** (1,3) | 0 | 0 |
| « validation » | 8 (1,0) | 1 (0,1) | 1 (0,2) |
| « test » | 14 (1,8) | 11 (1,5) | 25 (4,5) |

A est le seul document mesuré jusqu'ici où le vocabulaire des différenciateurs **D1** (hypothèses, domaine de
validité) et **D3** (limites connues) est réellement présent. Le raisonnement est robuste : la dégradation
*retire* du contenu, elle n'en ajoute pas — A possédait donc au minimum ces occurrences avant aplanissement.

⚠️ Ces mots sont **employés**, pas **structurés** : aucune section ne liste systématiquement les hypothèses
d'un énoncé donné. La présence du vocabulaire n'est pas l'existence de la pratique.

### 3.3 Trois sections sont directement exploitables

- **§20 — Matrice centrale** ✅ : 12 lignes *problème rencontré → mathématiques → méthode ou algorithme →
  application*. C'est, dans le corpus, la formalisation la plus proche d'une table de correspondance
  maths ↔ usage.
- **§21 — Matrice algorithme → applications** ✅ : 13 méthodes × 5 domaines (programmation, Web, IA
  symbolique, cybersécurité, systèmes), avec une légende explicite à quatre valeurs (Directe / Indirecte /
  Spécialisée / « — »). Le « — » est **défini** : « pas d'application générale à retenir ici ». La convention
  du registre des licences (un `?` est une non-évaluation, pas un non) est déjà respectée ici.
- **§22 — Problèmes types à reconnaître** ✅ : 10 énoncés en langage naturel, chacun renvoyant aux notions
  pertinentes. Matière première directe pour un moteur de recommandation.

### 3.4 Le §23 valide la pile technique du projet

Le tableau des outils ✅ associe explicitement **« JavaScript / TypeScript — Construire des visualisations
interactives et outils Web »**, et cite Python, Prolog, les solveurs SAT/SMT, Lean/Coq/Isabelle, Graphviz et
Jupyter. La pile pressentie par le projet est donc déjà celle que le corpus prescrit pour ce domaine.

---

## 4. Formalisme : état détaillé

### 4.1 Aucun bloc display, aucun délimiteur

A contient **0 bloc `\[ … \]`** et **0 délimiteur `$`**. Ce point distingue A des documents K, L, I, N, J :
dans ceux-ci, la dégradation avait **vidé** les blocs en laissant les délimiteurs en place (78 blocs
« sans contenu »). Dans A, il ne reste **aucun délimiteur**. Deux lectures sont possibles et **ne peuvent pas
être départagées sur pièce** :

1. A n'a jamais comporté de blocs display — son formalisme était intégralement en ligne ;
2. les blocs ont été supprimés **avec** leurs délimiteurs, ce qui serait un mécanisme distinct de celui
   observé sur K, L, I, N, J.

⚠️ Je ne tranche pas. Toute restauration qui postulerait la thèse 2 devrait d'abord établir l'existence de
blocs display dans une version antérieure — or il a été établi le 2026-10-18 qu'**aucune version antérieure de
A, B, C, D n'existe**. La thèse 2 est donc, en l'état, **instruisible mais non démontrable**.

### 4.2 Les formules n'ont pas disparu : elles ont été déplacées

C'est la découverte structurante de cette fiche. Les formules en ligne ont été dépouillées de leurs
délimiteurs, concaténées, puis **réinsérées en un autre point du texte**. Trois cas vérifiés ✅ :

**(a) Fin du §7.2** — fragments orphelins appartenant au §7.1 :

```
∧   P   ∧   Q   ⊢   P  ∨   P   ⊢   P   ∨   Q  ∨   P   ∨   Q  ⊢
⊨  P   ( n )   n   ≥   n 0  P   ( n   ) 0  P   ( n ) →   P   ( n   + 1)
P   ( n )   n   ≥   n 0  P   ( n )  n
```

S'y lisent sans ambiguïté `P ∧ Q ⊢ P` (élimination de ∧), `P ⊢ P ∨ Q` (introduction de ∨), `P(n₀)`
(initialisation) et `P(n) → P(n+1)` (hérédité) — c'est-à-dire **exactement les trois formules absentes du §7.1**,
dont l'énoncé est resté sur place : « Pour démontrer une propriété _ pour tout entier _ , on établit :
1. Initialisation : _. 2. Hérédité : _. 3. Conclusion : _ est vraie pour tout _ ».

**(b) Milieu du §10.2** — une phrase est littéralement coupée en deux par l'insertion :

> « La résolution propositionnelle est une règle d'inférence importante ; elle ne signifie pas que toute
> question logique imaginable devient automatiquement décidable par cette **[ici : `¬(P ∧ Q) ≡ ¬P ∨ ¬Q`,
> `¬(P ∨ Q) ≡ ¬P ∧ ¬Q`, `(P ∨ A), (¬P ∨ B) ⇒ (A ∨ B)`]** méthode. »

**(c) Entre le §10.6 et son contenu** — le fragment `H(P, x) = {1 si P(x) s'arrête, 0 sinon}` s'est intercalé
entre l'intitulé « Ce que cela ne veut pas dire » et son paragraphe.

Le même mécanisme déplace des **blocs de prose entiers**, pas seulement des formules ✅✅ : en §1.2/§1.3 la
réponse de 1.2 apparaît après l'amorce de 1.3 ; en §32/§33 la liste d'auto-évaluation de 17 items du §32 se
retrouve au milieu de la liste de références du §33 ; en §35 les exemples de réflexes du « principe de sortie »
sont rejetés en fin de document.

### 4.3 Ce qui survit intégralement

| Objet | État | Vérification |
|---|---|---|
| Tables de vérité (5) | ✅ **complètes et correctes** | Séquences V/F relues et confrontées aux définitions : négation `VF/FV`, conjonction `VVV·VFF·FVF·FFF`, disjonction, implication `VV→V, VF→F, FV→V, FF→V`, équivalence — **toutes exactes** |
| Symboles logiques | ✅ présents en Unicode nu | `¬`×34, `∨`×19, `∧`×16, `≡`×10, `∀`×9, `∃`×9, `⊢`×6, `→`×55, `⊨`×2, `⊤`, `⊥`, `∈`×3, `≤`, `≥`×3 |
| Tableaux | ✅ aplatis mais complets | Cellules séparées par doubles espaces, en-têtes identifiables (§20, §21, §23, §28) |
| Contenu de code | ⚠️ partiel | Un extrait lisible : `const canSubmit = isAuthenticated && formIsValid && !isSubmitting` ; la balise `JavaScript` a survécu comme mot isolé (×2), avec `TypeScript` ×1 et `Python` ×1 |

⚠️ **Attention sur les balises** : `Prolog` apparaît 10 fois, mais Prolog est aussi un sujet du §18.3. Seules
les balises JavaScript, TypeScript et Python sont indicatives d'anciens blocs de code — et même là, avec
prudence.

### 4.4 Ce qui est définitivement perdu

- L'**emphase** (`**gras**`) : 0 astérisque survivant ; la hiérarchie visuelle interne est irrécupérable.
- Le **niveau hiérarchique** des titres : les intitulés subsistent, pas leur rang (`#`, `##`, `###`).
- Les **frontières de listes** : 0 puce ; les items sont séparés par des doubles espaces ou des points-virgules.
- La **position** des formules — c'est la perte la plus coûteuse, et la seule qui rende la restauration risquée.

---

## 5. Typologie de la dégradation (vaut pour A, B, C, D)

Quatre mécanismes distincts, de récupérabilité très inégale :

| # | Mécanisme | Trace | Récupérable ? | Risque |
|---:|---|---|---|---|
| 1 | **Aplanissement Markdown** | titres, gras, puces, tableaux réduits à la prose | **Oui** — les intitulés et les cellules subsistent | Faible |
| 2 | **Aplanissement des tableaux** | doubles espaces entre cellules | **Oui** — en-têtes identifiables | Faible |
| 3 | **Déplacement des formules** | tas de fragments orphelins | **Partiellement** — le contenu existe, l'emplacement n'est plus attesté | **Élevé : erreur d'attribution** |
| 4 | **Décomposition des accents** | `s'arrête` → `s'arr te e ˆ` ; `Tables de v é rit é` (§27) | Oui, trivialement | Nul |

**Le mécanisme 3 est le seul qui interdise une restauration mécanique.** Rendre `P(n) → P(n+1)` au §7.1 est une
inférence, pas une lecture : elle est ici très bien fondée (le texte énonce « Hérédité : _ »), mais elle reste
une reconstruction et doit être marquée comme telle. C'est une différence de nature avec les 773 restaurations
du chantier précédent, où le **contenu manquait dans un emplacement connu** ; ici, le contenu existe dans un
**emplacement inconnu**.

Le mécanisme 4 est mineur en volume (8 caractères dans A) mais révèle un passage par une décomposition Unicode
qui a substitué des lettres modificatives (`U+02CA`, `U+02CB`, `U+02C6`) aux accents combinants.

---

## 6. Lacunes relevées

1. **Aucune bibliographie.** §33 le reconnaît explicitement ✅. 1 occurrence de « bibliographie », 6 de
   « référence » — et ce sont des renvois génériques (« les cours universitaires de… »), pas des citations.
2. **Aucune démonstration complète.** Déclaré, assumé, conforme au statut de cartographie — mais cela
   interdit de traiter A comme une source de preuves réutilisables.
3. **Zéro bloc de code formaté.** Un seul extrait JavaScript lisible dans tout le document, alors que le §24
   propose cinq projets d'implémentation.
4. **Zéro formule display.** Voir §4.1 — cause non départageable.
5. **Le §28 indexe deux domaines absents du corpus.** La table « Connexions avec les autres domaines A → V »
   liste 22 entrées (B → V) ✅ ; or le corpus ne contient que 20 documents de maths, **sans T ni V**
   (T — théorie des jeux, V — théorie des catégories). Le document maître décrit donc un parcours plus vaste
   que le corpus livré. Lacune de complétude, pas d'exactitude.
6. **Déplacement de contenu non cartographié.** Le nombre exact de blocs déplacés dans A n'a pas été mesuré ;
   seuls trois cas ont été vérifiés en détail (§4.2). Toute exploitation du document doit intégrer cette
   incertitude.
7. **Aucune équation indexée.** Impossible de produire un inventaire « notion → formule → ligne » comme pour K
   : il n'y a ni formule en place ni numéro de ligne stable.

---

## 7. Relations mathématiques ↔ usages

A est un domaine **non visuel par nature** : la logique ne produit pas spontanément une image. Le §24 fournit
cependant la transposition, et le §20 la table de correspondance.

| Bloc du document | Usage produit envisageable | Attesté par |
|---|---|---|
| Connecteurs, tables de vérité, tautologies | **Générateur de tables de vérité** | §24.1, §15.2 ✅ |
| Évaluation booléenne, formes normales | **Éditeur / évaluateur de formules** | §24 portfolio ✅ |
| Satisfaisabilité, DPLL, CDCL | **Mini-solveur SAT** avec exploration d'arbre | §24.2, §15.3–15.5 ✅ |
| Résolution, règles d'inférence | **Visualiseur de règles d'inférence** | §24 portfolio ✅ |
| Induction, récurrence, invariants | Démonstration pas à pas animée | §7, §15 ✅ |
| Automates finis, langages réguliers | **Éditeur d'automates** | §24 portfolio, §14.3 ✅ |
| Grammaires, analyse syntaxique, AST | **Visualiseur d'AST** | §24.3, §14.6 ✅ |
| Chaînage, unification, prédicats | **Moteur de règles symboliques** | §24.4, §18 ✅ |
| Diagonalisation de Cantor, machines de Turing | Diagonale animée, ruban de Turing | §8.4, §11.4 ⚠️ |

⚠️ Les trois dernières lignes du bas de tableau sont des propositions dérivées de la lecture, non des projets
énoncés par le corpus — sauf mention contraire dans la colonne de droite.

---

## 8. Index — premières notions (A)

Colonne « État du formalisme » : ✅ formule en place · ⚠️ énoncé sans formule · ❌ formule déplacée ou perdue.

| Notion | Objet mathématique | Représentation visualisable | Composant potentiel | Ce qui serait vérifiable | État |
|---|---|---|---|---|---|
| Table de vérité | fonction booléenne | grille V/F | *Générateur de tables* | exhaustivité des `2ⁿ` affectations ; détection tautologie / contradiction | ✅ |
| Évaluation booléenne | arbre d'évaluation | arbre annoté | *Évaluateur de formules* | comparaison à une référence ; cas limites | ⚠️ |
| Lois de De Morgan | équivalence logique | deux formules reliées | *Réécriture animée* | invariance de la table | ❌ |
| Résolution propositionnelle | règle d'inférence | étapes de dérivation | *Visualiseur de résolution* | préservation de la satisfaisabilité | ❌ |
| Induction simple | `P(n₀)`, `P(n) → P(n+1)` | déroulé des cas | *Induction animée* | les deux conditions ; cas de base | ❌ |
| Invariant de boucle | logique de Hoare | état avant / après itération | *Vérificateur d'invariant* | initialisation, préservation, sortie | ⚠️ |
| Satisfaisabilité (SAT) | affectation, clause | exploration d'arbre | *Mini-solveur SAT* | jeux satisfiables / insatisfiables ; croissance du coût | ⚠️ |
| Automate fini | langage régulier | graphe d'états | *Éditeur d'automates* | acceptation / rejet de mots tests | ⚠️ |
| AST | grammaire formelle | arbre syntaxique | *Visualiseur d'AST* | correspondance grammaire ↔ arbre | ⚠️ |
| Unification | substitution | termes avant / après | *Moteur d'unification* | échec (occurs check) | ❌ |
| Diagonalisation de Cantor | cardinalité | tableau diagonal | *Diagonale de Cantor* | construction du contre-exemple | ⚠️ |
| Machine de Turing | calculabilité | ruban et tête | *Machine de Turing* | rubans de référence à résultat connu | ⚠️ |

---

## 9. Fiabilité, cohérence, traçabilité

- **Cohérence interne :** bonne ✅. La progression §1 → §35 est logique (fondations → formalismes → théorèmes →
  algorithmes → applications → auto-évaluation), et le document distingue soigneusement ce qui est démontrable
  de ce qui est calculable (§1 : « une proposition peut être vraie sans être démontrable dans un système formel
  donné »).
- **Exactitude des objets vérifiables :** bonne ✅. Les cinq tables de vérité relues sont **toutes correctes**,
  y compris l'implication matérielle — piège classique. Aucune erreur détectée dans les énoncés lus.
- **Traçabilité :** faible ❌. Aucune référence bibliographique, aucune attribution de formule, aucune source.
  §33 le concède.
- **Fiabilité du formalisme :** **non évaluable** ❌. Il n'existe aucune formule en place à contrôler. Les
  fragments récupérables sont corrects mais non situés.
- **Fiabilité de l'ordre du contenu :** **compromise** ❌. Voir §4.2 — trois cas de déplacement vérifiés,
  nombre total non mesuré. C'est le point le plus pénalisant du document : on peut faire confiance aux
  énoncés lus un par un, **pas à leur enchaînement**.

---

## 10. Niveau de maturité

| Dimension | Évaluation | Justification |
|---|---|---|
| Conceptuelle | **Élevée** | 35 sections, plan complet, distinctions fines (correction vs complétude vs incomplétude, syntaxe vs interprétation vs vérité) |
| Pédagogique | **Élevée** | 6 niveaux d'apprentissage, 12 expérimentations, 17 items d'auto-évaluation, 5 projets, challenges avec et sans IA |
| Applicative | **Élevée** | §20 et §21 : deux matrices de correspondance problème → méthode → application |
| Formelle | **Nulle en l'état** | 0 formule en place ; fragments récupérables mais non situés |
| Exécutable | **Quasi nulle** | 1 extrait de code, non formaté |
| Validation | **Faible** | vocabulaire présent (22 « hypothèse », 10 « contre-exemple ») mais non structuré en pratique |
| Structurelle | **Nulle** | 0 titre, 0 liste, 0 tableau formaté ; plan reconstruit par lecture, pas par balisage |

---

## 11. Méthode retenue pour B, C et D

A ayant servi de banc d'épreuve, la méthode suivante est **validée sur un document** et sera appliquée
identiquement à B, C et D. Elle est volontairement **non reconstructrice** : elle mesure et décrit, elle ne
restaure rien sans validation lot par lot.

1. **Profiler d'abord** — `profil_degradation.py` sur le document et sur le corpus. Le diagnostic
   `aplanie` / `structuree` doit être établi par la mesure, jamais par impression.
2. **Reconstruire le plan par détection**, jamais par échantillonnage : les intitulés de section survivent en
   texte (`NN. TITRE`). Sur A, cette étape a rendu **35 sections sur 35**, sans perte.
3. **Lire les sections porteuses** plutôt que le document linéairement : pour un document de cartographie, les
   sections « matrice », « projets », « applications » et « connexions » concentrent l'essentiel.
4. **Séparer les trois mécanismes récupérables** (aplanissement, tableaux, accents) du mécanisme non
   mécanique (déplacement des formules). Les trois premiers se traitent par lecture ; le quatrième exige une
   proposition explicite, avec le risque d'attribution **toujours** énoncé.
5. **Vérifier les objets contrôlables** — tables de vérité, symboles, énoncés — et dire lesquels ont été
   effectivement contrôlés. Sur A : 5 tables sur 5 relues, toutes correctes.
6. **Ne jamais compter les blocs pour juger de l'intégrité** : le déplacement rend le comptage trompeur.
   Utiliser l'équilibre des délimiteurs, ou renoncer au comptage.

**Deux pièges rencontrés, à ne pas reproduire :**
- Une sortie d'outil peut présenter des `\n` qui n'existent pas dans le fichier (double échappement JSON).
  Toujours confirmer une « découverte » par une seconde mesure indépendante — ici, un comptage de backslashes
  qui a renvoyé 0 et infirmé la première lecture.
- Un motif non échappé peut matcher à côté : `C++` est un quantificateur possessif en Python 3.11+, il
  comptait les lettres `C` isolées. Toujours `re.escape` les chaînes littérales.

---

## 12. Besoins de documentation complémentaire

1. **Restituer les formules déplacées** — en priorité celles dont l'emplacement est attesté par l'énoncé
   environnant (induction §7.1, De Morgan §10.1, résolution §10.2, arrêt §10.6). Chaque restitution doit être
   marquée comme reconstruction, avec le texte-source qui la justifie.
2. **Cartographier exhaustivement les déplacements** dans A avant toute exploitation : le nombre n'a pas été
   mesuré, seuls trois cas sont documentés.
3. **Établir une bibliographie** — lacune auto-déclarée au §33.
4. **Ajouter les hypothèses et conditions de validité** de chaque théorème. Le vocabulaire existe (22
   occurrences d'« hypothèse ») ; la pratique structurée n'existe pas.
5. **Combler ou retirer les renvois vers T et V** (§28) : le parcours décrit 22 domaines, le corpus en
   contient 20.
6. **Traiter le projet « Logic Lab » du §24 comme une hypothèse de catalogue**, pas comme une direction
   produit validée : le verdict de l'étude de demande s'applique.

---

**Référence de méthode :** la procédure de reconstitution du clone et de réapplication des 17 diffs est dans
`docs/restauration/CLOTURE-CHANTIER.md` §6, validée au §6.1. Le profilage de ce document est reproductible par
`tools/audit-phase1/profil_degradation.py`.
