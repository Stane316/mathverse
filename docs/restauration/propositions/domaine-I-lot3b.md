# LOT 3b — DOMAINE I : CALCUL DIFFÉRENTIEL (sections 41 à 179)

**Date :** 2026-10-18 · **Statut :** propositions soumises, non appliquées
**Document :** `Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md`
**Portée :** lignes 792 à 3 175. Completé par le **lot 3a** (lignes 29 à 784).
**Complément :** les 26 blocs à arbitrer sont repris, avec leurs candidats, dans
`domaine-I-blocs-a-trancher.md`.

---

## 1. La confirmation décisive : le motif « objet → objet »

La synthèse finale (§180, lignes 3 121 à 3 137) conserve cinq blocs partiellement intacts :

```
À une variable                  \[ f(x) f’(x) \]        →  f(x) → f'(x)
À plusieurs variables           \[ f(x) f(x) \]         →  f(x) → ∇f(x)
Pour une transformation         \[ F(x) J_F(x) \]       →  F(x) → J_F(x)
Pour la courbure                \[ f(x) H_f(x) \]       →  f(x) → H_f(x)
Pour l'optimisation             \[ f(x) x-f(x) \]       →  f(x) → x − η∇f(x)
```

Ce motif valide rétroactivement **toutes les flèches reconstruites dans ce document** (l. 424,
812, 3 121, 3 125, 3 129, 3 133, 3 137) et, par extension, la restauration de la ligne 2 221 du
document L, qui reposait sur la même lecture.

## 2. La synecdoque du `\eta`

Le pas d'apprentissage `\eta` est détruit **partout**, y compris dans la section 57 qui lui est
consacrée (`Le paramètre : [vide] contrôle la taille du déplacement.`). Sa présence est pourtant
imposée par les blocs voisins : en l. 3 137, le résidu `x-f(x)` ne se lit qu'avec le `\eta` et le
`\nabla` restitués. C'est un cas d'école de la méthode : **l'absence n'est pas une preuve d'absence,
c'est une information**.

## 3. Deux artefacts distincts de la destruction

| Artefact | Mécanisme | Exemples |
|---|---|---|
| `+` en tête de ligne devient une puce `-` | conversion Markdown | Taylor (l. 528, 535, 545), momentum (l. 1 045, 1 063, 1 069), Adam |
| `-` conservé | il s'agit d'un **vrai** signe moins | descente de gradient (l. 1 031, 1 051, 2 032, 2 932) |

La distinction ne se fait pas à la forme mais au sens : on *descend* le gradient, on *cumule* les
moments. Chaque bloc a été tranché sur cette base, et la décision est indiquée dans sa
justification.

## 4. Les sections les plus atteintes

| Section | Blocs | Nature de la perte |
|---|---|---|
| §171 à §180 (synthèses) | ~25 | **blocs de mots** — chaînes conceptuelles, non des équations |
| §55 à §60 (optimisation) | ~12 | lettres grecques (`η`, `β`, `θ`) |
| §72 à §73 (perte, objectif) | ~8 | `θ`, `\mathcal{L}`, chapeaux de `ŷ` |
| §80 à §89 (numérique, réseaux) | ~15 | formules entières détruites (`\frac`, `\partial`) |

Les sections de synthèse concentrent l'essentiel des blocs non restituables. C'est cohérent avec
l'hypothèse déjà formulée sur le document L : **la dégradation frappe systématiquement les
sections de synthèse**, parce qu'elles contenaient des chaînes de mots plutôt que des équations.

## 5. Corps technique

**Correctif :** `domaine-I-lot3b.patch.json` — 159 entrées : 113 haute, 20 moyenne, 26 inconnue — **133 applicables**

### Confiance haute (113)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 800 | `\[ = \]` | `\[ \frac{dz}{dx}=\frac{dz}{du}\frac{du}{dx} \]` | Rendu : dz/dx = dz/du · du/dx. |
| 812 | `\[ x z a L \]` | `\[ x \to z \to a \to L \]` | Rendu : x → z → a → L. Cohérent avec les trois blocs suivants (z, a, L). |
| 816 | `\[ z=Wx+b \]` | `\[ a=\sigma(z) \]` | Rendu : a=σ(z). L'activation entre la pré-activation et la perte. |
| 834 | `\[ f(x^\*)=0 \]` | `\[ \nabla f(x^{*})=0 \]` | Condition de stationnarité ; la phrase suivante évoque l'absence de dérivée, ce qui confirme qu'il s'agit bien du gradient. |
| 851 | `\[ f(x^\*)f(x) \]` | `\[ f(x^{*})\leq f(x) \]` | Rendu : f(x*) ≤ f(x). |
| 857 | `\[ f(x^\*)f(x) \]` | `\[ f(x^{*})\geq f(x) \]` | Rendu : f(x*) ≥ f(x). |
| 895 | `\[ H(x^\*) \]` | `\[ \nabla^{2}f(x^{*})\succ 0 \]` | Rendu : ∇²f(x*) ≻ 0. |
| 901 | `\[ H(x^\*) \]` | `\[ \nabla^{2}f(x^{*})\prec 0 \]` | Rendu : ∇²f(x*) ≺ 0. |
| 919 | `\[ \_i>0 \]` | `\[ \lambda_i>0 \]` | Rendu : λᵢ > 0. |
| 931 | `\[ f(tx+(1-t)y) tf(x)+(1-t)f(y) \]` | `\[ f(tx+(1-t)y)\leq tf(x)+(1-t)f(y) \]` | Définition standard de la convexité. |
| 952 | `\[ H_f(x) \]` | `\[ \nabla^{2}f(x)\succeq 0 \]` | Rendu : ∇²f(x) ⪰ 0. |
| 958 | `\[ H_f(x) \]` | `\[ \nabla^{2}f(x)\succ 0 \]` | Rendu : ∇²f(x) ≻ 0. |
| 966 | `\[ \|f(x)-f(y)\| L\|x-y\| \]` | `\[ \\|\nabla f(x)-\nabla f(y)\\|\leq L\\|x-y\\| \]` | Définition standard du gradient L-Lipschitz. |
| 984 | `\[ x_{k+1} = x_k-f(x_k) \]` | `\[ x_{k+1}=x_k-\eta\nabla f(x_k) \]` | Rendu : x_{k+1}=x_k−η∇f(x_k). |
| 1000 | `\[ -f(x) \]` | `\[ -\nabla f(x) \]` | Rendu : −∇f(x). |
| 1004 | `\[ x_{k+1} = x_k-f(x_k) \]` | `\[ x_{k+1}=x_k-\eta\nabla f(x_k) \]` | Rendu : x_{k+1}=x_k−η∇f(x_k). |
| 1010 | `\[ \]` | `\[ \eta \]` | Rendu : η. La phrase suivante (« trop grand… trop petit ») confirme qu'il s'agit du pas. |
| 1031 | `\[ \_{t+1} = \_t ⏎  ⏎ - \_L_B(\_t) \]` | `\[ \theta_{t+1}=\theta_t ⏎  ⏎ - \eta\nabla L_B(\theta_t) \]` | Rendu : θ_{t+1}=θ_t−η∇L_B(θ_t). |
| 1045 | `\[ v_t = v_{t-1} ⏎  ⏎ - (1-)g_t \]` | `\[ v_t=\beta v_{t-1} ⏎  ⏎ + (1-\beta)g_t \]` | Rendu : v_t=βv_{t-1}+(1−β)g_t. Forme standard du momentum. |
| 1051 | `\[ _t =_ {t-1} ⏎  ⏎ - v_t \]` | `\[ \theta_t=\theta_{t-1} ⏎  ⏎ - \eta v_t \]` | Rendu : θ_t=θ_{t-1}−ηv_t. |
| 1063 | `\[ m_t = _1m_{t-1} ⏎  ⏎ - (1-\_1)g_t \]` | `\[ m_t=\beta_1 m_{t-1} ⏎  ⏎ + (1-\beta_1)g_t \]` | Rendu : m_t=β₁m_{t-1}+(1−β₁)g_t. Premier moment. |
| 1069 | `\[ v_t = _2v_{t-1} ⏎  ⏎ - (1-\_2)g_t^2 \]` | `\[ v_t=\beta_2 v_{t-1} ⏎  ⏎ + (1-\beta_2)g_t^{2} \]` | Rendu : v_t=β₂v_{t-1}+(1−β₂)g_t². |
| 1081 | `\[ f \]` | `\[ \nabla f \]` | Rendu : ∇f. Opposé à la Hessienne du bloc suivant. |
| 1085 | `\[ H_f \]` | `\[ \nabla^{2}f \]` | Rendu : ∇²f. |
| 1089 | `\[ x_{k+1} = x_k-H(x_k)^{-1}f(x_k) \]` | `\[ x_{k+1}=x_k-H(x_k)^{-1}\nabla f(x_k) \]` | Rendu : x_{k+1}=x_k−H(x_k)^{-1}∇f(x_k). |
| 1101 | `\[ x_{k+1} = x_k- \]` | `\[ x_{k+1}=x_k-\frac{f'(x_k)}{f''(x_k)} \]` | Newton scalaire : x_{k+1}=x_k−f'(x_k)/f''(x_k). |
| 1105 | `\[ x_{k+1} = x_k- H(x_k)^{-1}f(x_k) \]` | `\[ x_{k+1}=x_k-\nabla^{2}f(x_k)^{-1}\nabla f(x_k) \]` | Newton multivariable, cohérent avec le cas scalaire de la ligne précédente. |
| 1133 | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` | Rendu : min_x f(x). |
| 1137 | `\[ g_i(x) \]` | `\[ g_i(x)\leq 0 \]` | Rendu : g_i(x) ≤ 0. Convention usuelle de l'optimisation sous contraintes. |
| 1157 | `\[ (x,) = f(x)+g(x) \]` | `\[ \mathcal{L}(x,\lambda)=f(x)+\lambda g(x) \]` | Rendu : 𝓛(x,λ)=f(x)+λg(x). |
| 1194 | `\[ \_x f=a \]` | `\[ \nabla_x f=a \]` | Rendu : ∇_x f=a. |
| 1204 | `\[ \_x f = (A+A^T)x \]` | `\[ \nabla_x f=(A+A^{T})x \]` | Rendu : ∇_x f=(A+A^T)x. |
| 1208 | `\[ \_x f=2Ax \]` | `\[ \nabla_x f=2Ax \]` | Le cas symétrique simplifie (A+A^T) en 2A. |
| 1218 | `\[ f(x)=\|Ax-b\|^2 \]` | `\[ f(x)=\\|Ax-b\\|^{2} \]` | Rendu : f(x)=‖Ax−b‖². |
| 1222 | `\[ f(x) = A^T(Ax-b) \]` | `\[ \nabla f(x)=2A^{T}(Ax-b) \]` | Vérifier : ∇‖Ax−b‖²=2A^T(Ax−b). |
| 1242 | `\[ \_() \]` | `\[ \nabla_\theta \mathcal{L}(\theta) \]` | Rendu : ∇_θ 𝓛(θ). |
| 1248 | `\[ \_^2() \]` | `\[ \nabla_\theta^{2}\mathcal{L}(\theta) \]` | Rendu : ∇²_θ 𝓛(θ). |
| 1258 | `\[ y=f_(x) \]` | `\[ \hat{y}=f_\theta(x) \]` | Rendu : ŷ=f_θ(x). |
| 1262 | `\[ L(y,y) \]` | `\[ L(\hat{y},y) \]` | Rendu : L(ŷ,y). |
| 1266 | `\[ J() = 1n _{i=1}^{n} L(f_(x_i),y_i) \]` | `\[ J(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i) \]` | Rendu : J(θ)=1/n Σ L(f_θ(x_i),y_i). |
| 1270 | `\[ ^\* = \_J() \]` | `\[ \theta^{*}=\arg\min_\theta J(\theta) \]` | Rendu : θ*=argmin_θ J(θ). |
| 1274 | `\[ \_J() \]` | `\[ \nabla_\theta J(\theta) \]` | Rendu : ∇_θ J(θ). |
| 1350 | `\[ = \]` | `\[ \frac{dz}{dx}=\frac{dz}{dy}\frac{dy}{dx} \]` | Rendu : dz/dx = dz/dy · dy/dx. |
| 1392 | `\[ f’(x) \]` | `\[ f'(x)\approx\frac{f(x+h)-f(x)}{h} \]` | Rendu : f'(x)≈(f(x+h)−f(x))/h. |
| 1396 | `\[ f’(x) \]` | `\[ f'(x)\approx\frac{f(x+h)-f(x-h)}{2h} \]` | Rendu : f'(x)≈(f(x+h)−f(x−h))/2h. |
| 1434 | `\[ f_nf_{n-1}f_1 \]` | `\[ f_n\circ f_{n-1}\circ\cdots\circ f_1 \]` | Rendu : f_n∘f_{n-1}∘⋯∘f_1. |
| 1440 | `\[ \_i a_i \]` | `\[ \prod_i a_i \]` | Rendu : ∏ᵢ aᵢ. |
| 1452 | `\[ \_i a_i \]` | `\[ \prod_i a_i \]` | Rendu : ∏ᵢ aᵢ. |
| 1470 | `\[ (x)= \]` | `\[ \sigma(x)=\frac{1}{1+e^{-x}} \]` | Vérifier : σ(x)=1/(1+e^{−x}) ⇒ σ'=σ(1−σ). |
| 1474 | `\[ ’(x) = (x)(1-(x)) \]` | `\[ \sigma'(x)=\sigma(x)(1-\sigma(x)) \]` | Dérivée de la sigmoïde. |
| 1482 | `\[ (x) = (0,x) \]` | `\[ \text{ReLU}(x)=\max(0,x) \]` | Rendu : ReLU(x)=max(0,x). |
| 1486 | `\[ ’(x) = ⏎  ⏎ \]` | `\[ \text{ReLU}'(x)=\begin{cases}0&\text{si }x<0\\ 1&\text{si }` | Rendu : ReLU'(x)=0 si x<0, 1 si x>0. La convention en 0 reste ouverte, comme le dit la phrase. |
| 1496 | `\[ (z_i) = {\_j e^{z_j}} \]` | `\[ \sigma(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}} \]` | Rendu : σ(z_i)=e^{z_i}/Σ_j e^{z_j}. |
| 1500 | `\[ = s_i(\_{ij}-s_j) \]` | `\[ \frac{\partial s_i}{\partial z_j}=s_i(\delta_{ij}-s_j) \]` | Jacobienne du softmax : ∂s_i/∂z_j=s_i(δ_ij−s_j). |
| 1510 | `\[ L=-\_i y_ip_i \]` | `\[ L=-\sum_i y_i\log p_i \]` | Rendu : L=−Σ y_i log p_i. C'est la cross-entropie annoncée par le §88. |
| 1522 | `\[ f_ = f_Lf_{L-1}f_1 \]` | `\[ f_\theta=f_L\circ f_{L-1}\circ\cdots\circ f_1 \]` | Rendu : f_θ=f_L∘f_{L-1}∘⋯∘f_1. |
| 1526 | `\[ \_J() \]` | `\[ \min_\theta J(\theta) \]` | Rendu : min_θ J(θ). |
| 1530 | `\[ \_J \]` | `\[ \nabla_\theta J \]` | Rendu : ∇_θ J. |
| 1578 | `\[ \|f(x)\| \]` | `\[ \\|\nabla f(x)\\| \]` | Rendu : ‖∇f(x)‖. |
| 1624 | `\[ J(w) = \_i (w<sup>Tx_i-y_i)</sup>2 \]` | `\[ J(w)=\sum_i(w^{T}x_i-y_i)^{2} \]` | Rendu : J(w)=Σ(w^T x_i−y_i)². |
| 1628 | `\[ J(w) = 1n X^T(Xw-y) \]` | `\[ \nabla J(w)=\frac{1}{n}X^{T}(Xw-y) \]` | Rendu : ∇J(w)=1/n X^T(Xw−y). |
| 1632 | `\[ w_{t+1} = w_t-J(w_t) \]` | `\[ w_{t+1}=w_t-\eta\nabla J(w_t) \]` | Rendu : w_{t+1}=w_t−η∇J(w_t). |
| 1644 | `\[ R()=\|\|\_2^2 \]` | `\[ R(\theta)=\\|\theta\\|_2^{2} \]` | Rendu : R(θ)=‖θ‖²₂. |
| 1648 | `\[ R()=2 \]` | `\[ \nabla R(\theta)=2\theta \]` | Vérifier : ∇‖θ‖²₂=2θ. |
| 1656 | `\[ y=f_(x) \]` | `\[ \hat{y}=f_\theta(x) \]` | Rendu : ŷ=f_θ(x). |
| 1660 | `\[ L(y,y) \]` | `\[ L(\hat{y},y) \]` | Rendu : L(ŷ,y). |
| 1664 | `\[ \_L \]` | `\[ \nabla_\theta L \]` | Rendu : ∇_θ L. |
| 1735 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 1753 | `\[ H^{nn} \]` | `\[ H\in\mathbb{R}^{n\times n} \]` | Rendu : H ∈ ℝ^{n×n}. |
| 1814 | `\[ F \]` | `\[ \nabla F \]` | Rendu : ∇F. |
| 1824 | `\[ =v \]` | `\[ \dot{x}=v \]` | Rendu : ẋ=v. |
| 1828 | `\[ =a \]` | `\[ \dot{v}=a \]` | Rendu : v̇=a. |
| 1844 | `\[ =f(x,t) \]` | `\[ \frac{dx}{dt}=f(x,t) \]` | Rendu : dx/dt=f(x,t). |
| 1887 | `\[ \_(a\|s) \]` | `\[ \pi_\theta(a\|s) \]` | Rendu : π_θ(a\|s). |
| 1895 | `\[ \_J() \]` | `\[ \max_\theta J(\theta) \]` | Rendu : max_θ J(θ). |
| 1903 | `\[ p_(x) \]` | `\[ p_\theta(x) \]` | Rendu : p_θ(x). |
| 1923 | `\[ ^\* = _ L() \]` | `\[ \theta^{*}=\arg\max_\theta \mathcal{L}(\theta) \]` | Rendu : θ*=argmax_θ 𝓛(θ). |
| 1927 | `\[ ^\* = _ -L() \]` | `\[ \theta^{*}=\arg\min_\theta -\mathcal{L}(\theta) \]` | Équivalent au maximum de vraisemblance. |
| 1939 | `\[ {xp_} \[f_(x)\] \]` | `\[ \nabla_\theta\,\mathbb{E}_{x\sim p_\theta}\left[f_\theta(x)` | Rendu : ∇_θ 𝔼_{x∼p_θ}[f_θ(x)]. Le §117 renvoie à la score function et au reparamétrage. |
| 1952 | `\[ z=g(,) \]` | `\[ z=g(\theta,\epsilon) \]` | Rendu : z=g(θ,ε). |
| 1985 | `\[ f(x) \]` | `\[ \nabla f(x) \]` | Rendu : ∇f(x). |
| 2004 | `\[ f(x^\*)=0 \]` | `\[ \nabla f(x^{*})=0 \]` | Rendu : ∇f(x*)=0. |
| 2032 | `\[ \_{t+1} = \_t-_t_J(\_t) \]` | `\[ \theta_{t+1}=\theta_t-\eta_t\nabla_\theta J(\theta_t) \]` | Rendu : θ_{t+1}=θ_t−η_t∇_θ J(θ_t). |
| 2038 | `\[ \|J()\|< \]` | `\[ \\|\nabla J(\theta)\\|<\epsilon \]` | Rendu : ‖∇J(θ)‖<ε. |
| 2042 | `\[ \|J_{t+1}-J_t\|< \]` | `\[ \|J_{t+1}-J_t\|<\epsilon \]` | Rendu : \|J_{t+1}−J_t\|<ε. |
| 2056 | `\[ x_kx^\* \]` | `\[ x_k\to x^{*} \]` | Rendu : x_k → x*. |
| 2145 | `\[ \_i e^{x_i} \]` | `\[ \log\sum_i e^{x_i} \]` | Rendu : log Σᵢ e^{xᵢ}. |
| 2149 | `\[ m+\_i e^{x_i-m} \]` | `\[ m+\log\sum_i e^{x_i-m} \]` | Astuce du max : log Σ e^{x_i} = m + log Σ e^{x_i−m}. |
| 2153 | `\[ m=\_i x_i \]` | `\[ m=\max_i x_i \]` | Rendu : m=maxᵢ xᵢ. |
| 2163 | `\[ g g \]` | `\[ g\gets \frac{c\,g}{\\|g\\|} \]` | Rendu : g ← cg/‖g‖. C'est le clipping par la norme. |
| 2167 | `\[ \|g\|>c \]` | `\[ \\|g\\|>c \]` | Rendu : ‖g‖>c. |
| 2217 | `\[ f’(x) \]` | `\[ f'(x)\approx\frac{f(x+h)-f(x)}{h} \]` | Rendu : f'(x)≈(f(x+h)−f(x))/h. |
| 2252 | `\[ f(x) \]` | `\[ \nabla f(x) \]` | Rendu : ∇f(x). |
| 2490 | `\[ x_{t+1} = x_t-f(x_t) \]` | `\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]` | Rendu : x_{t+1}=x_t−η∇f(x_t). |
| 2514 | `\[ J(w,b) = 1n \_i (y_i-y_i)^2 \]` | `\[ J(w,b)=\frac{1}{n}\sum_i(\hat{y}_i-y_i)^{2} \]` | Rendu : J(w,b)=1/n Σ(ŷ_i−y_i)². |
| 2518 | `\[ \_wJ \]` | `\[ \nabla_w J \]` | Rendu : ∇_w J. |
| 2522 | `\[ \]` | `\[ \nabla_b J \]` | Rendu : ∇_b J. |
| 2608 | `\[ f(x,y) \]` | `\[ \nabla f(x,y) \]` | Rendu : ∇f(x,y). |
| 2622 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 2650 | `\[ a=(z) \]` | `\[ a=\sigma(z) \]` | Rendu : a=σ(z). |
| 2686 | `\[ f=0 \]` | `\[ \nabla f=0 \]` | Rendu : ∇f=0. |
| 2858 | `\[ f: \]` | `\[ f:\mathbb{R}\to\mathbb{R} \]` | Rendu : f : ℝ → ℝ. |
| 2872 | `\[ f(x) \]` | `\[ \nabla f(x) \]` | Rendu : ∇f(x). |
| 2878 | `\[ F:<sup>n</sup>m \]` | `\[ F:\mathbb{R}^{n}\to\mathbb{R}^{m} \]` | Rendu : F : ℝⁿ → ℝᵐ. |
| 2888 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 2932 | `\[ \_{t+1} = \_t ⏎  ⏎ - _t_ J(\_t) \]` | `\[ \theta_{t+1}=\theta_t ⏎  ⏎ - \eta_t\nabla_\theta J(\theta_t` | Rendu : θ_{t+1}=θ_t−η_t∇_θ J(θ_t). Identique à l. 2032, ce qui confirme. |
| 2980 | `\[ f=0 \]` | `\[ \nabla f=0 \]` | Rendu : ∇f=0. |
| 2986 | `\[ f \]` | `\[ \nabla f \]` | Rendu : ∇f opposé à J_f. |
| 3121 | `\[ f(x) f’(x) \]` | `\[ f(x)\to f'(x) \]` | Rendu : f(x) → f'(x). |
| 3125 | `\[ f(x) f(x) \]` | `\[ f(x)\to \nabla f(x) \]` | Rendu : f(x) → ∇f(x). |
| 3129 | `\[ F(x) J_F(x) \]` | `\[ F(x)\to J_F(x) \]` | Rendu : F(x) → J_F(x). |
| 3133 | `\[ f(x) H_f(x) \]` | `\[ f(x)\to H_f(x) \]` | Rendu : f(x) → H_f(x). |
| 3137 | `\[ f(x) x-f(x) \]` | `\[ f(x)\to x-\eta\nabla f(x) \]` | Rendu : f(x) → x−η∇f(x). Cohérent avec l. 984. |

### Confiance moyenne (20)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 824 | `\[ = \]` | `\[ \frac{\partial L}{\partial W}=\frac{\partial L}{\partial a}` | Candidat alternatif : \frac{\partial L}{\partial W}=\delta x^{T}. Formulation à confirmer par l'auteur. |
| 1234 | `\[ () \]` | `\[ \max_\theta \mathcal{L}(\theta) \]` | Candidat alternatif : \max_\theta \log \mathcal{L}(\theta). La vraisemblance ou sa log-forme : à confirmer. |
| 1238 | `\[ -() \]` | `\[ -\mathcal{L}(\theta) \]` | Négatif de la quantité maximisée en l. 1234. |
| 1280 | `\[ f(x) f’(x) f(x) \]` | `\[ f(x)\to f'(x)\to x-\eta f'(x) \]` | Candidat alternatif : f(x) → f'(x) → min f(x). Le troisième terme reste à confirmer. |
| 1404 | `\[ g_{} \]` | `\[ g_{\text{analytique}} \]` | Candidat alternatif : g_{\text{exact}}. À confirmer par l'auteur. |
| 1408 | `\[ g_{} \]` | `\[ g_{\text{numérique}} \]` | Candidat alternatif : g_{\text{approx}}. À confirmer. |
| 1514 | `\[ p-y \]` | `\[ \nabla_z L=p-y \]` | Résultat classique softmax + cross-entropie. Le membre de gauche reste à confirmer. |
| 1564 | `\[ x_{} x_{} \]` | `\[ x_{\text{local}}\neq x_{\text{global}} \]` | Candidat alternatif : f(x_{\text{local}})>f(x_{\text{global}}). À confirmer. |
| 1614 | `\[ g_t J(\_t) \]` | `\[ g_t\approx\nabla_\theta J(\theta_t) \]` | Candidat alternatif : g_t=\hat{\nabla}_\theta J(\theta_t). À confirmer. |
| 1668 | `\[ = \]` | `\[ \nabla_\theta L=\frac{\partial L}{\partial \hat{y}}\frac{\p` | Candidat alternatif : \nabla_\theta L=\frac{\partial L}{\partial y}\frac{\partial y}{\partial \theta}. Notation de la cible à conf |
| 1909 | `\[ _p_(x) \]` | `\[ \nabla_\theta\log p_\theta(x) \]` | Candidat alternatif : \nabla_\theta p_\theta(x). Le contexte penche pour le gradient du log. |
| 1977 | `\[ x \]` | `\[ \Delta x\to 0 \]` | Candidat alternatif : x\to x+\Delta x. À confirmer. |
| 2283 | `\[ p_(x) \]` | `\[ \nabla_\theta p_\theta(x) \]` | Candidat alternatif : \frac{\partial}{\partial\theta}p_\theta(x). À confirmer. |
| 2287 | `\[ p_(x) \]` | `\[ \nabla_\theta\log p_\theta(x) \]` | Candidat alternatif : \nabla_\theta \log \mathcal{L}(\theta). À confirmer. |
| 2461 | `\[ x \]` | `\[ \sqrt{x} \]` | Candidat alternatif : \sin x ou \ln x. À confirmer. |
| 2596 | `\[ x \]` | `\[ \ln x \]` | Candidat : ln x. Alternatives : \sin x, \cos x — voir les blocs suivants. |
| 2598 | `\[ x \]` | `\[ \sin x \]` | Candidat. L'ordre {ln, sin, cos} reprend celui de la section 12. |
| 2600 | `\[ x \]` | `\[ \cos x \]` | Candidat. À confirmer ; \tan x est une alternative. |
| 2640 | `\[ \]` | `\[ \frac{dL}{dx} \]` | Candidat alternatif : \frac{\partial L}{\partial x}. À confirmer. |
| 2656 | `\[ \]` | `\[ \frac{\partial L}{\partial w} \]` | Candidat alternatif : \frac{\partial L}{\partial \theta}. À confirmer. |

### Confiance inconnue — décision requise (26)

| Ligne | Bloc actuel | Ce que le bloc contenait |
|---:|---|---|
| 1284 | `\[ \]` | §74 « Plus précisément : [vide] Cette boucle constitue l'une des structures mathématiques fondamentales du Machine Learning. » — la forme détaillée de la chaîne |
| 1536 | `\[ \]` | §89 « Ainsi : [vide] » — conclusion de la section sur la composition différentiable. Aucun résidu. |
| 1693 | `\[ \]` | §102 TENSEURS « Le principe reste le même : [vide] Chaque opération possède une règle de différentiation. » — aucun résidu. |
| 1933 | `\[ \]` | §116 « Ainsi : [vide] » — conclusion du maximum de vraisemblance. Aucun résidu. |
| 1991 | `\[ = \]` | §121 « Elle ne garantit pas automatiquement : [= ] Pour obtenir des garanties globales, il faut exploiter des structures supplémentaires : - convexité ; … ». La |
| 2124 | `\[ \]` | §130 CHECKPOINTING « On échange donc : [vide] ». Le compromis mémoire/calcul est décrit en prose autour du bloc. |
| 2838 | `\[ \]` | §171 CE QU'IL FAUT ABSOLUMENT RETENIR, premier des quatre blocs (« doit contenir : »). Bloc vide, aucun résidu. |
| 2842 | `\[ \]` | §171, deuxième bloc (« puis : »). Bloc vide, aucun résidu. |
| 2846 | `\[ \]` | §171, troisième bloc (« puis : »). Bloc vide, aucun résidu. |
| 2850 | `\[ \]` | §171, quatrième bloc (« et enfin : »). Bloc vide, aucun résidu. |
| 2958 | `\[ \]` | §174 « La backpropagation peut donc être comprise comme : [vide] ». La chaîne ASCII qui précède (Paramètres → Opérations → Sortie → Loss → Dérivée locale → Règl |
| 3016 | `\[ \]` | §176 Niveau 1 — Calcul différentiel. Bloc vide, aucun résidu. |
| 3020 | `\[ \]` | §176 Niveau 2 — Optimisation. Bloc vide, aucun résidu. |
| 3024 | `\[ \]` | §176 Niveau 3 — Apprentissage. Bloc vide, aucun résidu. |
| 3056 | `\[ \]` | §178 Probabilités. Bloc vide, aucun résidu. |
| 3060 | `\[ \]` | §178 Statistiques. Bloc vide, aucun résidu. |
| 3064 | `\[ \]` | §178 Calcul différentiel. Bloc vide, aucun résidu. |
| 3068 | `\[ \]` | §178 En Machine Learning. Bloc vide, aucun résidu. |
| 3117 | `\[ \]` | §180 « Son idée fondamentale est : ». Bloc vide, aucun résidu. |
| 3141 | `\[ \]` | §180 « Pour les réseaux neuronaux : [vide] ». Les quatre blocs suivants suivent le même motif « objet → objet » et sont tous vides. |
| 3145 | `\[ \]` | §180 « Pour le Machine Learning : [vide] ». |
| 3149 | `\[ \]` | §180 « Pour la simulation : [vide] ». |
| 3153 | `\[ \]` | §180 « Pour la computer graphics : [vide] ». |
| 3161 | `\[ \]` | §180 « Le domaine I constitue ainsi le pont mathématique direct entre : [vide] ». |
| 3165 | `\[ \]` | §180 « et, plus largement : [vide] ». |
| 3175 | `\[ \]` | FIN DU DOCUMENT « **Noyau absolument fondamental :** [vide] ». |

