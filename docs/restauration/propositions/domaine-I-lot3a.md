# LOT 3a — DOMAINE I : CALCUL DIFFÉRENTIEL (sections 1 à 40)

**Date :** 2026-10-18 · **Statut :** propositions soumises, non appliquées
**Document :** `Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md`
**Portée :** lignes 29 à 784, soit les sections 1 à 40. Le reste du document (sections 41 à 179, lignes 792 à 3175) fera l'objet du **lot 3b**.
**Méthode :** relecture intégrale des 318 blocs d'affichage du document, un par un — pas seulement les blocs signalés par l'inventaire.

---

## 1. Ce que la lecture intégrale a révélé

L'inventaire automatique signalait 109 blocs pour ce document ; la lecture exhaustive en montre
environ **150 touchés**. L'écart vient de trois destructions invisibles aux heuristiques.

### 1.1 Règles de dégradation propres au document I

| Résidu | Commande détruite | Exemple |
|---|---|---|
| `\_` | `\lim` (et `\sum`) | `\[ \_{xa}f(x) \]` → `\lim_{x\to a}f(x)` |
| `()` ou `_` | lettres grecques (`\theta`, `\Delta`) | `J()` → `J(\theta)` ; `f_(x)` → `f_\theta(x)` |
| rien | `\nabla` | `f(x)` → `\nabla f(x)` |
| `AB` | `\frac{A}{B}` | `1n` → `\frac{1}{n}` ; `1x` → `\frac{1}{x}` |
| `(x)` | `\sin`, `\cos`, `\ln`, `\sigma` | `(x)=(x)` → `\frac{d}{dx}(\sin x)=\cos x` |
| `<sup>…` | `^{…}` converti en balise HTML | `x<sup>2+y</sup>2` → `x^2+y^2` |
| deux termes accolés | `\to`, `\approx`, `\times`, `\|`, `\cdot`, `\perp` détruits | `f(x) f'(x)` → `f(x)\to f'(x)` |
| `- ` en tête | artefact : un `+` de début de ligne devient une puce | blocs Taylor (l. 528, 535, 545) |

### 1.2 Deux régimes de destruction des fractions

C'est le point le plus délicat du lot, et il justifie que plusieurs reconstructions soient
présentées avec leur raisonnement :

- **régime « contenu conservé »** : `\frac{1}{n}` laisse `1n`, `\frac{1}{x}` laisse `1x` — les
  arguments restent, les accolades disparaissent ;
- **régime « tout détruit »** : `\frac{d}{dx}` et `\frac{u'v-uv'}{v^2}` ne laissent rien.

Le second régime explique les blocs vidés des sections 16, 17 et 24. Les reconstructions
correspondantes s'appuient donc sur la forme canonique de la formule attendue, pas sur un résidu :
c'est indiqué dans la justification de chaque ligne concernée (l. 266, 340-360, 392-396, 414, 535).

### 1.3 Le préfixe `\frac{d}{dx}` est une hypothèse

Les six blocs de la section 12 (dérivées fondamentales) ont tous perdu leur opérateur de
dérivation. Je propose `\frac{d}{dx}`, cohérent avec le fait que les six blocs aient été vidés de
la même manière. Les **égalités elles-mêmes ne font pas débat** — `x^n = nx^{n-1}`, `(c)' = 0`,
`e^x = e^x`, `(\ln x)' = 1/x`, `(\sin x)' = \cos x`, `(\cos x)' = -\sin x` —, seul l'opérateur de
gauche est restitué par hypothèse. Si vous préférez `(…)’`, un simple remplacement suffit.

## 2. Blocs dont le contenu ne peut pas être restitué (2)

| Ligne | Contexte | Pourquoi |
|---:|---|---|
| 75 | « nécessite donc de comprendre au minimum : » | bloc de mots, liste de prérequis probable — aucune trace |
| 332 | « Ainsi : … est une application fondamentale du calcul différentiel. » | le sujet de la phrase a disparu ; candidat : « la dérivation » |

## 3. Corps technique

**Correctif :** `domaine-I-lot3a.patch.json` — 64 entrées : 58 haute, 4 moyenne, 2 inconnue — **62 applicables**

### Confiance haute (58)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 29 | `\[ f : \]` | `\[ f:\mathbb{R}\to\mathbb{R} \]` | Rendu : f : ℝ → ℝ. Même forme qu'en §5 (l. 226), ce qui confirme la lecture. |
| 206 | `\[ f : XY \]` | `\[ f:X\to Y \]` | Rendu : f : X → Y. |
| 218 | `\[ f_(x) \]` | `\[ f_\theta(x) \]` | Rendu : f_θ(x). |
| 226 | `\[ f: \]` | `\[ f:\mathbb{R}\to\mathbb{R} \]` | Rendu : f : ℝ → ℝ. |
| 244 | `\[ \_{xa}f(x) \]` | `\[ \lim_{x\to a}f(x) \]` | Rendu : lim_{x→a} f(x). Cohérent avec la phrase « une variable se rapproche d'une valeur ». |
| 254 | `\[ \_{xa}f(x)=f(a) \]` | `\[ \lim_{x\to a}f(x)=f(a) \]` | C'est la définition même de la continuité en un point. |
| 266 | `\[ \]` | `\[ \frac{f(x+h)-f(x)}{h} \]` | L'expression ne fait intervenir que f, x et h, tous nommés dans la phrase qui précède. |
| 278 | `\[ f’(x) = \_{h} \]` | `\[ f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h} \]` | Définition standard de la dérivée ; le quotient apparaît déjà en l. 266. |
| 340 | `\[ x<sup>n=nx</sup>{n-1} \]` | `\[ \frac{d}{dx}x^{n}=nx^{n-1} \]` | Rendu : d/dx x^n = n x^{n-1}. La dérivée de x^n est bien n x^{n-1}. |
| 344 | `\[ c=0 \]` | `\[ \frac{d}{dx}c=0 \]` | Rendu : d/dx c = 0. La dérivée d'une constante est nulle. |
| 348 | `\[ e<sup>x=e</sup>x \]` | `\[ \frac{d}{dx}e^{x}=e^{x} \]` | e^x est sa propre dérivée. |
| 352 | `\[ (x)=1x \]` | `\[ \frac{d}{dx}(\ln x)=\frac{1}{x} \]` | d/dx ln x = 1/x. |
| 356 | `\[ (x)=(x) \]` | `\[ \frac{d}{dx}(\sin x)=\cos x \]` | d/dx sin x = cos x. |
| 360 | `\[ (x)=-(x) \]` | `\[ \frac{d}{dx}(\cos x)=-\sin x \]` | d/dx cos x = −sin x. Le signe conservé est la preuve. |
| 392 | `\[ f(x)= \]` | `\[ f(x)=\frac{u(x)}{v(x)} \]` | La dérivée de u/v a bien v² au dénominateur, ce que confirme le bloc suivant. |
| 396 | `\[ f’(x) = {v(x)^2} \]` | `\[ f'(x)=\frac{u'(x)v(x)-u(x)v'(x)}{v(x)^2} \]` | Formule standard du quotient, vérifiable à la main. |
| 410 | `\[ = f’(g(x))g’(x) \]` | `\[ \frac{dy}{dx}=f'(g(x))g'(x) \]` | La dérivée de f∘g est f'(g)·g'. |
| 424 | `\[ x z_1 a_1 z_2 a_2 L \]` | `\[ x \to z_1 \to a_1 \to z_2 \to a_2 \to L \]` | Rendu : x → z₁ → a₁ → z₂ → a₂ → L, cohérent avec la composition écrite juste après. |
| 448 | `\[ x<sup>2+y</sup>2=1 \]` | `\[ x^{2}+y^{2}=1 \]` | L'équation d'un cercle de rayon 1 ; la suite du §19 la dérive. |
| 452 | `\[ 2x+2y=0 \]` | `\[ 2x+2yy'=0 \]` | Vérifier en dérivant x²+y²=1 : 2x+2yy'=0. |
| 456 | `\[ =- \]` | `\[ y'=-\frac{x}{y} \]` | Isoler y' dans 2x+2yy'=0 donne bien y'=−x/y. |
| 508 | `\[ fdf \]` | `\[ \Delta f\approx df \]` | Rendu : Δf ≈ df. La différentielle approxime la variation. |
| 512 | `\[ ff’(x)x \]` | `\[ \Delta f\approx f'(x)\Delta x \]` | Rendu : Δf ≈ f'(x)Δx. C'est la définition même de la différentielle. |
| 518 | `\[ f(x) f(a)+f’(a)(x-a) \]` | `\[ f(x)\approx f(a)+f'(a)(x-a) \]` | C'est l'approximation par la tangente, comme le dit la phrase suivante. |
| 528 | `\[ f(x) f(a) ⏎  ⏎ - f’(a)(x-a) ⏎ - (x-a)^2 + \` | `\[ f(x)\approx f(a) ⏎  ⏎ + f'(a)(x-a) ⏎ + \frac{f''(a)}{2}(x-a` | Développement de Taylor à l'ordre 2 autour de a. |
| 535 | `\[ f(x) = \_{k=0}^{n} (x-a)^k ⏎  ⏎ - R_n(x) \]` | `\[ f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k ⏎  ⏎ + R_n(` | Somme de Taylor finie avec reste de Lagrange. |
| 545 | `\[ f(x+x) f(x) ⏎  ⏎ - f(x)^Tx ⏎ - x^THx \]` | `\[ f(x+\Delta x)\approx f(x) ⏎  ⏎ + \nabla f(x)^T\Delta x ⏎ + ` | Taylor à l'ordre 2 en plusieurs variables ; le facteur 1/2 est imposé par la dérivation seconde. |
| 559 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 563 | `\[ f(x,y)=x<sup>2+y</sup>2 \]` | `\[ f(x,y)=x^{2}+y^{2} \]` | Cohérent avec la fonction à deux variables annoncée. |
| 575 | `\[ \]` | `\[ \frac{\partial f}{\partial x} \]` | Rendu : ∂f/∂x. |
| 579 | `\[ f(x,y)=x<sup>2+3xy+y</sup>2 \]` | `\[ f(x,y)=x^{2}+3xy+y^{2} \]` | Vérifier : ∂/∂x (x²+3xy+y²) = 2x+3y. |
| 583 | `\[ = 2x+3y \]` | `\[ \frac{\partial f}{\partial x}=2x+3y \]` | Cohérent avec la fonction de la ligne précédente. |
| 587 | `\[ = 3x+2y \]` | `\[ \frac{\partial f}{\partial y}=3x+2y \]` | Vérifier : ∂/∂y (x²+3xy+y²) = 3x+2y. |
| 593 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 597 | `\[ f(x) = ⏎  ⏎ \]` | `\[ \nabla f(x)=\begin{pmatrix}\frac{\partial f}{\partial x_1}\` | Rendu : un vecteur colonne de dérivées partielles. Alternative : la forme transposée (∂f/∂x₁, …, ∂f/∂xₙ)^T. |
| 609 | `\[ \|f(x)\| \]` | `\[ \\|\nabla f(x)\\| \]` | Rendu : ‖∇f(x)‖. |
| 615 | `\[ -f(x) \]` | `\[ -\nabla f(x) \]` | Rendu : −∇f(x). |
| 623 | `\[ D_uf(x) = f(x)^Tu \]` | `\[ D_uf(x)=\nabla f(x)^Tu \]` | La dérivée directionnelle est le produit scalaire du gradient et de la direction. |
| 629 | `\[ D_uf(x)=f(x)u \]` | `\[ D_uf(x)=\nabla f(x)\cdot u \]` | Cohérent avec la ligne précédente. |
| 635 | `\[ D_uf(x) = \|f(x)\| \]` | `\[ D_uf(x)=\\|\nabla f(x)\\|\cos\theta \]` | Rendu : D_u f(x)=‖∇f(x)‖cos θ. |
| 641 | `\[ u= {\|f(x)\|} \]` | `\[ u=\frac{\nabla f(x)}{\\|\nabla f(x)\\|} \]` | La direction de plus forte pente est le gradient normalisé. |
| 645 | `\[ u= - {\|f(x)\|} \]` | `\[ u=-\frac{\nabla f(x)}{\\|\nabla f(x)\\|} \]` | Strict opposé du cas précédent. |
| 667 | `\[ f:<sup>n</sup>m \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R}^{m} \]` | Rendu : f : ℝⁿ → ℝᵐ. |
| 675 | `\[ \]` | `\[ \frac{\\|r(h)\\|}{\\|h\\|}\to 0 \]` | Équivalent à r(h)=o(‖h‖). |
| 679 | `\[ h \]` | `\[ h\to 0 \]` | Rendu : h → 0. |
| 685 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 689 | `\[ df = \_{i=1}^{n} dx_i \]` | `\[ df=\sum_{i=1}^{n}\frac{\partial f}{\partial x_i}dx_i \]` | Somme des différentielles partielles. |
| 693 | `\[ df=f(x)^Tdx \]` | `\[ df=\nabla f(x)^Tdx \]` | Équivalent vectoriel de la ligne précédente. |
| 701 | `\[ F:<sup>n</sup>m \]` | `\[ F:\mathbb{R}^{n}\to\mathbb{R}^{m} \]` | Rendu : F : ℝⁿ → ℝᵐ. |
| 705 | `\[ J_F(x) = ⏎  ⏎ \]` | `\[ J_F(x)=\begin{pmatrix}\frac{\partial F_1}{\partial x_1}&\cd` | Cohérence : m lignes, n colonnes (l. 711). |
| 711 | `\[ mn \]` | `\[ m\times n \]` | Rendu : m × n. |
| 717 | `\[ F(x+x) F(x)+J_F(x)x \]` | `\[ F(x+\Delta x)\approx F(x)+J_F(x)\Delta x \]` | Linéarisation locale par la Jacobienne. |
| 725 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 731 | `\[ F:<sup>n</sup>m \]` | `\[ F:\mathbb{R}^{n}\to\mathbb{R}^{m} \]` | Rendu : F : ℝⁿ → ℝᵐ. |
| 753 | `\[ f:^n \]` | `\[ f:\mathbb{R}^{n}\to\mathbb{R} \]` | Rendu : f : ℝⁿ → ℝ. |
| 757 | `\[ H_f(x) = ^2f(x) \]` | `\[ H_f(x)=\nabla^{2}f(x) \]` | Rendu : H_f(x)=∇²f(x). |
| 761 | `\[ H_f(x) = ⏎  ⏎ \]` | `\[ H_f(x)=\begin{pmatrix}\frac{\partial^{2}f}{\partial x_1^{2}` | Matrice carrée n×n, symétrique sous les hypothèses de la section 40. |
| 784 | `\[ {x_ix_j} = {x_jx_i} \]` | `\[ \frac{\partial^{2}f}{\partial x_i\partial x_j}=\frac{\parti` | La phrase suivante conclut : « La Hessienne est alors symétrique. » |

### Confiance moyenne (4)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 232 | `\[ f(x)=(x) \]` | `\[ f(x)=\sin x \]` | Candidat alternatif : \cos x. À confirmer par l'auteur. |
| 236 | `\[ f(x)=(x) \]` | `\[ f(x)=\ln x \]` | Candidat alternatif : \cos x. À confirmer par l'auteur. |
| 414 | `\[ \]` | `\[ \frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx} \]` | Candidat alternatif : \frac{dz}{dx}=\frac{dz}{dy}\frac{dy}{dx}. Les variables restent à confirmer par l'auteur. |
| 657 | `\[ f(x,y) \]` | `\[ \nabla f(x,y)\perp\{(x,y)\mid f(x,y)=c\} \]` | Candidat alternatif : \nabla f(x,y)\cdot T=0, T vecteur tangent. Formulation à choisir par l'auteur. |

### Confiance inconnue — décision requise (2)

| Ligne | Bloc actuel | Ce que le bloc contenait |
|---:|---|---|
| 75 | `\[ \]` | « Une compréhension sérieuse du Machine Learning nécessite donc de comprendre au minimum : [vide] ». Aucun résidu : ce bloc contenait des mots, pas une équation |
| 332 | `\[ \]` | « Ainsi : [vide] est une application fondamentale du calcul différentiel. » — après l'accélération. Le sujet grammatical est un nom ou une formule ; rien ne sub |

