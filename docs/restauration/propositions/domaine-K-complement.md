# LOT 1 bis — COMPLÉMENT DU DOMAINE K (10 propositions)

**Date :** 2026-10-18 — **Statut :** **propositions soumises à validation** — **non appliquées**
**Correctif prêt :** `domaine-K-complement.patch.json` (10 entrées, vérifiées par `--apply` à sec)
**Numéros de ligne :** valides **après** application du lot 1 (`domaine-K.patch.json`)

---

## 1. Pourquoi un complément

En relisant le document K **bloc par bloc** pour appliquer le lot 1 — et non plus seulement
les lignes signalées par l'inventaire automatique — dix autres dégradations sont apparues.
Aucune n'était détectée par les six heuristiques, pour trois raisons distinctes :

1. **Le bloc reste syntaxiquement valide** : `\[ x_0, x_1, x_2, \]` ne déclenche aucune alerte,
   la virgule finale étant le seul indice d'un `\ldots` détruit.
2. **La dégradation a eu lieu dans du texte courant**, pas dans un bloc mathématique :
   « boîtes de taille () » (l. 859).
3. **La dégradation a supprimé un symbole sans vider la parenthèse** : `(\lambda<0)` est devenu
   `(<0)`, qui reste bien formé.

**Conséquence méthodologique** : le taux réel de dégradation du corpus est **supérieur** aux
31,4 % mesurés. Pour un lot donné, les heuristiques fournissent un plancher ; seule une lecture
des blocs permet de traiter le reste. Cela rallonge chaque lot — c'est le prix de l'honnêteté.

## 2. Propositions

### 2.1 Confiance haute (8)

| Ligne | Actuel | Proposition | Validation |
|---:|---|---|---|
| 348 | `\[ x_0, x_1, x_2, \]` | `\[ x_0, x_1, x_2, \ldots \]` | la suite est infinie ; la relation de récurrence est donnée ligne 352 |
| 793 | `\[ T_1,T_2,,T_n \]` | `\[ T_1,T_2,\ldots,T_n \]` | énumération elliptique de n transformations, comme en 348 |
| 859 | « boîtes de taille () » | « boîtes de taille `\varepsilon` » | le même ε réapparaît ligne 863 dans `N(ε)` |
| 955 | `\[ f(x<sup>\*)=x</sup>\* \]` | `\[ f(x^*)=x^* \]` | corrigé en `f(x^*)=x^*` : c'est la définition d'un point fixe, énoncée ligne 953 |
| 1130 | `- (<0) : convergence ;` | `- (\lambda<0) : convergence ;` | λ < 0 ⇔ convergence des trajectoires voisines |
| 1131 | `- () : régime critique ;` | `- (\lambda=0) : régime critique ;` | λ = 0 est le seuil entre convergence et divergence |
| 1132 | `- (>0) : divergence…` | `- (\lambda>0) : divergence…` | λ > 0 ⇔ divergence exponentielle locale, critère usuel de chaos |
| — | *(cf. lot 1, l. 1150)* | forme révisée, voir §3 | — |

### 2.2 Confiance moyenne (2)

| Ligne | Actuel | Proposition | Réserve |
|---:|---|---|---|
| 869 | `\[ D {(1/)} \]` | `\[ D=\lim_{\varepsilon\to 0}\frac{\log N(\varepsilon)}{\log(1/\varepsilon)} \]` | dimension de comptage par boîtes : les fragments `{(1/)}` correspondent à `\log(1/\varepsilon)` entre accolades, mais le conditionnement exact (présence du `=`, bornes du `lim`) est reconstitué. **Test** : sur [0,1], N(ε)=1/ε → D=1 ; sur le carré, N(ε)=1/ε² → D=2 ; sur Sierpiński, D≈1,585 comme en section 17 |
| 1209 | `\[ N:^n \]` | `\[ N:\mathbb{R}^n\rightarrow\mathbb{R} \]` | `\mathbb{R}` a été supprimé deux fois ; la cible `ℝ` est la plus probable (`[-1,1]` est possible pour un bruit normalisé) |
| 1213 | `\[ N(x,y)v \]` | `\[ N(x,y)\rightarrow v \]` | l'opérateur a disparu ; la flèche est cohérente avec 1209 et avec « pour une surface 2D ». **Alternative défendable : ne rien écrire**, le bloc restant lisible en l'état |

## 3. Une révision du lot 1 déjà appliqué

En rédigeant ce complément, la forme retenue pour les paramètres de Lorenz (l. 1150) a été
**révisée**, pour s'aligner sur la convention typographique du document lui-même
(lignes 788-789 : « - (A) est une matrice ; - (b) est un vecteur de translation. ») :

| | Première proposition | Forme retenue |
|---|---|---|
| 1150 | `- \(\sigma\) (nombre de Prandtl) ;` | `- (\sigma) est le nombre de Prandtl ;` |
| 1151 | `- \(\rho\) (nombre de Rayleigh) ;` | `- (\rho) est le nombre de Rayleigh ;` |
| 1152 | `- \(\beta\) (paramètre géométrique)` | `- (\beta) est le paramètre géométrique` |

Les trois symboles et leurs appellations sont inchangés : seule la forme éditoriale diffère.
Le diff livré (`livrables/domaine-K-lot1.gitdiff`) contient la forme retenue.

## 4. État du document K après le lot 1

| | Défauts restants |
|---|---:|
| Défauts détectés par l'inventaire | 18 → **1** (section 166, en attente de votre décision) |
| Défauts du présent complément | **10** |
| **Restant si le complément est validé** | **1** |

Le corpus passe de 724 à 707 défauts détectés après le lot 1.

## 5. Ce que je vous demande

1. **Valider ou refuser** ce complément (en totalité ou entrée par entrée) ;
2. **Trancher la ligne 4312** (ancienne 4314, section 166 « FORMULE DE RÉFÉRENCE ») :
   chaîne opérationnelle de la ligne 37, ou formule itérative `x_{n+1}=f(x_n)` ;
3. me dire si la **forme révisée des paramètres de Lorenz** vous convient.
