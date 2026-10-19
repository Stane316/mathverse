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
| **OpenShaders** (`openshaders/openshaders`) | MIT | 264 | par **David H.** — le même auteur que React Bits ; en développement |
| **Paper Shaders** (`paper-design/shaders`) | **Apache 2.0** | — | 30+ effets WebGL, zéro dépendance, usage commercial sans attribution |
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
- **OpenShaders** : périmètre réel, gouvernance, et surtout — comme Shadertoy — **le régime des
  shaders déposés par les créateurs** (« Creators will choose the licenses for their own shaders »).
- **Paper Shaders** (Apache 2.0) : nombre d'effets, qualité, et périmètre exact de la publication.
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
