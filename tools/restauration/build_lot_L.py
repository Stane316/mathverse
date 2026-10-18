#!/usr/bin/env python3
"""Construit le correctif du lot L (analyse numerique).

Table de reconstruction ecrite a la main, apres lecture de la totalite des
178 blocs d'affichage du document. Le bloc `ancien` est toujours relu dans le
fichier : aucune chaine n'est recopiee de memoire, ce qui garantit que le
correctif porte sur le texte reel.

Entrees de confiance « inconnue » : nouveau = None, candidats proposes dans le
document du lot. apply_patch.py les ignore.
"""
import json
import sys

ROOT = "/home/user/_audit/connaissance"
FICHIER = "Maths-vers-Informatiques/DOCUMENT L — ANALYSE NUMÉRIQUE.md"

# (ligne, nouveau, confiance, justification, validation)
H = "haute"
M = "moyenne"
I = "inconnue"

T = [
 # ---------- CHAINE / VUE D'ENSEMBLE ----------
 (136, r"\[ f(x),\quad Ax=b,\quad \nabla f,\quad \int_a^b f(x)\,dx,\quad y'=f(t,y) \]", M,
  "Enumeration des objets produits par les domaines precedents. f(x), Ax=b, y'=f(t,y) sont intacts ; "
  "\\_a^b f(x),dx est \\int_a^b f(x)\\,dx ; le troisieme terme « f » est un residu dont \\nabla a ete supprime.",
  "Coherence avec le texte : L pose la question du calcul effectif de ces objets."),

 # ---------- SECTION 4 : ERREURS ----------
 (166, "Si (x) est la valeur exacte et (\\hat{x}) la valeur calculée :", H,
  "Parentheses vides dans du texte courant : le symbole de la valeur calculee a ete supprime. "
  "L'equation qui suit, E_a=|x-x̂|, impose \\hat{x}.",
  "La ligne 168 restauree utilise le meme symbole."),
 (168, r"\[ E_a=|x-\hat{x}|. \]", H,
  "Definition de l'erreur absolue ; le fragment |x-| ne laisse pas d'autre lecture que |x-x̂|.",
  "Avec x=10 et x̂=9,99 : E_a=0,01, ce qui est exactement le resultat affiche ligne 180."),
 (176, r"\[ \hat{x}=9.99. \]", H,
  "Le bloc commence par = : la variable a ete supprimee. Ligne 172 donne x=10 ; l'exemple oppose la valeur "
  "exacte a la valeur calculee, donc x̂=9,99.",
  "E_a=|10-9,99|=0,01 = valeur de la ligne 180."),
 (186, r"\[ E_r=\frac{|x-\hat{x}|}{|x|}. \]", H,
  "Definition de l'erreur relative ; le \\frac a ete supprime avec ses arguments, ne laissant que E_r=.",
  "E_r=E_a/|x| : pour x=10 et E_a=0,01, E_r=0,001."),
 (192, r"\[ E_r(\%)=\frac{|x-\hat{x}|}{|x|}\times 100. \]", H,
  "Erreur relative en pourcentage ; les fragments conserves sont (%) et 100.",
  "100x l'erreur relative : 0,001 → 0,1 %."),

 # ---------- SECTION 5 : SOURCES D'ERREUR ----------
 (222, r"\[ e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!} \]", H,
  "Developpement en serie de l'exponentielle. \\sum est devenu \\_ ; ^{} et les balises <sup> sont des "
  "artefacts de conversion HTML de \\infty.",
  "Somme de 0 a l'infini de x^k/k! : developpement de Taylor de e^x en 0."),
 (226, r"\[ e^x \approx \sum_{k=0}^{N}\frac{x^k}{k!}. \]", H,
  "Troncature au rang N de la meme serie ; \\approx et \\sum supprimes.",
  "N fini : la somme partielle approche e^x, le reste est l'erreur de troncature annoncee par le texte."),

 # ---------- SECTIONS 6-8 : FLOTTANTS ----------
 (154, r"\[ \hat{x}. \]", M,
  "« Il stocke une approximation : [x.] ». Le symbole de la valeur calculee a ete supprime ; "
  "la ligne 168, restauree avec une confiance haute, designe cette valeur par \\hat{x}. "
  "L'autre lecture est fl(x).",
  "Coherence avec E_a=|x-\\hat{x}|."),
 (875, r"\[ h\to 0. \]", M,
  "« Plus l'ordre est eleve, plus l'erreur de discretisation diminue rapidement lorsque : [h.] » : "
  "la fleche a ete supprimee, comme aux lignes 369, 1001, 1271 et 2221.",
  "Les ordres O(h^p) de la section 48 s'entendent pour h tendant vers 0."),
 (2201, r"\[ x=m\,b^e \]", M,
  "Resume §115, rubrique Representation : la formule de la section 6.",
  "Coherence avec la ligne 238."),
 (2205, r"\[ E_r=\frac{|x-\hat{x}|}{|x|} \]", M,
  "Resume §115, rubrique Erreur : la formule de la section 4.2.",
  "Coherence avec la ligne 186."),
 (2241, r"\[ r=Ax-b \]", M,
  "Resume §115, rubrique Fiabilite : le residu, seul critere de verification formule dans le document "
  "(section 75, ligne 1236).",
  "Coherence avec la ligne 1236."),
 (2286, r"\[ \min_x f(x) \]", M,
  "Relation avec le domaine J : la forme de la section 66, ligne 1071.",
  "Coherence avec la ligne 1071."),
 (2290, r"\[ y'=f(t,y). \]", M,
  "Relation avec le domaine K : les systemes dynamiques s'ecrivent sous cette forme (sections 50 et 2233).",
  "Coherence avec les lignes 901 et 2233."),
 (242, r"\[ x=m\,2^e. \]", M,
  "« Dans les systemes binaires » : la base b de la ligne 238 devient 2. Le fragment conserve est x=m^e, "
  "la base et le signe de multiplication ayant ete supprimes.",
  "b=2 : representation binaire m x 2^e."),
 (255, r"\[ \mathbb{R} \]", H,
  "« Il existe une difference fondamentale entre : [ ] et l'ensemble fini des nombres representables ». "
  "\\mathbb{R} a ete supprime avec son argument : il ne reste rien.",
  "La ligne 261 confirme : l'ensemble en question est « continu et infini »."),
 (261, r"\[ \mathbb{R} \]", H,
  "« Ainsi : [ ] est continu et infini tandis que les nombres flottants sont finis ».",
  "Seul R est continu, infini et oppose a un ensemble fini de flottants."),
 (271, r"\[ \varepsilon_{\text{mach}} \approx \beta^{-p} \]", M,
  "Fragments \\_{}^{-p} : un indice vide et un exposant -p. \\varepsilon (grec) et \\beta (grec) ont ete "
  "supprimes, ainsi que le nom de l'indice et \\approx.",
  "En double precision IEEE-754 : beta=2, p=53, 2^-52 ≈ 2,2x10^-16, l'epsilon machine connu. "
  "Le texte signale « selon la convention utilisee » : l'exposant peut aussi valoir 1-p."),

 # ---------- SECTION 9 : PIEGES DU FLOTTANT ----------
 (297, r"\[ \text{annulation catastrophique} \]", M,
  "« On parle de : [ ] ou catastrophic cancellation » : le terme francais, dont la traduction est donnee "
  "juste apres.",
  "Terme consacre : cancellation = annulation, catastrophic = catastrophique."),
 (309, r"\[ \mathrm{fl}((a+b)+c) \]", M,
  "« En flottant : ((a+b)+c) peut etre different de (a+(b+c)) ». L'operateur fl(.) a ete supprime, "
  "ce qui vide la phrase de son sens : sans lui les deux expressions sont egales en arithmetique exacte.",
  "fl(a+b+c) differe de fl(a+fl(b+c)) : c'est precisement la perte d'associativite."),
 (313, r"\[ \mathrm{fl}(a+(b+c)). \]", M,
  "Meme operateur, second membre de la comparaison.",
  "Idem."),

 # ---------- SECTION 12-14 : CONVERGENCE ----------
 (365, r"\[ x_0,x_1,x_2,\ldots \]", H,
  "L'enumeration s'arrete sur une virgule : \\ldots a ete supprime. Defaut invisible aux heuristiques "
  "(le bloc reste syntaxiquement valide).",
  "Une suite iterative est infinie."),
 (369, r"\[ x_k\to x^*. \]", H,
  "Fragments x_k et x^ : la fleche a ete supprimee et l'etoile de x* aussi (meme trace qu'aux lignes "
  "382, 435, 1170, 1271).",
  "« qui doit idealement verifier » : convergence vers la solution x*."),
 (382, r"\[ e_k=|x_k-x^*| \]", H,
  "Definition de l'erreur a l'iteration k ; x* prive de son etoile.",
  "e_k → 0 ssi x_k → x*."),
 (386, r"\[ e_{k+1}\leq C e_k^p, \]", H,
  "Le comparateur a disparu mais pas la constante C : \\leq (commande sans argument) a ete supprime, alors "
  "que = aurait survecu comme partout ailleurs dans le document.",
  "Definition usuelle de l'ordre de convergence : e_{k+1} <= C e_k^p."),
 (408, r"\[ |x_{k+1}-x_k|<\varepsilon \]", H,
  "Critere d'arret sur l'increment ; la tolerance (grec epsilon) a ete supprimee.",
  "Critere absolu standard ; le texte enumere ensuite tolerance absolue, relative, residu."),
 (412, r"\[ |F(x_k)|<\varepsilon \]", H,
  "Critere d'arret sur le residu ; meme suppression.",
  "Le residu s'annule a la solution."),
 (416, r"\[ |x_{k+1}-x_k|<\varepsilon\max(1,|x_k|). \]", M,
  "Fragments {(1,|x_k|)} et < : forme mixte absolu/relatif. Le \\max et l'epsilon ont ete supprimes, "
  "ainsi que la partie gauche que rien n'explique — la lecture reste donc incertaine.",
  "Critere relatif standard : borne l'increment par une tolerance fois max(1,|x|). "
  "Si ce n'est pas la forme voulue, la replacer par la vostre."),

 # ---------- SECTIONS 15-19 : EQUATIONS ----------
 (435, r"\[ x^*. \]", M,
  "« On cherche donc : x^x ». L'exposant x est inexplique ; la lecture la plus probable est x* "
  "(la solution), l'etoile ayant subi une alteration.",
  "Coherence avec les lignes 369, 382, 1170, 1271 ou x* apparait sous la forme x^."),
 (449, r"\[ m=\frac{a+b}{2}. \]", H,
  "Milieu de l'intervalle de bissection ; le \\frac a ete supprime avec ses arguments.",
  "m est le milieu de [a,b] : le texte decrit ensuite la conservation du sous-intervalle de changement de signe."),
 (465, r"\[ f'(x_n) \]", M,
  "« La methode de Newton utilise : [ ] Elle repose sur l'approximation locale de (f) par sa tangente » : "
  "la derivee. La notation exacte reste un choix (f'(x_n), f'(x), ∇f).",
  "Newton-Raphson requiert f' : section 17.3 sur les risques quand f'(x) est proche de zero."),
 (485, r"\[ \text{convergence quadratique}. \]", M,
  "« ## 17.2 Avantage — Pres d'une racine simple et sous des conditions favorables : [ ] ». L'avantage de "
  "Newton est sa convergence quadratique (section 13 : p=2). Le bloc ne contenait peut-etre qu'un terme.",
  "Newton est quadratique pres d'une racine simple : ordre p=2."),
 (501, r"\[ f'(x_n)\approx\frac{f(x_n)-f(x_{n-1})}{x_n-x_{n-1}}. \]", H,
  "Pente de la secante. Fragment conservé : {x_n-x_{n-1}} — le denominateur entre accolades, "
  "le numerateur ayant ete emporte avec le \\frac ( meme trace qu'au document K, ligne 869 ).",
  "Quotient des differences finies : la pente entre les deux derniers points."),

 # ---------- SECTIONS 20-31 : LINEAIRE ----------
 (631, r"\[ x_0,x_1,x_2,\ldots \]", H,
  "Meme enumeration tronquee qu'a la ligne 365, pour les methodes iteratives.",
  "Une suite iterative est infinie."),
 (669, r"\[ \min_x \frac{1}{2}x^TAx-b^Tx. \]", H,
  "Forme variationnelle du gradient conjugue. \\min_x est devenu \\_x ; \\frac{1}{2} est devenu 12 ; "
  "x^T A x - b^T x a ete hache par les balises <sup>.",
  "Le gradient de 1/2 x'Ax - b'x est Ax-b : minimiser revient a resoudre Ax=b, ce que dit le texte."),
 (691, r"\[ (x_0,y_0),\ldots,(x_n,y_n). \]", H,
  "Double virgule : \\ldots supprime. Defaut invisible aux heuristiques.",
  "Enumeration elliptique de n+1 points."),

 # ---------- SECTIONS 32-36 : INTERPOLATION ----------
 (701, r"\[ p(x)=\sum_{i=0}^{n} y_iL_i(x) \]", H,
  "Forme de Lagrange ; \\sum devenu \\_.",
  "p(x_i)=y_i : en x=x_i, seul L_i vaut 1, les autres s'annulent."),
 (705, r"\[ L_i(x)=\prod_{j\neq i}\frac{x-x_j}{x_i-x_j}. \]", H,
  "Polynome de base de Lagrange. \\prod devenu \\_ et \\neq supprime laissant ji ; le quotient a ete "
  "emporte avec le \\frac.",
  "L_i(x_j)=1 si j=i, 0 sinon : c'est la definition des polynomes de Lagrange."),

 # ---------- SECTIONS 37-39 : APPROXIMATION ----------
 (748, r"\[ p(x)\approx f(x) \]", H,
  "« L'approximation cherche plutot : [ ] selon un critere donne » : \\approx supprime.",
  "Opposition avec l'interpolation de la ligne 744 qui impose p(x_i)=f(x_i)."),
 (756, r"\[ \sum_i (y_i-f(x_i))^2. \]", H,
  "Somme des carres des residus ; \\sum_i devenu \\_i.",
  "Minimum atteint quand les residus sont nuls en moyenne quadratique."),
 (760, r"\[ \min_x\|Ax-b\|_2^2. \]", H,
  "Moindres carres matriciels. \\min_x devenu \\_x ; \\| et \\|_2 supprimes.",
  "La norme au carre de Ax-b est la somme des carres des residus de la ligne 756."),
 (776, r"\[ \min_x \|Ax-b\|_2^2+\lambda\|x\|_2^2. \]", M,
  "Regularisation de Tikhonov : le terme de penalisation subsiste, mais son coefficient (grec lambda) "
  "a ete supprime. λ est le choix standard, il pourrait etre note alpha.",
  "Le texte parle de regularisation ; la penalite quadratique limite les solutions instables."),

 # ---------- SECTIONS 40-45 : INTEGRATION ----------
 (786, r"\[ I=\int_a^b f(x)\,dx. \]", H,
  "Integrale definie ; \\int devenu \\_ et \\, supprime devant dx.",
  "Notation standard de l'integrale a approcher."),
 (794, r"\[ \int_a^b f(x)\,dx \approx \sum_i f(x_i)\,\Delta x. \]", H,
  "Regle des rectangles ; \\approx et \\sum supprimes, \\Delta reduit a x.",
  "Somme des aires de rectangles de largeur Delta x."),
 (804, r"\[ \int_a^b f(x)\,dx \approx \frac{b-a}{2}\left[f(a)+f(b)\right]. \]", H,
  "Regle des trapezes ; le crochet [f(a)+f(b)] a survecu, le facteur (b-a)/2 a ete emporte avec le \\frac.",
  "Aire du trapeze : base fois (f(a)+f(b))/2."),
 (814, r"\[ \int_a^b f(x)\,dx \approx \frac{b-a}{6}\left[f(a)+4f\left(\frac{a+b}{2}\right)+f(b)\right]. \]", M,
  "Methode de Simpson : le texte annonce une approximation quadratique locale. Seule la structure est "
  "reconstruite, le contenu exact a disparu ; la forme composite est une autre possibilite.",
  "Simpson est exacte pour les polynomes de degre 3 : verifiable sur un polynome de degre 2."),

 # ---------- SECTION 47 : DIFFERENCES FINIES ----------
 (847, r"\[ f'(x)\approx\frac{f(x+h)-f(x)}{h}. \]", H,
  "Différence avant (section 47.1). Les trois blocs de la section sont identiques dans le fichier : "
  "seuls les titres permettent de les distinguer.",
  "Developpement de Taylor : (f(x+h)-f(x))/h = f'(x) + O(h)."),
 (851, r"\[ f'(x)\approx\frac{f(x)-f(x-h)}{h}. \]", H,
  "Différence arrière (section 47.2).",
  "(f(x)-f(x-h))/h = f'(x) + O(h)."),
 (855, r"\[ f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}. \]", H,
  "Différence centrée (section 47.3).",
  "Erreur en O(h^2) : la section 48 annonce O(h), O(h^2), O(h^4)."),

 # ---------- SECTION 50-52 : EDO ----------
 (901, r"\[ y'=f(t,y). \]", H,
  "« Une EDO peut s'ecrire : =f(t,y) » : la fonction inconnue a ete supprimee.",
  "Forme standard d'un probleme de Cauchy, complete par y(t_0)=y_0 ligne 905."),
 (936, r"\[ \text{problèmes raides} \]", M,
  "« On parle notamment de : [ ] ou stiff problems » : le terme francais.",
  "Traduction consacree de stiff problems."),

 # ---------- SECTION 58-60 : MONTE-CARLO ----------
 (997, r"\[ I_N = \frac{1}{N}\sum_{i=1}^{N}f(X_i). \]", H,
  "Estimateur de Monte-Carlo. \\frac{1}{N} est devenu 1N et \\sum est devenu \\_.",
  "Estimateur sans biais de E[f(X)] : moyenne empirique de N tirages."),
 (1001, r"\[ I_N\to I. \]", H,
  "Convergence de l'estimateur ; la fleche a ete supprimee.",
  "Loi des grands nombres : I_N tend vers I quand N croit."),
 (1007, r"\[ O\left(\frac{1}{\sqrt{N}}\right). \]", H,
  "Ordre de l'erreur Monte-Carlo ; le \\frac et la racine ont ete supprimes, laissant des parentheses vides.",
  "L'ecart-type de la moyenne empirique est sigma/racine de N : diviser l'erreur par 10 coute 100 fois "
  "plus d'echantillons, ce que dit le texte."),

 # ---------- SECTION 63-67 : VALEURS PROPRES, OPTIMISATION ----------
 (1044, r"\[ Av=\lambda v. \]", H,
  "Definition valeur/vecteur propre ; le lambda grec a ete supprime.",
  "v propre associe a la valeur propre lambda."),
 (1061, r"\[ x_{k+1}=\frac{Ax_k}{\|Ax_k\|}. \]", M,
  "Iteration de la puissance. Seule la forme normalisee est compatible avec « approximer la valeur propre "
  "dominante » ; la forme non normalisee x_{k+1}=Ax_k est l'autre lecture possible.",
  "La normalisation empeche la divergence ; le rapport de Rayleigh donne alors la valeur propre."),
 (1071, r"\[ \min_x f(x). \]", H,
  "« Le domaine J definit le probleme : \\_x f(x) » : \\min_x devenu \\_x.",
  "Probleme d'optimisation sans contrainte."),
 (1089, r"\[ \min f(x), \]", H,
  "« Pour : [f(x)], on utilise : x_{k+1}=x_k-H_f(x_k)^{-1}∇f(x_k) » : \\min supprime.",
  "Newton pour l'optimisation minimise f."),
 (1093, r"\[ x_{k+1} = x_k- H_f(x_k)^{-1}\nabla f(x_k). \]", H,
  "Newton pour l'optimisation. Le gradient a ete supprime devant f(x_k) : sans lui l'iteration n'a pas de sens "
  "(H^{-1}f(x_k) n'est pas homogene a une position).",
  "H_f est la hessienne : l'iteration annule le gradient au second ordre."),
 (1101, r"\[ H\delta=-\nabla f \]", H,
  "Systeme de Newton. \\delta (grec) et \\nabla supprimes, laissant H=-f.",
  "Resolution du systeme lineaire en le pas delta."),
 (1105, r"\[ x_{k+1}=x_k+\delta. \]", H,
  "Mise a jour. Le meme delta grec a ete supprime, ce qui confirme la lecture de la ligne 1101.",
  "Le pas delta calcule en 1101 est ajoute a x_k."),

 # ---------- SECTION 69 : DIFFERENTIATION AUTOMATIQUE ----------
 (1142, r"\[ \frac{dy}{dx}=\frac{dy}{dz}\frac{dz}{dx}. \]", H,
  "Regle de chaine. z=f(x), y=g(z) sont donnes aux lignes 1134 et 1138 ; les trois \\frac ont ete supprimes, "
  "ne laissant que le signe egal.",
  "Derivee de la composee : produit des derivees."),

 # ---------- SECTIONS 70-71 : POINT FIXE ----------
 (1154, r"\[ x_{k+1}=\varphi(x_k). \]", H,
  "Iteration de point fixe ; le phi grec a ete supprime, laissant des parentheses vides.",
  "Forme generale annoncee par le titre de section."),
 (1158, r"\[ x^*=\varphi(x^*). \]", H,
  "Point fixe. Meme suppression, plus l'etoile de x* ; les balises <sup> sont un artefact de conversion.",
  "Le point fixe verifie x=phi(x)."),
 (1164, r"\[ x=\varphi(x) \]", H,
  "« Resoudre : [x=(x)] peut etre equivalent a resoudre une equation » : meme phi supprime.",
  "Coherence avec la ligne 1158."),
 (1170, r"\[ |\varphi'(x^*)|<1, \]", H,
  "Condition de convergence locale. phi' et l'etoile supprimes, laissant |'(x^)|<1.",
  "Le module de la derivee au point fixe doit etre inferieur a 1 : theoreme du point fixe."),

 # ---------- SECTIONS 77-82 : VALIDATION, ECHELLES ----------
 (1271, r"\[ x_h\to x^*, \]", H,
  "Test de convergence pratique : comparer x_h, x_{h/2}, x_{h/4}. La fleche et l'etoile ont ete supprimees.",
  "Si les resultats convergent vers x*, la discretisation est convergente."),
 (1295, r"\[ x_1\sim 10^{-10} \]", H,
  "Ordre de grandeur ; \\sim supprime.",
  "Opposition des echelles : 10^-10 contre 10^10, ecart de 20 decades."),
 (1299, r"\[ x_2\sim 10^{10}, \]", H,
  "Meme suppression.",
  "Idem."),
 (1326, r"\[ A\in\mathbb{R}^{n\times n} \]", H,
  "Matrice dense carree. \\in, \\mathbb{R} et \\times supprimes, laissant AR^{nn}.",
  "Une matrice n x n demandee O(n^2) de memoire, comme l'annonce la ligne 1330."),
 (1336, r"\[ O(\mathrm{nnz}(A)). \]", M,
  "Cout de stockage d'une matrice creuse : proportionnel au nombre de coefficients non nuls. "
  "Le nom de la fonction a ete supprime avec son argument.",
  "Formulation standard nnz(A)."),

 # ---------- SECTION 85 : IA ----------
 (1394, r"\[ \min_{\theta}\mathcal{L}(\theta). \]", H,
  "Entrainement : minimisation de la perte. \\min_{\\theta} devenu \\_ (l'indice grec a disparu), "
  "\\mathcal{L} reduit a L, (\\theta) vide.",
  "Forme standard ; le bloc « Gradient » qui suit porte sur la meme perte."),
 (1398, r"\[ \nabla_\theta \mathcal{L}. \]", H,
  "Gradient de la perte. \\nabla_\\theta devenu \\_ ; \\mathcal{L} reduit a L.",
  "Gradient de la fonction minimisee en 1394."),
 (1402, r"\[ \theta_{t+1}=\theta_t-\eta\nabla\mathcal{L}. \]", H,
  "Descente de gradient. Les theta et eta grecs ont ete supprimes ainsi que \\nabla : il reste _{t+1}=_t-L.",
  "Pas de descente : on retranche au parametre le gradient multiplie par le pas d'apprentissage."),
 (1464, r"\[ \frac{dv}{dt}=a. \]", H,
  "Physique des jeux video. Le \\frac a ete supprime ; l'equation manquante est celle de la vitesse : "
  "les lignes 1468 et 1472 integrent v puis x.",
  "Euler : v_{n+1}=v_n+h a_n est l'integration de dv/dt=a."),

 # ---------- SECTION 102 : EXACT / APPROCHE / NUMERIQUE ----------
 (1697, r"\[ \text{exact} \]", M,
  "Section 102 « EXACT, APPROCHE, NUMERIQUE » : les trois blocs vides qui suivent « Il faut distinguer : » "
  "reprennent les trois termes du titre. Le contenu est donc tres probable, la mise en forme (terme ou "
  "formule) reste incertaine.",
  "Le titre de section nomme les trois notions."),
 (1699, r"\[ \text{approché} \]", M,
  "Deuxieme terme du titre de la section 102.",
  "Idem."),
 (1701, r"\[ \text{numérique} \]", M,
  "Troisieme terme du titre de la section 102.",
  "Idem."),

 # ---------- DIVERS ----------
 (1580, r"\[ K\times L \]", M,
  "« Ainsi : [KL] peut produire des systemes proceduraux beaucoup plus riches ». Le signe a ete supprime ; "
  "la trace de \\times est la meme qu'a la ligne 1326 (AR^{nn} pour A dans R^{n x n}). "
  "K+L reste une lecture defendable.",
  "Combinaison des domaines K (structures) et L (calcul)."),
 (1794, r"\[ T_{\text{calcul}}<T_{\text{budget}}. \]", M,
  "Temps reel : le temps de calcul doit rester sous le temps imparti. Les deux indices ont ete supprimes.",
  "Contrainte de temps reel annoncee par le titre de section."),
 (2221, r"\[ (x_i,y_i)\to f(x) \]", H,
  "Resume §115, rubrique Interpolation : la fleche a ete supprimee.",
  "Des donnees vers la fonction interpolee."),
 (2225, r"\[ \int_a^b f(x)\,dx. \]", H,
  "Resume §115, rubrique Integration : \\int supprime, le ,dx a survecu.",
  "Coherence avec la ligne 786."),
 (2233, r"\[ y'=f(t,y). \]", H,
  "Resume §115, rubrique Dynamique : meme forme qu'a la ligne 901.",
  "Coherence avec la ligne 901."),
 (2065, r"\[ x,\ \hat{x},\ |x-\hat{x}|. \]", H,
  "Projet 1 : visualiseur d'erreur flottante. Les double virgules trahissent un terme supprime entre x et "
  "|x-| : la valeur calculee, soit x̂.",
  "Coherence avec les lignes 168 et 176."),
]

# multi-lignes : (ligne, ancien, nouveau, ...)
MULTI = [
 (711, "\\[ p(x) = a_0+ a_1(x-x_0)\n\n- a_2(x-x_0)(x-x_1) + \\]",
  r"\[ p(x) = a_0+ a_1(x-x_0)+ a_2(x-x_0)(x-x_1)+\ldots+a_n(x-x_0)\ldots(x-x_{n-1}) \]", M,
  "Forme de Newton pour l'interpolation, section 34 « on peut utiliser les differences divisees ». "
  "Le bloc occupe trois lignes et le signe + initial est devenu un tiret, meme alteration qu'aux lignes "
  "1205-1208 et dans les blocs de combinaison de la section 108.",
  "Forme imbriquee : chaque terme ajoute un facteur (x-x_j), le texte vante l'ajout progressif de points."),
 (1203, "\\[ E_{} E_{}\n\n- E_{}\n- E_{}\n- E_{}\n- E_{}. \\]",
  r"\[ E_{\text{total}}=E_{\text{modèle}}+E_{\text{données}}+E_{\text{arrondi}}+E_{\text{troncature}}"
  r"+E_{\text{algorithme}}. \]", M,
  "Decomposition de l'erreur, section 74. Six termes subsistent dont les indices ont ete vides : un total "
  "et cinq contributions — exactement les cinq sources enumerees en section 5. "
  "L'ordre des termes est reconstruit.",
  "Les cinq contributions sont celles des sections 5.1 a 5.6."),
]

# inconnues : contenu non recuperable (nouveau = None)
INCONNUES = [
 (13, "tension entre [ ] et [ ] — le couple oppose n'est pas nomme ailleurs dans le document "
      "(candidats : precision / cout, exactitude / vitesse, stabilite / rapidite)"),
 (17, "second terme de la meme opposition"),
 (55, "ce que le systeme ne doit jamais considerer sans analyser les conditions du calcul"),
 (61, "principe directeur du domaine (probablement un enonce, pas une formule)"),
 (115, "chaine des domaines A a L (candidat : A → B → … → L)"),
 (146, "le reel que l'on ecrit exactement sur papier (candidats : racine de 2, 0,1, 1/3, pi)"),
 (158, "ce qui reste vrai dans la plupart des cas (candidat : x̂ ≈ x)"),
 (202, "erreur de modele : bloc vide"),
 (343, "ce qui distingue stabilite, conditionnement et convergence"),
 (351, "condition de mauvais conditionnement"),
 (416, None),  # traite en moyenne
 (723, "ce que montre le phenomene de Runge"),
 (808, "regle des trapezes composee"),
 (883, "ce qui diminue quand h diminue"),
 (887, "ce qui augmente quand h diminue"),
 (893, "forme de la courbe d'erreur (candidat : E(h) = C1 h^p + C2 eps / h)"),
 (1017, "ce qui rend les methodes deterministes couteuses (candidat : la malediction de la dimension)"),
 (1148, "les deux poles relies par la differentiation automatique"),
 (1193, "idee des methodes multigrilles"),
 (1197, "ce que deviennent les erreurs"),
 (1281, "examen analytique de la sensibilite"),
 (1285, "examen experimental"),
 (1364, "le compromis ameliore par la precision mixte (candidat : vitesse / precision)"),
 (1604, "architecture d'un solveur serieuse"),
 (1770, "criteres d'evaluation d'une methode"),
 (1812, "combinaison L + K → mondes proceduraux dynamiques"),
 (1820, "combinaison L + J → systemes de decision numeriques"),
 (1828, "combinaison L + I → apprentissage et simulation"),
 (1836, "combinaison L + C → calcul scientifique et IA"),
 (1844, "combinaison L + G → simulation sous incertitude"),
 (1852, "combinaison L + D → reconstruction et animation 3D"),
 (1860, "combinaison L + E/F → planification et systemes complexes"),
 (1870, "ce que le systeme applique pour inventer une application"),
 (1874, "premier exemple"),
 (1878, "second exemple"),
 (2106, "quantite a estimer par Monte-Carlo (candidats : pi, une integrale)"),
 (2191, "ce que le developpeur doit pouvoir verifier"),
 (2282, "relation avec le domaine I"),
 (2298, None),  # artefact d'echappement, non traite
 (2302, "relation avec le domaine H"),
 (2308, "l'idee fondamentale enseignee par le domaine L"),
 (2312, "la chaine entre le modele et le resultat"),
 (2340, "formule mentale a conserver pour tout probleme numerique"),
 (2344, "ce que l'IA doit appliquer pour passer du concept au logiciel"),
 (2350, "point de depart"),
 (2354, "point d'arrivee"),
]


def main():
    lines = open(f"{ROOT}/{FICHIER}", encoding="utf-8").read().split("\n")
    out = []
    for ligne, nouveau, conf, just, val in T:
        out.append({"fichier": FICHIER, "ligne": ligne, "ancien": lines[ligne - 1],
                    "nouveau": nouveau, "confiance": conf,
                    "justification": just, "validation": val})
    for ligne, ancien, nouveau, conf, just, val in MULTI:
        assert lines[ligne - 1] == ancien.split("\n")[0], f"L{ligne}: premiere ligne inattendue"
        out.append({"fichier": FICHIER, "ligne": ligne, "ancien": ancien, "nouveau": nouveau,
                    "confiance": conf, "justification": just, "validation": val})
    for ligne, note in INCONNUES:
        if note is None:
            continue
        out.append({"fichier": FICHIER, "ligne": ligne, "ancien": lines[ligne - 1],
                    "nouveau": None, "confiance": I, "statut": "en_attente_de_decision",
                    "justification": "Bloc vide ou ininterpretable : " + note +
                                     ". Le contenu d'origine n'existe plus dans le fichier.",
                    "validation": None})
    out.sort(key=lambda e: e["ligne"])
    path = "docs/restauration/propositions/domaine-L.patch.json"
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    n_h = sum(1 for e in out if e["confiance"] == H)
    n_m = sum(1 for e in out if e["confiance"] == M)
    n_i = sum(1 for e in out if e["confiance"] == I)
    print(f"{path} : {len(out)} entrees — {n_h} haute, {n_m} moyenne, {n_i} inconnue")
    return 0


if __name__ == "__main__":
    sys.exit(main())
