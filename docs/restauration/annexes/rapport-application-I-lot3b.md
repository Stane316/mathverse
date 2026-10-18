# Rapport d'application — docs/restauration/propositions/domaine-I-lot3b.patch.json

**Date :** 2026-10-18 — **Mode :** écriture

Entrées du correctif : 159 — appliquées : 133

| Fichier | L. avant | L. après | Confiance | Ancien | Nouveau |
|---|---:|---:|---|---|---|
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 800 | 800 | haute | `\[ = \]` | `\[ \frac{dz}{dx}=\frac{dz}{du}\frac{du}{dx} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 812 | 812 | haute | `\[ x z a L \]` | `\[ x \to z \to a \to L \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 816 | 816 | haute | `\[ z=Wx+b \]` | `\[ a=\sigma(z) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 824 | 824 | moyenne | `\[ = \]` | `\[ \frac{\partial L}{\partial W}=\frac{\partial L}{\partial a}\cdot\frac{\partia` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 834 | 834 | haute | `\[ f(x^\*)=0 \]` | `\[ \nabla f(x^{*})=0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 851 | 851 | haute | `\[ f(x^\*)f(x) \]` | `\[ f(x^{*})\leq f(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 857 | 857 | haute | `\[ f(x^\*)f(x) \]` | `\[ f(x^{*})\geq f(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 895 | 895 | haute | `\[ H(x^\*) \]` | `\[ \nabla^{2}f(x^{*})\succ 0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 901 | 901 | haute | `\[ H(x^\*) \]` | `\[ \nabla^{2}f(x^{*})\prec 0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 919 | 919 | haute | `\[ \_i>0 \]` | `\[ \lambda_i>0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 931 | 931 | haute | `\[ f(tx+(1-t)y) tf(x)+(1-t)f(y) \]` | `\[ f(tx+(1-t)y)\leq tf(x)+(1-t)f(y) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 952 | 952 | haute | `\[ H_f(x) \]` | `\[ \nabla^{2}f(x)\succeq 0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 958 | 958 | haute | `\[ H_f(x) \]` | `\[ \nabla^{2}f(x)\succ 0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 966 | 966 | haute | `\[ \|f(x)-f(y)\| L\|x-y\| \]` | `\[ \\|\nabla f(x)-\nabla f(y)\\|\leq L\\|x-y\\| \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 984 | 984 | haute | `\[ x_{k+1} = x_k-f(x_k) \]` | `\[ x_{k+1}=x_k-\eta\nabla f(x_k) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1000 | 1000 | haute | `\[ -f(x) \]` | `\[ -\nabla f(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1004 | 1004 | haute | `\[ x_{k+1} = x_k-f(x_k) \]` | `\[ x_{k+1}=x_k-\eta\nabla f(x_k) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1010 | 1010 | haute | `\[ \]` | `\[ \eta \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1031 | 1031 | haute | `\[ \_{t+1} = \_t âµ  âµ - \_L_B(\_t) \]` | `\[ \theta_{t+1}=\theta_t âµ  âµ - \eta\nabla L_B(\theta_t) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1045 | 1045 | haute | `\[ v_t = v_{t-1} âµ  âµ - (1-)g_t \]` | `\[ v_t=\beta v_{t-1} âµ  âµ + (1-\beta)g_t \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1051 | 1051 | haute | `\[ _t =_ {t-1} âµ  âµ - v_t \]` | `\[ \theta_t=\theta_{t-1} âµ  âµ - \eta v_t \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1063 | 1063 | haute | `\[ m_t = _1m_{t-1} âµ  âµ - (1-\_1)g_t \]` | `\[ m_t=\beta_1 m_{t-1} âµ  âµ + (1-\beta_1)g_t \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1069 | 1069 | haute | `\[ v_t = _2v_{t-1} âµ  âµ - (1-\_2)g_t^2 \]` | `\[ v_t=\beta_2 v_{t-1} âµ  âµ + (1-\beta_2)g_t^{2} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1081 | 1081 | haute | `\[ f \]` | `\[ \nabla f \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1085 | 1085 | haute | `\[ H_f \]` | `\[ \nabla^{2}f \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1089 | 1089 | haute | `\[ x_{k+1} = x_k-H(x_k)^{-1}f(x_k) \]` | `\[ x_{k+1}=x_k-H(x_k)^{-1}\nabla f(x_k) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1101 | 1101 | haute | `\[ x_{k+1} = x_k- \]` | `\[ x_{k+1}=x_k-\frac{f'(x_k)}{f''(x_k)} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1105 | 1105 | haute | `\[ x_{k+1} = x_k- H(x_k)^{-1}f(x_k) \]` | `\[ x_{k+1}=x_k-\nabla^{2}f(x_k)^{-1}\nabla f(x_k) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1133 | 1133 | haute | `\[ \_x f(x) \]` | `\[ \min_x f(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1137 | 1137 | haute | `\[ g_i(x) \]` | `\[ g_i(x)\leq 0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1157 | 1157 | haute | `\[ (x,) = f(x)+g(x) \]` | `\[ \mathcal{L}(x,\lambda)=f(x)+\lambda g(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1194 | 1194 | haute | `\[ \_x f=a \]` | `\[ \nabla_x f=a \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1204 | 1204 | haute | `\[ \_x f = (A+A^T)x \]` | `\[ \nabla_x f=(A+A^{T})x \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1208 | 1208 | haute | `\[ \_x f=2Ax \]` | `\[ \nabla_x f=2Ax \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1218 | 1218 | haute | `\[ f(x)=\|Ax-b\|^2 \]` | `\[ f(x)=\\|Ax-b\\|^{2} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1222 | 1222 | haute | `\[ f(x) = A^T(Ax-b) \]` | `\[ \nabla f(x)=2A^{T}(Ax-b) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1234 | 1234 | moyenne | `\[ () \]` | `\[ \max_\theta \mathcal{L}(\theta) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1238 | 1238 | moyenne | `\[ -() \]` | `\[ -\mathcal{L}(\theta) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1242 | 1242 | haute | `\[ \_() \]` | `\[ \nabla_\theta \mathcal{L}(\theta) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1248 | 1248 | haute | `\[ \_^2() \]` | `\[ \nabla_\theta^{2}\mathcal{L}(\theta) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1258 | 1258 | haute | `\[ y=f_(x) \]` | `\[ \hat{y}=f_\theta(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1262 | 1262 | haute | `\[ L(y,y) \]` | `\[ L(\hat{y},y) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1266 | 1266 | haute | `\[ J() = 1n _{i=1}^{n} L(f_(x_i),y_i) \]` | `\[ J(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1270 | 1270 | haute | `\[ ^\* = \_J() \]` | `\[ \theta^{*}=\arg\min_\theta J(\theta) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1274 | 1274 | haute | `\[ \_J() \]` | `\[ \nabla_\theta J(\theta) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1280 | 1280 | moyenne | `\[ f(x) f’(x) f(x) \]` | `\[ f(x)\to f'(x)\to x-\eta f'(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1284 | 1284 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1350 | 1350 | haute | `\[ = \]` | `\[ \frac{dz}{dx}=\frac{dz}{dy}\frac{dy}{dx} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1392 | 1392 | haute | `\[ f’(x) \]` | `\[ f'(x)\approx\frac{f(x+h)-f(x)}{h} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1396 | 1396 | haute | `\[ f’(x) \]` | `\[ f'(x)\approx\frac{f(x+h)-f(x-h)}{2h} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1404 | 1404 | moyenne | `\[ g_{} \]` | `\[ g_{\text{analytique}} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1408 | 1408 | moyenne | `\[ g_{} \]` | `\[ g_{\text{numérique}} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1434 | 1434 | haute | `\[ f_nf_{n-1}f_1 \]` | `\[ f_n\circ f_{n-1}\circ\cdots\circ f_1 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1440 | 1440 | haute | `\[ \_i a_i \]` | `\[ \prod_i a_i \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1452 | 1452 | haute | `\[ \_i a_i \]` | `\[ \prod_i a_i \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1470 | 1470 | haute | `\[ (x)= \]` | `\[ \sigma(x)=\frac{1}{1+e^{-x}} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1474 | 1474 | haute | `\[ ’(x) = (x)(1-(x)) \]` | `\[ \sigma'(x)=\sigma(x)(1-\sigma(x)) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1482 | 1482 | haute | `\[ (x) = (0,x) \]` | `\[ \text{ReLU}(x)=\max(0,x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1486 | 1486 | haute | `\[ ’(x) = âµ  âµ \]` | `\[ \text{ReLU}'(x)=\begin{cases}0&\text{si }x<0\\ 1&\text{si }x>0\end{cases} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1496 | 1494 | haute | `\[ (z_i) = {\_j e^{z_j}} \]` | `\[ \sigma(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1500 | 1498 | haute | `\[ = s_i(\_{ij}-s_j) \]` | `\[ \frac{\partial s_i}{\partial z_j}=s_i(\delta_{ij}-s_j) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1510 | 1508 | haute | `\[ L=-\_i y_ip_i \]` | `\[ L=-\sum_i y_i\log p_i \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1514 | 1512 | moyenne | `\[ p-y \]` | `\[ \nabla_z L=p-y \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1522 | 1520 | haute | `\[ f_ = f_Lf_{L-1}f_1 \]` | `\[ f_\theta=f_L\circ f_{L-1}\circ\cdots\circ f_1 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1526 | 1524 | haute | `\[ \_J() \]` | `\[ \min_\theta J(\theta) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1530 | 1528 | haute | `\[ \_J \]` | `\[ \nabla_\theta J \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1536 | 1536 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1564 | 1562 | moyenne | `\[ x_{} x_{} \]` | `\[ x_{\text{local}}\neq x_{\text{global}} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1578 | 1576 | haute | `\[ \|f(x)\| \]` | `\[ \\|\nabla f(x)\\| \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1614 | 1612 | moyenne | `\[ g_t J(\_t) \]` | `\[ g_t\approx\nabla_\theta J(\theta_t) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1624 | 1622 | haute | `\[ J(w) = \_i (w<sup>Tx_i-y_i)</sup>2 \]` | `\[ J(w)=\sum_i(w^{T}x_i-y_i)^{2} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1628 | 1626 | haute | `\[ J(w) = 1n X^T(Xw-y) \]` | `\[ \nabla J(w)=\frac{1}{n}X^{T}(Xw-y) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1632 | 1630 | haute | `\[ w_{t+1} = w_t-J(w_t) \]` | `\[ w_{t+1}=w_t-\eta\nabla J(w_t) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1644 | 1642 | haute | `\[ R()=\|\|\_2^2 \]` | `\[ R(\theta)=\\|\theta\\|_2^{2} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1648 | 1646 | haute | `\[ R()=2 \]` | `\[ \nabla R(\theta)=2\theta \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1656 | 1654 | haute | `\[ y=f_(x) \]` | `\[ \hat{y}=f_\theta(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1660 | 1658 | haute | `\[ L(y,y) \]` | `\[ L(\hat{y},y) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1664 | 1662 | haute | `\[ \_L \]` | `\[ \nabla_\theta L \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1668 | 1666 | moyenne | `\[ = \]` | `\[ \nabla_\theta L=\frac{\partial L}{\partial \hat{y}}\frac{\partial \hat{y}}{\p` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1693 | 1693 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1735 | 1733 | haute | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1753 | 1751 | haute | `\[ H^{nn} \]` | `\[ H\in\mathbb{R}^{n\times n} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1814 | 1812 | haute | `\[ F \]` | `\[ \nabla F \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1824 | 1822 | haute | `\[ =v \]` | `\[ \dot{x}=v \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1828 | 1826 | haute | `\[ =a \]` | `\[ \dot{v}=a \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1844 | 1842 | haute | `\[ =f(x,t) \]` | `\[ \frac{dx}{dt}=f(x,t) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1887 | 1885 | haute | `\[ \_(a\|s) \]` | `\[ \pi_\theta(a\|s) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1895 | 1893 | haute | `\[ \_J() \]` | `\[ \max_\theta J(\theta) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1903 | 1901 | haute | `\[ p_(x) \]` | `\[ p_\theta(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1909 | 1907 | moyenne | `\[ _p_(x) \]` | `\[ \nabla_\theta\log p_\theta(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1923 | 1921 | haute | `\[ ^\* = _ L() \]` | `\[ \theta^{*}=\arg\max_\theta \mathcal{L}(\theta) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1927 | 1925 | haute | `\[ ^\* = _ -L() \]` | `\[ \theta^{*}=\arg\min_\theta -\mathcal{L}(\theta) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1933 | 1933 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1939 | 1937 | haute | `\[ {xp_} \[f_(x)\] \]` | `\[ \nabla_\theta\,\mathbb{E}_{x\sim p_\theta}\left[f_\theta(x)\right] \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1952 | 1950 | haute | `\[ z=g(,) \]` | `\[ z=g(\theta,\epsilon) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1977 | 1975 | moyenne | `\[ x \]` | `\[ \Delta x\to 0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1985 | 1983 | haute | `\[ f(x) \]` | `\[ \nabla f(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 1991 | 1991 | inconnue | `\[ = \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2004 | 2002 | haute | `\[ f(x^\*)=0 \]` | `\[ \nabla f(x^{*})=0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2032 | 2030 | haute | `\[ \_{t+1} = \_t-_t_J(\_t) \]` | `\[ \theta_{t+1}=\theta_t-\eta_t\nabla_\theta J(\theta_t) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2038 | 2036 | haute | `\[ \|J()\|< \]` | `\[ \\|\nabla J(\theta)\\|<\epsilon \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2042 | 2040 | haute | `\[ \|J_{t+1}-J_t\|< \]` | `\[ \|J_{t+1}-J_t\|<\epsilon \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2056 | 2054 | haute | `\[ x_kx^\* \]` | `\[ x_k\to x^{*} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2124 | 2124 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2145 | 2143 | haute | `\[ \_i e^{x_i} \]` | `\[ \log\sum_i e^{x_i} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2149 | 2147 | haute | `\[ m+\_i e^{x_i-m} \]` | `\[ m+\log\sum_i e^{x_i-m} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2153 | 2151 | haute | `\[ m=\_i x_i \]` | `\[ m=\max_i x_i \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2163 | 2161 | haute | `\[ g g \]` | `\[ g\gets \frac{c\,g}{\\|g\\|} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2167 | 2165 | haute | `\[ \|g\|>c \]` | `\[ \\|g\\|>c \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2217 | 2215 | haute | `\[ f’(x) \]` | `\[ f'(x)\approx\frac{f(x+h)-f(x)}{h} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2252 | 2250 | haute | `\[ f(x) \]` | `\[ \nabla f(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2283 | 2281 | moyenne | `\[ p_(x) \]` | `\[ \nabla_\theta p_\theta(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2287 | 2285 | moyenne | `\[ p_(x) \]` | `\[ \nabla_\theta\log p_\theta(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2461 | 2459 | moyenne | `\[ x \]` | `\[ \sqrt{x} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2490 | 2488 | haute | `\[ x_{t+1} = x_t-f(x_t) \]` | `\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2514 | 2512 | haute | `\[ J(w,b) = 1n \_i (y_i-y_i)^2 \]` | `\[ J(w,b)=\frac{1}{n}\sum_i(\hat{y}_i-y_i)^{2} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2518 | 2516 | haute | `\[ \_wJ \]` | `\[ \nabla_w J \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2522 | 2520 | haute | `\[ \]` | `\[ \nabla_b J \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2596 | 2594 | moyenne | `\[ x \]` | `\[ \ln x \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2598 | 2596 | moyenne | `\[ x \]` | `\[ \sin x \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2600 | 2598 | moyenne | `\[ x \]` | `\[ \cos x \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2608 | 2606 | haute | `\[ f(x,y) \]` | `\[ \nabla f(x,y) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2622 | 2620 | haute | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2640 | 2638 | moyenne | `\[ \]` | `\[ \frac{dL}{dx} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2650 | 2648 | haute | `\[ a=(z) \]` | `\[ a=\sigma(z) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2656 | 2654 | moyenne | `\[ \]` | `\[ \frac{\partial L}{\partial w} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2686 | 2684 | haute | `\[ f=0 \]` | `\[ \nabla f=0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2838 | 2838 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2842 | 2842 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2846 | 2846 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2850 | 2850 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2858 | 2856 | haute | `\[ f: \]` | `\[ f:\mathbb{R}\to\mathbb{R} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2872 | 2870 | haute | `\[ f(x) \]` | `\[ \nabla f(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2878 | 2876 | haute | `\[ F:<sup>n</sup>m \]` | `\[ F:\mathbb{R}^{n}\to\mathbb{R}^{m} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2888 | 2886 | haute | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2932 | 2930 | haute | `\[ \_{t+1} = \_t âµ  âµ - _t_ J(\_t) \]` | `\[ \theta_{t+1}=\theta_t âµ  âµ - \eta_t\nabla_\theta J(\theta_t) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2958 | 2958 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2980 | 2978 | haute | `\[ f=0 \]` | `\[ \nabla f=0 \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 2986 | 2984 | haute | `\[ f \]` | `\[ \nabla f \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3016 | 3016 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3020 | 3020 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3024 | 3024 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3056 | 3056 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3060 | 3060 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3064 | 3064 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3068 | 3068 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3117 | 3117 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3121 | 3119 | haute | `\[ f(x) f’(x) \]` | `\[ f(x)\to f'(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3125 | 3123 | haute | `\[ f(x) f(x) \]` | `\[ f(x)\to \nabla f(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3129 | 3127 | haute | `\[ F(x) J_F(x) \]` | `\[ F(x)\to J_F(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3133 | 3131 | haute | `\[ f(x) H_f(x) \]` | `\[ f(x)\to H_f(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3137 | 3135 | haute | `\[ f(x) x-f(x) \]` | `\[ f(x)\to x-\eta\nabla f(x) \]` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3141 | 3141 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3145 | 3145 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3149 | 3149 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3153 | 3153 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3161 | 3161 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3165 | 3165 | inconnue | `\[ \]` | `—` |
| Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md | 3175 | 3175 | inconnue | `\[ \]` | `—` |
