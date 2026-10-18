#!/usr/bin/env python3
"""Construction du lot 4a : domaine N — Transformees, sections 1 a 64 (lignes 1 a 1301).

Voir build_lot_I_a.py pour le format. Les entrees "inconnue" portent un candidat
dans le champ `validation`.
"""

import json
from collections import Counter

SOURCE = "Maths-vers-Informatiques/DOCUMENT N — TRANSFORMÉES.md"
RACINE = "/home/user/_audit/connaissance"
SORTIE = "docs/restauration/propositions/domaine-N-lot4a.patch.json"

E = [
 (75, 75, r"\[ f \to F \]", "haute",
  "« Une transformée associe à un objet mathématique (f) une autre représentation (F) : [ ] ». Les deux lettres sont intactes, la flèche a été détruite — même destruction que dans le document I (l. 3121 à 3137).",
  "Rendu : f → F."),

 (142, 142, None, "inconnue",
  "§3 « La convolution devient une multiplication. On peut donc avoir : [vide] C'est précisément cette propriété qui explique l'importance des transformées en informatique. » — le bloc désigne le bénéfice retiré, qui n'est pas nommé ailleurs dans la section.",
  "Candidat : \\[ O(N^2)\\to O(N\\log N) \\] — le gain de complexité, effet concret de la propriété. Alternative : \\[ (f\\ast g)\\to F\\cdot G \\]."),

 (190, 193, "\\[ f(t)=\\frac{a_0}{2}\n\n+ \\sum_{n=1}^{\\infty}\\left[a_n\\cos(n\\omega_0t)+b_n\\sin(n\\omega_0t)\\right] \\]", "haute",
  "§5.1 série de Fourier. Le résidu conserve le \\sum_{n=1}^{} et les deux lignes a_n(...) / b_n(...) : les fonctions \\cos et \\sin ont été détruites, ainsi que la borne supérieure \\infty et l'exposant \\omega. La ligne vide entre f(t)= et la somme correspond au terme constant a_0/2. Les crochets \\[...\\] sont le résidu d'un \\left[. Artefact : les + de tête de ligne sont devenus des puces -.",
  "Forme canonique de la série de Fourier trigonométrique. Le terme a_0/2 est restitué d'après la ligne vide et l'usage ; à confirmer."),

 (197, 197, r"\[ \omega_0=\frac{2\pi}{T} \]", "haute",
  "§5.1 « avec : [ \\_0= ] ». Le \\omega a été détruit ; \\frac détruit. La pulsation fondamentale ne peut être que 2π/T pour une fonction de période T.",
  "Rendu : ω₀=2π/T."),

 (203, 203, r"\[ a_n=\frac{2}{T}\int_0^T f(t)\cos(n\omega_0t)\,dt \]", "haute",
  "§6 coefficients de Fourier. Résidu \\_0^T : \\frac{2}{T} réduit à 2T (régime « contenu conservé ») devant \\int_0^T réduit à \\_0^T. Le \\cos a été détruit, le \\, est devenu une virgule.",
  "Rendu : a_n=(2/T)∫₀ᵗ f(t)cos(nω₀t)dt."),

 (207, 207, r"\[ b_n=\frac{2}{T}\int_0^T f(t)\sin(n\omega_0t)\,dt \]", "haute",
  "§6 « et : [ ] ». Même reconstruction, avec \\sin. Le bloc est identique au précédent en apparence, ce qui est la marque même de la destruction des fonctions.",
  "Rendu : b_n=(2/T)∫₀ᵗ f(t)sin(nω₀t)dt."),

 (215, 215, r"\[ f(t)=\sum_{n=-\infty}^{+\infty}c_ne^{in\omega_0t} \]", "haute",
  "§7 formulation complexe. Le \\_ est le résidu de \\sum ; les bornes -\\infty et +\\infty ont laissé - et + ; le \\omega a été détruit.",
  "Rendu : f(t)=Σ_{n=-∞}^{+∞} c_n e^{inω₀t}."),

 (219, 219, r"\[ c_n=\frac{1}{T}\int_0^T f(t)e^{-in\omega_0t}\,dt \]", "haute",
  "§7 « avec : [ ] ». Même structure qu'en l. 203, mais le facteur est 1/T et non 2/T : c'est la convention de la forme complexe.",
  "Vérifier : la forme complexe utilise 1/T, la forme trigonométrique 2/T."),

 (231, 231, None, "inconnue",
  "§8 « La série de Fourier dit essentiellement : … Cela permet de passer : [vide] Cette idée est fondamentale pour : ».",
  "Candidat : \\[ \\text{d'une description temporelle à une description fréquentielle} \\]."),

 (247, 247, r"\[ F(\omega)=\int_{-\infty}^{+\infty}f(t)e^{-i\omega t}\,dt \]", "haute",
  "§9 transformée de Fourier. Le \\omega a été détruit dans F(·) et dans l'exponentielle ; le \\_ est le résidu de \\int ; le \\, est devenu une virgule.",
  "Rendu : F(ω)=∫_{-∞}^{+∞} f(t)e^{-iωt}dt. La phrase suivante rappelle que les conventions varient."),

 (251, 251, r"\[ f(t)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}F(\omega)e^{i\omega t}\,d\omega \]", "haute",
  "§9 « et l'inverse : [ ] ». Le facteur 1/2π a été détruit avec \\frac ; le d\\omega final ne subsiste que par la lettre d.",
  "Rendu : f(t)=(1/2π)∫F(ω)e^{iωt}dω. Cohérent avec la convention retenue en l. 247."),

 (267, 267, r"\[ F(\omega) \]", "haute",
  "§10 « On passe approximativement de : [f(t)] à : [ ] où : ». Le \\omega a été détruit.",
  "Rendu : F(ω)."),

 (280, 280, r"\[ F(\omega)=a(\omega)+ib(\omega) \]", "moyenne",
  "§11 « Pour : [F()=a()+ib()] la magnitude est : ». Les trois \\omega ont été détruits. Le choix de a et b comme parties réelle et imaginaire est conservé du résidu.",
  "Candidat alternatif : F(\\omega)=\\Re(F)+i\\Im(F). La notation a/b est celle du résidu."),

 (284, 284, r"\[ |F(\omega)|=\sqrt{a(\omega)^{2}+b(\omega)^{2}} \]", "haute",
  "§11 « la magnitude est : [ |F()|= ] ». \\sqrt et les exposants détruits.",
  "Rendu : |F(ω)|=√(a²+b²)."),

 (288, 288, r"\[ \varphi(\omega)=\arg(F(\omega)) \]", "haute",
  "§11 « et la phase : [ ()=(F()) ] ». Le \\varphi et le \\arg ont été détruits.",
  "Rendu : φ(ω)=arg(F(ω))."),

 (304, 304, r"\[ \mathcal{F}\{af+bg\}=aF+bG \]", "haute",
  "§12 linéarité. Le \\mathcal{F} a été détruit, ses accolades ont survécu — signature constante dans tout le document (l. 322, 326, 744, 748, 752, 756, 1301).",
  "Rendu : 𝓕{af+bg}=aF+bG."),

 (314, 314, r"\[ G(\omega)=e^{-i\omega t_0}F(\omega) \]", "haute",
  "§12 translation temporelle « alors : [ ] ». Deux \\omega détruits.",
  "Rendu : G(ω)=e^{-iωt₀}F(ω)."),

 (322, 322, r"\[ \mathcal{F}\{f\ast g\}=F\cdot G \]", "haute",
  "§12 convolution. \\mathcal{F} et \\cdot détruits.",
  "Rendu : 𝓕{f∗g}=F·G."),

 (326, 326, r"\[ \mathcal{F}\{fg\}=F\ast G \]", "haute",
  "§12 multiplication « [ {fg} ] est reliée à une convolution des transformées. » — \\mathcal{F}, le membre de droite et le \\ast ont été détruits. La phrase qui suit dit exactement ce qu'il contient.",
  "Rendu : 𝓕{fg}=F∗G. Dualité de la ligne précédente."),

 (336, 336, r"\[ (f\ast g)(t)=\int_{-\infty}^{+\infty}f(\tau)g(t-\tau)\,d\tau \]", "haute",
  "§13 convolution continue. Le \\tau a été détruit aux deux endroits ; le \\_ est le résidu de \\int ; le \\, est devenu une virgule.",
  "Rendu : (f∗g)(t)=∫f(τ)g(t−τ)dτ."),

 (373, 373, r"\[ Y(\omega)=X(\omega)H(\omega) \]", "haute",
  "§15 « Dans le domaine fréquentiel : [ ] ». Trois \\omega détruits.",
  "Rendu : Y(ω)=X(ω)H(ω)."),

 (377, 377, r"\[ H(\omega)=\frac{Y(\omega)}{X(\omega)} \]", "haute",
  "§15 « avec : [ H()= ] lorsque le rapport est défini. » — la phrase nomme le rapport, ce qui impose la fraction.",
  "Rendu : H(ω)=Y(ω)/X(ω)."),

 (405, 405, r"\[ Y(\omega)=X(\omega)H(\omega) \]", "haute",
  "§15 filtre coupe-bande « Conceptuellement : [ ] ». Trois \\omega détruits.",
  "Rendu : Y(ω)=X(ω)H(ω)."),

 (425, 425, r"\[ f_N=\frac{f_s}{2} \]", "haute",
  "§16 « Si la fréquence d'échantillonnage est (f_s), la fréquence de Nyquist est : [ ] ».",
  "Rendu : f_N=f_s/2."),

 (429, 429, r"\[ f_s>2f_{\max} \]", "haute",
  "§16 « Pour reconstruire correctement un signal limité en bande, il faut idéalement : [ ] C'est le principe de Nyquist-Shannon. » — le \\max a été détruit.",
  "Rendu : f_s>2f_max."),

 (439, 439, None, "inconnue",
  "§17 « Ce phénomène est appelé : [vide] Il est particulièrement important en : ». Le titre de la section donne le terme, mais la forme exacte du bloc reste inconnue.",
  "Candidat : \\[ \\text{aliasing} \\] (ou \\text{repliement de spectre})."),

 (461, 461, r"\[ X[k]=\sum_{n=0}^{N-1}x[n]e^{-i2\pi kn/N} \]", "haute",
  "§18 DFT. Le \\pi et le \\sum ont été détruits (le \\sum laisse \\_).",
  "Rendu : X[k]=Σ_{n=0}^{N-1} x[n]e^{-i2πkn/N}."),

 (465, 465, r"\[ k=0,\ldots,N-1 \]", "haute",
  "§18 « pour : [k=0,,N-1] ». Le \\ldots est devenu une virgule — conversion systématique dans ce document (l. 2251, 2872).",
  "Rendu : k=0,…,N−1."),

 (469, 469, r"\[ x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{i2\pi kn/N} \]", "haute",
  "§18 « L'inverse est : [ ] ». Le facteur 1/N et le \\pi ont été détruits.",
  "Rendu : x[n]=(1/N)Σ X[k]e^{i2πkn/N}."),

 (475, 475, r"\[ x[n] \]", "moyenne",
  "§19 « La DFT transforme un vecteur temporel fini : [vide] en un vecteur de coefficients fréquentiels : [vide] ». Les deux blocs sont vides ; le premier ne peut désigner que la séquence d'entrée.",
  "Candidat alternatif : \\mathbf{x}. La notation à confirmer."),

 (479, 479, r"\[ X[k] \]", "moyenne",
  "§19, second bloc. Pendant du précédent.",
  "Candidat alternatif : \\mathbf{X}."),

 (497, 497, r"\[ f_k=\frac{kf_s}{N} \]", "haute",
  "§20 « Pour une DFT de (N) points avec fréquence d'échantillonnage (f_s) : [ ] ».",
  "Rendu : f_k=k·f_s/N."),

 (501, 501, r"\[ \Delta f=\frac{f_s}{N} \]", "haute",
  "§20 « La résolution fréquentielle est : [ ] ». Le \\Delta a été détruit.",
  "Rendu : Δf=f_s/N."),

 (547, 547, r"\[ O(N\log N) \]", "haute",
  "§22 « Une FFT classique de type Cooley-Tukey permet typiquement : [O(NN)] ». Le \\log a été détruit ; le résidu NN est la marque de O(N log N), présente trois fois dans ce document (l. 606, 2046, 3530).",
  "Rendu : O(N log N)."),

 (562, 564, "\\[ X[k]=\\sum_{m=0}^{N/2-1}x[2m]e^{-i2\\pi k(2m)/N}\n\n+ \\sum_{m=0}^{N/2-1}x[2m+1]e^{-i2\\pi k(2m+1)/N} \\]", "haute",
  "§23 décomposition paire/impaire. Les deux \\pi ont été détruits ; le + de tête de ligne est devenu une puce -, artefact constant. Le bloc décompose la somme en indices pairs puis impairs, conformément au texte qui précède.",
  "Première étape de Cooley-Tukey : séparation des termes pairs et impairs."),

 (574, 574, r"\[ W_N=e^{-i2\pi/N} \]", "haute",
  "§24 twiddle factors « On utilise : [ ] ». Le \\pi a été détruit.",
  "Rendu : W_N=e^{-i2π/N}."),

 (596, 596, r"\[ \log_2 N \]", "haute",
  "§25 radix-2 « et construit : [ \\_2N ] niveaux de décomposition. » Le \\_ est ici le résidu de \\log, et le 2 est son indice.",
  "Rendu : log₂ N."),

 (606, 606, r"\[ O(N\log_2 N) \]", "haute",
  "§25 « ce qui produit : [O(N_2N)] ». Le \\log_2 a été détruit, laissant ses deux arguments.",
  "Rendu : O(N log₂ N)."),

 (666, 666, r"\[ C_k=\alpha_k\sum_{n=0}^{N-1}x_n\cos\left(\frac{\pi}{N}\left(n+\frac{1}{2}\right)k\right) \]", "haute",
  "§29 DCT « Une forme classique : [C_k=_k_ {n=0}^{N-1} x_n] ». Le résidu montre le facteur d'échelle \\alpha_k (deux lettres grecques détruites encadrant le k), le \\sum_{n=0}^{N-1}, et un \\cos détruit avec son argument.",
  "Forme DCT-II. L'argument du cosinus est restitué d'après la forme standard ; à confirmer."),

 (676, 676, None, "inconnue",
  "§30 « Principe général : [vide] L'idée est de représenter efficacement les informations importantes. »",
  "Candidat : \\[ x\\to T(x)\\to Q\\to C \\] — la chaîne complète est donnée au §130 (transformée, quantification, codage)."),

 (712, 712, r"\[ F(s)=\int_0^{\infty}f(t)e^{-st}\,dt \]", "haute",
  "§31 Laplace. Le \\_ est le résidu de \\int ; la borne \\infty a été détruite ; le \\, est devenu une virgule.",
  "Rendu : F(s)=∫₀^∞ f(t)e^{-st}dt."),

 (716, 716, r"\[ s=\sigma+i\omega \]", "haute",
  "§31 « où : [s=+i] ». Le \\sigma et le \\omega ont été détruits, le + et le i sont restés.",
  "Rendu : s=σ+iω."),

 (726, 726, r"\[ \mathcal{L}\{y'\}=sY(s)-y(0) \]", "haute",
  "§32 « Une dérivée devient, sous Laplace : [ ] ». Le \\mathcal{L} a été détruit, ses accolades ont survécu.",
  "Rendu : 𝓛{y'}=sY(s)−y(0)."),

 (732, 732, None, "inconnue",
  "§32 « On passe de : [vide] à : [vide] puis on effectue la transformée inverse. »",
  "Candidats : \\[ \\text{une équation différentielle} \\] puis \\[ \\text{une équation algébrique} \\] — c'est l'objet même de la section."),

 (736, 736, None, "inconnue",
  "§32, pendant du bloc précédent.",
  "Voir l. 732."),

 (744, 744, r"\[ \mathcal{L}\{af+bg\}=aF+bG \]", "haute",
  "§33 linéarité de Laplace. Même signature que la ligne 304 : \\mathcal{L} détruit, accolades conservées.",
  "Rendu : 𝓛{af+bg}=aF+bG."),

 (748, 748, r"\[ \mathcal{L}\{f'\}=sF(s)-f(0) \]", "haute",
  "§33 dérivée.",
  "Rendu : 𝓛{f'}=sF(s)−f(0)."),

 (752, 752, r"\[ \mathcal{L}\{f''\}=s^{2}F(s)-sf(0)-f'(0) \]", "haute",
  "§33 seconde dérivée. Les exposants ont survécu.",
  "Rendu : 𝓛{f''}=s²F(s)−sf(0)−f'(0)."),

 (756, 756, r"\[ \mathcal{L}\{f\ast g\}=F(s)G(s) \]", "haute",
  "§33 convolution. Seul \\mathcal{L} manque.",
  "Rendu : 𝓛{f∗g}=F(s)G(s)."),

 (768, 768, None, "inconnue",
  "§34 « Il faut également déterminer les valeurs de (s) pour lesquelles l'intégrale converge. On parle de : [vide] ».",
  "Candidat : \\[ \\text{région de convergence} \\] (ou \\text{domaine de convergence}, ou ROC)."),

 (776, 776, r"\[ H(s)=\frac{N(s)}{D(s)} \]", "haute",
  "§35 pôles et zéros « Une fonction de transfert peut s'écrire : [H(s)=] Les racines de : [N(s)=0] sont les zéros … [D(s)=0] sont les pôles. » — les deux blocs suivants nomment N(s) et D(s), ce qui impose la fraction.",
  "Rendu : H(s)=N(s)/D(s)."),

 (805, 805, r"\[ n\geq 0 \]", "haute",
  "§36 transformée en Z « Une version unilatérale utilise généralement : [n] ». Le \\geq a été détruit.",
  "Rendu : n ≥ 0."),

 (845, 845, r"\[ z=e^{i\omega} \]", "haute",
  "§39 lien entre Z et Fourier « Sur le cercle unité : [ ] ». Le \\omega a été détruit.",
  "Rendu : z=e^{iω}."),

 (895, 895, r"\[ X(\tau,\omega)=\int x(t)w(t-\tau)e^{-i\omega t}\,dt \]", "haute",
  "§42 STFT « On applique une fenêtre (w) localement : [X(,)=x(t)w(t-)e^{-it},dt] ». Le \\tau et le \\omega ont été détruits, ainsi que le \\int ; le \\, est devenu une virgule.",
  "Rendu : X(τ,ω)=∫x(t)w(t−τ)e^{-iωt}dt."),

 (901, 901, r"\[ |X(\tau,\omega)|^{2} \]", "haute",
  "§43 spectrogramme « Le spectrogramme représente généralement : [ ] ». Deux lettres grecques détruites.",
  "Rendu : |X(τ,ω)|²."),

 (942, 942, r"\[ \psi(t) \]", "haute",
  "§45 ondelette mère « Une famille peut être construite à partir d'une ondelette mère : [ ] ». Le \\psi a été détruit.",
  "Rendu : ψ(t)."),

 (946, 946, r"\[ \psi_{a,b}(t)=\frac{1}{\sqrt{a}}\psi\left(\frac{t-b}{a}\right) \]", "haute",
  "§45 « par translation et dilatation : [\\_{a,b}(t)=( )] ». Le \\psi a été détruit aux deux endroits ; la fraction de normalisation et l'argument ont été détruits.",
  "Rendu : ψ_{a,b}(t)=(1/√a)ψ((t−b)/a). Forme usuelle de la dilatation-translation."),

 (952, 952, r"\[ W(a,b)=\int x(t)\psi_{a,b}(t)\,dt \]", "haute",
  "§46 transformée en ondelettes continue « Une formulation classique est : [W(a,b)=x(t) dt] ». Le \\psi_{a,b}(t) a été détruit, ainsi que \\int et \\, .",
  "Rendu : W(a,b)=∫x(t)ψ_{a,b}(t)dt."),

 (964, 964, None, "inconnue",
  "§47 « L'échelle possède une relation inverse approximative avec la fréquence : [vide] [vide] ». Deux blocs vides consécutifs.",
  "Candidats : \\[ a\\propto\\frac{1}{f} \\] puis \\[ f\\approx\\frac{f_c}{a} \\]."),

 (966, 966, None, "inconnue",
  "§47, second bloc.",
  "Voir l. 964."),

 (1058, 1058, r"\[ x(t)=A\sin(2\pi f_0t) \]", "haute",
  "§52 signal stationnaire « Pour ce type de signal, une représentation fréquentielle … [x(t)=A(2f_0t)] La Fourier révèle clairement (f_0). » — le \\sin et le \\pi ont été détruits.",
  "Rendu : x(t)=A sin(2πf₀t)."),

 (1066, 1068, "\\[ x(t)=\\sin(2\\pi f_1t)+\\sin(2\\pi f_2t) \\]", "moyenne",
  "§53 signal non stationnaire « Supposons : [x(t)= ] Une Fourier globale révèle les fréquences mais perd une partie de l'information sur leur localisation temporelle. » — le bloc est vide ; l'exemple doit montrer deux fréquences successives ou un chirp.",
  "Candidat alternatif : un chirp, \\[ x(t)=\\sin(2\\pi f(t)t) \\]. Le premier candidat est le plus courant pour illustrer la perte de localisation."),

 (1085, 1085, None, "inconnue",
  "§54 reconnaissance vocale « On peut appliquer : [vide] On peut également utiliser : ».",
  "Candidat : \\[ \\text{une STFT ou des MFCC} \\]."),

 (1153, 1153, r"\[ x\to T(x) \]", "haute",
  "§57 « ### Prétraitement [ ] ### Extraction de caractéristiques ». La flèche a été détruite ; la structure « x → objet » est celle de toute la section.",
  "Rendu : x → T(x)."),

 (1157, 1157, r"\[ x\to \phi(x) \]", "moyenne",
  "§57 « ### Extraction de caractéristiques [x(x)] ». Le \\phi a été détruit, laissant deux x identiques en apparence.",
  "Candidat alternatif : x\\to \\varphi(x)."),

 (1161, 1161, r"\[ x\to \tilde{x} \]", "moyenne",
  "§57 « ### Réduction du bruit [x] ». Le tilde a été détruit.",
  "Candidat alternatif : x\\to \\hat{x}."),

 (1165, 1165, r"\[ x\to z \]", "haute",
  "§57 « ### Compression [xz] ### Représentation ». Deux lettres accolées : la flèche a été détruite.",
  "Rendu : x → z."),

 (1169, 1169, r"\[ x\to X \]", "moyenne",
  "§57 « ### Représentation [x] ### Analyse ». Un seul symbole subsiste ; la représentation transformée est notée en majuscule dans tout le document.",
  "Candidat alternatif : x\\to T(x), mais cela répéterait l. 1153."),

 (1190, 1190, None, "inconnue",
  "§58 « Une donnée temporelle devient ainsi une structure 2D exploitable par des architectures de vision. Cela crée un pont entre : [vide] ».",
  "Candidat : \\[ \\text{le traitement du signal et la vision par ordinateur} \\]."),

 (1226, 1226, None, "inconnue",
  "§60 transformée de Radon « Conceptuellement : [vide] Elle constitue notamment une base mathématique importante de la tomographie. »",
  "Candidat : \\[ R(\\rho,\\theta)=\\int f(x,y)\\,ds \\]."),

 (1258, 1258, None, "inconnue",
  "§62 transformées et simulation « Exemple conceptuel : [vide] Elles peuvent donc servir à : ».",
  "Candidat : \\[ \\mathcal{F}\\{u_{xx}\\}=-k^{2}U \\], repris au §64."),

 (1274, 1274, r"\[ u(x)\approx\sum_{k=0}^{N}a_k\phi_k(x) \]", "haute",
  "§63 méthodes spectrales « Par exemple : [u(x) \\_{k=0}^{N} a_k_k(x)] ». Le \\phi a été détruit (résidu _k), le \\sum réduit à \\_, et \\approx détruit.",
  "Rendu : u(x)≈Σ a_k φ_k(x)."),

 (1278, 1278, r"\[ \phi_k(x) \]", "haute",
  "§63 « avec : [ ] comme fonctions de base. » Le \\phi a été détruit.",
  "Rendu : φ_k(x)."),

 (1295, 1295, r"\[ u(x,t)\to U(k,t) \]", "haute",
  "§64 « Exemple conceptuel : [u(x,t) U(k,t)] ». La flèche a été détruite.",
  "Rendu : u(x,t) → U(k,t)."),

 (1301, 1301, r"\[ \mathcal{F}\left\{\frac{\partial^{2}u}{\partial x^{2}}\right\}=-k^{2}U(k,t) \]", "haute",
  "§64 « Par exemple : [{ } = -k^2U(k,t)] Cela peut transformer une PDE en une famille d'EDO. » — le \\mathcal{F} et la dérivée seconde ont été détruits ; seules les accolades et le membre de droite subsistent.",
  "Rendu : 𝓕{∂²u/∂x²}=−k²U(k,t)."),
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
