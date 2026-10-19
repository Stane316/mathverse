# FICHE DE DOMAINE I — CALCUL DIFFÉRENTIEL

**Fiche 5 / 29** — Phase 1 (audit documentaire et technique)
Date de rédaction : 2026-10-19
Statut : **rédigée sur un document restauré** — non validée par l'auteur
Document source : `Maths-vers-Informatiques/Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md` (dépôt `my-own-connaissance`)

> **Note de traçabilité.** Rédigée **après** application des lots 3a, 3b et 3c (204 blocs).
> C'est la quatrième fiche produite dans l'ordre « restaurer puis documenter » validé le
> 2026-10-18, et la **dernière du lot ordonné D → I → L → N** fixé par l'auteur
> (D ✓ · L ✓ · N ✓ · **I**).

---

## 1. Identification et volume

| Mesure | Valeur |
|---|---:|
| Lignes | **3 169** |
| Octets | 60 549 |
| Octets / ligne (moyenne) | 19 |
| Sections numérotées (`# 0 —` → `# 180 —`) | **181** |
| Titrages `#` (dont le titre de document) | 182 |
| Sous-titrages `##` | 4 |
| Blocs d'équations display `\[…\]` | **318** |
| Blocs de code (```) | **0** |
| Équations inline `$…$` | 0 |

### État du formalisme après restauration

| | Valeur |
|---|---:|
| Restaurations appliquées | **204** (lots 3a : 62 · 3b : 133 · 3c : 9) |
| Blocs **sans contenu** | **27** |
| Blocs à lettre seule | 10 — **ce sont les blocs de la Grande Carte** (§177, `A`…`I`) |
| Point absorbé (`\[ . \]`) | **0** — artefact propre au domaine L, absent ici |
| Mojibake | 0 |

> **Rectification.** Le README annonçait « blocs vides 44 → 27 » pour ce document. Ces deux
> chiffres étaient faux. Mesure de référence prise sur le **blob exact** cité par l'en-tête du
> diff (`index 9aa1df2…`) : 318 blocs, **59** sans contenu avant restauration, **27** après.
> La reconstruction est fidèle ; seuls les chiffres publiés étaient erronés.
>
> **Et une seconde correction, plus générale** : le décompte de tous les documents confondait
> « bloc sans contenu » et « bloc à un seul caractère ». Un bloc comme `\[ x \]` ou `\[ A \]`
> n'est pas vide. Sur les cinq documents instruits, **44 blocs comptés comme vides tiennent en
> réalité un seul caractère**. Le total réel est de **127 blocs sans contenu**, non 171.

---

## 2. Objectif déclaré et couverture

Le document s'ouvre (§0.2) sur une définition serrée :

> « Le calcul différentiel étudie la manière dont une quantité varie lorsqu'une autre quantité
> varie. » — et : « La notion centrale est celle de **dérivée**. »

Le sous-titre annonce l'orientation : **« Cartographie complète pour le machine learning »**.
Ce n'est pas un traité de calcul différentiel ; c'est un traité de calcul différentiel **vu
depuis le machine learning**, et c'est ce qui le rend directement utile au projet.

Le §2 organise le domaine en **neuf familles** (A à I) : fondements · calcul à une variable ·
calcul multivariable · approximation locale · optimisation · différenciation automatique ·
applications · apprentissage · synthèse.

### Structure réelle en six blocs

| Sections | Contenu | Volume |
|---|---|---|
| 0–3 | Identité, place dans la cartographie, grande cartographie, vocabulaire | intro |
| 4–25 | Une variable : fonctions, limite, continuité, dérivée, règles, chaîne, dérivées d'ordre supérieur, Taylor | socle |
| 26–52 | Multivariable : dérivée partielle, gradient, dérivée directionnelle, différentielle, Jacobienne, Hessienne, points critiques, convexité | socle |
| 53–73 | Optimisation : descente de gradient, learning rate, momentum, Adam, Newton, quasi-Newton, contraintes, Lagrange, KKT | cœur ML |
| 74–95 | Machine learning : chaîne fondamentale, backpropagation, graphe de calcul, autodiff, vanishing/exploding, activations, paysage de perte | cœur ML |
| 96–145 | Étendu : différenciation des tenseurs, JVP/VJP, simulation, EDO, RL, stabilité numérique, les trois approches de différenciation, connexions à six domaines | transversal |
| 146–180 | Applications, projets, exercices, erreurs conceptuelles, synthèses | clôture |

---

## 3. Ce qui est remarquablement aligné avec le projet

### 3.1 Quatre projets qui sont des cahiers des charges de composants

C'est le document du corpus qui fournit les **spécifications de composants les plus
directement exécutables** — elles donnent la fonction, les éléments à afficher et l'objectif
pédagogique.

| Section | Projet | Éléments demandés | Objectif énoncé |
|---|---|---|---|
| §154 (l. 2440) | **Visualisateur de dérivée** | fonction, **tangente**, pente, valeur de la dérivée — exemples `x²`, `√x`, `eˣ` | « comprendre visuellement la dérivée » |
| §155 (l. 2461) | **Visualisateur de gradient** | surface `f(x,y)`, **courbes de niveau**, gradient, direction de descente, **trajectoire d'un optimiseur** | « visualiser la relation entre gradient et optimisation » |
| §160 (l. 2544) | **Visualisation de Hessienne** | surface, gradient, Hessienne, **valeurs propres**, **directions principales** | « relier calcul différentiel et algèbre linéaire » |
| §161 (l. 2562) | **Optimisation sous contrainte** | `f(x,y)` sous `g(x,y)=0`, visualisation des deux | — |

Les trois premiers sont des composants **complets et paramétrables** : entrée mathématique,
sortie visuelle, et réglages implicites (choix de la fonction, pas de l'optimiseur, point de
départ).

### 3.2 §109 — le gradient comme normale : la base mathématique des SDF

```
Pour une surface implicite  F(x,y,z) = 0
le gradient                 ∇F
est normal à la surface sous les conditions régulières appropriées.
```

C'est l'énoncé exact qui fonde le **raymarching**, les **signed distance fields** et le
calcul des normales dans un shader. Le document ajoute : « Le calcul différentiel rejoint
ainsi directement la géométrie computationnelle. »

### 3.3 §151–153 — l'animation, avec le bon niveau de dérivée

- §151 : trajectoire `x(t)` → vitesse `v(t)=x'(t)` → accélération `a(t)=x''(t)`.
  « Le contrôle de l'accélération permet d'obtenir des animations plus naturelles. »
- §152 : interpolation — ce sont les propriétés de `f'(t)` et `f''(t)` qui permettent de
  contrôler vitesse, accélération, **fluidité**, **continuité du mouvement**.
- §153 : une transition peut être continue, dérivable, deux fois dérivable ;
  « une transition visuellement fluide peut nécessiter plus qu'une simple continuité. »

**C'est la théorie des fonctions d'easing, écrite explicitement** — avec le critère C¹/C² qui
distingue une transition correcte d'une transition agréable.

### 3.4 §29–31 — le gradient comme grandeur d'entrée

`‖∇f(x)‖` mesure l'intensité maximale de variation ; la direction de descente maximale est
`−∇f(x)` ; la dérivée directionnelle vaut `D_u f(x) = ‖∇f(x)‖ cos θ`. Trois grandeurs
directement exploitables pour piloter un paramètre visuel.

### 3.5 §150 — optimisation dans un moteur 3D

Position, rotation, paramètres de caméra, paramètres de matériau, éclairage, géométrie :
« le gradient indique comment modifier ces paramètres pour réduire une erreur. »

### 3.6 §107 et §146

- §107 : le calcul différentiel intervient dans l'animation, l'optimisation de formes, la
  reconstruction 3D, **le rendu différentiable**, l'estimation de paramètres, **l'inverse
  rendering**, la simulation, le contrôle.
- §146 : après une liste d'applications web indirectes (recommandation, ranking,
  personnalisation…), le document écrit : « Il peut également intervenir **directement** dans
  des applications graphiques et interactives avancées. »

---

## 4. Équations : état détaillé

### 4.1 Régime de dégradation

I relève du **régime 1** (commandes LaTeX détruites avec leurs arguments) et du **régime 2**
(lettres grecques détruites). Les blocs `\[…\]` survivent, réduits à un résidu.

### 4.2 Les blocs restants sont concentrés en fin de document

Sur les 27 blocs sans contenu, **la majorité appartient aux sections de synthèse** :

| Section | Blocs sans contenu |
|---|---:|
| §180 — Synthèse finale | **8** |
| §178 — Relation entre G, H et I | 4 |
| §171 — Ce qu'il faut absolument retenir | 4 |
| §176 — Différencier trois niveaux | 3 |
| 8 autres sections | 1 chacune |

**Conséquence : ce sont les conclusions du document qui ont le plus souffert.** Les sections
de cours (§4–§145) sont largement intactes ; les synthèses finales, qui devraient porter la
formule la plus紧凑 du domaine, sont les plus vides.

Le cas le plus dommageable est **§180 « Synthèse finale » (l. 3107)** :

```
Son idée fondamentale est :
\[ \]
```

**Le bloc qui devait porter l'idée fondamentale du domaine est vide.** Les cinq blocs qui
suivent (`f(x)→f'(x)`, `f(x)→∇f(x)`, `F(x)→J_F(x)`, `f(x)→H_f(x)`, `f(x)→x−η∇f(x)`) ont,
eux, survécu — de sorte que l'idée fondamentale est perdue mais que son développement
subsiste.

### 4.3 Quatre blocs jamais soumis — et une fausse alerte

La mesure de couverture lot par lot révèle **quatre blocs vides absents de tous les lots**,
tous situés juste après les neuf blocs qu'a restaurés le lot 3c, dans la zone charnière entre
§177 (Synthèse des domaines précédents) et §178 (Relation entre G, H et I). Ce n'est pas un
reste : c'est une lacune de couverture.

**Une fausse alerte est à signaler, parce qu'elle a d'abord été publiée.** Une première mesure
avait annoncé cinq lacunes, dont une en §106 « Hessian-vector product ». C'était faux : le bloc
§106 contient `\[ H \]`, qui a survécu (« Plutôt que construire `H`, on peut calculer `Hv` »).
Il avait été compté comme vide uniquement parce qu'une lettre seule tient en un caractère.
**Toute la mesure des lacunes a été refaite avec la définition stricte** (contenu de longueur
nulle, ou réduit au point absorbé) : le corpus compte **4 lacunes, toutes dans ce document**,
et non 18 comme annoncé initialement.

---

## 5. Lacunes relevées

1. **Navier–Stokes : toujours introuvable — et le constat s'aggrave.** `navier` = 0, `CFL` = 0,
   `shader` = 0. La section §110 « Simulation physique » se réduit à **deux équations** :
   `ẋ = v` et `v̇ = a`, suivies d'une liste de six mots (mouvement, vitesse, accélération,
   forces, dynamique des systèmes). **C'est de la cinématique du point matériel, pas de la
   dynamique des fluides.** C'est la quatrième fiche qui le constate (K, L, N, I).
   → **La famille 5 (simulations) devra être sourcée hors corpus, sans équivoque.**

2. **Aucune implémentation.** 0 bloc de code sur 3 169 lignes, alors que le document décrit
   huit projets, six niveaux d'exercices et « un mini réseau neuronal sans autodiff » (§158).

3. **Le vocabulaire de la rigueur est quasi absent** : `garantie` **1**, `borne` **0**,
   `hypothèse` 5, `validation` **1**, et **`précision` 0 occurrence**. Pour un document qui
   traite de stabilité numérique (§131), de conditioning (§54, §94) et de convergence
   (§125–126), l'absence totale du mot « précision » est un manque structurel.

4. **Conventions de normalisation non déclarées**, comme en L et N.

5. **GPU : 1 occurrence. Visualisation : 2.** Le document parle de rendu différentiable et
   d'inverse rendering sans jamais mentionner le matériel qui les rend possibles, ni un
   langage de shader.

6. **Aucune référence bibliographique.**

7. **Les fiches de deep dive annoncées au §170 ne sont pas rédigées.**

---

## 6. Fiabilité, cohérence, traçabilité

**Cohérence interne : forte.** La progression est rigoureuse et sans rupture : une variable →
multivariable → optimisation → machine learning → tenseurs → applications. La cartographie du
§2 en neuf familles est respectée par le plan réel.

**Statut de carrefour : démontré.** Six sections de connexions explicites (§140–145) vers
l'algèbre linéaire, la géométrie, les probabilités, les statistiques, la combinatoire et la
théorie des graphes — cette dernière donnant une chaîne complète :
« théorie des graphes → graphe de calcul → différenciation → backpropagation ».

**Esprit critique présent.** Deux sections y sont consacrées : §172 « les quatre objets à ne
pas confondre » et §175 « les erreurs conceptuelles ». Le §139 compare les trois approches de
la différenciation (symbolique, numérique, automatique). C'est rare dans le corpus et
précieux.

**Traçabilité de la restauration :** 204 blocs, chacun avec confiance et justification, lots
3a/3b/3c archivés avec leurs rapports d'application.

---

## 7. Relations mathématiques ↔ usages visuels

| Section | Contenu mathématique | Usage visuel Mathemirum |
|---|---|---|
| §154 (l. 2440) | fonction, tangente, pente | **composant « visualisateur de dérivée »** — spécification complète |
| §155 (l. 2461) | surface, courbes de niveau, gradient, trajectoire d'optimiseur | **composant « visualisateur de gradient »** |
| §160 (l. 2544) | Hessienne, valeurs propres, directions principales | **composant « visualisation de Hessienne »** |
| §161 (l. 2562) | `f(x,y)` sous `g(x,y)=0` | **composant « optimisation sous contrainte »** |
| §109 (l. 1798) | `∇F` normal à `F(x,y,z)=0` | **base des SDF, du raymarching, des normales de surface** |
| §151 (l. 2391) | `x(t) → x'(t) → x''(t)` | animation : contrôle de l'accélération |
| §152 (l. 2407) | contrôle de `f'(t)` et `f''(t)` | **courbes d'interpolation et easing** |
| §153 (l. 2428) | continuité C⁰/C¹/C² | **critère de qualité d'une transition** |
| §150 (l. 2378) | gradient sur caméra, matériau, éclairage | optimisation dans un moteur 3D |
| §29–31 (l. 601) | `‖∇f‖`, `−∇f`, `D_u f = ‖∇f‖ cos θ` | grandeurs d'entrée pour paramètres ajustables |
| §107 (l. 1769) | rendu différentiable, inverse rendering | famille 5 — à sourcer |
| §110 (l. 1812) | `ẋ=v`, `v̇=a` | base cinématique — insuffisant pour les fluides |

### ⚠️ Conséquence sur la famille 5 (simulations)

Quatrième constat identique. I apporte néanmoins deux éléments que K, L et N n'avaient pas :
**le gradient comme normale** (§109), qui est la brique de rendu implicite, et **la théorie
des transitions C¹/C²** (§152–153), qui est un critère de qualité mesurable pour une
animation. Mais ni l'un ni l'autre ne constitue une simulation de fluides.

---

## 8. Index — premières lignes (I)

| l. | Contenu |
|---|---|
| 1 | `# DOCUMENT I — CALCUL DIFFÉRENTIEL` (titre de fichier) |
| 5 | `# 0 — IDENTITÉ DU DOMAINE` |
| 11 | `**Domaine I — Calcul différentiel**` |
| 15 | « étudie la manière dont une quantité varie lorsqu'une autre quantité varie » |
| 27 | « La notion centrale est celle de **dérivée**. » |
| 43 | `# 1 — PLACE DU CALCUL DIFFÉRENTIEL DANS LA CARTOGRAPHIE MATHÉMATIQUE` |
| 77 | `# 2 — LA GRANDE CARTOGRAPHIE DU DOMAINE` — neuf familles A → I |
| 3024–3040 | `\[ A \]` … `\[ I \]` — la Grande Carte, **intacte** |
| 3103 | `# 180 — SYNTHÈSE FINALE` |
| 3109 | `\[ \]` — l'idée fondamentale du domaine, **perdue** |

---

## 9. Niveau de maturité

| Dimension | Évaluation |
|---|---|
| Couverture thématique | **Très forte** — 181 sections, du fondement à la backpropagation |
| Structure pédagogique | **Très forte** — cartographie en neuf familles, respectée |
| Esprit critique | **Forte** — §139, §172, §175 : rare dans le corpus |
| Formalisme mathématique | **Bon** — 291 blocs sur 318 exploitables (92 %) |
| Exploitabilité pour Mathemirum | **Très forte** — quatre cahiers des charges de composants, la base SDF, la théorie des transitions |
| Rigueur (hypothèses, bornes, garanties) | **Faible** — borne 0, précision 0, garantie 1 |
| Implémentation | **Nulle** — 0 bloc de code |
| Références | **Nulles** |

**Verdict :** avec N, le document **le plus directement exploitable** du corpus instruit. N
fournit les chaînes de production (audio → spectre → rendu) ; I fournit les **composants
pédagogiques** et les **briques géométriques**. Les deux se complètent.

---

## 10. Besoins de documentation complémentaire

1. **Compléter le §180** — le bloc de l'idée fondamentale est le plus dommageable des 27.
2. **Traiter les cinq blocs jamais soumis** (§106, §178).
3. **Compléter les 27 blocs sans contenu**, en priorisant les sections de synthèse.
4. **Sourcer Navier–Stokes, CFL et un schéma temporel** hors corpus pour la famille 5.
5. **Ajouter le vocabulaire de la précision** : `précision` = 0 occurrence est une anomalie
   pour un document qui traite de stabilité numérique.
6. **Rédiger les projets §154, §155, §160, §161** en spécifications de composants complètes
   (paramètres, sorties, tests d'acceptation).
7. **Déclarer les conventions** de normalisation du gradient et de la Hessienne.

---

## Métadonnées de la fiche

| Champ | Valeur |
|---|---|
| Rédigée le | 2026-10-19 |
| Document source | `Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md` |
| État du document | **restauré** (lots 3a, 3b, 3c — 204 écritures) |
| Méthode | mesure directe (lignes, octets, sections, blocs), lecture intégrale du plan des 181 sections, lecture des sections listées au §7 |
| Validée par l'auteur | **Non** |
| Fiches produites | K (1/29), L (2/29), D (3/29), N (4/29), **I (5/29)** |
| Fiches restantes | 24 |
| Lot ordonné D → I → L → N | **achevé** |
