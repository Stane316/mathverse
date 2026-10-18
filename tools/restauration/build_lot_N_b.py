#!/usr/bin/env python3
"""Construction du lot 4b : domaine N — Transformees, sections 65 a 178 (lignes 1309 a 3940).

Voir build_lot_I_a.py pour le format. Les entrees "inconnue" portent un candidat
dans le champ `validation`.

Ressource decisive : le tableau du §164 (lignes 3254 a 3265) est INTACT. Il donne,
pour chaque outil, son entree et sa sortie sous la forme « entree -> sortie ». Il
fournit le vocabulaire exact des fiches de reconnaissance (§157 a §162) et de la
formule fondamentale (§178), dont tous les blocs sont vides.
"""

import json
from collections import Counter

SOURCE = "Maths-vers-Informatiques/DOCUMENT N — TRANSFORMÉES.md"
RACINE = "/home/user/_audit/connaissance"
SORTIE = "docs/restauration/propositions/domaine-N-lot4b.patch.json"

T = lambda s: r"\[ \text{" + s + r"} \]"

E = [
 (1309, 1309, r"\[ z(t)=x(t)+i\mathcal{H}\{x(t)\} \]", "haute",
  "§65 transformée de Hilbert « permet de construire le signal analytique : [z(t)=x(t)+i{x(t)}] ». Le \\mathcal{H} a été détruit, ses accolades ont survécu — même signature que \\mathcal{F} et \\mathcal{L}.",
  "Rendu : z(t)=x(t)+i𝓗{x(t)}."),

 (1350, 1350, r"\[ x\to ax \]", "haute",
  "§67 transformée de Mellin « Elle est conceptuellement intéressante lorsque : [x ax] joue un rôle fondamental. » — la flèche a été détruite, laissant deux termes accolés.",
  "Rendu : x → ax (changement d'échelle)."),

 (1389, 1389, r"\[ x=\sum_k c_k\phi_k \]", "haute",
  "§69 « Un vecteur (x) peut être représenté dans une autre base : [x=\\_k c_k_k] ». Le \\sum réduit à \\_, le \\phi détruit (résidu _k).",
  "Rendu : x=Σ c_k φ_k."),

 (1409, 1409, r"\[ x\in\mathbb{R}^{N} \]", "haute",
  "§70 « Pour un vecteur : [x^N] une transformée discrète peut souvent s'écrire : ». Le \\in et le \\mathbb ont été détruits.",
  "Rendu : x ∈ ℝ^N."),

 (1417, 1417, r"\[ T\in\mathbb{R}^{N\times N} \]", "haute",
  "§70 « où : [T^{NN}] est une matrice de transformation. » — \\in, \\mathbb et \\times détruits ; les deux N ont survécu en exposant.",
  "Rendu : T ∈ ℝ^{N×N}."),

 (1427, 1427, r"\[ \{\phi_k\} \]", "haute",
  "§71 base orthonormale « Une famille : [{\\_k}] est orthonormale si : ». Le \\phi a été détruit à l'intérieur des accolades.",
  "Rendu : {φ_k}."),

 (1431, 1431, r"\[ \langle\phi_i,\phi_j\rangle=\delta_{ij} \]", "haute",
  "§71 « est orthonormale si : [\\_i,_j =_ {ij}] ». Le \\langle, le \\rangle, les deux \\phi et le \\delta ont été détruits ; les virgules sont le résidu de la forme.",
  "Rendu : ⟨φ_i,φ_j⟩=δ_ij."),

 (1449, 1449, r"\[ x\to T(x) \]", "haute",
  "§72 parcimonie « Conceptuellement : [x T(x)] avec : ». La flèche a été détruite.",
  "Rendu : x → T(x)."),

 (1453, 1455, "\\[ T(x)=(c_1,\\ldots,c_n)\n\\text{avec la plupart des } c_i\\approx 0 \\]", "moyenne",
  "§72 « avec : [T(x) … ] Cela est extrêmement intéressant pour : - compression ; - débruitage ; … ». Le bloc occupe trois lignes : le contenu décrivait la structure du vecteur transformé.",
  "Le candidat traduit la phrase qui précède (« un grand nombre de coefficients proches de zéro »). Formulation à confirmer."),

 (1469, 1471, "\\[ c_i'=\\begin{cases}c_i&\\text{si }|c_i|>\\lambda\\\\ 0&\\text{sinon}\\end{cases} \\]", "haute",
  "§73 seuil et débruitage « Une stratégie simple consiste à supprimer les petits coefficients : [trois lignes vides] Puis : [x'=T^{-1}(c')] ». Le bloc sur trois lignes et la retransformée qui suit imposent une définition par cas.",
  "Seuillage dur. Le seuil λ n'est pas nommé dans la section : proposé par cohérence."),

 (1485, 1485, r"\[ S_\lambda(x)=x\cdot\mathbf{1}_{|x|>\lambda} \]", "haute",
  "§74 hard thresholding. Résidu S_(x)=x,\\_{|x|} : le \\lambda a été détruit, le \\cdot est devenu une virgule, et le \\mathbf{1} (indicatrice) a disparu en ne laissant que \\_.",
  "Rendu : S_λ(x)=x·1_{|x|>λ}. Définition standard du seuillage dur."),

 (1489, 1489, r"\[ S_\lambda(x)=\mathrm{sign}(x)\max(|x|-\lambda,0) \]", "haute",
  "§74 soft thresholding. Résidu (x)(|x|-,0) : \\mathrm{sign} et \\max détruits, leurs parenthèses conservées. Le \\lambda a disparu.",
  "Rendu : S_λ(x)=sign(x)·max(|x|−λ,0). Définition standard du seuillage doux."),

 (1505, 1505, r"\[ m\ll n \]", "haute",
  "§75 acquisition comprimée « avec : [m n] mais avec des hypothèses adaptées sur (x), (A) et la parcimonie. » — le \\ll a été détruit ; le contexte (peu de mesures, signal parcimonieux) impose l'inégalité large.",
  "Rendu : m ≪ n."),

 (1527, 1527, r"\[ z=f_\theta(x) \]", "haute",
  "§76 « ### Représentation apprise [z=f_(x)] où (f_) est appris. » Le \\theta a été détruit — même destruction que dans le document I.",
  "Rendu : z=f_θ(x)."),

 (1533, 1533, r"\[ z=f_\theta(T(x)) \]", "haute",
  "§76 « ### Représentation hybride [z=f_(T(x))] ». Le \\theta a été détruit.",
  "Rendu : z=f_θ(T(x))."),

 (1694, 1694, None, "inconnue",
  "§85 « On cherche souvent : [vide] tout en conservant une qualité acceptable. »",
  "Candidat : \\[ \\text{réduire le nombre de coefficients} \\] — ou \\[ \\text{compacter la représentation} \\]."),

 (1720, 1720, r"\[ N(x)=\sum_{k=0}^{K}a_kN_k(x) \]", "haute",
  "§87 bruit procédural « comme combinaison de composantes à différentes échelles : [N(x)=\\_{k=0}^{K} a_kN_k(x)] ». Le \\sum a été détruit (résidu \\_).",
  "Rendu : N(x)=Σ_{k=0}^{K} a_k N_k(x)."),

 (1795, 1795, r"\[ H(i\omega) \]", "haute",
  "§91 diagrammes de Bode « À partir de : [H(i)] on peut représenter : ». Le \\omega a été détruit.",
  "Rendu : H(iω)."),

 (1801, 1801, r"\[ 20\log_{10}|H(i\omega)| \]", "haute",
  "§91 « ### Magnitude [20_{10}|H(i)|] ». Le \\log a été détruit, son indice 10 a survécu ; le \\omega aussi a été détruit.",
  "Rendu : 20 log₁₀|H(iω)| — le gain en décibels."),

 (1805, 1805, r"\[ \arg(H(i\omega)) \]", "haute",
  "§91 « ### Phase [H(i)] en fonction de la fréquence logarithmique. » Le \\arg et le \\omega ont été détruits.",
  "Rendu : arg(H(iω))."),

 (1817, 1817, None, "inconnue",
  "§92 détection de motifs « On peut donc rechercher : [vide] comme indicateur de : ».",
  "Candidat : \\[ \\text{une signature fréquentielle} \\]."),

 (1926, 1926, r"\[ e^{-i\omega t_0} \]", "haute",
  "§97 phase et retard « Un retard (x(t−t_0)) produit un facteur fréquentiel : [e^{-it_0}] ». Le \\omega a été détruit.",
  "Rendu : e^{-iωt₀}."),

 (1932, 1932, r"\[ \tau_g(\omega)=-\frac{d\varphi}{d\omega} \]", "haute",
  "§97 « Le retard peut être relié à la pente de phase : [\\_g()=-] ». Le \\tau et le \\omega ont été détruits ; \\frac et les dérivées aussi. La phrase qui précède nomme explicitement la pente de phase.",
  "Rendu : τ_g(ω)=−dφ/dω. Définition du retard de groupe."),

 (1955, 1955, r"\[ x\to X\to x \]", "haute",
  "§99 inversibilité « Une transformée utile doit souvent permettre : [x X x] ». Les deux flèches ont été détruites.",
  "Rendu : x → X → x."),

 (1973, 1973, r"\[ x\to y \]", "haute",
  "§100 problème inverse « Un problème direct : [xy] Un problème inverse : [yx] ». Les flèches ont été détruites ; le sens distingue les deux blocs.",
  "Rendu : x → y (problème direct)."),

 (1977, 1977, r"\[ y\to x \]", "haute",
  "§100 « Un problème inverse : [ ] ». Pendant du précédent.",
  "Rendu : y → x (problème inverse)."),

 (1987, 1987, r"\[ X=H^{-1}Y \]", "haute",
  "§100 « Exemple : [Y=HX] Retrouver (X) implique : [X=] si (H). » — le \\frac ou la puissance −1 a été détruit, ainsi que la condition (H inversible).",
  "Rendu : X=H^{-1}Y."),

 (1993, 1993, r"\[ |H|\approx 0 \]", "haute",
  "§100 « Mais si : [|H|] le bruit peut être énormément amplifié. » — l'inégalité et l'approximation ont été détruites. La phrase donne le sens : H proche de zéro.",
  "Rendu : |H|≈0."),

 (2005, 2005, None, "inconnue",
  "§101 régularisation « Par exemple, au lieu de : [vide] on peut utiliser une forme régularisée. »",
  "Candidat : \\[ \\frac{Y}{H} \\] — la division instable que la régularisation remplace."),

 (2011, 2011, None, "inconnue",
  "§101 « L'idée générale : [vide] Cette idée fait directement le lien avec le domaine L — Analyse numérique. »",
  "Candidat : \\[ \\frac{Y}{H}\\to\\frac{\\bar{H}Y}{|H|^{2}+\\lambda} \\] — forme régularisée de Tikhonov."),

 (2032, 2034, None, "inconnue",
  "§102 « Une FFT théorique parfaite n'existe pas comme opération abstraite dans une machine. Elle est exécutée avec : [trois lignes, dont une puce -] ». Le bloc contenait une liste.",
  "Candidat : \\[ \\text{des nombres flottants} \\] et \\[ \\text{une arithmétique finie} \\] — la puce conservée montre une liste d'au moins deux items."),

 (2046, 2046, r"\[ O(N\log N) \]", "haute",
  "§103 « Une FFT : [O(NN)] rend de nombreux traitements pratiques. » — troisième occurrence du résidu NN dans ce document (l. 547, 606).",
  "Rendu : O(N log N)."),

 (2052, 2052, None, "inconnue",
  "§103 « Cette différence est un excellent exemple de passage : [vide] ».",
  "Candidat : \\[ \\text{de la théorie à l'implémentation} \\]."),

 (2060, 2060, r"\[ \mathcal{F}\{x\ast h\}=\mathcal{F}\{x\}\cdot\mathcal{F}\{h\} \]", "haute",
  "§104 « Grâce à : [(x\\*h)=(x)(h)] on peut calculer : ». Les trois \\mathcal{F} ont été détruits, leurs parenthèses conservées ; le \\cdot aussi.",
  "Rendu : 𝓕{x∗h}=𝓕{x}·𝓕{h}."),

 (2109, 2109, r"\[ T_{\text{calcul}}<T_{\text{disponible}} \]", "haute",
  "§107 temps réel « Un système temps réel impose : [T_{} < T_{}] ». Les deux indices ont été détruits ; la phrase suivante parle de budget temporel.",
  "Rendu : T_calcul < T_disponible."),

 (2173, 2173, None, "inconnue",
  "§110 UX visuelle « Une donnée sonore peut devenir une expérience visuelle : [vide] Exemples : ».",
  "Candidat : \\[ \\text{audio}\\to\\text{visuel} \\]."),

 (2251, 2251, r"\[ T_1,T_2,\ldots,T_k \]", "haute",
  "§113 transformées adaptatives « On peut sélectionner : [T_1,T_2,,T_k] ». Le \\ldots est devenu une virgule.",
  "Rendu : T₁,T₂,…,T_k."),

 (2265, 2265, r"\[ \hat{T}=\arg\max_T \mathrm{score}(T,x) \]", "haute",
  "§113 « Puis sélectionner celle qui maximise un objectif : [T^=\\_T (T,x)] Le score peut mesurer : ». Le chapeau de T̂, le \\arg\\max et le \\mathrm{score} ont été détruits.",
  "Rendu : T̂=argmax_T score(T,x)."),

 (2280, 2280, r"\[ T_\theta \]", "haute",
  "§114 transformées apprenables « On peut aller plus loin et chercher une transformation : [T_] dont les paramètres sont appris. » Le \\theta a été détruit.",
  "Rendu : T_θ."),

 (2286, 2286, r"\[ \hat{\theta}=\arg\min_\theta L(T_\theta(x),y) \]", "haute",
  "§114 « On cherche alors : [^=_L(T_(x),y)] Cela crée un pont entre : ». Le chapeau, le \\arg\\min et les deux \\theta ont été détruits.",
  "Rendu : θ̂=argmin_θ L(T_θ(x),y)."),

 (2301, 2301, r"\[ \nabla_\theta L \]", "moyenne",
  "§115 transformées différentiables « Dans un modèle neuronal, une transformée peut être intégrée comme une opération différentiable. On peut alors calculer : [vide] à travers la transformation. » — le bloc est vide, mais la phrase ne laisse guère d'alternative.",
  "Candidat alternatif : \\[ \\frac{\\partial L}{\\partial\\theta} \\]."),

 (2307, 2309, None, "inconnue",
  "§115 « Cela permet de construire des architectures combinant : [trois lignes, dont une puce -] ». Le bloc contenait une liste d'au moins deux items.",
  "Candidat : \\[ \\text{réseaux neuronaux} \\] et \\[ \\text{transformées} \\]."),

 # §117 — les six questions de la matrice de décision. Les réponses sont données
 # par le tableau intact du §164 et par les fiches de reconnaissance.
 (2383, 2383, T("Fourier"), "moyenne",
  "§117 Question 3 « Cherche-t-on des fréquences ? Alors : [vide] ». Le tableau du §164 donne : Fourier — entrée « fonction », sortie « spectre », question « quelle structure fréquentielle ? ».",
  "Candidat fondé sur le tableau du §164. Alternative : \\text{DFT} si le signal est échantillonné."),
 (2391, 2391, T("Laplace"), "moyenne",
  "§117 Question 4 « Cherche-t-on une dynamique ou une EDO ? Alors : [vide] ». Le §32 dit : « Une équation différentielle devient une équation algébrique. »",
  "Candidat fondé sur le §32 et le tableau du §164."),
 (2399, 2399, T("transformée en Z"), "moyenne",
  "§117 Question 5 « Travaille-t-on avec un système discret ? Alors : [vide] ».",
  "Candidat fondé sur les fiches §159 et le tableau du §164."),
 (2407, 2407, T("STFT"), "moyenne",
  "§117 Question 6 « Cherche-t-on une localisation temporelle et fréquentielle ? Alors : [vide] ».",
  "Candidat fondé sur la fiche §160 et le tableau du §164."),
 (2415, 2415, T("ondelettes"), "moyenne",
  "§117 Question 7 « Cherche-t-on une représentation multi-échelle ? Alors : [vide] ».",
  "Candidat fondé sur la fiche §161 et le tableau du §164 (DWT : échelles/détails)."),
 (2423, 2423, T("DCT"), "moyenne",
  "§117 Question 8 « Cherche-t-on une compression efficace d'image ? Alors : [vide] ».",
  "Candidat fondé sur la fiche §162 et le tableau du §164 (DCT : concentration d'énergie)."),

 (2537, 2537, r"\[ x[n]=\sin(2\pi fn/f_s) \]", "haute",
  "§123 tests « ### Sinusoïde pure [x[n]=(2f n/f_s)] On doit observer un pic correspondant à (f). » — le \\sin et le \\pi ont été détruits.",
  "Rendu : x[n]=sin(2πfn/f_s)."),

 (2557, 2557, r"\[ x\to T(x)\to T^{-1}(T(x)) \]", "haute",
  "§124 test de l'inverse « Pour une transformée réversible : [x T(x) T^{-1}(T(x))] on doit vérifier : ». Les flèches ont été détruites.",
  "Rendu : x → T(x) → T^{-1}(T(x))."),

 (2561, 2561, r"\[ \|x-T^{-1}(T(x))\| \]", "haute",
  "§124 « on doit vérifier : [|x-T^{-1}(T(x))|] Cette erreur doit rester compatible avec : ». Le \\| a été détruit.",
  "Rendu : ‖x−T^{-1}(T(x))‖."),

 (2589, 2589, r"\[ X[N-k]=\overline{X[k]} \]", "haute",
  "§126 « Pour Fourier, le théorème de Parseval fournit … avec une normalisation dépendante de la convention : [X[N-k]=] dans la convention classique. » — il s'agit de la symétrie hermitienne d'un signal réel.",
  "Rendu : X[N−k]=conj(X[k]). Propriété de symétrie pour signal réel."),

 (2601, 2601, None, "inconnue",
  "§127 mémoire « Il faut distinguer : [vide] et : [vide] Une représentation complexe peut nécessiter davantage de mémoire qu'une représentation réelle. »",
  "Candidats : \\[ \\text{la mémoire de la représentation d'origine} \\] puis \\[ \\text{la mémoire de la transformée} \\]."),

 (2605, 2605, None, "inconnue",
  "§127, pendant du bloc précédent.",
  "Voir l. 2601."),

 (2639, 2639, r"\[ c\to Q(c) \]", "haute",
  "§129 quantification « Dans une compression avec perte : [c Q(c)] où (Q) est une quantification. » — la flèche a été détruite.",
  "Rendu : c → Q(c)."),

 (2647, 2647, None, "inconnue",
  "§129 « Le compromis devient : [vide] ».",
  "Candidat : \\[ \\text{qualité contre taille} \\] — ou \\[ \\text{débit contre fidélité} \\]."),

 (2653, 2653, r"\[ x\to T(x)\to Q\to C \]", "haute",
  "§130 « Pipeline générique : [x T(x) Q C] où : ». Les flèches ont été détruites ; la légende qui suit nomme Q (quantification) et C (codage).",
  "Rendu : x → T(x) → Q → C."),

 (2663, 2663, r"\[ \hat{x}=T^{-1}(Q^{-1}(C)) \]", "haute",
  "§130 « La reconstruction : [C Q^{-1} T^{-1}] avec : ». Les flèches et le chapeau de x̂ ont été détruits.",
  "Rendu : x̂=T^{-1}(Q^{-1}(C))."),

 (2667, 2667, r"\[ \hat{x} \]", "haute",
  "§130 « avec : [x] dans le cas avec perte. » Le chapeau a été détruit.",
  "Rendu : x̂."),

 (2675, 2675, r"\[ \hat{x}=x \]", "haute",
  "§131 compression sans perte « la reconstruction doit être exacte : [=x] ». Le chapeau a été détruit.",
  "Rendu : x̂=x."),

 (2699, 2699, None, "inconnue",
  "§133 lien avec la théorie de l'information « On peut donc avoir : [vide] ».",
  "Candidat : \\[ \\text{entropie} \\] ou \\[ \\text{compacité de la représentation} \\]."),

 (2747, 2747, r"\[ \varphi_X(t)=\mathbb{E}\left[e^{itX}\right] \]", "haute",
  "§135 lien avec les probabilités « Une variable aléatoire possède une fonction caractéristique : [\\_X(t)=\\[e^{itX}\\]] ». Le \\varphi, le \\mathbb{E}, le \\left et le \\right ont été détruits — les crochets échappés sont le résidu de \\left[.",
  "Rendu : φ_X(t)=𝔼[e^{itX}]."),

 (2774, 2774, r"\[ x:V\to\mathbb{R} \]", "haute",
  "§137 graphes « Une idée plus avancée consiste à définir des signaux sur les sommets : [x:V] ». Le \\to et le \\mathbb{R} ont été détruits.",
  "Rendu : x : V → ℝ."),

 (2780, 2780, None, "inconnue",
  "§137 « On peut alors construire des analogues de Fourier sur les graphes à partir des vecteurs propres du Laplacien du graphe. Cela mène à la : [vide] avec des applications en : ».",
  "Candidat : \\[ \\text{transformée de Fourier sur graphes (GFT)} \\]."),

 (2814, 2814, r"\[ x\to T(x)\to z\to T^{-1}(z) \]", "haute",
  "§139 IA générative « Exemple conceptuel : [x T(x) z T^{-1}()] ». Les flèches ont été détruites ; le dernier terme a perdu son argument z.",
  "Rendu : x → T(x) → z → T^{-1}(z)."),

 (2824, 2824, None, "inconnue",
  "§140 modèles de diffusion « Même l'… [vide] reste profondément similaire. » — la phrase elle-même est tronquée dans le document.",
  "Candidat : \\[ \\text{idée de transformer pour simplifier} \\]. Le bloc reste très incertain : la phrase qui l'introduit est elle-même amputée."),

 (2851, 2851, r"\[ x\to T(x)\to T^{-1}\to x' \]", "haute",
  "§142 stéganographie « Conceptuellement : [x T(x) T^{-1} x'] ». Les flèches ont été détruites.",
  "Rendu : x → T(x) → T^{-1} → x'."),

 (2872, 2872, r"\[ x_0,x_1,\ldots,x_N \]", "haute",
  "§144 données temporelles « Une série temporelle : [x_0,x_1,,x_N] ». Le \\ldots est devenu une virgule.",
  "Rendu : x₀,x₁,…,x_N."),

 (2914, 2914, None, "inconnue",
  "§146 détection d'anomalies « Exemple : [vide] puis : [vide] On peut alors construire : [s(x)=d(T(x),μ)] ».",
  "Candidats : \\[ \\text{un spectre de référence} \\] puis \\[ \\text{un pic spectral inattendu} \\]."),

 (2918, 2918, None, "inconnue",
  "§146, pendant du bloc précédent.",
  "Voir l. 2914."),

 (2922, 2922, r"\[ s(x)=d(T(x),\mu) \]", "haute",
  "§146 « On peut alors construire : [(x)=d(T(x),)] où () représente le comportement normal. » — le s, le \\mu ont été détruits.",
  "Rendu : s(x)=d(T(x),μ)."),

 (3068, 3068, r"\[ T^{-1}(T(x))\approx x \]", "haute",
  "§153 exactitude « ### Exactitude [T^{-1}(T(x))x] ». Le \\approx a été détruit ; l'égalité stricte serait fausse en arithmétique flottante.",
  "Rendu : T^{-1}(T(x))≈x."),

 # §156 a §162 — fiches de reconnaissance. Le tableau du §164 donne la réponse
 # attendue pour chacune, sous la forme « entrée -> sortie ».
 (3140, 3140, T("transformée de Fourier"), "moyenne",
  "§156 FICHE DE RECONNAISSANCE — FOURIER « Si le problème contient : fréquence, spectre, oscillation, harmonique, périodicité, convolution, signal — penser : [vide] ». Le titre de la section et le tableau du §164 (Fourier : fonction → spectre) désignent la réponse.",
  "Candidat fondé sur le titre de la fiche et le tableau du §164."),
 (3154, 3154, T("FFT"), "moyenne",
  "§157 FICHE — FFT (DFT, grand volume, performance, temps réel, convolution rapide).",
  "Candidat fondé sur le titre de la fiche."),
 (3169, 3169, T("Laplace"), "moyenne",
  "§158 FICHE — LAPLACE (EDO, conditions initiales, système continu, fonction de transfert, pôles, stabilité).",
  "Candidat fondé sur le titre de la fiche."),
 (3183, 3183, T("transformée en Z"), "moyenne",
  "§159 FICHE — Z (séquence, système discret, équation aux différences, filtre numérique, cercle unité).",
  "Candidat fondé sur le titre de la fiche."),
 (3197, 3197, T("STFT"), "moyenne",
  "§160 FICHE — STFT (fréquence qui change dans le temps, événement sonore, parole, spectrogramme, signal non stationnaire).",
  "Candidat fondé sur le titre de la fiche."),
 (3212, 3212, T("ondelettes"), "moyenne",
  "§161 FICHE — ONDELETTES (transitoires, événements localisés, multirésolution, structures à différentes échelles, compression multi-échelle).",
  "Candidat fondé sur le titre de la fiche."),
 (3225, 3225, T("DCT"), "moyenne",
  "§162 FICHE — DCT (compression, image, coefficients cosinus, concentration d'énergie).",
  "Candidat fondé sur le titre de la fiche."),

 (3231, 3231, T("la DFT et la FFT"), "moyenne",
  "§163 « Ne jamais confondre : [vide] La relation est : » suivi d'un arbre ASCII intact (Fourier → continu/discret → DFT → FFT « algorithme rapide »). L'arbre dit exactement ce qu'il ne faut pas confondre : la DFT est une transformée, la FFT un algorithme.",
  "Candidat fondé sur l'arbre ASCII qui suit le bloc, lequel est intact."),

 (3248, 3248, T("la transformée de Fourier et la DFT"), "moyenne",
  "§163 « De même : [vide] mais elles jouent des rôles conceptuellement analogues dans les domaines continu et discret. » — la phrase désigne l'analogie continu/discret.",
  "Candidat fondé sur la phrase elle-même et l'arbre du §163."),

 (3426, 3426, None, "inconnue",
  "PROJET 2 — Spectrogramme « Construire : [vide] et permettre de modifier : - taille de fenêtre ; - hop size ; - fréquence d'échantillonnage. »",
  "Candidat : \\[ \\text{un spectrogramme interactif} \\]."),

 (3438, 3438, r"\[ X(f)\to H(f)\to Y(f) \]", "haute",
  "PROJET 3 — Égaliseur audio « Créer un système : [X(f) H(f) Y(f)] avec : ». Les flèches ont été détruites.",
  "Rendu : X(f) → H(f) → Y(f)."),

 (3470, 3470, r"\[ x\to \text{DWT}\to \text{seuil}\to \text{IDWT} \]", "haute",
  "PROJET 5 — Débruitage par ondelettes « Créer : [x DWT Threshold IDWT] et mesurer : ». Les flèches ont été détruites.",
  "Rendu : x → DWT → seuil → IDWT."),

 (3530, 3530, r"\[ O(N\log N) \]", "haute",
  "CHALLENGE 2 « Comparer : [O(N^2)] contre : [O(NN)] ».",
  "Rendu : O(N log N)."),

 (3600, 3600, r"\[ \hat{T} \]", "haute",
  "§169 « Le système recommande ensuite : [T^] selon le problème. » Le chapeau a été détruit.",
  "Rendu : T̂."),

 (3610, 3610, None, "inconnue",
  "§170 expérience créative audio → monde visuel « Construire : [vide] Le système pourrait contrôler : ».",
  "Candidat : \\[ \\text{audio}\\to\\text{paramètres visuels} \\]."),

 (3720, 3720, None, "inconnue",
  "§173 « ### Niveau 7 — Création / Construire de nouvelles applications à partir du principe : [vide] ».",
  "Candidat : \\[ \\text{changer de représentation} \\]."),

 (3794, 3794, None, "inconnue",
  "§176 SYNTHÈSE DES GRANDES TRANSFORMÉES : un bloc unique et vide, sans phrase d'introduction. Le tableau du §164 en donne la matière.",
  "Candidat : \\[ \\text{Fourier, Laplace, Z, STFT, ondelettes, DCT} \\] — ou la chaîne du §178."),

 # §178 — formule fondamentale. Le tableau du §164 fournit le couple
 # entrée/sortie de chaque outil, dans le vocabulaire exact du document.
 (3858, 3858, T("changer de représentation pour simplifier le problème"), "moyenne",
  "§178 « La contribution la plus importante de ce domaine peut être résumée ainsi : [vide] ». La question posée au §176 — « Quelle représentation rend le problème plus simple ? » — est la réponse.",
  "Candidat fondé sur le §176, dont la phrase-clé est intacte."),
 (3862, 3862, T("une fonction en spectre"), "moyenne",
  "§178 « Fourier transforme : [vide] ». Le tableau du §164 donne : Fourier — entrée « fonction », sortie « spectre ».",
  "Candidat fondé mot pour mot sur le tableau intact du §164."),
 (3866, 3866, T("une fonction temporelle en F(s)"), "moyenne",
  "§178 « Laplace transforme : [vide] ». Tableau du §164 : Laplace — « fonction temporelle » → « F(s) ».",
  "Candidat fondé mot pour mot sur le tableau du §164."),
 (3870, 3870, T("une séquence en X(z)"), "moyenne",
  "§178 « Z transforme : [vide] ». Tableau du §164 : Z — « séquence » → « X(z) ».",
  "Candidat fondé mot pour mot sur le tableau du §164."),
 (3874, 3874, T("un signal en représentation temps-fréquence"), "moyenne",
  "§178 « STFT transforme : [vide] ». Tableau du §164 : STFT — « signal » → « temps-fréquence ».",
  "Candidat fondé mot pour mot sur le tableau du §164."),
 (3878, 3878, T("un signal en échelles et détails"), "moyenne",
  "§178 « Les ondelettes transforment : [vide] ». Tableau du §164 : DWT — « signal » → « échelles/détails ».",
  "Candidat fondé mot pour mot sur le tableau du §164."),
 (3882, 3882, T("des données en coefficients cosinus"), "moyenne",
  "§178 « La DCT transforme : [vide] ». Tableau du §164 : DCT — « données » → « coefficients cosinus ».",
  "Candidat fondé mot pour mot sur le tableau du §164."),

 # §179 — les six blocs de la chaîne finale. La FORMULE MENTALE du domaine N
 # (lignes 3941 a 3945) est INTACTE et donne les six termes dans l'ordre.
 (3898, 3898, T("transformer"), "moyenne",
  "§179 « C'est ce qui permet de passer : [vide] [vide] … » — six blocs vides consécutifs. La FORMULE MENTALE DU DOMAINE N, qui clôt le document (l. 3941-3945), est intacte et énonce six verbes : transformer, voir, comprendre, simplifier, calculer, construire.",
  "Candidat fondé sur la FORMULE MENTALE intacte du document, qui fournit les six termes dans l'ordre."),
 (3900, 3900, T("voir"), "moyenne", "§179, deuxième terme de la chaîne.", "Voir l. 3898."),
 (3902, 3902, T("comprendre"), "moyenne", "§179, troisième terme.", "Voir l. 3898."),
 (3904, 3904, T("simplifier"), "moyenne", "§179, quatrième terme.", "Voir l. 3898."),
 (3906, 3906, T("calculer"), "moyenne", "§179, cinquième terme.", "Voir l. 3898."),
 (3908, 3908, T("construire"), "moyenne", "§179, sixième terme.", "Voir l. 3898."),

 (3935, 3935, T("chercher la représentation qui simplifie"), "moyenne",
  "§179 « Le réflexe d'ingénieur à développer est donc : [vide] mais : [vide] ». La question centrale du document, énoncée deux paragraphes plus haut, est : « Quelle représentation rend le problème plus simple ? »",
  "Candidat fondé sur la phrase intacte du §176."),
 (3939, 3939, T("vérifier les hypothèses et les limites"), "moyenne",
  "§179, second bloc (« mais : »). Le « mais » oppose une précaution au réflexe précédent.",
  "Candidat. Alternative : \\[ \\text{ne pas oublier le coût de calcul} \\]."),
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
