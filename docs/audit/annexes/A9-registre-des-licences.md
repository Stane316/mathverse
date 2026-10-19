# A9 — REGISTRE DES LICENCES

**Livrable 5 de la phase 2**
**Date d'établissement :** 2026-10-19
**Objet :** consolider les onze fiches de plateforme en un **tableau opposable** — ce qui est
réutilisable, ce qui ne l'est pas, et sous quelles conditions.
**Portée :** 35 plateformes. ⚠️ **Ce registre est un document de travail, pas un avis juridique.**

---

## 1. Mode d'emploi — les quatre statuts

Une même plateforme peut être utilisable de trois manières distinctes, soumises à des régimes
différents. Les confondre est l'erreur la plus fréquente du secteur.

| Statut | Définition | Ce que ça engage |
|---|---|---|
| **BASE** | reprendre le code pour bâtir Mathemirum dessus, ou le redistribuer dans un registre | exige une licence **sans restriction de redistribution** |
| **DÉPENDANCE** | installer le paquet et l'appeler, sans le redistribuer | exige une licence **compatible** avec celle de Mathemirum |
| **RÉFÉRENCE** | lire le code ou les résultats pour comprendre, vérifier, comparer | exige seulement le **droit de lire** |
| **INTERDIT** | aucun des trois | — |

**Règle de lecture :** ⚠️ « utilisable en commercial » ne signifie jamais « redistribuable ». Ce
sont deux droits distincts, et seule la redistribution concerne une bibliothèque de composants.
C'est la confusion qui traverse React Bits, Aceternity et le contrat Shaders.

**Échelle de confiance :**

| Marque | Signification |
|---|---|
| ✅ | vérifié sur une source primaire (fichier de licence, page officielle de l'éditeur, API) |
| ⚠️ | vérifié mais **conditionnel**, **partiel**, ou **conflit documenté** — à qualifier avant usage |
| ❌ | exclu par le texte de la licence |

---

## 2. Tableau opposable

### 2.1 Licences ouvertes — réutilisables

| Plateforme | Licence | Base | Dép. | Réf. | Conditions et réserves | Fiche |
|---|---|:--:|:--:|:--:|---|:--:|
| **shadcn/ui** | MIT | ✅ | ✅ | ✅ | la **mécanique de registre** est le bien le plus réutilisable du secteur | F02 |
| **Shaders** (paquet npm) | MIT | ⚠️ | ✅ | ✅ | ⚠️ **conflit avec le contrat de plateforme v1.7** — voir §3.1 | F11 |
| **Paper Shaders** | Apache-2.0 | ⚠️ | ✅ | ✅ | usage commercial sans attribution ; ⚠️ périmètre non vérifié | F11 |
| **OpenShaders** | MIT | ⚠️ | ✅ | ✅ | ⚠️ les créateurs choisissent la licence de **leurs** shaders | F11 |
| **Magic UI** | MIT | ⚠️ | ✅ | ✅ | | — |
| **Motion** (ex-Framer) | MIT | ✅ | ✅ | ✅ | | — |
| **Motion Primitives** | MIT | ✅ | ✅ | ✅ | | — |
| **three.js** | MIT | ✅ | ✅ | ✅ | | — |
| **react-three-fiber** | MIT | ✅ | ✅ | ✅ | | — |
| **MathBox** | MIT | ✅ | ✅ | ✅ | ⚠️ inactif depuis 2023 | — |
| **CindyJS** | Apache-2.0 | ✅ | ✅ | ✅ | | — |
| **Motion Canvas** | MIT | ✅ | ✅ | ✅ | | — |
| **D3** | ISC | ✅ | ✅ | ✅ | | — |
| **Observable Plot** | ISC | ✅ | ✅ | ✅ | | — |
| **Math-To-Manim** | MIT | ⚠️ | ⚠️ | ✅ | sortie vidéo ; ⚠️ dépend d'API d'IA payantes | F03 |
| **ExcaliMath** | MIT | ⚠️ | ✅ | ✅ | tableau blanc, non une bibliothèque de composants | — |
| **MathViz-E** | MIT | ✅ | ✅ | ✅ | | — |
| **reactive-manim** | MIT | ✅ | ✅ | ✅ | écosystème Python | — |
| **manim-video-generator** | MIT | ✅ | ✅ | ✅ | | — |
| **Manimly** | MIT | ✅ | ✅ | ✅ | ⚠️ 0 étoile, traction nulle | — |
| **Manim** (communauté) | MIT | ⚠️ | ⚠️ | ✅ | Python, sortie vidéo | F03 |
| **3b1b/manim** | MIT | ⚠️ | ⚠️ | ✅ | Python, sortie vidéo | — |
| **MathVerse** (ZrrSkywalker) | MIT | ✅ | ⚠️ | ✅ | benchmark, hors sujet mais **occupe le nom** | — |
| **Uiverse** (dépôt galaxy) | MIT | ⚠️ | ⚠️ | ✅ | ⚠️ **vérifier élément par élément** ; dépôt inactif depuis 2 ans | F05 |
| **p5.js** | **LGPL-2.1** | ⚠️ | ✅ | ✅ | copyleft faible : contraintes en cas de modification ou de liaison statique | — |
| **JSXGraph** | **LGPL-3.0** | ⚠️ | ✅ | ✅ | copyleft faible, **plus strict** que LGPL-2.1 | — |

### 2.2 Licences fermées ou restrictives — non réutilisables comme base

| Plateforme | Licence | Base | Dép. | Réf. | Motif | Fiche |
|---|---|:--:|:--:|:--:|---|:--:|
| **React Bits** | MIT + **Commons Clause** | ❌ | ⚠️ | ✅ | redistribution, portage et service similaire **interdits** | F01 |
| **Aceternity UI** | licence propre | ❌ | ❌ | ⚠️ | redistribution interdite **même modifiée** ; dépôt public inexistant | F04 |
| **Shadertoy** | **CC BY-NC-SA 3.0** par défaut | ❌ | ❌ | ⚠️ | non commercial **et** viral ; l'absence d'en-tête vaut interdiction | F08 |
| **GeoGebra** | EUPL + non commercial + CC BY-NC-SA | ❌ | ⚠️ | ✅ | quatre régimes ; **co-propriété des productions** ; EUPL incompatible avec une licence permissive | F07 |
| **Desmos** | service, gratuit = non commercial | ❌ | ❌ | ✅ | licence **révocable** ; encadrement par iframe interdit sans accord | F06 |
| **Wolfram** | propriétaire | ❌ | ❌ | ✅ | gratuit limité au **pré-production** ; interdiction de produire des sorties commerciales | F09 |
| **CoCalc** | **MS-RSL** | ❌ | ❌ | ✅ | licence de **référence** : lecture seule, **distribution exclue** | F09 |
| **GLSL Sandbox** | MIT (plateforme) | ❌ | ❌ | ✅ | ⚠️ aucune licence par défaut pour les shaders déposés | F11 |
| **MathVerse** (sadeepas) | **aucune** | ❌ | ❌ | ❌ | tous droits réservés ; ⚠️ **même nom et même sujet** que le projet | F10 |

---

## 3. Les quatre points ouverts — à qualifier avant toute décision

⚠️ **Ces points ne sont pas tranchés ici.** Ils nécessitent une lecture juridique ou une réponse
écrite de l'éditeur. Ils sont listés parce que des décisions en dépendent.

### 3.1 Shaders — conflit entre le paquet MIT et le contrat de plateforme

Le dépôt et l'annonce d'ouverture (6 octobre 2026) déclarent le moteur, les composants et les
liaisons **sous MIT**, utilisables « partout, y compris en clientèle commerciale, SaaS, outils
internes ». Le **contrat de licence de la plateforme (v1.7, 3 août 2026)**, antérieur de deux mois,
énonce : « The Proprietary Technology is the **exclusive intellectual property** » et « **You may
not sell, license, or redistribute content or code created with Shaders** ».

La lecture la plus cohérente est la séparation annoncée par le README (MIT sur le paquet,
conditions propres sur la plateforme et les préréglages Pro). ⚠️ **Mais cette cohérence est une
interprétation.** Si la clause « code créé avec Shaders » s'appliquait au code exporté, elle
**viderait de sens la licence MIT**.

**→ Action : demander une confirmation écrite à l'éditeur** avant tout usage dans une bibliothèque
redistribuée.

### 3.2 React Bits — une « configuration exportable » est-elle un export au sens de la clause ?

La clause Commons Clause interdit de vendre ou redistribuer « les exports eux-mêmes…
individuellement ou comme le produit lui-même, tel un pack de sons, de textures, de fonds ou de
**gabarits** ». Le cahier des charges prévoit, par composant, une **configuration exportable**.

Un jeu de paramètres n'est probablement pas un export au sens de la clause. Un pack de gabarits
distribué pour lui-même le serait. **La frontière est juridique.**

### 3.3 GeoGebra — la portée de la co-propriété des productions

« Materials generated using GeoGebra are a derived product of the GeoGebra software and thus are
**under the copyright of both GeoGebra** and the party who generated the materials. »

Une figure produite avec GeoGebra est co-détenue et son usage commercial est restreint.
⚠️ La portée exacte sur une figure exportée n'est pas établie.

### 3.4 Wolfram — la brèche « open-source projects approved by Wolfram »

Les conditions de la Wolfram Engine gratuite autorisent notamment les « **Open-source projects
approved by Wolfram** ». Une voie existe donc, **soumise à approbation explicite**.
⚠️ Ni les critères ni la procédure n'ont été vérifiés.

---

## 4. Ce que le registre montre

### 4.1 Le secteur est majoritairement fermé, et majoritairement présenté comme ouvert

Sur les 35 plateformes, **9 relèvent d'un régime fermé ou restrictif**, et ce sont souvent les plus
visibles. Trois mécanismes de présentation trompeuse ont été documentés :

1. **Le titre de licence qui rassure.** « MIT + Commons Clause » : le mot MIT est exact, la clause
   emporte tout (React Bits).
2. **L'agrégateur qui répète sans vérifier.** Une dizaine d'annuaires annoncent Aceternity UI sous
   MIT ; la page officielle de l'éditeur décrit autre chose.
3. **Le dépôt public sans licence.** Publier son code ne le rend pas réutilisable : GeoGebra ne
   déclare aucune licence sur GitHub, le projet `sadeepas` non plus.

### 4.2 La séparation paquet / plateforme devient la norme

Shaders, Aceternity et React Bits adoptent tous le même schéma : **le code est ouvert, le service
est payant, les préréglages sont sous conditions propres.** C'est un modèle viable — mais il rend
la licence **illisibles d'un coup d'œil** et impose de lire deux textes là où on en attendait un.

### 4.3 Ce qui reste réellement disponible comme base

**Une seule plateforme du secteur est à la fois ouverte, massive, et sans restriction de
redistribution : shadcn/ui (MIT).** C'est d'elle que vient la mécanique de registre que toutes les
autres imitent. Toutes les autres plateformes de composants étudiées imposent une restriction de
redistribution ou une ambiguïté.

C'est un résultat structurant : **la couche infrastructurelle est libre, la couche catalogue ne
l'est pas.**

---

## 5. Ce qui est réutilisable, en pratique

| Besoin | Reprendre | Écarter |
|---|---|---|
| **Mécanique de distribution** (registre, CLI, copier-coller) | shadcn/ui — MIT | React Bits (clause), Aceternity (propriétaire) |
| **Rendu et animation web** | three.js, react-three-fiber, Motion — tous MIT | — |
| **Composants d'effets** | Shaders (⚠️ sous réserve du §3.1), Paper Shaders (Apache-2.0) | React Bits, Aceternity, Shadertoy |
| **Tracé mathématique** | JSXGraph (LGPL-3.0), MathBox (MIT), CindyJS (Apache-2.0) | Desmos, GeoGebra (régimes fermés) |
| **Vérification mathématique** | Wolfram en **référence** uniquement | Wolfram en dépendance |
| **Chaîne IA → maths** | Math-To-Manim (MIT) en référence d'architecture | sa sortie vidéo |

---

## 6. Méthode, sources et limites

**Sources.** Pour chaque plateforme : le fichier de licence du dépôt quand il existe (API GitHub
`contents`), la page de licence de l'éditeur, et les métadonnées de dépôt (`GET /repos`). Les
plateformes sans dépôt public ont été traitées par leurs pages publiques de conditions.

**Dates.** Toutes les observations datent du **2026-10-19**, sauf mention contraire. ⚠️ **Une
licence se vérifie à la date de l'usage** : le cas Shaders, ouvert depuis deux semaines, en est
l'illustration.

**Limites, énoncées explicitement :**

- ⚠️ **Aucune vérification juridique.** Ce registre n'est pas un avis de juriste et ne s'y substitue
  pas.
- ⚠️ **Aucun registre de marques consulté.**
- ⚠️ **Certaines plateformes n'ont pas été testées** (aucune application ouverte, aucun paquet
  installé) : l'environnement ne dispose ni de GPU ni de navigateur.
- ⚠️ **Les licences par élément ne sont pas vérifiées** là où une plateforme est contributive
  (Uiverse, Shadertoy, OpenShaders, GLSL Sandbox) : le régime applicable dépend de chaque auteur.
- ⚠️ **Les informations sur GLSL Sandbox proviennent d'une source tierce**, non de l'éditeur.
- ⚠️ **Les tarifs n'ont pas été vérifiés** : ils changent et ne figurent donc pas dans ce registre.

**Fiches sources :** `../fiches-phase-2/F01` à `F11`.
