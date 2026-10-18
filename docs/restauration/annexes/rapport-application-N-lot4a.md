# Rapport d'application — docs/restauration/propositions/domaine-N-lot4a.patch.json

**Date :** 2026-10-18 — **Mode :** écriture

Entrées du correctif : 75 — appliquées : 62

| Fichier | L. avant | L. après | Confiance | Ancien | Nouveau |
|---|---:|---:|---|---|---|
| DOCUMENT N — TRANSFORMÉES.md | 75 | 75 | haute | `\[ f F \]` | `\[ f \to F \]` |
| DOCUMENT N — TRANSFORMÉES.md | 142 | 142 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 190 | 190 | haute | `\[ f(t) = âµ  âµ - \_{n=1}^{} \[ a_n(n_0t) âµ - b_n(n_0t) \]` | `\[ f(t)=\frac{a_0}{2} âµ  âµ + \sum_{n=1}^{\infty}\left[a_n\cos(n\omega_0t)+b_n\` |
| DOCUMENT N — TRANSFORMÉES.md | 197 | 196 | haute | `\[ \_0= \]` | `\[ \omega_0=\frac{2\pi}{T} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 203 | 202 | haute | `\[ a_n= \_0^T f(t)(n_0t),dt \]` | `\[ a_n=\frac{2}{T}\int_0^T f(t)\cos(n\omega_0t)\,dt \]` |
| DOCUMENT N — TRANSFORMÉES.md | 207 | 206 | haute | `\[ b_n= \_0^T f(t)(n_0t),dt \]` | `\[ b_n=\frac{2}{T}\int_0^T f(t)\sin(n\omega_0t)\,dt \]` |
| DOCUMENT N — TRANSFORMÉES.md | 215 | 214 | haute | `\[ f(t) = \_{n=-}^{+} c_ne^{in_0t} \]` | `\[ f(t)=\sum_{n=-\infty}^{+\infty}c_ne^{in\omega_0t} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 219 | 218 | haute | `\[ c_n= \_0^T f(t)e^{-in_0t},dt \]` | `\[ c_n=\frac{1}{T}\int_0^T f(t)e^{-in\omega_0t}\,dt \]` |
| DOCUMENT N — TRANSFORMÉES.md | 231 | 231 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 247 | 246 | haute | `\[ F() = \_{-}^{+} f(t)e^{-it},dt \]` | `\[ F(\omega)=\int_{-\infty}^{+\infty}f(t)e^{-i\omega t}\,dt \]` |
| DOCUMENT N — TRANSFORMÉES.md | 251 | 250 | haute | `\[ f(t) = \_{-}^{+} F()e^{it},d \]` | `\[ f(t)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}F(\omega)e^{i\omega t}\,d\omega \]` |
| DOCUMENT N — TRANSFORMÉES.md | 267 | 266 | haute | `\[ F() \]` | `\[ F(\omega) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 280 | 279 | moyenne | `\[ F()=a()+ib() \]` | `\[ F(\omega)=a(\omega)+ib(\omega) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 284 | 283 | haute | `\[ \|F()\| = \]` | `\[ \|F(\omega)\|=\sqrt{a(\omega)^{2}+b(\omega)^{2}} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 288 | 287 | haute | `\[ () = (F()) \]` | `\[ \varphi(\omega)=\arg(F(\omega)) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 304 | 303 | haute | `\[ {af+bg} = aF+bG \]` | `\[ \mathcal{F}\{af+bg\}=aF+bG \]` |
| DOCUMENT N — TRANSFORMÉES.md | 314 | 313 | haute | `\[ G()=e^{-it_0}F() \]` | `\[ G(\omega)=e^{-i\omega t_0}F(\omega) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 322 | 321 | haute | `\[ {f\*g} = FG \]` | `\[ \mathcal{F}\{f\ast g\}=F\cdot G \]` |
| DOCUMENT N — TRANSFORMÉES.md | 326 | 325 | haute | `\[ {fg} \]` | `\[ \mathcal{F}\{fg\}=F\ast G \]` |
| DOCUMENT N — TRANSFORMÉES.md | 336 | 335 | haute | `\[ (f\*g)(t) = \_{-}^{+} f()g(t-),d \]` | `\[ (f\ast g)(t)=\int_{-\infty}^{+\infty}f(\tau)g(t-\tau)\,d\tau \]` |
| DOCUMENT N — TRANSFORMÉES.md | 373 | 372 | haute | `\[ Y()=X()H() \]` | `\[ Y(\omega)=X(\omega)H(\omega) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 377 | 376 | haute | `\[ H()= \]` | `\[ H(\omega)=\frac{Y(\omega)}{X(\omega)} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 405 | 404 | haute | `\[ Y()=X()H() \]` | `\[ Y(\omega)=X(\omega)H(\omega) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 425 | 424 | haute | `\[ f_N= \]` | `\[ f_N=\frac{f_s}{2} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 429 | 428 | haute | `\[ f_s>2f_{} \]` | `\[ f_s>2f_{\max} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 439 | 439 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 461 | 460 | haute | `\[ X\[k\] = \_{n=0}^{N-1} x\[n\]e^{-i2kn/N} \]` | `\[ X[k]=\sum_{n=0}^{N-1}x[n]e^{-i2\pi kn/N} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 465 | 464 | haute | `\[ k=0,,N-1 \]` | `\[ k=0,\ldots,N-1 \]` |
| DOCUMENT N — TRANSFORMÉES.md | 469 | 468 | haute | `\[ x\[n\] = \_{k=0}^{N-1} X\[k\]e^{i2kn/N} \]` | `\[ x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{i2\pi kn/N} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 475 | 474 | moyenne | `\[ \]` | `\[ x[n] \]` |
| DOCUMENT N — TRANSFORMÉES.md | 479 | 478 | moyenne | `\[ \]` | `\[ X[k] \]` |
| DOCUMENT N — TRANSFORMÉES.md | 497 | 496 | haute | `\[ f_k= \]` | `\[ f_k=\frac{kf_s}{N} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 501 | 500 | haute | `\[ f= \]` | `\[ \Delta f=\frac{f_s}{N} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 547 | 546 | haute | `\[ O(NN) \]` | `\[ O(N\log N) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 562 | 561 | haute | `\[ X\[k\] = \_{m=0}^{N/2-1} x\[2m\]e^{-i2k(2m)/N} âµ  âµ - \` | `\[ X[k]=\sum_{m=0}^{N/2-1}x[2m]e^{-i2\pi k(2m)/N} âµ  âµ + \sum_{m=0}^{N/2-1}x[2` |
| DOCUMENT N — TRANSFORMÉES.md | 574 | 573 | haute | `\[ W_N=e^{-i2/N} \]` | `\[ W_N=e^{-i2\pi/N} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 596 | 595 | haute | `\[ \_2N \]` | `\[ \log_2 N \]` |
| DOCUMENT N — TRANSFORMÉES.md | 606 | 605 | haute | `\[ O(N_2N) \]` | `\[ O(N\log_2 N) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 666 | 665 | haute | `\[ C_k = _k_ {n=0}^{N-1} x_n \]` | `\[ C_k=\alpha_k\sum_{n=0}^{N-1}x_n\cos\left(\frac{\pi}{N}\left(n+\frac{1}{2}\rig` |
| DOCUMENT N — TRANSFORMÉES.md | 676 | 676 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 712 | 711 | haute | `\[ F(s) = \_0^ f(t)e^{-st},dt \]` | `\[ F(s)=\int_0^{\infty}f(t)e^{-st}\,dt \]` |
| DOCUMENT N — TRANSFORMÉES.md | 716 | 715 | haute | `\[ s=+i \]` | `\[ s=\sigma+i\omega \]` |
| DOCUMENT N — TRANSFORMÉES.md | 726 | 725 | haute | `\[ {y’} = sY(s)-y(0) \]` | `\[ \mathcal{L}\{y'\}=sY(s)-y(0) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 732 | 732 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 736 | 736 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 744 | 743 | haute | `\[ {af+bg} = aF+bG \]` | `\[ \mathcal{L}\{af+bg\}=aF+bG \]` |
| DOCUMENT N — TRANSFORMÉES.md | 748 | 747 | haute | `\[ {f’} = sF(s)-f(0) \]` | `\[ \mathcal{L}\{f'\}=sF(s)-f(0) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 752 | 751 | haute | `\[ {f’‘} = s^2F(s)-sf(0)-f’(0) \]` | `\[ \mathcal{L}\{f''\}=s^{2}F(s)-sf(0)-f'(0) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 756 | 755 | haute | `\[ {f\*g} = F(s)G(s) \]` | `\[ \mathcal{L}\{f\ast g\}=F(s)G(s) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 768 | 768 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 776 | 775 | haute | `\[ H(s)= \]` | `\[ H(s)=\frac{N(s)}{D(s)} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 805 | 804 | haute | `\[ n \]` | `\[ n\geq 0 \]` |
| DOCUMENT N — TRANSFORMÉES.md | 845 | 844 | haute | `\[ z=e^{i} \]` | `\[ z=e^{i\omega} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 895 | 894 | haute | `\[ X(,) = x(t)w(t-)e^{-it},dt \]` | `\[ X(\tau,\omega)=\int x(t)w(t-\tau)e^{-i\omega t}\,dt \]` |
| DOCUMENT N — TRANSFORMÉES.md | 901 | 900 | haute | `\[ \|X(,)\|^2 \]` | `\[ \|X(\tau,\omega)\|^{2} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 942 | 941 | haute | `\[ (t) \]` | `\[ \psi(t) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 946 | 945 | haute | `\[ \_{a,b}(t) = ( ) \]` | `\[ \psi_{a,b}(t)=\frac{1}{\sqrt{a}}\psi\left(\frac{t-b}{a}\right) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 952 | 951 | haute | `\[ W(a,b) = x(t) dt \]` | `\[ W(a,b)=\int x(t)\psi_{a,b}(t)\,dt \]` |
| DOCUMENT N — TRANSFORMÉES.md | 964 | 964 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 966 | 966 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 1058 | 1057 | haute | `\[ x(t)=A(2f_0t) \]` | `\[ x(t)=A\sin(2\pi f_0t) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1066 | 1065 | moyenne | `\[ x(t)= âµ  âµ \]` | `\[ x(t)=\sin(2\pi f_1t)+\sin(2\pi f_2t) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1085 | 1085 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 1153 | 1150 | haute | `\[ xT(x) \]` | `\[ x\to T(x) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1157 | 1154 | moyenne | `\[ x(x) \]` | `\[ x\to \phi(x) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1161 | 1158 | moyenne | `\[ x \]` | `\[ x\to \tilde{x} \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1165 | 1162 | haute | `\[ xz \]` | `\[ x\to z \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1169 | 1166 | moyenne | `\[ x \]` | `\[ x\to X \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1190 | 1190 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 1226 | 1226 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 1258 | 1258 | inconnue | `\[ \]` | `—` |
| DOCUMENT N — TRANSFORMÉES.md | 1274 | 1271 | haute | `\[ u(x) \_{k=0}^{N} a_k_k(x) \]` | `\[ u(x)\approx\sum_{k=0}^{N}a_k\phi_k(x) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1278 | 1275 | haute | `\[ \_k(x) \]` | `\[ \phi_k(x) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1295 | 1292 | haute | `\[ u(x,t) U(k,t) \]` | `\[ u(x,t)\to U(k,t) \]` |
| DOCUMENT N — TRANSFORMÉES.md | 1301 | 1298 | haute | `\[ { } = -k^2U(k,t) \]` | `\[ \mathcal{F}\left\{\frac{\partial^{2}u}{\partial x^{2}}\right\}=-k^{2}U(k,t) \` |
