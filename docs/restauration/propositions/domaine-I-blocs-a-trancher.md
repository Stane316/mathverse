# DOMAINE I — LES 26 BLOCS À TRANCHER

**Date :** 2026-10-18 · **Statut :** candidats soumis, non appliqués
**Protocole validé :** une réponse par document — « lot accepté », « lot accepté sauf les lignes
X, Y », ou votre texte pour certaines lignes.

---

## 1. Comment répondre

Une seule réponse clôt le document I. Sûreté : **[proposé]** = lecture raisonnable, à confirmer ;
**[faible]** = hypothèse de départ, à remplacer sans scrupule.

Pour tout bloc que vous ne retrouvez pas : **le repli « contenu perdu » est une issue valide**,
validée par vous le 2026-10-18. Le bloc reste vide, il est inscrit au registre, et il n'est pas
compté comme restauré.

## 2. Les blocs

| Ligne | Section | Candidat proposé | Sûreté |
|---:|---|---|---|
| **1284** | §74 | `\[ x_{k+1}=x_k-\eta\nabla f(x_k) \]` | proposé |
| **1536** | §89 | `\nabla_\theta J=J_{f_L}\cdots J_{f_1} (produit de Jacobiennes)` | proposé |
| **1693** | §102 TENSEURS | `\text{différencier chaque opération élémentaire}` | proposé |
| **1933** | §116 | `\text{le gradient permet de remonter à l'optimum}` | proposé |
| **1991** | §121 | `\text{un minimum global}` | proposé |
| **2124** | §130 CHECKPOINTING | `\text{de la mémoire contre du calcul}` | proposé |
| **2838** | §171 CE QU'IL FAUT ABSOLUMENT RETENIR, premier des quatre blocs ( | `dérivée — la dérivée, puis le gradient, puis la règle de chaîne, puis l'optimisation — les quatre piliers du document` | proposé |
| **2842** | §171, deuxième bloc ( | `gradient` | proposé |
| **2846** | §171, troisième bloc ( | `règle de chaîne` | proposé |
| **2850** | §171, quatrième bloc ( | `optimisation` | proposé |
| **2958** | §174 | `\frac{\partial L}{\partial\theta}=\frac{\partial L}{\partial a}\cdot\frac{\partial a}{\partial z}\cdot\frac{\partial z}{\partial\theta}` | proposé |
| **3016** | §176 Niveau 1 | `\[ f'(x) \] — l'objet du niveau 1 est la dérivée` | proposé |
| **3020** | §176 Niveau 2 | `\[ \min_x f(x) \] — l'objet du niveau 2 est la minimisation` | proposé |
| **3024** | §176 Niveau 3 | `\[ \min_\theta J(\theta) \] — l'objet du niveau 3 est la minimisation du risque empirique` | proposé |
| **3056** | §178 Probabilités. Bloc vide, aucun résidu | `\[ p_\theta(x) \] — cf. §115` | proposé |
| **3060** | §178 Statistiques. Bloc vide, aucun résidu | `\[ \theta^{*}=\arg\max_\theta \mathcal{L}(\theta) \] — cf. §116` | proposé |
| **3064** | §178 Calcul différentiel. Bloc vide, aucun résidu | `\[ \nabla_\theta J(\theta) \] — cf. §73` | proposé |
| **3068** | §178 En Machine Learning. Bloc vide, aucun résidu | `\[ \theta_{t+1}=\theta_t-\eta\nabla_\theta J(\theta_t) \] — cf. §123 et §173` | proposé |
| **3117** | §180 | `\[ \text{mesurer la variation locale} \] — reprend le paragraphe de conclusion, qui parle de « mesurer comment un système change localement »` | proposé |
| **3141** | §180 | `\[ L\to\nabla_\theta L \] (la perte vers le gradient par backpropagation)` | proposé |
| **3145** | §180 | `\[ J(\theta)\to\theta_{t+1}=\theta_t-\eta\nabla_\theta J(\theta_t) \]` | proposé |
| **3149** | §180 | `\[ x(t)\to\dot{x}=f(x,t) \], en écho au §110` | proposé |
| **3153** | §180 | `\[ F(x,y,z)\to\nabla F \], la normale d'une surface implicite (§109)` | proposé |
| **3161** | §180 | `\text{les fonctions et leur optimisation}` | proposé |
| **3165** | §180 | `\text{l'apprentissage automatique}` | proposé |
| **3175** | FIN DU DOCUMENT « **Noyau absolument fondamental :** [vide] | `\[ f\to f'\to\nabla\to H \] — la chaîne qui résume tout le document` | proposé |

## 3. Ce que ces blocs ont en commun

**Vingt-deux des vingt-six blocs appartiennent aux sections de synthèse** (§171 à §180). Ce n'est
pas un hasard, et cela confirme l'hypothèse formulée sur le document L : la dégradation frappe
systématiquement ces sections parce qu'elles contenaient des **chaînes de mots** — « dérivée →
gradient → chaîne → optimisation » — et non des équations. Une chaîne de mots ne laisse aucun
résidu exploitable ; une équation en laisse toujours un.

Conséquence méthodologique, à retenir pour les vingt-six documents restants : **les sections de
synthèse sont les moins restaurables du corpus.** Leur contenu dépendra toujours de vous, jamais
de la reconstruction.

## 4. Le cas de la §180 en particulier

Les quatre blocs vides de la synthèse finale (l. 3 141, 3 145, 3 149, 3 153) suivent un motif
parfaitement régulier — « Pour X : [objet → objet] » — dont cinq occurrences **ont survécu**. Les
candidats proposés en découlent directement :

| Section | Survivant (modèle) | Candidat pour le bloc vide |
|---|---|---|
| Pour les réseaux neuronaux | `f(x) → ∇f(x)` | `L → ∇_θ L` |
| Pour le Machine Learning | `f(x) → x − η∇f(x)` | `J(θ) → θ_{t+1}=θ_t−η∇_θ J(θ_t)` |
| Pour la simulation | — | `x(t) → ẋ=f(x,t)` (écho au §110) |
| Pour la computer graphics | — | `F(x,y,z) → ∇F` (la normale, §109) |

Ce sont des **propositions**, pas des restitutions : le motif donne la forme, pas le contenu.
