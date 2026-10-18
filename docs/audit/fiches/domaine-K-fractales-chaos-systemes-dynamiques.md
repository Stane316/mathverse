# FICHE DE DOMAINE K — FRACTALES, CHAOS & SYSTÈMES DYNAMIQUES

**Date :** 2026-10-18 — **Phase :** 1 (audit documentaire) — **Statut :** fiche 1/21, **partiellement vérifiée**
**Source :** `Maths-vers-Informatiques/DOCUMENT K — FRACTALES, CHAOS & SYSTÈMES DYNAMIQUES.md`
**Outils :** `tools/extract_domain.py`, `tools/check_equations2.py` ; digest complet dans `/home/user/audit/phase1/digests/`
**Convention :** ✅ vérifié par lecture ou mesure · ⚠️ attesté par le plan mais non lu en détail · ❌ absent ou perdu

---

## 1. Identification et volume

| Métrique | Valeur |
|---|---|
| Lignes / octets | 4 316 / 77 148 |
| Titres Markdown | 340 |
| Sections numérotées | **166** (de « 00 — Prédisposition d'intégration » à « 166 — Formule de référence ») |
| Équations display | 64 (dont **18 incomplètes**, 28,1 % — voir `A7`) |
| Blocs de code | **0** |
| Occurrences « hypothèse » / « validation » / « erreur » | **0** / 1 / 11 |
| Occurrences « algorithme » / « exemple » | 11 / — |

C'est le document le plus long du corpus et le plus directement utile aux familles de composants prioritaires. Sa densité en formalismes est en revanche la plus faible des documents très développés : 64 équations pour 4 316 lignes, contre 318 pour le calcul différentiel (3 177 lignes).

## 2. Objectif déclaré et couverture

Le document se présente comme une cartographie « maths → informatique → création ». Sa structure en 166 sections couvre quatre grands blocs ✅ :

1. **Fondations et vocabulaire** (00–05) : prédisposition d'intégration, identité du domaine, **distinction fractale ≠ bruit procédural** (02 — §02.1 à 02.3), place dans la pile mathématique, cartographie en 9 familles (A géométrie fractale → I rendu et interaction), vocabulaire (itération, orbite, état, trajectoire, attracteur, bifurcation, chaos déterministe, auto-similarité, dimension fractale, bruit).
2. **Fractales et systèmes dynamiques** (06–33) : auto-similarité (exacte / approximative / statistique), fractales déterministes et stochastiques, **Mandelbrot**, **ensembles de Julia**, triangle de Sierpiński, courbe et flocon de Koch, dragon curve, courbes de Hilbert et Peano, **L-systems**, **IFS**, dimension de similarité, dimension box-counting, systèmes discret/continu/multidimensionnel, points fixes et stabilité, cycles, bifurcation, route vers le chaos, exposant de Lyapunov, **attracteur de Lorenz**, intégration numérique, stabilité numérique.
3. **Bruit procédural et génération** (34–66) : propriétés d'un bon bruit, value / Perlin / simplex / Worley, **fBm**, lacunarité, turbulence, **domain warping**, bruit multi-échelle, terrain / nuages / végétation procéduraux, seed et reproductibilité, systèmes à agents, automates cellulaires, émergence, shaders et fractales, shaders et bruit, particules, **champs de vecteurs**, systèmes de fluides, eau, animation procédurale, chaos comme outil créatif, LOD, performance, **CPU vs GPU**, **précalcul vs temps réel**, architecture d'un générateur procédural, paramétrisation, **validation d'un générateur**, déterminisme et debugging.
4. **Création, ingénierie et synthèse** (117–166) : robotique, contrôle, jeux, création d'expériences génératives, **règle de conception « modèle avant effet »** (121), **règle « simple règle, complexe résultat »** (122), moteur d'origininalité, matrice d'idéation, **connexions avec les domaines J, G, H, I, C, D, E, F** (126–133), **tests unitaires / stabilité / performance / documentation d'un générateur** (135–138), fiches de référence, projets progressifs, exercices, niveaux de maîtrise, synthèse.

⚠️ Les blocs 3 et 4 sont attestés par le plan ; leur contenu n'a pas encore été lu section par section.

## 3. Ce qui est remarquablement aligné avec le projet

Trois sections méritent d'être citées dès maintenant, car elles énoncent des principes que le cahier des charges formule autrement :

- **§02 — « Fractale ≠ bruit procédural »** ✅ : distinction explicite, avec une sous-section « ils peuvent être combinés ». C'est exactement la tripartition demandée par le cahier des charges (*effet artistique* / *visualisation explicable* / *simulation validée*).
- **§121 — « Règle de conception : modèle avant effet »** ⚠️ : le principe fondateur du produit (les mathématiques comme moteur, pas comme décor).
- **§135–138 — tests unitaires, tests de stabilité, tests de performance, documentation d'un générateur** ⚠️ : un squelette de stratégie de validation déjà présent dans le corpus, à confronter au protocole de benchmark du projet.
- **§67–73 — performance, CPU vs GPU, précalcul vs temps réel, paramétrisation, déterminisme** ⚠️ : à articuler avec le moteur de recommandation technique (Phase 3).

## 4. Équations : état détaillé

### ✅ Équations complètes et exploitables

| Notion | Formule (telle qu'écrite dans la source) | Ligne |
|---|---|---|
| Itération / orbite | `x_{n+1} = f(x_n)` | 342, 352, 908, 961 |
| Mandelbrot | `z_{n+1} = z_n^2 + c`, `z_0 = 0`, critère sur `|z_n|` | 515, 519, 527 |
| Julia | `z_{n+1} = z_n^2 + c`, `z_0 = x + iy` | 578, 595, 599 |
| Application logistique | `x_{n+1} = r x_n(1 - x_n)` | 1063 |
| IFS | `T(x) = Ax + b`, famille `T_1 … T_n` | 784, 793 |
| fBm | `F(x) = Σ_{i=0}^{n-1} a_i N(f_i x)` | 1324 |
| Turbulence | `T(x) = Σ_i a_i |N(f_i x)|` | 1363 |
| Domain warping | `N(x + w(x))` | 1386 |
| Terrain procédural | `h(x,y) = a_1 N(x,y) + a_2 N(2x,2y) + a_3 N(4x,4y)` | 1458 |

### ❌ Équations perdues (à réécrire)

| Notion | Ce qui reste dans la source | Ligne | Formule attendue (à valider) |
|---|---|---|---|
| Système de Lorenz (3 équations) | `= (y-x)`, `= x(-z) - y`, `= xy - z` ; liste de paramètres vide | 1142–1146 | `dx/dt = σ(y-x)`, `dy/dt = x(ρ-z) - y`, `dz/dt = xy - βz` |
| Dimension de similarité | `D =` (vide), exemple Sierpiński idem | 830, 841 | `D = log N / log(1/r)` |
| Dimension box-counting | `N()` | 863, 869 | `D = lim_{ε→0} log N(ε) / log(1/ε)` |
| Exposant de Lyapunov | `_{n}_ {i=0}^{n-1} |f'(x_i)|` | 1126 | `λ = lim_{n→∞} (1/n) Σ ln |f'(x_i)|` |
| Stabilité d'un point fixe | `|f'(x*)| < 1` (partiel, lisible) | 975 | critère complet + interprétation |
| Systèmes continu / multidimensionnel | `= f(x,t)`, `= F(·,t)` | 914, 920 | `dx/dt = f(x,t)` |

## 5. Lacunes relevées

1. **Aucune occurrence du mot « hypothèse » dans 4 316 lignes.** Pour un domaine où les résultats (chaos, dimensions, convergence) reposent sur des conditions précises, c'est un manque structurant : les énoncés sont affirmés sans leurs conditions de validité.
2. **Une seule occurrence de « validation »**, contre 11 pour « erreur ». La culture de la validation est présente en filigrane (§72) mais peu étayée.
3. **Zéro bloc de code**, y compris dans les sections « pseudocode conceptuel » (§09.2) et « algorithme conceptuel » (§11.1) : ces sections décrivent des algorithmes, probablement en prose ⚠️.
4. **Le formalisme des systèmes continus est détruit** (Lorenz, intégration, stabilité) : c'est précisément le bloc le plus délicat à implémenter et à valider.
5. **Les sections « particules », « champs de vecteurs », « fluides »** (58–60) ne contiennent **aucune équation display** : le formalisme (Euler, Navier–Stokes, advection) est absent, ce qui interdit de traiter ces sections comme une base de simulation fidèle — conformément à la mise en garde du cahier des charges.

## 6. Fiabilité, cohérence, traçabilité

- **Cohérence interne :** bonne ✅. La progression pédagogique (vocabulaire → objets → dimension → dynamique → bruit → génération → ingénierie) est claire et la distinction fractale/bruit est maintenue.
- **Traçabilité :** faible ❌. 11 occurrences de marqueurs de référence, aucune bibliographie structurée ; les formules ne sont pas attribuées.
- **Fiabilité du formalisme :** médiocre ❌, du fait des troncatures (28,1 %). Les énoncés conceptuels restent fiables ; les formules ne peuvent pas être reprises telles quelles.

## 7. Relations mathématiques ↔ usages visuels

| Bloc du document | Usage produit direct |
|---|---|
| Mandelbrot, Julia, Sierpiński, Koch, dragon, Hilbert | **Famille 1** — fractales et géométrie générative |
| L-systems, IFS, courbes de Hilbert/Peano, superformula | **Famille 2** — courbes, surfaces, structures paramétriques |
| fBm, turbulence, domain warping, terrain, nuages | **Famille 3** — arrière-plans et animations mathématiques |
| Champs de vecteurs, particules, systèmes dynamiques, attracteurs | **Famille 4** — particules, champs, forces, mouvement |
| Fluides, eau, intégration numérique, stabilité | **Famille 5** — simulations (avec réserve : formalisme absent) |
| Seed, reproductibilité, déterminisme, débogage | Exigences transverses du produit (`A11`, critères d'acceptation) |
| CPU vs GPU, précalcul vs temps réel, LOD | Moteur de recommandation technique (Phase 3) |

## 8. Index — premières lignes (K)

| Notion | Modèle | Équation | Paramètres | Algorithme | Moteur | Rendu | Composant potentiel | Tests / validation | Statut formalisme |
|---|---|---|---|---|---|---|---|---|---|
| Suite logistique | récurrence | `x_{n+1}=r x_n(1-x_n)` ✅ | `r`, `x_0`, `n` | itération | CPU (GPU pour le diagramme) | diagramme de bifurcation, série temporelle | *Bifurcation interactive* | régimes de référence selon `r` ; reproductibilité bit à bit ; sensibilité à la précision | ✅ complet |
| Ensemble de Mandelbrot | itération complexe | `z_{n+1}=z_n^2+c`, `z_0=0` ✅ | `c`, `max_iter`, seuil `|z|>2` | escape-time | **GPU** (shader) | image + palette + zoom profond | *Explorateur Mandelbrot* | symétrie par rapport à l'axe réel ; temps d'échappement connus ; stabilité en `float`/`double` | ✅ complet |
| Ensembles de Julia | idem, `c` fixe | `z_{n+1}=z_n^2+c`, `z_0=x+iy` ✅ | `c(Re,Im)`, `max_iter` | escape-time | **GPU** | animation par variation de `c` | *Julia animé* | continuité en `c` ; cas dégénérés | ✅ complet |
| Triangle de Sierpiński | IFS / chaos game | `N=3`, `r=1/2`, `D=` ❌ | profondeur, graine | chaos game, récursion | CPU ou GPU | tracé récursif animé | *Sierpiński progressif* | dimension mesurée ≈ `log3/log2 = 1,585` ; invariance d'échelle | ❌ dimension perdue |
| fBm | somme d'octaves | `F(x)=Σ a_i N(f_i x)` ✅ | octaves, lacunarité, gain, graine | sommation pondérée | CPU ou GPU | relief, nuage, texture | *Relief procédural* | reproductibilité par graine ; continuité ; contrôle de la variance | ✅ complet |
| Turbulence / warping | transformée du bruit | `T(x)=Σ a_i|N(f_i x)|`, `N(x+w(x))` ✅ | amplitude de déformation | évaluation composée | GPU | marbre, fumée, flammes | *Matière déformée* | bornes de sortie ; stabilité aux bords | ✅ complet |
| Attracteur de Lorenz | EDO 3D | ❌ perdue | `σ, ρ, β`, pas `h`, méthode | RK4 / Euler | CPU (GPU possible) | trajectoire 3D | *Attracteur de Lorenz* | divergence λ > 0 ; invariance ; comparaison RK4 vs Euler | ❌ à réécrire |
| Dimension box-counting | mesure d'échelle | ❌ perdue | `ε`, grille | comptage de boîtes | CPU | courbe log-log | *Mesure de dimension* | validation sur objets de dimension connue | ❌ à réécrire |

## 9. Niveau de maturité

| Dimension | Évaluation | Justification |
|---|---|---|
| Conceptuelle | **Élevée** | 166 sections, progression claire, distinctions utiles, vocabulaire défini |
| Pédagogique | **Élevée** | fiches de référence, projets progressifs, exercices, niveaux de maîtrise |
| Formelle | **Faible à moyenne** | 64 équations, 28,1 % incomplètes ; systèmes continus détruits |
| Exécutable | **Nulle** | 0 bloc de code, 0 pseudocode formaté |
| Validation | **Faible** | 1 occurrence de « validation » ; principes énoncés (§72, §135–137) mais non appliqués |

## 10. Besoins de documentation complémentaire

1. **Réécrire les 18 équations perdues**, avec sources de référence — en priorité Lorenz, dimension de similarité, box-counting, exposant de Lyapunov.
2. **Ajouter les hypothèses et conditions de validité** de chaque résultat (aucune occurrence du mot dans le document).
3. **Traduire les algorithmes en pseudocode exécutable** (§09.2, §11.1 et les sections de génération) — c'est le travail que le produit devra produire de toute façon.
4. **Traiter les sections « fluides » et « champs de vecteurs »** comme des pistes artistiques, pas comme des modèles validés, tant que leur formalisme n'est pas réécrit.
5. **Établir une bibliographie** pour les formules et les valeurs de référence utilisées dans les tests.

---

**Prochaines fiches (ordre prévu) :** D — géométrie computationnelle · I — calcul différentiel · L — analyse numérique · N — transformées · G — probabilités · C — algèbre linéaire · puis E, F, H, J, M, O, P, Q, R, S, U, A, B.
