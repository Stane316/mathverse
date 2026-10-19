# A9 — PLAN DE LA PHASE 2 : ÉTUDE D'ÉCOSYSTÈME ET DE CONCURRENCE

**Date d'ouverture :** 2026-10-19
**Statut :** collecte **complète** (35 plateformes, 11 fiches). **Les cinq livrables sont établis.**
L'étude de demande (R3) est **engagée** — `A10-etude-de-demande.md`. La licence du corpus source
fait l'objet d'une **proposition soumise** — `../decisions/0002-licence-du-corpus-source.md`.
Reste quatre points ouverts nécessitant une qualification juridique (§7.4).
**Décision préalable :** le chantier de restauration a été clos sur un périmètre réduit par le
porteur le 2026-10-19 — voir `../restauration/CLOTURE-CHANTIER.md`. Cette clôture lève la règle
du 2026-10-18 qui subordonnait l'ouverture de la phase 2 à l'achèvement du chantier.

---

## 1. Question à résoudre

Reprise du §13.2 du rapport de phase 0 :

> Existe-t-il déjà une plateforme réunissant **composants visuels + explication mathématique +
> prompts + CLI**, et quelles sont les places libres ?

La question porte sur une **conjonction** de quatre attributs, pas sur chacun séparément. Des
plateformes excellent dans l'un ou l'autre ; c'est leur réunion qui est en cause.

## 2. Pourquoi cette question conditionne la suite

Le cahier des charges impose, pour chaque composant livré, seize attributs — dont une explication
mathématique, les équations et hypothèses, un prompt IA réutilisable (13 champs), une commande
CLI, des tests et des mesures de performance. Ce couplage est **la thèse de Mathemirum**. Si une
plateforme le réalise déjà et qu'elle est libre, la construction doit s'y greffer plutôt que la
refaire. Si elle existe mais n'est pas libre, le périmètre se resserre. Si elle n'existe pas, la
thèse tient — mais il faut alors vérifier qu'elle n'est pas vide pour une raison.

## 3. Méthode

Reprise sans modification de celle du §13.2 du rapport de phase 0 :

| Moyen | Emploi |
|---|---|
| `fetch_page` | parcours du site, documentation, page d'un composant |
| API GitHub (`api.github.com`) | licence, étoiles, langue, dernière activité, structure du dépôt |
| Clone | **uniquement** si le dépôt est public **et** que la licence le permet |
| `web_search` | éléments non observables directement (modèle économique, traction, gouvernance) |

**Garde-fous, inchangés :** pas de contournement d'accès ; pas d'extraction de secrets ni de
contenu privé ; respect des limites de débit ; pas de copie massive de code tiers ; chaque fiche
horodatée, avec le mode d'accès employé et la source précise.

**Règle de preuve, reprise de A6 §5 :** toute affirmation s'appuie sur une mesure ou un extrait
situé. Ce qui n'a pas été lu est marqué ⚠️ ; ce qui est absent est marqué ❌. Aucune case n'est
remplie par inférence silencieuse.

## 4. Périmètre

Reprise de la liste du §13.2, restant **ouverte aux découvertes** :

- **Composants web :** React Bits · shadcn/ui · Magic UI · Aceternity UI · Uiverse (+ `galaxy`) ·
  Motion (ex-Framer Motion) · Motion Primitives
- **Moteurs et mathématiques :** p5.js · Manim (3b1b et communauté) · three.js /
  react-three-fiber · D3 · Observable Plot · MathBox · JSXGraph · CindyJS · Desmos (API
  d'intégration) · GeoGebra
- **Création et shaders :** Shadertoy · ShaderFrog · Motion Canvas
- **Génération par IA :** Math-To-Manim · Manimly · Manimator · MathViz-E · ExcaliMath
- **Exploration scientifique :** Wolfram · Cocalc
- **Homonymes détectés en phase 0 :** `ZrrSkywalker/MathVerse` (benchmark ECCV-2024) ·
  `sadeepas/-MathVerse-An-Interactive-Suite-of-Mathematical-Web-Applications`

## 5. Fiche type par plateforme — 16 champs

Inchangée par rapport au §13.2 :

1. présentation et positionnement · 2. fonctionnalités · 3. parcours utilisateur ·
4. architecture technique observable · 5. mode de distribution · 6. prévisualisation et
personnalisation · 7. stratégie documentaire · 8. modèle de contribution ·
9. **licences et contraintes de réutilisation** · 10. points forts · 11. limites ·
12. **éléments non vérifiés** · 13. idées à retenir · 14. erreurs à éviter ·
15. opportunités de différenciation · 16. **sources, dates et preuves**.

## 6. Livrables attendus

1. **Registre des plateformes** — avancé : `annexes/A9-registre-plateformes.md`
2. **Fiches détaillées**, une par plateforme, selon les 16 champs — **10 rédigées** dans
   `fiches-phase-2/` : F01 React Bits, F02 shadcn/ui, F03 Math-To-Manim, F04 Aceternity UI,
   F05 Uiverse, F06 Desmos, F07 GeoGebra, F08 Shadertoy, F09 Wolfram et CoCalc,
   F10 MathVerse (sadeepas)
3. **Comparaison transversale** — **établie** : `annexes/A9-comparaison-transversale.md`.
   18 attributs × 27 plateformes, plus la question des quatre attributs et la synthèse par
   attribut
4. **Synthèse des différenciateurs** — **établie** : `annexes/A9-synthese-differenciateurs.md`.
   Sept différenciateurs retenus (avec preuve et coût), **neuf revendications écartées** parce que
   déjà occupées, et le risque central énoncé
5. **Registre des licences** — **établi** : `annexes/A9-registre-des-licences.md`. 35 plateformes
   classées selon quatre statuts (base / dépendance / référence / interdit), avec quatre points
   ouverts à qualifier. C'est le livrable qui alimentera la décision de licence, reportée par le
   porteur à l'après-phase-2

## 7. Premiers résultats vérifiés

Les données figurent dans `annexes/A9-registre-plateformes.md`. Deux constats se dégagent
d'ores et déjà.

### 7.1 Le concurrent le plus direct n'est pas open source

**React Bits** (49 719 ★, le plus gros acteur du secteur) est sous **MIT + Commons Clause**. Ce
n'est pas une licence open source : elle interdit de redistribuer les composants, de les porter,
et d'offrir un service « substantiellement similaire ». La clause vise **précisément** le modèle
d'une bibliothèque de composants distribuée sous registre.

Ce n'est pas un obstacle majeur — React Bits n'apporte aucune explication mathématique, et ce que
Mathemirum veut en reprendre est la *mécanique*, pas le code. Or cette mécanique est ouverte :
**shadcn/ui est sous MIT (125 966 ★)**.

⚠️ **Rectification du 2026-10-19.** Le rapport de phase 0 décrivait React Bits comme reposant sur
le registre shadcn. L'observation du dépôt corrige : React Bits construit sa distribution avec
**jsrepo** et l'adaptateur **`@jsrepo/shadcn`**. Il émet au format shadcn, mais par un autre
outil. La conclusion de fond tient — la mécanique est ouverte —, pas le chemin de dépendance
annoncé. Détail en `annexes/A9-registre-plateformes.md` §1.

### 7.3 ⚠️ Le constat dominant de la deuxième vague est juridique

Sur les sept plateformes étudiées en profondeur, **six ne peuvent pas servir de base** à un projet
de bibliothèque ouverte : Aceternity (redistribution interdite), Desmos (gratuit = non commercial),
GeoGebra (quatre régimes, dont deux non commerciaux), Shadertoy (CC BY-NC-SA par défaut), Wolfram
(propriétaire), MathVerse/sadeepas (aucune licence). Une seule est ouverte sans réserve :
**Uiverse**, dont le dépôt miroir est toutefois inactif depuis deux ans.

Ce n'est pas un obstacle à la thèse — c'est **une confirmation qu'elle vaut la peine d'être
instruite** : le territoire n'est pas occupé par des acteurs libres, mais par des acteurs fermés ou
ambiguës. Deux échappatoires identifiées et non encore vérifiées : **Shaders** (`shaders.com`,
MIT annoncé) et la clause Wolfram « open-source projects approved by Wolfram ».

⚠️ **Les licences relevées proviennent de pages publiques d'éditeurs et de métadonnées GitHub.**
Aucune n'a été vérifiée par un conseil juridique, et plusieurs sont susceptibles d'avoir changé.

### 7.4 Troisième vague : Shaders, GLSL Sandbox, CoCalc

- **Shaders** (`shader-effects-inc/shaders`, **MIT**, 5 106 ★, WebGPU, 200+ composants, cinq
  frameworks, CLI et MCP) — ouvert depuis le **6 octobre 2026**, soit treize jours avant
  l'observation. C'est le concurrent le plus sérieux sur le plan technique. ⚠️ **Mais un conflit est
  documenté** : son contrat de plateforme (v1.7, 3 août 2026, antérieur à l'ouverture) déclare la
  technologie « propriété exclusive » et interdit de redistribuer « le code créé avec Shaders ».
  **Point ouvert n°1.**
- **CoCalc** — ⚠️ **licence lue : MS-RSL (Microsoft Reference Source License)**. Ce n'est pas une
  licence open source : le code est consultable **à titre de référence uniquement**, et
  **la distribution est expressément exclue**. Correction apportée à la fiche F09.
- **GLSL Sandbox** — MIT annoncé pour la plateforme, mais ⚠️ **aucune licence par défaut pour les
  shaders déposés** : même problème que Shadertoy. Source indirecte, à confirmer.
- **Découverts en cours de route** : **Paper Shaders** (`paper-design/shaders`, **Apache 2.0**,
  usage commercial sans attribution) et **OpenShaders** (`openshaders`, MIT, par l'auteur de React
  Bits — avec là encore une licence laissée au choix de chaque créateur).

### 7.5 Ce que dit le registre des licences

Sur 35 plateformes, **9 relèvent d'un régime fermé ou restrictif** — et ce sont souvent les plus
visibles. Trois mécanismes de présentation trompeuse sont documentés : le titre de licence qui
rassure (« MIT + Commons Clause »), l'agrégateur qui répète sans vérifier (Aceternity annoncé MIT
par une dizaine d'annuaires), et le dépôt public sans licence (GeoGebra, `sadeepas`).

**Résultat structurant :** une seule plateforme du secteur est à la fois ouverte, massive et sans
restriction de redistribution — **shadcn/ui (MIT)**, d'où vient la mécanique de registre que toutes
les autres imitent. **La couche infrastructurelle est libre ; la couche catalogue ne l'est pas.**

### 7.2 Le courant « IA + maths » sort de la vidéo

Sept projets de génération mathématique par IA ont été relevés. **Tous produisent une vidéo
(MP4/WebM/GIF)** ou un graphe figé, aucun ne produit un composant web réutilisable. Les deux
exceptions partielles confirment la règle : ExcaliMath est bien un composant React mais c'est un
tableau blanc, et `dynamic-manim-components` vise bien une bibliothèque de composants mais dans
l'écosystème Python/Manim.

⚠️ **Il s'agit d'un constat sur 24 plateformes et une requête, pas d'une preuve d'absence.**
Voir §8.

### 7.6 Ce que révèle la comparaison transversale

La matrice 18 attributs × 27 plateformes fait apparaître un motif net, et il ne concerne pas la
technique :

- **Tout ce qui relève de la mise à disposition est couvert** — nom, description, catégorie, aperçu,
  code source, dépendances, installation, exemples d'intégration. C'est acquis partout.
- **Tout ce qui relève de la preuve est vide** — explication mathématique, équations et hypothèses,
  mesures de performance, limites connues. **La case « limites connues » est la plus vide de la
  matrice**, et celle des « équations et hypothèses » est vide **sans une seule exception**.

**Le résultat le plus net porte sur la question des quatre attributs (§1).** Aucune plateforme ne
réunit composants visuels + explication mathématique + prompts + CLI. **Mais les deux plus proches
sont complémentaires, et leur complémentaire est la thèse même de Mathemirum :** Shaders a les
composants, les prompts et la CLI — il lui manque l'explication mathématique, et c'est son seul
manque ; Math-To-Manim a l'explication, les prompts et la CLI — il lui manque la sortie composant.

⚠️ **Ce constat ne vaut pas preuve d'absence**, et une case vide peut être vide par choix rationnel :
documenter les équations et les limites d'un composant coûte cher. Que personne ne le fasse peut
signifier une opportunité — ou un marché qui ne le valorise pas. Question non instruite (R3).

### 7.7 Ce que dit la synthèse des différenciateurs

Sept différenciateurs retenus, chacun adossé à une case vide documentée : les équations et
hypothèses par composant (D1) ; le classement tripartite assumé (D2) ; les limites connues publiées
(D3) ; les performances mesurées avec méthode (D4) ; la clarté de licence (D5) ; le registre à
champs étendus (D6) ; la boucle prompt → composant → test (D7).

**Neuf revendications ont été écartées**, et c'est aussi instructif : le nombre de composants, la
beauté visuelle, le WebGPU, le caractère open source, la CLI, l'intégration aux agents IA, le
multi-framework, l'éditeur visuel, la profondeur mathématique de l'outil. **Toutes sont occupées
par des acteurs mieux dotés.** Sur toute la couche technique et distributive, Mathemirum arriverait
après les autres.

⚠️ **Le risque central est énoncé sans détour dans le livrable :** les sept différenciateurs retenus
sont **tous des centres de coût**, et aucun des 27 acteurs étudiés ne les engage. Soit personne n'a
voulu payer, soit le marché ne les valorise pas. **Ces deux hypothèses ne sont pas départagées par
cette phase.**

### 7.8 Ce que dit l'étude de demande (R3)

⚠️ **Le résultat n'est pas celui qu'on espérait, et il est rapporté tel quel.**

- ✅ **La documentation est le premier critère de choix** d'un paquet, mesuré à **93 % d'accord**
  dans une étude universitaire sur la sélection de paquets npm.
- ✅ **« L'aptitude à l'IA » est un critère apparu en 2026** : serveur MCP, `llms.txt`,
  documentation lisible par un assistant.
- ✅ **La douleur n°1 des développeurs de shaders est le débogage et le profilage**, pas le manque
  d'effets (enquête Khronos 2026, 400+ répondants : 53 % en top 3 ; 64 % adaptent des shaders entre
  plateformes).
- ❌ **Mais aucun des ~20 guides de choix de bibliothèques de composants consultés ne mentionne
  l'explication mathématique, les équations, les hypothèses ou le domaine de validité.** Pas un seul.

**La demande pour la couche de preuve est donc adjacente et indirecte, pas directe.** Elle existe
dans le discours et dans des critères voisins, pas comme critère de choix formulé.

**Le levier le plus solide n'est pas la preuve pour elle-même, mais la preuve rendue lisible par une
machine** : c'est là qu'elle rencontre un critère de choix observé en 2026. Recommandation R3.2.

⚠️ L'étude est une **première passe** : trois requêtes, sources majoritairement secondaires, aucun
volume de recherche mesuré, aucune disposition à payer évaluée.

## 8. Hypothèses — à confirmer, non à tenir pour acquises

⚠️ **Ce qui suit est une hypothèse.** Elle ne sera étayée qu'après les fiches détaillées et
plusieurs requêtes indépendantes.

1. **L'espace se diviserait en deux territoires disjoints** : des bibliothèques de composants
   web sans profondeur mathématique, et des moteurs mathématiques qui sortent de la vidéo.
   L'intersection — composant web portant son explication mathématique, ses équations, ses
   hypothèses, son prompt et sa CLI — serait libre. **Précision apportée par la matrice (§7.6) :
   la ligne de partage ne passe pas entre le visuel et le mathématique, mais entre la mise à
   disposition et la preuve.**
2. **Risque attaché à cette hypothèse :** une place peut être libre **pour une raison**. Soit la
   demande est faible, soit la combinaison coûte plus cher à maintenir qu'elle ne rapporte.
   **Cette question n'a pas encore été instruite et conditionne la valeur de la thèse.**
3. **Aucune preuve d'absence n'est établie.** Le cahier des charges interdit de revendiquer
   l'exhaustivité ; une recherche sans résultat n'est pas une démonstration.

## 9. Recommandations

Classées selon les critères du §15 du cahier des charges : **impact, urgence, coût, risque,
dépendance**.

| # | Recommandation | Impact | Urgence | Coût | Risque | Dépendance |
|---|---|---|---|---|---|---|
| **R1** | Lever les **quatre points ouverts du registre des licences** (§7.4) : confirmation écrite de Shader Effects, qualification de la « configuration exportable » face à la clause React Bits, portée de la co-propriété GeoGebra, procédure d'approbation Wolfram | **élevé** | **haute** | faible | **moyen** | aucune |
| **R2** | Rédiger la fiche licence de React Bits en priorité, et qualifier le périmètre exact de la clause Commons Clause vis-à-vis d'une « configuration exportable » par composant | **élevé** | **haute** | faible | **moyen** (lecture juridique) | aucune |
| **R3** | ~~Instruire la question de la demande~~ — **engagée le 2026-10-19** sur décision du porteur. Première passe livrée : `A10-etude-de-demande.md`. **Résultat nuancé** : documentation et IA sont des critères mesurés, l'explication mathématique n'apparaît dans aucun guide de choix. Voir §7.8 | — | — | — | — | — |
| **R6** | ~~Registre des licences~~ — **fait** (livrable 5) | — | — | — | — | — |
| **R7** | Vérifier **Paper Shaders** (Apache 2.0) et **OpenShaders** (MIT) : deux candidats libres apparus en cours de collecte, non encore étudiés en détail | **élevé** | moyenne | faible | faible | aucune |
| **R4** | Vérifier les homonymes `MathVerse` : ils occupent le nom et le sujet | moyen | moyenne | faible | faible | aucune |
| **R5** | Traiter séparément les deux licences copyleft faible relevées (p5.js LGPL-2.1, JSXGraph LGPL-3.0) dans le registre des licences | moyen | basse | faible | faible | R1 |

## 9. Deux actions requises du porteur

### 9.1 Clarifier la licence du corpus source

⚠️ Le dépôt de connaissances `Stane316/my-own-connaissance`, d'où proviennent les équations et les
773 restaurations appliquées, est **public sans fichier LICENSE** (constat de phase 0). Publier un
composant Mathemirum dont l'explication mathématique en dérive, sans clarifier ce régime,
**reproduirait exactement le défaut critique chez GeoGebra et `sadeepas`**. → **Votre décision.**

### 9.2 Arbitrer la question du marché — **décidé le 2026-10-19**

Le porteur a choisi **d'instruire l'étude de demande (R3)**. Elle est engagée : `A10-etude-de-demande.md`.
Ses résultats (§7.8) sont nuancés et **ne valident pas la thèse sans réserve** : ils déplacent la
question vers l'aptitude à l'IA et la documentation plutôt que vers la preuve mathématique en soi.

## 10. Prochaine étape

Compléter la collecte (R1) puis rédiger les premières fiches selon les 16 champs, en commençant
par les trois plateformes dont la licence ou la mécanique sont structurantes pour Mathemirum :
**React Bits** (licence), **shadcn/ui** (mécanique de registre), **Math-To-Manim** (le plus
proche du couplage prompt + CLI + maths, malgré la sortie vidéo).

---

## 11. Références

- `../PHASE-0-rapport-audit-initial.md` §13.2 — plan de recherche concurrentielle d'origine
- `annexes/A9-registre-plateformes.md` — relevé des plateformes, avec provenance
- `../restauration/CLOTURE-CHANTIER.md` — clôture du chantier au périmètre réduit
- `../A6-plan-phase-1.md` §5 — règle de preuve appliquée aux fiches
- Cahier des charges §15 (structure des rapports en 14 points) et §16 (rapports de fin de phase)
