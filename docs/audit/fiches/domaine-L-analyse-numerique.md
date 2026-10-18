# FICHE DE DOMAINE L — ANALYSE NUMÉRIQUE

**Date :** 2026-10-18 — **Phase :** 1 (audit documentaire) — **Statut :** fiche 2/21, **partiellement vérifiée**
**Source :** `Maths-vers-Informatiques/DOCUMENT L — ANALYSE NUMÉRIQUE.md`
**Rédigée sur le document restauré** — lots L et 2 bis appliqués (102 écritures), le 2026-10-18.
Voir `docs/restauration/annexes/rapport-application-L.md` et `…-L-lot2bis.md`.
**Outils :** `tools/audit-phase1/extract_domain.py`, comptage manuel des blocs `\[…\]`
**Convention :** ✅ vérifié par lecture ou mesure · ⚠️ attesté par le plan mais non lu en détail · ❌ absent ou perdu

---

## 1. Identification et volume

| Métrique | Valeur |
|---|---|
| Lignes / octets | 2 349 / 46 844 |
| Titres Markdown | 257 |
| Sections numérotées | **120** (de « 0 — Prédisposition d'intégration » à « 120 — Formule mentale à conserver ») |
| Équations display | **178** |
| Blocs de code | **0** |
| Marqueurs de référence | **0** |
| Occurrences « hypothèse » / « garantie » / « bornes » | **0** / 1 / **0** |
| Occurrences « erreur » / « précision » / « stabilité » | 48 / 39 / 27 |
| Occurrences « convergence » / « conditionnement » / « validation » | 25 / 15 / 3 |

Document deux fois plus court que K (2 349 lignes contre 4 316) mais **trois fois plus dense en
formalisme** : 178 équations contre 64. C'est le document le plus resserré du corpus étudié
jusqu'ici, et le seul dont la vocation déclarée soit la **fiabilité du calcul** plutôt que la
génération d'objets.

### État du formalisme avant / après restauration

| État | Blocs | Part |
|---|---:|---:|
| Défauts identifiés par lecture intégrale (avant) | **131** | — |
| Reconstruits et appliqués | **98** | 74,8 % |
| Corrections d'échappement appliquées | 4 | — |
| **Blocs encore dégradés** | **33** | **25,2 %** |

Les 33 blocs restants sont tous **vides** : leur contenu n'existe plus dans le fichier. Trente-trois
candidats argumentés sont soumis depuis le 2026-10-18 dans
`docs/restauration/propositions/domaine-L-blocs-a-trancher-suite.md`, en attente d'arbitrage.
Les numéros de ligne de ce fichier ont été **vérifiés contre le document restauré** : la
correspondance est exacte, bloc par bloc.

---

## 2. Objectif déclaré et couverture

Le document se présente comme une « référence complète pour transformer les mathématiques en
calculs fiables sur ordinateur ». Sa structure en 120 sections couvre sept blocs ✅ :

1. **Fondations et philosophie** (0–3) : prédisposition d'intégration, identité du domaine, place
   dans la cartographie, **principe fondamental « l'ordinateur calcule des approximations »** (3).
2. **Erreurs et arithmétique** (4–14) : erreur absolue et relative, cinq sources d'erreur (modèle,
   données, représentation, arrondi, troncature, algorithmique), **virgule flottante** (6),
   **précision finie** (7), **machine epsilon** (8), les cinq problèmes classiques (9 : addition
   d'échelles différentes, **soustraction catastrophique**, associativité non garantie, overflow,
   underflow), **stabilité / conditionnement / convergence** (10), conditionnement (11),
   convergence (12), **ordre de convergence** (13), **critères d'arrêt** (14).
3. **Résolution et algèbre linéaire** (15–31) : bissection, **Newton-Raphson**, sécante, méthodes
   hybrides, systèmes linéaires, élimination de Gauss, **LU**, pivotage, **Cholesky**, **QR**,
   systèmes creux, directs vs itératifs, **Jacobi**, **Gauss-Seidel**, **gradient conjugué**,
   préconditionnement.
4. **Approximation et intégration** (32–49) : interpolation, **Lagrange**, **Newton**,
   **phénomène de Runge**, **splines**, approximation, **moindres carrés**, régularisation,
   intégration numérique (rectangles, milieu, trapèzes, **Simpson**, **quadrature gaussienne**,
   adaptative), **différences finies** (avant / arrière / centrée), **ordre d'approximation**,
   **compromis discrétisation ↔ arrondi** (49).
5. **Équations différentielles et simulation** (50–62) : EDO et **Euler**, **Runge-Kutta**,
   **stabilité des méthodes d'EDO**, **EDP**, **éléments finis**, **volumes finis**,
   **méthodes spectrales**, **Monte-Carlo**, erreur Monte-Carlo, avantage Monte-Carlo,
   **réduction de variance**, application à la finance.
6. **Valeurs propres, optimisation, différenciation** (63–73) : valeurs et vecteurs propres,
   **méthode de la puissance**, **algorithme QR**, Newton pour l'optimisation,
   **différentiation automatique**, structure des méthodes itératives, **point fixe**,
   **accélération de convergence**, **multigrille**.
7. **Discipline de validation et applications** (74–120) : **analyse de l'erreur** (74),
   **résilience numérique** (75), **validation d'un calcul numérique** (76), test de convergence
   pratique (77), **analyse de sensibilité** (78), normalisation (79), complexité (80), dense vs
   creux (81), parallélisation (82), **précision mixte** (83), **calcul reproductible** (84),
   applications (85–97 : IA, deep learning, 2D/3D, jeux vidéo, **intégrateurs symplectiques**,
   robotique, finance, signal, cybersécurité, web, UI/UX, **génération procédurale**,
   **simulation de fluides**), architecture d'un solveur (98–100), **patterns de reconnaissance**
   (101), **distinction exact / approché / numérique** (102), **chaîne de conception en 10 étapes**
   (103), erreurs de conception à éviter (104), **critère de qualité** (105), méthodes adaptatives
   (106), temps réel (107), combinaisons avec les autres domaines (108), moteur de créativité
   (109), **questions à poser avant toute implémentation** (110), catalogue de 20 fiches
   deep-dive (111), 8 projets (112), challenges (113–114), synthèse (118–120).

⚠️ Les sections 111 à 116 (fiches deep-dive, projets, challenges, checklist) sont attestées par le
plan ; leur contenu n'a pas été lu ligne à ligne.

---

## 3. Ce qui est remarquablement aligné avec le projet

Le cahier des charges exige de distinguer **effet artistique**, **visualisation explicable** et
**simulation validée**, et interdit de présenter un effet d'inspiration fluide comme une simulation
de Navier–Stokes sans méthode, hypothèses et validation. Le document L fournit précisément
l'armature de cette exigence — quatre sections la portent à elles seules.

- **§76 — Validation d'un calcul numérique** ✅ : un protocole en six points, immédiatement
  transposable en critères d'acceptation produit : (1) **résidu** `r=Ax-b`, (2) erreur estimée
  comparée à une tolérance, (3) **conservation** des invariants physiques ou mathématiques,
  (4) **cas limites** (zéro, très grand, très petit, paramètres extrêmes), (5) **comparaison
  analytique** quand la solution exacte est connue, (6) **raffinement** (augmenter la précision ou
  diminuer le pas et vérifier la stabilité du résultat). La section ouvre sur un avertissement qui
  vaut pour tout composant du produit : *« Un résultat numérique ne doit pas être considéré comme
  fiable uniquement parce que le programme s'est exécuté sans erreur. »*
- **§103 — Chaîne de conception d'une solution numérique** ✅ : dix étapes, dont trois sont des
  points de contrôle explicites — étape 6 *Analyser* (« Convergence ? Stabilité ? Conditionnement ? »),
  étape 8 *Tester* (« cas connus et cas limites »), étape 9 *Valider* (« résidu, erreur,
  conservation, convergence »). C'est un squelette de revue de composant.
- **§102 — Distinction fondamentale : exact, approché, numérique** ✅ : trois blocs display
  intacts. Elle formule, dans le vocabulaire du corpus, la tripartition du cahier des charges — et
  ajoute la nuance utile : *« Une solution numérique peut être extrêmement précise sans être
  symboliquement exacte. »*
- **§104 — Erreurs de conception à éviter** ✅ : douze interdits, dont quatre concernent
  directement la présentation honnête d'un composant : *« confondre précision et stabilité »*,
  *« ignorer le conditionnement »*, *« utiliser une tolérance arbitraire »*, *« comparer uniquement
  les sorties sans comparer les résidus »*.

Deux formules de synthèse, intactes, méritent d'être retenues comme telles :

- **§120** — `\[ \text{erreur} = \text{conditionnement} \times \text{stabilité} \]` ✅
- **§118** — `\[ \text{un calcul juste peut produire un résultat faux} \]` ✅

---

## 4. Équations : état détaillé

Le document a été **restauré avant rédaction de cette fiche**, conformément à l'entrelacement
validé. Les équations ci-dessous sont donc, pour la plupart, lisibles dans le fichier source.

### ✅ Équations complètes et exploitables

| Notion | Formule (telle qu'écrite dans la source) | Ligne |
|---|---|---|
| Principe directeur | `\text{un résultat n'a de sens qu'avec son erreur}` | 61 |
| Erreur absolue | `E_a=\|x-\hat{x}\|.` | 168 |
| Erreur relative | `E_r=\frac{\|x-\hat{x}\|}{\|x|}.` | 186 |
| Erreur relative en % | `E_r(\%)=\frac{\|x-\hat{x}\|}{\|x\|}\times 100.` | 192 |
| Troncature (série de l'exponentielle) | `e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!}` vs `\approx \sum_{k=0}^{N}` | 222, 226 |
| Représentation flottante | `x=mb^e.` puis `x=m\,2^e.` | 238, 242 |
| **Machine epsilon** | `\varepsilon_{\text{mach}} \approx \beta^{-p}` | 271 |
| Associativité perdue | `(a+b)+c=a+(b+c).` / `\mathrm{fl}((a+b)+c)` ≠ `\mathrm{fl}(a+(b+c)).` | 305, 309, 313 |
| Triptyque fondamental | `\text{stabilité} \neq \text{conditionnement} \neq \text{convergence}` | 343 |
| **Ordre de convergence** | `e_{k+1}\leq C e_k^p,` avec `p=1.` (linéaire) et `p=2.` (quadratique) | 386, 392, 396 |
| Critères d'arrêt (trois formes) | `\|x_{k+1}-x_k\|<\varepsilon` · `\|F(x_k)\|<\varepsilon` · `<\varepsilon\max(1,\|x_k\|)` | 408, 412, 416 |
| Bissection | `f(a)f(b)<0.` · `m=\frac{a+b}{2}.` | 441, 449 |
| Sécante | `f'(x_n)\approx\frac{f(x_n)-f(x_{n-1})}{x_n-x_{n-1}}.` | 501 |
| Factorisations | `A=LU.` · `PA=LU.` · `A=LL^T.` · `A=QR` | 548, 569, 579, 587 |
| Gradient conjugué (forme quadratique) | `\min_x \frac{1}{2}x^TAx-b^Tx.` | 669 |
| Lagrange | `p(x)=\sum_{i=0}^{n} y_iL_i(x)` · `L_i(x)=\prod_{j\neq i}\frac{x-x_j}{x_i-x_j}.` | 701, 705 |
| Interpolation de Newton | forme par différences divisées | 711 |
| Moindres carrés | `\sum_i (y_i-f(x_i))^2.` · `\min_x\|Ax-b\|_2^2.` | 754, 758 |
| **Régularisation de Tikhonov** | `\min_x \|Ax-b\|_2^2+\lambda\|x\|_2^2.` | 774 |
| Quadrature | rectangles (792) · trapèzes (802) · **Simpson** (812) | 792, 802, 812 |
| **Différences finies** | avant `O(h)` · arrière `O(h)` · **centrée `O(h^2)`** | 845, 849, 853 |
| Ordres d'approximation | `O(h)` · `O(h^2)` · `O(h^4).` | 861, 865, 869 |
| Euler (EDO) | `y_{n+1} = y_n+ hf(t_n,y_n).` | 907 |
| Éléments finis | `K u=f.` | 966 |
| **Monte-Carlo** | `I=E[f(X)],` · `I_N = \frac{1}{N}\sum_{i=1}^{N}f(X_i).` · `O(1/\sqrt{N}).` | 991, 995, 1005 |
| Valeurs propres | `Av=\lambda v.` · puissance itérée `x_{k+1}=\frac{Ax_k}{\|Ax_k\|}.` | 1042, 1059 |
| Newton pour l'optimisation | `x_{k+1} = x_k- H_f(x_k)^{-1}\nabla f(x_k).` · `H\delta=-\nabla f` | 1091, 1099 |
| **Différentiation automatique** | `z=f(x)` · `y=g(z),` · `\frac{dy}{dx}=\frac{dy}{dz}\frac{dz}{dx}.` | 1132–1140 |
| Point fixe | `x_{k+1}=\varphi(x_k).` · `x^*=\varphi(x^*).` · `\|\varphi'(x^*)\|<1,` | 1152, 1156, 1168 |
| **Décomposition de l'erreur totale** | `E_{\text{total}}=E_{\text{modèle}}+E_{\text{données}}+E_{\text{arrondi}}+E_{\text{troncature}}+E_{\text{algorithme}}.` | 1201 |
| Résidu | `r=Ax-b.` | 1229 |
| Test de convergence pratique | `x_h,x_{h/2},x_{h/4}.` | 1260 |
| Complexité | `O(n^2)` dense vs `O(\mathrm{nnz}(A))` creux | 1323, 1329 |
| Apprentissage | `\min_{\theta}\mathcal{L}(\theta).` · `\theta_{t+1}=\theta_t-\eta\nabla\mathcal{L}.` | 1387, 1395 |
| Physique jeu vidéo (Euler) | `\frac{dv}{dt}=a.` · `v_{n+1}=v_n+ha_n` · `x_{n+1}=x_n+hv_n.` | 1457–1465 |
| Temps réel | `T_{\text{calcul}}<T_{\text{budget}}.` | 1787 |
| **Formule mentale** | `\text{erreur} = \text{conditionnement} \times \text{stabilité}` | 2333 |

### ❌ Les 33 blocs encore vides

Aucun résidu : le contenu n'existe plus dans le fichier. Répartition par section :

| Sections | Blocs | Lignes |
|---|---:|---|
| §0 prédisposition (3), §3 principe fondamental (2) | 5 | 13, 17, 55, 146, 158 |
| §5.1 erreur de modèle | 1 | 202 |
| §11 conditionnement | 1 | 351 |
| §35 phénomène de Runge | 1 | 721 |
| §43 trapèzes (forme composée) | 1 | 806 |
| §49 compromis discrétisation ↔ arrondi | 3 | 881, 885, 891 |
| §60 avantage Monte-Carlo | 1 | 1015 |
| §69 différenciation automatique | 1 | 1146 |
| §73 multigrille | 2 | 1191, 1195 |
| §78 analyse de sensibilité | 2 | 1274, 1278 |
| §83 précision mixte | 1 | 1357 |
| §105 critère de qualité | 1 | 1763 |
| **§108 combinaisons L+K, L+J, L+I, L+C, L+G, L+D, L+E/F** | **7** | 1805–1853 |
| §109 moteur de créativité | 3 | 1863, 1867, 1871 |
| §112 projet 5 (Monte-Carlo) | 1 | 2099 |
| §117 relations avec I et H | 2 | 2275, 2295 |

Le bloc le plus structurant est la série du **§108** : sept blocs, un par combinaison de domaines
(L+K, L+J, L+I, L+C, L+G, L+D, L+E/F), qui constituent la seule section du document consacrée aux
**synthèses inter-domaines** — précisément ce que le produit doit articuler.

---

## 5. Lacunes relevées

1. **Zéro occurrence du mot « hypothèse »** dans 2 349 lignes — comme dans le document K. Pour un
   domaine entièrement construit sur des conditions de validité (convergence, stabilité,
   régularité), c'est un manque structurant : les théorèmes sont énoncés sans leurs hypothèses.
2. **Zéro occurrence de « bornes »**, une seule de « garantie ». Le vocabulaire de l'encadrement
   d'erreur est absent, alors que la section 74 s'intitule « Analyse de l'erreur ».
3. **Zéro bloc de code et zéro pseudocode formaté**, y compris dans les sections d'architecture
   (98–100) et les huit projets d'apprentissage (112).
4. **Zéro marqueur de référence** : aucune source, aucune attribution, aucun renvoi bibliographique.
5. **La section 97 « Simulation de fluides » ne contient aucune équation** et ne nomme jamais
   Navier–Stokes — voir §7 ci-dessous, conséquence directe pour le produit.
6. **La section 105 « Critère de qualité d'un algorithme numérique » a son bloc vide** : la liste
   des critères (précision, stabilité, coût, robustesse, simplicité…) a disparu, privant le
   document de sa propre grille d'évaluation.
7. **Les huit projets d'apprentissage (112) ne portent que trois blocs display** sur 87 lignes
   (l. 2058, 2099 vide, 2124) : ce sont des énoncés, pas des cahiers des charges
   d'implémentation.

---

## 6. Fiabilité, cohérence, traçabilité

- **Cohérence interne :** excellente ✅. La progression est rigoureuse et sans rupture :
  erreur → flottant → stabilité → convergence → méthodes → applications → discipline de
  validation. Les distinctions (exact/approché/numérique, stabilité/conditionnement/convergence)
  sont posées puis tenues jusqu'à la synthèse finale.
- **Traçabilité :** nulle ❌. Aucun marqueur, aucune source, aucune attribution.
- **Fiabilité du formalisme :** **bonne depuis la restauration** ✅. 98 des 131 défauts ont été
  reconstruits ; les 98 l'ont été avec une confiance déclarée, une justification et un test de
  validation, et l'auteur les a validés lot par lot. Les 33 blocs restants sont vides, donc
  **muets** : ils ne risquent pas d'induire en erreur, ils laissent simplement un trou.
- **Réserve de méthode :** les restaurations sont des **reconstructions**, non des restitutions.
  Elles sont conformes au sens du document, mais la formulation exacte de l'auteur est perdue.
  Cette réserve vaut pour les 98 blocs restaurés.

---

## 7. Relations mathématiques ↔ usages visuels

| Bloc du document | Usage produit direct |
|---|---|
| Erreurs absolue/relative, machine epsilon, annulation catastrophique | Exigence transverse : **affichage honnête de la précision** d'un composant |
| Conditionnement, stabilité, ordre de convergence, critères d'arrêt | **Panneau de diagnostic** de tout composant itératif (famille 5) |
| Bissection, Newton, sécante | Famille 2 — recherche de racines, tracé de courbes implicites |
| LU, Cholesky, QR, gradient conjugué, préconditionnement | Socle des composants de **résolution** (famille 5), et de l'**ajustement de surfaces** (famille 2) |
| Interpolation, Lagrange, splines, phénomène de Runge | **Famille 2** — courbes et surfaces paramétriques ; le phénomène de Runge est un cas d'école de composant « expliqué » |
| Moindres carrés, régularisation de Tikhonov | **Ajustement de données** — familles 2 et 3 |
| Quadrature, Simpson, quadrature gaussienne, intégration adaptative | **Famille 5** — intégration de trajectoires, aires, quantités conservées |
| Différences finies, ordres `O(h)` / `O(h²)` | **Famille 5** — dérivation numérique, gradients de champs |
| Euler, Runge-Kutta, stabilité des EDO, **intégrateurs symplectiques** | **Famille 4** — particules, champs, forces, mouvement ; les symplectiques sont le bon choix pour les orbites à long terme |
| Monte-Carlo, réduction de variance, `O(1/\sqrt{N})` | **Famille 3** — éclairage, échantillonnage, bruit ; l'ordre `O(1/\sqrt{N})` donne un critère de convergence visuel |
| Éléments finis, volumes finis, méthodes spectrales | **Famille 5** — simulations, avec réserve (voir ci-dessous) |
| Précision mixte, dense vs creux, parallélisation, complexité | Moteur de recommandation technique (Phase 3) |
| §76 validation, §103 chaîne en 10 étapes, §104 interdits | **Critères d'acceptation** transverses du produit |

### ⚠️ Conséquence directe sur la famille 5 (simulations)

La section 97 « Applications en simulation de fluides » tient en **quinze lignes**, sans une seule
équation. Elle se contente d'énoncer que « les équations de fluides sont discrétisées sur une grille
ou un maillage » et d'énumérer sept effets visuels : fumée, eau, feu, vent, turbulence, effets
spéciaux, simulation scientifique.

Mesures faites sur le document restauré : **« Navier » : 0 occurrence · « CFL » : 0 · « shader » : 0**.

**Le corpus ne contient donc aucun élément permettant d'étayer une simulation de fluides.** Ni
équation, ni schéma de discrétisation, ni condition de stabilité, ni protocole de validation
spécifique. Toute composante de la famille 5 devra être construite sur des sources externes, et
c'est précisément le cas que le cahier des charges a anticipé en interdisant de présenter un effet
d'inspiration fluide comme une simulation de Navier–Stokes sans méthode, hypothèses et validation.
Le document L fournit la **discipline** qui permettrait de valider une telle composante (§76, §103,
§104) ; il ne fournit **aucun modèle** de fluide.

---

## 8. Index — premières lignes (L)

| Notion | Modèle | Équation | Paramètres | Algorithme | Moteur | Rendu | Composant potentiel | Tests / validation | Statut |
|---|---|---|---|---|---|---|---|---|---|
| **Machine epsilon** | borne de représentation | `\varepsilon_{\text{mach}}\approx\beta^{-p}` ✅ | base `β`, précision `p` | mesure directe | CPU | courbe d'erreur vs magnitude | *Explorateur de précision flottante* | écart à `2^{-52}` en double ; à `2^{-23}` en simple | ✅ complet |
| **Annulation catastrophique** | perte de chiffres significatifs | `x-y` ⚠️ (bloc court, §9.2) | valeurs proches | soustraction | CPU | comparaison simple vs double | *Démonstrateur d'annulation* | écart entre deux formulations algébriquement équivalentes | ⚠️ à confirmer |
| **Erreur absolue / relative** | métrique d'écart | `E_a=\|x-\hat{x}\|`, `E_r=E_a/\|x\|` ✅ | `x`, `x̂` | direct | CPU | jauge d'erreur | *Indicateur d'erreur intégré* | comparaison à une tolérance déclarée ; cas `x=0` | ✅ complet |
| **Ordre de convergence** | loi de décroissance | `e_{k+1}\leq Ce_k^p` ✅ | `p`, `C` | régression log-log | CPU | courbe d'erreur | *Mesureur d'ordre* | pente mesurée vs `p` théorique sur un cas connu | ✅ complet |
| **Bissection** | recherche de racine | `f(a)f(b)<0` ✅ | `[a,b]`, tolérance | dichotomie | CPU | tracé des intervalles | *Chercheur de racines* | nombre d'itérations prédit ; robustesse vs Newton | ✅ complet |
| **Newton-Raphson** | point fixe tangent | `x_{n+1}` ⚠️ (bloc court) | `x_0`, tolérance | itération tangente | CPU | tracé des tangentes | *Newton interactif* | convergence quadratique mesurée ; cas de divergence | ⚠️ à confirmer |
| **Gradient conjugué** | minimisation quadratique | `\min_x ½x^TAx-b^Tx` ✅ | `A` SPD, préconditionneur | Krylov | CPU (GPU possible) | courbe de convergence | *Solveur interactif* | résidu `r=Ax-b` ; nombre d'itérations vs `n` pour `A` bien conditionnée | ✅ complet |
| **Splines / Runge** | interpolation | Lagrange ✅, Newton ✅ | nœuds, degré | évaluation | CPU | courbe + nœuds | *Interpolateur interactif* | reproduction exacte des nœuds ; **oscillations de Runge** aux bords | ✅ complet |
| **Moindres carrés / Tikhonov** | ajustement | `\min_x\|Ax-b\|²+λ\|x\|²` ✅ | `λ` | solveur normal ou QR | CPU | courbe ajustée | *Ajusteur de données* | résidu ; stabilité selon `λ` ; conditionnement | ✅ complet |
| **Simpson / quadrature** | intégration | trapèzes ✅, Simpson ✅ | bornes, pas `h` | sommation | CPU | aire + erreur | *Intégrateur visuel* | ordre mesuré (`h²` vs `h⁴`) sur intégrale analytique connue | ✅ complet |
| **Différences finies** | dérivation | avant `O(h)`, centrée `O(h²)` ✅ | pas `h` | évaluation | CPU | comparaison des schémas | *Comparateur de schémas* | ordre observé ; **compromis `h→0` vs arrondi** (§49, blocs vides) | ✅ complet |
| **Euler / Runge-Kutta** | EDO | `y_{n+1}=y_n+hf(t_n,y_n)` ✅ | `h`, méthode | pas explicite | CPU | trajectoire | *Intégrateur d'EDO* | comparaison à la solution analytique ; **stabilité selon `h`** ; dérive d'énergie | ✅ complet |
| **Intégrateurs symplectiques** | géométrie | ❌ aucune équation | pas, système | leapfrog | CPU | orbite long terme | *Orbite préservée* | conservation de l'énergie sur 10⁵ pas ; comparaison Euler | ❌ à documenter |
| **Monte-Carlo** | estimation statistique | `I_N=(1/N)Σf(X_i)`, `O(1/\sqrt{N})` ✅ | `N`, graine | tirage | **GPU** | convergence de l'image | *Échantillonneur MC* | ordre `1/\sqrt{N}` mesuré ; **reproductibilité par graine** | ✅ complet |
| **Valeurs propres** | spectre | `Av=\lambda v`, puissance itérée ✅ | tolérance, `k` | itération | CPU | convergence du rapport | *Spectre interactif* | résidu `\|Av-\lambda v\|` ; séparation des valeurs propres | ✅ complet |
| **Différentiation automatique** | composition de dérivées | `dy/dx=(dy/dz)(dz/dx)` ✅ | graphe | forward / reverse | CPU | graphe annoté | *Graphe de dérivation* | comparaison aux différences finies ; exactitude machine | ✅ complet |
| **Simulation de fluides** | — | ❌ **aucune équation** | — | — | — | fumée, eau, feu | *Famille 5 — à construire hors corpus* | §76 s'applique, mais aucun modèle n'est fourni | ❌ hors corpus |

---

## 9. Niveau de maturité

| Dimension | Évaluation | Justification |
|---|---|---|
| Conceptuelle | **Élevée** | 120 sections, progression rigoureuse, distinctions tenues de bout en bout |
| Pédagogique | **Élevée** | 20 fiches deep-dive, 8 projets, challenges avec et sans IA, checklist de maîtrise, formule mentale |
| Formelle | **Moyenne à élevée** | 178 équations ; 74,8 % des défauts reconstruits, les 33 restants étant vides et non trompeurs |
| Exécutable | **Nulle** | 0 bloc de code, 0 pseudocode formaté |
| Validation | **Moyenne** | la discipline est énoncée avec précision (§76, §103, §104) mais peu appliquée : 3 occurrences de « validation », aucune d'« hypothèse » |

---

## 10. Besoins de documentation complémentaire

1. **Trancher les 33 blocs restants**, en priorité la série du §108 (sept blocs, seules synthèses
   inter-domaines du document) et le §105 (critère de qualité).
2. **Ajouter les hypothèses et conditions de validité** de chaque résultat — zéro occurrence du mot
   dans 2 349 lignes. C'est le manque le plus coûteux pour le produit, qui devra publier des
   conditions d'usage par composant.
3. **Documenter les intégrateurs symplectiques** (§89) : la section affirme leurs propriétés sans
   donner une seule équation, alors que c'est le choix pertinent pour les orbites et les animations
   à long terme de la famille 4.
4. **Traiter la simulation de fluides comme un chantier externe** : le corpus ne fournit ni modèle,
   ni schéma, ni condition de stabilité. Toute composante de la famille 5 devra être sourcée hors
   corpus et validée avec la discipline du §76.
5. **Traduire l'architecture des solveurs (§98–100) et les huit projets (§112) en pseudocode
   exécutable** — travail que le produit devra produire de toute façon.
6. **Rattacher chaque méthode à une référence** : aucune source, aucune attribution dans le document.
