# FICHE DE DOMAINE D — GÉOMÉTRIE COMPUTATIONNELLE

**Date :** 2026-10-18 — **Phase :** 1 (audit documentaire) — **Statut :** fiche 3/29, **partiellement vérifiée**
**Source :** `Maths-vers-Informatiques/DOCUMENT D — GÉOMÉTRIE COMPUTATIONNELLE.md`
**Document non restauré** — le domaine D relève du chantier distinct A–D (§6 du `README` de restauration).
**Outils :** `tools/audit-phase1/extract_domain.py` (inopérant : aucun titre), comptages manuels
**Convention :** ✅ vérifié par lecture ou mesure · ⚠️ attesté par le plan mais non lu en détail · ❌ absent ou perdu

---

## 1. Identification et volume

| Métrique | Valeur |
|---|---|
| Lignes / octets | 133 / 58 287 |
| **Titres Markdown** | **0** |
| Parties (« PARTIE I — … ») | **30** (de I à XXX) |
| Sections numérotées (« N — … ») | **122** occurrences, numéro maximal **111** |
| Équations display `\[…\]` | **0** |
| Mathématiques inline `$…$` | **0** |
| Blocs de code | **0** |
| Marqueurs de référence | 0 |

Ce document ne ressemble à aucun autre du corpus. **Il n'a pas un seul titre Markdown** :
les trente parties, les cent onze sections, les tableaux et les catalogues existent dans
le texte mais ne sont **pas balisés**. La structure est donc invisible à tout outil qui
compte les `#` — y compris `extract_domain.py`, qui n'a rien pu en extraire. Elle a été
relevée à la main.

Sa densité est extrême : 58 287 octets en 133 lignes, soit **438 octets par ligne**
contre 20 en moyenne dans le document L. Le document entier tient en une trentaine de
paragraphes-fleuves.

---

## 2. Objectif déclaré et couverture

> « L'objectif est de construire une **carte mentale opérationnelle** permettant de répondre
> à une question essentielle » ✅

Le document s'ouvre sur une chaîne fondamentale qui le situe par rapport au domaine C :
C fournit vecteurs, matrices, transformations, projections, espaces, produits scalaires ;
**D utilise ces outils pour résoudre des problèmes géométriques algorithmiques**.

**Dix grandes familles** structurent le domaine ✅ :

| | Famille | Contenu |
|---|---|---|
| A | Géométrie élémentaire | points, vecteurs, droites, segments, rayons, plans, distances, angles, orientations |
| B | Primitives géométriques | point, segment, droite, rayon, cercle, disque, rectangle, boîte englobante, triangle, plan, sphère, capsule, cylindre, cône |
| C | Relations géométriques | appartenance, colinéarité, coplanarité, orientation, proximité, distance, intersection, inclusion, séparation |
| D | Géométrie polygonale | polygones, triangulation, convexes, concaves, contours, maillages |
| E | Géométrie convexe | convexité, enveloppe convexe, séparation, support, Minkowski |
| F | Géométrie algorithmique | balayage, recherche d'intersections, plus proche voisin, recherche spatiale, enveloppe, triangulation |
| G | Structures spatiales | grille uniforme, quadtree, octree, k-d tree, BVH, R-tree |
| H | Géométrie 3D | plans, rayons, triangles, maillages, normales, visibilité |
| I | Géométrie numérique | tolérances, erreurs flottantes, dégénérescences, robustesse, prédicats robustes |

**Les trente parties** ✅ : I vue d'ensemble · II vocabulaire · III points, vecteurs et primitives ·
IV distances, normes et proximité · V orientation et prédicats · VI intersections ·
VII coordonnées barycentriques · VIII polygones · IX point dans un polygone ·
X enveloppe convexe · XI triangulation · XII structures spatiales ·
XIII SAT, collision et géométrie convexe · XIV plus proche voisin · XV balayage ·
XVI robustesse numérique et dégénérescences · XVII géométrie (maillages 3D) ·
XVIII WebGL et géométrie interactive · XIX applications par domaine ·
XX théorèmes et propriétés à reconnaître · XXI catalogue des algorithmes ·
XXII structures de données à retenir · XXIII catalogue des fiches individuelles ·
XXIV projets pratiques · XXV questions de maîtrise · XXVI défis sans IA ·
XXVII défis avec IA · XXVIII ce qu'il faut absolument retenir ·
XXIX erreurs à ne pas commettre · XXX checklist de maîtrise.

Le catalogue de fiches (partie XXIII) est organisé en **onze groupes** ✅ : A fondamen-
taux géométriques, B orientation et prédicats, C intersections, D polygones, E enveloppes
convexes, F triangulation, G structures spatiales, H collision, I 3D et rendu,
J WebGL et expériences interactives, **K robustesse**.

⚠️ Les parties XIX à XXX n'ont pas été lues ligne à ligne ; leur existence et leur titre
sont attestés par le texte, leur contenu reste à examiner.

---

## 3. Ce qui est remarquablement aligné avec le projet

Le domaine D est, de tous les documents du corpus, **le plus directement utile au produit** :
c'est le seul dont l'objet soit la fabrication d'objets visuels.

- **§87 — Applications en 3D** ✅ : « La géométrie computationnelle intervient particulière-
  ment dans : génération des géométries ; intersections ; normales ; coordonnées… »
- **§88 — Systèmes interactifs** ✅ : le document écrit explicitement que « cela correspond
  directement à la logique du système d'expérience interactive où **les entrées utilisateur
  peuvent devenir des coordonnées** », et cite « drag-and-drop spatial ; collisions ;
  particules ». C'est la description du produit lui-même.
- **Partie XVI — Robustesse numérique et dégénérescences** ⚠️ : tolérances, erreurs
  flottantes, prédicats robustes. Le document avertit qu'« une tolérance fixe n'est pas une
  solution universelle » (§71) et promeut l'**exactitude adaptative** (§74). C'est le
  pendant géométrique du §76 du domaine L.
- **Partie XXIX — Erreurs à ne pas commettre** ⚠️ : relève notamment « ignorer les segments
  de longueur nulle », « comparer naïvement des flottants », « croire qu'une tolérance fixe
  résout tous les problèmes » — trois pièges directement transposables en tests de
  composant.
- **Partie XXIV — Cinq projets pratiques** ⚠️, dont *Convex Hull Visualizer* (§98) et
  *Spatial Partitioning Lab* (§101, « créer une scène contenant des milliers d'objets…
  comparer… mesurer ») — ce dernier est un banc d'essai de performance, exactement ce que
  le cahier des charges demande.

---

## 4. Équations : état détaillé — **un troisième régime de dégradation**

C'est la découverte la plus importante de cette fiche.

Le corpus présentait jusqu'ici **deux** régimes de dégradation des équations :

| | Régime | Documents | Ce qui reste |
|---|---|---|---|
| 1 | Blocs `\[…\]` intacts, **commandes détruites** avec leurs arguments | E à U | le bloc, son squelette, les fragments (`\_`, `_{}`, `( )`) |
| 2 | Blocs `\[…\]` intacts, **lettres grecques détruites** | E à U | idem |
| 3 | **Blocs supprimés, formules aplaties en texte inline** | **A à D** | **les variables et la structure** |

Dans le document D, les blocs `\[…\]` ont été **supprimés** : il n'en reste aucun. Mais
les formules n'ont pas disparu — elles ont été **réécrites en texte inline**, chaque
symbole séparé par des doubles espaces, et **rejetées en fin de paragraphe**.

Exemple relevé à la ligne 33 (section 24, intersection rayon/plan) :

```
… 0 ≤   t   ≤ 1  0 ≤   u   ≤ 1  R ( t ) =   O   +   td  n   ⋅   X   +   c   = 0
X  n   ⋅ ( O   +   td ) +   c   = 0  t   = −   n   ⋅   d n   ⋅   O   +   c
n   ⋅   d   =   0  t   ≥ 0  C   r  ∥ P   −   C ∥   = 2   r 2  P   =   O   +   td
```

qui se recompose sans ambiguïté en :

| Formule recomposée | Usage |
|---|---|
| `R(t)=O+td,\quad t\geq 0` | rayon |
| `n\cdot X+c=0` | plan |
| `n\cdot(O+td)+c=0` | substitution |
| `t=-\frac{n\cdot O+c}{n\cdot d}` | paramètre d'intersection |
| `n\cdot d\neq 0` | condition de non-parallélisme |
| `t\geq 0` | appartenance au rayon |
| `\\|P-C\\|^{2}=r^{2}` avec `P=O+td` | intersection rayon/sphère |

Autres recompositions vérifiées, mêmes lignes 11 à 21 :

| Run relevé | Formule |
|---|---|
| `P = ( x , y )` / `P = ( x , y , z )` | `P=(x,y)`, `P=(x,y,z)` |
| `v ( v x v y )` | `v=(v_x,v_y)` |
| `S ( t ) = A + t ( B − A ), 0 ≤ t ≤ 1` | `S(t)=A+t(B-A),\ 0\leq t\leq 1` |
| `lerp( A , B , t ) = (1 − t ) A + tB` | interpolation linéaire |
| `P ( t ) = P + 0 td`, `d =   0` | `P(t)=P_0+td`, `d\neq 0` |
| `d ( P , Q ) = ( x − x ) + ( y − y ) Q P 2 Q P 2` | `d(P,Q)^{2}=(x_Q-x_P)^{2}+(y_Q-y_P)^{2}` |
| `d ( P , Q ) = ∥ Q − P ∥` | `d(P,Q)=\|Q-P\|` |
| `t = d ⋅ d ( P − A ) ⋅ d` | `t=\frac{(P-A)\cdot d}{d\cdot d}` |
| `t = ′ max(0, min(1, t ))` | `t'=\max(0,\min(1,t))` |

**Ce que ce régime détruit :** les commandes LaTeX (`\frac`, `\cdot` → parfois rendues en
Unicode `⋅`), **les lettres grecques** (`θ` : 0 occurrence, `π` : 0 occurrence dans tout le
document), les exposants et indices (aplatissement de `x²` en `x 2`), et quelques glyphes
(`≠` est perdu, remplacé par un caractère de remplacement).

**Ce qu'il préserve :** les variables, la structure, l'ordre des opérations. La barre de
fraction disparaît, mais numérateur et dénominateur restent **adjacents et dans l'ordre** —
ce qui rend la recomposition déterministe dans la plupart des cas.

### Mesures

| Mesure | Valeur |
|---|---:|
| Lignes portant un run mathématique recomposable | **22** |
| Slots « :  » où l'annonce reste mais la formule a disparu | **212** |
| Lignes du document | 133 |

Les 212 slots correspondent aux formules qui **n'ont pas** été aplaties : leur emplacement
est marqué par un « : » suivi d'un vide, et le contenu est perdu. Le document présente
donc les deux situations : des runs récupérables **et** des trous.

### Conséquence pour le chantier A–D

L'hypothèse de travail du chantier distinct était que les documents A à D étaient les plus
atteints du corpus. **C'est faux dans le cas de D, au moins partiellement** : leur notation
n'est pas détruite, elle est **déstructurée**. Une méthode de recomposition — repérer les
runs, rétablir les opérateurs, reconstruire fractions et exposants — est applicable, et
elle est *plus sûre* que la reconstruction pratiquée sur E à U, puisqu'elle part de
variables conservées et non de résidus.

⚠️ Cette conclusion est établie sur le document D seul. Elle doit être vérifiée sur
A, B et C avant d'être généralisée.

---

## 5. Lacunes relevées

1. **Zéro titre Markdown.** Trente parties, cent onze sections, onze groupes de fiches —
   aucun balisage. Le document est illisible par un outil, inexploitable en l'état par une
   IA qui segmenterait par titre, et impossible à référencer par ancre.
2. **Zéro bloc `\[…\]` et zéro mathématique inline.** Toute la notation est à l'état de
   runs aplatis ou de trous.
3. **Les lettres grecques ont été supprimées**, sans laisser le résidu `\_` observé dans
   E à U. Aucun indice ne subsiste de leur présence.
4. **Zéro bloc de code**, y compris dans les parties XXI (catalogue d'algorithmes),
   XXII (structures de données) et XXIV (cinq projets).
5. **Zéro marqueur de référence**, comme dans tout le corpus.
6. **Les 212 slots vides** ne peuvent pas être comblés par recomposition : il n'y a rien à
   recomposer. Ils relèvent de la reconstruction, comme pour E à U.
7. ⚠️ **Les parties XIX à XXX** (applications, théorèmes, catalogues, projets, questions,
   défis, checklist) n'ont pas été lues en détail.

---

## 6. Fiabilité, cohérence, traçabilité

- **Cohérence interne :** excellente ✅. La progression est exemplaire : vocabulaire →
  primitives → distances → prédicats → intersections → polygones → enveloppe →
  triangulation → structures spatiales → collision → robustesse → 3D → WebGL → applications.
  Les dix familles annoncées en ouverture sont effectivement traitées.
- **Traçabilité :** nulle ❌.
- **Fiabilité du formalisme :** **à reconsidérer** ✅/❌. Le formalisme n'est pas détruit
  mais déstructuré : 22 lignes portent des formules recomposables, 212 slots sont vides.
  Toute lecture automatique du document produirait aujourd'hui un résultat faux dans les
  deux cas — soit en manquant les runs, soit en butant sur les trous.
- **Réserve de méthode :** les recompositions proposées au §4 sont des **lectures**, pas des
  restitutions. Elles s'appuient sur l'ordre des opérandes, qui est conservé, mais la
  barre de fraction et les exposants doivent être rétablis par raisonnement.

---

## 7. Relations mathématiques ↔ usages visuels

| Bloc du document | Usage produit direct |
|---|---|
| Primitives, point vs vecteur, segment paramétrique `S(t)=A+t(B-A)` | Socle de **toutes** les familles — familles 1 à 5 |
| Distances, normes, `d(P,Q)=\|Q-P\|`, projection sur segment | **Famille 4** — particules, champs, forces, mouvement |
| Orientation, déterminant 2D, produit vectoriel, produit mixte | **Famille 2 et 3** — prédicats de tracé, remplissage, sens de rotation |
| Intersections (droite/droite, segment/segment, rayon/plan, rayon/sphère, rayon/AABB, rayon/triangle, Möller–Trumbore) | **Famille 5** — picking, lancer de rayons, sélection interactive |
| Coordonnées barycentriques | **Famille 2 et 5** — interpolation d'attributs, rasterizing, déformation |
| Polygones, test de convexité, point dans un polygone | **Famille 2** — formes, masques, aires de sélection |
| Enveloppe convexe (monotone chain, Jarvis march, Graham), triangulation (ear clipping), Voronoï | **Famille 1 et 3** — motifs génératifs, partitionnement de l'espace |
| Structures spatiales (grille, quadtree, octree, k-d tree, BVH, R-tree) | **Transverse** — performance, moteur de recommandation (Phase 3) |
| SAT, GJK, broad phase / narrow phase | **Famille 4 et 5** — collisions, simulations de particules |
| Maillages 3D, normales, représentation indexée, back-face culling | **Famille 2 et 5** — rendu, surfaces |
| WebGL et géométrie interactive, picking 3D | **Toutes familles** — la couche de rendu du produit |
| Robustesse, tolérances, exactitude adaptative | **Critères d'acceptation** transverses |

---

## 8. Index — premières lignes (D)

*Le formalisme étant déstructuré, la colonne « équation » distingue le run relevé (R) de la
formule recomposée (→).*

| Notion | Équation | Paramètres | Algorithme | Moteur | Rendu | Composant potentiel | Tests / validation | Statut |
|---|---|---|---|---|---|---|---|---|
| **Segment paramétrique** | R `S ( t ) = A + t ( B − A ), 0 ≤ t ≤ 1` → ✅ | `A`, `B`, `t` | évaluation | CPU | tracé animé du paramètre | *Segment paramétrique* | `t=0`→`A`, `t=1`→`B`, `t=0.5`→ milieu | ✅ recomposable |
| **Interpolation linéaire** | R `lerp( A , B , t ) = (1 − t ) A + tB` → ✅ | `A`, `B`, `t` | mix | CPU/GPU | morphing, transitions | *Interpolateur* | bornes ; `t∉[0,1]` ; stabilité | ✅ recomposable |
| **Distance euclidienne** | R `d ( P , Q ) = ∥ Q − P ∥` et sa forme au carré → ✅ | `P`, `Q` | racine | CPU | carte de distance | *Champ de distance* | symétrie ; identité ; invariance par translation | ✅ recomposable |
| **Projection sur segment** | R `t = d ⋅ d ( P − A ) ⋅ d`, `t' = max(0, min(1,t))` → ✅ | `P`, `A`, `B` | clamp | CPU | point le plus proche | *Aimantation sur courbe* | cas dégénéré `A=B` (**segment de longueur nulle**, §XXIX) | ✅ recomposable |
| **Orientation 2D** | déterminant — ❌ slot vide | `P`, `Q`, `R` | signe du déterminant | CPU | coloriage gauche/droite | *Prédicat d'orientation* | colinéarité ; cas entiers vs flottants | ❌ à reconstruire |
| **Intersection de segments** | deux prédicats d'orientation — ❌ slot vide | 4 points | test de signes | CPU | croisements | *Détecteur d'intersections* | sécants, parallèles, colinéaires (§XXVI) | ❌ à reconstruire |
| **Intersection rayon/plan** | R `t = − n⋅O + c / n⋅d`, `n⋅d ≠ 0` → ✅ | `O`, `d`, `n`, `c` | résolution | CPU | lancer de rayon | *Lancer de rayons* | parallélisme (`n·d=0`) ; `t<0` | ✅ recomposable |
| **Intersection rayon/sphère** | R `∥P − C∥² = r²`, discriminant → ✅ | `O`, `d`, `C`, `r` | quadratique | CPU/GPU | sphère cliquable | *Cible sphérique* | discriminant nul (tangence), négatif | ✅ recomposable |
| **Coordonnées barycentriques** | ❌ slot vide (§27) | triangle, point | pondération | CPU ou GPU | dégradé sur triangle | *Interpolation d'attributs* | somme = 1 ; signes ; point hors triangle | ❌ à reconstruire |
| **Point dans un polygone** | ray casting — ❌ slot vide | point, polygone | parité | CPU | remplissage | *Sélection de forme* | sommet, arête, extérieur | ❌ à reconstruire |
| **Enveloppe convexe** | monotone chain, Graham, Jarvis — ❌ | nuage | tri + balayage | CPU | contour animé | *Convex Hull Visualizer* (projet §98) | points alignés, doublons, cas à 1-2 points | ❌ à reconstruire |
| **Triangulation (ear clipping)** | ❌ (§46) | polygone | retrait d'oreilles | CPU | maillage | *Triangulateur* | polygone concave, auto-intersection | ❌ à reconstruire |
| **Quadtree / octree / k-d tree** | ❌ | points, profondeur | subdivision | CPU | grille adaptative | *Partitionnement spatial* | profondeur max ; dégénérescences | ❌ à reconstruire |
| **SAT (convexes)** | ❌ (§60) | 2 polygones | axes séparateurs | CPU | collision 2D | *Collision convexe* | contact exact ; objets imbriqués | ❌ à reconstruire |
| **Normale d'une face** | produit vectoriel, ordre des sommets — ❌ | 3 sommets | produit vectoriel | CPU | éclairage, culling | *Éclaireur* | orientation ; triangle dégénéré | ❌ à reconstruire |
| **Picking 3D** | rayon + intersections — ❌ | caméra, écran | lancer | CPU/GPU | sélection | *Sélecteur 3D* | précision aux bords ; objets superposés | ❌ à reconstruire |

---

## 9. Niveau de maturité

| Dimension | Évaluation | Justification |
|---|---|---|
| Conceptuelle | **Élevée** | 30 parties, dix familles, progression exemplaire, catalogues |
| Pédagogique | **Élevée** | 11 groupes de fiches, 5 projets, questions de maîtrise, défis avec et sans IA, checklist |
| Formelle | **Faible en l'état** — mais **potentiellement élevée** | 0 bloc `\[…\]` ; la notation existe sous forme de runs aplatis (22 lignes) et de trous (212 slots) |
| Exécutable | **Nulle** | 0 bloc de code |
| Validation | **Moyenne** | la partie XVI (robustesse) et la partie XXIX (erreurs) forment une vraie culture de la validation, mais non chiffrée ni automatisée |

---

## 10. Besoins de documentation complémentaire

1. **Vérifier le troisième régime sur A, B et C.** Si la déstructuration inline s'y
   retrouve, le chantier A–D change de nature : il devient une **recomposition** et non une
   reconstruction, avec un taux de réussite bien meilleur et une confiance plus élevée.
2. **Rétablir les titres Markdown.** Trente parties et cent onze sections sans balisage :
   c'est la première intervention à mener, et la moins risquée — elle ne touche pas au fond.
3. **Recomposer les 22 lignes de runs** en blocs `\[…\]`, avec la même discipline que le
   chantier E–U : confiance déclarée, justification, test de validation.
4. **Traiter les 212 slots vides** comme des reconstructions ordinaires.
5. **Documenter les lettres grecques manquantes** : supprimées sans résidu, elles doivent
   être rétablies par raisonnement, en signalant chaque restitution.
6. **Traduire le catalogue d'algorithmes (XXI) et les cinq projets (XXIV) en pseudocode** —
   le *Spatial Partitioning Lab* (§101) est un prototype de banc d'essai de performance.
7. **Lire les parties XIX à XXX**, qui n'ont pas encore été examinées : théorèmes,
   catalogues, projets, questions de maîtrise, checklist.
