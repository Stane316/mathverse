# Rapport d'application — docs/restauration/propositions/domaine-N-lot4b.patch.json

**Date :** 2026-10-18 — **Mode :** écriture

Entrées du correctif : 104 — appliquées : 84

| Fichier | L. avant | L. après | Confiance | Ancien | Nouveau |
|---|---:|---:|---|---|---|
| DOCUMENT N — TRANSFORMÉES.md | 1309 | 1309 | haute | `\[ z(t)=x(t)+i{x(t)} \]` | `\[ z(t)=x(t)+i\mathcal{H}\{x(t)\} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1350 | 1350 | haute | `\[ x ax \]` | `\[ x\to ax \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1389 | 1389 | haute | `\[ x=\_k c_k_k \]` | `\[ x=\sum_k c_k\phi_k \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1409 | 1409 | haute | `\[ x^N \]` | `\[ x\in\mathbb{R}^{N} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1417 | 1417 | haute | `\[ T^{NN} \]` | `\[ T\in\mathbb{R}^{N\times N} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1427 | 1427 | haute | `\[ {\_k} \]` | `\[ \{\phi_k\} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1431 | 1431 | haute | `\[ \_i,_j =_ {ij} \]` | `\[ \langle\phi_i,\phi_j\rangle=\delta_{ij} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1449 | 1449 | haute | `\[ x T(x) \]` | `\[ x\to T(x) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1453 | 1453 | moyenne | `\[ T(x) âµ  âµ \]` | `\[ T(x)=(c_1,\ldots,c_n) âµ \text{avec la plupart des } c_i\approx 0 \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1469 | 1468 | haute | `\[ c_i’= âµ  âµ \]` | `\[ c_i'=\begin{cases}c_i&\text{si }\|c_i\|>\lambda\\ 0&\text{sinon}\end{cases} \` |
| DOCUMENT N — TRANSFORMÉES.md | 1485 | 1482 | haute | `\[ S_(x) = x,\_{\|x\|} \]` | `\[ S_\lambda(x)=x\cdot\mathbf{1}_{\|x\|>\lambda} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1489 | 1486 | haute | `\[ S_(x) = (x) (\|x\|-,0) \]` | `\[ S_\lambda(x)=\mathrm{sign}(x)\max(\|x\|-\lambda,0) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1505 | 1502 | haute | `\[ mn \]` | `\[ m\ll n \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1527 | 1524 | haute | `\[ z=f_(x) \]` | `\[ z=f_\theta(x) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1533 | 1530 | haute | `\[ z=f_(T(x)) \]` | `\[ z=f_\theta(T(x)) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1694 | 1694 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 1720 | 1717 | haute | `\[ N(x) = \_{k=0}^{K} a_kN_k(x) \]` | `\[ N(x)=\sum_{k=0}^{K}a_kN_k(x) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1795 | 1792 | haute | `\[ H(i) \]` | `\[ H(i\omega) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1801 | 1798 | haute | `\[ 20_{10}\|H(i)\| \]` | `\[ 20\log_{10}\|H(i\omega)\| \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1805 | 1802 | haute | `\[ H(i) \]` | `\[ \arg(H(i\omega)) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1817 | 1817 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 1926 | 1923 | haute | `\[ e^{-it_0} \]` | `\[ e^{-i\omega t_0} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1932 | 1929 | haute | `\[ \_g() = - \]` | `\[ \tau_g(\omega)=-\frac{d\varphi}{d\omega} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1955 | 1952 | haute | `\[ x X x \]` | `\[ x\to X\to x \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1973 | 1970 | haute | `\[ xy \]` | `\[ x\to y \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1977 | 1974 | haute | `\[ yx \]` | `\[ y\to x \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1987 | 1984 | haute | `\[ X= \]` | `\[ X=H^{-1}Y \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1993 | 1990 | haute | `\[ \|H\| \]` | `\[ \|H\|\approx 0 \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2005 | 2005 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2011 | 2011 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2032 | 2032 | inconnue | `\[ âµ  âµ - \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2046 | 2043 | haute | `\[ O(NN) \]` | `\[ O(N\log N) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2052 | 2052 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2060 | 2057 | haute | `\[ (x\*h) = (x)(h) \]` | `\[ \mathcal{F}\{x\ast h\}=\mathcal{F}\{x\}\cdot\mathcal{F}\{h\} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2109 | 2106 | haute | `\[ T_{} < T_{} \]` | `\[ T_{\text{calcul}}<T_{\text{disponible}} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2173 | 2173 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2251 | 2248 | haute | `\[ T_1,T_2,,T_k \]` | `\[ T_1,T_2,\ldots,T_k \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2265 | 2262 | haute | `\[ T^ = \_T (T,x) \]` | `\[ \hat{T}=\arg\max_T \mathrm{score}(T,x) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2280 | 2277 | haute | `\[ T_ \]` | `\[ T_\theta \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2286 | 2283 | haute | `\[ ^ = _L(T_(x),y) \]` | `\[ \hat{\theta}=\arg\min_\theta L(T_\theta(x),y) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2301 | 2298 | moyenne | `\[ \]` | `\[ \nabla_\theta L \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2307 | 2307 | inconnue | `\[ âµ  âµ - \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2383 | 2380 | moyenne | `\[ \]` | `\[ \text{Fourier} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2391 | 2388 | moyenne | `\[ \]` | `\[ \text{Laplace} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2399 | 2396 | moyenne | `\[ \]` | `\[ \text{transformée en Z} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2407 | 2404 | moyenne | `\[ \]` | `\[ \text{STFT} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2415 | 2412 | moyenne | `\[ \]` | `\[ \text{ondelettes} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2423 | 2420 | moyenne | `\[ \]` | `\[ \text{DCT} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2537 | 2534 | haute | `\[ x\[n\]=(2f n/f_s) \]` | `\[ x[n]=\sin(2\pi fn/f_s) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2557 | 2554 | haute | `\[ x T(x) T^{-1}(T(x)) \]` | `\[ x\to T(x)\to T^{-1}(T(x)) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2561 | 2558 | haute | `\[ \|x-T^{-1}(T(x))\| \]` | `\[ \\|x-T^{-1}(T(x))\\| \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2589 | 2586 | haute | `\[ X\[N-k\] = \]` | `\[ X[N-k]=\overline{X[k]} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2601 | 2601 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2605 | 2605 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2639 | 2636 | haute | `\[ c Q(c) \]` | `\[ c\to Q(c) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2647 | 2647 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2653 | 2650 | haute | `\[ x T(x) Q C \]` | `\[ x\to T(x)\to Q\to C \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2663 | 2660 | haute | `\[ C Q^{-1} T^{-1} \]` | `\[ \hat{x}=T^{-1}(Q^{-1}(C)) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2667 | 2664 | haute | `\[ x \]` | `\[ \hat{x} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2675 | 2672 | haute | `\[ =x \]` | `\[ \hat{x}=x \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2699 | 2699 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2747 | 2744 | haute | `\[ \_X(t) = \[e^{itX}\] \]` | `\[ \varphi_X(t)=\mathbb{E}\left[e^{itX}\right] \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2774 | 2771 | haute | `\[ x:V \]` | `\[ x:V\to\mathbb{R} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2780 | 2780 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2814 | 2811 | haute | `\[ x T(x) z T^{-1}() \]` | `\[ x\to T(x)\to z\to T^{-1}(z) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2824 | 2824 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2851 | 2848 | haute | `\[ x T(x) T^{-1} x’ \]` | `\[ x\to T(x)\to T^{-1}\to x' \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2872 | 2869 | haute | `\[ x_0,x_1,,x_N \]` | `\[ x_0,x_1,\ldots,x_N \]` |
| DOCUMENT N — TRANSFORMÉES.md | 2914 | 2914 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2918 | 2918 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 2922 | 2919 | haute | `\[ (x) = d(T(x),) \]` | `\[ s(x)=d(T(x),\mu) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3068 | 3065 | haute | `\[ T^{-1}(T(x))x \]` | `\[ T^{-1}(T(x))\approx x \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3140 | 3137 | moyenne | `\[ \]` | `\[ \text{transformée de Fourier} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3154 | 3151 | moyenne | `\[ \]` | `\[ \text{FFT} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3169 | 3166 | moyenne | `\[ \]` | `\[ \text{Laplace} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3183 | 3180 | moyenne | `\[ \]` | `\[ \text{transformée en Z} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3197 | 3194 | moyenne | `\[ \]` | `\[ \text{STFT} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3212 | 3209 | moyenne | `\[ \]` | `\[ \text{ondelettes} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3225 | 3222 | moyenne | `\[ \]` | `\[ \text{DCT} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3231 | 3228 | moyenne | `\[ \]` | `\[ \text{la DFT et la FFT} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3248 | 3245 | moyenne | `\[ \]` | `\[ \text{la transformée de Fourier et la DFT} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3426 | 3426 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 3438 | 3435 | haute | `\[ X(f) H(f) Y(f) \]` | `\[ X(f)\to H(f)\to Y(f) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3470 | 3467 | haute | `\[ x DWT Threshold IDWT \]` | `\[ x\to \text{DWT}\to \text{seuil}\to \text{IDWT} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3530 | 3527 | haute | `\[ O(NN) \]` | `\[ O(N\log N) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3600 | 3597 | haute | `\[ T^ \]` | `\[ \hat{T} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3610 | 3610 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 3720 | 3720 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 3794 | 3794 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 3858 | 3855 | moyenne | `\[ \]` | `\[ \text{changer de représentation pour simplifier le problème} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3862 | 3859 | moyenne | `\[ \]` | `\[ \text{une fonction en spectre} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3866 | 3863 | moyenne | `\[ \]` | `\[ \text{une fonction temporelle en F(s)} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3870 | 3867 | moyenne | `\[ \]` | `\[ \text{une séquence en X(z)} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3874 | 3871 | moyenne | `\[ \]` | `\[ \text{un signal en représentation temps-fréquence} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3878 | 3875 | moyenne | `\[ \]` | `\[ \text{un signal en échelles et détails} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3882 | 3879 | moyenne | `\[ \]` | `\[ \text{des données en coefficients cosinus} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3898 | 3895 | moyenne | `\[ \]` | `\[ \text{transformer} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3900 | 3897 | moyenne | `\[ \]` | `\[ \text{voir} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3902 | 3899 | moyenne | `\[ \]` | `\[ \text{comprendre} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3904 | 3901 | moyenne | `\[ \]` | `\[ \text{simplifier} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3906 | 3903 | moyenne | `\[ \]` | `\[ \text{calculer} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3908 | 3905 | moyenne | `\[ \]` | `\[ \text{construire} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3935 | 3932 | moyenne | `\[ \]` | `\[ \text{chercher la représentation qui simplifie} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 3939 | 3936 | moyenne | `\[ \]` | `\[ \text{vérifier les hypothèses et les limites} \]` |
