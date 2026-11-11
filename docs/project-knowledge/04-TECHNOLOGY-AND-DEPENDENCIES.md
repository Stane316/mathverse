# 04 — Technologies et dépendances

**Date :** 2026-11-11 · **Commit :** `6f87baf`

---

## 1. Le fait central

✅ **Confirmé par mesure directe : le projet n'a aucune dépendance logicielle.**

```
$ ls package.json package-lock.json requirements.txt pyproject.toml setup.py Cargo.toml
(aucun fichier)
```

Il n'existe **ni manifeste de dépendances, ni gestionnaire de paquets, ni registre de versions**
dans le dépôt. Le seul code présent — 30 scripts Python — **n'utilise que la bibliothèque standard**.

Cette situation est normale et attendue : le projet est en phase d'audit, pas en phase de
construction. ⚠️ **Elle ne doit pas être présentée comme un choix d'architecture minimaliste.**
C'est un état de fait, pas une décision.

---

## 2. Technologies effectivement utilisées

### 2.1 Langage

| Technologie | Version | Rôle | Étendue |
|---|---|---|---|
| **Python 3** | non épinglée | tous les outils d'audit et de restauration | 30 scripts, ~6 400 lignes |

Modules de la bibliothèque standard employés : `os`, `re`, `sys`, `csv`, `json`, `shutil`,
`unicodedata`, `collections`, `argparse` (usage partiel).

⚠️ **Aucune dépendance tierce.** Aucun `pip install` n'est nécessaire.

### 2.2 Systèmes externes

| Système | Rôle | Statut |
|---|---|---|
| **Git** | versionnement, production et application des diffs | ✅ indispensable |
| **GitHub API** (`api.github.com`) | vérification des métadonnées de dépôts, recherche | ✅ utilisée |
| **GitHub CLI** (`gh`) | requêtes sur les dépôts et branches | ✅ utilisée |
| **npm registry** (`registry.npmjs.org`) | sondes de disponibilité de noms, métadonnées de paquets | ✅ utilisée |
| **PyPI** (`pypi.org`) | sondes de disponibilité de noms | ✅ utilisée |
| **Bash** | le script de reconstitution de l'atelier | ✅ utilisé |

### 2.3 Formats de données

| Format | Usage |
|---|---|
| **Markdown** | tout le contenu du corpus, des fiches et des rapports |
| **LaTeX** (`\[…\]`, `\(…\)`) | notation des mathématiques dans le corpus — c'est l'objet même de l'audit |
| **CSV** | inventaires structurés (`A2-inventaire-structurel.csv`, `A7-integrite-equations.csv`, `inventaire-defauts.csv`) |
| **JSON** | patchs de restauration (`.patch.json`), journaux d'application (`.journal.json`), registres |
| **`.gitdiff`** | **format de livraison** des 23 lots de restauration — le livrable opposable |
| **Mermaid** | diagrammes dans la documentation (présent dossier) |

---

## 3. Environnement d'exécution — contraintes mesurées

✅ Source : `PHASE-0-rapport-audit-initial.md` §3 et §5. Ces limites ont une conséquence directe sur
le différenciateur D4 (performances mesurées).

| Capacité | État | Conséquence |
|---|---|---|
| Accès réseau | ⚠️ **restreint** à `github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org` | `curl` direct est bloqué vers la plupart des hôtes ; utiliser `fetch_page` |
| Clone Git | ✅ disponible | le corpus est reconstituable |
| API GitHub | ✅ disponible | métadonnées vérifiables |
| **GPU** | ❌ **absent** | aucune mesure de performance GPU/WebGL/WebGPU possible ici |
| **Navigateur** | ❌ **absent** | aucun composant n'a pu être vu fonctionner |
| Exécution de code tiers | ⚠️ non recommandée | aucune plateforme n'a été installée ni exécutée |

### Conséquence sur D4

⚠️ **Les mesures de performance devront être déportées** — exécutées sur les machines du porteur ou
en intégration continue. Ce que la synthèse des différenciateurs retourne en avantage :

> C'est une difficulté, mais c'est aussi ce qui garantit que les mesures seront faites sur du
> matériel réel et déclaré.

---

## 4. Technologies étudiées, non adoptées

Cette section est la plus importante du document. ⚠️ **Aucune des technologies ci-dessous n'est
utilisée.** Elles ont été **analysées** lors de la Phase 2 pour éclairer les choix futurs. Les
présenter comme adoptées serait faux.

### 4.1 Les 27 plateformes de la matrice comparative

✅ Source : `annexes/A9-comparaison-transversale.md`. Trois familles.

| Famille | Plateformes |
|---|---|
| **A — bibliothèques de composants web** | shadcn/ui, React Bits, Aceternity UI, Uiverse, Magic UI, Motion Primitives, shaders (Paper Shaders), OpenShaders |
| **B — moteurs et bibliothèques mathématiques** | three.js, D3, Manim, Motion, react-three-fiber, MathBox, p5.js, JSXGraph, CindyJS, Math-To-Manim, Desmos, GeoGebra, Wolfram |
| **C — génération par IA** | Math-To-Manim, Aceternity (MCP), Shaders (MCP) |

Détail individuel dans `05-EXTERNAL-REFERENCES.md`.

### 4.2 Licences des plateformes étudiées — synthèse

✅ Source : `annexes/A9-registre-des-licences.md`.

| Régime | Plateformes | Ce qu'il faut retenir |
|---|---|---|
| **Ouvert sans restriction** | shadcn/ui (MIT), three.js (MIT), D3 (ISC), Manim (MIT), Motion (MIT), react-three-fiber (MIT), MathBox (MIT), Magic UI (MIT), Motion Primitives (MIT), CindyJS (Apache-2.0), **Paper Shaders (Apache-2.0)** | réutilisables |
| **Ouvert avec piège** | React Bits (**MIT + Commons Clause**, 49 807 ★ — *pas* open source), Uiverse (MIT, inactif depuis 2024-09-02), Shaders (paquet MIT ⚠️ **mais** contrat de plateforme v1.7 interdisant la revente) | **à instruire** |
| **Copyleft faible** | p5.js (**LGPL-2.1**), JSXGraph (**LGPL-3.0**) | obligations de réciprocité |
| **Fermé ou restrictif** | Aceternity (interdit la redistribution), GeoGebra (EUPL-1.2 / CC BY-NC-SA, co-propriété des productions), Desmos (non commercial, **révocable**), Shadertoy (par auteur, CC BY-NC-SA 3.0 par défaut), Wolfram (propriétaire), CoCalc (**MS-RSL**, usage de référence uniquement) | exclus ou à instruire |

⚠️ **Quatre points restent ouverts** et exigent une réponse écrite des éditeurs —
voir `09-KNOWN-ISSUES-AND-RISKS.md` §2.

### 4.3 Résultats de la vérification R7 (levée le 2026-10-21)

✅ Source : `fiches-phase-2/F11-shaders-et-openshaders.md` §17.

| | **Paper Shaders** | **OpenShaders** |
|---|---|---|
| Dépôt | `github.com/paper-design/shaders` | `github.com/openshaders/openshaders` |
| Licence | **Apache-2.0** | MIT |
| Étoiles | 3 793 | 277 |
| Création | 2024-10-09 | 2026-09-06 |
| Dernière activité | **2026-10-20** (la veille de la mesure) | 2026-09-09 — **arrêté, 42 jours** |
| Contenu | monorepo : `shaders` (zéro dépendance), `shaders-react`, `docs` | ⚠️ **`LICENSE` + `README.md`, aucun code** |
| npm | `@paper-design/shaders` 0.0.81, **0 dépendance**, 859 Kio | ❌ **aucun paquet** |
| Effets | 30 | 0 |
| `llms.txt` | ✅ déployé | ❌ |
| **Explication mathématique** | ❌ **aucune** | ❌ |

**Conclusion de la fiche :** le meilleur acteur ouvert du secteur s'arrête exactement là où
Mathemirum veut commencer — il publie 30 effets avec des paramètres typés, mais **aucune équation,
aucune hypothèse, aucun domaine de validité**.

⚠️ **OpenShaders n'existe pas encore en tant que code.** Ses 277 étoiles récompensent une promesse
adosée à la notoriété de React Bits. Son régime annoncé est en outre défavorable : *« Creators will
choose the licenses for their own shaders »* — **la même structure de risque que Shadertoy**.

---

## 5. Technologies candidates pour le produit

🔷 **Envisagé.** Aucune décision prise. Ce tableau consolide les signaux mesurés.

| Signal | Valeur | Source |
|---|---|---|
| React dominant | **83 %** d'usage ; satisfaction en baisse à 62 % | State of JS 2025 |
| GLSL vs HLSL | 60 % / 41 % | enquête Khronos 2026 |
| Linux comme plateforme de développement | **74 %** | enquête Khronos 2026 |
| Adaptation des shaders entre plateformes | **64 %** des répondants | enquête Khronos 2026 |
| Douleur n°1 des développeurs de shaders | **débogage et profilage** (53 % en top 3) | enquête Khronos 2026 |
| Critère n°1 de choix d'un paquet | **la documentation** (93 %) | étude Concordia |
| Critère apparu en 2026 | **l'« aptitude à l'IA »** (MCP, `llms.txt`) | guides 2026 |

⚠️ **Réserve de méthode, énoncée par la source elle-même** : les téléchargements npm ne mesurent pas
le choix des développeurs. Et les « guides de choix » sont du contenu éditorial — ils décrivent ce
que les rédacteurs estiment important, pas nécessairement ce que les développeurs font.

---

## 6. Ce qui a été écarté, et pourquoi

| Technologie | Raison de l'écart | Statut |
|---|---|---|
| **`mathverse` comme nom** | collision : benchmark ECCV 2024, dataset HuggingFace, paquet PyPI | ❌ écarté (reste le nom du dépôt) |
| WebGPU comme différenciateur | Shaders y est déjà, via TypeGPU | ❌ écarté |
| La course au nombre de composants | Shaders 200+, React Bits 215+, Uiverse 7 456 | ❌ écartée |
| Shadertoy comme source | licence par auteur, pas de régime unifié | ❌ écarté |
| CoCalc | MS-RSL, usage de référence uniquement | ❌ écarté |
| Aceternity UI | interdiction de redistribuer l'Item ou ses fichiers source | ❌ écarté |
| `curl` direct pour la veille | bloqué par la politique réseau du sandbox | ⚠️ contourné par `fetch_page` |

---

## 7. Résumé

| Catégorie | Technologies |
|---|---|
| **Adoptées** | Python 3 (bibliothèque standard), Git, GitHub API, Bash, Markdown, LaTeX (comme objet d'étude), CSV, JSON |
| **Testées** | les sondes npm/PyPI, le clonage, la réapplication de 23 diffs |
| **Étudiées** | 27 plateformes, dont Paper Shaders, shadcn/ui, React Bits, Math-To-Manim, three.js, D3, Manim, Desmos, GeoGebra, Wolfram |
| **Écartées** | voir §6 |
| **Envisagées** | React (83 % d'usage), un moteur de rendu non choisi, un registre au schéma shadcn |
| **Dépendances déclarées** | **aucune** |
