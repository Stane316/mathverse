# A9 — REGISTRE DES PLATEFORMES ÉTUDIÉES (PHASE 2)

**Date de collecte :** 2026-10-19 (complétée le même jour)
**Mode d'accès :** API publique GitHub (`api.github.com`, non authentifiée, données publiques) et
recherche web générale. Aucun contournement d'accès, aucune extraction de contenu privé.
**Statut :** **31 plateformes vérifiées** sur les ~32 du périmètre prévu. **Dix fiches détaillées
rédigées** dans `../fiches-phase-2/` : F01 React Bits, F02 shadcn/ui, F03 Math-To-Manim,
**F04 Aceternity UI, F05 Uiverse, F06 Desmos, F07 GeoGebra, F08 Shadertoy, F09 Wolfram et CoCalc,
F10 MathVerse (sadeepas)**.

> ⚠️ **Ce registre est un relevé de faits observables, pas une évaluation.** Les colonnes
> « étoiles » et « dernière activité » datent du 2026-10-19 et bougeront. Les licences sont
> celles que déclare GitHub (`spdx_id`) ou que porte le fichier `LICENSE` du dépôt — elles
> doivent être relues avant toute décision de réutilisation.

---

## 1. Famille A — bibliothèques de composants web

Le positionnement de cette famille est visuel : composants prêts à copier, prévisualisation,
personnalisation. **Aucune ne porte d'explication mathématique.**

| Plateforme | Dépôt | Licence | ★ | Langue | Dernière activité | Remarque vérifiée |
|---|---|---|---:|---|---|---|
| **React Bits** | `DavidHDev/react-bits` | **MIT + Commons Clause** ⚠️ | 49 719 | JavaScript | 2026-10-19 | **N'est pas open source** (voir §3) |
| **shadcn/ui** | `shadcn-ui/ui` | MIT | 125 966 | TypeScript | 2026-10-19 | mécanique de registre, la référence du modèle « copier-coller » |
| **Magic UI** | `magicuidesign/magicui` | MIT | 22 748 | MDX | 2026-10-17 | composants animés, même modèle |
| **Motion** (ex-Framer Motion) | `motiondivision/motion` | MIT | 34 360 | TypeScript | 2026-10-19 | moteur d'animation, brique de base |
| **Motion Primitives** | `ibelick/motion-primitives` | MIT | 6 753 | TypeScript | 2026-09-28 | primitives d'animation pour React |
| **Uiverse Galaxy** | `uiverse-io/galaxy` | MIT | 13 585 | HTML | **2024-09-02** | **inactif depuis 2 ans** |

**Non vérifiés à ce jour :** Aceternity UI (dépôt public non identifié sous `aceternity/ui`),
Uiverse site principal (`uiverse.io`).

> **Rectification (2026-10-19).** Le rapport de phase 0 décrivait React Bits comme reposant sur
> la « mécanique de registre » de shadcn/ui. L'observation du dépôt corrige : React Bits construit
> sa distribution avec **jsrepo** (`jsrepo.config.ts`), en important l'adaptateur
> **`@jsrepo/shadcn`**. Il **émet donc bien des articles au format shadcn**, mais son outil de
> construction est un tiers. La conclusion de fond ne change pas — la mécanique reste ouverte —,
> mais le chemin de dépendance n'est pas celui qui était annoncé.

---

## 2. Famille B — moteurs et bibliothèques mathématiques

Le positionnement est inverse : la profondeur mathématique est réelle, mais **la sortie est une
image, une vidéo ou un canevas — pas un composant web réutilisable avec des propriétés**.

| Plateforme | Dépôt | Licence | ★ | Langue | Dernière activité | Sortie |
|---|---|---|---:|---|---|---|
| **three.js** | `mrdoob/three.js` | MIT | 116 630 | JavaScript | 2026-10-19 | WebGL, rendu |
| **react-three-fiber** | `pmndrs/react-three-fiber` | MIT | 33 081 | TypeScript | 2026-10-17 | pont React ↔ three.js |
| **p5.js** | `processing/p5.js` | **LGPL-2.1** | 24 145 | JavaScript | 2026-10-19 | canevas 2D/WebGL |
| **Manim** (communauté) | `ManimCommunity/manim` | MIT | 41 698 | Python | 2026-10-16 | **vidéo** |
| **D3** | `d3/d3` | ISC | 113 775 | Shell | 2026-05-28 | SVG/Canvas |
| **Observable Plot** | `observablehq/plot` | ISC | 5 407 | HTML | 2026-09-01 | SVG |
| **MathBox** | `unconed/mathbox` | MIT | 1 505 | JavaScript | **2023-05-05** | WebGL, **inactif** |
| **JSXGraph** | `jsxgraph/jsxgraph` | **LGPL-3.0** ⚠️ | 1 478 | JavaScript | 2026-10-19 | SVG/Canvas, géométrie |
| **CindyJS** | `CindyJS/CindyJS` | Apache-2.0 | 717 | JavaScript | 2026-10-14 | contenu mathématique interactif |
| **Motion Canvas** | `motion-canvas/motion-canvas` | MIT | 19 393 | TypeScript | 2026-07-02 | **vidéo** |

**À noter pour la stratégie de licence (reportée après la phase 2) :** deux licences à copyleft
faible apparaissent dans cette famille — **p5.js en LGPL-2.1** et **JSXGraph en LGPL-3.0**. Elles
sont utilisables, mais imposent des contraintes en cas de modification ou de liaison statique.

---

## 3. ⚠️ Constat majeur — React Bits n'est pas open source

`DavidHDev/react-bits` est le concurrent le plus direct : c'est la plus grande bibliothèque de
composants animés React/Next.js, avec prévisualisation, personnalisation et outils en ligne
(Background Studio, Texture Lab, Shape Magic, Center Stage, Sound Lab).

**Sa licence n'est pas une licence open source.** GitHub ne la reconnaît pas (`spdx_id =
NOASSERTION`) ; le fichier `LICENSE.md` porte le titre « MIT + Commons Clause License Condition
v1.0 ». Le `package.json` ne déclare aucun champ `license` et marque le paquet `private`.

Extraits textuels du fichier (consulté le 2026-10-19) :

> « You may use this Software, including for any commercial purpose, **so long as you do not sell,
> sublicense, or redistribute the components themselves** — whether alone, in a bundle, or as a
> ported version. »

> « **You may not sell, sublicense, or redistribute the tools or the sounds themselves, or offer
> the tools or a substantially similar copy of them as a hosted service** — whether alone, in a
> bundle, or as a ported version. »

> « What you make with the tools is yours to use. […] **You may not sell or redistribute the
> exports on their own**, either individually or as the product itself, such as a sound, texture,
> background, or template pack. »

**Conséquences pour Mathemirum, dont le cahier des charges impose le libre d'abord :**

1. **Interdit** : redistribuer les composants React Bits, seuls ou intégrés à un registre
   Mathemirum ; porter les composants ; héberger un service « substantiellement similaire ».
   La clause vise **exactement** le modèle d'une bibliothèque de composants publiée sous
   registre — c'est-à-dire Mathemirum.
2. **Autorisé** : utiliser React Bits pour construire un produit final ; réutiliser ce que les
   outils exportent dans une application, y compris commerciale.
3. **Une asymétrie à noter** : la clause interdit de vendre *les exports eux-mêmes* (pack de
   textures, de fonds, de gabarits). Or le cahier des charges de Mathemirum prévoit, par
   composant, une « configuration exportable ». Le périmètre exact de ce qui serait une
   redistribution d'export reste à qualifier juridiquement — **point à signaler, pas à trancher
   ici.**

Lecture stratégique : cette fermeture n'est pas un obstacle majeur, parce que React Bits
n'offre de toute façon **aucune explication mathématique**. Ce que Mathemirum veut reprendre du
modèle React Bits, c'est la *mécanique* (prévisualisation, paramètres réglables, copier-coller,
CLI de registre) — pas le code. La mécanique, elle, est ouverte : **shadcn/ui (MIT) en est
l'origine déclarée**, et React Bits lui-même s'y réfère.

---

## 4. Famille C — la génération par IA : tout converge vers la vidéo

Recherche du 2026-10-19 sur la question « existe-t-il une plateforme réunissant composants
visuels + explication mathématique + prompts + CLI ». Résultats :

| Projet | Licence | Nature | Sortie |
|---|---|---|---|
| **Math-To-Manim** (`HarleyCoops`) | MIT | chaîne d'agents IA → scènes Manim ; **CLI** (`math-to-manim run "…"`) | **MP4** |
| **Manimly** (`shubhamrawat-gh`) | — | studio IA navigateur, sans code ; bibliothèque de gabarits | **MP4 / WebM / GIF**, et source Python |
| **Manimator** (arXiv 2507.14306) | — | système agentique, article + code de démonstration | **vidéo** |
| **MathViz-E** (`EmergenceAI`) | — | agents vocaux + WolframAlpha + Desmos | graphe Desmos |
| **ExcaliMath** (`tamerUAE`) | MIT | KaTeX + Plotly greffés sur Excalidraw | **composant React** |
| **JMathAnim** (Codeberg) | GPL | moteur 2D en Groovy/Java, éditeur propre | **MP4 / PNG / SVG** |
| **dynamic-manim-components** (`philip-murray`) | — | « bibliothèque de composants mathématiques » pour ManimCE | scènes Manim |

**Constat :** l'ensemble du courant « IA + maths → visuel » **sort de la vidéo**. Aucun des
projets trouvés ne produit un composant web réutilisable, avec propriétés réglables, aperçu en
direct et tests — ce qui est précisément le livrable exigé par le cahier des charges de
Mathemirum.

Deux exceptions partielles, et elles sont instructives :
- **ExcaliMath** est bien un composant React (MIT), mais c'est un *tableau blanc*, pas une
  bibliothèque de composants visuels.
- **dynamic-manim-components** poursuit l'idée d'une bibliothèque de composants
  mathématiques — mais dans l'écosystème Python/Manim, donc hors du web.

---

## 4 bis. Complément de collecte (2026-10-19, fin de journée)

### Homonymes détectés en phase 0

| Projet | Licence | ★ | Langue | Activité | Nature |
|---|---|---:|---|---|---|
| **MathVerse** (`ZrrSkywalker`) | MIT | 184 | Python | 2025-04-28 | benchmark MLLM de maths visuelles (ECCV-2024) |
| **-MathVerse-An-Interactive-Suite…** (`sadeepas`) | **aucune** | 2 | HTML | 2025-11-25 | suite d'applications web mathématiques |

Le premier occupe le **nom** mais pas le sujet (c'est un jeu d'évaluation de modèles). Le second
occupe le **sujet** — « suite interactive d'applications web mathématiques » — mais n'a aucune
licence déclarée et quasiment aucune traction (2 ★). **Aucun des deux ne bloque Mathemirum**, mais
le second mérite une fiche : c'est le seul projet trouvé dont l'intitulé recouvre exactement
l'objet visé.

### Projets de génération mathématique par IA — vérification des licences

| Projet | Licence | ★ | Langue | Activité |
|---|---|---:|---|---|
| **Math-To-Manim** (`HarleyCoops`) | MIT | 2 787 | Python | 2026-10-17 |
| **3b1b/manim** (moteur d'origine) | MIT | 95 373 | Python | 2026-09-09 |
| **manim-video-generator** (`rohitg00`) | MIT | 306 | TypeScript | 2026-01-29 |
| **ExcaliMath** (`tamerUAE`) | MIT | 35 | TypeScript | 2026-04-05 |
| **reactive-manim** (`philip-murray`) | MIT | 77 | Python | 2026-08-31 |
| **MathViz-E** (`EmergenceAI`) | MIT | 36 | Python | 2026-04-17 |
| **Manimly** (`shubhamrawat-gh`) | MIT | 0 | TypeScript | 2026-09-29 |

**Tous sous MIT.** Le constat du §4 est donc confirmé sur sept projets : le couplage
IA + maths est **massivement ouvert** — et **massivement orienté vers la vidéo**.

### Distribution : deux outils, pas un

- **shadcn/ui** : monorepo, paquets `shadcn` (CLI), `registry` (le registre), `react`, `helpers`,
  `tests`. MIT.
- **jsrepo** : utilisé par React Bits pour *construire* le registre, avec l'adaptateur
  `@jsrepo/shadcn` pour *émettre* au format shadcn.

Conséquence pour Mathemirum : il existe **deux** chaînes d'outils, et la compatibilité se joue au
niveau du **format d'article de registre**, pas de l'outil.

---

## 4 ter. Deuxième vague de collecte (2026-10-19)

Sept plateformes étudiées en profondeur. **Le constat dominant est juridique.**

| Plateforme | Régime | Réutilisable comme base ? | Fiche |
|---|---|---|---|
| **Aceternity UI** | licence **propriétaire** (redistribution interdite) | ❌ **non** | F04 |
| **Uiverse** | **MIT** sur le dépôt miroir, inactif depuis 2 ans | ⚠️ à vérifier élément par élément | F05 |
| **Desmos** | service fermé ; gratuit = **non commercial** | ❌ **non** | F06 |
| **GeoGebra** | **4 régimes** : EUPL (code), non commercial (services), CC BY-NC-SA (ressources) | ❌ **non** | F07 |
| **Shadertoy** | **CC BY-NC-SA 3.0 par défaut** (non commercial + viral) | ❌ **non** | F08 |
| **Wolfram** | **propriétaire** ; gratuit = pré-production | ❌ **non** | F09 |
| **CoCalc** | licence **non identifiée** (`NOASSERTION`) | ⚠️ non vérifié | F09 |
| **MathVerse (sadeepas)** | **aucune licence** = tous droits réservés | ❌ **non** | F10 |

### Les trois découvertes les plus contraignantes

1. **Shadertoy — le corpus de référence est fermé.** La licence par défaut est
   **CC BY-NC-SA 3.0** : non commerciale *et* à partage à l'identique. La plupart des auteurs ne
   déclarent rien, donc **l'absence d'en-tête vaut interdiction, pas autorisation**. C'est la plus
   grosse contrainte de cette phase pour un projet de composants visuels.
2. **GeoGebra — une clause de co-propriété des productions.** « Materials generated using GeoGebra
   are […] under the copyright of **both GeoGebra** and the party who generated the materials. »
   Une figure produite avec GeoGebra est co-détenue et son usage commercial restreint.
3. **Aceternity UI — le « MIT » répandu est faux.** De nombreux annuaires l'annoncent MIT ; la page
   de licence officielle décrit une licence propre interdisant **la redistribution du code, même
   modifié**. Leçons : la source de vérité est la page de l'éditeur, jamais un agrégateur.

### Contrepartie positive

**Shaders** (`shaders.com`) déclare son moteur et ses composants **sous licence MIT**, avec export
de code et usage commercial gratuit. ⚠️ **Non encore étudiée au-delà de sa page de conditions** —
candidate prioritaire pour la suite.

**Wolfram** autorise explicitement les « **open-source projects approved by Wolfram** » dans les
usages de la Wolfram Engine gratuite. Une brèche existe, soumise à approbation — critères non
vérifiés.

---

## 5. Ce que ce premier relevé suggère — hypothèses, non faits

⚠️ **Ce qui suit est une hypothèse, pas un résultat.** Elle s'appuie sur 15 plateformes
vérifiées sur ~20 prévues, et sur une seule requête de recherche. Elle demande à être
confirmée par les fiches détaillées.

L'espace semble se diviser en deux territoires qui **ne se recouvrent pas** :

- d'un côté, des **bibliothèques de composants web** très abouties visuellement, sans aucune
  profondeur mathématique ;
- de l'autre, des **moteurs mathématiques** très profonds, qui produisent des vidéos ou des
  canevas, pas des composants.

La place libre se situerait dans l'intersection : **un composant web qui porte avec lui son
explication mathématique, ses équations, ses hypothèses, sa validation, son prompt de
régénération et sa commande CLI**. C'est la thèse même de Mathemirum.

Deux réserves avant d'en tirer quoi que ce soit :
1. **Aucune preuve d'absence n'a été établie.** L'absence de résultat dans une recherche n'est
   pas la preuve qu'aucune plateforme n'existe. Le cahier des charges interdit de revendiquer
   l'exhaustivité.
2. **La place libre peut être libre pour une raison** : il est possible que personne ne la
   occupe parce que la demande est faible, ou parce que la combinaison est plus coûteuse à
   maintenir qu'elle n'apporte. Cette question relève de la phase 2 prolongée (étude de
   demande), pas du présent relevé.

---

## 6. Provenance des données

| Champ | Source | Date |
|---|---|---|
| Licence, ★, langue, activité | `GET https://api.github.com/repos/{propriétaire}/{dépôt}` | 2026-10-19 |
| Texte de la licence React Bits | `GET https://api.github.com/repos/DavidHDev/react-bits/contents/LICENSE.md` | 2026-10-19 |
| Projets de la famille C | recherche web générale | 2026-10-19 |

**Limites de la collecte :** l'API GitHub non authentifiée est limitée en débit (60 requêtes par
heure et par adresse IP). 18 requêtes ont été consommées. Aucune licence n'a été vérifiée contre
un registre de marques ou par un conseil juridique.
