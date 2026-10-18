# LOT 4b — DOMAINE N : TRANSFORMÉES (sections 65 à 178)

**Date :** 2026-10-18 · **Statut :** propositions soumises, non appliquées
**Document :** `DOCUMENT N — TRANSFORMÉES.md`
**Portée :** lignes 1 309 à 3 940. Complété par le **lot 4a** (lignes 75 à 1 301).
**Complément :** les blocs à arbitrer sont repris dans `domaine-N-blocs-a-trancher.md`.

---

## 1. La découverte du lot : un tableau intact au §164

Le **tableau de synthèse du §164** (lignes 3 254 à 3 265) n'est pas un bloc d'affichage : c'est un
tableau Markdown, et **il a survécu intact**. Il donne, pour chaque outil, son entrée, sa sortie et
sa question principale :

| Outil | Entrée | Sortie |
|---|---|---|
| Fourier | fonction | spectre |
| Laplace | fonction temporelle | F(s) |
| Z | séquence | X(z) |
| STFT | signal | temps-fréquence |
| DWT | signal | échelles/détails |
| DCT | données | coefficients cosinus |

Ce tableau est la clé des deux sections les plus vides du document : **les fiches de
reconnaissance** (§157 à §162, six blocs vides) et **la formule fondamentale** (§178, six blocs
vides). Les candidats proposés pour ces douze blocs en sont tirés **mot pour mot**.

C'est un cas de figure nouveau dans le chantier : jusqu'ici, les blocs non restituables l'étaient
parce que leur contenu n'existait nulle part. Ici, **le document contenait sa propre réponse**, à
cinq cents lignes de distance. La leçon est générale : avant de déclarer un bloc irrécupérable, il
faut chercher s'il existe un **tableau, une liste ou un arbre ASCII** qui dit la même chose.

## 2. Deux autres structures qui ont survécu

| Structure | Ligne | Apport |
|---|---|---|
| Arbre ASCII du §163 | 3 240 à 3 248 | Fourier → continu/discret → DFT → FFT : dit ce qu'il ne faut pas confondre |
| **FORMULE MENTALE du domaine N** | 3 941 à 3 945 | **intacte** — six verbes qui donnent les six blocs vides de la §179 |

La FORMULE MENTALE énonce :

> Transformer pour voir. Voir pour comprendre. Comprendre pour simplifier. Simplifier pour
> calculer. Calculer pour construire.

Les six blocs vides des lignes 3 898 à 3 908 sont précédés de « C'est ce qui permet de passer : ».
Les six candidats sont donc ces six verbes, dans cet ordre. **C'est la première fois qu'un bloc
vide trouve une source aussi directe**, et cela confirme l'hypothèse posée sur les documents I et
L : ces sections de synthèse contenaient des chaînes de mots, et les mots existent parfois
ailleurs dans le document.

## 3. Le `\pi` encore et toujours

Trois occurrences supplémentaires (l. 2 537, 3 530, 2 046) confirment la règle du lot 4a : le `\pi`
est détruit sans laisser de trace, y compris dans `O(N\log N)` dont le résidu `O(NN)` est devenu
la signature de reconnaissance du document.

## 4. Corps technique

**Correctif :** `domaine-N-lot4b.patch.json` — 104 entrées : 52 haute, 32 moyenne, 20 inconnue — **84 applicables**

### Confiance haute (52)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 1309 | `\[ z(t)=x(t)+i{x(t)} \]` | `\[ z(t)=x(t)+i\mathcal{H}\{x(t)\} \]` | Rendu : z(t)=x(t)+i𝓗{x(t)}. |
| 1350 | `\[ x ax \]` | `\[ x\to ax \]` | Rendu : x → ax (changement d'échelle). |
| 1389 | `\[ x=\_k c_k_k \]` | `\[ x=\sum_k c_k\phi_k \]` | Rendu : x=Σ c_k φ_k. |
| 1409 | `\[ x^N \]` | `\[ x\in\mathbb{R}^{N} \]` | Rendu : x ∈ ℝ^N. |
| 1417 | `\[ T^{NN} \]` | `\[ T\in\mathbb{R}^{N\times N} \]` | Rendu : T ∈ ℝ^{N×N}. |
| 1427 | `\[ {\_k} \]` | `\[ \{\phi_k\} \]` | Rendu : {φ_k}. |
| 1431 | `\[ \_i,_j =_ {ij} \]` | `\[ \langle\phi_i,\phi_j\rangle=\delta_{ij} \]` | Rendu : ⟨φ_i,φ_j⟩=δ_ij. |
| 1449 | `\[ x T(x) \]` | `\[ x\to T(x) \]` | Rendu : x → T(x). |
| 1469 | `\[ c_i’= ⏎  ⏎ \]` | `\[ c_i'=\begin{cases}c_i&\text{si }\|c_i\|>\lambda\\ 0&\text{s` | Seuillage dur. Le seuil λ n'est pas nommé dans la section : proposé par cohérence. |
| 1485 | `\[ S_(x) = x,\_{\|x\|} \]` | `\[ S_\lambda(x)=x\cdot\mathbf{1}_{\|x\|>\lambda} \]` | Rendu : S_λ(x)=x·1_{\|x\|>λ}. Définition standard du seuillage dur. |
| 1489 | `\[ S_(x) = (x) (\|x\|-,0) \]` | `\[ S_\lambda(x)=\mathrm{sign}(x)\max(\|x\|-\lambda,0) \]` | Rendu : S_λ(x)=sign(x)·max(\|x\|−λ,0). Définition standard du seuillage doux. |
| 1505 | `\[ mn \]` | `\[ m\ll n \]` | Rendu : m ≪ n. |
| 1527 | `\[ z=f_(x) \]` | `\[ z=f_\theta(x) \]` | Rendu : z=f_θ(x). |
| 1533 | `\[ z=f_(T(x)) \]` | `\[ z=f_\theta(T(x)) \]` | Rendu : z=f_θ(T(x)). |
| 1720 | `\[ N(x) = \_{k=0}^{K} a_kN_k(x) \]` | `\[ N(x)=\sum_{k=0}^{K}a_kN_k(x) \]` | Rendu : N(x)=Σ_{k=0}^{K} a_k N_k(x). |
| 1795 | `\[ H(i) \]` | `\[ H(i\omega) \]` | Rendu : H(iω). |
| 1801 | `\[ 20_{10}\|H(i)\| \]` | `\[ 20\log_{10}\|H(i\omega)\| \]` | Rendu : 20 log₁₀\|H(iω)\| — le gain en décibels. |
| 1805 | `\[ H(i) \]` | `\[ \arg(H(i\omega)) \]` | Rendu : arg(H(iω)). |
| 1926 | `\[ e^{-it_0} \]` | `\[ e^{-i\omega t_0} \]` | Rendu : e^{-iωt₀}. |
| 1932 | `\[ \_g() = - \]` | `\[ \tau_g(\omega)=-\frac{d\varphi}{d\omega} \]` | Rendu : τ_g(ω)=−dφ/dω. Définition du retard de groupe. |
| 1955 | `\[ x X x \]` | `\[ x\to X\to x \]` | Rendu : x → X → x. |
| 1973 | `\[ xy \]` | `\[ x\to y \]` | Rendu : x → y (problème direct). |
| 1977 | `\[ yx \]` | `\[ y\to x \]` | Rendu : y → x (problème inverse). |
| 1987 | `\[ X= \]` | `\[ X=H^{-1}Y \]` | Rendu : X=H^{-1}Y. |
| 1993 | `\[ \|H\| \]` | `\[ \|H\|\approx 0 \]` | Rendu : \|H\|≈0. |
| 2046 | `\[ O(NN) \]` | `\[ O(N\log N) \]` | Rendu : O(N log N). |
| 2060 | `\[ (x\*h) = (x)(h) \]` | `\[ \mathcal{F}\{x\ast h\}=\mathcal{F}\{x\}\cdot\mathcal{F}\{h\` | Rendu : 𝓕{x∗h}=𝓕{x}·𝓕{h}. |
| 2109 | `\[ T_{} < T_{} \]` | `\[ T_{\text{calcul}}<T_{\text{disponible}} \]` | Rendu : T_calcul < T_disponible. |
| 2251 | `\[ T_1,T_2,,T_k \]` | `\[ T_1,T_2,\ldots,T_k \]` | Rendu : T₁,T₂,…,T_k. |
| 2265 | `\[ T^ = \_T (T,x) \]` | `\[ \hat{T}=\arg\max_T \mathrm{score}(T,x) \]` | Rendu : T̂=argmax_T score(T,x). |
| 2280 | `\[ T_ \]` | `\[ T_\theta \]` | Rendu : T_θ. |
| 2286 | `\[ ^ = _L(T_(x),y) \]` | `\[ \hat{\theta}=\arg\min_\theta L(T_\theta(x),y) \]` | Rendu : θ̂=argmin_θ L(T_θ(x),y). |
| 2537 | `\[ x\[n\]=(2f n/f_s) \]` | `\[ x[n]=\sin(2\pi fn/f_s) \]` | Rendu : x[n]=sin(2πfn/f_s). |
| 2557 | `\[ x T(x) T^{-1}(T(x)) \]` | `\[ x\to T(x)\to T^{-1}(T(x)) \]` | Rendu : x → T(x) → T^{-1}(T(x)). |
| 2561 | `\[ \|x-T^{-1}(T(x))\| \]` | `\[ \\|x-T^{-1}(T(x))\\| \]` | Rendu : ‖x−T^{-1}(T(x))‖. |
| 2589 | `\[ X\[N-k\] = \]` | `\[ X[N-k]=\overline{X[k]} \]` | Rendu : X[N−k]=conj(X[k]). Propriété de symétrie pour signal réel. |
| 2639 | `\[ c Q(c) \]` | `\[ c\to Q(c) \]` | Rendu : c → Q(c). |
| 2653 | `\[ x T(x) Q C \]` | `\[ x\to T(x)\to Q\to C \]` | Rendu : x → T(x) → Q → C. |
| 2663 | `\[ C Q^{-1} T^{-1} \]` | `\[ \hat{x}=T^{-1}(Q^{-1}(C)) \]` | Rendu : x̂=T^{-1}(Q^{-1}(C)). |
| 2667 | `\[ x \]` | `\[ \hat{x} \]` | Rendu : x̂. |
| 2675 | `\[ =x \]` | `\[ \hat{x}=x \]` | Rendu : x̂=x. |
| 2747 | `\[ \_X(t) = \[e^{itX}\] \]` | `\[ \varphi_X(t)=\mathbb{E}\left[e^{itX}\right] \]` | Rendu : φ_X(t)=𝔼[e^{itX}]. |
| 2774 | `\[ x:V \]` | `\[ x:V\to\mathbb{R} \]` | Rendu : x : V → ℝ. |
| 2814 | `\[ x T(x) z T^{-1}() \]` | `\[ x\to T(x)\to z\to T^{-1}(z) \]` | Rendu : x → T(x) → z → T^{-1}(z). |
| 2851 | `\[ x T(x) T^{-1} x’ \]` | `\[ x\to T(x)\to T^{-1}\to x' \]` | Rendu : x → T(x) → T^{-1} → x'. |
| 2872 | `\[ x_0,x_1,,x_N \]` | `\[ x_0,x_1,\ldots,x_N \]` | Rendu : x₀,x₁,…,x_N. |
| 2922 | `\[ (x) = d(T(x),) \]` | `\[ s(x)=d(T(x),\mu) \]` | Rendu : s(x)=d(T(x),μ). |
| 3068 | `\[ T^{-1}(T(x))x \]` | `\[ T^{-1}(T(x))\approx x \]` | Rendu : T^{-1}(T(x))≈x. |
| 3438 | `\[ X(f) H(f) Y(f) \]` | `\[ X(f)\to H(f)\to Y(f) \]` | Rendu : X(f) → H(f) → Y(f). |
| 3470 | `\[ x DWT Threshold IDWT \]` | `\[ x\to \text{DWT}\to \text{seuil}\to \text{IDWT} \]` | Rendu : x → DWT → seuil → IDWT. |
| 3530 | `\[ O(NN) \]` | `\[ O(N\log N) \]` | Rendu : O(N log N). |
| 3600 | `\[ T^ \]` | `\[ \hat{T} \]` | Rendu : T̂. |

### Confiance moyenne (32)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 1453 | `\[ T(x) ⏎  ⏎ \]` | `\[ T(x)=(c_1,\ldots,c_n) ⏎ \text{avec la plupart des } c_i\app` | Le candidat traduit la phrase qui précède (« un grand nombre de coefficients proches de zéro »). Formulation à confirmer. |
| 2301 | `\[ \]` | `\[ \nabla_\theta L \]` | Candidat alternatif : \[ \frac{\partial L}{\partial\theta} \]. |
| 2383 | `\[ \]` | `\[ \text{Fourier} \]` | Candidat fondé sur le tableau du §164. Alternative : \text{DFT} si le signal est échantillonné. |
| 2391 | `\[ \]` | `\[ \text{Laplace} \]` | Candidat fondé sur le §32 et le tableau du §164. |
| 2399 | `\[ \]` | `\[ \text{transformée en Z} \]` | Candidat fondé sur les fiches §159 et le tableau du §164. |
| 2407 | `\[ \]` | `\[ \text{STFT} \]` | Candidat fondé sur la fiche §160 et le tableau du §164. |
| 2415 | `\[ \]` | `\[ \text{ondelettes} \]` | Candidat fondé sur la fiche §161 et le tableau du §164 (DWT : échelles/détails). |
| 2423 | `\[ \]` | `\[ \text{DCT} \]` | Candidat fondé sur la fiche §162 et le tableau du §164 (DCT : concentration d'énergie). |
| 3140 | `\[ \]` | `\[ \text{transformée de Fourier} \]` | Candidat fondé sur le titre de la fiche et le tableau du §164. |
| 3154 | `\[ \]` | `\[ \text{FFT} \]` | Candidat fondé sur le titre de la fiche. |
| 3169 | `\[ \]` | `\[ \text{Laplace} \]` | Candidat fondé sur le titre de la fiche. |
| 3183 | `\[ \]` | `\[ \text{transformée en Z} \]` | Candidat fondé sur le titre de la fiche. |
| 3197 | `\[ \]` | `\[ \text{STFT} \]` | Candidat fondé sur le titre de la fiche. |
| 3212 | `\[ \]` | `\[ \text{ondelettes} \]` | Candidat fondé sur le titre de la fiche. |
| 3225 | `\[ \]` | `\[ \text{DCT} \]` | Candidat fondé sur le titre de la fiche. |
| 3231 | `\[ \]` | `\[ \text{la DFT et la FFT} \]` | Candidat fondé sur l'arbre ASCII qui suit le bloc, lequel est intact. |
| 3248 | `\[ \]` | `\[ \text{la transformée de Fourier et la DFT} \]` | Candidat fondé sur la phrase elle-même et l'arbre du §163. |
| 3858 | `\[ \]` | `\[ \text{changer de représentation pour simplifier le problème` | Candidat fondé sur le §176, dont la phrase-clé est intacte. |
| 3862 | `\[ \]` | `\[ \text{une fonction en spectre} \]` | Candidat fondé mot pour mot sur le tableau intact du §164. |
| 3866 | `\[ \]` | `\[ \text{une fonction temporelle en F(s)} \]` | Candidat fondé mot pour mot sur le tableau du §164. |
| 3870 | `\[ \]` | `\[ \text{une séquence en X(z)} \]` | Candidat fondé mot pour mot sur le tableau du §164. |
| 3874 | `\[ \]` | `\[ \text{un signal en représentation temps-fréquence} \]` | Candidat fondé mot pour mot sur le tableau du §164. |
| 3878 | `\[ \]` | `\[ \text{un signal en échelles et détails} \]` | Candidat fondé mot pour mot sur le tableau du §164. |
| 3882 | `\[ \]` | `\[ \text{des données en coefficients cosinus} \]` | Candidat fondé mot pour mot sur le tableau du §164. |
| 3898 | `\[ \]` | `\[ \text{transformer} \]` | Candidat fondé sur la FORMULE MENTALE intacte du document, qui fournit les six termes dans l'ordre. |
| 3900 | `\[ \]` | `\[ \text{voir} \]` | Voir l. 3898. |
| 3902 | `\[ \]` | `\[ \text{comprendre} \]` | Voir l. 3898. |
| 3904 | `\[ \]` | `\[ \text{simplifier} \]` | Voir l. 3898. |
| 3906 | `\[ \]` | `\[ \text{calculer} \]` | Voir l. 3898. |
| 3908 | `\[ \]` | `\[ \text{construire} \]` | Voir l. 3898. |
| 3935 | `\[ \]` | `\[ \text{chercher la représentation qui simplifie} \]` | Candidat fondé sur la phrase intacte du §176. |
| 3939 | `\[ \]` | `\[ \text{vérifier les hypothèses et les limites} \]` | Candidat. Alternative : \[ \text{ne pas oublier le coût de calcul} \]. |

### Confiance inconnue — décision requise (20)

| Ligne | Bloc actuel | Ce que le bloc contenait |
|---:|---|---|
| 1694 | `\[ \]` | §85 « On cherche souvent : [vide] tout en conservant une qualité acceptable. » |
| 1817 | `\[ \]` | §92 détection de motifs « On peut donc rechercher : [vide] comme indicateur de : ». |
| 2005 | `\[ \]` | §101 régularisation « Par exemple, au lieu de : [vide] on peut utiliser une forme régularisée. » |
| 2011 | `\[ \]` | §101 « L'idée générale : [vide] Cette idée fait directement le lien avec le domaine L — Analyse numérique. » |
| 2032 | `\[ ⏎  ⏎ - \]` | §102 « Une FFT théorique parfaite n'existe pas comme opération abstraite dans une machine. Elle est exécutée avec : [trois lignes, dont une puce -] ». Le bloc c |
| 2052 | `\[ \]` | §103 « Cette différence est un excellent exemple de passage : [vide] ». |
| 2173 | `\[ \]` | §110 UX visuelle « Une donnée sonore peut devenir une expérience visuelle : [vide] Exemples : ». |
| 2307 | `\[ ⏎  ⏎ - \]` | §115 « Cela permet de construire des architectures combinant : [trois lignes, dont une puce -] ». Le bloc contenait une liste d'au moins deux items. |
| 2601 | `\[ \]` | §127 mémoire « Il faut distinguer : [vide] et : [vide] Une représentation complexe peut nécessiter davantage de mémoire qu'une représentation réelle. » |
| 2605 | `\[ \]` | §127, pendant du bloc précédent. |
| 2647 | `\[ \]` | §129 « Le compromis devient : [vide] ». |
| 2699 | `\[ \]` | §133 lien avec la théorie de l'information « On peut donc avoir : [vide] ». |
| 2780 | `\[ \]` | §137 « On peut alors construire des analogues de Fourier sur les graphes à partir des vecteurs propres du Laplacien du graphe. Cela mène à la : [vide] avec des  |
| 2824 | `\[ \]` | §140 modèles de diffusion « Même l'… [vide] reste profondément similaire. » — la phrase elle-même est tronquée dans le document. |
| 2914 | `\[ \]` | §146 détection d'anomalies « Exemple : [vide] puis : [vide] On peut alors construire : [s(x)=d(T(x),μ)] ». |
| 2918 | `\[ \]` | §146, pendant du bloc précédent. |
| 3426 | `\[ \]` | PROJET 2 — Spectrogramme « Construire : [vide] et permettre de modifier : - taille de fenêtre ; - hop size ; - fréquence d'échantillonnage. » |
| 3610 | `\[ \]` | §170 expérience créative audio → monde visuel « Construire : [vide] Le système pourrait contrôler : ». |
| 3720 | `\[ \]` | §173 « ### Niveau 7 — Création / Construire de nouvelles applications à partir du principe : [vide] ». |
| 3794 | `\[ \]` | §176 SYNTHÈSE DES GRANDES TRANSFORMÉES : un bloc unique et vide, sans phrase d'introduction. Le tableau du §164 en donne la matière. |

