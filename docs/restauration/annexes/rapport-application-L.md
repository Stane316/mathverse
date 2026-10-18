# Rapport d'application — docs/restauration/propositions/domaine-L.patch.json

**Date :** 2026-10-18 — **Mode :** écriture

Entrées du correctif : 135 — appliquées : 91

| Fichier | L. avant | L. après | Confiance | Ancien | Nouveau |
|---|---:|---:|---|---|---|
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 13 | 13 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 17 | 17 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 55 | 55 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 61 | 61 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 115 | 115 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 136 | 136 | moyenne | `\[ f(x),Ax=b,f,\_a^b f(x),dx,=f(t,y) \]` | `\[ f(x),\quad Ax=b,\quad \nabla f,\quad \int_a^b f(x)\,dx,\quad y'=f(t,y) \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 146 | 146 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 154 | 154 | moyenne | `\[ x. \]` | `\[ \hat{x}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 158 | 158 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 166 | 166 | haute | `Si (x) est la valeur exacte et () la valeur calculée :` | `Si (x) est la valeur exacte et (\hat{x}) la valeur calculée :` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 168 | 168 | haute | `\[ E_a=\|x-\|. \]` | `\[ E_a=\|x-\hat{x}\|. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 176 | 176 | haute | `\[ =9.99. \]` | `\[ \hat{x}=9.99. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 186 | 186 | haute | `\[ E_r=. \]` | `\[ E_r=\frac{\|x-\hat{x}\|}{\|x\|}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 192 | 192 | haute | `\[ E_r(%)= 100. \]` | `\[ E_r(\%)=\frac{\|x-\hat{x}\|}{\|x\|}\times 100. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 202 | 202 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 222 | 222 | haute | `\[ e^x = \_{k=0}<sup>{}\\frac{x</sup>k}{k!} \]` | `\[ e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 226 | 226 | haute | `\[ e^x \_{k=0}<sup>{N}\\frac{x</sup>k}{k!}. \]` | `\[ e^x \approx \sum_{k=0}^{N}\frac{x^k}{k!}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 242 | 242 | moyenne | `\[ x=m^e. \]` | `\[ x=m\,2^e. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 255 | 255 | haute | `\[ \]` | `\[ \mathbb{R} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 261 | 261 | haute | `\[ \]` | `\[ \mathbb{R} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 271 | 271 | moyenne | `\[ \_{}^{-p} \]` | `\[ \varepsilon_{\text{mach}} \approx \beta^{-p} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 297 | 297 | moyenne | `\[ \]` | `\[ \text{annulation catastrophique} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 309 | 309 | moyenne | `\[ ((a+b)+c) \]` | `\[ \mathrm{fl}((a+b)+c) \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 313 | 313 | moyenne | `\[ (a+(b+c)). \]` | `\[ \mathrm{fl}(a+(b+c)). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 343 | 343 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 351 | 351 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 365 | 365 | haute | `\[ x_0,x_1,x_2, \]` | `\[ x_0,x_1,x_2,\ldots \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 369 | 369 | haute | `\[ x_kx^. \]` | `\[ x_k\to x^*. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 382 | 382 | haute | `\[ e_k=\|x_k-x^\| \]` | `\[ e_k=\|x_k-x^*\| \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 386 | 386 | haute | `\[ e_{k+1}C e_k^p, \]` | `\[ e_{k+1}\leq C e_k^p, \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 408 | 408 | haute | `\[ \|x_{k+1}-x_k\|< \]` | `\[ \|x_{k+1}-x_k\|<\varepsilon \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 412 | 412 | haute | `\[ \|F(x_k)\|< \]` | `\[ \|F(x_k)\|<\varepsilon \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 416 | 416 | moyenne | `\[ {(1,\|x_k\|)} <. \]` | `\[ \|x_{k+1}-x_k\|<\varepsilon\max(1,\|x_k\|). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 435 | 435 | moyenne | `\[ x^x. \]` | `\[ x^*. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 445 | 445 | correction d'echappement | `\[ \[a,b\]. \]` | `\[ [a,b]. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 449 | 449 | haute | `\[ m=. \]` | `\[ m=\frac{a+b}{2}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 465 | 465 | moyenne | `\[ \]` | `\[ f'(x_n) \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 485 | 485 | moyenne | `\[ . \]` | `\[ \text{convergence quadratique}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 501 | 501 | haute | `\[ f’(x_n) {x_n-x_{n-1}}. \]` | `\[ f'(x_n)\approx\frac{f(x_n)-f(x_{n-1})}{x_n-x_{n-1}}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 631 | 631 | haute | `\[ x_0,x_1,x_2, \]` | `\[ x_0,x_1,x_2,\ldots \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 669 | 669 | haute | `\[ \_x 12x<sup>TAx-b</sup>Tx. \]` | `\[ \min_x \frac{1}{2}x^TAx-b^Tx. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 691 | 691 | haute | `\[ (x_0,y_0),,(x_n,y_n). \]` | `\[ (x_0,y_0),\ldots,(x_n,y_n). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 701 | 701 | haute | `\[ p(x)= \_{i=0}^{n} y_iL_i(x) \]` | `\[ p(x)=\sum_{i=0}^{n} y_iL_i(x) \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 705 | 705 | haute | `\[ L_i(x)= \_{ji} . \]` | `\[ L_i(x)=\prod_{j\neq i}\frac{x-x_j}{x_i-x_j}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 711 | 711 | moyenne | `\[ p(x) = a_0+ a_1(x-x_0) âµ  âµ - a_2(x-x_0)(x-x_1) + \]` | `\[ p(x) = a_0+ a_1(x-x_0)+ a_2(x-x_0)(x-x_1)+\ldots+a_n(x-x_0)\ldots(x-x_{n-1}) ` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 723 | 723 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 748 | 746 | haute | `\[ p(x)f(x) \]` | `\[ p(x)\approx f(x) \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 756 | 754 | haute | `\[ \_i (y_i-f(x_i))^2. \]` | `\[ \sum_i (y_i-f(x_i))^2. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 760 | 758 | haute | `\[ \_x\|Ax-b\|\_2^2. \]` | `\[ \min_x\\|Ax-b\\|_2^2. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 776 | 774 | moyenne | `\[ \_x \|Ax-b\|\_2^2+ \|x\|\_2^2. \]` | `\[ \min_x \\|Ax-b\\|_2^2+\lambda\\|x\\|_2^2. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 786 | 784 | haute | `\[ I= \_a^b f(x),dx. \]` | `\[ I=\int_a^b f(x)\,dx. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 794 | 792 | haute | `\[ \_a^b f(x),dx \_i f(x_i)x. \]` | `\[ \int_a^b f(x)\,dx \approx \sum_i f(x_i)\,\Delta x. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 804 | 802 | haute | `\[ \_a^b f(x),dx \[f(a)+f(b)\]. \]` | `\[ \int_a^b f(x)\,dx \approx \frac{b-a}{2}\left[f(a)+f(b)\right]. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 808 | 808 | inconnue | `\[ I h . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 814 | 812 | moyenne | `\[ \_a^b f(x),dx . \]` | `\[ \int_a^b f(x)\,dx \approx \frac{b-a}{6}\left[f(a)+4f\left(\frac{a+b}{2}\right` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 847 | 845 | haute | `\[ f’(x) . \]` | `\[ f'(x)\approx\frac{f(x+h)-f(x)}{h}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 851 | 849 | haute | `\[ f’(x) . \]` | `\[ f'(x)\approx\frac{f(x)-f(x-h)}{h}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 855 | 853 | haute | `\[ f’(x) . \]` | `\[ f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 875 | 873 | moyenne | `\[ h. \]` | `\[ h\to 0. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 883 | 883 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 887 | 887 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 893 | 893 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 901 | 899 | haute | `\[ =f(t,y). \]` | `\[ y'=f(t,y). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 936 | 934 | moyenne | `\[ \]` | `\[ \text{problèmes raides} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 993 | 991 | correction d'echappement | `\[ I=E\[f(X)\], \]` | `\[ I=E[f(X)], \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 997 | 995 | haute | `\[ I_N = 1N \_{i=1}^{N}f(X_i). \]` | `\[ I_N = \frac{1}{N}\sum_{i=1}^{N}f(X_i). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1001 | 999 | haute | `\[ I_NI. \]` | `\[ I_N\to I. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1007 | 1005 | haute | `\[ O(). \]` | `\[ O\left(\frac{1}{\sqrt{N}}\right). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1017 | 1017 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1044 | 1042 | haute | `\[ Av=v. \]` | `\[ Av=\lambda v. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1061 | 1059 | moyenne | `\[ x_{k+1}= . \]` | `\[ x_{k+1}=\frac{Ax_k}{\\|Ax_k\\|}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1071 | 1069 | haute | `\[ \_x f(x). \]` | `\[ \min_x f(x). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1089 | 1087 | haute | `\[ f(x), \]` | `\[ \min f(x), \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1093 | 1091 | haute | `\[ x_{k+1} = x_k- H_f(x_k)^{-1}f(x_k). \]` | `\[ x_{k+1} = x_k- H_f(x_k)^{-1}\nabla f(x_k). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1101 | 1099 | haute | `\[ H=-f \]` | `\[ H\delta=-\nabla f \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1105 | 1103 | haute | `\[ x_{k+1}=x_k+. \]` | `\[ x_{k+1}=x_k+\delta. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1142 | 1140 | haute | `\[ = . \]` | `\[ \frac{dy}{dx}=\frac{dy}{dz}\frac{dz}{dx}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1148 | 1148 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1154 | 1152 | haute | `\[ x_{k+1}=(x_k). \]` | `\[ x_{k+1}=\varphi(x_k). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1158 | 1156 | haute | `\[ x<sup>\=(x</sup>). \]` | `\[ x^*=\varphi(x^*). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1164 | 1162 | haute | `\[ x=(x) \]` | `\[ x=\varphi(x) \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1170 | 1168 | haute | `\[ \|’(x^)\|<1, \]` | `\[ \|\varphi'(x^*)\|<1, \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1193 | 1193 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1197 | 1197 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1203 | 1201 | moyenne | `\[ E_{} E_{} âµ  âµ - E_{} âµ - E_{} âµ - E_{} âµ - E_{}. \]` | `\[ E_{\text{total}}=E_{\text{modèle}}+E_{\text{données}}+E_{\text{arrondi}}+E_{\` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1271 | 1264 | haute | `\[ x_hx^, \]` | `\[ x_h\to x^*, \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1281 | 1281 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1285 | 1285 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1295 | 1288 | haute | `\[ x_110^{-10} \]` | `\[ x_1\sim 10^{-10} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1299 | 1292 | haute | `\[ x_210^{10}, \]` | `\[ x_2\sim 10^{10}, \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1326 | 1319 | haute | `\[ AR^{nn} \]` | `\[ A\in\mathbb{R}^{n\times n} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1336 | 1329 | moyenne | `\[ O((A)). \]` | `\[ O(\mathrm{nnz}(A)). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1364 | 1364 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1394 | 1387 | haute | `\[ \_L(). \]` | `\[ \min_{\theta}\mathcal{L}(\theta). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1398 | 1391 | haute | `\[ \_L. \]` | `\[ \nabla_\theta \mathcal{L}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1402 | 1395 | haute | `\[ \_{t+1} = \_t-L. \]` | `\[ \theta_{t+1}=\theta_t-\eta\nabla\mathcal{L}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1464 | 1457 | haute | `\[ =a. \]` | `\[ \frac{dv}{dt}=a. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1580 | 1573 | moyenne | `\[ KL \]` | `\[ K\times L \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1604 | 1604 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1697 | 1690 | moyenne | `\[ \]` | `\[ \text{exact} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1699 | 1692 | moyenne | `\[ \]` | `\[ \text{approché} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1701 | 1694 | moyenne | `\[ \]` | `\[ \text{numérique} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1770 | 1770 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1794 | 1787 | moyenne | `\[ T_{}<T_{}. \]` | `\[ T_{\text{calcul}}<T_{\text{budget}}. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1812 | 1812 | inconnue | `\[` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1820 | 1820 | inconnue | `\[` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1828 | 1828 | inconnue | `\[` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1836 | 1836 | inconnue | `\[` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1844 | 1844 | inconnue | `\[` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1852 | 1852 | inconnue | `\[` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1860 | 1860 | inconnue | `\[` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1870 | 1870 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1874 | 1874 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 1878 | 1878 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2065 | 2058 | haute | `\[ x,,\|x-\|. \]` | `\[ x,\ \hat{x},\ \|x-\hat{x}\|. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2106 | 2106 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2191 | 2191 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2201 | 2194 | moyenne | `\[ \]` | `\[ x=m\,b^e \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2205 | 2198 | moyenne | `\[ \]` | `\[ E_r=\frac{\|x-\hat{x}\|}{\|x\|} \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2221 | 2214 | haute | `\[ (x_i,y_i) f(x) \]` | `\[ (x_i,y_i)\to f(x) \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2225 | 2218 | haute | `\[ f(x),dx . \]` | `\[ \int_a^b f(x)\,dx. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2233 | 2226 | haute | `\[ =f(t,y) . \]` | `\[ y'=f(t,y). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2237 | 2230 | correction d'echappement | `\[ E\[f(X)\] . \]` | `\[ E[f(X)]. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2241 | 2234 | moyenne | `\[ \]` | `\[ r=Ax-b \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2282 | 2282 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2286 | 2279 | moyenne | `\[ \]` | `\[ \min_x f(x) \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2290 | 2283 | moyenne | `\[ . \]` | `\[ y'=f(t,y). \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2298 | 2291 | correction d'echappement | `\[ E\[X\] . \]` | `\[ E[X]. \]` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2302 | 2302 | inconnue | `\[ . \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2308 | 2308 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2312 | 2312 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2340 | 2340 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2344 | 2344 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2350 | 2350 | inconnue | `\[ \]` | `—` |
| DOCUMENT L — ANALYSE NUMÉRIQUE.md | 2354 | 2354 | inconnue | `\[ . \]` | `—` |
