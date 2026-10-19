# Rapport d'application — docs/restauration/propositions/domaine-J-lot5b.patch.json

**Date :** 2026-10-19 — **Mode :** écriture

Entrées du correctif : 186 — appliquées : 133

| Fichier | L. avant | L. après | Confiance | Ancien | Nouveau |
|---|---:|---:|---|---|---|
| Domaine J — Optimisation.md | 1026 | 1026 | haute | `\[ \]` | `\[ L(\theta)+\lambda R(\theta) \]` |
| Domaine J — Optimisation.md | 1032 | 1032 | haute | `\[ R()=\|\|\_2^2 \]` | `\[ R(\theta)=\\|\theta\\|_{2}^{2} \]` |
| Domaine J — Optimisation.md | 1036 | 1036 | haute | `\[ R()=\|\|\_1 \]` | `\[ R(\theta)=\\|\theta\\|_{1} \]` |
| Domaine J — Optimisation.md | 1046 | 1046 | haute | `\[ L_{} \]` | `\[ L_{\text{train}} \]` |
| Domaine J — Optimisation.md | 1050 | 1050 | haute | `\[ L_{} \]` | `\[ L_{\text{test}} \]` |
| Domaine J — Optimisation.md | 1054 | 1054 | haute | `\[ L_{} \]` | `\[ L_{\text{train}} \]` |
| Domaine J — Optimisation.md | 1058 | 1058 | haute | `\[ L_{} \]` | `\[ L_{\text{test}} \]` |
| Domaine J — Optimisation.md | 1072 | 1072 | haute | `\[ L() \]` | `\[ L(\theta) \]` |
| Domaine J — Optimisation.md | 1092 | 1092 | haute | `\[ g_t = f(x_t) âµ  âµ - \_t \]` | `\[ g_t=\nabla f(x_t) âµ  âµ + \xi_t \]` |
| Domaine J — Optimisation.md | 1116 | 1116 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1120 | 1120 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1146 | 1146 | haute | `\[ x N(x) x’ N(x’) \]` | `\[ x\to N(x)\to x'\to N(x') \]` |
| Domaine J — Optimisation.md | 1154 | 1154 | haute | `\[ x_0^{(1)}, x_0^{(2)}, , x_0^{(k)} \]` | `\[ x_0^{(1)},x_0^{(2)},\ldots,x_0^{(k)} \]` |
| Domaine J — Optimisation.md | 1168 | 1168 | moyenne | `\[ P = ( - ) \]` | `\[ P=\exp\left(-\frac{\Delta E}{T}\right) \]` |
| Domaine J — Optimisation.md | 1183 | 1183 | haute | `\[ P={x_1,x_2,,x_n} \]` | `\[ P=\{x_1,x_2,\ldots,x_n\} \]` |
| Domaine J — Optimisation.md | 1194 | 1194 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1202 | 1202 | moyenne | `\[ (x) \]` | `\[ F(x) \]` |
| Domaine J — Optimisation.md | 1265 | 1265 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1299 | 1299 | haute | `\[ f_1(x),f_2(x),,f_k(x) \]` | `\[ f_1(x),f_2(x),\ldots,f_k(x) \]` |
| Domaine J — Optimisation.md | 1303 | 1303 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1307 | 1307 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1311 | 1311 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1334 | 1334 | haute | `\[ F(x) = \_1 f_1(x) âµ  âµ - \_2 f_2(x) âµ  âµ - \_k f_k(x)` | `\[ F(x)=\lambda_1f_1(x) âµ  âµ + \lambda_2f_2(x) âµ  âµ + \lambda_kf_k(x) \]` |
| Domaine J — Optimisation.md | 1342 | 1342 | haute | `\[ \_i \]` | `\[ \lambda_i \]` |
| Domaine J — Optimisation.md | 1352 | 1352 | haute | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` |
| Domaine J — Optimisation.md | 1356 | 1356 | moyenne | `\[ _x_ {} f(x,) \]` | `\[ \min_x\max_{\delta\in\Delta}f(x,\delta) \]` |
| Domaine J — Optimisation.md | 1376 | 1376 | haute | `\[ \]` | `\[ \min_x\mathbb{E}[f(x,\xi)] \]` |
| Domaine J — Optimisation.md | 1384 | 1384 | haute | `\[ R() = 1n _{i=1}^{n} L(f_(x_i),y_i) \]` | `\[ R(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i) \]` |
| Domaine J — Optimisation.md | 1388 | 1388 | haute | `\[ \]` | `\[ \min_\theta R(\theta) \]` |
| Domaine J — Optimisation.md | 1396 | 1396 | haute | `\[ \|\|C \]` | `\[ \\|\theta\\|\leq C \]` |
| Domaine J — Optimisation.md | 1400 | 1400 | moyenne | `\[ \|\| \]` | `\[ \\|\theta\\| \]` |
| Domaine J — Optimisation.md | 1416 | 1416 | haute | `\[ _ 1n _i L(y_i,f_(x_i)) \]` | `\[ \min_\theta\frac{1}{n}\sum_i L(y_i,f_\theta(x_i)) \]` |
| Domaine J — Optimisation.md | 1424 | 1424 | moyenne | `\[ \]` | `\[ \theta \]` |
| Domaine J — Optimisation.md | 1428 | 1428 | haute | `\[ y=f_(x) \]` | `\[ \hat{y}=f_\theta(x) \]` |
| Domaine J — Optimisation.md | 1432 | 1432 | haute | `\[ ^\* = _L(f_(x),y) \]` | `\[ \theta^{*}=\arg\min_\theta L(f_\theta(x),y) \]` |
| Domaine J — Optimisation.md | 1436 | 1436 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1470 | 1470 | haute | `\[ = H_1H_2H_k \]` | `\[ \mathcal{H}=H_1\times H_2\times\cdots\times H_k \]` |
| Domaine J — Optimisation.md | 1486 | 1486 | moyenne | `\[ h \]` | `\[ L(h) \]` |
| Domaine J — Optimisation.md | 1496 | 1496 | moyenne | `\[ J() = \]` | `\[ J(\theta)=\mathbb{E}\left[\sum_{t}\gamma^{t}r_t\right] \]` |
| Domaine J — Optimisation.md | 1500 | 1500 | haute | `\[ \]` | `\[ \max_\theta J(\theta) \]` |
| Domaine J — Optimisation.md | 1508 | 1508 | haute | `\[ (t) \]` | `\[ \tau(t) \]` |
| Domaine J — Optimisation.md | 1512 | 1512 | inconnue | `\[ J() = J_{} âµ  âµ - J_{} âµ - J_{} âµ - J_{} \]` | `—` |
| Domaine J — Optimisation.md | 1528 | 1528 | moyenne | `\[ \]` | `\[ \min_\tau J(\tau) \]` |
| Domaine J — Optimisation.md | 1534 | 1534 | inconnue | `\[ ( âµ  âµ - ) \]` | `—` |
| Domaine J — Optimisation.md | 1552 | 1552 | haute | `\[ T_1,T_2,,T_n \]` | `\[ T_1,T_2,\ldots,T_n \]` |
| Domaine J — Optimisation.md | 1556 | 1556 | haute | `\[ M_1,M_2,,M_k \]` | `\[ M_1,M_2,\ldots,M_k \]` |
| Domaine J — Optimisation.md | 1560 | 1560 | haute | `\[ C_{} \]` | `\[ C_{\max} \]` |
| Domaine J — Optimisation.md | 1580 | 1580 | haute | `\[ A_1,,A_n \]` | `\[ A_1,\ldots,A_n \]` |
| Domaine J — Optimisation.md | 1588 | 1588 | haute | `\[ \_i x_iR \]` | `\[ \sum_i x_i\leq R \]` |
| Domaine J — Optimisation.md | 1614 | 1614 | haute | `\[ \_P (P) \]` | `\[ \min_P C(P) \]` |
| Domaine J — Optimisation.md | 1618 | 1618 | haute | `\[ \_x \_i U_i(x_i) \]` | `\[ \max_x\sum_i U_i(x_i) \]` |
| Domaine J — Optimisation.md | 1622 | 1622 | haute | `\[ \_i x_iC \]` | `\[ \sum_i x_i\leq C \]` |
| Domaine J — Optimisation.md | 1630 | 1630 | haute | `\[ w=(w_1,,w_n) \]` | `\[ w=(w_1,\ldots,w_n) \]` |
| Domaine J — Optimisation.md | 1634 | 1634 | moyenne | `\[ âµ  âµ - \]` | `\[ \max_w\left(w^{T}\mu âµ  âµ - \lambda w^{T}\Sigma w\right) \]` |
| Domaine J — Optimisation.md | 1640 | 1640 | haute | `\[ \_i w_i=1 \]` | `\[ \sum_i w_i=1 \]` |
| Domaine J — Optimisation.md | 1644 | 1644 | haute | `\[ w_i \]` | `\[ w_i\geq 0 \]` |
| Domaine J — Optimisation.md | 1664 | 1664 | haute | `\[ ^\* = _ \|R()-I\|^2 \]` | `\[ \theta^{*}=\arg\min_\theta\\|R(\theta)-I\\|^{2} \]` |
| Domaine J — Optimisation.md | 1676 | 1676 | haute | `\[ x^\* = \_x E(x) \]` | `\[ x^{*}=\arg\min_x E(x) \]` |
| Domaine J — Optimisation.md | 1702 | 1702 | haute | `\[ _ \_i L_i() \]` | `\[ \min_\theta\sum_i L_i(\theta) \]` |
| Domaine J — Optimisation.md | 1708 | 1708 | haute | `\[ y=Ax+ \]` | `\[ y=Ax+\epsilon \]` |
| Domaine J — Optimisation.md | 1712 | 1712 | haute | `\[ x^\* = \_x \|Ax-y\|^2 âµ  âµ - R(x) \]` | `\[ x^{*}=\arg\min_x\\|Ax-y\\|^{2} âµ  âµ + \lambda R(x) \]` |
| Domaine J — Optimisation.md | 1742 | 1742 | haute | `\[ \]` | `\[ \delta \]` |
| Domaine J — Optimisation.md | 1746 | 1746 | haute | `\[ \_{} L(x+,y) \]` | `\[ \max_{\\|\delta\\|\leq\epsilon}L(x+\delta,y) \]` |
| Domaine J — Optimisation.md | 1750 | 1750 | haute | `\[ \|\| \]` | `\[ \\|\delta\\|\leq\epsilon \]` |
| Domaine J — Optimisation.md | 1760 | 1760 | haute | `\[ _x_ {i=1}^{N} f_i(x) \]` | `\[ \min_x\sum_{i=1}^{N}f_i(x) \]` |
| Domaine J — Optimisation.md | 1781 | 1781 | haute | `\[ {k=1}^{K} p_k F_k() \]` | `\[ \min_\theta\sum_{k=1}^{K}p_kF_k(\theta) \]` |
| Domaine J — Optimisation.md | 1806 | 1806 | haute | `\[ x_1,x_2,x_3, \]` | `\[ x_1,x_2,x_3,\ldots \]` |
| Domaine J — Optimisation.md | 1824 | 1824 | moyenne | `\[ \]` | `\[ \min_x f(x) \]` |
| Domaine J — Optimisation.md | 1828 | 1828 | haute | `\[ T \]` | `\[ t\leq T \]` |
| Domaine J — Optimisation.md | 1832 | 1832 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1844 | 1844 | moyenne | `\[ x \]` | `\[ \hat{x} \]` |
| Domaine J — Optimisation.md | 1848 | 1848 | moyenne | `\[ f(x) f(x^\*) \]` | `\[ f(\hat{x})\leq\alpha f(x^{*}) \]` |
| Domaine J — Optimisation.md | 1860 | 1860 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1878 | 1878 | haute | `\[ \_1,\_2, \]` | `\[ S_1,S_2,\ldots \]` |
| Domaine J — Optimisation.md | 1884 | 1884 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 1892 | 1892 | haute | `\[ x_i{0,1} \]` | `\[ x_i\in\{0,1\} \]` |
| Domaine J — Optimisation.md | 1896 | 1896 | moyenne | `\[ 0x_i \]` | `\[ 0\leq x_i\leq 1 \]` |
| Domaine J — Optimisation.md | 1975 | 1975 | haute | `\[ 01 \]` | `\[ [0,1] \]` |
| Domaine J — Optimisation.md | 1979 | 1979 | haute | `\[ 010^6 \]` | `\[ [0,10^{6}] \]` |
| Domaine J — Optimisation.md | 2006 | 2006 | haute | `\[ x_tx^\* \]` | `\[ x_t\to x^{*} \]` |
| Domaine J — Optimisation.md | 2010 | 2010 | haute | `\[ f(x_t)f(x^\*) \]` | `\[ f(x_t)\to f(x^{*}) \]` |
| Domaine J — Optimisation.md | 2039 | 2039 | inconnue | `\[ âµ  âµ - \]` | `—` |
| Domaine J — Optimisation.md | 2051 | 2051 | haute | `\[ f \]` | `\[ \nabla f \]` |
| Domaine J — Optimisation.md | 2064 | 2064 | haute | `\[ ^2f \]` | `\[ \nabla^{2}f \]` |
| Domaine J — Optimisation.md | 2135 | 2135 | haute | `\[ f(x)=0 \]` | `\[ \nabla f(x)=0 \]` |
| Domaine J — Optimisation.md | 2162 | 2162 | haute | `\[ L_{} \]` | `\[ L_{\text{train}} \]` |
| Domaine J — Optimisation.md | 2166 | 2166 | haute | `\[ L_{} \]` | `\[ L_{\text{test}} \]` |
| Domaine J — Optimisation.md | 2174 | 2174 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2237 | 2237 | haute | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` |
| Domaine J — Optimisation.md | 2243 | 2243 | haute | `\[ \_x c^Tx \]` | `\[ \min_x c^{T}x \]` |
| Domaine J — Optimisation.md | 2247 | 2247 | haute | `\[ Axb \]` | `\[ Ax\leq b \]` |
| Domaine J — Optimisation.md | 2253 | 2253 | haute | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` |
| Domaine J — Optimisation.md | 2263 | 2263 | haute | `\[ \_x f(x)+R(x) \]` | `\[ \min_x f(x)+R(x) \]` |
| Domaine J — Optimisation.md | 2269 | 2269 | haute | `\[ x_{t+1}=x_t-f(x_t) \]` | `\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]` |
| Domaine J — Optimisation.md | 2275 | 2275 | haute | `\[ x_{t+1} = x_t-H^{-1}f \]` | `\[ x_{t+1}=x_t-H^{-1}\nabla f \]` |
| Domaine J — Optimisation.md | 2281 | 2281 | haute | `\[ \_x \[f(x,)\] \]` | `\[ \min_x\mathbb{E}[f(x,\xi)] \]` |
| Domaine J — Optimisation.md | 2287 | 2287 | haute | `\[ \_J() \]` | `\[ \max_\theta J(\theta) \]` |
| Domaine J — Optimisation.md | 2339 | 2339 | haute | `\[ f \]` | `\[ \nabla f \]` |
| Domaine J — Optimisation.md | 2341 | 2341 | haute | `\[ ^2f \]` | `\[ \nabla^{2}f \]` |
| Domaine J — Optimisation.md | 2345 | 2345 | haute | `\[ (x,) \]` | `\[ \mathcal{L}(x,\lambda) \]` |
| Domaine J — Optimisation.md | 2347 | 2347 | haute | `\[ Axb \]` | `\[ Ax\leq b \]` |
| Domaine J — Optimisation.md | 2349 | 2349 | haute | `\[ x \]` | `\[ x\geq 0 \]` |
| Domaine J — Optimisation.md | 2351 | 2351 | haute | `\[ x{0,1} \]` | `\[ x\in\{0,1\} \]` |
| Domaine J — Optimisation.md | 2353 | 2353 | haute | `\[ \|\|\_1 \]` | `\[ \\|x\\|_1 \]` |
| Domaine J — Optimisation.md | 2355 | 2355 | haute | `\[ \|\|\_2 \]` | `\[ \\|x\\|_2 \]` |
| Domaine J — Optimisation.md | 2357 | 2357 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2359 | 2359 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2361 | 2361 | haute | `\[ \[f(x,)\] \]` | `\[ \mathbb{E}[f(x,\xi)] \]` |
| Domaine J — Optimisation.md | 2363 | 2363 | haute | `\[ (f_1,,f_k) \]` | `\[ (f_1,\ldots,f_k) \]` |
| Domaine J — Optimisation.md | 2379 | 2379 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2383 | 2383 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2389 | 2389 | haute | `\[ \_x \[f(x,)\] \]` | `\[ \min_x\mathbb{E}[f(x,\xi)] \]` |
| Domaine J — Optimisation.md | 2397 | 2397 | haute | `\[ ^\* = _ L() \]` | `\[ \theta^{*}=\arg\min_\theta L(\theta) \]` |
| Domaine J — Optimisation.md | 2401 | 2401 | moyenne | `\[ ^\* = _ () \]` | `\[ \theta^{*}=\arg\max_\theta \mathcal{L}(\theta) \]` |
| Domaine J — Optimisation.md | 2409 | 2409 | haute | `\[ x \]` | `\[ x\in\mathcal{X} \]` |
| Domaine J — Optimisation.md | 2444 | 2444 | haute | `\[ H(x)p=-f(x) \]` | `\[ H(x)p=-\nabla f(x) \]` |
| Domaine J — Optimisation.md | 2573 | 2573 | inconnue | `\[ âµ  âµ - \]` | `—` |
| Domaine J — Optimisation.md | 2579 | 2579 | inconnue | `\[ âµ  âµ - \]` | `—` |
| Domaine J — Optimisation.md | 2595 | 2595 | haute | `\[ f(x^\*+) \]` | `\[ f(x^{*}+\delta) \]` |
| Domaine J — Optimisation.md | 2607 | 2607 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2609 | 2609 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2611 | 2611 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2613 | 2613 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2649 | 2649 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2688 | 2688 | inconnue | `\[ ( âµ  âµ - ) \]` | `—` |
| Domaine J — Optimisation.md | 2722 | 2722 | haute | `\[ a_1,a_2,,a_T \]` | `\[ a_1,a_2,\ldots,a_T \]` |
| Domaine J — Optimisation.md | 2732 | 2732 | inconnue | `\[ âµ  âµ - \]` | `—` |
| Domaine J — Optimisation.md | 2746 | 2746 | haute | `\[ J() = Q âµ  âµ - C âµ - T âµ - E \]` | `\[ J(a)=Q(a) âµ  âµ - C(a) âµ - T(a) âµ - E(a) \]` |
| Domaine J — Optimisation.md | 2765 | 2765 | haute | `\[ A_1,A_2,,A_n \]` | `\[ A_1,A_2,\ldots,A_n \]` |
| Domaine J — Optimisation.md | 2771 | 2771 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2791 | 2791 | inconnue | `\[ J = âµ  âµ - \]` | `—` |
| Domaine J — Optimisation.md | 2811 | 2811 | haute | `\[ h^\* = _h L_{}(h) \]` | `\[ h^{*}=\arg\min_h L_{\text{val}}(h) \]` |
| Domaine J — Optimisation.md | 2817 | 2817 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2823 | 2823 | haute | `\[ P=(a_1,a_2,,a_n) \]` | `\[ P=(a_1,a_2,\ldots,a_n) \]` |
| Domaine J — Optimisation.md | 2827 | 2827 | moyenne | `\[ J(P) = (P) \]` | `\[ J(P)=\text{coût}(P) \]` |
| Domaine J — Optimisation.md | 2831 | 2831 | haute | `\[ P^\* = \_P J(P) \]` | `\[ P^{*}=\arg\min_P J(P) \]` |
| Domaine J — Optimisation.md | 2839 | 2839 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2847 | 2847 | inconnue | `\[ âµ  âµ - \]` | `—` |
| Domaine J — Optimisation.md | 2857 | 2857 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2859 | 2859 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2861 | 2861 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2863 | 2863 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2865 | 2865 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 2879 | 2879 | haute | `\[ x_0,x_1,x_2, \]` | `\[ x_0,x_1,x_2,\ldots \]` |
| Domaine J — Optimisation.md | 2928 | 2928 | haute | `\[ Axb \]` | `\[ Ax\leq b \]` |
| Domaine J — Optimisation.md | 2994 | 2994 | haute | `\[ J(a) = Q(a) âµ  âµ - C(a) âµ - T(a) \]` | `\[ J(a)=Q(a) âµ  âµ - C(a) âµ - T(a) \]` |
| Domaine J — Optimisation.md | 3042 | 3042 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3054 | 3054 | haute | `\[ \_{x,y}x<sup>2+y</sup>2 \]` | `\[ \min_{x,y}x^{2}+y^{2} \]` |
| Domaine J — Optimisation.md | 3091 | 3091 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3372 | 3372 | moyenne | `\[ \]` | `\[ \min_{x\in\mathcal{X}}f(x) \]` |
| Domaine J — Optimisation.md | 3376 | 3376 | moyenne | `\[ \]` | `\[ \min_\theta L(\theta) \]` |
| Domaine J — Optimisation.md | 3380 | 3380 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3386 | 3386 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3388 | 3388 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3390 | 3390 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3392 | 3392 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3394 | 3394 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3396 | 3396 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3398 | 3398 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3400 | 3400 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3402 | 3402 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3404 | 3404 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3414 | 3414 | moyenne | `\[ \]` | `\[ \nabla f \]` |
| Domaine J — Optimisation.md | 3418 | 3418 | moyenne | `\[ \]` | `\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]` |
| Domaine J — Optimisation.md | 3422 | 3422 | moyenne | `\[ \]` | `\[ \min_\theta L(\theta) \]` |
| Domaine J — Optimisation.md | 3432 | 3432 | moyenne | `\[ \]` | `\[ \text{l'objectif} \]` |
| Domaine J — Optimisation.md | 3436 | 3436 | moyenne | `\[ \]` | `\[ \text{les variables} \]` |
| Domaine J — Optimisation.md | 3440 | 3440 | moyenne | `\[ \]` | `\[ \text{les contraintes} \]` |
| Domaine J — Optimisation.md | 3444 | 3444 | moyenne | `\[ \]` | `\[ \text{la fonction objectif} \]` |
| Domaine J — Optimisation.md | 3448 | 3448 | moyenne | `\[ \]` | `\[ \nabla f \]` |
| Domaine J — Optimisation.md | 3452 | 3452 | moyenne | `\[ \]` | `\[ \text{convexité} \]` |
| Domaine J — Optimisation.md | 3456 | 3456 | moyenne | `\[ \]` | `\[ x\in\{0,1\} \]` |
| Domaine J — Optimisation.md | 3460 | 3460 | moyenne | `\[ \]` | `\[ \text{optimisation bayésienne} \]` |
| Domaine J — Optimisation.md | 3464 | 3464 | moyenne | `\[ \]` | `\[ (f_1,\ldots,f_k) \]` |
| Domaine J — Optimisation.md | 3468 | 3468 | moyenne | `\[ \]` | `\[ x^{*}\ \text{ou}\ \hat{x} \]` |
| Domaine J — Optimisation.md | 3476 | 3476 | moyenne | `\[ \]` | `\[ \text{un problème réel} \]` |
| Domaine J — Optimisation.md | 3480 | 3480 | moyenne | `\[ \]` | `\[ \text{un modèle mathématique} \]` |
| Domaine J — Optimisation.md | 3484 | 3484 | moyenne | `\[ \]` | `\[ \text{une méthode adaptée} \]` |
| Domaine J — Optimisation.md | 3488 | 3488 | moyenne | `\[ \]` | `\[ \text{une solution validée} \]` |
| Domaine J — Optimisation.md | 3506 | 3506 | moyenne | `\[ \]` | `\[ \min_\theta L(\theta) \]` |
| Domaine J — Optimisation.md | 3510 | 3510 | moyenne | `\[ \]` | `\[ \min_\tau J(\tau) \]` |
| Domaine J — Optimisation.md | 3514 | 3514 | moyenne | `\[ \]` | `\[ \min\sum_{i,j}c_{ij}x_{ij} \]` |
| Domaine J — Optimisation.md | 3518 | 3518 | moyenne | `\[ \]` | `\[ \min_P C(P) \]` |
| Domaine J — Optimisation.md | 3522 | 3522 | moyenne | `\[ \]` | `\[ \max_\theta J(\theta) \]` |
| Domaine J — Optimisation.md | 3526 | 3526 | inconnue | `\[ \]` | `—` |
| Domaine J — Optimisation.md | 3534 | 3534 | inconnue | `\[ \]` | `—` |
