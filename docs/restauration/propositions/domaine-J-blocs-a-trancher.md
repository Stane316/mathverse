# DOMAINE J — BLOCS À TRANCHER

**Date :** 2026-10-18 · **Statut :** candidats soumis, **non appliqués**
**Lots concernés :** `domaine-J-lot5a` (13) + `domaine-J-lot5b` (43) = **56 blocs**
**Protocole validé :** une réponse par lot — « lot accepté », « lot accepté sauf les
lignes X, Y », ou votre texte pour certaines lignes. Repli « contenu perdu » accepté.

---

## 1. Réglé : la Grande Carte (§155)

Les dix blocs vides des lignes 3386 à 3404 ont été **tranchés par l'auteur le
2026-10-18** : l'hypothèse A→…→J est retenue. Ils sont passés du statut « inconnue »
au lot **`domaine-J-lot5c`**, en confiance moyenne — l'hypothèse d'ensemble est
validée, son encodage bloc par bloc reste une reconstruction puisque chaque résidu est
vide. Voir `domaine-J-lot5c.md`.

## 2. Trois familles de blocs

- **Chaînes de mots** — le bloc contenait un libellé, pas une formule. Le document écrit
  ce type de réponse en blocs display : le §144 en fournit quatre intacts
  (`\[ learning\ rate \]`, `\[ batch\ size \]`, `\[ weight\ decay \]`, `\[ architecture \]`).
  C'est la majorité des inconnues, et les plus sûres à trancher vous appartiennent.
- **Blocs techniques** — le contenu était mathématique mais sous-déterminé (§63, §77,
  §78, §92, §105, §126, §147…). Le candidat est argumenté dans la colonne de droite.
- **Schémas** — §56, §95, §109 : le bloc contenait probablement un schéma ASCII, dont
  le §122 montre que le document sait les produire.

## 3. Réserve sur le lot 5a

La ligne **473** (`0x` → `0\leq x\leq 1`) est proposée en haute dans le lot 5a. Le même
motif apparaît en l. 1896, classée moyenne : le résidu ne montre que le `0` et la
variable, sans le second `\leq` ni le `1` final. La reconstruction reste la seule
sémantiquement correcte, mais elle ne découle pas du résidu. À confirmer.

---

## 4. Les 56 blocs restants

| Ligne | Lot | § | Section | Candidat / ce que le bloc contenait |
|---:|:--:|---:|---|---|
| 17 | 5a | 0 | IDENTITÉ DU DOMAINE | Candidats : \[ \text{un objectif} \] puis \[ \text{des contraintes} \] — les deux piliers nommés partout dans le document. |
| 21 | 5a | 0 | IDENTITÉ DU DOMAINE | Voir l. 17. |
| 45 | 5a | 1 | PLACE DE L’OPTIMISATION DANS LA CARTO… | Voir l. 41. |
| 47 | 5a | 1 | PLACE DE L’OPTIMISATION DANS LA CARTO… | Voir l. 41. |
| 49 | 5a | 1 | PLACE DE L’OPTIMISATION DANS LA CARTO… | Voir l. 41. |
| 51 | 5a | 1 | PLACE DE L’OPTIMISATION DANS LA CARTO… | Voir l. 41. |
| 53 | 5a | 1 | PLACE DE L’OPTIMISATION DANS LA CARTO… | Voir l. 41. |
| 81 | 5a | 2 | POURQUOI L’OPTIMISATION EST CENTRALE … | Candidat : \[ \sum_{i,j} c_{ij}x_{ij} \] — les coûts de transport. La puce conservée montre au moins deux items. |
| 89 | 5a | 2 | POURQUOI L’OPTIMISATION EST CENTRALE … | Candidats : \[ \text{le temps total} \] puis \[ \text{le retard} \] — cf. §79 (l. 1560) qui parle du temps de fin global. |
| 93 | 5a | 2 | POURQUOI L’OPTIMISATION EST CENTRALE … | Voir l. 89. |
| 403 | 5a | 11 | PROBLÈMES CONVEXES ET NON CONVEXES | Candidat : \[ \text{plusieurs minima locaux} \] et \[ \text{des points selles} \] — cf. §6.3 et §91 du domaine I. |
| 618 | 5a | 21 | ALGORITHME DU SIMPLEXE | Candidat : \[ \text{de sommet en sommet} \]. |
| 922 | 5a | 41 | INTERPRÉTATION DE NEWTON | Candidat : \[ \nabla f \] et \[ \nabla^{2}f \] — Newton utilise le gradient ET la Hessienne. |
| 1116 | 5b | 51 | BATCH ET BRUIT DU GRADIENT | Candidats : \[ \text{bruit du gradient} \] et \[ \text{coût computationnel} \] — les deux items de tête de la liste (l. 1108-1109). |
| 1120 | 5b | 51 | BATCH ET BRUIT DU GRADIENT | Voir l. 1116. |
| 1194 | 5b | 56 | ALGORITHMES GÉNÉTIQUES | Candidat : \[ \text{sélection}\to\text{croisement}\to\text{mutation} \]. |
| 1265 | 5b | 61 | OPTIMISATION BAYÉSIENNE | Candidat : \[ x_{t+1}=\arg\max_x\ \text{EI}(x) \] — le critère d'amélioration espérée, ou plus sobrement \[ \text{modèle}\to\text{acquisition}\to\text{évaluation} \]. |
| 1303 | 5b | 63 | OPTIMISATION MULTI-OBJECTIFS | Candidats : \[ \min\ \text{coût} \], \[ \max\ \text{qualité} \], \[ \min\ \text{délai} \]. |
| 1307 | 5b | 63 | OPTIMISATION MULTI-OBJECTIFS | Voir l. 1303. |
| 1311 | 5b | 63 | OPTIMISATION MULTI-OBJECTIFS | Voir l. 1303. |
| 1436 | 5b | 71 | OPTIMISATION ET RÉSEAUX NEURONAUX | Candidat : \[ x\to f_\theta(x)\to L\to\nabla_\theta L\to\theta_{t+1} \]. |
| 1512 | 5b | 77 | OPTIMISATION ET ROBOTIQUE | Candidats : J_longueur, J_énergie, J_temps, J_sécurité. La liste des contraintes qui suit suggère d'autres découpages — à trancher par l'auteur. |
| 1534 | 5b | 78 | OPTIMISATION ET LOGISTIQUE | Le même gabarit « ( / - ) » réapparaît en l. 2688. Candidat : une somme de coûts de transport \[ \sum_{i,j}c_{ij}x_{ij} \] encadrée par \left( \right). |
| 1832 | 5b | 92 | OPTIMISATION SOUS CONTRAINTE TEMPOREL… | Candidat : \[ \text{qualité de la solution} \] et \[ \text{temps de calcul} \] ont pu tenir dans ce bloc. |
| 1860 | 5b | 94 | OPTIMISATION ET COMPLEXITÉ | Candidat : \[ \text{formuler} \] et \[ \text{résoudre} \] — l'opposition que la phrase énonce. |
| 1884 | 5b | 95 | BRANCH AND BOUND | Candidat : un arbre de partition ASCII, analogue à la chaîne du §122. |
| 2039 | 5b | 105 | COMPLEXITÉ DES OPTIMISEURS | Candidats : \[ \text{nombre d'itérations} \] et \[ \text{coût par itération} \] — les deux facteurs dont le produit donne le coût total annoncé juste après. |
| 2174 | 5b | 109 | OPTIMISATION COMME PROBLÈME D’INGÉNIE… | Piste : le §122 (l. 2464-2484) déploie en ASCII une chaîne de dix étapes intacte (Problem → Variables → Objective → Constraints → Model → Optimizer → Iteration → Evaluation → Stopping criterion → Sol… |
| 2357 | 5b | 114 | STRUCTURES MATHÉMATIQUES À MAÎTRISER | Candidats : \[ \sum_i f_i(x) \] et \[ DP[s] \], tous deux présents ailleurs dans le document (l. 1760 et l. 716). |
| 2359 | 5b | 114 | STRUCTURES MATHÉMATIQUES À MAÎTRISER | Voir l. 2357. |
| 2379 | 5b | 115 | RELATION AVEC LE DOMAINE I — CALCUL D… | Candidats : \[ \nabla f(x)=0 \] puis \[ x_{t+1}=x_t-\eta\nabla f(x_t) \] — la condition d'optimalité, puis l'algorithme qui l'exploite. |
| 2383 | 5b | 115 | RELATION AVEC LE DOMAINE I — CALCUL D… | Voir l. 2379. |
| 2573 | 5b | 126 | EXPÉRIMENTATION D’OPTIMISATION | Candidats : comparer \[ \text{plusieurs algorithmes} \] / \[ \text{plusieurs taux d'apprentissage} \], mesurer \[ \text{la convergence} \] / \[ \text{la stabilité entre runs} \] (cette dernière expre… |
| 2579 | 5b | 126 | EXPÉRIMENTATION D’OPTIMISATION | Voir l. 2573. |
| 2607 | 5b | 128 | OPTIMISATION ET TRADE-OFFS | Candidats : coût / qualité / temps / robustesse — les quatre critères énumérés au §153 (l. 3355-3358). |
| 2609 | 5b | 128 | OPTIMISATION ET TRADE-OFFS | Voir l. 2607. |
| 2611 | 5b | 128 | OPTIMISATION ET TRADE-OFFS | Voir l. 2607. |
| 2613 | 5b | 128 | OPTIMISATION ET TRADE-OFFS | Voir l. 2607. |
| 2649 | 5b | 129 | OPTIMISATION ET SYSTÈMES INTELLIGENTS | Candidat : \[ \min\ \text{latence}\ \text{ou}\ \max\ \text{débit} \]. |
| 2688 | 5b | 131 | APPLICATIONS SOFTWARE ENGINEERING | Voir l. 1534. |
| 2732 | 5b | 133 | APPLICATIONS IA AGENTIQUE | Candidat : \[ C(a) \] — le coût d'une action, par symétrie avec le bloc J(a)=Q(a)−C(a)−T(a)−E(a) de la l. 2746. |
| 2771 | 5b | 134 | APPLICATIONS À L’ORCHESTRATION D’AGEN… | Candidat : \[ x_{ij}\in\{0{,}1\} \] — la variable d'affectation d'une tâche à un agent, puisque la section se conclut sur « un problème d'allocation et de scheduling » (l. 2785). |
| 2791 | 5b | 135 | APPLICATIONS À STANE OS / PERSONAL AI | Même gabarit qu'au §133 : un objectif en deux termes. Candidat : \[ J=Q  - C \]. |
| 2817 | 5b | 136 | APPLICATIONS À LA RECHERCHE D’HYPERPA… | Candidat : \[ h_1,h_2,\ldots \] — la suite des configurations retenues. |
| 2839 | 5b | 138 | APPLICATIONS À LA ROBOTIQUE | Candidat : \[ \text{perception}\to\text{planification}\to\text{contrôle} \]. |
| 2847 | 5b | 139 | APPLICATIONS À LA LOGISTIQUE | Candidats : \[ \text{coût} \] et \[ \text{délai} \]. |
| 2857 | 5b | 140 | APPLICATIONS AUX RÉSEAUX | Candidats : latence, débit, coût, fiabilité, énergie. |
| 2859 | 5b | 140 | APPLICATIONS AUX RÉSEAUX | Voir l. 2857. |
| 2861 | 5b | 140 | APPLICATIONS AUX RÉSEAUX | Voir l. 2857. |
| 2863 | 5b | 140 | APPLICATIONS AUX RÉSEAUX | Voir l. 2857. |
| 2865 | 5b | 140 | APPLICATIONS AUX RÉSEAUX | Voir l. 2857. |
| 3042 | 5b | 147 | EXERCICES THÉORIQUES | Candidat : \[ \eta=0{,}1 \]. La valeur est un choix d'auteur — un exercice a besoin d'un nombre, mais ce nombre ne se déduit pas du document. |
| 3091 | 5b | 149 | CHALLENGE AVEC IA | Candidat : \[ \text{la modélisation produite} \] et \[ \text{la vôtre} \] — l'exercice consiste à confronter deux modélisations. |
| 3380 | 5b | 154 | SYNTHÈSE CONCEPTUELLE | Candidat : \[ J=Q-C-T-E \] (l. 2746). |
| 3526 | 5b | 158 | SYNTHÈSE FINALE | Candidat : \[ \min\ \text{coût}\ \text{sous}\ \text{contrainte de qualité} \] — d'après la question 10 du §110 (« Quel compromis entre qualité et temps de calcul est acceptable ? »). |
| 3534 | 5b | 158 | SYNTHÈSE FINALE | Candidat : \[ I\to J \] — la notation employée au §155. |
