# A9 — PLAN DE LA PHASE 2 : ÉTUDE D'ÉCOSYSTÈME ET DE CONCURRENCE

**Date d'ouverture :** 2026-10-19
**Statut :** phase **ouverte**, collecte **largement avancée** (24 plateformes vérifiées, 3 fiches
rédigées).
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
2. **Fiches détaillées**, une par plateforme, selon les 16 champs — **3 rédigées** : React Bits
   (F01), shadcn/ui (F02), Math-To-Manim (F03), dans `fiches-phase-2/`
3. **Comparaison transversale** — tableau croisé attributs × plateformes — **non commencée**
4. **Synthèse des différenciateurs** — ce que Mathemirum peut revendiquer — **non commencée**
5. **Registre des licences** — ce qui est réutilisable, ce qui ne l'est pas, sous quelles
   conditions — **non commencé** ; c'est le livrable qui alimentera la décision de licence,
   reportée par le porteur à l'après-phase-2

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

### 7.2 Le courant « IA + maths » sort de la vidéo

Sept projets de génération mathématique par IA ont été relevés. **Tous produisent une vidéo
(MP4/WebM/GIF)** ou un graphe figé, aucun ne produit un composant web réutilisable. Les deux
exceptions partielles confirment la règle : ExcaliMath est bien un composant React mais c'est un
tableau blanc, et `dynamic-manim-components` vise bien une bibliothèque de composants mais dans
l'écosystème Python/Manim.

⚠️ **Il s'agit d'un constat sur 24 plateformes et une requête, pas d'une preuve d'absence.**
Voir §8.

## 8. Hypothèses — à confirmer, non à tenir pour acquises

⚠️ **Ce qui suit est une hypothèse.** Elle ne sera étayée qu'après les fiches détaillées et
plusieurs requêtes indépendantes.

1. **L'espace se diviserait en deux territoires disjoints** : des bibliothèques de composants
   web sans profondeur mathématique, et des moteurs mathématiques qui sortent de la vidéo.
   L'intersection — composant web portant son explication mathématique, ses équations, ses
   hypothèses, son prompt et sa CLI — serait libre.
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
| **R1** | Compléter la collecte (Aceternity UI, Uiverse site, Desmos, GeoGebra, Shadertoy, Wolfram, Cocalc) et rédiger la fiche du projet `sadeepas` — seul trouvé dont l'intitulé recouvre exactement l'objet visé | **élevé** | **haute** | faible | faible | aucune |
| **R2** | Rédiger la fiche licence de React Bits en priorité, et qualifier le périmètre exact de la clause Commons Clause vis-à-vis d'une « configuration exportable » par composant | **élevé** | **haute** | faible | **moyen** (lecture juridique) | aucune |
| **R3** | Instruire explicitement la question de la demande (§8.2) avant de conclure à une place libre | **élevé** | moyenne | moyen | faible | R1 |
| **R4** | Vérifier les homonymes `MathVerse` : ils occupent le nom et le sujet | moyen | moyenne | faible | faible | aucune |
| **R5** | Traiter séparément les deux licences copyleft faible relevées (p5.js LGPL-2.1, JSXGraph LGPL-3.0) dans le registre des licences | moyen | basse | faible | faible | R1 |

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
