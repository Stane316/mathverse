# ANNEXE A0 — INVENTAIRE DES ACCÈS, PREUVES ET LIMITES
**Projet :** écosystème de création web/visuelle fondé sur les mathématiques (nom de travail à confirmer)
**Date d'observation :** 2026-10-17 (fuseau local utilisateur : UTC+1, Cotonou)
**Auteur :** agent Arena (audit en lecture seule)
**Statut :** vérifié — aucune écriture effectuée dans un dépôt distant ou local

---

## 1. Accès réseau depuis l'environnement d'exécution (bash)

| Hôte | Résultat `curl` | Usage |
|---|---|---|
| `github.com` | **200** | clone / push git (non utilisé en écriture) |
| `api.github.com` | **200** | API REST (métadonnées, arbres, recherche, README) |
| `codeload.github.com` | **301/200** | archives de dépôts |
| `registry.npmjs.org` | **200** | métadonnées de paquets, recherche npm |
| `pypi.org` | **200** | métadonnées de paquets Python |
| `raw.githubusercontent.com` | **échec (000)** | contenu brut de fichiers |
| `reactbits.dev` | **échec (000)** | site de référence |
| `uiverse.io` | **échec (000)** | site de référence |
| `www.geogebra.org` | **échec (000)** | site de référence |
| `p5js.org` | **échec (000)** | site de référence |

**Contournements disponibles et testés :**
- `fetch_page` (outil de navigation) : **reactbits.dev → OK**, **uiverse.io → OK**. La veille web est donc réalisable.
- `web_search` (outil de recherche) : **OK**.
- Clone git via `github.com` : **OK** (utilisé pour le dépôt de connaissances).
- API GitHub : **OK** (utilisée pour les métadonnées et le README des dépôts tiers).

## 2. Capacités de l'environnement d'exécution

| Capacité | État | Conséquence pour le projet |
|---|---|---|
| Node | v22.22.3 | OK pour outillage JS/TS, CLI |
| npm | 10.9.8 | OK |
| Python | 3.11.2 (5 paquets installés, pas de numpy/requests) | installable depuis `pypi.org` si nécessaire |
| `gh` CLI | 2.23.0, authentifié, droits *admin* sur les deux dépôts | OK, mais **aucune écriture** en Phase 0 |
| `git` | OK, branche de travail `arena/2e20eccb-mathverse` | conforme au workflow imposé |
| Navigateur (chromium/firefox) | **absent** | pas de rendu headless local |
| GPU (`/dev/dri`) | **absent** | **aucune mesure GPU/WebGL/WebGPU fiable dans ce sandbox** |
| CPU / RAM / disque | 2 vCPU / 3,8 Gio / 20 Gio | benchmarks CPU locaux possibles mais peu représentatifs |
| `playwright` / `puppeteer` | installables via npm (1.64.1 / 25.14.0) | le téléchargement du binaire Chromium passe par un CDN **hors liste autorisée** → probablement impossible ; à vérifier en Phase 3 |

## 3. Dépôt produit — `Stane316/mathverse` (vérifié par API + système de fichiers local)

| Champ | Valeur observée |
|---|---|
| Visibilité | public |
| Créé / poussé | 2026-10-17T19:03:26Z / 2026-10-17T19:04:27Z |
| Branche par défaut | `main` |
| Commits | 1 (`bdba473` « first commit », 2026-10-17 20:04:21 +0100, auteur « Stane ») |
| Fichiers suivis | 2 fichiers Markdown |
| Arborescence | `Equations Mathématiques/equations_courbes_animees_v2.md` (21 505 o), `Equations Mathématiques/equations_courbes_mathematiques.md` (18 654 o) |
| Taille hors `.git` | 44 Kio |
| README racine | **absent** |
| LICENSE | **absente** (`license: null`) |
| `.gitignore` | **absent** |
| Topics / description | description présente, topics vides |
| Étoiles / forks | 0 / 0 |

## 4. Dépôt de connaissances — `Stane316/my-own-connaissance` (vérifié par API + clone local en lecture seule)

| Champ | Valeur observée |
|---|---|
| Visibilité | public |
| Créé / poussé | 2026-10-17T18:51:17Z / 2026-10-17T18:58:11Z |
| Branche par défaut | `main` |
| Commits | 1 (`f0f5e2d` « first commit ») |
| Contenu | **29 fichiers `.md`**, aucun fichier de code, aucune image |
| Volume | 80 301 lignes / 1 912 005 octets (≈ 1,9 Mio) |
| Arborescence | `Maths-vers-Informatiques/` (21 fichiers) + `Ai Technical Litteracy/` (8 fichiers) |
| LICENSE / README racine | **absents** |
| Copie locale | `/home/user/_audit/connaissance` (clone `--depth 1`, hors dépôt produit, non versionné) |

### 4.1 Inventaire `Maths-vers-Informatiques/`

| Domaine | Fichier | Lignes | Octets | Titres MD (`^#`) |
|---|---|---:|---:|---:|
| — | `README.md` (document maître de contexte) | 1 121 | 56 373 | 130 |
| A | `DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE.md` | 118 | 81 681 | **0** |
| B | `DOCUMENT B — THÉORIE DES NOMBRES.md` | 102 | 68 220 | **0** |
| C | `DOCUMENT C — ALGÈBRE LINÉAIRE.md` | 122 | 76 998 | **0** |
| D | `DOCUMENT D — GÉOMÉTRIE COMPUTATIONNELLE.md` | 132 | 58 287 | **0** |
| E | `DOCUMENT E — THÉORIE DES GRAPHES…md` | 2 857 | 50 829 | 295 |
| F | `DOCUMENT F — COMBINATOIRE ET OPTIMISATION COMBINATOIRE.md` | 2 944 | 53 057 | 347 |
| G | `Document G - Probabilités — Cartographie complète.md` | 3 071 | 53 939 | 348 |
| H | `Document H — Statistiques.md` | 2 661 | 47 249 | 316 |
| I | `Domaine I - Calcul différentiel — … machine learning.md` | 3 176 | 56 819 | 285 |
| J | `Domaine J — Optimisation.md` | 3 541 | 61 865 | 359 |
| K | `DOCUMENT K — FRACTALES, CHAOS & SYSTÈMES DYNAMIQUES.md` | 4 315 | 77 148 | 340 |
| L | `DOCUMENT L — ANALYSE NUMÉRIQUE.md` | 2 355 | 44 929 | 257 |
| M | `DOCUMENT M — THÉORIE DE L'INFORMATION.md` | 4 275 | 81 165 | 308 |
| N | `DOCUMENT N — TRANSFORMÉES.md` | 3 946 | 72 116 | 290 |
| O | `Document O --Théorie de la complexité.md` | 3 617 | 70 587 | 275 |
| P | `Domaine P — Cryptographie.md` | 4 119 | 72 921 | 319 |
| Q | `Domaine Q — Logique, Automates & Langages.md` | 3 141 | 59 158 | 255 |
| R | `DOCUMENT R — ALGÈBRE ABSTRAITE.md` | 2 705 | 92 929 | 269 |
| S | `DOCUMENT S — TOPOLOGIE.md` | 2 523 | 91 634 | 272 |
| U | `DOMAINE U — LOGIQUE FLOUE.md` | 2 393 | 86 952 | 197 |
| **T** | **Théorie des jeux** | — | — | **AUCUN FICHIER** |

**Preuve du domaine T manquant :** le `README.md` (maître) décrit le domaine T en section « 7.14. Théorie des jeux : T » (« La théorie des jeux permet d'étudier des situations dans lesquelles plusieurs acteurs prennent des décisions qui interagissent… »), mais aucun fichier correspondant n'existe dans l'arbre Git (31 entrées : 2 arbres + 29 blobs).

### 4.2 Inventaire `Ai Technical Litteracy/`

| Fichier | Lignes | Octets | Titres MD |
|---|---:|---:|---:|
| DOCUMENT 01 — WEB & SOFTWARE ENGINEERING | 3 892 | 75 077 | 344 |
| DOCUMENT 02 — UI UX DESIGN | 3 201 | 58 002 | 277 |
| DOCUMENT 03 — CARTOGRAPHIE DE LA CYBERSÉCURITÉ | 2 480 | 44 286 | 165 |
| DOCUMENT 04 — SEO & WEB PERFORMANCE | 2 918 | 55 463 | 213 |
| DOCUMENT 05 — AI, MACHINE LEARNING & SYSTÈMES INTELLIGENTS | 3 573 | 70 811 | 309 |
| Document 06 — Product, SaaS & Start-up | 3 783 | 70 908 | 379 |
| DOCUMENT 07 — Branding, Marketing & Personal Branding | 2 944 | 58 288 | 312 |
| DOCUMENT 08 — Architecture & Systems | 3 823 | 64 314 | 380 |

## 5. Disponibilité des noms (vérifiée le 2026-10-17)

| Cible | Nom | Résultat |
|---|---|---|
| npm | `mathverse` | **404 = libre** |
| npm | `matheon` | **404 = libre** |
| npm | `mathverse-core`, `create-mathverse` | 404 = libres |
| PyPI | `mathverse` | **200 = déjà pris** |
| PyPI | `matheon` | 404 = libre |
| GitHub | `Stane316/matheon` | 404 = nom disponible |
| GitHub | `Stane316/mathverse` | 200 = **déjà utilisé par ce projet** |

**Collisions constatées (recherche GitHub + web) :**
- `ZrrSkywalker/MathVerse` — 184 ★, licence MIT, benchmark visuel de mathématiques pour MLLM (ECCV 2024), jeu de données `AI4Math/MathVerse` sur Hugging Face.
- `sadeepas/-MathVerse-An-Interactive-Suite-of-Mathematical-Web-Applications` — 2 ★, HTML/JS vanilla, « suite d'applications web mathématiques interactives » (calculatrice graphique, probabilités…), **sans licence**, créé le 2025-11-25.
- Autres homonymes mineurs : `JieyuZ2/MathVerse`, `TheCyberUchiha/MathVerse`, `CarneiroX/Mathverse`, `DavorJordacevic/MATHVERSE_Finbet_AI` (MIT).

## 6. Opérations effectivement réalisées (journal)

1. `git status/log/ls-files` sur le dépôt produit local → état et contenu du premier commit.
2. `gh api repos/…` sur les deux dépôts → métadonnées et permissions.
3. `gh api …/git/trees/main?recursive=1` sur les deux dépôts → arborescences complètes.
4. `git clone --depth 1` du dépôt de connaissances vers `/home/user/_audit/connaissance` (lecture seule, hors dépôt produit).
5. Comptages lignes/octets/titres, extraction des plans (`^#`) de chaque document.
6. Lecture du `README.md` maître (sections 00 à 07).
7. Tests d'accès réseau (10 hôtes) et sondes npm/PyPI/GitHub.
8. `fetch_page` sur `reactbits.dev` et `uiverse.io` ; `web_search` sur le nom « MathVerse ».

**Aucune écriture, aucun commit, aucun push, aucune création de branche, aucune publication.**
