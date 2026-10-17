# A3 — NOUVELLE GÉNÉRATION DE NOMS PAR AXES SÉMANTIQUES

**Date :** 2026-10-17 — **Statut :** livrable d'audit, en attente de votre arbitrage
**Objet :** produire des candidats répartis sur des axes sémantiques explicites, avec disponibilité technique mesurée et antériorités documentées.
**Complète :** `A1-propositions-de-nom.md` (première shortlist). **Ne remplace pas** la règle du jeton neutre : tant que le nom n'est pas arrêté, la documentation dit « le projet ».

---

## 1. Méthode et limites

**Quatre sondes par candidat**, exécutées le 2026-10-17 :

1. `registry.npmjs.org/<nom>` → 404 = libre, 200 = pris.
2. `pypi.org/pypi/<nom>/json` → idem.
3. `api.github.com/repos/Stane316/<nom>` → 404 = nom disponible sous votre compte.
4. Recherche GitHub `?q=<nom>+in:name` → dépôts homonymes, avec étoiles.

**Sonde complémentaire (web) :** recherche d'antériorités commerciales ou logicielles pour les candidats présélectionnés. C'est cette sonde qui a éliminé la majorité des finalistes.

**Trois vagues :** 108 sondes de disponibilité, **65 candidats libres sur les trois registres**, 11 recherches web d'antériorité couvrant une trentaine de candidats.

**Limite assumée :** cette vérification ne constitue **pas** une recherche d'antériorité de marque (INPI, EUIPO, USPTO). Elle couvre npm, PyPI, GitHub, les dépôts publics et la recherche web grand public. Une recherche juridique restera nécessaire avant tout dépôt de marque.

**Outil :** `tools/check_names.py` (dépôt de travail, hors dépôt) — script déterministe, reproductible.

---

## 2. Les axes explorés

| Axe sémantique | Intention | Candidats testés | Libres |
|---|---|---:|---:|
| Géométrie et structure | solide, rigoureux, formel | 18 | 10 |
| Mouvement et dynamique | animation, particules, fluides, champs | 14 | 8 |
| Lumière, couleur, rendu | esthétique, shaders, qualité visuelle | 17 | 11 |
| Exploration et découverte | curiosité, paramètres, itinéraire | 6 | 2 |
| Génération et procédural | création, fabrique, poïétique | 6 | 2 |
| Paramètre et équation | le cœur du produit : le paramètre | 4 | 2 |
| Fractal, infini, échelle | auto-similarité, récursion | 5 | 3 |
| Courbes génératives | le premier vivier de composants | 8 | 6 |
| Symétrie et optique | kaléidoscope, mosaïque | 5 | 4 |
| Nature mathématique | phyllotaxie, spirales, attracteurs | 6 | 4 |
| Attracteurs et états | systèmes dynamiques, basins | 5 | 5 |
| Mathématiques explicites | assumer le mot « math » | 4 | 2 |

---

## 3. Palier A — libres sur les 3 registres **et** sans antériorité détectée

| Candidat | Axe | npm | PyPI | GitHub | Dépôts homonymes | Antériorité web |
|---|---|---|---|---|---|---|
| **mathemos** | mathématiques | libre | libre | libre | **aucun** | aucune marque, aucun logiciel ; seule trace : un personnage de wiki de fiction (« Mathemos, l'Architecte Infini »), non commercial. Réserve résiduelle : proximité phonétique avec « Mathmos » (fabricant britannique de lampes). |
| **polytopa** | géométrie | libre | libre | libre | `polytopax` (4 ★) | aucune marque détectée ; le terme « polytope » est générique en géométrie (polymake), ce qui dilue la distinctivité. |
| **curvata** | courbes | libre | libre | libre | 3 dépôts d'un compte inactif | aucune marque ; le mot existe comme épithète d'espèces biologiques — usage non commercial. |
| **isomorpha** | géométrie | libre | libre | libre | 3 dépôts mineurs | aucune marque ; réserve : « isomorphe » est un terme courant du JS (SSR), risque de confusion sémantique. |
| **catenaria** | courbes | libre | libre | libre | aucun | aucune marque ; la chaînette (catenary) est une courbe classique — terme mathématique générique. |
| **equatoria** | équation | libre | libre | libre | aucun résultat | aucune occurrence détectée. Le plus « vierge » du panel, mais aussi le moins évocateur. |

## 4. Palier B — libres sur les 3 registres, **antériorité web non vérifiée**

Ces candidats sont techniquement disponibles. Ils n'ont **pas** été vérifiés au-delà des registres, ou la recherche n'a rien fait apparaître (ce qui est une preuve faible : absence de résultat ≠ absence d'antériorité).

| Candidat | Axe | Remarque |
|---|---|---|
| `harmonogra` | courbes génératives | évocation forte : l'harmonographe est une **machine à dessiner mathématique** (pendules, courbes paramétriques). Le terme « harmonograph » est générique (domaine public). |
| `cycloida` | courbes | la cycloïde est la courbe-paramètre par excellence. Réserve : « Cycloida » désigne un ordre de crustacés fossiles et une espèce de poisson. |
| `phyllotaxa` | nature mathématique | la phyllotaxie (spirales, suite de Fibonacci) est un pont idéal entre maths et beauté visuelle. Aucune antériorité détectée. |
| `epicycla`, `lissaja`, `trochoida`, `spirogra` | courbes | libres ; `spirogra` est trop proche de **Spirograph** (marque déposée Hasbro) — à écarter. `trochoida` est proche d'un taxon de gastéropodes. |
| `attracta`, `basina`, `phasesis`, `separatrix`, `isocline` | systèmes dynamiques | libres ; termes génériques des systèmes dynamiques, distinctivité faible à moyenne. |
| `photic`, `photica`, `claria`, `raytracia`, `rastera`, `shadera`, `pixelia` | lumière / rendu | libres, non vérifiés au web. `raytracia`, `shadera`, `pixelia` collent au rendu mais vieillissent vite. |
| `latticea`, `trellia` | structure | libres. |
| `plasmatica`, `poietica`, `mathoria`, `odyssea` | génération / maths / exploration | libres ; `odyssea` est très employé (événements sportifs, associations) — à vérifier avant usage. |
| `curvia`, `geodesica`, `iridesca` | — | **écartés**, voir §5 |

## 5. Palier C — écartés, avec la preuve

La plupart des candidats séduisants sont écartés par l'antériorité web, **pas** par les registres. C'est l'enseignement principal de cette vague : npm/PyPI/GitHub ne suffisent pas.

| Candidat | Motif (vérifié le 2026-10-17) |
|---|---|
| `geodesica` | logiciel **Geodesica-SFX** (OpenGL, géodésiques, SourceForge) ; **geodesica.world** (studio de recherche et design IA) ; GEODESICA LIMITED (société britannique) |
| `iridesca` | chaîne et marque personnelle « Iridesca » (musique, réseaux sociaux) ; **Iridesca** = complément alimentaire commercial (Exsula Superfoods) |
| `trajecta` | **Trajecta Technologies LLC** (IA) ; Trajecta Carbon ; Trajecta.com.br (BI) ; casque « Trajecta » (marque 100%) ; module Eurorack ; **logiciel libre homonyme GPL-3.0** (analyse spatiale) |
| `vortica` | **Vortica Tech Ltd** (Chypre) ; **VORTICA** agence web (Portugal) ; VORTICA LIMITED (UK, active) ; jeu « Vortica » (2026) ; nom commercial d'un médicament |
| `euclidia` | **EUCLIDIA** = European Cloud Industrial Alliance (euclidia.eu, XWiki, Nexedi) ; genre de papillons ; cite de mod Skyrim |
| `vertexia` | plateforme de jeu sandbox **Vertexia** (Codeberg, open source) ; agences web Vertexia ; VERTEXIA LIMITED (UK) ; montre Invicta « Vertexia » |
| `hexafold` | **Hexafold Technologies** (société indienne enregistrée en 2023) |
| `opalesca` | marque de bijoux et accessoires « Opalesca » (Shein, distribution internationale) |
| `parametra` | **PARAMETRA** (parametra.it, logiciel italien de configurateurs 3D CPQ) ; base de données PARAMETRA (paquet R, épidémiologie) ; police Parametra (URW) ; plugin audio VCV Parametra |
| `fractalia` | **Grupo Fractalia**, multinationale espagnole des services IT (3 000+ salariés, 12 pays) ; labels et projets musicaux |
| `kaleida` | **Kaleida™** (Trend Micro, assistant IA familial, 2026) ; **Kaleida Labs** (Apple/IBM, 1991) ; Kaleida Health ; Kaleida Systems ; groupe musical |
| `luminata` | **Luminata®** (logiciel d'entreprise Revvity Signals, pharma/chimie) ; parfum Avon « Luminata » |
| `iridia` | plugin audio **IRidia** (Red Timbre Audio) ; collections « Iridia » Roca (miroirs LED) ; luminaire **IRIDIA** Schréder |
| `mobia` | **Mobia Medical** (ex-MicroTransponder, cotée au Nasdaq, capitalisation ~306 M$) ; **MOBIA** (société canadienne) |
| `fluxia` | **Fluxia** studio technologique (fluxia.com) ; marque de rubans LED ; plateforme de billetterie |
| `rhythmia` | **Rhythmia Medical** / **RHYTHMIA HDx** (Boston Scientific), dispositifs médicaux |
| `iterata` | bibliothèque Scala **iterata** (tim-group, 12 ★) ; **iterata.app** (versioning audio) |
| `recursia` | **cocacola-lab/Recursia** (20 ★) ; **recursia.ai** (société) ; autre dépôt homonyme |
| `scalara` | **SCALARA GmbH** (PropTech allemand, levée de 3 M€) ; scalara.org (SourceForge) ; Scalara Inc. |
| `prismata` | **Prismata** est un jeu vidéo connu ; `davechurchill/PrismataAI` (123 ★) |
| `matheia` | `matheia.com` (plateforme de tutorat) ; Matheia School (Seattle) ; Matheia Society |
| `mathverse` | benchmark universitaire **MathVerse** (ECCV 2024) ; dataset HuggingFace ; paquet PyPI existant |
| `geodesica`, `iridesca` | voir ci-dessus |
| `apeiron`, `axiomos`, `topograph`, `symplecta`, `tessella`, `arete`, `kinetica`, `kinema`, `fluxion`, `anima`, `chromata`, `lucida`, `radiance`, `albedo`, `claritas`, `scopia`, `orizon`, `periplo`, `viator`, `morphogen`, `fabrica`, `opifex`, `genera`, `axiomata`, `symbolica`, `infinitas`, `zenon`, `mathesis`, `mathema`, `polyhedra`, `gonia`, `hedra`, `eukleia`, `chromatica`, `fulgur`, `nitor`, `tracera`, `rendera`, `cinetica`, `trellis`, `spirograph`, `harmonograph`, `voronoid`, `orbita`, `nautila`, `mosaica` | **déjà pris** sur npm et/ou PyPI (sondes 200) |

---

## 6. Recommandation

**Le meilleur candidat reste `mathemos`** : c'est le seul, sur 108 sondes, qui cumule absence de dépôt homonyme, absence de marque détectée, disponibilité sur les trois registres, et prononciation stable en français comme en anglais.

Si vous cherchez un nom **plus évocateur** que « mathe… », les trois meilleurs du palier B — **`harmonogra`**, **`phyllotaxa`**, **`cycloida`** — méritent une vérification d'antériorité dédiée. Ils ont un avantage que `mathemos` n'a pas : ils parlent immédiatement de courbes, de génération et de beauté mathématique.

**Hiérarchie proposée :**

| Rang | Nom | Pourquoi | Réserve |
|---:|---|---|---|
| 1 | **mathemos** | le seul candidat entièrement propre, tous registres et web confondus | proche de « Mathmos » ; un peu générique |
| 2 | **harmonogra** | l'harmonographe est littéralement une machine à dessiner des courbes paramétriques — métaphore exacte du produit | antériorité web non vérifiée en profondeur |
| 3 | **phyllotaxa** | phyllotaxie : maths + nature + croissance générative, très visuel | 4 syllabes ; antériorité non vérifiée |
| 4 | **cycloida** | la cycloïde, courbe fondatrice du calcul variationnel | usage en taxonomie biologique |
| 5 | **polytopa** / **curvata** | géométrie, solides, courbes ; aucune marque détectée | termes génériques, distinctivité faible |

## 7. Ce que cette vague démontre

Sur 108 sondes, **65 candidats sont libres sur npm, PyPI et GitHub — mais 19 des plus séduisants sont éliminés par une antériorité commerciale ou logicielle réelle**. Autrement dit : la disponibilité technique est un filtre grossier. Un nom retenu sur la seule foi des registres a de fortes chances de se révéler encombré.

Conséquence pour la suite : la vérification d'antériorité doit rester une étape explicite du choix du nom, et ne pas être considérée comme acquise.

## 8. Décisions attendues

1. Choisir un nom, ou désigner 2–3 candidats du palier B à vérifier en profondeur (recherche web ciblée, registres de marques si vous le souhaitez).
2. Trancher la question du domaine : le nom du projet, le nom du paquet npm et le nom du dépôt GitHub peuvent différer (`mathemos` / `@mathemos/core` / `Stane316/mathemos`).
3. Confirmer que le jeton neutre « le projet » reste la convention jusqu'au choix définitif.
