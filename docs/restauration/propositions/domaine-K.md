# LOT 1 — PROPOSITIONS DE RESTAURATION, DOMAINE K

**Date :** 2026-10-18 — **Statut :** **lot validé et appliqué** (19 entrées sur 20)
**Fichier source :** `Maths-vers-Informatiques/DOCUMENT K — FRACTALES, CHAOS & SYSTÈMES DYNAMIQUES.md` (commit `f0f5e2d`)
**Correctif applicable :** `domaine-K.patch.json` (20 entrées : ligne, ancien bloc, nouveau bloc)
**Livrables :** `livrables/domaine-K-lot1.gitdiff` (diff vérifié, applicable par `git apply`),
`livrables/domaine-K-lot1.message-commit.txt`, `livrables/RESTAURATION-EQUATIONS.md`
**Complément :** 10 propositions supplémentaires, non appliquées — `domaine-K-complement.md`
**Rappel :** il s'agit de **reconstructions**, pas de récupérations. Le contenu détruit n'existe plus dans le fichier.

---

## 0. État d'application (2026-10-18)

Lot validé par l'auteur le 2026-10-18, avec confirmation qu'une sauvegarde indépendante du
dépôt existe. Les 19 entrées de confiance haute et moyenne ont été appliquées ; la 20ᵉ
(section 166) reste en attente de l'intention de l'auteur.

**Contrainte rencontrée :** l'envoi git vers `my-own-connaissance` est refusé
(`403 — Permission to Stane316/my-own-connaissance.git denied`, puis
`403 — Resource not accessible by integration` sur l'API). Le dépôt est donc **préparé
localement** (branche `arena/restauration-equations`, commit `bb6ce27`) et livré sous forme
de diff. La procédure d'application est dans le README du chantier, §7.

---

## 1. Synthèse du lot

| Confiance | Nombre | Signification |
|---|---:|---|
| **Haute** | 14 | le fragment survivant et la forme canonique n'autorisent pas d'autre lecture raisonnable |
| **Moyenne** | 5 | forme canonique probable, mais un choix de notation ou de normalisation subsiste |
| **Inconnue** | 1 | l'intention de l'auteur est requise |
| **Total** | **20** | 18 défauts de l'inventaire + 2 défauts découverts hors inventaire |

Les 18 défauts de l'inventaire (`annexes/inventaire-defauts.csv`) sont tous traités. Deux blocs supplémentaires, non détectés par les heuristiques parce qu'ils sont courts sans être structurellement invalides (L2581, et la liste de paramètres L1150), ont été ajoutés — ce qui confirme que l'inventaire automatisé est un **plancher**, pas un décompte exact.

## 2. Nature du dommage observé dans ce document

Trois mécanismes, tous cohérents entre eux :

1. **Suppression des commandes LaTeX avec leurs arguments** : `\frac{…}{…}`, `\sum`, `\lim`, `\log`, `\lambda`, `\mathbf`. Le résultat est un membre gauche ou droit amputé (`=(y-x)`), ou un fragment (`\_i`).
2. **Suppression des lettres grecques** : σ, ρ, β ont disparu des équations de Lorenz **et** de la liste « où : » qui les définissait, laissée vide.
3. **Perte des définitions** : les blocs vides qui suivaient « où : » ou « donc : » contenaient des définitions (vecteur d'état, formule de référence) impossibles à redeviner avec certitude.

## 3. Propositions

### 3.1 Confiance haute (14)

| Ligne | Bloc actuel | Reconstruction proposée | Validation proposée |
|---:|---|---|---|
| 830 | `\[ D= \]` | `\[ D=\frac{\log N}{\log(1/r)} \]` | Sierpiński : N=3, r=1/2 → D≈1,585, compris entre 1 et 2 comme l'affirme le texte |
| 841 | `\[ D= \]` | `\[ D=\frac{\log 3}{\log 2}\approx 1{,}585 \]` | vérifier 1 < D < 2 |
| 863 | `\[ N() \]` | `\[ N(\varepsilon) \]` | N(ε) croît quand ε décroît ; pente log-log = dimension |
| 914 | `\[ =f(x,t) \]` | `\[ \frac{dx}{dt}=f(x,t) \]` | cohérence avec 20.1 (discret) et avec L3250 (même forme) |
| 920 | `\[ =F(,t) \]` | `\[ \frac{d\mathbf{x}}{dt}=F(\mathbf{x},t) \]` | se réduit à 20.2 pour x scalaire |
| 1126 | `\[ _{n}_ {i=0}^{n-1} |f'(x_i)| \]` | `\[ \lambda=\lim_{n\to\infty}\frac{1}{n}\sum_{i=0}^{n-1}\ln|f'(x_i)| \]` | carte logistique r=4 → λ=ln2≈0,693>0 (chaos) ; r=2 → λ<0 |
| 1142 | `\[ =(y-x) \]` | `\[ \frac{dx}{dt}=\sigma(y-x) \]` | (σ,ρ,β)=(10,28,8/3) → attracteur à deux lobes décrit par le texte |
| 1144 | `\[ =x(-z)-y \]` | `\[ \frac{dy}{dt}=x(\rho-z)-y \]` | points fixes en (±√(β(ρ−1)), ±√(β(ρ−1)), ρ−1) |
| 1146 | `\[ =xy-z \]` | `\[ \frac{dz}{dt}=xy-\beta z \]` | λ₁≈0,906 pour (10,28,8/3) |
| 1324 | `\[ F(x)= \_{i=0}^{n-1} a_i N(f_i x) \]` | `\[ F(x)=\sum_{i=0}^{n-1} a_i N(f_i x) \]` | convergence si a_i=gain^i, gain<1 |
| 1363 | `\[ T(x)=\_i a_i |N(f_i x)| \]` | `\[ T(x)=\sum_i a_i |N(f_i x)| \]` | T(x) ≥ 0 partout |
| 1756 | `\[ =v \]` | `\[ \frac{dx}{dt}=v \]` | cohérence dimensionnelle |
| 1760 | `\[ =a \]` | `\[ \frac{dv}{dt}=a \]` | cohérence avec la ligne précédente (Newton) |
| 3250 | `\[ =f(x,t) \]` | `\[ \frac{dx}{dt}=f(x,t) \]` | identique à 20.2 |

### 3.2 Confiance moyenne (5)

| Ligne | Bloc actuel | Reconstruction proposée | Réserve |
|---:|---|---|---|
| 924 | `\[ =` (bloc vide) | `\[ \mathbf{x}=(x_1,\ldots,x_n) \]` | le bloc suit « où : » : définition probable du vecteur d'état, mais la forme exacte n'est pas certaine |
| 1150-1152 | `- () ;` ×3, liste vide | `- (\sigma) est le nombre de Prandtl ; - (\rho) est le nombre de Rayleigh ; - (\beta) est le paramètre géométrique` *(forme révisée, cf. complément §3)* | les trois symboles sont certains (les équations les utilisent) ; les appellations sont un choix éditorial ; les valeurs usuelles (10, 28, 8/3) ne sont pas ajoutées |
| 2575 | `\[ x'= \]` | `\[ x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}} \]` | normalisation min-max vers [0,1] ; une normalisation centrée-réduite est possible |
| 2581 | `\[ x'\]` | `\[ x'\in[0,1] \]` | défaut découvert **hors inventaire** ; l'intervalle cible est probable mais non certain |
| 2951 | `\[ =f_(h,t) \]` | `\[ \frac{dh}{dt}=f_\theta(h,t) \]` | forme canonique des EDO neuronales ; l'indice (θ) est supprimé dans la source, donc reconstitué par hypothèse |

### 3.3 Confiance inconnue (1)

| Ligne | Bloc actuel | Candidats | Décision requise |
|---:|---|---|---|
| 4314 | `\[ \]` (bloc vide) | **(a)** la chaîne opérationnelle énoncée ligne 37 : PHÉNOMÈNE → CONCEPT MATHÉMATIQUE → RÈGLE OU ÉQUATION → PROCESSUS ITÉRATIF → REPRÉSENTATION NUMÉRIQUE → ALGORITHME → PARAMÈTRES → VISUALISATION → APPLICATION LOGICIELLE ; **(b)** la formule itérative centrale `x_{n+1}=f(x_n)` | l'arbitrage de l'auteur. Le titre de section est « FORMULE DE RÉFÉRENCE » et la phrase qui suit parle de « cette chaîne » : les deux lectures sont défendables |

## 4. Ce que ce lot démontre

**La reconstruction est fiable quand le fragment survivant contraint la forme.** Les équations de Lorenz, la dimension de similarité, l'exposant de Lyapunov et les sommes de bruit ne laissent guère d'alternative : les fragments (`=(y-x)`, `_{n}_`, `\_i`) sont des signatures univoques. En revanche, **tout ce qui était une définition** (vecteur d'état, paramètres, formule de référence) ne peut pas être reconstruit avec certitude — ce sont les 6 propositions de confiance moyenne ou inconnue.

## 5. Application

Le correctif `domaine-K.patch.json` contient, pour chaque entrée : le fichier, le numéro de ligne, le bloc actuel, le bloc proposé, la confiance, la justification et le test de validation.

**Le script d'application n'est pas exécuté.** Avant toute écriture dans `my-own-connaissance`, il faut :

1. votre validation de ce lot (en particulier les 6 propositions de confiance moyenne ou inconnue) ;
2. la confirmation qu'une **sauvegarde indépendante** du dépôt existe (il ne comporte qu'un seul commit) ;
3. votre accord sur le mode d'application (branche dédiée du dépôt de connaissances, ou correctif appliqué par vous).

## 6. Lot suivant

**L — Analyse numérique** (61 défauts) : c'est le socle des critères de validation du produit, et le deuxième domaine le plus utile aux composants. Suivront **I** (109) et **N** (104), en parallèle des fiches de la Phase 1.
