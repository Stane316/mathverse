#!/usr/bin/env python3
"""Construction du lot 3a : domaine I — Calcul differentiel, sections 1 a 40.

Chaque entree : (ligne_debut, ligne_fin, nouveau, confiance, justification, validation)
`nouveau` = None pour les blocs dont le contenu ne peut pas etre reconstruit.

L'ancien est relu dans le fichier au moment de la construction : les numeros de
ligne se rapportent a l'etat courant du clone (apres lots K, L, L bis).
"""

import json
import sys

SOURCE = "Maths-vers-Informatiques/Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md"
RACINE = "/home/user/_audit/connaissance"
SORTIE = "docs/restauration/propositions/domaine-I-lot3a.patch.json"

E = [
 (29, 29, r"\[ f:\mathbb{R}\to\mathbb{R} \]", "haute",
  "« Pour une fonction d'une variable : » — il ne reste que la lettre f et les deux-points. La phrase qui suit parle de f'(x) et de variation locale : la fonction est scalaire, de variable réelle. \\mathbb et \\to ont été détruits.",
  "Rendu : f : ℝ → ℝ. Même forme qu'en §5 (l. 226), ce qui confirme la lecture."),

 (75, 75, None, "inconnue",
  "« Une compréhension sérieuse du Machine Learning nécessite donc de comprendre au minimum : [vide] ». Aucun résidu : ce bloc contenait des mots, pas une équation. Très probablement une liste de prérequis (dérivées, gradients, optimisation), mais rien ne permet de la restituer.",
  "À trancher par l'auteur ; à défaut, mention « contenu perdu »."),

 (206, 206, r"\[ f:X\to Y \]", "haute",
  "« Une fonction associe une entrée à une sortie. » — X et Y subsistent, la flèche a été détruite.",
  "Rendu : f : X → Y."),

 (218, 218, r"\[ f_\theta(x) \]", "haute",
  "« En Machine Learning : [ ] désigne souvent un modèle dépendant de paramètres (θ). » — le θ nommé dans la phrase est l'indice détruit (même destruction que f_ en l. 1258, 1656).",
  "Rendu : f_θ(x)."),

 (226, 226, r"\[ f:\mathbb{R}\to\mathbb{R} \]", "haute",
  "§5 « Une fonction scalaire d'une variable possède la forme : ». Même reconstruction qu'en l. 29.",
  "Rendu : f : ℝ → ℝ."),

 (232, 232, r"\[ f(x)=\sin x \]", "moyenne",
  "§5, exemples de fonctions. Le nom de la fonction a été détruit — \\sin, \\cos, \\ln le sont partout dans ce document. L'ordre probable est x², sinus, exponentielle, logarithme, en miroir de la liste de dérivées de la section 12.",
  "Candidat alternatif : \\cos x. À confirmer par l'auteur."),

 (236, 236, r"\[ f(x)=\ln x \]", "moyenne",
  "§5, quatrième exemple. Même raisonnement qu'en l. 232.",
  "Candidat alternatif : \\cos x. À confirmer par l'auteur."),

 (244, 244, r"\[ \lim_{x\to a}f(x) \]", "haute",
  "§6 LIMITE. Le \\_ est le résidu de \\lim — cinq commandes le produisent dans ce corpus (\\lim, \\sum, \\int, \\prod, \\min), le contexte tranche. \\to a été détruit.",
  "Rendu : lim_{x→a} f(x). Cohérent avec la phrase « une variable se rapproche d'une valeur »."),

 (254, 254, r"\[ \lim_{x\to a}f(x)=f(a) \]", "haute",
  "§7 CONTINUITÉ « Une fonction est continue en (a) si : ». Même résidu qu'en l. 244, avec l'égalité à f(a).",
  "C'est la définition même de la continuité en un point."),

 (266, 266, r"\[ \frac{f(x+h)-f(x)}{h} \]", "haute",
  "§8 « Entre deux points (x) et (x+h) : [vide] mesure le taux de variation moyen. » — le bloc est vide : \\frac a été détruit (en l. 1266, \\frac{1}{n} n'a laissé que 1n ; ici, rien). Le taux de variation moyen ne peut être que ce quotient.",
  "L'expression ne fait intervenir que f, x et h, tous nommés dans la phrase qui précède."),

 (278, 278, r"\[ f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h} \]", "haute",
  "§9 DÉRIVÉE « La dérivée de (f) en (x) est : [ ] si cette limite existe. » — le résidu \\_{h} conjugue \\lim (détruit) et h→0 (la flèche détruite). La phrase finale nomme explicitement une limite.",
  "Définition standard de la dérivée ; le quotient apparaît déjà en l. 266."),

 (332, 332, None, "inconnue",
  "« Ainsi : [vide] est une application fondamentale du calcul différentiel. » — après l'accélération. Le sujet grammatical est un nom ou une formule ; rien ne subsiste.",
  "Candidat : \\text{la dérivation} ou \\text{le calcul des dérivées}. À trancher par l'auteur."),

 (340, 340, r"\[ \frac{d}{dx}x^{n}=nx^{n-1} \]", "haute",
  "§12 « Pour (n) : ». Le résidu x<sup>n=nx</sup>{n-1} se déplie en x^{n}=nx^{n-1} : c'est la règle de la puissance. Le préfixe \\frac{d}{dx} est une hypothèse, mais il explique pourquoi les cinq blocs suivants ont tous perdu leur opérateur.",
  "Rendu : d/dx x^n = n x^{n-1}. La dérivée de x^n est bien n x^{n-1}."),

 (344, 344, r"\[ \frac{d}{dx}c=0 \]", "haute",
  "§12 « Constante : ». Le bloc ne conserve que c=0 ; l'opérateur a été détruit.",
  "Rendu : d/dx c = 0. La dérivée d'une constante est nulle."),

 (348, 348, r"\[ \frac{d}{dx}e^{x}=e^{x} \]", "haute",
  "§12 « Exponentielle : ». Le résidu e<sup>x=e</sup>x se déplie en e^{x}=e^{x}.",
  "e^x est sa propre dérivée."),

 (352, 352, r"\[ \frac{d}{dx}(\ln x)=\frac{1}{x} \]", "haute",
  "§12 « Logarithme : ». Le résidu (x)=1x se lit : \\ln détruit à l'intérieur des parenthèses, et \\frac{1}{x} réduit à 1x (contenu conservé, accolades perdues) — exactement le comportement observé en l. 1266 avec \\frac{1}{n} → 1n.",
  "d/dx ln x = 1/x."),

 (356, 356, r"\[ \frac{d}{dx}(\sin x)=\cos x \]", "haute",
  "§12 « Sinus : ». Le résidu (x)=(x) montre les deux parenthèses vidées de \\sin et \\cos.",
  "d/dx sin x = cos x."),

 (360, 360, r"\[ \frac{d}{dx}(\cos x)=-\sin x \]", "haute",
  "§12 « Cosinus : ». Le résidu (x)=-(x) : le signe moins a survécu, ce qui distingue sans ambiguïté le cosinus du sinus.",
  "d/dx cos x = −sin x. Le signe conservé est la preuve."),

 (392, 392, r"\[ f(x)=\frac{u(x)}{v(x)} \]", "haute",
  "§16 RÈGLE DU QUOTIENT « Si : ». Le bloc suivant conserve {v(x)^2}, dénominateur de la dérivée : la fonction est donc un quotient u/v, et u, v sont les lettres employées par la section 15 (produit).",
  "La dérivée de u/v a bien v² au dénominateur, ce que confirme le bloc suivant."),

 (396, 396, r"\[ f'(x)=\frac{u'(x)v(x)-u(x)v'(x)}{v(x)^2} \]", "haute",
  "« alors : [ ] avec (v(x)). » — le résidu {v(x)^2} est le dénominateur ; le numérateur a été détruit avec \\frac. La fin de phrase (« avec v(x) ») désigne la condition de non-nullité.",
  "Formule standard du quotient, vérifiable à la main."),

 (410, 410, r"\[ \frac{dy}{dx}=f'(g(x))g'(x) \]", "haute",
  "§17 « Si y=f(g(x)) alors : [= f'(g(x))g'(x)] ». Le membre de droite est intact ; le membre de gauche a été détruit (\\frac ne laisse rien ici).",
  "La dérivée de f∘g est f'(g)·g'."),

 (414, 414, r"\[ \frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx} \]", "moyenne",
  "§17 « Autrement dit : [vide] ». La phrase annonce une reformulation de la règle de la chaîne, donc la notation de Leibniz. Bloc vide : les \\frac ont été détruites.",
  "Candidat alternatif : \\frac{dz}{dx}=\\frac{dz}{dy}\\frac{dy}{dx}. Les variables restent à confirmer par l'auteur."),

 (424, 424, r"\[ x \to z_1 \to a_1 \to z_2 \to a_2 \to L \]", "haute",
  "§18 « Un réseau neuronal est essentiellement une composition de fonctions. Par exemple : [ ] ». Les six termes sont intacts ; les flèches ont été détruites — même destruction qu'en l. 1280 (f(x) f'(x)) et l. 3121.",
  "Rendu : x → z₁ → a₁ → z₂ → a₂ → L, cohérent avec la composition écrite juste après."),

 (448, 448, r"\[ x^{2}+y^{2}=1 \]", "haute",
  "§19 DÉRIVATION IMPLICITE « Exemple : ». Le résidu x<sup>2+y</sup>2=1 se déplie en x²+y²=1 : le cercle unité, exemple canonique de dérivation implicite.",
  "L'équation d'un cercle de rayon 1 ; la suite du §19 la dérive."),

 (452, 452, r"\[ 2x+2yy'=0 \]", "haute",
  "§19 « donne : ». Dériver x²+y²=1 par rapport à x donne 2x+2yy'=0. Le résidu 2x+2y=0 a perdu le y' (le prime a été détruit) ; sans lui, l'équation serait fausse.",
  "Vérifier en dérivant x²+y²=1 : 2x+2yy'=0."),

 (456, 456, r"\[ y'=-\frac{x}{y} \]", "haute",
  "§19 « donc : ». Le résidu =- ne conserve que le signe et l'égalité ; \\frac a été détruit.",
  "Isoler y' dans 2x+2yy'=0 donne bien y'=−x/y."),

 (508, 508, r"\[ \Delta f\approx df \]", "haute",
  "§22 « Pour une petite variation (dx) : [ ] donc : ». Le résidu fdf montre deux f encadrant df : les deux \\Delta ont été détruits, ainsi que \\approx.",
  "Rendu : Δf ≈ df. La différentielle approxime la variation."),

 (512, 512, r"\[ \Delta f\approx f'(x)\Delta x \]", "haute",
  "« donc : ». Le résidu ff'(x)x : \\Delta détruit devant f et devant x, \\approx détruit.",
  "Rendu : Δf ≈ f'(x)Δx. C'est la définition même de la différentielle."),

 (518, 518, r"\[ f(x)\approx f(a)+f'(a)(x-a) \]", "haute",
  "§23 APPROXIMATION LINÉAIRE « Autour d'un point (a) : ». Tous les termes sont présents ; seul \\approx a été détruit.",
  "C'est l'approximation par la tangente, comme le dit la phrase suivante."),

 (528, 531, "\[ f(x)\\approx f(a)\n\n+ f'(a)(x-a)\n+ \\frac{f''(a)}{2}(x-a)^2 + \\cdots \]", "haute",
  "§24 TAYLOR « Autour de (a) : ». Le résidu conserve f'(a)(x-a) et (x-a)^2 ; manquent \\approx, le facteur \\frac{f''(a)}{2} et les points de suite. Artefact signalé : les lignes commençant par + ont été transformées en puces -, le même qu'en l. 535, 545, 1031, 1063.",
  "Développement de Taylor à l'ordre 2 autour de a."),

 (535, 537, "\[ f(x)=\\sum_{k=0}^{n}\\frac{f^{(k)}(a)}{k!}(x-a)^k\n\n+ R_n(x) \]", "haute",
  "§24 « Formellement : ». Le \\_ est le résidu de \\sum ; \\frac{f^{(k)}(a)}{k!} a été détruit ; R_n(x) a survécu, et la phrase suivante le nomme (« le terme R_n représente le reste »).",
  "Somme de Taylor finie avec reste de Lagrange."),

 (545, 548, "\[ f(x+\\Delta x)\\approx f(x)\n\n+ \\nabla f(x)^T\\Delta x\n+ \\frac{1}{2}\\Delta x^TH\\Delta x \]", "haute",
  "§25 « Autour d'un point (x), une fonction peut être approximée par : ». Résidus : f(x+x) → f(x+Δx) ; f(x)^Tx → \\nabla f(x)^TΔx ; x^THx → \\frac12 Δx^T H Δx. Les \\Delta, \\nabla et \\frac ont été détruits.",
  "Taylor à l'ordre 2 en plusieurs variables ; le facteur 1/2 est imposé par la dérivation seconde."),

 (559, 559, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§26 « On considère maintenant : [ ] » suivi d'un exemple à deux variables. \\mathbb et \\to détruits.",
  "Rendu : f : ℝⁿ → ℝ."),

 (563, 563, r"\[ f(x,y)=x^{2}+y^{2} \]", "haute",
  "§26 « Exemple : ». Le résidu x<sup>2+y</sup>2 se déplie en x²+y².",
  "Cohérent avec la fonction à deux variables annoncée."),

 (575, 575, r"\[ \frac{\partial f}{\partial x} \]", "haute",
  "§27 « La dérivée partielle par rapport à (x) consiste à faire varier (x) en maintenant les autres variables constantes. [vide] ». Le bloc est vide : \\frac et \\partial détruits. Cette notation est celle du document entier (l. 583, 587, 689).",
  "Rendu : ∂f/∂x."),

 (579, 579, r"\[ f(x,y)=x^{2}+3xy+y^{2} \]", "haute",
  "§27 « Exemple : ». La dérivée partielle donnée juste après vaut 2x+3y, qui est bien celle de x²+3xy+y² par rapport à x.",
  "Vérifier : ∂/∂x (x²+3xy+y²) = 2x+3y."),

 (583, 583, r"\[ \frac{\partial f}{\partial x}=2x+3y \]", "haute",
  "§27 « Alors : ». Membre de gauche détruit (\\frac, \\partial), membre de droite intact.",
  "Cohérent avec la fonction de la ligne précédente."),

 (587, 587, r"\[ \frac{\partial f}{\partial y}=3x+2y \]", "haute",
  "§27 « et : ». Membre de gauche détruit.",
  "Vérifier : ∂/∂y (x²+3xy+y²) = 3x+2y."),

 (593, 593, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§28 GRADIENT « Pour : [ ] le gradient est : ». \\mathbb et \\to détruits.",
  "Rendu : f : ℝⁿ → ℝ."),

 (597, 599, "\\[ \\nabla f(x)=\\begin{pmatrix}\\frac{\\partial f}{\\partial x_1}\\\\ \\vdots \\\\ \\frac{\\partial f}{\\partial x_n}\\end{pmatrix} \]", "haute",
  "§28 « le gradient est : [trois lignes vides] Le gradient est donc un vecteur. » — \\nabla détruit, contenu matriciel détruit. Le bloc occupe trois lignes : le contenu était présenté en colonne.",
  "Rendu : un vecteur colonne de dérivées partielles. Alternative : la forme transposée (∂f/∂x₁, …, ∂f/∂xₙ)^T."),

 (609, 609, r"\[ \|\nabla f(x)\| \]", "haute",
  "§29 « Sa norme : [ ] mesure l'intensité maximale de cette variation directionnelle. » — \\| et \\nabla détruits.",
  "Rendu : ‖∇f(x)‖."),

 (615, 615, r"\[ -\nabla f(x) \]", "haute",
  "§29 « La direction de descente maximale est : [ ] C'est le fondement de la descente de gradient. » — \\nabla détruit, signe moins conservé.",
  "Rendu : −∇f(x)."),

 (623, 623, r"\[ D_uf(x)=\nabla f(x)^Tu \]", "haute",
  "§30 DÉRIVÉE DIRECTIONNELLE « Pour une direction (u), la dérivée directionnelle est : [ ] ». \\nabla détruit.",
  "La dérivée directionnelle est le produit scalaire du gradient et de la direction."),

 (629, 629, r"\[ D_uf(x)=\nabla f(x)\cdot u \]", "haute",
  "§30 « Si (u) est unitaire : [ ] ». \\nabla et \\cdot détruits.",
  "Cohérent avec la ligne précédente."),

 (635, 635, r"\[ D_uf(x)=\|\nabla f(x)\|\cos\theta \]", "haute",
  "§31 « Pour une direction unitaire (u) : [ ] où (θ) est l'angle entre le gradient et (u). » — \\| , \\nabla et \\cos détruits, mais la phrase qui suit nomme explicitement l'angle.",
  "Rendu : D_u f(x)=‖∇f(x)‖cos θ."),

 (641, 641, r"\[ u=\frac{\nabla f(x)}{\|\nabla f(x)\|} \]", "haute",
  "§31 « Le maximum est obtenu lorsque : [ ] ». Le résidu {|f(x)|} est le dénominateur \\|\\nabla f(x)\\| ; le numérateur a été détruit avec \\frac.",
  "La direction de plus forte pente est le gradient normalisé."),

 (645, 645, r"\[ u=-\frac{\nabla f(x)}{\|\nabla f(x)\|} \]", "haute",
  "§31 « Le minimum lorsque : [ ] ». Même résidu que la ligne précédente, avec le signe moins en prime.",
  "Strict opposé du cas précédent."),

 (657, 657, r"\[ \nabla f(x,y)\perp\{(x,y)\mid f(x,y)=c\} \]", "moyenne",
  "§32 SURFACES DE NIVEAU « Le gradient est orthogonal aux surfaces de niveau. Ainsi : [ ] ». \\nabla, \\perp et \\mid détruits. Le bloc répète sous forme mathématique ce que la phrase précédente énonce.",
  "Candidat alternatif : \\nabla f(x,y)\\cdot T=0, T vecteur tangent. Formulation à choisir par l'auteur."),

 (667, 667, r"\[ f:\mathbb{R}^{n}\to\mathbb{R}^{m} \]", "haute",
  "§33. Le résidu f:<sup>n</sup>m : \\mathbb détruit, les \\mathbb{R} réduits à <sup> par la conversion des exposants.",
  "Rendu : f : ℝⁿ → ℝᵐ."),

 (675, 675, r"\[ \frac{\|r(h)\|}{\|h\|}\to 0 \]", "haute",
  "§33 « avec : [vide] lorsque : [h] ». Le reste r(h) doit être négligeable devant h : c'est la définition de la différentiabilité. \\frac, \\| et \\to détruits.",
  "Équivalent à r(h)=o(‖h‖)."),

 (679, 679, r"\[ h\to 0 \]", "haute",
  "§33 « lorsque : [ ] ». \\to détruit.",
  "Rendu : h → 0."),

 (685, 685, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§34 DIFFÉRENTIELLE TOTALE « Pour : [ ] la différentielle est : ». \\mathbb et \\to détruits.",
  "Rendu : f : ℝⁿ → ℝ."),

 (689, 689, r"\[ df=\sum_{i=1}^{n}\frac{\partial f}{\partial x_i}dx_i \]", "haute",
  "§34 « la différentielle est : [ ] ». Le \\_ est le résidu de \\sum ; \\frac et \\partial détruits.",
  "Somme des différentielles partielles."),

 (693, 693, r"\[ df=\nabla f(x)^Tdx \]", "haute",
  "§34 « Sous forme vectorielle : [ ] ». \\nabla détruit ; la phrase suivante dit exactement qu'il s'agit du lien entre différentielle et gradient.",
  "Équivalent vectoriel de la ligne précédente."),

 (701, 701, r"\[ F:\mathbb{R}^{n}\to\mathbb{R}^{m} \]", "haute",
  "§35 JACOBIENNE « Pour une fonction : [ ] ». \\mathbb et \\to détruits.",
  "Rendu : F : ℝⁿ → ℝᵐ."),

 (705, 707, "\\[ J_F(x)=\\begin{pmatrix}\\frac{\\partial F_1}{\\partial x_1}&\\cdots&\\frac{\\partial F_1}{\\partial x_n}\\\\ \\vdots&\\ddots&\\vdots\\\\ \\frac{\\partial F_m}{\\partial x_1}&\\cdots&\\frac{\\partial F_m}{\\partial x_n}\\end{pmatrix} \]", "haute",
  "§35 « la Jacobienne est la matrice des dérivées premières : [trois lignes vides] Sa dimension est : [m n] ». Le bloc sur trois lignes et la dimension m×n imposent une matrice.",
  "Cohérence : m lignes, n colonnes (l. 711)."),

 (711, 711, r"\[ m\times n \]", "haute",
  "§35 « Sa dimension est : [ ] ». \\times détruit.",
  "Rendu : m × n."),

 (717, 717, r"\[ F(x+\Delta x)\approx F(x)+J_F(x)\Delta x \]", "haute",
  "§36 « Localement : [ ] ». Résidu F(x+x) F(x)+J_F(x)x : les \\Delta et le \\approx ont été détruits.",
  "Linéarisation locale par la Jacobienne."),

 (725, 725, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§37 « Pour : [ ] le gradient est un vecteur. » \\mathbb et \\to détruits.",
  "Rendu : f : ℝⁿ → ℝ."),

 (731, 731, r"\[ F:\mathbb{R}^{n}\to\mathbb{R}^{m} \]", "haute",
  "§37 « Pour : [ ] la Jacobienne est une matrice. » \\mathbb et \\to détruits.",
  "Rendu : F : ℝⁿ → ℝᵐ."),

 (753, 753, r"\[ f:\mathbb{R}^{n}\to\mathbb{R} \]", "haute",
  "§38 HESSIENNE « Pour une fonction scalaire : [ ] ». \\mathbb et \\to détruits.",
  "Rendu : f : ℝⁿ → ℝ."),

 (757, 757, r"\[ H_f(x)=\nabla^{2}f(x) \]", "haute",
  "§38 « la Hessienne contient les dérivées secondes : [ ] ». Le résidu ^2f(x) : le \\nabla a été détruit, l'exposant 2 est resté.",
  "Rendu : H_f(x)=∇²f(x)."),

 (761, 763, "\\[ H_f(x)=\\begin{pmatrix}\\frac{\\partial^{2}f}{\\partial x_1^{2}}&\\cdots&\\frac{\\partial^{2}f}{\\partial x_1\\partial x_n}\\\\ \\vdots&\\ddots&\\vdots\\\\ \\frac{\\partial^{2}f}{\\partial x_n\\partial x_1}&\\cdots&\\frac{\\partial^{2}f}{\\partial x_n^{2}}\\end{pmatrix} \]", "haute",
  "§38 « avec : [trois lignes vides] ». La Hessienne est la matrice des dérivées secondes ; le bloc occupe trois lignes.",
  "Matrice carrée n×n, symétrique sous les hypothèses de la section 40."),

 (784, 784, r"\[ \frac{\partial^{2}f}{\partial x_i\partial x_j}=\frac{\partial^{2}f}{\partial x_j\partial x_i} \]", "haute",
  "§40 SYMÉTRIE DE LA HESSIENNE. Les résidus {x_ix_j} et {x_jx_i} sont les dénominateurs des deux \\frac ; les numérateurs \\partial^2f ont été détruits.",
  "La phrase suivante conclut : « La Hessienne est alors symétrique. »"),
]

VALIDATION = {
 "haute": "Rendu LaTeX conforme au contexte ; l'équation est la seule possible.",
 "moyenne": "Rendu plausible ; un choix de l'auteur reste nécessaire.",
 "inconnue": "Aucune reconstruction possible : le bloc contenait des mots.",
}


def main(mode="json"):
    lignes = open(f"{RACINE}/{SOURCE}", encoding="utf-8").read().split("\n")
    out = []
    for deb, fin, nouveau, conf, justif, valid in E:
        ancien = "\n".join(lignes[deb - 1:fin])
        out.append({
            "fichier": SOURCE,
            "ligne": deb,
            "ancien": ancien,
            "nouveau": nouveau,
            "confiance": conf,
            "justification": justif,
            "validation": valid,
        })
    json.dump(out, open(SORTIE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    c = Counter(e[3] for e in E)
    print(f"{len(E)} entrees -> {SORTIE}  {dict(c)}")
    return out


if __name__ == "__main__":
    main()
