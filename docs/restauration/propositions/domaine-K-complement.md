# LOT 1 bis — COMPLÉMENT DU DOMAINE K (10 propositions)

**Date :** 2026-10-18 — **Statut :** **validé et appliqué** (11 entrées : 10 du complément + la section 166)
**Correctif :** `domaine-K-lot1bis.patch.json` (11 entrées, vérifiées par `--apply` à sec puis appliquées)
**Livrables :** `livrables/domaine-K-lot1bis.gitdiff` — **à appliquer APRÈS** `domaine-K-lot1.gitdiff`
**Numéros de ligne :** valides **après** application du lot 1 (`domaine-K.patch.json`)

> **Décision de l'auteur (2026-10-18).** Complément validé en totalité (10 entrées).
> Section 166 « FORMULE DE RÉFÉRENCE » tranchée : **les deux** — la chaîne opérationnelle
> *et* la formule itérative centrale. Le bloc retenu :
>
> `\[ \text{PHÉNOMÈNE}\to\text{CONCEPT}\to\text{RÈGLE}\to\text{PROCESSUS}\to\text{REPRÉSENTATION}\to\text{ALGORITHME}\to\text{PARAMÈTRES}\to\text{VISUALISATION}\to\text{APPLICATION},\quad x_{n+1}=f(x_n) \]`
>
> Les neuf maillons sont ceux des lignes 39-55, en forme compacte ; la formule est celle des
> sections 05.1, 20.1, 22 et 24. Le contenu est autorisé, la mise en forme LaTeX reste une
> proposition modifiable.

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

## 4. État du document K après les lots 1 et 1 bis

| | Défauts |
|---|---:|
| Défauts signalés par l'inventaire au départ | 18 |
| Défauts découverts à la lecture (présent complément) | 10 |
| **Total traité** | **30** (19 + 11) |
| **Défauts restants** | **0** |

Le document K est le premier du corpus à être **exempt de défaut détecté**. Il reste
néanmoins vrai qu'une reconstruction n'est pas une restitution : les 30 équations concernées
doivent être relues par vous, en particulier les 7 de confiance moyenne.

**Corpus : 706 défauts signalés** restants (724 au départ, 18 dans le document K).

*Précision de mesure* : l'inventaire compte 709 blocs sur la copie de travail, dont 3
provenant du fichier de traçabilité `RESTAURATION-EQUATIONS.md` — qui cite l'exemple dégradé
de Lorenz à titre d'illustration. Le chiffre retenu exclut ce fichier, qui n'appartient pas
au corpus d'origine.
