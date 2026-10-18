# LOT 2 — PROPOSITIONS DE RESTAURATION, DOMAINE L (ANALYSE NUMÉRIQUE)

**Date :** 2026-10-18 — **Statut :** **propositions soumises à validation** — **non appliquées**
**Fichier source :** `Maths-vers-Informatiques/DOCUMENT L — ANALYSE NUMÉRIQUE.md` (commit `f0f5e2d`)
**Rappel :** il s'agit de **reconstructions**, pas de récupérations. Le contenu détruit n'existe plus dans le fichier.

---

## 1. Synthèse

Le lot L a été établi en relisant **les 178 blocs d'affichage** du document, et non la seule liste
des 61 défauts signalés par l'inventaire automatique.

| | |
|---|---:|
| Défauts signalés par l'inventaire | 61 |
| Défauts découverts à la lecture | **70** |
| **Défauts au total** | **131** |
| Confiance haute | 58 |
| Confiance moyenne | 29 |
| Confiance inconnue (votre décision requise) | 44 |
| **Propositions applicables** | **87** |

Le pronostic « sans doute ~95 » était donc pessimiste de moitié : la relecture révèle **115 % de
défauts supplémentaires** par rapport à l'inventaire (+70 sur 61). C'est le pire ratio observé
jusqu'ici (K : +55 %).

## 2. Ce que ce document apprend sur la dégradation

Le document L n'est pas dégradé comme le document K. Cinq mécanismes s'y ajoutent ou s'y
précisent :

1. **Les blocs vides contenaient souvent des termes, pas des équations.** L'auteur affiche des
   notions en mode mathématique (`\[ précision \]`, `\[ problèmes raides \]`). Quand le contenu
   est détruit, il ne reste aucune trace exploitable : c'est l'essentiel des **44 inconnues**.
   Dans K, la plupart des blocs vides contenaient des équations, donc des fragments.
2. **Les lettres grecques sont systématiquement détruites**, y compris quand elles portent tout le
   sens : `Av=v` (λ), `x_{k+1}=(x_k)` (φ), `H=-f` (δ et ∇), `_{t+1}=_t-L` (θ, η, ∇),
   `x_kx^` (→ et *), `h.` (→).
3. **`\_` est la trace de cinq commandes différentes** : `\sum`, `\int`, `\prod`, `\min`, `\max`.
   Le contexte seul permet de trancher — ce qui rend certaines reconstructions quasi certaines
   (`\int_a^b f(x)dx`) et d'autres non (`\_x` = `\min_x`, mais `\_i` = `\sum_i`).
4. **Les commandes sans argument sont aussi détruites** : `\times`, `\approx`, `\leq`, `\|`,
   `\nabla`, `\infty`, `\Delta`, `\mathrm{…}`, `\mathbb{…}`, `\mathcal{…}`. Conséquence utile :
   quand un signe `=` subsiste (`e_{k+1}C e_k^p`), c'est que l'auteur **n'avait pas** écrit `=` —
   il avait écrit `\leq`. L'absence de `=` est donc une information.
5. **Deux artefacts de mise en forme, distincts de la destruction :**
   - un `+` en début de ligne à l'intérieur d'un bloc devient un tiret de liste `-`
     (lignes 713, 1205-1208, et les 7 blocs de combinaison de la section 108) ;
   - des balises HTML `<sup>` apparaissent là où se trouvait un exposant
     (lignes 222, 226, 669, 1158).

## 3. Trois reconstructions confirmées par cohérence interne

Trois propositions se valident mutuellement, ce qui les rend plus sûres que leur apparence :

- **L1101 / L1105** : `H=-f` et `x_{k+1}=x_k+` — le même δ grec a disparu des deux blocs. La paire
  « résoudre Hδ = −∇f, puis x_{k+1} = x_k + δ » est la seule lecture qui rende les deux blocs
  cohérents entre eux.
- **L309 / L313** : sans l'opérateur `fl(·)`, la phrase « ((a+b)+c) peut être différent de
  (a+(b+c)) » est fausse en arithmétique exacte. Les deux blocs n'ont de sens qu'ensemble.
- **L369, L382, L435, L1170, L1271** : la trace `x^` revient cinq fois pour `x^*`. L435 (`x^x`)
  est la seule occurrence inexpliquée, reconstruite en `x^*` avec réserve.

## 4. Les propositions

**Correctif :** `domaine-L.patch.json` — 131 entrées : 58 haute, 29 moyenne, 44 inconnue — **87 applicables**

### Confiance haute (58)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 166 | `Si (x) est la valeur exacte et () la valeur ca` | `Si (x) est la valeur exacte et (\hat{x}) la valeur calculée :` | La ligne 168 restaurée utilise le même symbole. |
| 168 | `\[ E_a=\|x-\|. \]` | `\[ E_a=\|x-\hat{x}\|. \]` | Avec x=10 et x̂=9,99 : E_a=0,01, ce qui est exactement le résultat affiché ligne 180. |
| 176 | `\[ =9.99. \]` | `\[ \hat{x}=9.99. \]` | E_a=\|10-9,99\|=0,01 = valeur de la ligne 180. |
| 186 | `\[ E_r=. \]` | `\[ E_r=\frac{\|x-\hat{x}\|}{\|x\|}. \]` | E_r=E_a/\|x\| : pour x=10 et E_a=0,01, E_r=0,001. |
| 192 | `\[ E_r(%)= 100. \]` | `\[ E_r(\%)=\frac{\|x-\hat{x}\|}{\|x\|}\times 100. \]` | 100x l'erreur relative : 0,001 → 0,1 %. |
| 222 | `\[ e^x = \_{k=0}<sup>{}\\frac{x</sup>k}{k!} \]` | `\[ e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!} \]` | Somme de 0 a l'infini de x^k/k! : développement de Taylor de e^x en 0. |
| 226 | `\[ e^x \_{k=0}<sup>{N}\\frac{x</sup>k}{k!}. \]` | `\[ e^x \approx \sum_{k=0}^{N}\frac{x^k}{k!}. \]` | N fini : la somme partielle approche e^x, le reste est l'erreur de troncature annoncée par le texte. |
| 255 | `\[ \]` | `\[ \mathbb{R} \]` | La ligne 261 confirmé : l'ensemble en question est « continu et infini ». |
| 261 | `\[ \]` | `\[ \mathbb{R} \]` | Seul R est continu, infini et oppose a un ensemble fini de flottants. |
| 365 | `\[ x_0,x_1,x_2, \]` | `\[ x_0,x_1,x_2,\ldots \]` | Une suite itérative est infinie. |
| 369 | `\[ x_kx^. \]` | `\[ x_k\to x^*. \]` | « qui doit idealement vérifier » : convergence vers la solution x*. |
| 382 | `\[ e_k=\|x_k-x^\| \]` | `\[ e_k=\|x_k-x^*\| \]` | e_k → 0 ssi x_k → x*. |
| 386 | `\[ e_{k+1}C e_k^p, \]` | `\[ e_{k+1}\leq C e_k^p, \]` | Definition usuelle de l'ordre de convergence : e_{k+1} <= C e_k^p. |
| 408 | `\[ \|x_{k+1}-x_k\|< \]` | `\[ \|x_{k+1}-x_k\|<\varepsilon \]` | Critère absolu standard ; le texte énuméré ensuite tolérance absolue, relative, résidu. |
| 412 | `\[ \|F(x_k)\|< \]` | `\[ \|F(x_k)\|<\varepsilon \]` | Le résidu s'annule a la solution. |
| 449 | `\[ m=. \]` | `\[ m=\frac{a+b}{2}. \]` | m est le milieu de [a,b] : le texte decrit ensuite la conservation du sous-intervalle de changement de signe. |
| 501 | `\[ f’(x_n) {x_n-x_{n-1}}. \]` | `\[ f'(x_n)\approx\frac{f(x_n)-f(x_{n-1})}{x_n-x_{n-1}}. \]` | Quotient des differences finies : la pente entre les deux derniers points. |
| 631 | `\[ x_0,x_1,x_2, \]` | `\[ x_0,x_1,x_2,\ldots \]` | Une suite itérative est infinie. |
| 669 | `\[ \_x 12x<sup>TAx-b</sup>Tx. \]` | `\[ \min_x \frac{1}{2}x^TAx-b^Tx. \]` | Le gradient de 1/2 x'Ax - b'x est Ax-b : minimiser revient a resoudre Ax=b, ce que dit le texte. |
| 691 | `\[ (x_0,y_0),,(x_n,y_n). \]` | `\[ (x_0,y_0),\ldots,(x_n,y_n). \]` | Enumeration elliptique de n+1 points. |
| 701 | `\[ p(x)= \_{i=0}^{n} y_iL_i(x) \]` | `\[ p(x)=\sum_{i=0}^{n} y_iL_i(x) \]` | p(x_i)=y_i : en x=x_i, seul L_i vaut 1, les autres s'annulent. |
| 705 | `\[ L_i(x)= \_{ji} . \]` | `\[ L_i(x)=\prod_{j\neq i}\frac{x-x_j}{x_i-x_j}. \]` | L_i(x_j)=1 si j=i, 0 sinon : c'est la définition des polynômes de Lagrange. |
| 748 | `\[ p(x)f(x) \]` | `\[ p(x)\approx f(x) \]` | Opposition avec l'interpolation de la ligne 744 qui impose p(x_i)=f(x_i). |
| 756 | `\[ \_i (y_i-f(x_i))^2. \]` | `\[ \sum_i (y_i-f(x_i))^2. \]` | Minimum atteint quand les résidus sont nuls en moyenne quadratique. |
| 760 | `\[ \_x\|Ax-b\|\_2^2. \]` | `\[ \min_x\\|Ax-b\\|_2^2. \]` | La norme au carré de Ax-b est la somme des carrés des résidus de la ligne 756. |
| 786 | `\[ I= \_a^b f(x),dx. \]` | `\[ I=\int_a^b f(x)\,dx. \]` | Notation standard de l'intégrale a approcher. |
| 794 | `\[ \_a^b f(x),dx \_i f(x_i)x. \]` | `\[ \int_a^b f(x)\,dx \approx \sum_i f(x_i)\,\Delta x. \]` | Somme des aires de rectangles de largeur Delta x. |
| 804 | `\[ \_a^b f(x),dx \[f(a)+f(b)\]. \]` | `\[ \int_a^b f(x)\,dx \approx \frac{b-a}{2}\left[f(a)+f(b)\righ` | Aire du trapèze : base fois (f(a)+f(b))/2. |
| 847 | `\[ f’(x) . \]` | `\[ f'(x)\approx\frac{f(x+h)-f(x)}{h}. \]` | Developpement de Taylor : (f(x+h)-f(x))/h = f'(x) + O(h). |
| 851 | `\[ f’(x) . \]` | `\[ f'(x)\approx\frac{f(x)-f(x-h)}{h}. \]` | (f(x)-f(x-h))/h = f'(x) + O(h). |
| 855 | `\[ f’(x) . \]` | `\[ f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}. \]` | Erreur en O(h^2) : la section 48 annoncé O(h), O(h^2), O(h^4). |
| 901 | `\[ =f(t,y). \]` | `\[ y'=f(t,y). \]` | Forme standard d'un problème de Cauchy, complété par y(t_0)=y_0 ligne 905. |
| 997 | `\[ I_N = 1N \_{i=1}^{N}f(X_i). \]` | `\[ I_N = \frac{1}{N}\sum_{i=1}^{N}f(X_i). \]` | Estimateur sans biais de E[f(X)] : moyenne empirique de N tirages. |
| 1001 | `\[ I_NI. \]` | `\[ I_N\to I. \]` | Loi des grands nombres : I_N tend vers I quand N croît. |
| 1007 | `\[ O(). \]` | `\[ O\left(\frac{1}{\sqrt{N}}\right). \]` | L'écart-type de la moyenne empirique est sigma/racine de N : diviser l'erreur par 10 coûte 100 fois plus d'échantillons, ce que di |
| 1044 | `\[ Av=v. \]` | `\[ Av=\lambda v. \]` | v propre associé a la valeur propre lambda. |
| 1071 | `\[ \_x f(x). \]` | `\[ \min_x f(x). \]` | Probleme d'optimisation sans contrainte. |
| 1089 | `\[ f(x), \]` | `\[ \min f(x), \]` | Newton pour l'optimisation minimise f. |
| 1093 | `\[ x_{k+1} = x_k- H_f(x_k)^{-1}f(x_k). \]` | `\[ x_{k+1} = x_k- H_f(x_k)^{-1}\nabla f(x_k). \]` | H_f est la hessienne : l'itération annule le gradient au second ordre. |
| 1101 | `\[ H=-f \]` | `\[ H\delta=-\nabla f \]` | Resolution du système linéaire en le pas delta. |
| 1105 | `\[ x_{k+1}=x_k+. \]` | `\[ x_{k+1}=x_k+\delta. \]` | Le pas delta calcule en 1101 est ajoute a x_k. |
| 1142 | `\[ = . \]` | `\[ \frac{dy}{dx}=\frac{dy}{dz}\frac{dz}{dx}. \]` | Dérivée de la composée : produit des dérivées. |
| 1154 | `\[ x_{k+1}=(x_k). \]` | `\[ x_{k+1}=\varphi(x_k). \]` | Forme générale annoncée par le titre de section. |
| 1158 | `\[ x<sup>\=(x</sup>). \]` | `\[ x^*=\varphi(x^*). \]` | Le point fixe vérifié x=phi(x). |
| 1164 | `\[ x=(x) \]` | `\[ x=\varphi(x) \]` | Coherence avec la ligne 1158. |
| 1170 | `\[ \|’(x^)\|<1, \]` | `\[ \|\varphi'(x^*)\|<1, \]` | Le module de la dérivée au point fixe doit être inférieur a 1 : théorème du point fixe. |
| 1271 | `\[ x_hx^, \]` | `\[ x_h\to x^*, \]` | Si les résultats convergent vers x*, la discrétisation est convergente. |
| 1295 | `\[ x_110^{-10} \]` | `\[ x_1\sim 10^{-10} \]` | Opposition des échelles : 10^-10 contre 10^10, écart de 20 decades. |
| 1299 | `\[ x_210^{10}, \]` | `\[ x_2\sim 10^{10}, \]` | Idem. |
| 1326 | `\[ AR^{nn} \]` | `\[ A\in\mathbb{R}^{n\times n} \]` | Une matrice n x n demandée O(n^2) de mémoire, comme l'annoncé la ligne 1330. |
| 1394 | `\[ \_L(). \]` | `\[ \min_{\theta}\mathcal{L}(\theta). \]` | Forme standard ; le bloc « Gradient » qui suit porte sur la même perte. |
| 1398 | `\[ \_L. \]` | `\[ \nabla_\theta \mathcal{L}. \]` | Gradient de la fonction minimisée en 1394. |
| 1402 | `\[ \_{t+1} = \_t-L. \]` | `\[ \theta_{t+1}=\theta_t-\eta\nabla\mathcal{L}. \]` | Pas de descente : on retranche au paramètre le gradient multiplie par le pas d'apprentissage. |
| 1464 | `\[ =a. \]` | `\[ \frac{dv}{dt}=a. \]` | Euler : v_{n+1}=v_n+h a_n est l'integration de dv/dt=a. |
| 2065 | `\[ x,,\|x-\|. \]` | `\[ x,\ \hat{x},\ \|x-\hat{x}\|. \]` | Coherence avec les lignes 168 et 176. |
| 2221 | `\[ (x_i,y_i) f(x) \]` | `\[ (x_i,y_i)\to f(x) \]` | Des données vers la fonction interpolée. |
| 2225 | `\[ f(x),dx . \]` | `\[ \int_a^b f(x)\,dx. \]` | Coherence avec la ligne 786. |
| 2233 | `\[ =f(t,y) . \]` | `\[ y'=f(t,y). \]` | Coherence avec la ligne 901. |

### Confiance moyenne (29)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 136 | `\[ f(x),Ax=b,f,\_a^b f(x),dx,=f(t,y) \]` | `\[ f(x),\quad Ax=b,\quad \nabla f,\quad \int_a^b f(x)\,dx,\qua` | Coherence avec le texte : L pose la question du calcul effectif de ces objets. |
| 154 | `\[ x. \]` | `\[ \hat{x}. \]` | Coherence avec E_a=\|x-\hat{x}\|. |
| 242 | `\[ x=m^e. \]` | `\[ x=m\,2^e. \]` | b=2 : représentation binaire m x 2^e. |
| 271 | `\[ \_{}^{-p} \]` | `\[ \varepsilon_{\text{mach}} \approx \beta^{-p} \]` | En double précision IEEE-754 : beta=2, p=53, 2^-52 ≈ 2,2x10^-16, l'epsilon machine connu. Le texte signale « selon la convention u |
| 297 | `\[ \]` | `\[ \text{annulation catastrophique} \]` | Terme consacre : cancellation = annulation, catastrophic = catastrophique. |
| 309 | `\[ ((a+b)+c) \]` | `\[ \mathrm{fl}((a+b)+c) \]` | fl(a+b+c) diffère de fl(a+fl(b+c)) : c'est précisément la perte d'associativité. |
| 313 | `\[ (a+(b+c)). \]` | `\[ \mathrm{fl}(a+(b+c)). \]` | Idem. |
| 416 | `\[ {(1,\|x_k\|)} <. \]` | `\[ \|x_{k+1}-x_k\|<\varepsilon\max(1,\|x_k\|). \]` | Critère relatif standard : borne l'incrément par une tolérance fois max(1,\|x\|). Si ce n'est pas la forme voulue, la replacer par |
| 435 | `\[ x^x. \]` | `\[ x^*. \]` | Coherence avec les lignes 369, 382, 1170, 1271 ou x* apparaît sous la forme x^. |
| 465 | `\[ \]` | `\[ f'(x_n) \]` | Newton-Raphson requiert f' : section 17.3 sur les risques quand f'(x) est proche de zero. |
| 485 | `\[ . \]` | `\[ \text{convergence quadratique}. \]` | Newton est quadratique pres d'une racine simple : ordre p=2. |
| 711 | `\[ p(x) = a_0+ a_1(x-x_0) ⏎  ⏎ - a_2(x-x_0)(x-` | `\[ p(x) = a_0+ a_1(x-x_0)+ a_2(x-x_0)(x-x_1)+\ldots+a_n(x-x_0)` | Forme imbriquée : chaque terme ajoute un facteur (x-x_j), le texte vante l'ajout progressif de points. |
| 776 | `\[ \_x \|Ax-b\|\_2^2+ \|x\|\_2^2. \]` | `\[ \min_x \\|Ax-b\\|_2^2+\lambda\\|x\\|_2^2. \]` | Le texte parle de régularisation ; la pénalité quadratique limite les solutions instables. |
| 814 | `\[ \_a^b f(x),dx . \]` | `\[ \int_a^b f(x)\,dx \approx \frac{b-a}{6}\left[f(a)+4f\left(\` | Simpson est exacte pour les polynômes de degré 3 : vérifiable sur un polynôme de degré 2. |
| 875 | `\[ h. \]` | `\[ h\to 0. \]` | Les ordres O(h^p) de la section 48 s'entendent pour h tendant vers 0. |
| 936 | `\[ \]` | `\[ \text{problèmes raides} \]` | Traduction consacrée de stiff problems. |
| 1061 | `\[ x_{k+1}= . \]` | `\[ x_{k+1}=\frac{Ax_k}{\\|Ax_k\\|}. \]` | La normalisation empêche la divergence ; le rapport de Rayleigh donne alors la valeur propre. |
| 1203 | `\[ E_{} E_{} ⏎  ⏎ - E_{} ⏎ - E_{} ⏎ - E_{} ⏎ -` | `\[ E_{\text{total}}=E_{\text{modèle}}+E_{\text{données}}+E_{\t` | Les cinq contributions sont celles des sections 5.1 a 5.6. |
| 1336 | `\[ O((A)). \]` | `\[ O(\mathrm{nnz}(A)). \]` | Formulation standard nnz(A). |
| 1580 | `\[ KL \]` | `\[ K\times L \]` | Combinaison des domaines K (structures) et L (calcul). |
| 1697 | `\[ \]` | `\[ \text{exact} \]` | Le titre de section nomme les trois notions. |
| 1699 | `\[ \]` | `\[ \text{approché} \]` | Idem. |
| 1701 | `\[ \]` | `\[ \text{numérique} \]` | Idem. |
| 1794 | `\[ T_{}<T_{}. \]` | `\[ T_{\text{calcul}}<T_{\text{budget}}. \]` | Contrainte de temps réel annoncée par le titre de section. |
| 2201 | `\[ \]` | `\[ x=m\,b^e \]` | Coherence avec la ligne 238. |
| 2205 | `\[ \]` | `\[ E_r=\frac{\|x-\hat{x}\|}{\|x\|} \]` | Coherence avec la ligne 186. |
| 2241 | `\[ \]` | `\[ r=Ax-b \]` | Coherence avec la ligne 1236. |
| 2286 | `\[ \]` | `\[ \min_x f(x) \]` | Coherence avec la ligne 1071. |
| 2290 | `\[ . \]` | `\[ y'=f(t,y). \]` | Coherence avec les lignes 901 et 2233. |

### Confiance inconnue — décision requise (44)

| Ligne | Bloc actuel | Ce que le bloc contenait |
|---:|---|---|
| 13 | `\[ \]` | tension entre [ ] et [ ] — le couple oppose n'est pas nomme ailleurs dans le document (candidats : précision / coût, exactitude / vitesse, stabilité / rapidité) |
| 17 | `\[ . \]` | second terme de la même opposition |
| 55 | `\[ \]` | ce que le système ne doit jamais considérer sans analyser les conditions du calcul |
| 61 | `\[ \]` | principe directeur du domaine (probablement un énoncé, pas une formule) |
| 115 | `\[ \]` | chaîne des domaines A a L (candidat : A → B → … → L) |
| 146 | `\[ \]` | le réel que l'on écrit exactement sur papier (candidats : racine de 2, 0,1, 1/3, pi) |
| 158 | `\[ \]` | ce qui reste vrai dans la plupart des cas (candidat : x̂ ≈ x) |
| 202 | `\[ . \]` | erreur de modele : bloc vide |
| 343 | `\[ \]` | ce qui distingue stabilité, conditionnement et convergence |
| 351 | `\[ . \]` | condition de mauvais conditionnement |
| 723 | `\[ . \]` | ce que montre le phénomène de Runge |
| 808 | `\[ I h . \]` | règle des trapèzes composée |
| 883 | `\[ \]` | ce qui diminue quand h diminue |
| 887 | `\[ \]` | ce qui augmente quand h diminue |
| 893 | `\[ \]` | forme de la courbe d'erreur (candidat : E(h) = C1 h^p + C2 eps / h) |
| 1017 | `\[ \]` | ce qui rend les méthodes deterministes coûteuses (candidat : la malediction de la dimension) |
| 1148 | `\[ . \]` | les deux poles reliés par la différentiation automatique |
| 1193 | `\[ \]` | idée des méthodes multigrilles |
| 1197 | `\[ . \]` | ce que deviennent les erreurs |
| 1281 | `\[ . \]` | examen analytique de la sensibilité |
| 1285 | `\[ . \]` | examen experimental |
| 1364 | `\[ . \]` | le compromis ameliore par la précision mixte (candidat : vitesse / précision) |
| 1604 | `\[ \]` | architecture d'un solveur sérieuse |
| 1770 | `\[ \]` | critères d'évaluation d'une méthode |
| 1812 | `\[` | combinaison L + K → mondes procéduraux dynamiques |
| 1820 | `\[` | combinaison L + J → systèmes de décision numériques |
| 1828 | `\[` | combinaison L + I → apprentissage et simulation |
| 1836 | `\[` | combinaison L + C → calcul scientifique et IA |
| 1844 | `\[` | combinaison L + G → simulation sous incertitude |
| 1852 | `\[` | combinaison L + D → reconstruction et animation 3D |
| 1860 | `\[` | combinaison L + E/F → planification et systèmes complexes |
| 1870 | `\[ \]` | ce que le système applique pour inventer une application |
| 1874 | `\[ \]` | premier exemple |
| 1878 | `\[ . \]` | second exemple |
| 2106 | `\[ \]` | quantité a estimer par Monte-Carlo (candidats : pi, une intégrale) |
| 2191 | `\[ \]` | ce que le développeur doit pouvoir vérifier |
| 2282 | `\[ \]` | relation avec le domaine I |
| 2302 | `\[ . \]` | relation avec le domaine H |
| 2308 | `\[ \]` | l'idée fondamentale enseignée par le domaine L |
| 2312 | `\[ \]` | la chaîne entre le modele et le résultat |
| 2340 | `\[ \]` | formule mentale a conserver pour tout problème numérique |
| 2344 | `\[ \]` | ce que l'IA doit appliquer pour passer du concept au logiciel |
| 2350 | `\[ \]` | point de départ |
| 2354 | `\[ . \]` | point d'arrivée |


## 5. Non traité : les artefacts d'échappement de crochets

Quatre blocs contiennent des crochets échappés à l'intérieur du mode mathématique :

| Ligne | Bloc | Ce que c'est |
|---:|---|---|
| 445 | `\[ \[a,b\]. \]` | l'intervalle `[a,b]` |
| 993 | `\[ I=E\[f(X)\], \]` | l'espérance `E[f(X)]` |
| 2237 | `\[ E\[f(X)\] . \]` | idem |
| 2298 | `\[ E\[X\] . \]` | l'espérance `E[X]` |

Ce ne sont **pas** des équations détruites : le contenu est intact, seuls les crochets ont été
échappés par un traitement automatique. C'est la même famille que les 48 blocs d'E, R, S et U
déjà écartés du décompte dans le rapport A7.

**Je ne les ai pas corrigés**, par cohérence avec cette décision. Ils posent néanmoins un problème
pratique : un `\[` imbriqué dans un `\[ … \]` rend le bloc mathématiquement invalide. Dites-moi si
vous voulez qu'ils soient déséchappés (`E[f(X)]` au lieu de `E\[f(X)\]`) — c'est un lot à part,
quatre lignes, sans risque.

## 6. Ce que je vous demande

1. **Valider ou refuser les 87 propositions** de confiance haute et moyenne (58 + 29).
2. **Arbitrer les 44 blocs inconnus.** Pour la plupart, un mot de vous suffit : dites-moi par
   exemple ce que contenait la ligne 61 (« Principe directeur ») ou la ligne 2340 (« formule
   mentale à conserver »), et je l'écris. Si vous préférez, je peux laisser ces blocs vides : ils
   ne nuisent pas à la lecture, ils sont simplement vides.
3. **Trancher les quatre artefacts d'échappement** (§5).

Une fois le lot validé, je l'applique sur la branche `arena/restauration-equations` et je vous
livre le diff, comme pour le lot 1.
