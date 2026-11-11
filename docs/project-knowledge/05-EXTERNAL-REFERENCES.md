# 05 — Références externes

**Date :** 2026-11-11 · **Commit :** `6f87baf`
**Sources :** `annexes/A9-registre-plateformes.md`, `annexes/A9-comparaison-transversale.md`,
`annexes/A9-registre-des-licences.md`, `fiches-phase-2/F01…F11`

---

## 1. Nature des relations — avertissement

⚠️ **Aucune des références listées ci-dessous n'est une dépendance du projet.** Le projet n'a aucun
code, donc aucune dépendance.

Toutes ces plateformes relèvent de la relation **« source d'inspiration / référence étudiée »**, et
pour certaines **« solution concurrente ou alternative »**. Les confondre avec des dépendances
serait une erreur grave.

| Type de relation | Nombre |
|---|---:|
| Dépendance directe | **0** |
| Dépendance indirecte | **0** |
| Source d'inspiration / référence étudiée | 27+ |
| Référence architecturale | 2 (shadcn/ui, Paper Shaders) |
| Solution concurrente ou alternative | la plupart |
| Dépôt appartenant au porteur | 2 (`my-own-connaissance`, `mathverse`) |

---

## 2. Les deux dépôts du porteur

| Dépôt | Rôle | Contenu | Licence |
|---|---|---|---|
| **`Stane316/my-own-connaissance`** | **corpus source** — la matière première du projet | 29 documents, 80 330 lignes, 2 354 équations | ❌ **aucune** |
| **`Stane316/mathverse`** | **dépôt de travail** — le présent dépôt | audit, outils, livrables | ❌ **aucune** |

✅ Vérifié par l'API GitHub le 2026-10-19 (`docs/decisions/0002`) : `my-own-connaissance` est
**public**, créé le **2026-10-17**, sans `LICENSE`, sans `README`, sans description, 0 étoile,
0 fork, un seul commit (`f0f5e2d`).

⚠️ **Conséquence juridique** : un dépôt public sans licence est soumis au droit d'auteur par défaut.
Le contenu est *visible*, il n'est pas *réutilisable*. C'est le point bloquant n°1 —
voir `09-KNOWN-ISSUES-AND-RISKS.md` §1.

---

## 3. Famille A — bibliothèques de composants web

### 3.1 shadcn/ui — la référence architecturale

| | |
|---|---|
| Dépôt | `shadcn-ui/ui` |
| Licence | ✅ **MIT** |
| Étoiles | 125 966 |
| Rôle pour le projet | **référence architecturale** — le format de registre |

**Pourquoi elle compte.** shadcn/ui a établi qu'un **article de registre** — un objet décrivant
fichiers, chemins cibles et dépendances — suffit à créer un écosystème interopérable. Ce format est
devenu un standard de fait : React Bits l'émet via `jsrepo`, Shaders l'utilise pour sa CLI, Paper
Shaders publie un `registry.json` au schéma shadcn.

**Éléments réutilisables :** le schéma de registre (fondement du différenciateur D6), le modèle
copier-coller.
**Éléments étudiés seulement :** tout le reste.
**Différence avec notre solution :** shadcn/ui n'expose aucune équation, hypothèse ni domaine de
validité. C'est **le seul acteur à la fois ouvert, massif et sans restriction de redistribution**.

### 3.2 React Bits — le modèle de popularité, avec un piège

| | |
|---|---|
| Dépôt | `DavidHDev/react-bits` |
| Licence | ⚠️ **MIT + Commons Clause** — **n'est pas open source** |
| Étoiles | 49 807 (relevé 2026-10-21) |
| Rôle | concurrente directe sur le créneau « composants animés » |

**Pourquoi elle compte.** C'est la référence de popularité du créneau, et le modèle de ce que le
projet veut éviter : **un titre rassurant (« MIT ») associé à une clause qui retire la qualification
open source**. Le registre des licences y voit le premier des trois mécanismes de présentation
trompeuse.

**Éléments étudiés :** la licence (pour la critiquer), le volume (215+ composants), les cinq outils
en ligne.
**Éléments repris :** ⚠️ **aucun** — la licence l'interdirait.

### 3.3 Paper Shaders — le meilleur acteur ouvert du secteur

✅ Vérifié le **2026-10-21** (`F11-shaders-et-openshaders.md` §17, recommandation R7).

| | |
|---|---|
| Dépôt | `github.com/paper-design/shaders` |
| Licence | ✅ **Apache-2.0**, sans piège identifié |
| Étoiles / forks | 3 793 / 166 |
| Créé / dernière activité | 2024-10-09 / **2026-10-20** — actif |
| npm | `@paper-design/shaders` 0.0.81 (2026-09-17), **0 dépendance**, 859 Kio |
| Contenu | monorepo : `packages/shaders` (zéro dépendance), `packages/shaders-react`, `docs` |
| Effets | **30** (30 fichiers source, 30 définitions, 30 items dans `registry.json`, 30 vignettes) |
| `llms.txt` | ✅ déployé — paramètres typés min/max/enum |

**Points forts :** zéro dépendance vérifiée sur npm, registre au schéma shadcn, `llms.txt` pour les
agents IA, usage commercial **sans attribution visible**, redistribution permise moyennant
conservation de `LICENSE` + `NOTICE`.

**Limites :** version `0.0.x` — le README recommande d'épingler la dépendance, « breaking changes
under 0.0.x ». WebGL, pas WebGPU. Projets communautaires « dans le futur ».
⚠️ **Aucune équation, aucune hypothèse, aucun domaine de validité.**

**Conclusion pour le projet :** c'est le meilleur acteur ouvert du secteur, **et il s'arrête
exactement là où Mathemirum veut commencer.**

### 3.4 OpenShaders — une promesse sans code

✅ Vérifié le **2026-10-21** (`F11` §17).

| | |
|---|---|
| Dépôt | `github.com/openshaders/openshaders` |
| Licence | MIT |
| Étoiles | 277 |
| Créé / dernière activité | 2026-09-06 / **2026-09-09** — arrêté depuis deux mois |
| **Contenu** | ⚠️ `.github/`, `LICENSE`, `README.md` — **aucun code**, 3 commits, un seul contributeur |
| npm | ❌ **aucun paquet** |

⚠️ **Ses 277 étoiles récompensent une promesse**, adossée à la notoriété de React Bits (son auteur
est `DavidHDev`). Le site `openshaders.com` est une campagne de réservation de nom d'utilisateur.

**Régime défavorable :** la page `/about` indique *« Creators will choose the licenses for their own
shaders »* — **exactement la même structure de risque que Shadertoy et GLSL Sandbox.**

### 3.5 Autres plateformes de la famille A

| Plateforme | Licence | Étoiles | Signal |
|---|---|---|---|
| **Uiverse** | MIT | 13 585 | ⚠️ **inactif depuis 2024-09-02** ; 7 456 éléments |
| **Magic UI** | MIT | — | — |
| **Motion Primitives** | MIT | — | — |
| **Motion** | MIT | — | animation |
| **Aceternity UI** | ⚠️ **propriétaire — redistribution interdite** | — | annonce le MCP dès le palier gratuit. ⚠️ Une dizaine d'annuaires l'annoncent à tort sous MIT |

---

## 4. Famille B — moteurs et bibliothèques mathématiques

| Plateforme | Dépôt | Licence | Étoiles | Signal |
|---|---|---|---:|---|
| **three.js** | — | MIT | — | rendu 3D, référence du secteur |
| **react-three-fiber** | — | MIT | — | pont React ↔ three.js |
| **D3** | — | ISC | — | visualisation de données |
| **Observable Plot** | — | — | — | — |
| **Manim** (communauté) | `ManimCommunity/manim` | MIT | 41 698 | **sortie vidéo** |
| **MathBox** | `unconed/mathbox` | MIT | 1 505 | WebGL, ⚠️ **inactif depuis 2023-05-05** |
| **p5.js** | `processing/p5.js` | ⚠️ **LGPL-2.1** | — | copyleft faible |
| **JSXGraph** | `jsxgraph/jsxgraph` | ⚠️ **LGPL-3.0** | — | copyleft faible |
| **CindyJS** | — | Apache-2.0 | — | géométrie dynamique |
| **Motion Canvas** | `motion-canvas/motion-canvas` | MIT | 19 393 | **sortie vidéo** |

### Les plateformes fermées — hors matrice, mais incontournables

✅ Source : `A9-comparaison-transversale.md` §5, `A9-registre-des-licences.md`.

| Plateforme | Régime | Pourquoi elle compte |
|---|---|---|
| **Desmos** | gratuit = **non commercial**, 90 jours d'essai, licence **révocable**, pas de cadrage ni de miroir | référence de l'expérience utilisateur |
| **GeoGebra** | **4 régimes** : EUPL-1.2 (code), non commercial (installateurs + web), CC BY-NC-SA (ressources), **co-propriété des productions générées** | ⚠️ son moteur est publié sur GitHub **sans licence déclarée** — « le contre-modèle de ce que Mathemirum doit faire » |
| **Wolfram** | propriétaire ; gratuit = pré-production | profondeur de calcul inatteignable |
| **CoCalc** | ⚠️ `LICENSE.md` = **MS-RSL** — usage de référence uniquement | écarté |
| **Shadertoy** | CC BY-NC-SA 3.0 **par défaut**, par auteur — pas de régime unifié | ⚠️ la structure de risque qu'OpenShaders reproduit |

---

## 5. Famille C — génération par IA

✅ Constat majeur : **les sept projets étudiés sont tous sous MIT, et tous produisent de la vidéo.**

| Projet | Licence | Sortie | Signal |
|---|---|---|---|
| **Math-To-Manim** (`HarleyCoops`) | MIT | **MP4** | chaîne d'agents IA → scènes Manim ; **CLI** ; produit un « dossier mathématique » mais ⚠️ **n'expose pas les hypothèses de validité**. C'est le seul à avoir une étape de vérification distincte |
| **Manimly** | — | MP4 / WebM / GIF | studio IA navigateur, sans code |
| **Manimator** (arXiv 2507.14306) | — | vidéo | système agentique, article + code de démonstration |
| **MathViz-E** | — | — | — |
| **ExcaliMath** | MIT | **composant React** | KaTeX + Plotly greffés sur Excalidraw |
| **JMathAnim** (Codeberg) | GPL | MP4 / PNG / SVG | moteur 2D en Groovy/Java |
| **reactive-manim** | — | vidéo | — |

**Ce que cette famille apprend au projet :**
- ✅ la boucle prompt → composant → test **n'est fermée par personne** (fondement de D7) ;
- ✅ produire une **vidéo** rend le test impossible ; produire un **composant web** le permet ;
- ⚠️ l'« aptitude à l'IA » (MCP, `llms.txt`) est un critère de choix **apparu en 2026**, avec un
  risque de cycle de mode.

---

## 6. L'homonyme : MathVerse (`sadeepas`)

⚠️ **À ne pas confondre avec le présent dépôt.**

| | |
|---|---|
| Dépôt | `sadeepas/MathVerse-An-Interactive-Suite…` |
| Licence | ❌ **aucune** — tous droits réservés |
| Rôle | homonyme du benchmark ECCV 2024, étudié pour documenter la collision de nom |

Inscrit au registre des plateformes comme l'un des trois cas de « dépôt public sans licence ». Sa
réutilisation est illicite par défaut.

---

## 7. Synthèse : ce que la veille a établi

| Conclusion | Statut |
|---|---|
| La case « équations et hypothèses » est vide sur **27 plateformes sans exception** | ✅ |
| La case « limites connues » est **la plus vide** de la matrice | ✅ |
| Une seule affirmation de performance trouvée, non vérifiée | ✅ |
| **Trois mécanismes** de présentation trompeuse des licences | ✅ |
| La boucle prompt → composant → test n'est fermée par personne | ✅ |
| Le secteur est majoritairement ouvert, **au moins en apparence** | ✅ |
| ⚠️ **Aucune plateforme n'a été installée ni exécutée** | ⚠️ limite de méthode |
| ⚠️ 27 plateformes observables ≠ l'écosystème entier | ⚠️ **aucune preuve d'absence** |

---

## 8. Disponibilité des références

⚠️ L'environnement restreint l'accès réseau à `github.com`, `codeload.github.com`,
`api.github.com`, `registry.npmjs.org`, `pypi.org` et `files.pythonhosted.org`.

| Référence | Accessible depuis l'environnement |
|---|---|
| Dépôts GitHub, API GitHub, npm, PyPI | ✅ oui |
| Sites de démonstration des plateformes (reactbits.dev, uiverse.io…) | ⚠️ via `fetch_page` uniquement ; `curl` direct bloqué |
| Exécution d'une quelconque plateforme | ❌ non |
