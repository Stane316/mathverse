# F11 — SHADERS, GLSL SANDBOX, OPENSHADERS, PAPER SHADERS

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** API GitHub, pages publiques, recherche web
**Motif :** Shaders (`shaders.com`) était le candidat prioritaire issu de la fiche F08. L'étude a
révélé **un conflit documenté** entre son dépôt et son contrat de licence, et fait apparaître trois
acteurs voisins qu'il fallait lever.

---

## 1. Présentation et positionnement

**Shaders** (`shader-effects-inc/shaders`) — « Composants WebGPU pour React, Vue, Svelte, Solid, JS
et Framer ». **5 106 étoiles, TypeScript, MIT, actif au 9 octobre 2026.** Le projet s'est ouvert
très récemment : une annonce datée du **6 octobre 2026** intitulée « Shaders is now open source »
déclare que le moteur de rendu, tous les composants et les liaisons de framework passent sous MIT.

Trois voisins, découverts en cours de recherche :

| Projet | Licence | ★ | Note |
|---|---|---:|---|
| **OpenShaders** (`openshaders/openshaders`) | MIT | 277 | par **David H.** — le même auteur que React Bits (**vérifié**) ; **dépôt sans code**, pré-lancement (§17) |
| **Paper Shaders** (`paper-design/shaders`) | **Apache 2.0** | **3 793** | **30** effets WebGL, zéro dépendance **vérifiée sur npm**, usage commercial sans attribution (§17) |
| **GLSL Sandbox** | **MIT** (plateforme) | — | ⚠️ aucune licence par défaut pour les shaders déposés |

## 2. Fonctionnalités (Shaders)

- **200+ composants WebGPU déclaratifs** (199 à 210 selon les sources) : dégradés, bruit, verre,
  métal, lumière, distorsions, transitions, flous, effets de curseur.
- **Composition par couches** : un composant `<Shader>` canvas ; les enfants s'empilent en couches
  mélangées par le GPU ; imbrication, mélange, masquage.
- **Propriétés dynamiques** : mise à jour à l'exécution (`shader.update()`), valeurs pilotées par le
  temps, par le curseur, ou par une autre couche.
- **Un éditeur de conception** sur toile infinie, avec **export du code vers le framework**.
- **CLI** : `npx shaders connect`, `npx shaders install`, `npx shaders update`, avec détection
  automatique du framework et fichier de verrouillage.
- **MCP** : installation de composants par un agent IA.
- **`defineShader` / `CustomShader`** : écrire ses propres effets en passant des propriétés et un
  bloc de peinture WGSL. Le langage interne est rendu public.

## 3. Parcours utilisateur

Installation par npm (`npm install shaders`) ou par CLI, ou conception dans l'éditeur puis export.
Le projet revendique des temps de compilation **~25× plus rapides** que des alternatives fondées sur
Three.js, grâce à un moteur bâti sur **TypeGPU** plutôt que sur un moteur 3D généraliste.
⚠️ **Cette affirmation n'a pas été vérifiée par mesure.**

## 4. Architecture technique observable

Le dépôt est public, TypeScript, avec un paquet npm. Le moteur repose sur **WebGPU** via TypeGPU —
un choix technique notablement plus moderne que le WebGL de Three.js, avec une conséquence
directe : **la compatibilité navigateur de WebGPU est plus restreinte que celle de WebGL.**

Cinq points d'entrée de framework : `shaders/js`, `shaders/react`, `shaders/vue`, `shaders/svelte`,
`shaders/solid`, avec les mêmes propriétés partout.

## 5. Mode de distribution

| Composant | Régime |
|---|---|
| Paquet npm et dépôt GitHub (moteur, composants, liaisons) | **MIT** |
| Éditeur de conception, présélections, sections, fonctions de plateforme | **conditions propres** |
| Palier Pro (préréglages et sections) | licence payante séparée |

## 6. Prévisualisation et personnalisation

Le point le plus abouti de toutes les plateformes étudiées : conception visuelle sur toile, réglage
en direct des propriétés, pilotage par curseur ou par ligne de temps, puis **export de l'arbre de
composants exact**. C'est la personnalisation paramétrique que React Bits et Aceternity n'offrent
qu'en partie.

## 7. et 8. Documentation et contribution

Documentation publique (installation, composition, leçons vidéo, référence par composant). Dépôt
ouvert aux issues et aux pull requests, avec une règle : **ouvrir une issue avant toute PR qui
n'est pas un correctif**. ⚠️ Le processus de contribution effectif n'a pas été observé.

## 9. ⚠️ Licences et contraintes de réutilisation — un conflit documenté

**Deux textes se contredisent, et c'est le point central de cette fiche.**

**Le dépôt GitHub et l'annonce d'ouverture (6 octobre 2026) :**

> « The rendering engine, every shader component, and the framework bindings are now MIT licensed
> on GitHub. Code export in the design editor is free for everyone. »
> « **Use Shaders components anywhere.** That includes both personal and commercial client work,
> SaaS products, internal tools, etc. No need for a license. »

> Séparation explicite (README) : « The engine, every component and the framework bindings in this
> repository and the shaders npm package are MIT licensed. **The design editor, presets, sections
> and other platform features at shaders.com are separate from this package and have their own
> terms.** »

**Le contrat de licence de la plateforme (« Shader Effects License Agreement v1.7 », page
`shaders.com/license`, dernière mise à jour **3 août 2026** — soit **deux mois avant** l'ouverture) :**

> « The Proprietary Technology is the **exclusive intellectual property** of Shader Effects, Inc. »
> « **You may not sell, license, or redistribute content or code created with Shaders.** »
> « You may not modify, decompile, reverse engineer, or attempt to extract the source code of the
> Proprietary Technology. »
> « Official open-source projects may use Shaders without a license key **only for their
> promotional or documentation websites, provided Shaders is not a core or monetized part of the
> project**. »

**Analyse.** La lecture la plus cohérente est celle du README : **MIT sur le paquet et le dépôt,
conditions propres sur la plateforme et les préréglages Pro**. Le contrat v1.7 antérieur à
l'ouverture décrirait alors le régime de la plateforme, non celui du paquet.

⚠️ **Mais cette cohérence est une interprétation, pas un fait établi.** Deux signaux imposent la
prudence :
1. Le contrat v1.7 est daté **3 août 2026** et l'ouverture **6 octobre 2026** : le contrat peut être
   **périmé** — ou n'avoir jamais été mis à jour.
2. La clause « vous ne pouvez pas vendre, licencier ou redistribuer le contenu ou le code **créé
   avec** Shaders », si elle s'appliquait au code exporté, **viderait de son sens la licence MIT** du
   paquet. Une bibliothèque de composants est par construction une redistribution de code créé avec
   l'outil.

**Conséquence pour Mathemirum :**

| | Verdict |
|---|---|
| Utiliser le paquet npm `shaders` (MIT) dans un produit | ✅ a priori autorisé |
| Redistribuer des composants Shaders dans un registre | ⚠️ **non tranché** — dépend de l'articulation entre les deux textes |
| Utiliser les préréglages Pro | ❌ licence payante, conditions propres |
| Utiliser la plateforme dans le cœur d'un projet open source | ⚠️ la clause « promotional or documentation websites only » est restrictive |

**→ Action requise :** ce conflit doit être levé **par écrit auprès de l'éditeur** avant tout usage
de Shaders dans une bibliothèque redistribuée. ⚠️ **Ce point est ouvert et n'est pas tranché ici.**

## 10. Points forts

- **Le seul acteur WebGPU sous licence ouverte** trouvé à cette échelle (200+ composants).
- **Cinq frameworks, un seul paquet**, mêmes propriétés partout — une portabilité rare.
- **Un éditeur qui exporte du code réel**, gratuitement.
- **CLI et MCP** : le pont vers les agents IA est déjà fait.
- **`defineShader` public** : on peut étendre la bibliothèque, pas seulement la consommer.
- MIT sur le paquet, sans clause Commons Clause ni restriction de redistribution apparente.

## 11. Limites

- ⚠️ **Conflit de licence non levé** entre le dépôt et le contrat de la plateforme.
- ⚠️ **WebGPU**, donc une compatibilité navigateur plus restreinte que WebGL.
- ⚠️ **Aucune explication mathématique** : 200 effets visuels, sans méthode ni hypothèses exposées.
- Le projet s'est ouvert depuis **deux semaines** : le recul manque sur la pérénnité et la
  gouvernance.
- ⚠️ L'affirmation de performance (25× plus rapide que Three.js) n'a pas été vérifiée.

## 12. Éléments non vérifiés ⚠️

- L'articulation exacte entre la licence MIT du paquet et le contrat v1.7 de la plateforme.
- La pérennité du palier gratuit de l'éditeur après l'ouverture.
- Les performances réelles (aucun test exécuté — pas de GPU ni de navigateur dans cet
  environnement).
- La compatibilité navigateur effective de WebGPU pour les composants.
- ~~**OpenShaders** : périmètre réel, gouvernance, et surtout — comme Shadertoy — **le régime des
  shaders déposés par les créateurs**~~ — **levé le 2026-10-21, recommandation R7** → §17.1
- ~~**Paper Shaders** (Apache 2.0) : nombre d'effets, qualité, et périmètre exact de la
  publication.~~ — **levé le 2026-10-21, recommandation R7** → §17.2
- **GLSL Sandbox** : ⚠️ aucune source directe consultée — la mention MIT provient d'un projet tiers.

## 13. Idées à retenir

- **L'ouverture peut être récente et stratégique.** Shaders est passé MIT deux semaines avant
  l'observation, en réaction probable à la fermeture du secteur. Le paysage bouge vite : **une
  licence se vérifie à la date de l'usage, jamais de mémoire.**
- **La séparation paquet / plateforme est le modèle qui se généralise.** MIT sur le code, conditions
  propres sur le service. C'est le schéma que Mathemirum devra clarifier pour lui-même.
- **L'éditeur qui exporte du code est la forme aboutie du modèle copier-coller** : on ne copie plus
  un composant, on conçoit le sien et on l'exporte.
- **WebGPU contre WebGL** est un choix d'architecture à assumer : modernité contre portée.

## 14. Erreurs à éviter

- ❌ Lire « MIT » sur le dépôt et ignorer le contrat de la plateforme : les deux textes coexistent
  et leur articulation n'est pas établie.
- ❌ Supposer que les préréglages Pro suivent le régime MIT du paquet.
- ❌ Croire qu'une licence ouverte récente est stabilisée : deux semaines de recul.

## 15. Opportunités de différenciation

Shaders est le concurrent le plus sérieux trouvé sur le plan **technique** : MIT, WebGPU, 200+
composants, éditeur, CLI, MCP, extensibilité. **Il ne couvre toujours pas l'explication
mathématique** — aucun des 200 effets n'expose sa méthode, ses hypothèses ou son domaine de
validité.

La différenciation de Mathemirum ne se joue donc pas sur la quantité ni sur la technique de rendu,
mais sur **la couche documentaire et probatoire** : équations, hypothèses, validation, tests,
mesures. C'est précisément la couche qu'aucun acteur du secteur ne porte — et c'est celle que le
cahier des charges impose.

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| MIT, 5 106 ★, TypeScript, activité 2026-10-09 ; un seul dépôt | `GET /repos/shader-effects-inc/shaders`, page de l'organisation | 2026-10-19 |
| Annonce d'ouverture, MIT sur moteur/composants/liaisons, export gratuit | `shaders.com/updates/shaders-is-open-source` (page publique, datée 2026-10-06) | 2026-10-19 |
| Séparation paquet MIT / plateforme à conditions propres | README du dépôt (page publique) | 2026-10-19 |
| Contrat v1.7 : propriété exclusive, interdiction de redistribuer, clause open source, tarifs | `shaders.com/license` et `/pricing` (pages publiques) | 2026-10-19 |
| 199–210 composants, points d'entrée par framework, CLI, TypeGPU, 25× | `cssscript.com`, `news.lavx.hu`, `shaders.com/pro` | 2026-10-19 |
| OpenShaders : MIT, 264 ★, David H., licence par créateur | `GET /repos/openshaders/openshaders`, recherche web | 2026-10-19 |
| Paper Shaders : Apache 2.0, usage commercial sans attribution | dépôt `paper-design/shaders`, recherche web | 2026-10-19 |
| GLSL Sandbox : MIT annoncé pour la plateforme | mention dans un projet tiers ⚠️ (source indirecte) | 2026-10-19 |

**Limites :** lectures de pages publiques. **Aucune vérification juridique.** Aucun composant
installé ni exécuté : pas de GPU ni de navigateur dans cet environnement. Le conflit de licence
n'est pas levé.

---

## 17. Vérification R7 — Paper Shaders et OpenShaders étudiés en détail

**Recommandation R7 (A9 §9) :** « Vérifier Paper Shaders (Apache 2.0) et OpenShaders (MIT) : deux
candidats libres apparus en cours de collecte, non encore étudiés en détail. »
**Levée le 2026-10-21.** Mode d'accès : API GitHub, registre npm, pages publiques du projet.

**Résultat en une phrase : les deux candidats ne se valent pas, et ils ne se valent pas dans le sens
que laissaient supposer leurs étoiles.** Paper Shaders est une bibliothèque **réelle, active,
sérieuse et sous-licenciée sans piège** — c'est le meilleur acteur ouvert trouvé après shadcn/ui.
OpenShaders **n'existe pas encore** : 277 étoiles, aucun code.

### 17.1 OpenShaders — un dépôt annonce, sans code

**Mesures relevées le 2026-10-21.**

| Donnée | Valeur | Source |
|---|---|---|
| Contenu du dépôt | `.github/`, `LICENSE` (1 069 o), `README.md` (3 120 o) — **et rien d'autre** | `GET /repos/openshaders/openshaders/contents/` |
| Langage détecté | **aucun** | API |
| Taille du dépôt | **473 Kio** | API |
| Commits | **3**, tous de `DavidHDev`, du 6 au 9 septembre 2026 | API |
| Contributeurs | **1** (`DavidHDev`) | API |
| Dernière poussée | **2026-09-09** — soit **42 jours** avant l'observation | API |
| Issues ouvertes | 0 · forks 13 · étoiles **277** | API |
| Paquet npm | **aucun** (`openshaders` : `{"error":"Not found"}`) | registre npm |

**Le dépôt le dit lui-même.** Le README porte un badge « status: **in development** » et une section
« Coming soon » : « Work on the platform is already underway. The full OpenShaders experience is
coming soon, **with its source code published here**. » La page `openshaders.com/about`, signée « I'm
building OpenShaders », décrit un projet à bâtir : éditeur WebGL/WebGPU, registry shadcn,
composants React. Le site se réduit aujourd'hui à une page d'atterrissage et à une campagne
« claim your username ».

**Gouvernance : une seule personne.** L'auteur est bien **David H.** — le compte `DavidHDev` est
propriétaire de `DavidHDev/react-bits` (49 807 ★, poussé la veille) ✅ *vérifié, l'hypothèse de la
fiche est confirmée*. Aucun second contributeur, aucune issue, aucune PR externe.

> ⚠️ **Conséquence pour Mathemirum : OpenShaders ne peut pas être évalué, il peut seulement être
> surveillé.** 277 étoiles récompensent une **promesse**, adossée à la notoriété de React Bits, non
> un code. Le retenir comme brique technique serait un pari sur une livraison non datée, par un
> auteur dont l'autre projet porte déjà une **clause Commons Clause** (F01).

### 17.2 Le régime des shaders déposés — la question était la bonne, la réponse est défavorable

C'était le point que la fiche avait laissé ouvert, par analogie avec Shadertoy (F08). Il est
tranché, et il l'est **deux fois, de la plume de l'auteur** :

> README du dépôt — « The platform's license covers the platform. **Creators will choose the
> licenses for their own shaders.** »

> `openshaders.com/about` — « It is still your call. Authors keep their credit everywhere a shader
> travels, and **choose the license their own pieces carry**. **The platform being open is a promise
> about the platform, not a claim on what you make with it.** »

**Analyse.** La formulation est limpide et honnête — mais elle reproduit **exactement** la structure
de risque de Shadertoy (F08, CC BY-NC-SA par défaut, licence au choix de l'auteur) : **MIT sur le
récipient, régime inconnu sur le contenu**. La plateforme annonce toutefois deux atténuations qu'il
faut porter à son crédit : elle « ouvre avec une bibliothèque de base » que l'auteur construit
lui-même, « libre et open source », et elle s'engage à ce que le choix d'une licence ouverte soit
« le chemin le plus facile ». Aucune de ces deux promesses n'est vérifiable avant l'ouverture.

**Verdict :** ⚠️ **structurellement identique à Shadertoy** sur le point qui compte pour un projet
qui redistribue. À réévaluer à l'ouverture — et à la date de l'usage, jamais de mémoire.

### 17.3 Paper Shaders — le meilleur acteur ouvert trouvé depuis shadcn/ui

**Mesures relevées le 2026-10-21.**

| Donnée | Valeur | Source |
|---|---|---|
| Licence | **Apache 2.0** (texte complet, avec appendice) | `LICENSE`, 11 357 o |
| Fichier `NOTICE` | présent — « Powered by Paper Shaders: https://shaders.paper.design » | dépôt |
| Étoiles / forks | **3 793** / 166 | API |
| Création · dernière poussée | 2024-10-09 · **2026-10-20 (la veille)** | API |
| Contributeurs | **15+**, tête à 175 commits | API |
| Issues ouvertes | 14 · PR numérotées jusqu'à **#294** | API |
| Paquets | `@paper-design/shaders` · `@paper-design/shaders-react` | npm |
| Version | **0.0.81** — 112 et 118 versions publiées depuis 2024-10-15 | npm |
| Dépendances (vanilla) | **AUCUNE** — ✅ *l'affirmation « zero-dependency » est vérifiée* | npm |
| Titulaire du droit | **Lost Coast Labs, Inc.** (paper.design) | README |

**Nombre d'effets : 30.** La fiche disait « 30+ » faute de mesure. Le comptage est fait ici par
**quatre sources indépendantes qui concordent** : 30 fichiers dans `packages/shaders/src/shaders/`,
30 définitions dans `docs/src/shader-defs/`, **30 items** dans `registry.json`, et 30 effets
présentés sur le site, répartis en **7 filtres d'image** (papier, verre cannelé, eau, tramage,
demi-teintes, distortion), **3 animations de logo** (carte de chaleur, métal liquide, fumée de
gemme) et **20 effets** (dégradés de maillage, bruits de Perlin et simplex, Voronoï, métaballes,
rayons divins, spirales, vagues…).

**Le périmètre exact de la publication** — c'était la seconde question ouverte. Le README y répond
sans ambiguïté :

> « You can use Paper Shaders in commercial websites, apps, games, videos, prototypes, internal
> tools, and other end products **without visible attribution**. »
> « **If you redistribute Paper Shaders code as part of another shader library, plugin, or tool,
> please preserve the included LICENSE and NOTICE files.** Visible credit such as “Powered by Paper
> Shaders” is also appreciated […] »

**Analyse.** Aucun piège : pas de clause Commons Clause, pas de restriction de redistribution, pas
de séparation paquet/plateforme à la manière de Shaders (§9). Les deux obligations — conserver
`LICENSE` et `NOTICE` — sont **celles de l'Apache 2.0 lui-même** (§4 a, c, d), que le projet rappelle
au lieu de les durcir. **C'est le régime le plus propre de tous les acteurs étudiés**, à l'exception
de shadcn/ui (MIT, sans `NOTICE`).

### 17.4 Deux réserves sur Paper Shaders, et une découverte

**Réserve 1 — la version.** `0.0.x` depuis octobre 2024, 112 versions, et le README prévient
explicitement : « **Please pin your dependency** – we will ship breaking changes under 0.0.x
versioning. » Deux ans de publication sans engagement de stabilité : ⚠️ le coût de maintenance pour
un projet qui dépend de la bibliothèque est réel.

**Réserve 2 — la portée des frameworks.** Vanilla JS et React aujourd'hui ; **Vue, Svelte et Solid
sont renvoyés à d'éventuelles PR communautaires** (« intent to accept community PRs in the future »).
C'est très en deçà des cinq liaisons de Shaders (§4).

**La découverte : un `llms.txt` complet et déployé.** `https://shaders.paper.design/llms.txt` existe
et expose, pour chacun des 30 shaders, la description, l'URL et **chaque paramètre avec son type, sa
description et ses bornes** (`lacunarity` : `number`, `1.5 to 10` ; `octaveCount` : `1 to 8`,
entier). Le registry suit le **schéma shadcn** (`ui.shadcn.com/schema/registry.json`).

Le rapprochement avec R3 est direct : l'« AI readiness » — serveur MCP, `llms.txt` — était le
**premier critère** de choix d'une bibliothèque de composants dans l'étude Telerik citée en
`A10-etude-de-demande.md`. **Paper Shaders coche cette case ; aucun autre acteur étudié ne la
cochait.**

### 17.5 Ce que ni l'un ni l'autre ne font : la mathématique

Page `perlin-noise`, lue en entier : sept paramètres nommés d'après la mathématique sous-jacente —
`octaveCount`, `persistence`, `lacunarity` —, chacun typé et borné, et pour toute explication :
**« Classic animated 3D Perlin noise with exposed controls. »**

Aucune équation. Aucune méthode. Aucune hypothèse. Aucun domaine de validité. La bruit de Perlin
est **nommée, paramétrée, réglable — et non expliquée.**

**C'est la conclusion utile de R7.** Le meilleur acteur ouvert trouvé — Apache 2.0, sans piège,
3 793 étoiles, zéro dépendance, `llms.txt`, registry shadcn — s'arrête **exactement là où
Mathemirum commence**. La différentiation ne se joue ni sur la licence, ni sur la technique de
rendu, ni désormais sur l'aptitude à l'IA : **elle se joue sur la couche probatoire**, la seule
qu'aucun acteur du secteur ne porte.

### 17.6 Tableau de décision

| | Verdict |
|---|---|
| Utiliser Paper Shaders dans un produit commercial | ✅ autorisé, sans attribution visible |
| Redistribuer du code Paper Shaders dans une bibliothèque | ✅ autorisé **sous réserve de conserver `LICENSE` et `NOTICE`** (obligation Apache 2.0 §4) |
| Dépendre de Paper Shaders sans épingler la version | ❌ déconseillé — `0.0.x`, ruptures annoncées |
| Compter sur Paper Shaders pour Vue / Svelte / Solid | ❌ non disponible — PR communautaires envisagées |
| Utiliser OpenShaders aujourd'hui | ❌ **impossible — aucun code publié** |
| Considérer OpenShaders comme MIT pour son contenu | ❌ **non** — les créateurs choisissent leur propre licence |
| Considérer Paper Shaders comme une source d'explication mathématique | ❌ **non** — paramètres documentés, mathématique absente |

### 17.7 Sources de la section 17

| Donnée | Source | Date |
|---|---|---|
| OpenShaders : contenu du dépôt, 3 commits, 1 contributeur, aucun langage, 473 Kio, 277 ★ | `GET /repos/openshaders/openshaders` (+ `/contents/`, `/commits`, `/contributors`) | 2026-10-21 |
| OpenShaders : « status in development », « coming soon », licence par créateur | `README.md` du dépôt | 2026-10-21 |
| OpenShaders : « the platform being open is a promise about the platform… », auteur unique, registry shadcn annoncé | `openshaders.com/about` (page publique) | 2026-10-21 |
| OpenShaders : aucun paquet publié | `GET registry.npmjs.org/openshaders` → `Not found` | 2026-10-21 |
| `DavidHDev` propriétaire de React Bits (49 807 ★, poussé 2026-10-19) | `GET /repos/DavidHDev/react-bits` | 2026-10-21 |
| Paper Shaders : Apache-2.0, 3 793 ★, 166 forks, créé 2024-10-09, poussé 2026-10-20, 14 issues | `GET /repos/paper-design/shaders` | 2026-10-21 |
| `NOTICE` « Powered by Paper Shaders » ; `LICENSE` Apache 2.0 complet avec appendice | dépôt | 2026-10-21 |
| 30 shaders, 30 définitions, 30 items de registre | `packages/shaders/src/shaders/`, `docs/src/shader-defs/`, `docs/registry.json` | 2026-10-21 |
| 30 effets en 3 catégories ; « use … without visible attribution » ; pin de version ; Lost Coast Labs | `shaders.paper.design`, `README.md` du dépôt | 2026-10-21 |
| `0.0.81`, zéro dépendance, peer React ^18‖^19, 112/118 versions | `GET registry.npmjs.org/@paper-design/shaders{,-react}` | 2026-10-21 |
| `llms.txt` déployé, paramètres typés et bornés ; registry au schéma shadcn | `shaders.paper.design/llms.txt`, `docs/registry.json` | 2026-10-21 |
| Page Perlin : paramètres sans équation, description en une ligne | `shaders.paper.design/perlin-noise` | 2026-10-21 |

**Limites de la section 17 :** lectures d'API et de pages publiques. **Aucune vérification
juridique.** Aucun composant installé ni exécuté : pas de GPU ni de navigateur dans cet
environnement — la qualité visuelle des 30 effets **n'a pas été évaluée**, seules leurs
caractéristiques déclarées et mesurables l'ont été. Les affirmations de performance (« ultra fast »)
ne sont pas vérifiées.
