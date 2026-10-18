#!/usr/bin/env python3
"""Construction du lot 5b : domaine J — Optimisation, sections 47 a 158
(lignes 1026 a 3534). Fin du document J.

Deux structures equivalentes survivantes ont ete exploitees (regle du lot 4b) :

  - la section 110 « MODÉLISATION AVANT ALGORITHME » (l. 2184-2193) est une
    liste numerotee INTACTE de dix questions ; la section 156 en pose dix
    egalement. Les dix blocs vides de la 156 sont donc les dix primitives de
    modelisation que la 110 nomme, dans l'ordre des questions posées.
  - la section 122 (l. 2464-2484) est une chaine ASCII intacte de dix etapes ;
    elle n'a PAS ete retenue pour la 155 (dix blocs vides) : la 122 decrit un
    moteur d'optimisation, la 155 une progression de domaines. La coincidence
    du nombre dix est signalee comme piste, pas comme preuve.

Convention de l'auteur pour les reponses en mots : \\ wyse-espace (l. 2972-2978,
« learning\\ rate », « batch\\ size »). Les reconstructions en \\text{…} suivent
cette convention ; le libelle exact reste un choix d'auteur.
"""

import json
from collections import Counter

SOURCE = "Maths-vers-Informatiques/Domaine J — Optimisation.md"
RACINE = "/home/user/_audit/connaissance"
SORTIE = "docs/restauration/propositions/domaine-J-lot5b.patch.json"

E = [
 # ---------- 47-52 : régularisation, généralisation, stochasticité ----------
 (1026, 1026, r"\[ L(\theta)+\lambda R(\theta) \]", "haute",
  "§47 « On peut ajouter une pénalité : [vide] Exemples : ### L2 … ### L1 ». Le \\theta et le \\lambda ont été détruits ; la structure « perte + pénalité » est imposée par les deux exemples qui suivent et par la forme 4 du §112 (l. 2263).",
  "Rendu : L(θ)+λR(θ)."),

 (1032, 1032, r"\[ R(\theta)=\|\theta\|_{2}^{2} \]", "haute",
  "§47 « ### L2 [R()=||\\_2^2] ». Le \\theta a été détruit dans R() et dans la norme ; \\| a perdu sa contre-oblique.",
  "Pénalité L2 au carré — la forme universelle du weight decay."),

 (1036, 1036, r"\[ R(\theta)=\|\theta\|_{1} \]", "haute",
  "§47 « ### L1 [R()=||\\_1] ». Même destruction.", "Pénalité L1 — la forme du lasso."),

 (1046, 1046, r"\[ L_{\text{train}} \]", "haute",
  "§48 « On distingue : [L_{}] et : [L_{}] ». Le contenu de \\text{…} a été détruit ; la paire entraînement/test est la seule distinction possible dans ce contexte.",
  "Rendu : L_train."),

 (1050, 1050, r"\[ L_{\text{test}} \]", "haute",
  "§48, second terme de la paire.", "Rendu : L_test."),

 (1054, 1054, r"\[ L_{\text{train}} \]", "haute",
  "§48 « Un modèle peut avoir : [L_{}] mais : [L_{}] ». Le surapprentissage est une perte d'entraînement faible avec une perte de test élevée : l'ordre est imposé par le sens.",
  "Rendu : L_train (faible)."),

 (1058, 1058, r"\[ L_{\text{test}} \]", "haute",
  "§48, second terme — la perte de test, élevée.", "Rendu : L_test (élevée)."),

 (1072, 1072, r"\[ L(\theta) \]", "haute",
  "§49 « Pour un réseau : [L()] où (θ) peut contenir des millions ou milliards de paramètres ». Le \\theta a été détruit.",
  "Rendu : L(θ)."),

 (1092, 1094, "\\[ g_t=\\nabla f(x_t)\n\n+ \\xi_t \\]", "haute",
  "§50 « Lorsque le gradient est bruité : [trois lignes] l'algorithme travaille avec une estimation du gradient. ». Le \\nabla et le \\xi ont été détruits ; le + de tête de ligne est devenu une puce -.",
  "Gradient bruité = vrai gradient + bruit ξ_t."),

 (1116, 1116, None, "inconnue",
  "§51 « Il existe donc un compromis entre : [vide] et : [vide] ». La liste qui précède énumère cinq effets de la taille du batch ; le compromis en oppose deux, mais lesquels n'est pas déterminé.",
  "Candidats : \\[ \\text{bruit du gradient} \\] et \\[ \\text{coût computationnel} \\] — les deux items de tête de la liste (l. 1108-1109)."),

 (1120, 1120, None, "inconnue", "§51, second terme du compromis.", "Voir l. 1116."),

 # ---------- 53-58 : recherche locale, recuit, génétiques ----------
 (1146, 1146, r"\[ x\to N(x)\to x'\to N(x') \]", "haute",
  "§53 « Schéma : [x N(x) x’ N(x’)] ». Les flèches ont été détruites ; quatre termes subsistent dans l'ordre d'une itération de recherche locale.",
  "Rendu : x → N(x) → x’ → N(x’)."),

 (1154, 1154, r"\[ x_0^{(1)},x_0^{(2)},\ldots,x_0^{(k)} \]", "haute",
  "§54 « On lance une recherche locale depuis plusieurs points de départ : [x_0^{(1)},x_0^{(2)},,x_0^{(k)}] ». Le \\ldots est devenu une virgule.",
  "Rendu : x₀⁽¹⁾,x₀⁽²⁾,…,x₀⁽ᵏ⁾."),

 (1168, 1168, r"\[ P=\exp\left(-\frac{\Delta E}{T}\right) \]", "moyenne",
  "§55 « Une probabilité typique d'acceptation est : [P=( - )] où (E) est l'augmentation de coût ; (T) est la température. ». Le résidu montre un exposant négatif entre parenthèses : \\exp et \\frac ont été détruits, ainsi que ΔE/T.",
  "Probabilité d'acceptation de Metropolis. La notation du numérateur (ΔE, Δc ou Δf) est un choix d'auteur ; la structure exponentielle est certaine."),

 (1183, 1183, r"\[ P=\{x_1,x_2,\ldots,x_n\} \]", "haute",
  "§56 « Une population : [P={x_1,x_2,,x_n}] ». Le \\ldots est devenu une virgule ; les accolades d'ensemble ont perdu leurs contre-obliques.",
  "Rendu : P={x₁,x₂,…,x_n}."),

 (1194, 1194, None, "inconnue",
  "§56 « Schéma : [vide] ». Le schéma d'évolution d'un algorithme génétique (sélection → croisement → mutation) tenait en un bloc.",
  "Candidat : \\[ \\text{sélection}\\to\\text{croisement}\\to\\text{mutation} \\]."),

 (1202, 1202, r"\[ F(x) \]", "moyenne",
  "§57 « Selon le problème : [(x)] peut être : ». La fonction de fitness est nommée en toutes lettres ; le symbole a été détruit.",
  "Candidat alternatif : \\[ \\text{fitness}(x) \\]."),

 # ---------- 62-69 : bayésien, multi-objectifs, robuste, ERM ----------
 (1265, 1265, None, "inconnue",
  "§62 optimisation bayésienne « Principe : [vide] Applications : ». Bloc entièrement détruit.",
  "Candidat : \\[ x_{t+1}=\\arg\\max_x\\ \\text{EI}(x) \\] — le critère d'amélioration espérée, ou plus sobrement \\[ \\text{modèle}\\to\\text{acquisition}\\to\\text{évaluation} \\]."),

 (1299, 1299, r"\[ f_1(x),f_2(x),\ldots,f_k(x) \]", "haute",
  "§63 « Certains problèmes possèdent plusieurs objectifs : [f_1(x),f_2(x),,f_k(x)] ». Le \\ldots est devenu une virgule.",
  "Rendu : f₁(x),f₂(x),…,f_k(x)."),

 (1303, 1303, None, "inconnue",
  "§63 « Par exemple : [vide] tout en : [vide] et : [vide] Ces objectifs peuvent être contradictoires. ». Trois blocs pour un exemple d'objectifs contradictoires.",
  "Candidats : \\[ \\min\\ \\text{coût} \\], \\[ \\max\\ \\text{qualité} \\], \\[ \\min\\ \\text{délai} \\]."),

 (1307, 1307, None, "inconnue", "§63, deuxième objectif de l'exemple.", "Voir l. 1303."),
 (1311, 1311, None, "inconnue", "§63, troisième objectif de l'exemple.", "Voir l. 1303."),

 (1334, 1338, "\\[ F(x)=\\lambda_1f_1(x)\n\n+ \\lambda_2f_2(x)\n\n+ \\lambda_kf_k(x) \\]", "haute",
  "§65 « On peut combiner plusieurs objectifs : [cinq lignes] avec des poids : [\\_i] ». Le \\lambda a été détruit trois fois ; les + de tête de ligne sont devenus des puces -.",
  "Somme pondérée — la scalarisation canonique. Rendu : F(x)=λ₁f₁(x)+λ₂f₂(x)+λ_kf_k(x)."),

 (1342, 1342, r"\[ \lambda_i \]", "haute",
  "§65 « avec des poids : [\\_i] ». Le \\lambda a été détruit ; le \\_ est son résidu, comme en l. 523 et l. 548.",
  "Rendu : λ_i."),

 (1352, 1352, r"\[ \min_x f(x) \]", "haute",
  "§66 « Au lieu de : [\\_x f(x)] on peut considérer : […] ».", "Rendu : min_x f(x)."),

 (1356, 1356, r"\[ \min_x\max_{\delta\in\Delta}f(x,\delta) \]", "moyenne",
  "§66 « on peut considérer : [_x_ {} f(x,)] où (δ) représente une incertitude. ». Le résidu porte la trace de deux opérateurs d'optimisation et d'un sous-script vide : c'est une forme min-max.",
  "Optimisation robuste. Le symbole de l'ensemble d'incertitude (Δ ou 𝒰) est un choix d'auteur."),

 (1376, 1376, r"\[ \min_x\mathbb{E}[f(x,\xi)] \]", "haute",
  "§67 « on peut chercher : [vide] ». La forme est donnée mot pour mot par la forme 7 du §112 (l. 2281) et par le §116 (l. 2389), tous deux lisibles.",
  "Minimisation d'une espérance — la forme de l'optimisation stochastique."),

 (1384, 1384, r"\[ R(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i) \]", "haute",
  "§68 « En apprentissage supervisé : [R()=1n _{i=1}^{n} L(f_(x_i),y_i)] ». \\frac{1}{n} réduit à 1n, \\sum réduit à \\_, le \\theta de f_θ détruit.",
  "Risque empirique — rendu : R(θ)=(1/n)Σ L(f_θ(x_i),y_i)."),

 (1388, 1388, r"\[ \min_\theta R(\theta) \]", "haute",
  "§68 « On cherche : [vide] ». Le principe ERM minimise le risque empirique.",
  "Rendu : min_θ R(θ)."),

 (1396, 1396, r"\[ \|\theta\|\leq C \]", "haute",
  "§69 « On peut imposer : [||C] ou ajouter : [||] ». Le \\theta et le \\leq ont été détruits, \\| a perdu sa contre-oblique.",
  "Contrainte de norme — rendu : ‖θ‖≤C."),

 (1400, 1400, r"\[ \|\theta\| \]", "moyenne",
  "§69 « ou ajouter : [||] ». Même résidu qu'en l. 1396, mais sans la borne : c'est le terme de pénalité ajouté à la perte.",
  "Un coefficient λ a pu précéder la norme (le grec est détruit sans laisser de trace) ; le résidu ne montre que ‖θ‖."),

 # ---------- 70-78 : classification, réseaux, hyperparamètres, RL, robotique ----------
 (1416, 1416, r"\[ \min_\theta\frac{1}{n}\sum_i L(y_i,f_\theta(x_i)) \]", "haute",
  "§70 « Exemple conceptuel : [_ 1n _i L(y_i,f_(x_i))] ». Le \\min_\\theta, le \\frac, le \\sum et le \\theta de f_θ ont été détruits.",
  "Rendu : min_θ (1/n)Σ L(y_i,f_θ(x_i))."),

 (1424, 1424, r"\[ \theta \]", "moyenne",
  "§71 « Un réseau neuronal possède des paramètres : [vide] et produit : [ŷ=f_θ(x)] ». Le bloc nomme les paramètres.",
  "Candidat alternatif : \\[ \\theta=(W,b) \\] — forme donnée en l. 1448 pour les paramètres."),

 (1428, 1428, r"\[ \hat{y}=f_\theta(x) \]", "haute",
  "§71 « et produit : [y=f_(x)] ». Le chapeau et le \\theta ont été détruits.", "Rendu : ŷ=f_θ(x)."),

 (1432, 1432, r"\[ \theta^{*}=\arg\min_\theta L(f_\theta(x),y) \]", "haute",
  "§71 « L'entraînement cherche : [^\\*=_L(f_(x),y)] ». Le \\theta, le \\arg\\min et le \\theta de f_θ ont été détruits.",
  "Rendu : θ*=argmin_θ L(f_θ(x),y)."),

 (1436, 1436, None, "inconnue",
  "§71 « La chaîne complète est : [vide] ». Une chaîne, mais le nombre et la nature des maillons ne sont pas déterminés.",
  "Candidat : \\[ x\\to f_\\theta(x)\\to L\\to\\nabla_\\theta L\\to\\theta_{t+1} \\]."),

 (1470, 1470, r"\[ \mathcal{H}=H_1\times H_2\times\cdots\times H_k \]", "haute",
  "§73 « On définit une grille : [=H_1H_2H_k] ». Le \\mathcal{H}, les \\times et le \\cdots ont été détruits.",
  "Produit cartésien des ensembles d'hyperparamètres."),

 (1486, 1486, r"\[ L(h) \]", "moyenne",
  "§75 « On peut modéliser : [h] et sélectionner progressivement les hyperparamètres les plus prometteurs. ». Le bloc ne peut pas être la variable seule : on modélise une réponse. Le §136 (l. 2811) écrit h*=argmin_h L_val(h), ce qui montre que J modélise bien L comme fonction de h.",
  "Candidat alternatif : \\[ L_{\\text{val}}(h) \\]."),

 (1496, 1496, r"\[ J(\theta)=\mathbb{E}\left[\sum_{t}\gamma^{t}r_t\right] \]", "moyenne",
  "§76 « l'agent cherche à maximiser une récompense cumulée : [J()=] ». Le membre de droite a été entièrement détruit — il ne contenait que des commandes et des lettres grecques.",
  "Récompense cumulée actualisée. L'absence ou la présence du facteur d'actualisation γ est un choix d'auteur ; l'espérance, elle, est certaine (le §76 parle d'un agent dans un environnement stochastique)."),

 (1500, 1500, r"\[ \max_\theta J(\theta) \]", "haute",
  "§76 « L'objectif devient : [vide] ». La forme est donnée mot pour mot par la forme 8 du §112 (l. 2287), lisible.",
  "Rendu : max_θ J(θ)."),

 (1508, 1508, r"\[ \tau(t) \]", "haute",
  "§77 « Une trajectoire peut être représentée par : [(t)] ». Le \\tau a été détruit.", "Rendu : τ(t)."),

 (1512, 1516, None, "inconnue",
  "§77 « On peut minimiser : [cinq lignes] sous des contraintes : obstacles, vitesse, accélération, articulation, énergie. ». Un coût J(τ) décomposé en quatre termes, tous détruits.",
  "Candidats : J_longueur, J_énergie, J_temps, J_sécurité. La liste des contraintes qui suit suggère d'autres découpages — à trancher par l'auteur."),

 (1528, 1528, r"\[ \min_\tau J(\tau) \]", "moyenne",
  "§77 « On obtient : [vide] ». Après l'énoncé des contraintes, le bloc énonce le problème complet.",
  "La mention explicite des contraintes (s.c. τ∈𝒯) a pu figurer dans le bloc."),

 (1534, 1536, None, "inconnue",
  "§78 logistique « Exemple : [trois lignes : une parenthèse ouvrante, une ligne vide, « - ) »] sous : capacité des véhicules, disponibilité, demandes, horaires, contraintes géographiques. ».",
  "Le même gabarit « ( / - ) » réapparaît en l. 2688. Candidat : une somme de coûts de transport \\[ \\sum_{i,j}c_{ij}x_{ij} \\] encadrée par \\left( \\right)."),

 # ---------- 79-89 : scheduling, allocation, réseaux, finance, vision, signal ----------
 (1552, 1552, r"\[ T_1,T_2,\ldots,T_n \]", "haute", "§79 « Supposons : [T_1,T_2,,T_n] ». Le \\ldots est devenu une virgule.", "Rendu : T₁,T₂,…,T_n."),
 (1556, 1556, r"\[ M_1,M_2,\ldots,M_k \]", "haute", "§79 « à affecter à : [M_1,M_2,,M_k] ».", "Rendu : M₁,M₂,…,M_k."),
 (1560, 1560, r"\[ C_{\max} \]", "haute",
  "§79 « On peut chercher à minimiser : [C_{}] où (C_max) représente le temps de fin global. ». Le \\max a été détruit ; la prose qui suit nomme C_max.", "Makespan."),
 (1580, 1580, r"\[ A_1,\ldots,A_n \]", "haute", "§80 « et de plusieurs activités : [A_1,,A_n] ».", "Rendu : A₁,…,A_n."),
 (1588, 1588, r"\[ \sum_i x_i\leq R \]", "haute", "§80 « sous : [\\_i x_iR] ». Le \\sum et le \\leq ont été détruits.", "Rendu : Σ x_i≤R."),
 (1614, 1614, r"\[ \min_P C(P) \]", "haute", "§81 « ### Routage [\\_P (P)] ». Le \\min et le C ont été détruits.", "Identique à la l. 75."),
 (1618, 1618, r"\[ \max_x\sum_i U_i(x_i) \]", "haute",
  "§81 « ### Allocation de bande passante [\\_x \\_i U_i(x_i)] sous : [\\_i x_iC] ». Le \\max et le \\sum ont été détruits.",
  "Somme d'utilités — l'allocation est un maximum, pas un minimum."),
 (1622, 1622, r"\[ \sum_i x_i\leq C \]", "haute", "§81 « sous : [\\_i x_iC] où (C) représente une capacité réseau. ».", "Rendu : Σ x_i≤C."),
 (1630, 1630, r"\[ w=(w_1,\ldots,w_n) \]", "haute", "§82 « Un portefeuille peut être représenté par : [w=(w_1,,w_n)] ».", "Rendu : w=(w₁,…,w_n)."),

 (1634, 1636, "\\[ \\max_w\\left(w^{T}\\mu\n\n- \\lambda w^{T}\\Sigma w\\right) \\]", "moyenne",
  "§82 « On peut chercher à optimiser : [trois lignes] sous : [Σw_i=1] et éventuellement : [w_i≥0]. L'optimisation permet donc de formaliser les compromis entre rendement, risque et contraintes. ».",
  "Les deux contraintes qui ont survécu (somme des poids égale à 1, poids non négatifs) sont exactement celles de Markowitz, et la phrase de clôture nomme les deux termes : rendement et risque. Le facteur λ et sa place restent un choix d'auteur."),

 (1640, 1640, r"\[ \sum_i w_i=1 \]", "haute", "§82 « sous : [\\_i w_i=1] ». Le \\sum a été détruit.", "Rendu : Σ w_i=1."),
 (1644, 1644, r"\[ w_i\geq 0 \]", "haute", "§82 « et éventuellement : [w_i] ». Le \\geq a été détruit.", "Rendu : w_i≥0."),

 (1664, 1664, r"\[ \theta^{*}=\arg\min_\theta\|R(\theta)-I\|^{2} \]", "haute",
  "§83 « Exemple : [^\\*=_ |R()-I|^2] où (R(θ)) représente un rendu et (I) une image cible. ». Le \\theta, le \\arg\\min et le \\| ont été détruits.",
  "Moindres carrés entre rendu et image cible."),

 (1676, 1676, r"\[ x^{*}=\arg\min_x E(x) \]", "haute", "§84 « Exemple conceptuel : [x^\\*=\\_x E(x)] ». Le \\arg\\min réduit à \\_.", "Minimisation d'énergie."),

 (1702, 1702, r"\[ \min_\theta\sum_i L_i(\theta) \]", "haute", "§85 « Une grande partie de ces problèmes peut être formulée sous forme : [_ \\_i L_i()] ». Le \\min_\\theta et le \\sum ont été détruits.", "Somme de pertes."),

 (1708, 1708, r"\[ y=Ax+\epsilon \]", "haute", "§86 « à partir d'observations bruitées : [y=Ax+] ». Le \\epsilon a été détruit.", "Modèle linéaire bruité."),

 (1712, 1714, "\\[ x^{*}=\\arg\\min_x\\|Ax-y\\|^{2}\n\n+ \\lambda R(x) \\]", "haute",
  "§86 « Puis : [trois lignes] Cette formulation apparaît notamment dans : ». Le \\arg\\min, le \\|, le \\lambda et le + de tête de ligne (devenu une puce -) ont été détruits.",
  "Régularisation de Tikhonov — reconstruction par moindres carrés régularisés."),

 (1742, 1742, r"\[ \delta \]", "haute",
  "§88 « on peut chercher une perturbation : [vide] maximisant la perte : […] ». La perturbation est nommée par les deux blocs suivants, qui la contiennent.",
  "Rendu : δ."),

 (1746, 1746, r"\[ \max_{\|\delta\|\leq\epsilon}L(x+\delta,y) \]", "haute",
  "§88 « maximisant la perte : [\\_{} L(x+,y)] sous : [||] ». Le \\max, le sous-script complet et le \\delta ont été détruits.",
  "Attaque adversariale bornée."),

 (1750, 1750, r"\[ \|\delta\|\leq\epsilon \]", "haute",
  "§88 « sous : [||] On obtient un problème d'optimisation sous contrainte. ». Le résidu || est exactement ce que laisse \\|δ\\|≤ε quand δ et ε (grecs) et \\leq sont détruits.",
  "Borne sur la perturbation."),

 (1760, 1760, r"\[ \min_x\sum_{i=1}^{N}f_i(x) \]", "haute", "§89 « Lorsque les données ou calculs sont répartis entre plusieurs machines : [_x_ {i=1}^{N} f_i(x)] ». Le \\min et le \\sum ont été détruits.", "Somme fédérée."),
 (1781, 1781, r"\[ \min_\theta\sum_{k=1}^{K}p_kF_k(\theta) \]", "haute", "§90 « On cherche : [{k=1}^{K} p_k F_k()] ». Le \\min_\\theta et le \\sum ont été détruits.", "Moyenne pondérée des objectifs locaux — FedAvg."),
 (1806, 1806, r"\[ x_1,x_2,x_3,\ldots \]", "haute", "§91 « on reçoit : [x_1,x_2,x_3,] ». Le \\ldots a été détruit.", "Flux de données."),

 # ---------- 92-98 : temps réel, approximation, complexité, relaxation ----------
 (1824, 1824, r"\[ \min_x f(x) \]", "moyenne",
  "§92 « Il faut donc parfois optimiser : [vide] sous : [T] ». Le second bloc porte la contrainte de temps ; le premier est l'objectif.",
  "Candidat alternatif : \\[ f(x) \\] sans l'opérateur."),

 (1828, 1828, r"\[ t\leq T \]", "haute", "§92 « sous : [T] ». Le \\leq et le t ont été détruits.", "Contrainte de latence."),

 (1832, 1832, None, "inconnue",
  "§92 « Cela introduit un compromis entre : [vide] ». Un seul bloc pour ce qui est annoncé comme un compromis.",
  "Candidat : \\[ \\text{qualité de la solution} \\] et \\[ \\text{temps de calcul} \\] ont pu tenir dans ce bloc."),

 (1844, 1844, r"\[ \hat{x} \]", "moyenne",
  "§93 « ### Solution exacte [x^\\*] ### Solution approximative [x] ». La solution approchée est notée par un chapeau, détruit.",
  "Rendu : x̂. Le §93 oppose x* (exact) à x̂ (approché) ; le chapeau est la notation la plus courante."),

 (1848, 1848, r"\[ f(\hat{x})\leq\alpha f(x^{*}) \]", "moyenne",
  "§93 « avec une garantie : [f(x) f(x^\\*)] dans certains problèmes de minimisation. ». Le résidu montre exactement deux termes séparés par des commandes détruites — donc un opérateur de comparaison et éventuellement un facteur grec, mais aucun signe + ou - n'a survécu.",
  "Garantie d'approximation : f(x̂)≤α·f(x*). L'absence de signe + écarte la forme additive f(x̂)≤f(x*)+ε. La restriction « dans certains problèmes de minimisation » est caractéristique du rapport d'approximation α."),

 (1860, 1860, None, "inconnue",
  "§94 « Un problème peut être facile à formuler mais difficile à résoudre. Il faut donc distinguer : [vide] ».",
  "Candidat : \\[ \\text{formuler} \\] et \\[ \\text{résoudre} \\] — l'opposition que la phrase énonce."),

 (1878, 1878, r"\[ S_1,S_2,\ldots \]", "haute",
  "§95 « Branch and Bound divise l'espace des solutions : [\\_1,\\_2,] ». Le \\ldots est devenu une virgule, le symbole de sous-ensemble a été détruit.",
  "Rendu : S₁,S₂,…"),

 (1884, 1884, None, "inconnue", "§95 « Schéma : [vide] ».", "Candidat : un arbre de partition ASCII, analogue à la chaîne du §122."),

 (1892, 1892, r"\[ x_i\in\{0,1\} \]", "haute", "§96 « Exemple : [x_i{0,1}] devient : [0x_i] On obtient une relaxation continue. ». Le \\in a été détruit, les accolades ont perdu leurs contre-obliques.", "Rendu : x_i∈{0,1}."),

 (1896, 1896, r"\[ 0\leq x_i\leq 1 \]", "moyenne",
  "§96 « devient : [0x_i] On obtient une relaxation continue. ». Le résidu ne montre que le 0 et la variable : les deux \\leq et le 1 ont été détruits.",
  "La relaxation continue d'une variable binaire est nécessairement l'intervalle [0,1] ; le résidu seul ne prouve pas la borne supérieure. Même motif qu'en l. 473 (lot 5a) : à confirmer par l'auteur."),

 # ---------- 101-108 : normalisation, convergence, ordres, erreurs ----------
 (1975, 1975, r"\[ [0,1] \]", "haute", "§101 « Si une caractéristique varie entre : [01] ». Les crochets et la virgule ont été détruits.", "Rendu : [0,1]."),
 (1979, 1979, r"\[ [0,10^{6}] \]", "haute", "§101 « et une autre entre : [010^6] ». Même destruction.", "Rendu : [0,10⁶]."),
 (2006, 2006, r"\[ x_t\to x^{*} \]", "haute", "§103 « Exemple : [x_tx^\\*] ou : [f(x_t)f(x^\\*)] ». Les flèches ont été détruites.", "Convergence des itérés."),
 (2010, 2010, r"\[ f(x_t)\to f(x^{*}) \]", "haute", "§103, second critère.", "Convergence des valeurs."),
 (2039, 2041, None, "inconnue",
  "§105 « Le coût d'un optimiseur dépend de : [trois lignes] Pour les modèles modernes, le coût total est souvent dominé par l'évaluation répétée du modèle et des gradients. ».",
  "Candidats : \\[ \\text{nombre d'itérations} \\] et \\[ \\text{coût par itération} \\] — les deux facteurs dont le produit donne le coût total annoncé juste après."),
 (2051, 2051, r"\[ \nabla f \]", "haute", "§106 « ### Premier ordre / Utilisent principalement : [f] ». Le \\nabla a été détruit.", "Rendu : ∇f."),
 (2064, 2064, r"\[ \nabla^{2}f \]", "haute", "§106 « ### Second ordre / Utilisent : [^2f] ou une approximation. ». Le \\nabla a été détruit.", "Rendu : ∇²f."),
 (2135, 2135, r"\[ \nabla f(x)=0 \]", "haute", "§108 « ## Erreur 1 — Confondre minimum local et global [f(x)=0] ne garantit pas l'optimalité globale. ». Le \\nabla a été détruit.", "Rendu : ∇f(x)=0."),
 (2162, 2162, r"\[ L_{\text{train}} \]", "haute", "§108 « ## Erreur 6 — Confondre perte d'entraînement et performance réelle [L_{}] n'implique pas nécessairement : [L_{}] ».", "Même paire qu'au §48."),
 (2166, 2166, r"\[ L_{\text{test}} \]", "haute", "§108, erreur 6, second terme.", "Rendu : L_test."),

 (2174, 2174, None, "inconnue",
  "§109 « Il faut suivre une chaîne : [vide] C'est cette chaîne qui transforme les mathématiques en système exploitable. ».",
  "Piste : le §122 (l. 2464-2484) déploie en ASCII une chaîne de dix étapes intacte (Problem → Variables → Objective → Constraints → Model → Optimizer → Iteration → Evaluation → Stopping criterion → Solution → Validation). Le bloc de la l. 2174 en est vraisemblablement le résumé, mais sa forme exacte reste à fixer."),

 # ---------- 112 : FORMES IMPORTANTES À RECONNAÎTRE ----------
 (2237, 2237, r"\[ \min_x f(x) \]", "haute", "§112 forme 1 « → optimisation générale ».", "Rendu : min_x f(x)."),
 (2243, 2243, r"\[ \min_x c^{T}x \]", "haute", "§112 forme 2 « → programmation linéaire ».", "Rendu : min_x c^T x."),
 (2247, 2247, r"\[ Ax\leq b \]", "haute", "§112 forme 2 « sous : [Axb] ». Le \\leq a été détruit.", "Rendu : Ax≤b."),
 (2253, 2253, r"\[ \min_x f(x) \]", "haute", "§112 forme 3 « → optimisation contrainte / Lagrangien ».", "Rendu : min_x f(x)."),
 (2263, 2263, r"\[ \min_x f(x)+R(x) \]", "haute", "§112 forme 4 « → régularisation ».", "Rendu : min_x f(x)+R(x)."),
 (2269, 2269, r"\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]", "haute",
  "§112 forme 5 « → gradient descent » : [x_{t+1}=x_t-f(x_t)]. Le \\eta et le \\nabla ont été détruits.",
  "Rendu : x_{t+1}=x_t−η∇f(x_t). C'est cette forme intacte qui a servi de référence à la l. 759 (lot 5a)."),
 (2275, 2275, r"\[ x_{t+1}=x_t-H^{-1}\nabla f \]", "haute", "§112 forme 6 « → Newton » : [x_{t+1}=x_t-H^{-1}f]. Le \\nabla a été détruit.", "Rendu : x_{t+1}=x_t−H^{-1}∇f."),
 (2281, 2281, r"\[ \min_x\mathbb{E}[f(x,\xi)] \]", "haute", "§112 forme 7 « → optimisation stochastique » : [\\_x \\[f(x,)\\]]. Le \\mathbb{E} et le \\xi ont été détruits.", "Rendu : min_x 𝔼[f(x,ξ)]."),
 (2287, 2287, r"\[ \max_\theta J(\theta) \]", "haute", "§112 forme 8 « → optimisation de politique en reinforcement learning » : [\\_J()]. Le \\max et le \\theta ont été détruits.", "Rendu : max_θ J(θ)."),

 # ---------- 114 : STRUCTURES MATHÉMATIQUES À MAÎTRISER ----------
 (2339, 2339, r"\[ \nabla f \]", "haute", "§114, premier item de la liste de structures. Le \\nabla a été détruit.", "Gradient."),
 (2341, 2341, r"\[ \nabla^{2}f \]", "haute", "§114, deuxième item : [^2f].", "Hessienne."),
 (2345, 2345, r"\[ \mathcal{L}(x,\lambda) \]", "haute", "§114, quatrième item : [(x,)]. Le \\mathcal{L} et le \\lambda ont été détruits.", "Lagrangien."),
 (2347, 2347, r"\[ Ax\leq b \]", "haute", "§114 : [Axb]. Le \\leq a été détruit.", "Rendu : Ax≤b."),
 (2349, 2349, r"\[ x\geq 0 \]", "haute", "§114 : [x]. Le \\geq a été détruit.", "Rendu : x≥0."),
 (2351, 2351, r"\[ x\in\{0,1\} \]", "haute", "§114 : [x{0,1}]. Le \\in a été détruit.", "Rendu : x∈{0,1}."),
 (2353, 2353, r"\[ \|x\|_1 \]", "haute", "§114 : [||\\_1]. Le \\| a perdu sa contre-oblique, la variable a été détruite.", "Norme L1."),
 (2355, 2355, r"\[ \|x\|_2 \]", "haute", "§114 : [||\\_2].", "Norme L2."),
 (2357, 2357, None, "inconnue",
  "§114, dixième item — bloc vide entre la norme L2 et l'espérance. Deux blocs consécutifs (l. 2357 et l. 2359) manquent dans une liste par ailleurs parfaitement lisible.",
  "Candidats : \\[ \\sum_i f_i(x) \\] et \\[ DP[s] \\], tous deux présents ailleurs dans le document (l. 1760 et l. 716)."),
 (2359, 2359, None, "inconnue", "§114, onzième item — bloc vide.", "Voir l. 2357."),
 (2361, 2361, r"\[ \mathbb{E}[f(x,\xi)] \]", "haute", "§114 : [\\[f(x,)\\]]. Le \\mathbb{E} et le \\xi ont été détruits ; les crochets de l'espérance ont survécu.", "Rendu : 𝔼[f(x,ξ)]."),
 (2363, 2363, r"\[ (f_1,\ldots,f_k) \]", "haute", "§114 : [(f_1,,f_k)]. Le \\ldots est devenu une virgule.", "Vecteur d'objectifs."),

 # ---------- 115-120 : relations avec les autres domaines ----------
 (2379, 2379, None, "inconnue",
  "§115 « Le Domaine I répond notamment à : Comment une fonction varie-t-elle ? Le Domaine J demande : Comment exploiter cette variation pour trouver une solution optimale ? Ainsi : [vide] Et : [vide] ».",
  "Candidats : \\[ \\nabla f(x)=0 \\] puis \\[ x_{t+1}=x_t-\\eta\\nabla f(x_t) \\] — la condition d'optimalité, puis l'algorithme qui l'exploite."),
 (2383, 2383, None, "inconnue", "§115, second bloc de la relation avec le Domaine I.", "Voir l. 2379."),
 (2389, 2389, r"\[ \min_x\mathbb{E}[f(x,\xi)] \]", "haute", "§116 « L'optimisation peut porter sur une espérance : [\\_x \\[f(x,)\\]] ».", "Identique à la forme 7."),
 (2397, 2397, r"\[ \theta^{*}=\arg\min_\theta L(\theta) \]", "haute", "§117 « L'estimation statistique peut devenir : [^\\*=_ L()] ou : […] Le maximum de vraisemblance est donc naturellement relié à l'optimisation. ».", "Moindres carrés / minimisation de perte."),
 (2401, 2401, r"\[ \theta^{*}=\arg\max_\theta \mathcal{L}(\theta) \]", "moyenne",
  "§117, second bloc : [^\\*=_ ()] — la fonction a été détruite, ce qui désigne une commande (\\mathcal{L} ou \\ell), pas une lettre latine. La phrase qui suit nomme le maximum de vraisemblance.",
  "Maximum de vraisemblance. Le symbole de la vraisemblance (𝓛 ou ℓ) est un choix d'auteur."),
 (2409, 2409, r"\[ x\in\mathcal{X} \]", "haute", "§118 « Lorsque l'espace de solutions est discret : [x] l'optimisation combinatoire devient centrale. ».", "Rendu : x∈𝓧 — identique à la l. 690."),
 (2444, 2444, r"\[ H(x)p=-\nabla f(x) \]", "haute", "§120 « Newton, par exemple, nécessite de résoudre : [H(x)p=-f(x)] plutôt que nécessairement de calculer explicitement (H^{-1}). ». Le \\nabla a été détruit.", "Système de Newton — direction de descente."),

 # ---------- 126-131 : expérimentation, robustesse, trade-offs ----------
 (2573, 2575, None, "inconnue",
  "§126 « Une bonne expérimentation compare : [trois lignes] et mesure : [trois lignes] Il faut éviter de conclure sur une seule exécution… ».",
  "Candidats : comparer \\[ \\text{plusieurs algorithmes} \\] / \\[ \\text{plusieurs taux d'apprentissage} \\], mesurer \\[ \\text{la convergence} \\] / \\[ \\text{la stabilité entre runs} \\] (cette dernière expression figure l. 2573)."),
 (2579, 2581, None, "inconnue", "§126, second bloc : « et mesure : [trois lignes] ».", "Voir l. 2573."),
 (2595, 2595, r"\[ f(x^{*}+\delta) \]", "haute",
  "§127 « Il faut parfois demander : [f(x^\\*)] mais aussi : [f(x^\\*+)] pour de petites perturbations (δ). ». Le \\delta a été détruit ; la prose qui suit le nomme.",
  "Évaluation de la robustesse — la valeur de l'objectif après perturbation."),
 (2607, 2607, None, "inconnue", "§128 « Par exemple : [quatre blocs vides] Comprendre l'optimisation signifie donc aussi comprendre les **compromis**. ».", "Candidats : coût / qualité / temps / robustesse — les quatre critères énumérés au §153 (l. 3355-3358)."),
 (2609, 2609, None, "inconnue", "§128, deuxième bloc.", "Voir l. 2607."),
 (2611, 2611, None, "inconnue", "§128, troisième bloc.", "Voir l. 2607."),
 (2613, 2613, None, "inconnue", "§128, quatrième bloc.", "Voir l. 2607."),
 (2649, 2649, None, "inconnue",
  "§131 « ### Réseau / Minimiser la latence ou maximiser le débit. Ainsi : [vide] Cette formule est volontairement conceptuelle… ».",
  "Candidat : \\[ \\min\\ \\text{latence}\\ \\text{ou}\\ \\max\\ \\text{débit} \\]."),
 (2688, 2690, None, "inconnue", "§131 « Exemple conceptuel : [trois lignes : « ( », ligne vide, « - ) »] ». Même gabarit qu'en l. 1534.", "Voir l. 1534."),

 # ---------- 133-140 : agents, Stane OS, planification, robotique, réseaux ----------
 (2722, 2722, r"\[ a_1,a_2,\ldots,a_T \]", "haute", "§133 « ### Planification / Choisir une séquence d'actions : [a_1,a_2,,a_T] ». Le \\ldots est devenu une virgule.", "Rendu : a₁,a₂,…,a_T."),
 (2732, 2734, None, "inconnue", "§133 « ### Coût / Minimiser : [trois lignes] ».", "Candidat : \\[ C(a) \\] — le coût d'une action, par symétrie avec le bloc J(a)=Q(a)−C(a)−T(a)−E(a) de la l. 2746."),

 (2746, 2750, "\\[ J(a)=Q(a)\n\n- C(a)\n- T(a)\n- E(a) \\]", "haute",
  "§133 « On peut donc construire : [cinq lignes] où : (Q) = qualité ; (C) = coût ; (T) = temps ; (E) = erreurs. ». Les lettres ont survécu, leurs arguments et les parenthèses ont été détruits.",
  "Objectif multi-critères d'un agent : qualité moins coût, moins temps, moins erreurs. Les quatre lettres et leurs sens sont donnés mot pour mot par la liste qui suit."),

 (2765, 2765, r"\[ A_1,A_2,\ldots,A_n \]", "haute", "§134 « Supposons plusieurs agents : [A_1,A_2,,A_n] ». Le \\ldots est devenu une virgule.", "Rendu : A₁,A₂,…,A_n."),
 (2771, 2771, None, "inconnue",
  "§134 « Le système doit déterminer : [vide] » — un seul bloc. Les objectifs, eux, sont donnés en liste et ont survécu : minimiser temps, coût, redondance ; maximiser qualité, fiabilité, couverture (l. 2775-2783).",
  "Candidat : \\[ x_{ij}\\in\\{0{,}1\\} \\] — la variable d'affectation d'une tâche à un agent, puisque la section se conclut sur « un problème d'allocation et de scheduling » (l. 2785)."),
 (2791, 2793, None, "inconnue",
  "§135 Stane OS « Dans un système personnel intelligent, on peut théoriquement optimiser : [J = / - ] Le système peut alors décider : quel modèle utiliser, quel outil appeler… ».",
  "Même gabarit qu'au §133 : un objectif en deux termes. Candidat : \\[ J=Q\n\n- C \\]."),
 (2811, 2811, r"\[ h^{*}=\arg\min_h L_{\text{val}}(h) \]", "haute", "§136 « On cherche : [h^\\*=_h L_{}(h)] où (h) représente les hyperparamètres. ». Le \\arg\\min et le contenu de \\text{…} ont été détruits.", "Rendu : h*=argmin_h L_val(h)."),
 (2817, 2817, None, "inconnue", "§136 « Cela donne : [vide] ».", "Candidat : \\[ h_1,h_2,\\ldots \\] — la suite des configurations retenues."),
 (2823, 2823, r"\[ P=(a_1,a_2,\ldots,a_n) \]", "haute", "§137 « Un plan est une séquence : [P=(a_1,a_2,,a_n)] ».", "Rendu : P=(a₁,a₂,…,a_n)."),
 (2827, 2827, r"\[ J(P)=\text{coût}(P) \]", "moyenne",
  "§137 « On peut définir : [J(P)=(P)] et chercher : [P^\\*=\\_P J(P)] ». Le membre de droite ne conserve que les parenthèses : la fonction a été détruite, donc c'était une commande (\\text{…}).",
  "Le coût d'un plan. Le libellé exact (coût, qualité, valeur) est un choix d'auteur."),
 (2831, 2831, r"\[ P^{*}=\arg\min_P J(P) \]", "haute", "§137 « et chercher : [P^\\*=\\_P J(P)] ». Le \\arg\\min réduit à \\_.", "Rendu : P*=argmin_P J(P)."),
 (2839, 2839, None, "inconnue", "§138 « Chaîne : [vide] ».", "Candidat : \\[ \\text{perception}\\to\\text{planification}\\to\\text{contrôle} \\]."),
 (2847, 2849, None, "inconnue", "§139 « Un système logistique peut optimiser simultanément : [trois lignes] Cela produit souvent des problèmes multi-objectifs, combinatoires ou mixtes. ».", "Candidats : \\[ \\text{coût} \\] et \\[ \\text{délai} \\]."),
 (2857, 2857, None, "inconnue", "§140 « On peut optimiser : [cinq blocs vides] La théorie des graphes et l'optimisation se complètent alors directement. ».", "Candidats : latence, débit, coût, fiabilité, énergie."),
 (2859, 2859, None, "inconnue", "§140, deuxième bloc.", "Voir l. 2857."),
 (2861, 2861, None, "inconnue", "§140, troisième bloc.", "Voir l. 2857."),
 (2863, 2863, None, "inconnue", "§140, quatrième bloc.", "Voir l. 2857."),
 (2865, 2865, None, "inconnue", "§140, cinquième bloc.", "Voir l. 2857."),

 # ---------- 141-147 : projets et exercices ----------
 (2879, 2879, r"\[ x_0,x_1,x_2,\ldots \]", "haute", "§141 projet 1 « puis la trajectoire : [x_0,x_1,x_2,] ». Le \\ldots a été détruit.", "Rendu : x₀,x₁,x₂,…"),
 (2928, 2928, r"\[ Ax\leq b \]", "haute", "§143 projet 4 « sous : [Axb] ». Le \\leq a été détruit.", "Rendu : Ax≤b."),
 (2994, 2997, "\\[ J(a)=Q(a)\n\n- C(a)\n- T(a) \\]", "haute",
  "§145 projet avancé « Pour chaque action : [quatre lignes] L'agent choisit l'action maximisant (J). ». Même gabarit que la l. 2746, sans le terme d'erreur.",
  "Objectif d'action : qualité moins coût moins temps."),
 (3042, 3042, None, "inconnue",
  "§147 exercice 2 « Appliquer gradient descent à : [f(x)=x²] avec : [vide] et : [x_0=10] Calculer plusieurs itérations. ». Le bloc manquant est le pas d'apprentissage.",
  "Candidat : \\[ \\eta=0{,}1 \\]. La valeur est un choix d'auteur — un exercice a besoin d'un nombre, mais ce nombre ne se déduit pas du document."),
 (3054, 3054, r"\[ \min_{x,y}x^{2}+y^{2} \]", "haute",
  "§147 exercice 3 « Résoudre avec Lagrange : [\\_{x,y}x<sup>2+y</sup>2] sous : [x+y=1] ». Le \\min réduit à \\_ ; l'artefact <sup> a fusionné les deux exposants.",
  "Exercice canonique de Lagrange : minimiser x²+y² sous x+y=1, dont la solution est x=y=1/2. Le second bloc (l. 3058) confirme la contrainte."),

 # ---------- 152 : utiliser l'IA ----------
 (3091, 3091, None, "inconnue",
  "§152 « Demander à une IA : « … Identifie d'abord les variables, l'objectif, les contraintes… » Puis comparer : [vide] ».",
  "Candidat : \\[ \\text{la modélisation produite} \\] et \\[ \\text{la vôtre} \\] — l'exercice consiste à confronter deux modélisations."),

 # ---------- 154 : SYNTHÈSE CONCEPTUELLE ----------
 (3372, 3372, r"\[ \min_{x\in\mathcal{X}}f(x) \]", "moyenne",
  "§154 « Le Domaine J peut être résumé par la chaîne : [vide] Pour le machine learning : [vide] Pour un système : [vide] ». Le premier bloc résume le domaine entier.",
  "Candidat alternatif : \\[ \\min_x f(x)\\ \\text{sous}\\ g_i(x)\\leq 0 \\]."),
 (3376, 3376, r"\[ \min_\theta L(\theta) \]", "moyenne", "§154 « Pour le machine learning : [vide] ».", "Forme documentée en l. 1004 et l. 1388."),
 (3380, 3380, None, "inconnue", "§154 « Pour un système : [vide] ».", "Candidat : \\[ J=Q-C-T-E \\] (l. 2746)."),

 # ---------- 155 : LA GRANDE CARTE DES DOMAINES ----------
 (3386, 3386, None, "inconnue",
  "§155 « La progression construite jusqu'ici peut être comprise comme : [dix blocs vides] La transition : [I→J] est particulièrement importante. ».",
  "Piste : le corpus compte dix domaines avant J (A, B, C, D, E, F, G, H, I puis J) et le bloc survivant \\[ IJ \\] montre que la notation est une flèche entre deux lettres. Candidat : les dix domaines A→…→J, la transition I→J étant celle que le texte met en avant."),
 (3388, 3388, None, "inconnue", "§155, deuxième bloc.", "Voir l. 3386."),
 (3390, 3390, None, "inconnue", "§155, troisième bloc.", "Voir l. 3386."),
 (3392, 3392, None, "inconnue", "§155, quatrième bloc.", "Voir l. 3386."),
 (3394, 3394, None, "inconnue", "§155, cinquième bloc.", "Voir l. 3386."),
 (3396, 3396, None, "inconnue", "§155, sixième bloc.", "Voir l. 3386."),
 (3398, 3398, None, "inconnue", "§155, septième bloc.", "Voir l. 3386."),
 (3400, 3400, None, "inconnue", "§155, huitième bloc.", "Voir l. 3386."),
 (3402, 3402, None, "inconnue", "§155, neuvième bloc.", "Voir l. 3386."),
 (3404, 3404, None, "inconnue", "§155, dixième bloc.", "Voir l. 3386."),

 (3414, 3414, r"\[ \nabla f \]", "moyenne",
  "§155 « Le calcul différentiel fournit les outils permettant de comprendre : [vide] L'optimisation transforme ces informations en : [vide] Et le machine learning assemble ensuite : [vide] ».",
  "Le §115 pose que le Domaine I répond à « Comment une fonction varie-t-elle ? », et le §114 ouvre sa liste de structures par ∇f. Candidat alternatif : \\[ \\nabla f,\\nabla^{2}f \\]."),
 (3418, 3418, r"\[ x_{t+1}=x_t-\eta\nabla f(x_t) \]", "moyenne",
  "§155, deuxième maillon : « L'optimisation transforme ces informations en : [vide] ».",
  "Candidat alternatif : \\[ \\min_x f(x) \\]."),
 (3422, 3422, r"\[ \min_\theta L(\theta) \]", "moyenne",
  "§155, troisième maillon : « Et le machine learning assemble ensuite : [vide] pour produire des systèmes capables d'apprendre. ».",
  "Candidat alternatif : \\[ \\theta^{*}=\\arg\\min_\\theta L(\\theta) \\]."),

 # ---------- 156 : FORMULE MENTALE FINALE ----------
 (3432, 3432, r"\[ \text{l'objectif} \]", "moyenne",
  "§156 « **Qu'est-ce que je cherche à améliorer ?** [vide] ». La question est intacte en gras ; le bloc est sa réponse.",
  "Primitive nommée au §3.2 (fonction objectif) et question 1 du §110 (« Que veut-on optimiser ? »). Le libellé exact est un choix d'auteur ; la case sémantique, elle, est fixée par la question."),
 (3436, 3436, r"\[ \text{les variables} \]", "moyenne",
  "§156 « **Qu'est-ce que je peux modifier ?** [vide] ».", "Primitive nommée au §3.1 (variable de décision) et question 2 du §110."),
 (3440, 3440, r"\[ \text{les contraintes} \]", "moyenne",
  "§156 « **Qu'est-ce que je n'ai pas le droit de violer ?** [vide] ».", "Primitive nommée au §3.5 (contrainte) et question 3 du §110."),
 (3444, 3444, r"\[ \text{la fonction objectif} \]", "moyenne",
  "§156 « **Comment mesurer une amélioration ?** [vide] ».", "Primitive nommée au §3.2 et au §125 (métriques de diagnostic)."),
 (3448, 3448, r"\[ \nabla f \]", "moyenne",
  "§156 « **Puis-je exploiter les dérivées ?** [vide] ».", "Question 5 du §110 (« La fonction est-elle différentiable ? ») et premier item du §114."),
 (3452, 3452, r"\[ \text{convexité} \]", "moyenne",
  "§156 « **Le problème est-il convexe ?** [vide] ».", "Question 6 du §110, reprise mot pour mot. Le §111 oppose « convexe / non convexe »."),
 (3456, 3456, r"\[ x\in\{0,1\} \]", "moyenne",
  "§156 « **Les solutions sont-elles discrètes ?** [vide] ».", "Question 7 du §110 (« continu ou discret ? ») ; le §114 donne x∈{0,1} comme structure de la discrétion."),
 (3460, 3460, r"\[ \text{optimisation bayésienne} \]", "moyenne",
  "§156 « **L'évaluation est-elle coûteuse ?** [vide] ».", "Question 8 du §110, et le §113 répond par une liste intacte : « Optimisation coûteuse — optimisation bayésienne ; surrogate models. »"),
 (3464, 3464, r"\[ (f_1,\ldots,f_k) \]", "moyenne",
  "§156 « **Ai-je plusieurs objectifs ?** [vide] ».", "Le §114 se termine sur (f₁,…,f_k), et le §111 oppose « mono-objectifs / multi-objectifs »."),
 (3468, 3468, r"\[ x^{*}\ \text{ou}\ \hat{x} \]", "moyenne",
  "§156 « **Ai-je besoin d'une solution exacte ?** [vide] ».", "Question 9 du §110, et le §93 oppose exactement \\[ x^{\\*} \\] et la solution approchée."),

 # ---------- 157 : CRITÈRE FINAL DE MAÎTRISE ----------
 (3476, 3476, r"\[ \text{un problème réel} \]", "moyenne",
  "§157 « Le Domaine J est suffisamment maîtrisé lorsque, face à un nouveau problème informatique, l'on peut spontanément effectuer la transformation : [vide] puis : [vide] puis : [vide] et enfin : [vide] ».",
  "Le §158, qui suit immédiatement, décrit cette transformation en prose intacte : l'optimisation « transforme une question générale « Que pourrais-je faire ? » en une question mathématiquement exploitable ». Les quatre maillons sont donc : problème → modèle → méthode → solution validée."),
 (3480, 3480, r"\[ \text{un modèle mathématique} \]", "moyenne", "§157, deuxième maillon.", "Voir l. 3476."),
 (3484, 3484, r"\[ \text{une méthode adaptée} \]", "moyenne", "§157, troisième maillon.", "Voir l. 3476."),
 (3488, 3488, r"\[ \text{une solution validée} \]", "moyenne", "§157, quatrième maillon.", "Voir l. 3476."),

 # ---------- 158 : SYNTHÈSE FINALE ----------
 (3506, 3506, r"\[ \min_\theta L(\theta) \]", "moyenne",
  "§158 « En machine learning : [vide] ». Le §2 (l. 65-69) pose exactement la même rubrique et la même forme.", "Reprise du §2, lisible en l. 1004."),
 (3510, 3510, r"\[ \min_\tau J(\tau) \]", "moyenne",
  "§158 « En robotique : [vide] ». Le §2 (l. 95-99) pose « Chercher une trajectoire : θ*=argmin_θ J(θ) ».", "Reprise du §2."),
 (3514, 3514, r"\[ \min\sum_{i,j}c_{ij}x_{ij} \]", "moyenne",
  "§158 « En logistique : [vide] ». Le §2 (l. 77-83) pose « Minimiser : [coûts] » et le §78 détaille le problème.", "Reprise du §2 — coût de transport."),
 (3518, 3518, r"\[ \min_P C(P) \]", "moyenne",
  "§158 « En réseaux : [vide] ». Le §2 (l. 71-75) pose « Chercher le chemin minimisant le coût : P*=argmin_P C(P) ».", "Reprise du §2."),
 (3522, 3522, r"\[ \max_\theta J(\theta) \]", "moyenne",
  "§158 « En systèmes intelligents : [vide] ». Forme 8 du §112 (l. 2287) : max_θ J(θ) → optimisation de politique en reinforcement learning.", "Le §133 propose une alternative multi-critères : J=Q−C−T−E."),
 (3526, 3526, None, "inconnue",
  "§158 « Et dans l'ingénierie logicielle : [vide] ». Rubrique absente du §2 : aucun équivalent survivant dans le document.",
  "Candidat : \\[ \\min\\ \\text{coût}\\ \\text{sous}\\ \\text{contrainte de qualité} \\] — d'après la question 10 du §110 (« Quel compromis entre qualité et temps de calcul est acceptable ? »)."),
 (3534, 3534, None, "inconnue",
  "§158 « Le Domaine I explique comment une fonction change. Le Domaine J explique comment exploiter cette information pour rechercher une solution. Ensemble : [vide] constitue l'une des chaînes mathématiques fondamentales de l'intelligence artificielle moderne. ».",
  "Candidat : \\[ I\\to J \\] — la notation employée au §155."),
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
