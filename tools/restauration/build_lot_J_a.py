#!/usr/bin/env python3
"""Construction du lot 5a : domaine J — Optimisation, sections introductives a 46
(lignes 17 a 1018).

Voir build_lot_I_a.py pour le format. Les entrees "inconnue" portent un candidat
dans le champ `validation`.

Ressource du document : la section 112 « FORMES IMPORTANTES A RECONNAITRE »
(lignes 2237 a 2287) est INTACTE — elle donnera les reperes du lot 5b.
"""

import json
from collections import Counter

SOURCE = "Maths-vers-Informatiques/Domaine J — Optimisation.md"
RACINE = "/home/user/_audit/connaissance"
SORTIE = "docs/restauration/propositions/domaine-J-lot5a.patch.json"

E = [
 (17, 17, None, "inconnue",
  "Introduction « permettant de chercher la meilleure solution possible selon : [vide] ou [vide] ». Deux blocs vides, aucun résidu.",
  "Candidats : \\[ \\text{un objectif} \\] puis \\[ \\text{des contraintes} \\] — les deux piliers nommés partout dans le document."),

 (21, 21, None, "inconnue",
  "Introduction, pendant du bloc précédent.", "Voir l. 17."),

 (41, 41, r"\[ \text{les mathématiques} \to \text{l'optimisation} \]", "moyenne",
  "§1 PLACE DE L'OPTIMISATION « On peut représenter une partie de la chaîne ainsi : » suivi de six blocs vides (l. 41, 45, 47, 49, 51, 53), puis « Ainsi, le Domaine J n'est pas isolé. ». C'est une chaîne de domaines.",
  "Candidat d'ouverture. La chaîne complète est à reconstituer par l'auteur : six terms, dont le dernier conduit à l'optimisation."),

 (45, 45, None, "inconnue", "§1, deuxième maillon de la chaîne (six blocs vides, l. 41 à 53).", "Voir l. 41."),
 (47, 47, None, "inconnue", "§1, troisième maillon.", "Voir l. 41."),
 (49, 49, None, "inconnue", "§1, quatrième maillon.", "Voir l. 41."),
 (51, 51, None, "inconnue", "§1, cinquième maillon.", "Voir l. 41."),
 (53, 53, None, "inconnue", "§1, sixième maillon.", "Voir l. 41."),

 (69, 69, r"\[ \theta^{*}=\arg\min_\theta \mathcal{L}(\theta) \]", "haute",
  "§2 Machine learning « Chercher les paramètres d'un modèle qui minimisent l'erreur : [ ] ». Le \\theta et le \\mathcal{L} ont été détruits ; \\arg\\min réduit à \\_.",
  "Rendu : θ*=argmin_θ 𝓛(θ)."),

 (75, 75, r"\[ P^{*}=\arg\min_P C(P) \]", "haute",
  "§2 Réseaux « Chercher le chemin minimisant le coût : [P^\\*=\\_P (P)] ». Le \\min et le C ont été détruits.",
  "Rendu : P*=argmin_P C(P)."),

 (81, 83, None, "inconnue",
  "§2 Logistique « Minimiser : [trois lignes, dont une puce -] ». Le bloc contenait une liste, presque certainement une somme de coûts.",
  "Candidat : \\[ \\sum_{i,j} c_{ij}x_{ij} \\] — les coûts de transport. La puce conservée montre au moins deux items."),

 (89, 89, None, "inconnue",
  "§2 Scheduling « Minimiser : [vide] ou : [vide] ». Deux blocs vides.",
  "Candidats : \\[ \\text{le temps total} \\] puis \\[ \\text{le retard} \\] — cf. §79 (l. 1560) qui parle du temps de fin global."),

 (93, 93, None, "inconnue", "§2 Scheduling, pendant du bloc précédent.", "Voir l. 89."),

 (99, 99, r"\[ \theta^{*}=\arg\min_\theta J(\theta) \]", "haute",
  "§2 Robotique « Chercher une trajectoire : [^\\*=_ J()] ». Le \\theta a été détruit, \\arg\\min réduit à \\_.",
  "Rendu : θ*=argmin_θ J(θ)."),

 (121, 121, r"\[ x=(x_1,x_2,\ldots,x_n) \]", "haute",
  "§3.1 variable de décision « Exemple : [x=(x_1,x_2,,x_n)] ». Le \\ldots est devenu une virgule.",
  "Rendu : x=(x₁,x₂,…,x_n)."),

 (135, 135, r"\[ \min_x C(x) \]", "haute",
  "§3.3 fonction de coût. Le \\_ est le résidu de \\min.",
  "Rendu : min_x C(x)."),

 (141, 141, r"\[ L(\theta) \]", "haute",
  "§3.4 fonction de perte « En machine learning : [L()] mesure l'écart entre les prédictions et les observations. » Le \\theta a été détruit.",
  "Rendu : L(θ)."),

 (151, 151, r"\[ x_1+x_2\leq b \]", "moyenne",
  "§3.5 contrainte « Condition que la solution doit respecter. Exemple : [x_1+x_2] ». L'inégalité et la borne ont été détruites : il ne reste qu'une somme, ce qui n'est pas une contrainte.",
  "Candidat alternatif : x_1+x_2\\leq 10 (la borne 10 est celle de l'exemple d'égalité du §14)."),

 (157, 157, r"\[ \mathcal{X}=\{x: g_i(x)\leq 0,\ h_j(x)=0\} \]", "haute",
  "§3.6 domaine admissible « Ensemble des solutions satisfaisant toutes les contraintes : [ = {x : g_i(x), h_j(x)=0}] ». Le \\mathcal{X} a été détruit, ainsi que l'inégalité de g_i. La virgule entre les deux conditions est restée.",
  "Rendu : 𝓧={x : g_i(x)≤0, h_j(x)=0}."),

 (181, 181, r"\[ f(\lambda x+(1-\lambda)y)\leq \lambda f(x)+(1-\lambda)f(y) \]", "haute",
  "§3.11 « Pour une fonction convexe : [f(x+(1-)y) f(x)+(1-)f(y)] pour : [0] ». Les deux \\lambda et le \\leq ont été détruits.",
  "Définition de la convexité. Le bloc suivant donne l'intervalle de λ."),

 (185, 185, r"\[ \lambda\in[0,1] \]", "haute",
  "§3.11 « pour : [0] ». Le \\lambda, le \\in et le crochet droit ont été détruits ; le 0 est le résidu de la borne inférieure.",
  "Rendu : λ∈[0,1]."),

 (203, 203, r"\[ \min_x f(x) \]", "haute",
  "§4 « La forme générale peut être écrite : [vide] sous : [g_i(x)] et : [h_j(x)=0] ». Le premier bloc est vide ; les deux suivants donnent les contraintes, donc le premier est l'objectif.",
  "Rendu : min_x f(x). Confirmé par les blocs suivants."),

 (207, 207, r"\[ g_i(x)\leq 0 \]", "haute",
  "§4 « sous : [g_i(x)] ». L'inégalité a été détruite, comme partout dans ce document (l. 433, 515, 542).",
  "Rendu : g_i(x)≤0."),

 (215, 215, r"\[ \min_x f(x) \]", "moyenne",
  "§4 « On peut donc avoir : [vide] Cette formulation est fondamentale. » — après l'énoncé objectif + contraintes. Le bloc résume probablement la forme complète.",
  "Candidat alternatif : \\[ \\min_{x\\in\\mathcal{X}}f(x) \\]."),

 (227, 227, r"\[ f(x^{*})\leq f(x) \]", "haute",
  "§5.1 minimum global « Un point (x*) est un minimum global si : [ ] pour tout (x) admissible. » \\leq détruit.",
  "Rendu : f(x*)≤f(x)."),

 (235, 235, r"\[ f(x^{*})\geq f(x) \]", "haute",
  "§5.2 maximum global. \\geq détruit ; le minimum et le maximum ne se distinguent plus visuellement.",
  "Rendu : f(x*)≥f(x)."),

 (243, 243, r"\[ \max_x f(x) \]", "haute",
  "§5.3 « Un problème : [\\_x f(x)] peut être transformé en : [\\_x -f(x)] ». Le premier est un maximum, comme l'indique la transformation qui suit.",
  "Rendu : max_x f(x)."),

 (247, 247, r"\[ \min_x -f(x) \]", "haute",
  "§5.3 « peut être transformé en : [ ] ». Le signe moins a survécu, ce qui tranche sans ambiguïté.",
  "max f ≡ min −f."),

 (257, 257, r"\[ f(x^{*})\leq f(x) \]", "haute",
  "§6.1 minimum local. \\leq détruit.", "Rendu : f(x*)≤f(x) dans le voisinage."),

 (263, 263, r"\[ f(x^{*})\leq f(x) \]", "haute",
  "§6.2 minimum global. \\leq détruit.", "Rendu : f(x*)≤f(x) pour tout x admissible."),

 (271, 271, r"\[ x_{\text{local}}^{*} \]", "haute",
  "§6.3 « Une méthode peut trouver : [x_{}^\\*] sans trouver : [x_{}^\\*] ». Les deux indices ont été détruits ; le premier est le minimum local.",
  "Rendu : x*_local."),

 (275, 275, r"\[ x_{\text{global}}^{*} \]", "haute",
  "§6.3, pendant du bloc précédent.", "Rendu : x*_global."),

 (292, 292, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§7 « Pour une fonction différentiable : [f:^n] ». \\mathbb et \\to détruits.",
  "Rendu : f : ℝⁿ → ℝ."),

 (296, 296, r"\[ \nabla f(x^{*})=0 \]", "haute",
  "§7 « un optimum intérieur peut satisfaire : [vide] Cela signifie que toutes les dérivées partielles sont nulles : [ ] ». Le premier bloc est vide ; la phrase qui suit le décrit exactement.",
  "Condition de stationnarité. Le bloc suivant explicite les dérivées partielles."),

 (300, 300, r"\[ \frac{\partial f}{\partial x_1}=0,\ \ldots,\ \frac{\partial f}{\partial x_n}=0 \]", "haute",
  "§7 « Cela signifie que toutes les dérivées partielles sont nulles : [=0, , =0] ». Le résidu montre deux « =0 » encadrant une virgule — le \\ldots est devenu une virgule, les \\frac et \\partial ont disparu.",
  "Rendu : ∂f/∂x₁=0, …, ∂f/∂x_n=0."),

 (304, 304, r"\[ \nabla f(x)=0 \]", "haute",
  "§7 « Attention : [f(x)=0] ne signifie pas nécessairement que (x) est un minimum. » \\nabla détruit.",
  "Rendu : ∇f(x)=0."),

 (319, 319, r"\[ H_f(x)=\nabla^{2}f(x) \]", "haute",
  "§8 « La Hessienne : [H_f(x)=^2 f(x)] permet d'étudier la courbure locale. » Le \\nabla a été détruit.",
  "Rendu : H_f(x)=∇²f(x)."),

 (327, 327, r"\[ \nabla^{2}f(x^{*})\succ 0 \]", "haute",
  "§8 « ### Hessienne définie positive [H_f(x^\\*)] → minimum local strict. » \\nabla^2 et \\succ détruits.",
  "Rendu : ∇²f(x*)≻0."),

 (333, 333, r"\[ \nabla^{2}f(x^{*})\prec 0 \]", "haute",
  "§8 « ### Hessienne définie négative [ ] → maximum local strict. »",
  "Rendu : ∇²f(x*)≺0."),

 (351, 351, r"\[ f(\lambda x+(1-\lambda)y)\leq \lambda f(x)+(1-\lambda)f(y) \]", "haute",
  "§9 « Une fonction convexe satisfait : [ ] ». Deux \\lambda et un \\leq détruits.",
  "Définition de la convexité, identique à la l. 181."),

 (357, 357, r"\[ \min_x f(x) \]", "haute",
  "§9.1 « Dans un problème de minimisation convexe : [\\_x f(x)] tout minimum local est également un minimum global. »",
  "Rendu : min_x f(x)."),

 (369, 369, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§10 « Pour une fonction deux fois différentiable : [ ] ». \\mathbb et \\to détruits.",
  "Rendu : f : ℝⁿ → ℝ."),

 (373, 373, r"\[ \nabla^{2}f(x)\succeq 0 \]", "haute",
  "§10 « une condition classique de convexité est : [vide] pour tout (x). Autrement dit, la Hessienne est semi-définie positive partout. » — la phrase qui suit décrit exactement le bloc.",
  "Rendu : ∇²f(x)⪰0."),

 (381, 381, r"\[ \nabla^{2}f(x)\succ 0 \]", "haute",
  "§10 « Pour une convexité stricte, on recherche des conditions plus fortes, typiquement : [^2 f(x)] ». Le \\nabla a été détruit.",
  "Rendu : ∇²f(x)≻0."),

 (391, 391, r"\[ f(x)\ \text{convexe} \]", "moyenne",
  "§11 « ## Problème convexe / Structure favorable : [f(x)] avec : - contraintes appropriées. » Le bloc ne porte que sur f(x) : il qualifiait la fonction.",
  "Candidat alternatif : \\[ \\min_x f(x) \\]."),

 (403, 405, None, "inconnue",
  "§11 « ## Problème non convexe / Le paysage peut contenir : [trois lignes, dont une puce -] ». Liste détruite.",
  "Candidat : \\[ \\text{plusieurs minima locaux} \\] et \\[ \\text{des points selles} \\] — cf. §6.3 et §91 du domaine I."),

 (413, 413, r"\[ \min_x f(x) \]", "haute",
  "§12 optimisation sans contraintes « Forme : [vide] sans restriction supplémentaire. Exemple : [f(x)=x²]. »",
  "Rendu : min_x f(x)."),

 (429, 429, r"\[ \min_x f(x) \]", "haute",
  "§13 optimisation sous contraintes « Forme : [\\_x f(x)] sous : [g_i(x)] et : [h_j(x)=0]. »",
  "Rendu : min_x f(x)."),

 (433, 433, r"\[ g_i(x)\leq 0 \]", "haute",
  "§13 « sous : [ ] ». L'inégalité a été détruite.",
  "Rendu : g_i(x)≤0."),

 (465, 465, r"\[ x+y\leq 10 \]", "haute",
  "§15 contraintes d'inégalité « Exemple : [x+y] ou : [x] ou : [0x] ». Le premier est la contrainte d'inégalité ; la borne 10 est celle de l'exemple du §14.",
  "Rendu : x+y≤10."),

 (469, 469, r"\[ x\geq 0 \]", "haute",
  "§15 « ou : [x] ». \\geq détruit.",
  "Rendu : x≥0."),

 (473, 473, r"\[ 0\leq x\leq 1 \]", "haute",
  "§15 « ou : [0x] ». Le 0 a survécu en tête ; les deux inégalités et le 1 ont été détruits.",
  "Rendu : 0≤x≤1. Encadrement, seul cas où deux inégalités sont nécessaires."),

 (481, 481, r"\[ \min_x f(x) \]", "haute",
  "§16 multiplicateurs de Lagrange « Pour : [\\_x f(x)] sous : [g(x)=0] on construit le Lagrangien : [ ]. »",
  "Rendu : min_x f(x)."),

 (489, 489, r"\[ \mathcal{L}(x,\lambda)=f(x)+\lambda g(x) \]", "haute",
  "§16 « on construit le Lagrangien : [vide] Les conditions stationnaires sont : [ ] ». Le \\mathcal{L} et le \\lambda ont été détruits.",
  "Rendu : 𝓛(x,λ)=f(x)+λg(x)."),

 (493, 493, r"\[ \nabla_x\mathcal{L}=0 \]", "haute",
  "§16 « Les conditions stationnaires sont : [\\_x=0] et : [g(x)=0] ». Le \\nabla et le \\mathcal{L} ont été détruits.",
  "Rendu : ∇_x𝓛=0."),

 (511, 511, r"\[ \min_x f(x) \]", "haute",
  "§17 KKT « Pour : [ ] sous : [g_i(x)] et : [h_j(x)=0] ».",
  "Rendu : min_x f(x)."),

 (515, 515, r"\[ g_i(x)\leq 0 \]", "haute",
  "§17 « sous : [ ] ».", "Rendu : g_i(x)≤0."),

 (523, 523, r"\[ \lambda_i \]", "haute",
  "§17 « on introduit des multiplicateurs : [\\_i] et (\\_j). » Le \\lambda a été détruit.",
  "Rendu : λ_i."),

 (529, 532, "\\[ \\mathcal{L}(x,\\lambda,\\mu)=f(x)\n\n+ \\sum_i\\lambda_i g_i(x)\n+ \\sum_j\\mu_j h_j(x) \\]", "haute",
  "§17 « Le Lagrangien devient : [quatre lignes] ». Le \\mathcal{L}, les deux \\sum, le \\lambda_i et le \\mu_j ont été détruits ; le signe + de tête de ligne est devenu une puce -, artefact constant.",
  "Rendu : 𝓛(x,λ,μ)=f(x)+Σλ_i g_i(x)+Σμ_j h_j(x)."),

 (538, 538, r"\[ \nabla_x\mathcal{L}=0 \]", "haute",
  "§17 « ### Stationnarité [\\_x=0] ».", "Rendu : ∇_x𝓛=0."),

 (542, 542, r"\[ g_i(x)\leq 0 \]", "haute",
  "§17 « ### Faisabilité primale [g_i(x)] [h_j(x)=0] ».",
  "Rendu : g_i(x)≤0."),

 (548, 548, r"\[ \lambda_i\geq 0 \]", "haute",
  "§17 « ### Faisabilité duale [\\_i] ### Complémentarité [ ] ». Le \\lambda et le \\geq ont été détruits.",
  "Rendu : λ_i≥0. Condition de dualité."),

 (552, 552, r"\[ \lambda_i g_i(x)=0 \]", "haute",
  "§17 « ### Complémentarité [vide] Ces conditions sont fondamentales. » La complémentarité est la quatrième condition KKT, et c'est la seule qui manque.",
  "Rendu : λ_i g_i(x)=0."),

 (562, 562, r"\[ \text{dualité faible} \]", "moyenne",
  "§18 « À un problème primal peut être associé un problème dual. On peut avoir : [vide] La dualité permet notamment : ».",
  "Candidat alternatif : \\[ d^{*}\\leq p^{*} \\] — l'inégalité de dualité faible."),

 (574, 574, r"\[ p^{*}=d^{*} \]", "haute",
  "§18 « Dans certains problèmes convexes, sous des hypothèses appropriées, la dualité forte… [vide] où (p*) et (d*) représentent les valeurs optimales primal et dual. » — la dualité forte est l'égalité des deux valeurs.",
  "Rendu : p*=d*."),

 (584, 584, r"\[ \min_x c^{T}x \]", "haute",
  "§19 programmation linéaire « Forme générale : [vide] sous : [Axb] et éventuellement : [x]. » Le premier bloc est l'objectif linéaire.",
  "Rendu : min_x c^T x. Cohérent avec la forme 2 du §112 (l. 2243)."),

 (588, 588, r"\[ Ax\leq b \]", "haute",
  "§19 « sous : [Axb] ». \\leq détruit.", "Rendu : Ax≤b."),

 (592, 592, r"\[ x\geq 0 \]", "haute",
  "§19 « et éventuellement : [x] ». \\geq détruit.", "Rendu : x≥0."),

 (618, 618, None, "inconnue",
  "§21 algorithme du simplexe « Le simplexe explore les sommets du polyèdre admissible. Conceptuellement : [vide] jusqu'à atteindre une solution optimale. »",
  "Candidat : \\[ \\text{de sommet en sommet} \\]."),

 (632, 632, r"\[ x_i\in\mathbb{Z} \]", "haute",
  "§23 programmation entière « certaines variables doivent être entières : [x_i] ». Le \\in et le \\mathbb{Z} ont été détruits.",
  "Rendu : x_i∈ℤ."),

 (636, 636, r"\[ x_i\in\{0,1\} \]", "haute",
  "§23 « Exemple : [x_i{0,1}] pour représenter : ». Le \\in a été détruit, les accolades d'ensemble ont perdu leurs contre-obliques.",
  "Rendu : x_i∈{0,1}."),

 (649, 649, r"\[ x_i\in\{0,1\} \]", "haute",
  "§24 programmation binaire « Cas particulier : [ ] ». Même reconstruction qu'en l. 636.",
  "Rendu : x_i∈{0,1}."),

 (690, 690, r"\[ x\in\mathcal{X} \]", "haute",
  "§26 optimisation combinatoire « Lorsque les solutions sont discrètes et nombreuses : [x] avec (|\\mathcal{X}|) potentiellement énorme. » — la phrase suivante nomme la cardinalité de l'ensemble.",
  "Rendu : x∈𝓧."),

 (712, 712, r"\[ DP[s]=\text{valeur optimale du sous-problème } s \]", "moyenne",
  "§27 programmation dynamique « Une formulation typique : [DP[s]=s] avec une relation de récurrence : [DP[s]=min_a{…}] ». Le premier bloc définit DP[s].",
  "Candidat alternatif : DP[s]=\\text{opt}. Le second bloc (l. 716) donne la récurrence."),

 (716, 716, r"\[ DP[s]=\min_{a}\{c(s,a)+DP[s']\} \]", "haute",
  "§27 « avec une relation de récurrence : [DP[s]=\\_a {(s,a)+DP[s']}] ». Le \\min et le c ont été détruits.",
  "Rendu : DP[s]=min_a{c(s,a)+DP[s']}. Forme canonique de Bellman."),

 (741, 741, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§29 optimisation différentiable « Pour : [ ] on peut utiliser : [f(x)] ». \\mathbb et \\to détruits.",
  "Rendu : f : ℝⁿ → ℝ."),

 (745, 745, r"\[ \nabla f(x) \]", "haute",
  "§29 « on peut utiliser : [ ] pour déterminer la direction de croissance maximale locale. » \\nabla détruit.",
  "Rendu : ∇f(x)."),

 (751, 751, r"\[ -\nabla f(x) \]", "haute",
  "§29 « Pour minimiser (f), on se déplace généralement dans la direction opposée : [-f(x)] C'est le fondement du gradient descent. »",
  "Rendu : −∇f(x)."),

 (759, 759, r"\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]", "haute",
  "§30 « L'algorithme fondamental : [vide] où : [ ] ». Le \\eta et le \\nabla ont été détruits.",
  "Rendu : x_{t+1}=x_t−η∇f(x_t). Identique à la forme 5 du §112 (l. 2269)."),

 (773, 773, r"\[ \eta\ \text{petit} \]", "moyenne",
  "§31 « ### Trop petit [vide] → convergence potentiellement très lente. » Le bloc désigne la valeur du pas.",
  "Candidat alternatif : \\[ \\eta\\ll 1 \\]."),

 (779, 779, r"\[ \eta\ \text{grand} \]", "moyenne",
  "§31 « ### Trop grand [vide] → oscillations ou divergence possibles. »",
  "Candidat alternatif : \\[ \\eta\\gg 1 \\]."),

 (793, 793, r"\[ \nabla L(\theta) \]", "haute",
  "§32 « au lieu de calculer le gradient sur tout le dataset : [L()] on peut utiliser un mini-batch (B) : [ ]. » \\nabla et \\theta détruits.",
  "Rendu : ∇L(θ)."),

 (797, 797, r"\[ \frac{1}{|B|}\sum_{i\in B}\nabla L_i(\theta) \]", "haute",
  "§32 « on peut utiliser un mini-batch (B) : [vide] C'est la base du SGD. » Le bloc est vide : \\frac, \\sum, \\in et \\nabla détruits.",
  "Estimateur du gradient sur un mini-batch."),

 (815, 815, r"\[ B\subset D \]", "haute",
  "§33 « ### Mini-batch Gradient Descent / Utilise un sous-ensemble : [BD] ». Le \\subset a été détruit.",
  "Rendu : B⊂D."),

 (825, 827, "\\[ v_t=\\beta v_{t-1}\n\n+ (1-\\beta)\\nabla f(x_t) \\]", "haute",
  "§34 momentum « Une forme classique : [trois lignes] puis : [x_{t+1}=x_t-v_t] ». Le \\beta a été détruit aux deux endroits, le \\nabla aussi ; le + de tête de ligne est devenu une puce -.",
  "Rendu : v_t=βv_{t-1}+(1−β)∇f(x_t). Identique à l. 1045 du domaine I."),

 (831, 831, r"\[ x_{t+1}=x_t-\eta v_t \]", "haute",
  "§34 « puis : [x_{t+1}=x_t-v_t] ». Le \\eta a été détruit.",
  "Rendu : x_{t+1}=x_t−ηv_t."),

 (884, 884, r"\[ \|\nabla f(x)\|<\epsilon \]", "haute",
  "§39 critères d'arrêt « Critères possibles : [|f(x)|<] ou : [ ] ». \\|, \\nabla et \\epsilon détruits.",
  "Rendu : ‖∇f(x)‖<ε."),

 (888, 888, r"\[ |f(x_{t+1})-f(x_t)|<\epsilon \]", "haute",
  "§39 « ou : [ ] ». Seul \\epsilon manque.", "Rendu : |f(x_{t+1})−f(x_t)|<ε."),

 (892, 892, r"\[ \|x_{t+1}-x_t\|<\epsilon \]", "haute",
  "§39 « ou : [ ] ». \\| et \\epsilon détruits.", "Rendu : ‖x_{t+1}−x_t‖<ε."),

 (896, 896, r"\[ t>T_{\max} \]", "haute",
  "§39 « ou simplement : [tT_{}] ». Le \\geq (ou >) et l'indice ont été détruits.",
  "Rendu : t>T_max."),

 (906, 906, r"\[ x_{t+1}=x_t-\frac{f'(x_t)}{f''(x_t)} \]", "haute",
  "§40 Newton « La méthode de Newton utilise la dérivée seconde. En dimension 1 : [vide] En dimension (n) : [vide]. »",
  "Newton scalaire. Le bloc suivant donne le cas multidimensionnel."),

 (910, 910, r"\[ x_{t+1}=x_t-H^{-1}\nabla f(x_t) \]", "haute",
  "§40 « En dimension (n) : [vide] lorsque la Hessienne est inversible. »",
  "Identique à la forme 6 du §112 (l. 2275)."),

 (918, 918, r"\[ \nabla f \]", "haute",
  "§41 « Gradient descent utilise principalement : [vide] Newton utilise : [liste] ». Le premier bloc est vide.",
  "Rendu : ∇f. Opposé au bloc suivant, qui ajoute la Hessienne."),

 (922, 924, None, "inconnue",
  "§41 « Newton utilise : [trois lignes, dont une puce -] Cela peut permettre une convergence beaucoup plus rapide près de l'optimum. » Liste de deux items.",
  "Candidat : \\[ \\nabla f \\] et \\[ \\nabla^{2}f \\] — Newton utilise le gradient ET la Hessienne."),

 (936, 936, r"\[ B_t\approx H_f(x_t) \]", "haute",
  "§42 quasi-Newton « Elles construisent une approximation : [B_tH_f(x_t)] ou de son inverse. » Le \\approx a été détruit.",
  "Rendu : B_t≈H_f(x_t)."),

 (978, 978, r"\[ \nabla_\theta L \]", "haute",
  "§44 « Le calcul différentiel permet de calculer : [vide] La backpropagation permet de calculer efficacement ces dérivées dans un réseau. » \\nabla et \\theta détruits.",
  "Rendu : ∇_θ L."),

 (984, 986, "\\[ \\theta_{t+1}=\\theta_t\n\n- \\eta\\nabla_\\theta L \\]", "haute",
  "§44 « L'optimiseur utilise ensuite ces gradients : [trois lignes] Ainsi : [ ]. » Le \\theta, le \\eta et le \\nabla_\\theta ont été détruits ; le signe moins est réel.",
  "Rendu : θ_{t+1}=θ_t−η∇_θ L."),

 (990, 990, r"\[ \theta^{*}=\arg\min_\theta L(\theta) \]", "moyenne",
  "§44 « Ainsi : [vide] » avant le §45. Le bloc conclut la section sur la chaîne d'apprentissage.",
  "Candidat alternatif : \\[ \\hat{\\theta} \\]."),

 (996, 996, r"\[ f(x)\to f'(x)\to x-\eta f'(x)\to x^{*} \]", "moyenne",
  "§45 « La chaîne du Domaine I devient ici : [f(x) f'(x) f(x) ^\\*] ». Les flèches ont été détruites ; quatre termes subsistent, dont le dernier est l'optimum. Le troisième ne peut pas être f(x) : la chaîne va de la fonction vers la solution.",
  "Candidat alternatif pour le troisième terme : x_{t+1}=x_t-\\eta f'(x_t). Cf. l. 1280 du domaine I, même motif."),

 (1004, 1004, r"\[ \min_\theta L(\theta) \]", "haute",
  "§46 fonction de perte « Le problème d'apprentissage peut être formulé comme : [vide] Exemples : ». Le \\min et le \\theta ont été détruits.",
  "Rendu : min_θ L(θ)."),

 (1012, 1012, r"\[ MSE=\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i-y_i)^{2} \]", "haute",
  "§46 régression « Erreur quadratique : [MSE=1n \\_{i=1}^{n}(y_i-y_i)^2] ». \\frac{1}{n} réduit à 1n, \\sum réduit à \\_, le chapeau de ŷ détruit — les deux arguments sont donc identiques en apparence.",
  "Rendu : MSE=(1/n)Σ(ŷ_i−y_i)²."),

 (1018, 1018, r"\[ L=-\sum_i y_i\log(\hat{y}_i) \]", "haute",
  "§46 classification « Cross-entropy : [L=-\\_i y_i(y_i)] ». Le \\log entre les deux y a été détruit, ainsi que le chapeau du second.",
  "Rendu : L=−Σ y_i log(ŷ_i). Idem l. 1510 du domaine I."),
]


def main():
    lignes = open(f"{RACINE}/{SOURCE}", encoding="utf-8").read().split("\n")
    out = [{
        "fichier": SOURCE, "ligne": deb,
        "ancien": "\n".join(lignes[deb - 1:fin]),
        "nouveau": nouv, "confiance": conf,
        "justification": just, "validation": val,
    } for deb, fin, nouv, conf, just, val in E]
    json.dump(out, open(SORTIE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    c = Counter(e["confiance"] for e in out)
    print(f"{len(out)} entrees -> {SORTIE}  {dict(c)}")
    print("applicables :", sum(1 for e in out if e["nouveau"]))


if __name__ == "__main__":
    main()
