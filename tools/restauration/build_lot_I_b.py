#!/usr/bin/env python3
"""Construction du lot 3b : domaine I — Calcul differentiel, sections 41 a 179.

Lignes 792 a 3175. Voir build_lot_I_a.py pour le format.
Les entrees de confiance "inconnue" portent un candidat dans le champ
`validation` ; elles ne sont pas applicables en l'etat.
"""

import json
from collections import Counter

SOURCE = "Maths-vers-Informatiques/Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md"
RACINE = "/home/user/_audit/connaissance"
SORTIE = "docs/restauration/propositions/domaine-I-lot3b.patch.json"

E = [
 (800, 800, r"\[ \frac{dz}{dx}=\frac{dz}{du}\frac{du}{dx} \]", "haute",
  "§41 « Si z=f(u) et u=g(x), alors : [= ] ». Règle de la chaîne en notation de Leibniz ; les trois \\frac ont été détruites. Les variables sont celles des deux blocs précédents.",
  "Rendu : dz/dx = dz/du · du/dx."),

 (812, 812, r"\[ x \to z \to a \to L \]", "haute",
  "§42 « Considérons : [ ] ». Les quatre termes sont intacts, les flèches ont été détruites — même destruction qu'en l. 424.",
  "Rendu : x → z → a → L. Cohérent avec les trois blocs suivants (z, a, L)."),

 (816, 816, r"\[ a=\sigma(z) \]", "haute",
  "§42 « avec : z=Wx+b, [a=(z)], L=L(a,y) ». Le \\sigma a été détruit, la parenthèse est restée. Le §85 nomme explicitement la fonction d'activation.",
  "Rendu : a=σ(z). L'activation entre la pré-activation et la perte."),

 (824, 824, r"\[ \frac{\partial L}{\partial W}=\frac{\partial L}{\partial a}\cdot\frac{\partial a}{\partial z}\cdot\frac{\partial z}{\partial W} \]", "moyenne",
  "§42 « Alors : [= ] La backpropagation répète ce principe. » — les numérateurs et dénominateurs ont été détruits avec \\frac et \\partial ; il ne reste que le signe égal.",
  "Candidat alternatif : \\frac{\\partial L}{\\partial W}=\\delta x^{T}. Formulation à confirmer par l'auteur."),

 (834, 834, r"\[ \nabla f(x^{*})=0 \]", "haute",
  "§43 POINTS CRITIQUES « Un point (x*) peut être critique lorsque : [ ] ou lorsque la dérivée n'existe pas. » — \\nabla détruit.",
  "Condition de stationnarité ; la phrase suivante évoque l'absence de dérivée, ce qui confirme qu'il s'agit bien du gradient."),

 (851, 851, r"\[ f(x^{*})\leq f(x) \]", "haute",
  "§44 MINIMUM LOCAL « (x*) est un minimum local si, dans un voisinage de (x*) : [ ] ». \\leq détruit.",
  "Rendu : f(x*) ≤ f(x)."),

 (857, 857, r"\[ f(x^{*})\geq f(x) \]", "haute",
  "§45 MAXIMUM LOCAL. \\geq détruit ; le minimum et le maximum se distinguent uniquement par le sens de l'inégalité, perdu avec la commande.",
  "Rendu : f(x*) ≥ f(x)."),

 (895, 895, r"\[ \nabla^{2}f(x^{*})\succ 0 \]", "haute",
  "§48 « ### Hessienne définie positive [ ] implique un minimum local strict ». Le résidu H(x*) : \\nabla^2 et \\succ détruits.",
  "Rendu : ∇²f(x*) ≻ 0."),

 (901, 901, r"\[ \nabla^{2}f(x^{*})\prec 0 \]", "haute",
  "§48 « ### Hessienne définie négative [ ] implique un maximum local strict. »",
  "Rendu : ∇²f(x*) ≺ 0."),

 (919, 919, r"\[ \lambda_i>0 \]", "haute",
  "§49 « Si : [ ] dans toutes les directions, la courbure est positive. » Les valeurs propres de la Hessienne : \\lambda détruit.",
  "Rendu : λᵢ > 0."),

 (931, 931, r"\[ f(tx+(1-t)y)\leq tf(x)+(1-t)f(y) \]", "haute",
  "§50 CONVEXITÉ « Une fonction (f) est convexe si, pour (x,y) et (t) : [ ] ». Tous les termes sont présents ; seul \\leq a été détruit.",
  "Définition standard de la convexité."),

 (952, 952, r"\[ \nabla^{2}f(x)\succeq 0 \]", "haute",
  "§52 CRITÈRE HESSIEN « Pour une fonction deux fois différentiable : [ ] sur un domaine convexe constitue un critère de convexité. » \\nabla^2 et \\succeq détruits.",
  "Rendu : ∇²f(x) ⪰ 0."),

 (958, 958, r"\[ \nabla^{2}f(x)\succ 0 \]", "haute",
  "§52 « Si : [ ] partout, on obtient une forme de convexité stricte. » Le bloc est distinct du précédent : c'est le cas strict.",
  "Rendu : ∇²f(x) ≻ 0."),

 (966, 966, r"\[ \|\nabla f(x)-\nabla f(y)\|\leq L\|x-y\| \]", "haute",
  "§53 LIPSCHITZIANITÉ DU GRADIENT « Une fonction possède un gradient (L)-Lipschitz si : [ ] ». Résidu |f(x)-f(y)| L|x-y| : \\nabla, \\| et \\leq détruits.",
  "Définition standard du gradient L-Lipschitz."),

 (984, 984, r"\[ x_{k+1}=x_k-\eta\nabla f(x_k) \]", "haute",
  "§55 DESCENTE DE GRADIENT « Le principe est : [ ] où : ». Le \\eta (pas d'apprentissage) et \\nabla ont été détruits ; la section 57 leur est consacrée.",
  "Rendu : x_{k+1}=x_k−η∇f(x_k)."),

 (1000, 1000, r"\[ -\nabla f(x) \]", "haute",
  "§56 « Pour diminuer (f), on choisit donc : [ ] D'où : ». \\nabla détruit.",
  "Rendu : −∇f(x)."),

 (1004, 1004, r"\[ x_{k+1}=x_k-\eta\nabla f(x_k) \]", "haute",
  "§56 « D'où : [ ] ». Même reconstruction qu'en l. 984.",
  "Rendu : x_{k+1}=x_k−η∇f(x_k)."),

 (1010, 1010, r"\[ \eta \]", "haute",
  "§57 LEARNING RATE « Le paramètre : [vide] contrôle la taille du déplacement. » — le \\eta a été détruit ; c'est le seul paramètre de cette section.",
  "Rendu : η. La phrase suivante (« trop grand… trop petit ») confirme qu'il s'agit du pas."),

 (1031, 1033, "\\[ \\theta_{t+1}=\\theta_t\n\n- \\eta\\nabla L_B(\\theta_t) \\]", "haute",
  "§58 SGD « Au lieu d'utiliser toute la fonction de perte : [ ] où (B) représente un mini-batch. » — le \\_ est le résidu de \\sum ailleurs, ici les lettres grecques \\theta et \\eta ont été détruites. Le signe moins est réel : on descend.",
  "Rendu : θ_{t+1}=θ_t−η∇L_B(θ_t)."),

 (1045, 1047, "\\[ v_t=\\beta v_{t-1}\n\n+ (1-\\beta)g_t \\]", "haute",
  "§59 MOMENTUM « Une forme classique : [ ] ». Le \\beta a été détruit dans les deux occurrences (l'une d'elles laisse 1-). Le signe + a été converti en puce -, artefact déjà observé dans les blocs de Taylor.",
  "Rendu : v_t=βv_{t-1}+(1−β)g_t. Forme standard du momentum."),

 (1051, 1053, "\\[ \\theta_t=\\theta_{t-1}\n\n- \\eta v_t \\]", "haute",
  "§59 « puis : [ ] ». Mise à jour des paramètres avec la vitesse. Le signe moins est conforme à une descente.",
  "Rendu : θ_t=θ_{t-1}−ηv_t."),

 (1063, 1065, "\\[ m_t=\\beta_1 m_{t-1}\n\n+ (1-\\beta_1)g_t \\]", "haute",
  "§60 ADAM « On calcule : [ ] ». Le \\beta_1 a été détruit ; le signe + est devenu une puce.",
  "Rendu : m_t=β₁m_{t-1}+(1−β₁)g_t. Premier moment."),

 (1069, 1071, "\\[ v_t=\\beta_2 v_{t-1}\n\n+ (1-\\beta_2)g_t^{2} \\]", "haute",
  "§60 « et : [ ] ». Second moment : le \\beta_2 a été détruit, l'exposant 2 du gradient a survécu.",
  "Rendu : v_t=β₂v_{t-1}+(1−β₂)g_t²."),

 (1081, 1081, r"\[ \nabla f \]", "haute",
  "§61 « Les méthodes du premier ordre utilisent principalement : [ ] Les méthodes du second ordre utilisent également : ». \\nabla détruit.",
  "Rendu : ∇f. Opposé à la Hessienne du bloc suivant."),

 (1085, 1085, r"\[ \nabla^{2}f \]", "haute",
  "§61 second ordre. Le résidu H_f est le nom de la Hessienne ; \\nabla^2 détruit.",
  "Rendu : ∇²f."),

 (1089, 1089, r"\[ x_{k+1}=x_k-H(x_k)^{-1}\nabla f(x_k) \]", "haute",
  "§61 « Exemple : [ ] C'est l'idée de la méthode de Newton. » \\nabla détruit.",
  "Rendu : x_{k+1}=x_k−H(x_k)^{-1}∇f(x_k)."),

 (1101, 1101, r"\[ x_{k+1}=x_k-\frac{f'(x_k)}{f''(x_k)} \]", "haute",
  "§62 MÉTHODE DE NEWTON « Pour résoudre f'(x)=0, on peut utiliser : [x_{k+1}=x_k−] ». La fraction a été détruite (régime « tout détruit »), mais c'est la seule itération qui résolve f'=0.",
  "Newton scalaire : x_{k+1}=x_k−f'(x_k)/f''(x_k)."),

 (1105, 1105, r"\[ x_{k+1}=x_k-\nabla^{2}f(x_k)^{-1}\nabla f(x_k) \]", "haute",
  "§62 « En optimisation multivariable : [ ] ». \\nabla et \\nabla^2 détruits.",
  "Newton multivariable, cohérent avec le cas scalaire de la ligne précédente."),

 (1133, 1133, r"\[ \min_x f(x) \]", "haute",
  "§65 OPTIMISATION SOUS CONTRAI NTES « On peut chercher : [ ] sous : ». Le \\_ est le résidu de \\min.",
  "Rendu : min_x f(x)."),

 (1137, 1137, r"\[ g_i(x)\leq 0 \]", "haute",
  "§65 « sous : [g_i(x)] et : [h_j(x)=0] ». L'inégalité a été détruite ; la contrainte d'égalité, elle, est intacte, ce qui distingue les deux.",
  "Rendu : g_i(x) ≤ 0. Convention usuelle de l'optimisation sous contraintes."),

 (1157, 1157, r"\[ \mathcal{L}(x,\lambda)=f(x)+\lambda g(x) \]", "haute",
  "§66 MULTIPLICATEURS DE LAGRANGE « on construit : [ ] ». Le résidu (x,) = f(x)+g(x) montre le \\mathcal{L} détruit, le \\lambda détruit, et la virgule orpheline de l'argument manquant.",
  "Rendu : 𝓛(x,λ)=f(x)+λg(x)."),

 (1194, 1194, r"\[ \nabla_x f=a \]", "haute",
  "§69 « Soit f(x)=a^Tx. Alors : [ ] ». Le \\_ est le résidu de \\nabla.",
  "Rendu : ∇_x f=a."),

 (1204, 1204, r"\[ \nabla_x f=(A+A^{T})x \]", "haute",
  "§70 FORME QUADRATIQUE « on obtient, dans le cas général : [ ] ». \\nabla détruit.",
  "Rendu : ∇_x f=(A+A^T)x."),

 (1208, 1208, r"\[ \nabla_x f=2Ax \]", "haute",
  "§70 « Si (A) est symétrique : [ ] ». \\nabla détruit.",
  "Le cas symétrique simplifie (A+A^T) en 2A."),

 (1218, 1218, r"\[ f(x)=\|Ax-b\|^{2} \]", "haute",
  "§71 SQUARED ERROR « Considérons : [ ] ». Le \\| a été détruit, remplacé par des barres simples.",
  "Rendu : f(x)=‖Ax−b‖²."),

 (1222, 1222, r"\[ \nabla f(x)=2A^{T}(Ax-b) \]", "haute",
  "§71 « Alors : [ ] ». \\nabla détruit ; le facteur 2 manque, détruit avec lui.",
  "Vérifier : ∇‖Ax−b‖²=2A^T(Ax−b)."),

 (1234, 1234, r"\[ \max_\theta \mathcal{L}(\theta) \]", "moyenne",
  "§72 LOG-LIKELIHOOD « on cherche souvent à maximiser : [ ] ou à minimiser : ». Le \\max et le \\mathcal{L} ont été détruits ; le θ ne subsiste que dans les parenthèses vides.",
  "Candidat alternatif : \\max_\\theta \\log \\mathcal{L}(\\theta). La vraisemblance ou sa log-forme : à confirmer."),

 (1238, 1238, r"\[ -\mathcal{L}(\theta) \]", "moyenne",
  "§72 « ou à minimiser : [-()] ». Même incertitude que la ligne précédente.",
  "Négatif de la quantité maximisée en l. 1234."),

 (1242, 1242, r"\[ \nabla_\theta \mathcal{L}(\theta) \]", "haute",
  "§72 « Le gradient : [ ] indique comment modifier les paramètres. » \\nabla et \\mathcal{L} détruits.",
  "Rendu : ∇_θ 𝓛(θ)."),

 (1248, 1248, r"\[ \nabla_\theta^{2}\mathcal{L}(\theta) \]", "haute",
  "§72 « La Hessienne : [ ] décrit la courbure locale de la vraisemblance. » Le résidu \\_^2() montre \\nabla_\\theta^2 détruit.",
  "Rendu : ∇²_θ 𝓛(θ)."),

 (1258, 1258, r"\[ \hat{y}=f_\theta(x) \]", "haute",
  "§73 FONCTION DE PERTE « Un modèle produit : [y=f_(x)] ». Le chapeau de ŷ et le θ ont été détruits ; la perte du bloc suivant compare deux arguments, donc une prédiction et une cible.",
  "Rendu : ŷ=f_θ(x)."),

 (1262, 1262, r"\[ L(\hat{y},y) \]", "haute",
  "§73 « On définit une fonction de perte : [L(y,y)] ». Les deux arguments sont identiques en apparence : le chapeau du premier a été détruit.",
  "Rendu : L(ŷ,y)."),

 (1266, 1266, r"\[ J(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i) \]", "haute",
  "§73 « Puis une fonction objectif : [ ] ». Résidu J() = 1n _{i=1}^{n} L(f_(x_i),y_i) : \\frac{1}{n} a laissé 1n (régime « contenu conservé »), \\sum a laissé \\_, le θ a disparu.",
  "Rendu : J(θ)=1/n Σ L(f_θ(x_i),y_i)."),

 (1270, 1270, r"\[ \theta^{*}=\arg\min_\theta J(\theta) \]", "haute",
  "§73 « L'entraînement cherche alors : [ ] ». Résidu ^\\* = \\_J() : l'étoile a survécu, \\arg\\min réduit à \\_.",
  "Rendu : θ*=argmin_θ J(θ)."),

 (1274, 1274, r"\[ \nabla_\theta J(\theta) \]", "haute",
  "§73 « Le calcul différentiel intervient pour calculer : [ ] ». \\nabla détruit.",
  "Rendu : ∇_θ J(θ)."),

 (1280, 1280, r"\[ f(x)\to f'(x)\to x-\eta f'(x) \]", "moyenne",
  "§74 « La chaîne centrale est : [f(x) f'(x) f(x)] ». Les flèches ont été détruites. Le troisième terme ne peut pas être f(x) tel quel : la chaîne va de la fonction à la dérivée puis à la mise à jour.",
  "Candidat alternatif : f(x) → f'(x) → min f(x). Le troisième terme reste à confirmer."),

 (1284, 1284, None, "inconnue",
  "§74 « Plus précisément : [vide] Cette boucle constitue l'une des structures mathématiques fondamentales du Machine Learning. » — la forme détaillée de la chaîne a disparu.",
  "Candidat : \\[ x_{k+1}=x_k-\\eta\\nabla f(x_k) \\] — mais c'est redondant avec l. 1280."),

 (1350, 1350, r"\[ \frac{dz}{dx}=\frac{dz}{dy}\frac{dy}{dx} \]", "haute",
  "§77 « Si z=f(y) et y=g(x), alors : [= ] ». Notation de Leibniz ; les variables sont celles des deux blocs précédents.",
  "Rendu : dz/dx = dz/dy · dy/dx."),

 (1392, 1392, r"\[ f'(x)\approx\frac{f(x+h)-f(x)}{h} \]", "haute",
  "§80 DIFFÉRENCE FINIE « Différence avant : [f'(x)] Différence centrée : [f'(x)] ». Les deux blocs sont identiques en apparence : le membre de droite a été détruit dans les deux.",
  "Rendu : f'(x)≈(f(x+h)−f(x))/h."),

 (1396, 1396, r"\[ f'(x)\approx\frac{f(x+h)-f(x-h)}{2h} \]", "haute",
  "§80 « Différence centrée : [ ] ». Même destruction ; la différence centrée est la seule formule qui distingue ce bloc du précédent.",
  "Rendu : f'(x)≈(f(x+h)−f(x−h))/2h."),

 (1404, 1404, r"\[ g_{\text{analytique}} \]", "moyenne",
  "§81 GRADIENT CHECKING « Pour tester une implémentation de gradient : [g_{}] est comparé à : [g_{}] ». Les deux indices ont été détruits ; la méthode compare le gradient analytique au gradient numérique.",
  "Candidat alternatif : g_{\\text{exact}}. À confirmer par l'auteur."),

 (1408, 1408, r"\[ g_{\text{numérique}} \]", "moyenne",
  "§81 « est comparé à : [g_{}] ». Pendant du bloc précédent.",
  "Candidat alternatif : g_{\\text{approx}}. À confirmer."),

 (1434, 1434, r"\[ f_n\circ f_{n-1}\circ\cdots\circ f_1 \]", "haute",
  "§83 VANISHING GRADIENT « Dans une longue composition : [ ] la règle de chaîne produit des produits de dérivées. » \\circ et \\cdots détruits.",
  "Rendu : f_n∘f_{n-1}∘⋯∘f_1."),

 (1440, 1440, r"\[ \prod_i a_i \]", "haute",
  "§83 « Si les facteurs sont souvent inférieurs à 1 : [ ] peut devenir extrêmement petit. » Le \\_ est le résidu de \\prod.",
  "Rendu : ∏ᵢ aᵢ."),

 (1452, 1452, r"\[ \prod_i a_i \]", "haute",
  "§84 EXPLODING GRADIENT « si les facteurs sont fréquemment supérieurs à 1 : [ ] peut devenir extrêmement grand. »",
  "Rendu : ∏ᵢ aᵢ."),

 (1470, 1470, r"\[ \sigma(x)=\frac{1}{1+e^{-x}} \]", "haute",
  "§85 SIGMOÏDE « Exemple : [ (x)= ] et : [ '(x)=...] ». Le \\sigma a été détruit ; la dérivée du bloc suivant, σ(1−σ), n'appartient qu'à la sigmoïde.",
  "Vérifier : σ(x)=1/(1+e^{−x}) ⇒ σ'=σ(1−σ)."),

 (1474, 1474, r"\[ \sigma'(x)=\sigma(x)(1-\sigma(x)) \]", "haute",
  "§85 « et : [ '(x)=(x)(1-(x)) ] La dérivée de l'activation participe directement à la backpropagation. »",
  "Dérivée de la sigmoïde."),

 (1482, 1482, r"\[ \text{ReLU}(x)=\max(0,x) \]", "haute",
  "§86 RELU « La fonction ReLU est : [ (x)=(0,x) ] ». Le \\max a été détruit, laissant ses arguments.",
  "Rendu : ReLU(x)=max(0,x)."),

 (1486, 1488, "\\[ \\text{ReLU}'(x)=\\begin{cases}0&\\text{si }x<0\\\\ 1&\\text{si }x>0\\end{cases} \\]", "haute",
  "§86 « Sa dérivée est : [trois lignes vides] Le point (x=0) nécessite une convention particulière. » — la mention du point 0 et le bloc sur trois lignes imposent une définition par cas.",
  "Rendu : ReLU'(x)=0 si x<0, 1 si x>0. La convention en 0 reste ouverte, comme le dit la phrase."),

 (1496, 1496, r"\[ \sigma(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}} \]", "haute",
  "§87 SOFTMAX « Pour des logits (z_i) : [ (z_i) = {\\_j e^{z_j}} ] ». Le résidu montre le dénominateur \\sum_j e^{z_j} (régime « contenu conservé ») et un numérateur détruit.",
  "Rendu : σ(z_i)=e^{z_i}/Σ_j e^{z_j}."),

 (1500, 1500, r"\[ \frac{\partial s_i}{\partial z_j}=s_i(\delta_{ij}-s_j) \]", "haute",
  "§87 « Sa Jacobienne est non diagonale : [ = s_i(\\_{ij}-s_j) ] ». Le \\delta a été détruit, le membre de gauche détruit avec \\frac et \\partial.",
  "Jacobienne du softmax : ∂s_i/∂z_j=s_i(δ_ij−s_j)."),

 (1510, 1510, r"\[ L=-\sum_i y_i\log p_i \]", "haute",
  "§88 « Dans la classification : [ L=-\\_i y_ip_i ] ». Le \\log entre le y_i et le p_i a été détruit ; sans lui, l'expression ne serait pas une cross-entropie.",
  "Rendu : L=−Σ y_i log p_i. C'est la cross-entropie annoncée par le §88."),

 (1514, 1514, r"\[ \nabla_z L=p-y \]", "moyenne",
  "§88 « on obtient par rapport aux logits une expression simplifiée liée à : [p-y] ». Le gradient par rapport aux logits est p−y ; le membre de gauche a été détruit.",
  "Résultat classique softmax + cross-entropie. Le membre de gauche reste à confirmer."),

 (1522, 1522, r"\[ f_\theta=f_L\circ f_{L-1}\circ\cdots\circ f_1 \]", "haute",
  "§89 « Un réseau peut être représenté comme : [ ] ». \\circ et \\cdots détruits.",
  "Rendu : f_θ=f_L∘f_{L-1}∘⋯∘f_1."),

 (1526, 1526, r"\[ \min_\theta J(\theta) \]", "haute",
  "§89 « L'entraînement cherche : [ ] ». \\min détruit.",
  "Rendu : min_θ J(θ)."),

 (1530, 1530, r"\[ \nabla_\theta J \]", "haute",
  "§89 « Le gradient : [ ] est calculé par différentiation de la composition. » \\nabla détruit.",
  "Rendu : ∇_θ J."),

 (1536, 1536, None, "inconnue",
  "§89 « Ainsi : [vide] » — conclusion de la section sur la composition différentiable. Aucun résidu.",
  "Candidat : \\nabla_\\theta J=J_{f_L}\\cdots J_{f_1} (produit de Jacobiennes). À confirmer."),

 (1564, 1564, r"\[ x_{\text{local}}\neq x_{\text{global}} \]", "moyenne",
  "§91 « En optimisation non convexe : [x_{} x_{}] ». Les deux indices ont été détruits ; \\neq aussi.",
  "Candidat alternatif : f(x_{\\text{local}})>f(x_{\\text{global}}). À confirmer."),

 (1578, 1578, r"\[ \|\nabla f(x)\| \]", "haute",
  "§93 PLATEAUX « Un plateau correspond à une région dans laquelle : [ ] est faible. » \\| et \\nabla détruits.",
  "Rendu : ‖∇f(x)‖."),

 (1614, 1614, r"\[ g_t\approx\nabla_\theta J(\theta_t) \]", "moyenne",
  "§96 « le gradient exact de l'objectif total est souvent remplacé par une estimation : [g_t J(\\_t)] ». L'estimateur g_t et le vrai gradient sont reliés par une approximation.",
  "Candidat alternatif : g_t=\\hat{\\nabla}_\\theta J(\\theta_t). À confirmer."),

 (1624, 1624, r"\[ J(w)=\sum_i(w^{T}x_i-y_i)^{2} \]", "haute",
  "§97 « Pour : [ J(w)=\\_i (w<sup>Tx_i-y_i)</sup>2 ] ». Le \\sum a laissé \\_ ; l'exposant 2 a été converti en balise <sup> qui englobe mal le reste.",
  "Rendu : J(w)=Σ(w^T x_i−y_i)²."),

 (1628, 1628, r"\[ \nabla J(w)=\frac{1}{n}X^{T}(Xw-y) \]", "haute",
  "§97 « on obtient : [ ] ». Résidu J(w)=1n X^T(Xw-y) : \\nabla détruit, \\frac{1}{n} réduit à 1n.",
  "Rendu : ∇J(w)=1/n X^T(Xw−y)."),

 (1632, 1632, r"\[ w_{t+1}=w_t-\eta\nabla J(w_t) \]", "haute",
  "§97 « La mise à jour devient : [ ] ». \\eta et \\nabla détruits.",
  "Rendu : w_{t+1}=w_t−η∇J(w_t)."),

 (1644, 1644, r"\[ R(\theta)=\|\theta\|_2^{2} \]", "haute",
  "§98 RÉGULARISATION L2 « Exemple L2 : [ R()=||\\_2^2 ] ». Le résidu || est la norme \\|…\\|₂, le θ a été détruit.",
  "Rendu : R(θ)=‖θ‖²₂."),

 (1648, 1648, r"\[ \nabla R(\theta)=2\theta \]", "haute",
  "§98 « Alors : [ R()=2 ] La régularisation influence donc directement le gradient. » \\nabla détruit ; le θ du membre de droite aussi.",
  "Vérifier : ∇‖θ‖²₂=2θ."),

 (1656, 1656, r"\[ \hat{y}=f_\theta(x) \]", "haute",
  "§99 « Pour un modèle : [ y=f_(x) ] ». Même reconstruction qu'en l. 1258.",
  "Rendu : ŷ=f_θ(x)."),

 (1660, 1660, r"\[ L(\hat{y},y) \]", "haute",
  "§99 « et une perte : [ L(y,y) ] ». Même reconstruction qu'en l. 1262.",
  "Rendu : L(ŷ,y)."),

 (1664, 1664, r"\[ \nabla_\theta L \]", "haute",
  "§99 « on cherche : [ ] La chaîne fondamentale est : ». \\nabla détruit.",
  "Rendu : ∇_θ L."),

 (1668, 1668, r"\[ \nabla_\theta L=\frac{\partial L}{\partial \hat{y}}\frac{\partial \hat{y}}{\partial \theta} \]", "moyenne",
  "§99 « La chaîne fondamentale est : [= ] Dans un réseau profond, cette relation se propage à travers toutes les couches. » — \\frac et \\partial détruits des deux côtés.",
  "Candidat alternatif : \\nabla_\\theta L=\\frac{\\partial L}{\\partial y}\\frac{\\partial y}{\\partial \\theta}. Notation de la cible à confirmer."),

 (1693, 1693, None, "inconnue",
  "§102 TENSEURS « Le principe reste le même : [vide] Chaque opération possède une règle de différentiation. » — aucun résidu.",
  "Candidat : \\text{différencier chaque opération élémentaire}. À confirmer."),

 (1735, 1735, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§104 « Pour : [ ] le gradient possède (n) composantes. » \\mathbb et \\to détruits.",
  "Rendu : f : ℝⁿ → ℝ."),

 (1753, 1753, r"\[ H\in\mathbb{R}^{n\times n} \]", "haute",
  "§105 « Si un modèle possède (n) paramètres : [H^{nn}] Le stockage naïf nécessite : [O(n²)] éléments. » — \\in, \\mathbb, \\times détruits ; les deux n ont survécu en exposant.",
  "Rendu : H ∈ ℝ^{n×n}."),

 (1814, 1814, r"\[ \nabla F \]", "haute",
  "§109 « Pour une surface implicite F(x,y,z)=0, le gradient : [F] est normal à la surface. » \\nabla détruit.",
  "Rendu : ∇F."),

 (1824, 1824, r"\[ \dot{x}=v \]", "haute",
  "§110 SIMULATION PHYSIQUE « Une dynamique peut être décrite par : [=v] et : [=a] ». Le point sur x a été détruit (notation newtonienne).",
  "Rendu : ẋ=v."),

 (1828, 1828, r"\[ \dot{v}=a \]", "haute",
  "§110 « et : [=a] ». Même destruction.",
  "Rendu : v̇=a."),

 (1844, 1844, r"\[ \frac{dx}{dt}=f(x,t) \]", "haute",
  "§111 « Une équation différentielle relie une fonction à ses dérivées. Exemple : [=f(x,t)] ». \\frac détruit.",
  "Rendu : dx/dt=f(x,t)."),

 (1887, 1887, r"\[ \pi_\theta(a|s) \]", "haute",
  "§114 REINFORCEMENT LEARNING « Une politique peut être paramétrée par : [\\_(a|s)] ». Le \\_ est le résidu d'une lettre grecque indicée — \\pi_\\theta, la politique.",
  "Rendu : π_θ(a|s)."),

 (1895, 1895, r"\[ \max_\theta J(\theta) \]", "haute",
  "§114 « On cherche : [ ] ». \\max détruit.",
  "Rendu : max_θ J(θ)."),

 (1903, 1903, r"\[ p_\theta(x) \]", "haute",
  "§115 « Dans les modèles probabilistes : [p_(x)] dépend de paramètres. » Le θ a été détruit.",
  "Rendu : p_θ(x)."),

 (1909, 1909, r"\[ \nabla_\theta\log p_\theta(x) \]", "moyenne",
  "§115 « On peut chercher : [_p_(x)] Cette quantité apparaît dans : - maximum de vraisemblance ; … ». Le \\log a été détruit ; la liste qui suit (score function, vraisemblance) désigne le gradient du log.",
  "Candidat alternatif : \\nabla_\\theta p_\\theta(x). Le contexte penche pour le gradient du log."),

 (1923, 1923, r"\[ \theta^{*}=\arg\max_\theta \mathcal{L}(\theta) \]", "haute",
  "§116 « Le maximum de vraisemblance cherche : [ ^\\* = _ L() ] ». \\arg\\max réduit à \\_ ; \\mathcal{L} détruit.",
  "Rendu : θ*=argmax_θ 𝓛(θ)."),

 (1927, 1927, r"\[ \theta^{*}=\arg\min_\theta -\mathcal{L}(\theta) \]", "haute",
  "§116 « ou : [ ^\\* = _ -L() ] ». Le signe moins a survécu : c'est la minimisation de la négative.",
  "Équivalent au maximum de vraisemblance."),

 (1933, 1933, None, "inconnue",
  "§116 « Ainsi : [vide] » — conclusion du maximum de vraisemblance. Aucun résidu.",
  "Candidat : \\text{le gradient permet de remonter à l'optimum}. À confirmer."),

 (1939, 1939, r"\[ \nabla_\theta\,\mathbb{E}_{x\sim p_\theta}\left[f_\theta(x)\right] \]", "haute",
  "§117 GRADIENT D'UNE ESPÉRANCE « on doit différencier : [ {xp_} \\[f_(x)\\] ] ». Le résidu montre l'espérance sous p_θ (le \\sim et le \\nabla détruits) et l'intérieur f_θ(x). Les crochets échappés \\[ \\] sont un artefact, pas une seconde équation.",
  "Rendu : ∇_θ 𝔼_{x∼p_θ}[f_θ(x)]. Le §117 renvoie à la score function et au reparamétrage."),

 (1952, 1952, r"\[ z=g(\theta,\epsilon) \]", "haute",
  "§118 REPARAMÉTRISATION « réécrire une variable aléatoire dépendant de (θ) sous la forme : [ z=g(,) ] ». Les deux lettres grecques θ et ε ont été détruites, la virgule est restée.",
  "Rendu : z=g(θ,ε)."),

 (1977, 1977, r"\[ \Delta x\to 0 \]", "moyenne",
  "§120 « Il décrit ce qui se passe lorsque : [x] ». Le \\Delta et la flèche ont été détruits ; le calcul différentiel est local, donc la variation tend vers zéro.",
  "Candidat alternatif : x\\to x+\\Delta x. À confirmer."),

 (1985, 1985, r"\[ \nabla f(x) \]", "haute",
  "§121 « Une information différentielle : [ ] décrit le comportement autour de (x). » \\nabla détruit.",
  "Rendu : ∇f(x)."),

 (1991, 1991, None, "inconnue",
  "§121 « Elle ne garantit pas automatiquement : [= ] Pour obtenir des garanties globales, il faut exploiter des structures supplémentaires : - convexité ; … ». La liste qui suit indique de quelles garanties il s'agit, mais le bloc est vide.",
  "Candidat : \\text{un minimum global}. À confirmer."),

 (2004, 2004, r"\[ \nabla f(x^{*})=0 \]", "haute",
  "§122 STATIONNARITÉ « Une condition fondamentale d'optimalité intérieure est : [ ] ». \\nabla détruit.",
  "Rendu : ∇f(x*)=0."),

 (2032, 2032, r"\[ \theta_{t+1}=\theta_t-\eta_t\nabla_\theta J(\theta_t) \]", "haute",
  "§123 « Mathématiquement : [ \\_{t+1}=\\_t-_t_J(\\_t) ] ». Le \\eta_t et le \\nabla_\\theta ont été détruits ; le signe moins est réel.",
  "Rendu : θ_{t+1}=θ_t−η_t∇_θ J(θ_t)."),

 (2038, 2038, r"\[ \|\nabla J(\theta)\|<\epsilon \]", "haute",
  "§124 CRITÈRES D'ARRÊT « Une optimisation peut être arrêtée lorsque : [ |J()|< ] ». \\|, \\nabla détruits ; \\epsilon détruit.",
  "Rendu : ‖∇J(θ)‖<ε."),

 (2042, 2042, r"\[ |J_{t+1}-J_t|<\epsilon \]", "haute",
  "§124 « ou lorsque : [ |J_{t+1}-J_t|< ] ». Seul \\epsilon manque.",
  "Rendu : |J_{t+1}−J_t|<ε."),

 (2056, 2056, r"\[ x_k\to x^{*} \]", "haute",
  "§125 CONVERGENCE « Une suite (x_k) converge vers (x*) si : [ ] ». \\to détruit.",
  "Rendu : x_k → x*."),

 (2124, 2124, None, "inconnue",
  "§130 CHECKPOINTING « On échange donc : [vide] ». Le compromis mémoire/calcul est décrit en prose autour du bloc.",
  "Candidat : \\text{de la mémoire contre du calcul}. À confirmer."),

 (2145, 2145, r"\[ \log\sum_i e^{x_i} \]", "haute",
  "§132 LOG-SUM-EXP « Pour calculer : [\\_i e^{x_i}] de manière stable ». Le \\log a été détruit ; la section entière porte sur la stabilité du logarithme d'une somme d'exponentielles.",
  "Rendu : log Σᵢ e^{xᵢ}."),

 (2149, 2149, r"\[ m+\log\sum_i e^{x_i-m} \]", "haute",
  "§132 « on utilise généralement : [ m+\\_i e^{x_i-m} ] ». Même destruction du \\log.",
  "Astuce du max : log Σ e^{x_i} = m + log Σ e^{x_i−m}."),

 (2153, 2153, r"\[ m=\max_i x_i \]", "haute",
  "§132 « avec : [ m=\\_i x_i ] ». Le \\_ est ici le résidu de \\max.",
  "Rendu : m=maxᵢ xᵢ."),

 (2163, 2163, r"\[ g\gets \frac{c\,g}{\|g\|} \]", "haute",
  "§133 GRADIENT CLIPPING « on peut limiter leur norme. Par exemple : [g g] lorsque : [‖g‖>c] ». Le \\gets (ou \\leftarrow) et \\frac ont été détruits.",
  "Rendu : g ← cg/‖g‖. C'est le clipping par la norme."),

 (2167, 2167, r"\[ \|g\|>c \]", "haute",
  "§133 « lorsque : [ |g|>c ] ». \\| détruit.",
  "Rendu : ‖g‖>c."),

 (2217, 2217, r"\[ f'(x)\approx\frac{f(x+h)-f(x)}{h} \]", "haute",
  "§136 « Exemple : [f'(x)] Elle est simple mais sujette aux erreurs numériques. » Même reconstruction qu'en l. 1392.",
  "Rendu : f'(x)≈(f(x+h)−f(x))/h."),

 (2252, 2252, r"\[ \nabla f(x) \]", "haute",
  "§139 « Exemple : [ ] est un vecteur. » — le gradient est le vecteur, la Jacobienne la matrice (blocs suivants). \\nabla détruit.",
  "Rendu : ∇f(x)."),

 (2283, 2283, r"\[ \nabla_\theta p_\theta(x) \]", "moyenne",
  "§140 « On différencie : [p_(x)] ou : [p_(x)] pour effectuer de l'estimation et de l'optimisation. » Les deux blocs sont identiques en apparence ; la conjonction « ou » les distingue.",
  "Candidat alternatif : \\frac{\\partial}{\\partial\\theta}p_\\theta(x). À confirmer."),

 (2287, 2287, r"\[ \nabla_\theta\log p_\theta(x) \]", "moyenne",
  "§140 second bloc. Le « ou » suggère l'alternative usuelle : la dérivée de la densité ou celle de son logarithme.",
  "Candidat alternatif : \\nabla_\\theta \\log \\mathcal{L}(\\theta). À confirmer."),

 (2461, 2461, r"\[ \sqrt{x} \]", "moyenne",
  "§154 « Exemples : [x²] [x] [e^x] ». Le nom de la fonction médiane a été détruit ; entre x² et e^x, la racine carrée est l'exemple canonique de dérivée non entière.",
  "Candidat alternatif : \\sin x ou \\ln x. À confirmer."),

 (2490, 2490, r"\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]", "haute",
  "§156 PROJET 2 « Implémenter : [ ] sur plusieurs fonctions. » \\eta et \\nabla détruits.",
  "Rendu : x_{t+1}=x_t−η∇f(x_t)."),

 (2514, 2514, r"\[ J(w,b)=\frac{1}{n}\sum_i(\hat{y}_i-y_i)^{2} \]", "haute",
  "§157 « avec : [ J(w,b)=1n \\_i (y_i-y_i)^2 ] ». Les deux arguments sont identiques en apparence : le chapeau du premier a été détruit.",
  "Rendu : J(w,b)=1/n Σ(ŷ_i−y_i)²."),

 (2518, 2518, r"\[ \nabla_w J \]", "haute",
  "§157 « Puis calculer manuellement : [ ] ». \\nabla détruit.",
  "Rendu : ∇_w J."),

 (2522, 2522, r"\[ \nabla_b J \]", "haute",
  "§157 « et : [vide] ». Pendant du bloc précédent, pour le biais.",
  "Rendu : ∇_b J."),

 (2596, 2596, r"\[ \ln x \]", "moyenne",
  "§162 EXERCICES NIVEAU 1 « Être capable de dériver sans assistance : [x^n] [e^x] [x] [x] [x] ainsi que des compositions et produits. » Cinq fonctions ; les trois dernières ont perdu leur nom.",
  "Candidat : ln x. Alternatives : \\sin x, \\cos x — voir les blocs suivants."),

 (2598, 2598, r"\[ \sin x \]", "moyenne",
  "§162, quatrième fonction de la liste.",
  "Candidat. L'ordre {ln, sin, cos} reprend celui de la section 12."),

 (2600, 2600, r"\[ \cos x \]", "moyenne",
  "§162, cinquième fonction de la liste.",
  "Candidat. À confirmer ; \\tan x est une alternative."),

 (2608, 2608, r"\[ \nabla f(x,y) \]", "haute",
  "§163 EXERCICES NIVEAU 2 « Calculer : [ ] pour plusieurs fonctions. » \\nabla détruit.",
  "Rendu : ∇f(x,y)."),

 (2622, 2622, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§164 « Pour une fonction : [ ] être capable d'expliquer : ». \\mathbb et \\to détruits.",
  "Rendu : f : ℝⁿ → ℝ."),

 (2640, 2640, r"\[ \frac{dL}{dx} \]", "moyenne",
  "§165 « Pour une fonction composée L=f_3(f_2(f_1(x))), calculer : [vide] manuellement par la règle de chaîne. »",
  "Candidat alternatif : \\frac{\\partial L}{\\partial x}. À confirmer."),

 (2650, 2650, r"\[ a=\sigma(z) \]", "haute",
  "§166 « Prendre un neurone : z=wx+b, [a=(z)], L=(a−y)² ». \\sigma détruit.",
  "Rendu : a=σ(z)."),

 (2656, 2656, r"\[ \frac{\partial L}{\partial w} \]", "moyenne",
  "§166 « et calculer : [vide] manuellement. » — la dérivée de la perte par rapport au poids.",
  "Candidat alternatif : \\frac{\\partial L}{\\partial \\theta}. À confirmer."),

 (2686, 2686, r"\[ \nabla f=0 \]", "haute",
  "§168 Défi 4 « Expliquer pourquoi : [f=0] ne signifie pas nécessairement minimum. » \\nabla détruit.",
  "Rendu : ∇f=0."),

 (2858, 2858, r"\[ f:\mathbb{R}\to\mathbb{R} \]", "haute",
  "§172 LES QUATRE OBJETS « ### Dérivée — Pour une fonction : [ ] on obtient : [f'(x)] ». \\mathbb et \\to détruits.",
  "Rendu : f : ℝ → ℝ."),

 (2872, 2872, r"\[ \nabla f(x) \]", "haute",
  "§172 « ### Gradient — Pour : [f:^n] on obtient : [f(x)] ». \\nabla détruit.",
  "Rendu : ∇f(x)."),

 (2878, 2878, r"\[ F:\mathbb{R}^{n}\to\mathbb{R}^{m} \]", "haute",
  "§172 « ### Jacobienne — Pour : [F:<sup>n</sup>m] on obtient : [J_F(x)] ».",
  "Rendu : F : ℝⁿ → ℝᵐ."),

 (2888, 2888, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§172 « ### Hessienne — Pour : [ ] on obtient : [H_f(x)] ».",
  "Rendu : f : ℝⁿ → ℝ."),

 (2932, 2934, "\\[ \\theta_{t+1}=\\theta_t\n\n- \\eta_t\\nabla_\\theta J(\\theta_t) \\]", "haute",
  "§173 LA GRANDE CHAÎNE DU ML « Mathématiquement : [ ] C'est l'une des équations les plus importantes à comprendre pour le Machine Learning. » — le \\theta, le \\eta_t et le \\nabla_\\theta ont été détruits.",
  "Rendu : θ_{t+1}=θ_t−η_t∇_θ J(θ_t). Identique à l. 2032, ce qui confirme."),

 (2958, 2958, None, "inconnue",
  "§174 « La backpropagation peut donc être comprise comme : [vide] ». La chaîne ASCII qui précède (Paramètres → Opérations → Sortie → Loss → Dérivée locale → Règle de chaîne → Gradient → Paramètres) est intacte ; le bloc mathématique qui la résume est vide.",
  "Candidat : \\frac{\\partial L}{\\partial\\theta}=\\frac{\\partial L}{\\partial a}\\cdot\\frac{\\partial a}{\\partial z}\\cdot\\frac{\\partial z}{\\partial\\theta}."),

 (2980, 2980, r"\[ \nabla f=0 \]", "haute",
  "§175 Erreur 2 « Un point selle peut avoir : [f=0] ». \\nabla détruit.",
  "Rendu : ∇f=0."),

 (2986, 2986, r"\[ \nabla f \]", "haute",
  "§175 Erreur 3 « Confondre : [f] et : [J_f] ». Le premier est le gradient, le second la Jacobienne ; \\nabla détruit.",
  "Rendu : ∇f opposé à J_f."),

 (3121, 3121, r"\[ f(x)\to f'(x) \]", "haute",
  "§180 SYNTHÈSE FINALE « À une variable : [f(x) f'(x)] ». Les flèches ont été détruites ; la structure « objet → objet » est celle de toute la section.",
  "Rendu : f(x) → f'(x)."),

 (3125, 3125, r"\[ f(x)\to \nabla f(x) \]", "haute",
  "§180 « À plusieurs variables : [f(x) f(x)] ». Les deux termes sont identiques en apparence : le \\nabla du second a été détruit.",
  "Rendu : f(x) → ∇f(x)."),

 (3129, 3129, r"\[ F(x)\to J_F(x) \]", "haute",
  "§180 « Pour une transformation vectorielle : [ ] ». Les termes sont intacts, la flèche a été détruite.",
  "Rendu : F(x) → J_F(x)."),

 (3133, 3133, r"\[ f(x)\to H_f(x) \]", "haute",
  "§180 « Pour la courbure : [ ] ». Même structure.",
  "Rendu : f(x) → H_f(x)."),

 (3137, 3137, r"\[ f(x)\to x-\eta\nabla f(x) \]", "haute",
  "§180 « Pour l'optimisation : [f(x) x-f(x)] ». Le troisième terme montre le \\eta détruit et le \\nabla détruit ; le signe moins a survécu.",
  "Rendu : f(x) → x−η∇f(x). Cohérent avec l. 984."),

 (3141, 3141, None, "inconnue",
  "§180 « Pour les réseaux neuronaux : [vide] ». Les quatre blocs suivants suivent le même motif « objet → objet » et sont tous vides.",
  "Candidat : \\[ L\\to\\nabla_\\theta L \\] (la perte vers le gradient par backpropagation)."),

 (3145, 3145, None, "inconnue",
  "§180 « Pour le Machine Learning : [vide] ».",
  "Candidat : \\[ J(\\theta)\\to\\theta_{t+1}=\\theta_t-\\eta\\nabla_\\theta J(\\theta_t) \\]."),

 (3149, 3149, None, "inconnue",
  "§180 « Pour la simulation : [vide] ».",
  "Candidat : \\[ x(t)\\to\\dot{x}=f(x,t) \\], en écho au §110."),

 (3153, 3153, None, "inconnue",
  "§180 « Pour la computer graphics : [vide] ».",
  "Candidat : \\[ F(x,y,z)\\to\\nabla F \\], la normale d'une surface implicite (§109)."),

 (3161, 3161, None, "inconnue",
  "§180 « Le domaine I constitue ainsi le pont mathématique direct entre : [vide] ».",
  "Candidat : \\text{les fonctions et leur optimisation}. À confirmer."),

 (3165, 3165, None, "inconnue",
  "§180 « et, plus largement : [vide] ».",
  "Candidat : \\text{l'apprentissage automatique}. À confirmer."),

 (3175, 3175, None, "inconnue",
  "FIN DU DOCUMENT « **Noyau absolument fondamental :** [vide] ».",
  "Candidat : \\[ f\\to f'\\to\\nabla\\to H \\] — la chaîne qui résume tout le document."),
]

# Blocs vides des sections de synthese : meme traitement que ci-dessus.
SYNTHESE = [
 (2838, "§171 CE QU'IL FAUT ABSOLUMENT RETENIR, premier des quatre blocs (« doit contenir : »)",
  "dérivée", "la dérivée, puis le gradient, puis la règle de chaîne, puis l'optimisation — les quatre piliers du document"),
 (2842, "§171, deuxième bloc (« puis : »)", "gradient", "ordre proposé : dérivée → gradient → chaîne → optimisation"),
 (2846, "§171, troisième bloc (« puis : »)", "règle de chaîne", "ordre proposé"),
 (2850, "§171, quatrième bloc (« et enfin : »)", "optimisation", "ordre proposé"),
 (3016, "§176 Niveau 1 — Calcul différentiel", r"\[ f'(x) \]", "l'objet du niveau 1 est la dérivée"),
 (3020, "§176 Niveau 2 — Optimisation", r"\[ \min_x f(x) \]", "l'objet du niveau 2 est la minimisation"),
 (3024, "§176 Niveau 3 — Apprentissage", r"\[ \min_\theta J(\theta) \]", "l'objet du niveau 3 est la minimisation du risque empirique"),
 (3056, "§178 Probabilités", r"\[ p_\theta(x) \]", "cf. §115"),
 (3060, "§178 Statistiques", r"\[ \theta^{*}=\arg\max_\theta \mathcal{L}(\theta) \]", "cf. §116"),
 (3064, "§178 Calcul différentiel", r"\[ \nabla_\theta J(\theta) \]", "cf. §73"),
 (3068, "§178 En Machine Learning", r"\[ \theta_{t+1}=\theta_t-\eta\nabla_\theta J(\theta_t) \]", "cf. §123 et §173"),
 (3117, "§180 « Son idée fondamentale est : »", r"\[ \text{mesurer la variation locale} \]", "reprend le paragraphe de conclusion, qui parle de « mesurer comment un système change localement »"),
]


def main():
    lignes = open(f"{RACINE}/{SOURCE}", encoding="utf-8").read().split("\n")
    out = []
    for deb, fin, nouveau, conf, justif, valid in E:
        out.append({
            "fichier": SOURCE, "ligne": deb,
            "ancien": "\n".join(lignes[deb - 1:fin]),
            "nouveau": nouveau, "confiance": conf,
            "justification": justif, "validation": valid,
        })
    for deb, contexte, candidat, pourquoi in SYNTHESE:
        out.append({
            "fichier": SOURCE, "ligne": deb,
            "ancien": lignes[deb - 1], "nouveau": None, "confiance": "inconnue",
            "justification": f"{contexte}. Bloc vide, aucun résidu.",
            "validation": f"Candidat : {candidat} — {pourquoi}.",
        })
    out.sort(key=lambda e: e["ligne"])
    json.dump(out, open(SORTIE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    c = Counter(e["confiance"] for e in out)
    print(f"{len(out)} entrees -> {SORTIE}  {dict(c)}")
    print(f"applicables : {sum(1 for e in out if e['nouveau'])}")


if __name__ == "__main__":
    main()
