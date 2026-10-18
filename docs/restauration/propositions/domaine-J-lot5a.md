# Lot 5a — Domaine J, Optimisation

**Source :** `Maths-vers-Informatiques/Domaine J — Optimisation.md` (3 940 lignes, 332 blocs `\[…\]`, 119 blocs dégradés)
**Périmètre du lot :** sections introductives à 46 — lignes **17 à 1018**
**Statut :** propositions à valider. **Rien n'a été écrit dans le fichier source.**

## Notes de lecture

Le document J se dégrade exactement comme L, I et N : les commandes à argument
sont détruites (`\min`, `\max`, `\arg\min`, `\nabla`, `\mathbb{R}`, `\sum`,
`\frac`, `\log`, `\mathcal{L}`, `\lambda`, `\eta`, `\beta`, `\epsilon`, `\mu`,
`\theta`, `\{`), et les opérateurs de comparaison disparaissent.

Deux faits propres à J rendent la restauration plus sûre que la moyenne :

1. **La section 112 « FORMES IMPORTANTES À RECONNAÎTRE » (lignes 2237–2287) est intacte.**
   Elle énonce les huit formes canoniques du document — dont `\min_x c^Tx` sous
   `Ax\leq b`, `x_{t+1}=x_t-\eta\nabla f(x_t)` et `x_{t+1}=x_t-H^{-1}\nabla f` — et
   elle sert de référence pour les blocs détruits des sections 19, 30 et 40. C'est une
   application directe de la règle méthodologique : **chercher une structure
   équivalente survivante avant de classer un bloc « inconnue »**.
2. **Les paires sont fréquentes et s'éclairent mutuellement.** Un bloc vide qui précède
   « sous : `g_i(x)` » est un objectif ; un bloc `f(x^*)f(x)` est une inégalité dont
   le sens est fixé par le titre de sous-section (minimum → `\leq`, maximum → `\geq`).
   Le signe moins de `\_x -f(x)` (l. 247) tranche à lui seul le max/min.

Trois conventions sont récurrentes et ont été appliquées :

- `\_` = résidu de `\min`, `\max`, `\arg\min`, `\sum` ou `\int` ;
- `Axb` = `Ax\leq b`, `0x` = `0\leq x\leq 1`, `x_i{0,1}` = `x_i\in\{0,1\}` ;
- un `+` en tête de ligne d'un bloc multi-ligne devient une puce `-` dans le rendu
  Markdown : il a été rétabli en `+` (lignes 529, 825, 984).

---

**Correctif :** `domaine-J-lot5a.patch.json` — 102 entrées : 79 haute, 10 moyenne, 13 inconnue — **89 applicables**

### Confiance haute (79)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 69 | `\[ ^\* = _ L() \]` | `\[ \theta^{*}=\arg\min_\theta \mathcal{L}(\theta) \]` | Rendu : θ*=argmin_θ 𝓛(θ). |
| 75 | `\[ P^\* = \_P (P) \]` | `\[ P^{*}=\arg\min_P C(P) \]` | Rendu : P*=argmin_P C(P). |
| 99 | `\[ ^\* = _ J() \]` | `\[ \theta^{*}=\arg\min_\theta J(\theta) \]` | Rendu : θ*=argmin_θ J(θ). |
| 121 | `\[ x=(x_1,x_2,,x_n) \]` | `\[ x=(x_1,x_2,\ldots,x_n) \]` | Rendu : x=(x₁,x₂,…,x_n). |
| 135 | `\[ \_x C(x) \]` | `\[ \min_x C(x) \]` | Rendu : min_x C(x). |
| 141 | `\[ L() \]` | `\[ L(\theta) \]` | Rendu : L(θ). |
| 157 | `\[ = {x : g_i(x), h_j(x)=0} \]` | `\[ \mathcal{X}=\{x: g_i(x)\leq 0,\ h_j(x)=0\} \]` | Rendu : 𝓧={x : g_i(x)≤0, h_j(x)=0}. |
| 181 | `\[ f(x+(1-)y) f(x)+(1-)f(y) \]` | `\[ f(\lambda x+(1-\lambda)y)\leq \lambda f(x)+(1-\lambda)f(y) ` | Définition de la convexité. Le bloc suivant donne l'intervalle de λ. |
| 185 | `\[ 0 \]` | `\[ \lambda\in[0,1] \]` | Rendu : λ∈[0,1]. |
| 203 | `\[ \]` | `\[ \min_x f(x) \]` | Rendu : min_x f(x). Confirmé par les blocs suivants. |
| 207 | `\[ g_i(x) \]` | `\[ g_i(x)\leq 0 \]` | Rendu : g_i(x)≤0. |
| 227 | `\[ f(x^\*)f(x) \]` | `\[ f(x^{*})\leq f(x) \]` | Rendu : f(x*)≤f(x). |
| 235 | `\[ f(x^\*)f(x) \]` | `\[ f(x^{*})\geq f(x) \]` | Rendu : f(x*)≥f(x). |
| 243 | `\[ \_x f(x) \]` | `\[ \max_x f(x) \]` | Rendu : max_x f(x). |
| 247 | `\[ \_x -f(x) \]` | `\[ \min_x -f(x) \]` | max f ≡ min −f. |
| 257 | `\[ f(x^\*)f(x) \]` | `\[ f(x^{*})\leq f(x) \]` | Rendu : f(x*)≤f(x) dans le voisinage. |
| 263 | `\[ f(x^\*)f(x) \]` | `\[ f(x^{*})\leq f(x) \]` | Rendu : f(x*)≤f(x) pour tout x admissible. |
| 271 | `\[ x_{}^\* \]` | `\[ x_{\text{local}}^{*} \]` | Rendu : x*_local. |
| 275 | `\[ x_{}^\* \]` | `\[ x_{\text{global}}^{*} \]` | Rendu : x*_global. |
| 292 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 296 | `\[ \]` | `\[ \nabla f(x^{*})=0 \]` | Condition de stationnarité. Le bloc suivant explicite les dérivées partielles. |
| 300 | `\[ =0, , =0 \]` | `\[ \frac{\partial f}{\partial x_1}=0,\ \ldots,\ \frac{\partial` | Rendu : ∂f/∂x₁=0, …, ∂f/∂x_n=0. |
| 304 | `\[ f(x)=0 \]` | `\[ \nabla f(x)=0 \]` | Rendu : ∇f(x)=0. |
| 319 | `\[ H_f(x) = ^2 f(x) \]` | `\[ H_f(x)=\nabla^{2}f(x) \]` | Rendu : H_f(x)=∇²f(x). |
| 327 | `\[ H_f(x^\*) \]` | `\[ \nabla^{2}f(x^{*})\succ 0 \]` | Rendu : ∇²f(x*)≻0. |
| 333 | `\[ H_f(x^\*) \]` | `\[ \nabla^{2}f(x^{*})\prec 0 \]` | Rendu : ∇²f(x*)≺0. |
| 351 | `\[ f(x+(1-)y) f(x)+(1-)f(y) \]` | `\[ f(\lambda x+(1-\lambda)y)\leq \lambda f(x)+(1-\lambda)f(y) ` | Définition de la convexité, identique à la l. 181. |
| 357 | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` | Rendu : min_x f(x). |
| 369 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 373 | `\[ \]` | `\[ \nabla^{2}f(x)\succeq 0 \]` | Rendu : ∇²f(x)⪰0. |
| 381 | `\[ ^2 f(x) \]` | `\[ \nabla^{2}f(x)\succ 0 \]` | Rendu : ∇²f(x)≻0. |
| 413 | `\[ \]` | `\[ \min_x f(x) \]` | Rendu : min_x f(x). |
| 429 | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` | Rendu : min_x f(x). |
| 433 | `\[ g_i(x) \]` | `\[ g_i(x)\leq 0 \]` | Rendu : g_i(x)≤0. |
| 465 | `\[ x+y \]` | `\[ x+y\leq 10 \]` | Rendu : x+y≤10. |
| 469 | `\[ x \]` | `\[ x\geq 0 \]` | Rendu : x≥0. |
| 473 | `\[ 0x \]` | `\[ 0\leq x\leq 1 \]` | Rendu : 0≤x≤1. Encadrement, seul cas où deux inégalités sont nécessaires. |
| 481 | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` | Rendu : min_x f(x). |
| 489 | `\[ \]` | `\[ \mathcal{L}(x,\lambda)=f(x)+\lambda g(x) \]` | Rendu : 𝓛(x,λ)=f(x)+λg(x). |
| 493 | `\[ \_x=0 \]` | `\[ \nabla_x\mathcal{L}=0 \]` | Rendu : ∇_x𝓛=0. |
| 511 | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` | Rendu : min_x f(x). |
| 515 | `\[ g_i(x) \]` | `\[ g_i(x)\leq 0 \]` | Rendu : g_i(x)≤0. |
| 523 | `\[ \_i \]` | `\[ \lambda_i \]` | Rendu : λ_i. |
| 529 | `\[ (x,,) = f(x) ⏎  ⏎ - \_i_i g_i(x) ⏎ - \_j_j ` | `\[ \mathcal{L}(x,\lambda,\mu)=f(x) ⏎  ⏎ + \sum_i\lambda_i g_i(` | Rendu : 𝓛(x,λ,μ)=f(x)+Σλ_i g_i(x)+Σμ_j h_j(x). |
| 538 | `\[ \_x=0 \]` | `\[ \nabla_x\mathcal{L}=0 \]` | Rendu : ∇_x𝓛=0. |
| 542 | `\[ g_i(x) \]` | `\[ g_i(x)\leq 0 \]` | Rendu : g_i(x)≤0. |
| 548 | `\[ \_i \]` | `\[ \lambda_i\geq 0 \]` | Rendu : λ_i≥0. Condition de dualité. |
| 552 | `\[ \]` | `\[ \lambda_i g_i(x)=0 \]` | Rendu : λ_i g_i(x)=0. |
| 574 | `\[ \]` | `\[ p^{*}=d^{*} \]` | Rendu : p*=d*. |
| 584 | `\[ \]` | `\[ \min_x c^{T}x \]` | Rendu : min_x c^T x. Cohérent avec la forme 2 du §112 (l. 2243). |
| 588 | `\[ Axb \]` | `\[ Ax\leq b \]` | Rendu : Ax≤b. |
| 592 | `\[ x \]` | `\[ x\geq 0 \]` | Rendu : x≥0. |
| 632 | `\[ x_i \]` | `\[ x_i\in\mathbb{Z} \]` | Rendu : x_i∈ℤ. |
| 636 | `\[ x_i{0,1} \]` | `\[ x_i\in\{0,1\} \]` | Rendu : x_i∈{0,1}. |
| 649 | `\[ x_i{0,1} \]` | `\[ x_i\in\{0,1\} \]` | Rendu : x_i∈{0,1}. |
| 690 | `\[ x \]` | `\[ x\in\mathcal{X} \]` | Rendu : x∈𝓧. |
| 716 | `\[ DP\[s\] = \_{a} { (s,a)+DP\[s’\] } \]` | `\[ DP[s]=\min_{a}\{c(s,a)+DP[s']\} \]` | Rendu : DP[s]=min_a{c(s,a)+DP[s']}. Forme canonique de Bellman. |
| 741 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 745 | `\[ f(x) \]` | `\[ \nabla f(x) \]` | Rendu : ∇f(x). |
| 751 | `\[ -f(x) \]` | `\[ -\nabla f(x) \]` | Rendu : −∇f(x). |
| 759 | `\[ \]` | `\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]` | Rendu : x_{t+1}=x_t−η∇f(x_t). Identique à la forme 5 du §112 (l. 2269). |
| 793 | `\[ L() \]` | `\[ \nabla L(\theta) \]` | Rendu : ∇L(θ). |
| 797 | `\[ \]` | `\[ \frac{1}{\|B\|}\sum_{i\in B}\nabla L_i(\theta) \]` | Estimateur du gradient sur un mini-batch. |
| 815 | `\[ BD \]` | `\[ B\subset D \]` | Rendu : B⊂D. |
| 825 | `\[ v_t = v_{t-1} ⏎  ⏎ - f(x_t) \]` | `\[ v_t=\beta v_{t-1} ⏎  ⏎ + (1-\beta)\nabla f(x_t) \]` | Rendu : v_t=βv_{t-1}+(1−β)∇f(x_t). Identique à l. 1045 du domaine I. |
| 831 | `\[ x_{t+1} = x_t-v_t \]` | `\[ x_{t+1}=x_t-\eta v_t \]` | Rendu : x_{t+1}=x_t−ηv_t. |
| 884 | `\[ \|f(x)\|< \]` | `\[ \\|\nabla f(x)\\|<\epsilon \]` | Rendu : ‖∇f(x)‖<ε. |
| 888 | `\[ \|f(x_{t+1})-f(x_t)\|< \]` | `\[ \|f(x_{t+1})-f(x_t)\|<\epsilon \]` | Rendu : \|f(x_{t+1})−f(x_t)\|<ε. |
| 892 | `\[ \|x_{t+1}-x_t\|< \]` | `\[ \\|x_{t+1}-x_t\\|<\epsilon \]` | Rendu : ‖x_{t+1}−x_t‖<ε. |
| 896 | `\[ tT_{} \]` | `\[ t>T_{\max} \]` | Rendu : t>T_max. |
| 906 | `\[ \]` | `\[ x_{t+1}=x_t-\frac{f'(x_t)}{f''(x_t)} \]` | Newton scalaire. Le bloc suivant donne le cas multidimensionnel. |
| 910 | `\[ \]` | `\[ x_{t+1}=x_t-H^{-1}\nabla f(x_t) \]` | Identique à la forme 6 du §112 (l. 2275). |
| 918 | `\[ \]` | `\[ \nabla f \]` | Rendu : ∇f. Opposé au bloc suivant, qui ajoute la Hessienne. |
| 936 | `\[ B_tH_f(x_t) \]` | `\[ B_t\approx H_f(x_t) \]` | Rendu : B_t≈H_f(x_t). |
| 978 | `\[ \]` | `\[ \nabla_\theta L \]` | Rendu : ∇_θ L. |
| 984 | `\[ \_{t+1} = \_t ⏎  ⏎ - \_L \]` | `\[ \theta_{t+1}=\theta_t ⏎  ⏎ - \eta\nabla_\theta L \]` | Rendu : θ_{t+1}=θ_t−η∇_θ L. |
| 1004 | `\[ \]` | `\[ \min_\theta L(\theta) \]` | Rendu : min_θ L(θ). |
| 1012 | `\[ MSE = 1n \_{i=1}^{n} (y_i-y_i)^2 \]` | `\[ MSE=\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i-y_i)^{2} \]` | Rendu : MSE=(1/n)Σ(ŷ_i−y_i)². |
| 1018 | `\[ L = -\_i y_i(y_i) \]` | `\[ L=-\sum_i y_i\log(\hat{y}_i) \]` | Rendu : L=−Σ y_i log(ŷ_i). Idem l. 1510 du domaine I. |

### Confiance moyenne (10)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 41 | `\[ \]` | `\[ \text{les mathématiques} \to \text{l'optimisation} \]` | Candidat d'ouverture. La chaîne complète est à reconstituer par l'auteur : six terms, dont le dernier conduit à l'optimisation. |
| 151 | `\[ x_1+x_2 \]` | `\[ x_1+x_2\leq b \]` | Candidat alternatif : x_1+x_2\leq 10 (la borne 10 est celle de l'exemple d'égalité du §14). |
| 215 | `\[ \]` | `\[ \min_x f(x) \]` | Candidat alternatif : \[ \min_{x\in\mathcal{X}}f(x) \]. |
| 391 | `\[ f(x) \]` | `\[ f(x)\ \text{convexe} \]` | Candidat alternatif : \[ \min_x f(x) \]. |
| 562 | `\[ \]` | `\[ \text{dualité faible} \]` | Candidat alternatif : \[ d^{*}\leq p^{*} \] — l'inégalité de dualité faible. |
| 712 | `\[ DP\[s\] = s \]` | `\[ DP[s]=\text{valeur optimale du sous-problème } s \]` | Candidat alternatif : DP[s]=\text{opt}. Le second bloc (l. 716) donne la récurrence. |
| 773 | `\[ \]` | `\[ \eta\ \text{petit} \]` | Candidat alternatif : \[ \eta\ll 1 \]. |
| 779 | `\[ \]` | `\[ \eta\ \text{grand} \]` | Candidat alternatif : \[ \eta\gg 1 \]. |
| 990 | `\[ \]` | `\[ \theta^{*}=\arg\min_\theta L(\theta) \]` | Candidat alternatif : \[ \hat{\theta} \]. |
| 996 | `\[ f(x) f’(x) f(x) ^\* \]` | `\[ f(x)\to f'(x)\to x-\eta f'(x)\to x^{*} \]` | Candidat alternatif pour le troisième terme : x_{t+1}=x_t-\eta f'(x_t). Cf. l. 1280 du domaine I, même motif. |

### Confiance inconnue — décision requise (13)

| Ligne | Bloc actuel | Ce que le bloc contenait |
|---:|---|---|
| 17 | `\[ \]` | Introduction « permettant de chercher la meilleure solution possible selon : [vide] ou [vide] ». Deux blocs vides, aucun résidu. |
| 21 | `\[ \]` | Introduction, pendant du bloc précédent. |
| 45 | `\[ \]` | §1, deuxième maillon de la chaîne (six blocs vides, l. 41 à 53). |
| 47 | `\[ \]` | §1, troisième maillon. |
| 49 | `\[ \]` | §1, quatrième maillon. |
| 51 | `\[ \]` | §1, cinquième maillon. |
| 53 | `\[ \]` | §1, sixième maillon. |
| 81 | `\[ ⏎  ⏎ - \]` | §2 Logistique « Minimiser : [trois lignes, dont une puce -] ». Le bloc contenait une liste, presque certainement une somme de coûts. |
| 89 | `\[ \]` | §2 Scheduling « Minimiser : [vide] ou : [vide] ». Deux blocs vides. |
| 93 | `\[ \]` | §2 Scheduling, pendant du bloc précédent. |
| 403 | `\[ ⏎  ⏎ - \]` | §11 « ## Problème non convexe / Le paysage peut contenir : [trois lignes, dont une puce -] ». Liste détruite. |
| 618 | `\[ \]` | §21 algorithme du simplexe « Le simplexe explore les sommets du polyèdre admissible. Conceptuellement : [vide] jusqu'à atteindre une solution optimale. » |
| 922 | `\[ ⏎  ⏎ - \]` | §41 « Newton utilise : [trois lignes, dont une puce -] Cela peut permettre une convergence beaucoup plus rapide près de l'optimum. » Liste de deux items. |

