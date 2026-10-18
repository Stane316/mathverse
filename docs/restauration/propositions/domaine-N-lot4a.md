# LOT 4a — DOMAINE N : TRANSFORMÉES (sections 1 à 64)

**Date :** 2026-10-18 · **Statut :** propositions soumises, non appliquées
**Document :** `DOCUMENT N — TRANSFORMÉES.md`
**Portée :** lignes 75 à 1 301. Le reste du document (sections 65 à 178, lignes 1 309 à 3 940) fera l'objet du **lot 4b**.
**Méthode :** relecture intégrale des 248 blocs d'affichage, un par un.

---

## 1. Les règles de dégradation propres au document N

| Résidu | Ce qui a été détruit | Exemple |
|---|---|---|
| rien | **lettres grecques, y compris `\pi`** | `e^{-i2kn/N}` → `e^{-i2\pi kn/N}` |
| `,` (virgule) | `\,` (espace fine) **et** `\ldots` | `f(t)e^{-it},dt` ; `k=0,,N-1` |
| `{…}` | `\mathcal{F}` ou `\mathcal{L}` | `{af+bg} = aF+bG` → `\mathcal{F}\{af+bg\}=aF+bG` |
| `\_` | `\int` **ou** `\sum` — le contexte tranche | `\_0^T` → `\frac{2}{T}\int_0^T` |
| `\_2N` | `\log_2 N` | le `\log` disparaît, son indice reste |
| `_{10}` | `\log_{10}` | `20_{10}|H(i)|` → `20\log_{10}|H(i\omega)|` |
| `(…)` | `\max`, `\min`, `\mathrm{sign}` | `(\|x\|-,0)` → `\max(\|x\|-\lambda,0)` |
| deux termes accolés | `\to` | `x T(x)` → `x\to T(x)` |
| `\[ … \]` dans un bloc | crochets échappés, résidu de `[…]` ou de `\mathbb{E}[…]` | l. 190, 2 747 |

**Le cas le plus trompeur : le `\pi` détruit.** Dans `e^{-i2kn/N}`, rien n'indique visuellement qu'un
π manquait. C'est la cohérence mathématique — une DFT sans 2π n'est pas une DFT — qui impose la
restitution. Ce type de destruction est invisible à toute heuristique.

## 2. Deux familles de blocs, deux traitements

**Les blocs de propriétés** (§12, §33) portent une signature constante : `\mathcal{F}` ou
`\mathcal{L}` détruit, **accolades conservées**. La reconstruction est mécanique et sûre :

```
\[ {af+bg} = aF+bG \]      →  𝓕{af+bg} = aF+bG
\[ {f\*g} = FG \]          →  𝓕{f∗g} = F·G
\[ {f’} = sF(s)-f(0) \]    →  𝓛{f'} = sF(s)-f(0)
```

**Les blocs de définition** (§5, §9, §18, §31) perdent leurs fonctions et leurs bornes : `\cos`,
`\sin`, `\int`, `\infty`. Ils sont reconnaissables à ce que deux blocs voisins deviennent
**identiques en apparence** — c'est précisément le signe de la destruction, et le meilleur
indicateur pour les repérer à la lecture.

## 3. La convention de normalisation est un choix, pas une restitution

Le document emploie la convention `F(ω)=∫f(t)e^{-iωt}dt` et `f(t)=(1/2π)∫F(ω)e^{iωt}dω`. La
phrase qui suit le bloc le rappelle : « Les conventions de normalisation et de signe peuvent
varier selon les disciplines. » Les reconstructions des lignes 247 et 251 sont donc cohérentes
entre elles, mais **si votre convention était différente, il faut me le dire** : six blocs du
document en dépendent.

## 4. Corps technique

**Correctif :** `domaine-N-lot4a.patch.json` — 75 entrées : 55 haute, 7 moyenne, 13 inconnue — **62 applicables**

### Confiance haute (55)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 75 | `\[ f F \]` | `\[ f \to F \]` | Rendu : f → F. |
| 190 | `\[ f(t) = ⏎  ⏎ - \_{n=1}^{} \[ a_n(n_0t) ⏎ - b` | `\[ f(t)=\frac{a_0}{2} ⏎  ⏎ + \sum_{n=1}^{\infty}\left[a_n\cos(` | Forme canonique de la série de Fourier trigonométrique. Le terme a_0/2 est restitué d'après la ligne vide et l'usage ; à confirmer |
| 197 | `\[ \_0= \]` | `\[ \omega_0=\frac{2\pi}{T} \]` | Rendu : ω₀=2π/T. |
| 203 | `\[ a_n= \_0^T f(t)(n_0t),dt \]` | `\[ a_n=\frac{2}{T}\int_0^T f(t)\cos(n\omega_0t)\,dt \]` | Rendu : a_n=(2/T)∫₀ᵗ f(t)cos(nω₀t)dt. |
| 207 | `\[ b_n= \_0^T f(t)(n_0t),dt \]` | `\[ b_n=\frac{2}{T}\int_0^T f(t)\sin(n\omega_0t)\,dt \]` | Rendu : b_n=(2/T)∫₀ᵗ f(t)sin(nω₀t)dt. |
| 215 | `\[ f(t) = \_{n=-}^{+} c_ne^{in_0t} \]` | `\[ f(t)=\sum_{n=-\infty}^{+\infty}c_ne^{in\omega_0t} \]` | Rendu : f(t)=Σ_{n=-∞}^{+∞} c_n e^{inω₀t}. |
| 219 | `\[ c_n= \_0^T f(t)e^{-in_0t},dt \]` | `\[ c_n=\frac{1}{T}\int_0^T f(t)e^{-in\omega_0t}\,dt \]` | Vérifier : la forme complexe utilise 1/T, la forme trigonométrique 2/T. |
| 247 | `\[ F() = \_{-}^{+} f(t)e^{-it},dt \]` | `\[ F(\omega)=\int_{-\infty}^{+\infty}f(t)e^{-i\omega t}\,dt \]` | Rendu : F(ω)=∫_{-∞}^{+∞} f(t)e^{-iωt}dt. La phrase suivante rappelle que les conventions varient. |
| 251 | `\[ f(t) = \_{-}^{+} F()e^{it},d \]` | `\[ f(t)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}F(\omega)e^{i\om` | Rendu : f(t)=(1/2π)∫F(ω)e^{iωt}dω. Cohérent avec la convention retenue en l. 247. |
| 267 | `\[ F() \]` | `\[ F(\omega) \]` | Rendu : F(ω). |
| 284 | `\[ \|F()\| = \]` | `\[ \|F(\omega)\|=\sqrt{a(\omega)^{2}+b(\omega)^{2}} \]` | Rendu : \|F(ω)\|=√(a²+b²). |
| 288 | `\[ () = (F()) \]` | `\[ \varphi(\omega)=\arg(F(\omega)) \]` | Rendu : φ(ω)=arg(F(ω)). |
| 304 | `\[ {af+bg} = aF+bG \]` | `\[ \mathcal{F}\{af+bg\}=aF+bG \]` | Rendu : 𝓕{af+bg}=aF+bG. |
| 314 | `\[ G()=e^{-it_0}F() \]` | `\[ G(\omega)=e^{-i\omega t_0}F(\omega) \]` | Rendu : G(ω)=e^{-iωt₀}F(ω). |
| 322 | `\[ {f\*g} = FG \]` | `\[ \mathcal{F}\{f\ast g\}=F\cdot G \]` | Rendu : 𝓕{f∗g}=F·G. |
| 326 | `\[ {fg} \]` | `\[ \mathcal{F}\{fg\}=F\ast G \]` | Rendu : 𝓕{fg}=F∗G. Dualité de la ligne précédente. |
| 336 | `\[ (f\*g)(t) = \_{-}^{+} f()g(t-),d \]` | `\[ (f\ast g)(t)=\int_{-\infty}^{+\infty}f(\tau)g(t-\tau)\,d\ta` | Rendu : (f∗g)(t)=∫f(τ)g(t−τ)dτ. |
| 373 | `\[ Y()=X()H() \]` | `\[ Y(\omega)=X(\omega)H(\omega) \]` | Rendu : Y(ω)=X(ω)H(ω). |
| 377 | `\[ H()= \]` | `\[ H(\omega)=\frac{Y(\omega)}{X(\omega)} \]` | Rendu : H(ω)=Y(ω)/X(ω). |
| 405 | `\[ Y()=X()H() \]` | `\[ Y(\omega)=X(\omega)H(\omega) \]` | Rendu : Y(ω)=X(ω)H(ω). |
| 425 | `\[ f_N= \]` | `\[ f_N=\frac{f_s}{2} \]` | Rendu : f_N=f_s/2. |
| 429 | `\[ f_s>2f_{} \]` | `\[ f_s>2f_{\max} \]` | Rendu : f_s>2f_max. |
| 461 | `\[ X\[k\] = \_{n=0}^{N-1} x\[n\]e^{-i2kn/N} \]` | `\[ X[k]=\sum_{n=0}^{N-1}x[n]e^{-i2\pi kn/N} \]` | Rendu : X[k]=Σ_{n=0}^{N-1} x[n]e^{-i2πkn/N}. |
| 465 | `\[ k=0,,N-1 \]` | `\[ k=0,\ldots,N-1 \]` | Rendu : k=0,…,N−1. |
| 469 | `\[ x\[n\] = \_{k=0}^{N-1} X\[k\]e^{i2kn/N} \]` | `\[ x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{i2\pi kn/N} \]` | Rendu : x[n]=(1/N)Σ X[k]e^{i2πkn/N}. |
| 497 | `\[ f_k= \]` | `\[ f_k=\frac{kf_s}{N} \]` | Rendu : f_k=k·f_s/N. |
| 501 | `\[ f= \]` | `\[ \Delta f=\frac{f_s}{N} \]` | Rendu : Δf=f_s/N. |
| 547 | `\[ O(NN) \]` | `\[ O(N\log N) \]` | Rendu : O(N log N). |
| 562 | `\[ X\[k\] = \_{m=0}^{N/2-1} x\[2m\]e^{-i2k(2m)` | `\[ X[k]=\sum_{m=0}^{N/2-1}x[2m]e^{-i2\pi k(2m)/N} ⏎  ⏎ + \sum_` | Première étape de Cooley-Tukey : séparation des termes pairs et impairs. |
| 574 | `\[ W_N=e^{-i2/N} \]` | `\[ W_N=e^{-i2\pi/N} \]` | Rendu : W_N=e^{-i2π/N}. |
| 596 | `\[ \_2N \]` | `\[ \log_2 N \]` | Rendu : log₂ N. |
| 606 | `\[ O(N_2N) \]` | `\[ O(N\log_2 N) \]` | Rendu : O(N log₂ N). |
| 666 | `\[ C_k = _k_ {n=0}^{N-1} x_n \]` | `\[ C_k=\alpha_k\sum_{n=0}^{N-1}x_n\cos\left(\frac{\pi}{N}\left` | Forme DCT-II. L'argument du cosinus est restitué d'après la forme standard ; à confirmer. |
| 712 | `\[ F(s) = \_0^ f(t)e^{-st},dt \]` | `\[ F(s)=\int_0^{\infty}f(t)e^{-st}\,dt \]` | Rendu : F(s)=∫₀^∞ f(t)e^{-st}dt. |
| 716 | `\[ s=+i \]` | `\[ s=\sigma+i\omega \]` | Rendu : s=σ+iω. |
| 726 | `\[ {y’} = sY(s)-y(0) \]` | `\[ \mathcal{L}\{y'\}=sY(s)-y(0) \]` | Rendu : 𝓛{y'}=sY(s)−y(0). |
| 744 | `\[ {af+bg} = aF+bG \]` | `\[ \mathcal{L}\{af+bg\}=aF+bG \]` | Rendu : 𝓛{af+bg}=aF+bG. |
| 748 | `\[ {f’} = sF(s)-f(0) \]` | `\[ \mathcal{L}\{f'\}=sF(s)-f(0) \]` | Rendu : 𝓛{f'}=sF(s)−f(0). |
| 752 | `\[ {f’‘} = s^2F(s)-sf(0)-f’(0) \]` | `\[ \mathcal{L}\{f''\}=s^{2}F(s)-sf(0)-f'(0) \]` | Rendu : 𝓛{f''}=s²F(s)−sf(0)−f'(0). |
| 756 | `\[ {f\*g} = F(s)G(s) \]` | `\[ \mathcal{L}\{f\ast g\}=F(s)G(s) \]` | Rendu : 𝓛{f∗g}=F(s)G(s). |
| 776 | `\[ H(s)= \]` | `\[ H(s)=\frac{N(s)}{D(s)} \]` | Rendu : H(s)=N(s)/D(s). |
| 805 | `\[ n \]` | `\[ n\geq 0 \]` | Rendu : n ≥ 0. |
| 845 | `\[ z=e^{i} \]` | `\[ z=e^{i\omega} \]` | Rendu : z=e^{iω}. |
| 895 | `\[ X(,) = x(t)w(t-)e^{-it},dt \]` | `\[ X(\tau,\omega)=\int x(t)w(t-\tau)e^{-i\omega t}\,dt \]` | Rendu : X(τ,ω)=∫x(t)w(t−τ)e^{-iωt}dt. |
| 901 | `\[ \|X(,)\|^2 \]` | `\[ \|X(\tau,\omega)\|^{2} \]` | Rendu : \|X(τ,ω)\|². |
| 942 | `\[ (t) \]` | `\[ \psi(t) \]` | Rendu : ψ(t). |
| 946 | `\[ \_{a,b}(t) = ( ) \]` | `\[ \psi_{a,b}(t)=\frac{1}{\sqrt{a}}\psi\left(\frac{t-b}{a}\rig` | Rendu : ψ_{a,b}(t)=(1/√a)ψ((t−b)/a). Forme usuelle de la dilatation-translation. |
| 952 | `\[ W(a,b) = x(t) dt \]` | `\[ W(a,b)=\int x(t)\psi_{a,b}(t)\,dt \]` | Rendu : W(a,b)=∫x(t)ψ_{a,b}(t)dt. |
| 1058 | `\[ x(t)=A(2f_0t) \]` | `\[ x(t)=A\sin(2\pi f_0t) \]` | Rendu : x(t)=A sin(2πf₀t). |
| 1153 | `\[ xT(x) \]` | `\[ x\to T(x) \]` | Rendu : x → T(x). |
| 1165 | `\[ xz \]` | `\[ x\to z \]` | Rendu : x → z. |
| 1274 | `\[ u(x) \_{k=0}^{N} a_k_k(x) \]` | `\[ u(x)\approx\sum_{k=0}^{N}a_k\phi_k(x) \]` | Rendu : u(x)≈Σ a_k φ_k(x). |
| 1278 | `\[ \_k(x) \]` | `\[ \phi_k(x) \]` | Rendu : φ_k(x). |
| 1295 | `\[ u(x,t) U(k,t) \]` | `\[ u(x,t)\to U(k,t) \]` | Rendu : u(x,t) → U(k,t). |
| 1301 | `\[ { } = -k^2U(k,t) \]` | `\[ \mathcal{F}\left\{\frac{\partial^{2}u}{\partial x^{2}}\righ` | Rendu : 𝓕{∂²u/∂x²}=−k²U(k,t). |

### Confiance moyenne (7)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 280 | `\[ F()=a()+ib() \]` | `\[ F(\omega)=a(\omega)+ib(\omega) \]` | Candidat alternatif : F(\omega)=\Re(F)+i\Im(F). La notation a/b est celle du résidu. |
| 475 | `\[ \]` | `\[ x[n] \]` | Candidat alternatif : \mathbf{x}. La notation à confirmer. |
| 479 | `\[ \]` | `\[ X[k] \]` | Candidat alternatif : \mathbf{X}. |
| 1066 | `\[ x(t)= ⏎  ⏎ \]` | `\[ x(t)=\sin(2\pi f_1t)+\sin(2\pi f_2t) \]` | Candidat alternatif : un chirp, \[ x(t)=\sin(2\pi f(t)t) \]. Le premier candidat est le plus courant pour illustrer la perte de lo |
| 1157 | `\[ x(x) \]` | `\[ x\to \phi(x) \]` | Candidat alternatif : x\to \varphi(x). |
| 1161 | `\[ x \]` | `\[ x\to \tilde{x} \]` | Candidat alternatif : x\to \hat{x}. |
| 1169 | `\[ x \]` | `\[ x\to X \]` | Candidat alternatif : x\to T(x), mais cela répéterait l. 1153. |

### Confiance inconnue — décision requise (13)

| Ligne | Bloc actuel | Ce que le bloc contenait |
|---:|---|---|
| 142 | `\[ \]` | §3 « La convolution devient une multiplication. On peut donc avoir : [vide] C'est précisément cette propriété qui explique l'importance des transformées en info |
| 231 | `\[ \]` | §8 « La série de Fourier dit essentiellement : … Cela permet de passer : [vide] Cette idée est fondamentale pour : ». |
| 439 | `\[ \]` | §17 « Ce phénomène est appelé : [vide] Il est particulièrement important en : ». Le titre de la section donne le terme, mais la forme exacte du bloc reste incon |
| 676 | `\[ \]` | §30 « Principe général : [vide] L'idée est de représenter efficacement les informations importantes. » |
| 732 | `\[ \]` | §32 « On passe de : [vide] à : [vide] puis on effectue la transformée inverse. » |
| 736 | `\[ \]` | §32, pendant du bloc précédent. |
| 768 | `\[ \]` | §34 « Il faut également déterminer les valeurs de (s) pour lesquelles l'intégrale converge. On parle de : [vide] ». |
| 964 | `\[ \]` | §47 « L'échelle possède une relation inverse approximative avec la fréquence : [vide] [vide] ». Deux blocs vides consécutifs. |
| 966 | `\[ \]` | §47, second bloc. |
| 1085 | `\[ \]` | §54 reconnaissance vocale « On peut appliquer : [vide] On peut également utiliser : ». |
| 1190 | `\[ \]` | §58 « Une donnée temporelle devient ainsi une structure 2D exploitable par des architectures de vision. Cela crée un pont entre : [vide] ». |
| 1226 | `\[ \]` | §60 transformée de Radon « Conceptuellement : [vide] Elle constitue notamment une base mathématique importante de la tomographie. » |
| 1258 | `\[ \]` | §62 transformées et simulation « Exemple conceptuel : [vide] Elles peuvent donc servir à : ». |

