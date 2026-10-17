# RAPPORT — PHASE 0 : VÉRIFICATION DES ACCÈS ET DU PÉRIMÈTRE
**Projet :** écosystème open source de création web et visuelle fondé sur les mathématiques
**Nom de travail :** non arrêté (deux noms coexistent dans le cahier des charges : « MATHVERSE » et « MATHÉON ») — voir §9, point bloquant 1
**Date :** 2026-10-17 — **Auteur :** agent Arena (mode audit, lecture seule)
**Branche de travail :** `arena/2e20eccb-mathverse` (dépôt `Stane316/mathverse`)
**Statut :** Phase 0 terminée — **aucune modification de dépôt, aucun commit, aucun push**

---

## 1. Résumé exécutif

Les deux dépôts annoncés **existent, sont publics et sont pleinement accessibles** en lecture : `Stane316/my-own-connaissance` (1,9 Mio, 29 documents Markdown, 1 commit) et `Stane316/mathverse` (44 Kio, 2 documents Markdown, 1 commit). Le clone local du dépôt de connaissances a été réalisé et son contenu inventorié fichier par fichier.

Trois constats structurants, tous vérifiés :

1. **Aucun des deux dépôts ne possède de licence.** `license: null` côté API, aucun fichier `LICENSE`, aucun `README` racine. Juridiquement, un dépôt public sans licence reste soumis au droit d'auteur par défaut : le projet ne peut donc pas encore être qualifié d'open source, et toute réutilisation de code tiers (React Bits, Uiverse, shadcn…) devra être instruite avant intégration.
2. **Le domaine T (théorie des jeux) est annoncé par le document maître mais n'existe pas.** Le `README.md` le décrit (§7.14) ; aucun fichier correspondant dans l'arbre Git. Par ailleurs, **quatre documents (A maître, B, C, D) ont perdu toute leur structure de titres Markdown** (`grep -c '^#'` = 0, contre 130 à 380 pour les autres), ce qui bloque l'indexation automatique et la navigation.
3. **Le nom « MathVerse » est déjà occupé dans le même espace conceptuel.** Il désigne un benchmark de mathématiques visuelles (ECCV 2024, 184 ★, MIT), un jeu de données Hugging Face et un paquet PyPI existant. Une suite d'applications web mathématiques interactives homonyme existe également. Les noms `matheon` (npm, PyPI, GitHub) et `mathverse` (npm) sont libres.

Côté capacités : la veille web est opérationnelle (`fetch_page` atteint reactbits.dev et uiverse.io, `web_search` fonctionne), l'API GitHub et le clonage sont disponibles. En revanche, **l'environnement ne dispose ni de GPU ni de navigateur** : les mesures de performance GPU/WebGL/WebGPU devront être déportées (protocole exécuté chez vous ou en CI), et non simulées ici.

Aucune écriture n'a été effectuée. Le présent rapport et son annexe sont déposés **hors dépôt**, dans `/home/user/audit/`, pour respecter la règle d'audit en lecture seule.

## 2. Périmètre effectivement traité

- Vérification des URL fournies et de l'existence réelle des deux dépôts.
- Vérification des permissions et des capacités réelles de l'environnement (réseau, outillage, matériel).
- Inventaire complet et mesuré du dépôt de connaissances (arborescence, tailles, densité de structure).
- Inventaire du dépôt produit (contenu du premier commit, structure, signaux de qualité).
- Sondes de disponibilité de noms (npm, PyPI, GitHub) et détection de collisions.
- Test des outils de recherche et de navigation.
- Définition des plans d'audit documentaire (Phase 1) et de veille concurrentielle (Phase 2).

**Hors périmètre de la Phase 0 (volontairement) :** lecture approfondie du contenu mathématique, fiches plateformes, proposition d'architecture, toute écriture.

## 3. Ressources et sources examinées

| Ressource | Nature de l'accès | Statut |
|---|---|---|
| `github.com/Stane316/mathverse` | git local + API REST | ✅ vérifié |
| `github.com/Stane316/my-own-connaissance` | API REST + clone `--depth 1` | ✅ vérifié (29 fichiers lus en métadonnées, échantillons lus en contenu) |
| `reactbits.dev` | `fetch_page` (curl direct bloqué) | ✅ accessible |
| `uiverse.io` | `fetch_page` (curl direct bloqué) | ✅ accessible |
| `api.github.com` (recherche, arbres, README) | curl / `gh` | ✅ accessible |
| `registry.npmjs.org`, `pypi.org` | curl | ✅ accessibles |
| `raw.githubusercontent.com`, `geogebra.org`, `p5js.org`, `reactbits.dev`, `uiverse.io` (depuis bash) | curl | ❌ bloqués par la politique réseau du sandbox |

Détail chiffré, preuves et journal des opérations : **annexe `annexes/A0-inventaire-acces-et-preuves.md`**.

## 4. Méthode suivie

1. Constater l'état réel des dépôts avant toute interprétation (`git`, `gh api`, arbres Git récursifs).
2. Mesurer plutôt qu'estimer (nombre de lignes, d'octets, de titres Markdown par document).
3. Ne qualifier un fait de « vérifié » qu'après observation directe ; tout le reste est étiqueté « hypothèse » ou « non vérifié ».
4. Tester les limites de l'environnement avant de promettre des livrables (réseau, GPU, navigateur).
5. Consigner chaque accès, son date et son mode de preuve dans une annexe séparée.
6. Aucune écriture : les livrables d'audit sont produits hors dépôt pendant la Phase 0.

## 5. Résultats vérifiés

### 5.1 Dépôt produit `Stane316/mathverse`

- Public, créé le 2026-10-17, **1 commit** (`bdba473`), branche par défaut `main`, 0 étoile, 0 fork.
- Contenu : **2 documents Markdown** dans un dossier `Equations Mathématiques/` (nom avec espace et accent) :
  - `equations_courbes_mathematiques.md` (18 654 o, 27 sections) — panoplie de courbes « artistiques » : cœur paramétrique/implicite/polaire, spirale logarithmique, papillon de Clifford/Fay, rose de Rhodonea, lemniscate de Bernoulli, cardioïde, astroïde, deltoïde, épicycloïde/hypocycloïde, Lissajous, spirales d'Archimède/Fermat/lituus, folium de Descartes, néphroïde, limaçon, **superformula**, courbes harmoniques, trèfles, nautile, étoile de mer, fleur de vie.
  - `equations_courbes_animees_v2.md` (21 505 o, 14 sections) — mêmes familles orientées animation : trois niveaux d'animation (manuelle, automatique, temporelle), vocabulaire (pulsation, rotation, oscillation, déphasage, morphing, tracé progressif), méthode d'animation en 4 étapes, hypotrochoïde/épitrochoïde, conchoïde, cissoïde, strophoïde, courbe du diable, nœud de trèfle, superformula animée, Lissajous animées, **et des sections outillage : Desmos, GeoGebra, p5.js, Manim Community, Wolfram Alpha, Matplotlib**.
- **Valeur :** ces deux documents sont une matière première réelle pour la famille « courbes et surfaces paramétriques », avec équations, paramètres et plages de variation — exactement le niveau « équations + paramètres » exigé par le cahier des charges.
- **Signaux faibles détectés :** 63 marqueurs de citation non résolus de la forme `[web:31]`…`[web:58]` (39 dans la v2, 24 dans le v1) — trace d'une rédaction assistée par recherche web non sourcée. Ces renvois ne pointent vers aucune bibliographie présente dans le dépôt : la traçabilité des affirmations sur les logiciels (Desmos, GeoGebra, p5.js…) est donc **non vérifiée à ce stade**.

### 5.2 Dépôt de connaissances `Stane316/my-own-connaissance`

- Public, **1 commit**, 1,9 Mio, **29 fichiers `.md`**, **aucun fichier de code, aucune image, aucune donnée**.
- Deux collections : `Maths-vers-Informatiques/` (document maître + 20 documents de domaine) et `Ai Technical Litteracy/` (8 documents : ingénierie web, UI/UX, cybersécurité, SEO & performance, IA/ML, produit & start-up, branding, architecture & systèmes).
- Couverture A–U : **A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, U présents — T absent** (alors que décrit au §7.14 du maître).
- Hétérogénéité structurelle forte :
  - 17 documents bien structurés (130 à 380 titres Markdown, plans numérotés, sections « prédisposition d'intégration », « cartographie », « vocabulaire », familles de notions).
  - **4 documents sans aucun titre Markdown** : `A` (maître logique), `B` (théorie des nombres), `C` (algèbre linéaire), `D` (géométrie computationnelle). Le contenu existe mais apparaît aplati (titres convertis en texte), ce qui empêche la génération automatique d'un index fiable pour ces domaines.
- Le document maître énonce explicitement et honnêtement sa limite : « Ce document constitue une carte d'orientation. Il ne constitue pas une preuve que chaque notion mentionnée est intégralement développée dans les documents A à U. »
- Documents les plus volumineux et *a priori* les plus exploitables pour les cinq familles de composants prioritaires : **K** (fractales, chaos, systèmes dynamiques — 4 315 lignes, plan détaillé : géométrie fractale, systèmes itératifs, fractales complexes, attracteurs, bifurcations, bruit procédural, génération procédurale, simulation, rendu et interaction), **D** (géométrie computationnelle), **C** (algèbre linéaire), **L** (analyse numérique : erreurs, stabilité, conditionnement, convergence), **N** (transformées : Fourier, convolution, échantillonnage, aliasing), **I** (calcul différentiel), **G** (probabilités), **M** (théorie de l'information).

### 5.3 Environnement et limites

- Réseau sortant du sandbox limité à `github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org`. Contournement validé pour la veille : les outils `fetch_page` et `web_search`.
- **Pas de GPU, pas de navigateur installé, 2 vCPU / 3,8 Gio.** Toute affirmation de performance GPU dans ce contexte serait une fabrication. Le protocole de benchmark devra être exécuté sur des machines cibles documentées (ou en CI avec runners standard), pas ici.
- Droits du token GitHub : *admin* sur les deux dépôts. Le workflow imposé (jamais de `main`, jamais de PR, branche dédiée) est **techniquement applicable** et sera respecté.

### 5.4 Disponibilité des noms (sonde du 2026-10-17)

- Libres : `mathverse` (npm), `matheon` (npm, PyPI, GitHub), `mathverse-core`, `create-mathverse`.
- Pris : `mathverse` sur **PyPI** ; « MathVerse » comme **benchmark universitaire** (ECCV 2024, dépôt MIT, 184 ★) et comme **jeu de données Hugging Face** `AI4Math/MathVerse`.
- Homonyme concurrent-adjacent : `sadeepas/-MathVerse-An-Interactive-Suite-of-Mathematical-Web-Applications` (HTML/JS, 2 ★, sans licence) — suite d'applications web mathématiques interactives (graphiqueur multi-mode, simulateur de probabilités…).

## 6. Hypothèses et inférences

- **Hypothèse H1 :** les différences de structure entre documents (titres présents/absents) résultent d'un export hétérogène (copier-coller depuis un traitement de texte ou un format riche) plutôt que d'un choix éditorial. *Inférence*, à confirmer en Phase 1 par inspection du contenu de A/B/C/D.
- **Hypothèse H2 :** les deux documents du dépôt produit ont été rédigés (au moins en partie) avec l'assistance d'un outil de recherche web, d'où les marqueurs `[web:n]`. *Inférence* fondée sur la forme des marqueurs ; la vérification du fond (exactitude des affirmations sur Desmos/GeoGebra/p5.js/Manim) est reportée en Phase 1.
- **Hypothèse H3 :** les 8 documents `Ai Technical Litteracy` sont susceptibles d'alimenter directement la documentation produit (DX, performance web, accessibilité, architecture, SEO du site de découverte). *Inférence* fondée sur leurs titres ; contenu non encore audité.
- **Non vérifié à ce stade :** la qualité mathématique réelle (exactitude des équations, présence d'hypothèses et de limites) de chaque document ; la cohérence entre les domaines ; la présence d'algorithmes implémentables et de jeux de tests.

## 7. Lacunes et points non vérifiés

1. **Aucune licence** sur les deux dépôts (risque juridique et de positionnement « open source »).
2. **Domaine T manquant** (théorie des jeux) — annoncé, non écrit.
3. **Structure perdue pour A, B, C, D** — à confirmer par lecture, puis à corriger (sur votre autorisation).
4. **Traçabilité non établie** des deux documents du dépôt produit (marqueurs `[web:n]` orphelins).
5. **Contenu non audité** : aucun document n'a encore été évalué sur le fond (exactitude, hypothèses, limites, algorithmes, exemples).
6. **Dépôt produit sans socle technique** : pas de README, pas de `.gitignore`, pas de convention, pas de structure de répertoires, nom de dossier avec espace et accents.
7. **Impossibilité de mesurer ici** les performances GPU/WebGL/WebGPU ; à organiser autrement.
8. **Plateformes tierces non encore étudiées** : l'accès est confirmé, l'étude elle-même commence en Phase 2.

## 8. Risques et décisions à prendre

| # | Risque | Gravité | Décision attendue |
|---|---|---|---|
| R1 | Absence de licence : réutilisation et contribution bloquées juridiquement | **Haute** | Choisir une licence (produit) et clarifier la licence des connaissances |
| R2 | Collision du nom « MathVerse » avec un benchmark connu et un paquet PyPI | **Haute** | Arrêter un nom de travail et le figer dans une variable, pas en dur |
| R3 | Structure perdue de A/B/C/D → indexation automatisée impossible | Moyenne | Autoriser une restructuration (titres) après Phase 1 |
| R4 | Promesse de performance non mesurable dans ce sandbox | Moyenne | Valider un protocole de benchmark exécuté hors sandbox / en CI |
| R5 | Marqueurs `[web:n]` : affirmations non sourcées dans la documentation produit | Moyenne | Décider d'une règle de citation et d'un contrôle de traçabilité |
| R6 | Dépôt de connaissances = 1 seul commit : aucun historique, aucune sauvegarde | Moyenne | Définir une stratégie de sauvegarde avant toute modification |
| R7 | Confusion des rôles entre les deux dépôts (code vs documentation) | Moyenne | Trancher le mécanisme de liaison (Phase 3) |

## 9. Recommandations argumentées

Classement par **impact × urgence × coût × risque × dépendance**.

| # | Recommandation | Impact | Urgence | Coût | Risque | Dépendance |
|---|---|---|---|---|---|---|
| C1 | **Geler le nom dans une variable de configuration** (`PROJECT_CODENAME`) et utiliser un jeton neutre (`« le projet »`) dans toute la documentation produite avant arbitrage | Élevé | Immédiate | Nul | Nul | Aucune |
| C2 | **Traiter la licence en premier livrable juridique** : MIT (simple, permissif, compatible écosystème npm) pour le code produit ; CC BY-SA 4.0 ou CC BY-NC-SA pour les documents de connaissances ; `LICENSE` + en-têtes + politique de contribution | Élevé | Immédiate | Faible | Faible | Votre arbitrage |
| C3 | **Lancer la Phase 1 sur les domaines à rendement immédiat** (K, D, C, L, N, I, G) puis étendre | Élevé | Haute | Moyen | Faible | Aucune |
| C4 | **Instrumenter la lecture du dépôt de connaissances** (script d'extraction : titres, équations LaTeX, paramètres, algorithmes) plutôt que de relire 80 000 lignes à la main | Élevé | Haute | Moyen | Faible | Aucune |
| C5 | **Définir le protocole de benchmark dès la Phase 3**, avec exécution hors sandbox (votre machine + CI), jamais de seuils arbitraires | Élevé | Moyenne | Moyen | Moyen | C3 |
| C6 | **Ne pas créer de dépendance technique entre les dépôts avant arbitrage** (ni sous-module, ni copie) : commencer par des références documentées + un index généré | Moyen | Moyenne | Faible | Faible | Aucune |
| C7 | **Normaliser l'arborescence du dépôt produit** (`kebab-case`, anglais ou français assumé, `docs/`, `packages/`, `apps/`) au moment de la construction des fondations | Moyen | Basse | Faible | Faible | Validation des fondations |

**Recommandation transverse :** conserver, pour chaque livrable d'audit, la distinction explicite *vérifié / hypothèse / non vérifié*, et horodater chaque observation. C'est la seule façon de répondre à l'exigence « ne jamais transformer une hypothèse en fait » à l'échelle de 29 documents et d'une veille multi-plateformes.

## 10. Critères de validation de la Phase 0

| Critère | État |
|---|---|
| URL fournies vérifiées | ✅ les deux dépôts existent et sont accessibles |
| Dépôts existants distingués de ceux à créer | ✅ aucun dépôt à créer ; un éventuel renommage reste un choix, pas une nécessité |
| Permissions et capacités réelles identifiées | ✅ admin sur les deux dépôts ; limites réseau et matériel documentées |
| Outils de recherche, navigation, scraping, analyse identifiés | ✅ `fetch_page`, `web_search`, API GitHub, clone git, curl npm/PyPI ; limites notées |
| Ressources inaccessibles signalées | ✅ voir §3 et §5.3 |
| Aucune modification effectuée | ✅ 0 commit, 0 push, 0 branche créée ; livrables écrits hors dépôt |
| Plans Phase 1 et Phase 2 définis | ✅ voir §13 |

**Critère non satisfait :** la mesure de performance n'est pas réalisable dans cet environnement (§5.3) — elle est reportée et devra être organisée autrement.

## 11. Fichiers créés ou modifiés

| Fichier | Emplacement | Nature |
|---|---|---|
| `PHASE-0-RAPPORT-AUDIT-INITIAL.md` | `/home/user/audit/` (hors dépôt) | présent rapport |
| `annexes/A0-inventaire-acces-et-preuves.md` | `/home/user/audit/` | inventaire chiffré, journal des opérations |
| `_audit/connaissance/` | `/home/user/` | clone en lecture seule du dépôt de connaissances (non versionné, hors dépôt produit) |

**Aucun fichier du dépôt `mathverse` n'a été créé, modifié ou supprimé.**

## 12. Tests exécutés et résultats

| Test | Commande / méthode | Résultat |
|---|---|---|
| Existence et métadonnées des dépôts | `gh api repos/Stane316/{mathverse,my-own-connaissance}` | 200 ; publics ; `license: null` ; droits admin |
| Arborescences complètes | `gh api …/git/trees/main?recursive=1` | mathverse : 2 blobs ; connaissances : 2 arbres + 29 blobs |
| Clone du dépôt de connaissances | `git clone --depth 1` | OK, 29 fichiers, 1 912 005 octets |
| Mesure de structure | `wc -lc`, `grep -c '^#'` par fichier | 4 documents à 0 titre (A, B, C, D) ; les autres 130–380 |
| Présence du domaine T | comparaison arbre Git ↔ §7.14 du maître | **absent** |
| Marqueurs de citation orphelins | `grep -o '\[web:[0-9]*\]'` | 63 marqueurs (39 + 24), aucune bibliographie associée |
| Accès réseau sortant | `curl` sur 10 hôtes | 5 autorisés (200/301), 5 bloqués (000) |
| Accès aux sites de référence | `fetch_page reactbits.dev`, `fetch_page uiverse.io` | 200 — veille réalisable |
| Disponibilité des noms | sondes npm / PyPI / GitHub + `web_search` | `matheon` libre partout ; `mathverse` libre sur npm, pris sur PyPI, occupé par un benchmark ECCV 2024 |
| Capacité de benchmark | `ls /dev/dri`, recherche de navigateurs, `nproc`, `free` | **pas de GPU, pas de navigateur**, 2 vCPU / 3,8 Gio |

## 13. Prochaine étape proposée

### 13.1 Plan d'audit documentaire — Phase 1

**Question à résoudre :** que contient réellement la collection A–U, qu'est-ce qui est utilisable pour produire des composants expliquables, et où sont les lacunes ?

**Sources prioritaires :** le clone local `/home/user/_audit/connaissance` (source unique de vérité, horodatée) ; le dépôt produit pour ses deux documents d'équations.

**Méthode :**
1. Script d'extraction par document : titres, définitions, équations (LaTeX `\(…\)`, `\[…\]`), théorèmes, algorithmes (blocs ` ``` `), exemples, sections « limites / hypothèses », renvois inter-domaines.
2. Fiche par domaine, sur un modèle constant : objectif, couverture réelle, notions clés, équations exploitables, paramètres, algorithmes, exemples, limites, fiabilité et traçabilité, liens aux familles de composants, niveau de maturité, besoins de documentation complémentaire.
3. Index structuré (JSON/YAML) : **notion → modèle → équations → paramètres → algorithme → moteur de calcul → rendu → composant potentiel → tests et validation**, avec dépendances, sources et maturité.
4. Matrice de couverture A–U (présent / partiel / manquant) et cartographie des lacunes.
5. Relevé des incohérences et propositions de correction, **soumis à votre approbation** avant toute modification du dépôt de connaissances.

**Éléments de preuve attendus :** extraits cités avec chemin de fichier et numéro de ligne ; comptages reproductibles ; distinctions *vérifié / hypothèse / non vérifié*.

**Critères de validation :** les 21 domaines ont une fiche ; l'index couvre les 5 familles prioritaires ; chaque lacune est documentée avec son type (absence, imprécision, incohérence, non-traçabilité) ; aucune modification du dépôt source.

**Critères d'arrêt :** fiches complètes **ou** épuisement des documents accessibles **ou** impossibilité d'accès — avec, dans ce dernier cas, liste explicite des inconnues restantes.

**Estimation :** 21 fiches + 8 documents de littératie technique si vous les incluez dans le périmètre (question 3 ci-dessous).

### 13.2 Plan de recherche concurrentielle — Phase 2

**Question à résoudre :** existe-t-il déjà une plateforme réunissant composants visuels + explication mathématique + prompts + CLI, et quelles sont les places libres ?

**Méthode :** pour chaque plateforme — `fetch_page` (parcours, documentation, page d'un composant), API GitHub (licence, structure, release, contribution), clone si le dépôt est public et la licence le permet (ex. `DavidHDev/react-bits`), `web_search` pour les éléments non observables directement.

**Périmètre prévu :** React Bits ; Uiverse (+ `uiverse-io/galaxy`) ; shadcn/ui (mécanique de registre, reprise par React Bits) ; p5.js ; Manim Community ; GeoGebra (apps + intégration) ; three.js / react-three-fiber ; Aceternity UI, Magic UI ; Framer Motion / Motion ; D3 / Observable Plot ; MathBox ; JSXGraph ; CindyJS ; Desmos (API d'intégration) ; Shadertoy / ShaderFrog ; Motion Canvas ; projets homonymes détectés (§5.4) ; outils d'exploration scientifique (Wolfram, Cocalc…). La liste restera ouverte aux découvertes.

**Fiche type par plateforme (16 champs) :** présentation et positionnement ; fonctionnalités ; parcours utilisateur ; architecture technique observable ; mode de distribution ; prévisualisation et personnalisation ; stratégie documentaire ; modèle de contribution ; licences et contraintes de réutilisation ; points forts ; limites ; éléments non vérifiés ; idées à retenir ; erreurs à éviter ; opportunités de différenciation ; sources, dates et preuves.

**Livrables :** registre des plateformes, fiches, comparaison transversale, synthèse des différenciateurs, et registre des licences (ce qui est réutilisable, ce qui ne l'est pas, et sous quelles conditions).

**Garde-fous :** pas de contournement d'accès ; pas d'extraction de secrets ni de contenu privé ; respect des limites de débit ; pas de copie massive de code tiers ; chaque fiche horodatée avec le mode d'accès utilisé.

## 14. Points exigeant votre approbation

1. **Le nom de travail** — arbitrage entre MATHVERSE, MATHÉON ou un autre nom, au vu de la collision documentée (§5.4). Tant que ce n'est pas tranché, tout sera rédigé avec un jeton neutre.
2. **L'emplacement des livrables d'audit** — aujourd'hui hors dépôt (`/home/user/audit/`), par respect de la règle « aucune modification pendant l'audit initial ». Si vous préférez qu'ils vivent dans le dépôt produit sur la branche de travail (`docs/audit/`), dites-le : je les déplacerai au prochain tour, sans toucher à `main`.
3. **Le périmètre documentaire de la Phase 1** — limité aux 21 documents mathématiques, ou étendu aux 8 documents de littératie technique (web, UI/UX, performance, architecture, produit, IA/ML, sécurité, branding), utiles pour la partie « site de découverte », « DX » et « documentation ».
4. **La stratégie de licence** (recommandation C2) — à confirmer avant la construction des fondations, car elle conditionne les en-têtes de fichiers, la politique de contribution et la réutilisation des références étudiées.
