# Lot 5b — Domaine J, Optimisation (fin du document)

**Source :** `Maths-vers-Informatiques/Domaine J — Optimisation.md` (3 541 lignes, 332 blocs `\[…\]`, 119 blocs dégradés)
**Périmètre du lot :** sections **47 à 158** — lignes **1026 à 3534**
**Statut :** propositions à valider. **Rien n'a été écrit dans le fichier source.**
**Lot précédent :** `domaine-J-lot5a.md` (sections introductives à 46, lignes 17 à 1018).

## Ce que la lecture intégrale a révélé

### Deux structures équivalentes, deux verdicts opposés

La règle du lot 4b impose de chercher une structure survivante avant de conclure à
l'impasse. Le document J en offre deux, et elles n'appellent pas la même décision.

**1. Le §110 est intact, et il répond au §156.** La section 110 « MODÉLISATION AVANT
ALGORITHME » (l. 2184–2193) est une liste numérotée de dix questions, parfaitement
lisible : *Que veut-on optimiser ? Quelles sont les variables ? Quelles sont les
contraintes ? … Une solution exacte est-elle nécessaire ?* La section 156
« FORMULE MENTALE FINALE » pose **dix questions** elle aussi, en gras, chacune
suivie d'un bloc vide. Les dix blocs vides sont donc les dix primitives de
modélisation que le §110 nomme. Ce n'est plus une devinette : c'est un appariement.
Les dix reconstructions sont proposées en confiance **moyenne** — la case sémantique
est fixée par la question posée, le libellé exact reste un choix d'auteur.

Deux autres appuis confirment : le §113 répond à la question « l'évaluation est-elle
coûteuse ? » par une liste intacte (*optimisation bayésienne ; surrogate models*), et
le §114 se termine sur `(f_1,…,f_k)`, la structure du multi-objectifs.

**2. Le §122 est intact, mais il ne répond pas au §155.** La section 122 (l. 2464–2484)
déploie une chaîne ASCII de **dix** étapes — `Problem → Variables → Objective →
Constraints → Model → Optimizer → Iteration → Evaluation → Stopping criterion →
Solution → Validation`. La section 155 « LA GRANDE CARTE DES DOMAINES » contient
elle aussi **dix** blocs vides, suivis du bloc survivant `\[ IJ \]`. La coïncidence du
nombre est tentante. Je ne l'ai **pas** retenue, et voici pourquoi : le §122 décrit un
moteur d'optimisation, le §155 une progression entre domaines, et le seul bloc survivant
du §155 est une flèche entre deux lettres de domaines. Un comptage n'est pas une
preuve. Les dix blocs du §155 restent donc en **inconnue**, avec la piste A→…→J
documentée mais non appliquée.

### La convention de l'auteur pour les réponses en mots

Le §144 (l. 2972–2978) écrit `\[ learning\ rate \]`, `\[ batch\ size \]`,
`\[ weight\ decay \]`, `\[ architecture \]`. Ces quatre blocs sont **intacts** : ils
prouvent que l'auteur écrit des réponses en mots dans des blocs display. C'est cette
convention que suivent les reconstructions en `\text{…}` du §156, du §157 et du
§128.

### Le §158 est un écho du §2

La synthèse finale (l. 3504–3526) reprend rubrique par rubrique le §2 (l. 65–99) :
machine learning, robotique, logistique, réseaux. Quatre des six blocs sont donc
restaurables par report ; les deux rubriques absentes du §2 — *systèmes intelligents*
et *ingénierie logicielle* — sont traitées séparément, la seconde en inconnue.

## Un erratum sur le lot 5a

Le motif `0x` (l. 473 du lot 5a, l. 1896 de celui-ci) ne montre dans son résidu que le
`0` et la variable : ni le second `\leq`, ni le `1` final n'ont survécu. La
reconstruction `0\leq x\leq 1` reste la seule sémantiquement correcte — une relaxation
continue de variable binaire enferme dans [0,1] — mais le résidu ne la prouve pas. La
ligne 1896 est donc proposée en **moyenne** et non en haute, et la ligne 473 du lot 5a
mérite la même réserve.

## Répartition

| Confiance | Nombre | Traitement |
|---|---:|---|
| Haute | 94 | applicable après validation |
| Moyenne | 39 | applicable après validation — un choix d'auteur est signalé |
| Inconnue | 53 | non applicable, candidats argumentés |
| **Total** | **186** | **133 applicables** |

**Correctif :** `domaine-J-lot5b.patch.json` — 186 entrées : 94 haute, 39 moyenne, 53 inconnue — **133 applicables**

### Confiance haute (94)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 1026 | `\[ \]` | `\[ L(\theta)+\lambda R(\theta) \]` | Rendu : L(θ)+λR(θ). |
| 1032 | `\[ R()=\|\|\_2^2 \]` | `\[ R(\theta)=\\|\theta\\|_{2}^{2} \]` | Pénalité L2 au carré — la forme universelle du weight decay. |
| 1036 | `\[ R()=\|\|\_1 \]` | `\[ R(\theta)=\\|\theta\\|_{1} \]` | Pénalité L1 — la forme du lasso. |
| 1046 | `\[ L_{} \]` | `\[ L_{\text{train}} \]` | Rendu : L_train. |
| 1050 | `\[ L_{} \]` | `\[ L_{\text{test}} \]` | Rendu : L_test. |
| 1054 | `\[ L_{} \]` | `\[ L_{\text{train}} \]` | Rendu : L_train (faible). |
| 1058 | `\[ L_{} \]` | `\[ L_{\text{test}} \]` | Rendu : L_test (élevée). |
| 1072 | `\[ L() \]` | `\[ L(\theta) \]` | Rendu : L(θ). |
| 1092 | `\[ g_t = f(x_t) ⏎  ⏎ - \_t \]` | `\[ g_t=\nabla f(x_t) ⏎  ⏎ + \xi_t \]` | Gradient bruité = vrai gradient + bruit ξ_t. |
| 1146 | `\[ x N(x) x’ N(x’) \]` | `\[ x\to N(x)\to x'\to N(x') \]` | Rendu : x → N(x) → x’ → N(x’). |
| 1154 | `\[ x_0^{(1)}, x_0^{(2)}, , x_0^{(k)} \]` | `\[ x_0^{(1)},x_0^{(2)},\ldots,x_0^{(k)} \]` | Rendu : x₀⁽¹⁾,x₀⁽²⁾,…,x₀⁽ᵏ⁾. |
| 1183 | `\[ P={x_1,x_2,,x_n} \]` | `\[ P=\{x_1,x_2,\ldots,x_n\} \]` | Rendu : P={x₁,x₂,…,x_n}. |
| 1299 | `\[ f_1(x),f_2(x),,f_k(x) \]` | `\[ f_1(x),f_2(x),\ldots,f_k(x) \]` | Rendu : f₁(x),f₂(x),…,f_k(x). |
| 1334 | `\[ F(x) = \_1 f_1(x) ⏎  ⏎ - \_2 f_2(x) ⏎  ⏎ - ` | `\[ F(x)=\lambda_1f_1(x) ⏎  ⏎ + \lambda_2f_2(x) ⏎  ⏎ + \lambda_` | Somme pondérée — la scalarisation canonique. Rendu : F(x)=λ₁f₁(x)+λ₂f₂(x)+λ_kf_k(x). |
| 1342 | `\[ \_i \]` | `\[ \lambda_i \]` | Rendu : λ_i. |
| 1352 | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` | Rendu : min_x f(x). |
| 1376 | `\[ \]` | `\[ \min_x\mathbb{E}[f(x,\xi)] \]` | Minimisation d'une espérance — la forme de l'optimisation stochastique. |
| 1384 | `\[ R() = 1n _{i=1}^{n} L(f_(x_i),y_i) \]` | `\[ R(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i) \]` | Risque empirique — rendu : R(θ)=(1/n)Σ L(f_θ(x_i),y_i). |
| 1388 | `\[ \]` | `\[ \min_\theta R(\theta) \]` | Rendu : min_θ R(θ). |
| 1396 | `\[ \|\|C \]` | `\[ \\|\theta\\|\leq C \]` | Contrainte de norme — rendu : ‖θ‖≤C. |
| 1416 | `\[ _ 1n _i L(y_i,f_(x_i)) \]` | `\[ \min_\theta\frac{1}{n}\sum_i L(y_i,f_\theta(x_i)) \]` | Rendu : min_θ (1/n)Σ L(y_i,f_θ(x_i)). |
| 1428 | `\[ y=f_(x) \]` | `\[ \hat{y}=f_\theta(x) \]` | Rendu : ŷ=f_θ(x). |
| 1432 | `\[ ^\* = _L(f_(x),y) \]` | `\[ \theta^{*}=\arg\min_\theta L(f_\theta(x),y) \]` | Rendu : θ*=argmin_θ L(f_θ(x),y). |
| 1470 | `\[ = H_1H_2H_k \]` | `\[ \mathcal{H}=H_1\times H_2\times\cdots\times H_k \]` | Produit cartésien des ensembles d'hyperparamètres. |
| 1500 | `\[ \]` | `\[ \max_\theta J(\theta) \]` | Rendu : max_θ J(θ). |
| 1508 | `\[ (t) \]` | `\[ \tau(t) \]` | Rendu : τ(t). |
| 1552 | `\[ T_1,T_2,,T_n \]` | `\[ T_1,T_2,\ldots,T_n \]` | Rendu : T₁,T₂,…,T_n. |
| 1556 | `\[ M_1,M_2,,M_k \]` | `\[ M_1,M_2,\ldots,M_k \]` | Rendu : M₁,M₂,…,M_k. |
| 1560 | `\[ C_{} \]` | `\[ C_{\max} \]` | Makespan. |
| 1580 | `\[ A_1,,A_n \]` | `\[ A_1,\ldots,A_n \]` | Rendu : A₁,…,A_n. |
| 1588 | `\[ \_i x_iR \]` | `\[ \sum_i x_i\leq R \]` | Rendu : Σ x_i≤R. |
| 1614 | `\[ \_P (P) \]` | `\[ \min_P C(P) \]` | Identique à la l. 75. |
| 1618 | `\[ \_x \_i U_i(x_i) \]` | `\[ \max_x\sum_i U_i(x_i) \]` | Somme d'utilités — l'allocation est un maximum, pas un minimum. |
| 1622 | `\[ \_i x_iC \]` | `\[ \sum_i x_i\leq C \]` | Rendu : Σ x_i≤C. |
| 1630 | `\[ w=(w_1,,w_n) \]` | `\[ w=(w_1,\ldots,w_n) \]` | Rendu : w=(w₁,…,w_n). |
| 1640 | `\[ \_i w_i=1 \]` | `\[ \sum_i w_i=1 \]` | Rendu : Σ w_i=1. |
| 1644 | `\[ w_i \]` | `\[ w_i\geq 0 \]` | Rendu : w_i≥0. |
| 1664 | `\[ ^\* = _ \|R()-I\|^2 \]` | `\[ \theta^{*}=\arg\min_\theta\\|R(\theta)-I\\|^{2} \]` | Moindres carrés entre rendu et image cible. |
| 1676 | `\[ x^\* = \_x E(x) \]` | `\[ x^{*}=\arg\min_x E(x) \]` | Minimisation d'énergie. |
| 1702 | `\[ _ \_i L_i() \]` | `\[ \min_\theta\sum_i L_i(\theta) \]` | Somme de pertes. |
| 1708 | `\[ y=Ax+ \]` | `\[ y=Ax+\epsilon \]` | Modèle linéaire bruité. |
| 1712 | `\[ x^\* = \_x \|Ax-y\|^2 ⏎  ⏎ - R(x) \]` | `\[ x^{*}=\arg\min_x\\|Ax-y\\|^{2} ⏎  ⏎ + \lambda R(x) \]` | Régularisation de Tikhonov — reconstruction par moindres carrés régularisés. |
| 1742 | `\[ \]` | `\[ \delta \]` | Rendu : δ. |
| 1746 | `\[ \_{} L(x+,y) \]` | `\[ \max_{\\|\delta\\|\leq\epsilon}L(x+\delta,y) \]` | Attaque adversariale bornée. |
| 1750 | `\[ \|\| \]` | `\[ \\|\delta\\|\leq\epsilon \]` | Borne sur la perturbation. |
| 1760 | `\[ _x_ {i=1}^{N} f_i(x) \]` | `\[ \min_x\sum_{i=1}^{N}f_i(x) \]` | Somme fédérée. |
| 1781 | `\[ {k=1}^{K} p_k F_k() \]` | `\[ \min_\theta\sum_{k=1}^{K}p_kF_k(\theta) \]` | Moyenne pondérée des objectifs locaux — FedAvg. |
| 1806 | `\[ x_1,x_2,x_3, \]` | `\[ x_1,x_2,x_3,\ldots \]` | Flux de données. |
| 1828 | `\[ T \]` | `\[ t\leq T \]` | Contrainte de latence. |
| 1878 | `\[ \_1,\_2, \]` | `\[ S_1,S_2,\ldots \]` | Rendu : S₁,S₂,… |
| 1892 | `\[ x_i{0,1} \]` | `\[ x_i\in\{0,1\} \]` | Rendu : x_i∈{0,1}. |
| 1975 | `\[ 01 \]` | `\[ [0,1] \]` | Rendu : [0,1]. |
| 1979 | `\[ 010^6 \]` | `\[ [0,10^{6}] \]` | Rendu : [0,10⁶]. |
| 2006 | `\[ x_tx^\* \]` | `\[ x_t\to x^{*} \]` | Convergence des itérés. |
| 2010 | `\[ f(x_t)f(x^\*) \]` | `\[ f(x_t)\to f(x^{*}) \]` | Convergence des valeurs. |
| 2051 | `\[ f \]` | `\[ \nabla f \]` | Rendu : ∇f. |
| 2064 | `\[ ^2f \]` | `\[ \nabla^{2}f \]` | Rendu : ∇²f. |
| 2135 | `\[ f(x)=0 \]` | `\[ \nabla f(x)=0 \]` | Rendu : ∇f(x)=0. |
| 2162 | `\[ L_{} \]` | `\[ L_{\text{train}} \]` | Même paire qu'au §48. |
| 2166 | `\[ L_{} \]` | `\[ L_{\text{test}} \]` | Rendu : L_test. |
| 2237 | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` | Rendu : min_x f(x). |
| 2243 | `\[ \_x c^Tx \]` | `\[ \min_x c^{T}x \]` | Rendu : min_x c^T x. |
| 2247 | `\[ Axb \]` | `\[ Ax\leq b \]` | Rendu : Ax≤b. |
| 2253 | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` | Rendu : min_x f(x). |
| 2263 | `\[ \_x f(x)+R(x) \]` | `\[ \min_x f(x)+R(x) \]` | Rendu : min_x f(x)+R(x). |
| 2269 | `\[ x_{t+1}=x_t-f(x_t) \]` | `\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]` | Rendu : x_{t+1}=x_t−η∇f(x_t). C'est cette forme intacte qui a servi de référence à la l. 759 (lot 5a). |
| 2275 | `\[ x_{t+1} = x_t-H^{-1}f \]` | `\[ x_{t+1}=x_t-H^{-1}\nabla f \]` | Rendu : x_{t+1}=x_t−H^{-1}∇f. |
| 2281 | `\[ \_x \[f(x,)\] \]` | `\[ \min_x\mathbb{E}[f(x,\xi)] \]` | Rendu : min_x 𝔼[f(x,ξ)]. |
| 2287 | `\[ \_J() \]` | `\[ \max_\theta J(\theta) \]` | Rendu : max_θ J(θ). |
| 2339 | `\[ f \]` | `\[ \nabla f \]` | Gradient. |
| 2341 | `\[ ^2f \]` | `\[ \nabla^{2}f \]` | Hessienne. |
| 2345 | `\[ (x,) \]` | `\[ \mathcal{L}(x,\lambda) \]` | Lagrangien. |
| 2347 | `\[ Axb \]` | `\[ Ax\leq b \]` | Rendu : Ax≤b. |
| 2349 | `\[ x \]` | `\[ x\geq 0 \]` | Rendu : x≥0. |
| 2351 | `\[ x{0,1} \]` | `\[ x\in\{0,1\} \]` | Rendu : x∈{0,1}. |
| 2353 | `\[ \|\|\_1 \]` | `\[ \\|x\\|_1 \]` | Norme L1. |
| 2355 | `\[ \|\|\_2 \]` | `\[ \\|x\\|_2 \]` | Norme L2. |
| 2361 | `\[ \[f(x,)\] \]` | `\[ \mathbb{E}[f(x,\xi)] \]` | Rendu : 𝔼[f(x,ξ)]. |
| 2363 | `\[ (f_1,,f_k) \]` | `\[ (f_1,\ldots,f_k) \]` | Vecteur d'objectifs. |
| 2389 | `\[ \_x \[f(x,)\] \]` | `\[ \min_x\mathbb{E}[f(x,\xi)] \]` | Identique à la forme 7. |
| 2397 | `\[ ^\* = _ L() \]` | `\[ \theta^{*}=\arg\min_\theta L(\theta) \]` | Moindres carrés / minimisation de perte. |
| 2409 | `\[ x \]` | `\[ x\in\mathcal{X} \]` | Rendu : x∈𝓧 — identique à la l. 690. |
| 2444 | `\[ H(x)p=-f(x) \]` | `\[ H(x)p=-\nabla f(x) \]` | Système de Newton — direction de descente. |
| 2595 | `\[ f(x^\*+) \]` | `\[ f(x^{*}+\delta) \]` | Évaluation de la robustesse — la valeur de l'objectif après perturbation. |
| 2722 | `\[ a_1,a_2,,a_T \]` | `\[ a_1,a_2,\ldots,a_T \]` | Rendu : a₁,a₂,…,a_T. |
| 2746 | `\[ J() = Q ⏎  ⏎ - C ⏎ - T ⏎ - E \]` | `\[ J(a)=Q(a) ⏎  ⏎ - C(a) ⏎ - T(a) ⏎ - E(a) \]` | Objectif multi-critères d'un agent : qualité moins coût, moins temps, moins erreurs. Les quatre lettres et leurs sens sont donnés  |
| 2765 | `\[ A_1,A_2,,A_n \]` | `\[ A_1,A_2,\ldots,A_n \]` | Rendu : A₁,A₂,…,A_n. |
| 2811 | `\[ h^\* = _h L_{}(h) \]` | `\[ h^{*}=\arg\min_h L_{\text{val}}(h) \]` | Rendu : h*=argmin_h L_val(h). |
| 2823 | `\[ P=(a_1,a_2,,a_n) \]` | `\[ P=(a_1,a_2,\ldots,a_n) \]` | Rendu : P=(a₁,a₂,…,a_n). |
| 2831 | `\[ P^\* = \_P J(P) \]` | `\[ P^{*}=\arg\min_P J(P) \]` | Rendu : P*=argmin_P J(P). |
| 2879 | `\[ x_0,x_1,x_2, \]` | `\[ x_0,x_1,x_2,\ldots \]` | Rendu : x₀,x₁,x₂,… |
| 2928 | `\[ Axb \]` | `\[ Ax\leq b \]` | Rendu : Ax≤b. |
| 2994 | `\[ J(a) = Q(a) ⏎  ⏎ - C(a) ⏎ - T(a) \]` | `\[ J(a)=Q(a) ⏎  ⏎ - C(a) ⏎ - T(a) \]` | Objectif d'action : qualité moins coût moins temps. |
| 3054 | `\[ \_{x,y}x<sup>2+y</sup>2 \]` | `\[ \min_{x,y}x^{2}+y^{2} \]` | Exercice canonique de Lagrange : minimiser x²+y² sous x+y=1, dont la solution est x=y=1/2. Le second bloc (l. 3058) confirme la co |

### Confiance moyenne (39)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 1168 | `\[ P = ( - ) \]` | `\[ P=\exp\left(-\frac{\Delta E}{T}\right) \]` | Probabilité d'acceptation de Metropolis. La notation du numérateur (ΔE, Δc ou Δf) est un choix d'auteur ; la structure exponentiel |
| 1202 | `\[ (x) \]` | `\[ F(x) \]` | Candidat alternatif : \[ \text{fitness}(x) \]. |
| 1356 | `\[ _x_ {} f(x,) \]` | `\[ \min_x\max_{\delta\in\Delta}f(x,\delta) \]` | Optimisation robuste. Le symbole de l'ensemble d'incertitude (Δ ou 𝒰) est un choix d'auteur. |
| 1400 | `\[ \|\| \]` | `\[ \\|\theta\\| \]` | Un coefficient λ a pu précéder la norme (le grec est détruit sans laisser de trace) ; le résidu ne montre que ‖θ‖. |
| 1424 | `\[ \]` | `\[ \theta \]` | Candidat alternatif : \[ \theta=(W,b) \] — forme donnée en l. 1448 pour les paramètres. |
| 1486 | `\[ h \]` | `\[ L(h) \]` | Candidat alternatif : \[ L_{\text{val}}(h) \]. |
| 1496 | `\[ J() = \]` | `\[ J(\theta)=\mathbb{E}\left[\sum_{t}\gamma^{t}r_t\right] \]` | Récompense cumulée actualisée. L'absence ou la présence du facteur d'actualisation γ est un choix d'auteur ; l'espérance, elle, es |
| 1528 | `\[ \]` | `\[ \min_\tau J(\tau) \]` | La mention explicite des contraintes (s.c. τ∈𝒯) a pu figurer dans le bloc. |
| 1634 | `\[ ⏎  ⏎ - \]` | `\[ \max_w\left(w^{T}\mu ⏎  ⏎ - \lambda w^{T}\Sigma w\right) \]` | Les deux contraintes qui ont survécu (somme des poids égale à 1, poids non négatifs) sont exactement celles de Markowitz, et la ph |
| 1824 | `\[ \]` | `\[ \min_x f(x) \]` | Candidat alternatif : \[ f(x) \] sans l'opérateur. |
| 1844 | `\[ x \]` | `\[ \hat{x} \]` | Rendu : x̂. Le §93 oppose x* (exact) à x̂ (approché) ; le chapeau est la notation la plus courante. |
| 1848 | `\[ f(x) f(x^\*) \]` | `\[ f(\hat{x})\leq\alpha f(x^{*}) \]` | Garantie d'approximation : f(x̂)≤α·f(x*). L'absence de signe + écarte la forme additive f(x̂)≤f(x*)+ε. La restriction « dans certa |
| 1896 | `\[ 0x_i \]` | `\[ 0\leq x_i\leq 1 \]` | La relaxation continue d'une variable binaire est nécessairement l'intervalle [0,1] ; le résidu seul ne prouve pas la borne supéri |
| 2401 | `\[ ^\* = _ () \]` | `\[ \theta^{*}=\arg\max_\theta \mathcal{L}(\theta) \]` | Maximum de vraisemblance. Le symbole de la vraisemblance (𝓛 ou ℓ) est un choix d'auteur. |
| 2827 | `\[ J(P) = (P) \]` | `\[ J(P)=\text{coût}(P) \]` | Le coût d'un plan. Le libellé exact (coût, qualité, valeur) est un choix d'auteur. |
| 3372 | `\[ \]` | `\[ \min_{x\in\mathcal{X}}f(x) \]` | Candidat alternatif : \[ \min_x f(x)\ \text{sous}\ g_i(x)\leq 0 \]. |
| 3376 | `\[ \]` | `\[ \min_\theta L(\theta) \]` | Forme documentée en l. 1004 et l. 1388. |
| 3414 | `\[ \]` | `\[ \nabla f \]` | Le §115 pose que le Domaine I répond à « Comment une fonction varie-t-elle ? », et le §114 ouvre sa liste de structures par ∇f. Ca |
| 3418 | `\[ \]` | `\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]` | Candidat alternatif : \[ \min_x f(x) \]. |
| 3422 | `\[ \]` | `\[ \min_\theta L(\theta) \]` | Candidat alternatif : \[ \theta^{*}=\arg\min_\theta L(\theta) \]. |
| 3432 | `\[ \]` | `\[ \text{l'objectif} \]` | Primitive nommée au §3.2 (fonction objectif) et question 1 du §110 (« Que veut-on optimiser ? »). Le libellé exact est un choix d' |
| 3436 | `\[ \]` | `\[ \text{les variables} \]` | Primitive nommée au §3.1 (variable de décision) et question 2 du §110. |
| 3440 | `\[ \]` | `\[ \text{les contraintes} \]` | Primitive nommée au §3.5 (contrainte) et question 3 du §110. |
| 3444 | `\[ \]` | `\[ \text{la fonction objectif} \]` | Primitive nommée au §3.2 et au §125 (métriques de diagnostic). |
| 3448 | `\[ \]` | `\[ \nabla f \]` | Question 5 du §110 (« La fonction est-elle différentiable ? ») et premier item du §114. |
| 3452 | `\[ \]` | `\[ \text{convexité} \]` | Question 6 du §110, reprise mot pour mot. Le §111 oppose « convexe / non convexe ». |
| 3456 | `\[ \]` | `\[ x\in\{0,1\} \]` | Question 7 du §110 (« continu ou discret ? ») ; le §114 donne x∈{0,1} comme structure de la discrétion. |
| 3460 | `\[ \]` | `\[ \text{optimisation bayésienne} \]` | Question 8 du §110, et le §113 répond par une liste intacte : « Optimisation coûteuse — optimisation bayésienne ; surrogate models |
| 3464 | `\[ \]` | `\[ (f_1,\ldots,f_k) \]` | Le §114 se termine sur (f₁,…,f_k), et le §111 oppose « mono-objectifs / multi-objectifs ». |
| 3468 | `\[ \]` | `\[ x^{*}\ \text{ou}\ \hat{x} \]` | Question 9 du §110, et le §93 oppose exactement \[ x^{\*} \] et la solution approchée. |
| 3476 | `\[ \]` | `\[ \text{un problème réel} \]` | Le §158, qui suit immédiatement, décrit cette transformation en prose intacte : l'optimisation « transforme une question générale  |
| 3480 | `\[ \]` | `\[ \text{un modèle mathématique} \]` | Voir l. 3476. |
| 3484 | `\[ \]` | `\[ \text{une méthode adaptée} \]` | Voir l. 3476. |
| 3488 | `\[ \]` | `\[ \text{une solution validée} \]` | Voir l. 3476. |
| 3506 | `\[ \]` | `\[ \min_\theta L(\theta) \]` | Reprise du §2, lisible en l. 1004. |
| 3510 | `\[ \]` | `\[ \min_\tau J(\tau) \]` | Reprise du §2. |
| 3514 | `\[ \]` | `\[ \min\sum_{i,j}c_{ij}x_{ij} \]` | Reprise du §2 — coût de transport. |
| 3518 | `\[ \]` | `\[ \min_P C(P) \]` | Reprise du §2. |
| 3522 | `\[ \]` | `\[ \max_\theta J(\theta) \]` | Le §133 propose une alternative multi-critères : J=Q−C−T−E. |

### Confiance inconnue — décision requise (53)

| Ligne | Bloc actuel | Ce que le bloc contenait |
|---:|---|---|
| 1116 | `\[ \]` | §51 « Il existe donc un compromis entre : [vide] et : [vide] ». La liste qui précède énumère cinq effets de la taille du batch ; le compromis en oppose deux, ma |
| 1120 | `\[ \]` | §51, second terme du compromis. |
| 1194 | `\[ \]` | §56 « Schéma : [vide] ». Le schéma d'évolution d'un algorithme génétique (sélection → croisement → mutation) tenait en un bloc. |
| 1265 | `\[ \]` | §62 optimisation bayésienne « Principe : [vide] Applications : ». Bloc entièrement détruit. |
| 1303 | `\[ \]` | §63 « Par exemple : [vide] tout en : [vide] et : [vide] Ces objectifs peuvent être contradictoires. ». Trois blocs pour un exemple d'objectifs contradictoires. |
| 1307 | `\[ \]` | §63, deuxième objectif de l'exemple. |
| 1311 | `\[ \]` | §63, troisième objectif de l'exemple. |
| 1436 | `\[ \]` | §71 « La chaîne complète est : [vide] ». Une chaîne, mais le nombre et la nature des maillons ne sont pas déterminés. |
| 1512 | `\[ J() = J_{} ⏎  ⏎ - J_{} ⏎ - J_{} ⏎ - J` | §77 « On peut minimiser : [cinq lignes] sous des contraintes : obstacles, vitesse, accélération, articulation, énergie. ». Un coût J(τ) décomposé en quatre term |
| 1534 | `\[ ( ⏎  ⏎ - ) \]` | §78 logistique « Exemple : [trois lignes : une parenthèse ouvrante, une ligne vide, « - ) »] sous : capacité des véhicules, disponibilité, demandes, horaires, c |
| 1832 | `\[ \]` | §92 « Cela introduit un compromis entre : [vide] ». Un seul bloc pour ce qui est annoncé comme un compromis. |
| 1860 | `\[ \]` | §94 « Un problème peut être facile à formuler mais difficile à résoudre. Il faut donc distinguer : [vide] ». |
| 1884 | `\[ \]` | §95 « Schéma : [vide] ». |
| 2039 | `\[ ⏎  ⏎ - \]` | §105 « Le coût d'un optimiseur dépend de : [trois lignes] Pour les modèles modernes, le coût total est souvent dominé par l'évaluation répétée du modèle et des  |
| 2174 | `\[ \]` | §109 « Il faut suivre une chaîne : [vide] C'est cette chaîne qui transforme les mathématiques en système exploitable. ». |
| 2357 | `\[ \]` | §114, dixième item — bloc vide entre la norme L2 et l'espérance. Deux blocs consécutifs (l. 2357 et l. 2359) manquent dans une liste par ailleurs parfaitement l |
| 2359 | `\[ \]` | §114, onzième item — bloc vide. |
| 2379 | `\[ \]` | §115 « Le Domaine I répond notamment à : Comment une fonction varie-t-elle ? Le Domaine J demande : Comment exploiter cette variation pour trouver une solution  |
| 2383 | `\[ \]` | §115, second bloc de la relation avec le Domaine I. |
| 2573 | `\[ ⏎  ⏎ - \]` | §126 « Une bonne expérimentation compare : [trois lignes] et mesure : [trois lignes] Il faut éviter de conclure sur une seule exécution… ». |
| 2579 | `\[ ⏎  ⏎ - \]` | §126, second bloc : « et mesure : [trois lignes] ». |
| 2607 | `\[ \]` | §128 « Par exemple : [quatre blocs vides] Comprendre l'optimisation signifie donc aussi comprendre les **compromis**. ». |
| 2609 | `\[ \]` | §128, deuxième bloc. |
| 2611 | `\[ \]` | §128, troisième bloc. |
| 2613 | `\[ \]` | §128, quatrième bloc. |
| 2649 | `\[ \]` | §131 « ### Réseau / Minimiser la latence ou maximiser le débit. Ainsi : [vide] Cette formule est volontairement conceptuelle… ». |
| 2688 | `\[ ( ⏎  ⏎ - ) \]` | §131 « Exemple conceptuel : [trois lignes : « ( », ligne vide, « - ) »] ». Même gabarit qu'en l. 1534. |
| 2732 | `\[ ⏎  ⏎ - \]` | §133 « ### Coût / Minimiser : [trois lignes] ». |
| 2771 | `\[ \]` | §134 « Le système doit déterminer : [vide] » — un seul bloc. Les objectifs, eux, sont donnés en liste et ont survécu : minimiser temps, coût, redondance ; maxim |
| 2791 | `\[ J = ⏎  ⏎ - \]` | §135 Stane OS « Dans un système personnel intelligent, on peut théoriquement optimiser : [J = / - ] Le système peut alors décider : quel modèle utiliser, quel o |
| 2817 | `\[ \]` | §136 « Cela donne : [vide] ». |
| 2839 | `\[ \]` | §138 « Chaîne : [vide] ». |
| 2847 | `\[ ⏎  ⏎ - \]` | §139 « Un système logistique peut optimiser simultanément : [trois lignes] Cela produit souvent des problèmes multi-objectifs, combinatoires ou mixtes. ». |
| 2857 | `\[ \]` | §140 « On peut optimiser : [cinq blocs vides] La théorie des graphes et l'optimisation se complètent alors directement. ». |
| 2859 | `\[ \]` | §140, deuxième bloc. |
| 2861 | `\[ \]` | §140, troisième bloc. |
| 2863 | `\[ \]` | §140, quatrième bloc. |
| 2865 | `\[ \]` | §140, cinquième bloc. |
| 3042 | `\[ \]` | §147 exercice 2 « Appliquer gradient descent à : [f(x)=x²] avec : [vide] et : [x_0=10] Calculer plusieurs itérations. ». Le bloc manquant est le pas d'apprentis |
| 3091 | `\[ \]` | §152 « Demander à une IA : « … Identifie d'abord les variables, l'objectif, les contraintes… » Puis comparer : [vide] ». |
| 3380 | `\[ \]` | §154 « Pour un système : [vide] ». |
| 3386 | `\[ \]` | §155 « La progression construite jusqu'ici peut être comprise comme : [dix blocs vides] La transition : [I→J] est particulièrement importante. ». |
| 3388 | `\[ \]` | §155, deuxième bloc. |
| 3390 | `\[ \]` | §155, troisième bloc. |
| 3392 | `\[ \]` | §155, quatrième bloc. |
| 3394 | `\[ \]` | §155, cinquième bloc. |
| 3396 | `\[ \]` | §155, sixième bloc. |
| 3398 | `\[ \]` | §155, septième bloc. |
| 3400 | `\[ \]` | §155, huitième bloc. |
| 3402 | `\[ \]` | §155, neuvième bloc. |
| 3404 | `\[ \]` | §155, dixième bloc. |
| 3526 | `\[ \]` | §158 « Et dans l'ingénierie logicielle : [vide] ». Rubrique absente du §2 : aucun équivalent survivant dans le document. |
| 3534 | `\[ \]` | §158 « Le Domaine I explique comment une fonction change. Le Domaine J explique comment exploiter cette information pour rechercher une solution. Ensemble : [vi |

