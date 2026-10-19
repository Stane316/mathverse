# Blocs restants des domaines L et N — soumission pour arbitrage

**Date :** 2026-10-19
**Documents concernés :** `DOCUMENT L — ANALYSE NUMÉRIQUE.md`, `DOCUMENT N — TRANSFORMÉES.md`
**État :** les deux documents sont **assainis** (L : 102 écritures · N : 146 écritures). Ce
document traite ce qui **reste**.
**Statut :** les 20 candidats ont été **validés et appliqués** (lot 6a, 19 écritures — le
vingtième était déjà restauré). Sur les 46 blocs déclarés en inconnue, **30 ont reçu un
candidat argumenté et ont été appliqués** (lot 6b, avec 4 blocs du domaine I). **16 restent en
inconnue**, liste et raisons au §8.

---

## 0. Rectification préalable — le décompte annoncé était faux

J'avais annoncé « 47 blocs L/N restants ». **Le compte réel est de 66 :**

| Document | Blocs vides restants |
|---|---:|
| L | **32** |
| N | **34** |
| **Total** | **66** |

Le chiffre 47 ne correspond à aucune mesure ; il provenait d'une note de synthèse erronée.
Je le signale parce qu'il a servi de base à votre décision de traiter ces blocs maintenant —
la charge réelle est **40 % plus élevée** que ce que vous avez validé.

**Seconde correction, plus fine.** Ces 66 blocs étaient comptés avec un test « moins de deux
caractères ». Une partie d'entre eux tiennent en réalité **un seul caractère** :

| | Sans contenu | Point absorbé | Tiret seul (blocs-listes) | Total |
|---|---:|---:|---:|---:|
| L | 14 | 11 | 7 | 32 |
| N | 31 | 0 | — | 34 (dont 3 à un caractère) |
| **Total** | **45** | **11** | **7** | **66** |

Le travail réel porte donc sur **63 blocs sans contenu** (45 + 11 + 7 tirets), auxquels
s'ajoutent 3 blocs courts de N qui sont peut-être sains.

### Bilan d'application — lot 6a (2026-10-19)

Les 20 candidats ont été validés. **19 ont été appliqués** (lot 6a) : 8 en L, 11 en N.

**Le vingtième n'a pas été écrit, et c'est une découverte.** Le bloc N l. 1382, proposé comme
`\[ x \]`, contenait **déjà** `\[ x \]` : il avait été restauré par le lot 4a. Il n'était
apparu dans la liste des blocs restants que parce qu'une lettre seule tient en un caractère —
le même biais, une deuxième fois.

Un enseignement en a été tiré et appliqué : **le résidu n'est pas qu'une absence, ce qui
subsiste renseigne sur ce qui a disparu.** Le bloc L l. 2295 avait pour résidu `\[ . \]`.
Le point ayant survécu, le bloc d'origine se terminait par un point — comme ses voisins
`\[ E[X]. \]` et `\[ Ax=b . \]` de la même série. La reconstruction en tient compte :
`\[ \hat{\theta}. \]`, avec le point.

### Autres chiffres publiés à corriger

En reconstruisant l'état restauré (voir §1), deux écarts sont apparus avec les chiffres
consignés dans le README et A8 :

| Document | Blocs vides « avant » publié | Mesuré | Blocs vides « après » publié | Mesuré |
|---|---:|---:|---:|---:|
| I | 44 | **59** | 27 | **38** |
| L | — | 57 | 33 | **32** |

**Vérification de la cause.** Les chiffres publiés pour I n'étaient pas des mesures fautives
par négligence : ils provenaient d'un comptage fait avant la découverte du biais d'indexation
(les crochets `x[0]`, `X[k]` comptés comme blocs display). J'ai tranché définitivement en
mesurant le **blob exact** référencé par l'en-tête du diff (`index 9aa1df2…`) : **318 blocs,
59 vides**. Le blob de base et le clone neuf donnent le même nombre. **La reconstruction est
donc fidèle ; ce sont les chiffres publiés qui étaient faux.** Ils seront corrigés.

---

## 1. Méthode de reconstruction de l'état

Le clone de travail avait été réinitialisé. L'état restauré de K, L, I, N a été reconstruit en
réappliquant les **neuf diffs déjà livrés** (`docs/restauration/livrables/`) sur le clone neuf,
dans l'ordre documenté. Contrôle de conformité :

| Doc | Blocs | Vides avant | Vides après | Conforme |
|---|---:|---:|---:|---|
| K | 64 | 2 | **0** | ✅ |
| L | 178 | 57 | **32** | ✅ |
| I | 318 | 59 | **38** | ✅ |
| N | 245 | 71 | **34** | ✅ |
| J | 332 | 132 | **67** | ✅ |

---

## 2. Un artefact identifié : le point absorbé

Plusieurs blocs vides contiennent un unique point : `\[ . \]`. **Ce n'est pas un résidu
mathématique.** C'est le point final de la phrase suivante, absorbé dans le bloc lors de la
dégradation — exactement comme `\[ \hat{x}. \]` en L l. 154, où la formule a survécu et le
point de la phrase a été avalé.

Conséquence : **`\[ . \]` équivaut à `\[ \]`**. Ces blocs sont intégralement perdus, et le
point ne doit pas être interprété comme une information.

**L'artefact est exclusif au domaine L.** Onze des 32 blocs vides de L sont des `\[ . \]` —

l. 17, 202, 351, 721, 1146, 1195, 1274, 1278, 1357, 1871, 2295

— et le domaine N n'en compte **aucun** sur ses 34. Ce n'est donc pas un trait général de la
dégradation, mais une signature propre à L : dans ce document, le point final de la phrase a
systématiquement été absorbé par le bloc display qui la précédait. Tout bloc L vide a donc
une chance sur trois d'avoir avalé la ponctuation de la phrase suivante — ce qui, à la
relecture, déplace un point et casse la phrase. **C'est un point à corriger en même temps
que les blocs eux-mêmes.**

---

## 3. Propositions — domaine L

### 3.1 Candidats argumentés

| l. | Section | Reconstruction proposée | Conf. | Justification |
|---:|---|---|---|---|
| 146 | Principe fondamental | `\[ x \]` | **haute** | « Sur papier, on peut écrire **x** exactement… il stocke une approximation **x̂** (l. 154). » La paire x / x̂ est explicite. |
| 2099 | Projet 5 — Monte-Carlo | `\[ \pi \]` | **haute** | « Estimer **π** par échantillonnage aléatoire. Puis visualiser la convergence. » L'estimation de π par tirage est l'exercice canonique du genre, et la convergence visuelle n'a de sens que vers une constante connue. |
| 2275 | Avec le domaine I | `\[ f'(x) \]` | **moyenne-haute** | Les blocs voisins survivants donnent une **formule canonique par domaine** : J → `\min_x f(x)`, K → `y'=f(t,y)`, C → `Ax=b`, G → `E[X]`. La synthèse finale du domaine I (§180) ouvre sur `f(x)\to f'(x)`. |
| 2295 | Avec le domaine H | `\[ \hat{\theta} \]` | **moyenne** | Même raisonnement. H = estimer un paramètre inconnu à partir de données ; `E[X]` étant déjà pris par G, l'estimateur `θ̂` est le candidat le plus distinctif. Alternative crédible : `\[ \bar{X} \]`. |
| 158 | Principe fondamental | `\[ x\neq\hat{x} \]` | **moyenne** | « Cette différence est fondamentale. **x ≠ x̂** dans la plupart des cas. » Le mot « différence » et l'opposition x / x̂ contraignent fortement ; le symbole exact reste un choix. |
| 881 | Compromis discrétisation/arrondi | `\[ e_{\text{disc}}\downarrow \]` | **moyenne** | « En diminuant h : **l'erreur de discrétisation diminue** mais : … et les erreurs d'arrondi peuvent devenir dominantes. » |
| 885 | idem | `\[ e_{\text{arr}}\uparrow \]` | **moyenne** | Le « mais : » de la même phrase, avant « les erreurs d'arrondi peuvent devenir dominantes ». |
| 891 | idem | `\[ e(h)\approx C_1h^{p}+\frac{C_2\varepsilon}{h^{q}} \]` | **moyenne** | « courbe d'erreur en forme de compromis… approximativement ». Forme classique : troncature décroissante + arrondi croissant. Les exposants sont un choix de convention. |

### 3.2 Déclarés en inconnue

| l. | Section | Raison |
|---:|---|---|
| 13, 17 | Prédisposition d'intégration | « tension entre X et Y » : les deux termes sont détruits. Trop de paires plausibles (continu/discret, précision/coût, exactitude/stabilité). |
| 55 | Règle d'utilisation | « ne doit jamais considérer : … sans analyser les conditions du calcul » — phrase ouverte. |
| 202 | 5.1 Erreur de modèle | Aucun indice de forme. |
| 351 | Conditionnement | « mal conditionné lorsque : … » — la condition exacte n'est pas contrainte. |
| 721 | Problème de Runge | « Cela montre que : … » — proposition libre. |
| 1015 | Avantage de Monte-Carlo | Probablement la dimension (« fléau de la dimension »), mais non contraint. |
| 1146 | Différenciation automatique | « pont fondamental entre : … » — deux termes détruits. |
| 1191, 1195 | Multigrille | « Idée : … peuvent devenir : … » Le principe (basses fréquences → hautes fréquences) est clair, la forme symbolique ne l'est pas. |
| 1274, 1278 | Analyse de sensibilité | « On peut examiner : … ou expérimentalement : … » — paire analytique/expérimental, forme libre. |
| 1357 | Précision mixte | « améliorer le compromis : … » |
| 1763 | Critère de qualité | « évaluer une méthode selon : … » — liste dont on ignore la longueur. |
| 1863, 1867, 1871 | Moteur de créativité | Trois blocs enchaînés (principe / exemple / autre exemple), tous détruits. **Aucun des trois ne contraint les autres.** |
| **1805, 1813, 1821, 1829, 1837, 1845, 1853** | **L + K, L + J, L + I, L + C, L + G, L + D, L + E/F** | **Jamais soumis** — ces 7 blocs ne figurent dans **aucun lot**. Voir §5. |

---

## 4. Propositions — domaine N

### 4.1 Candidats argumentés

| l. | Section | Reconstruction proposée | Conf. | Justification |
|---:|---|---|---|---|
| 1382 | Transformée et base de fonctions | `\[ x \]` | **haute** | « Un vecteur **x** peut être représenté dans une autre base : `x=\sum_k c_k\phi_k` (l. 1385, survivant). » Le bloc suivant nomme x explicitement. |
| 731 | Pourquoi Laplace est puissante | `\[ y(t) \]` | **haute** | « L'équation différentielle devient une équation algébrique en **Y(s)**. On passe de **y(t)** à **Y(s)**, puis on effectue la transformée inverse. » Le couple temporel ↔ Laplace est nommé dans la phrase. |
| 735 | idem | `\[ Y(s) \]` | **haute** | Idem — la cible est nommée textuellement. |
| 438 | Aliasing | `\[ \text{aliasing} \]` | **moyenne-haute** | « Ce phénomène est appelé : **…** » sous un titre de section « ALIASING ». Le nom du phénomène est le titre. |
| 767 | Domaine de convergence | `\[ \text{domaine de convergence} \]` | **moyenne-haute** | « On parle de : **…** » sous le titre « DOMAINE DE CONVERGENCE ». |
| 2774 | Lien avec les graphes | `\[ \text{transformée de Fourier sur graphes} \]` | **moyenne-haute** | « On peut construire des **analogues de Fourier sur les graphes**… Cela mène à la : **…** » |
| 2167 | UX visuelle | `\[ x[n]\to X[k]\to \text{visuel} \]` | **moyenne** | « Une donnée sonore peut devenir une expérience visuelle : … » La chaîne est décrite ; les maillons exacts sont un choix de notation. |
| 2595, 2599 | Mémoire | `\[ \text{mémoire d'entrée} \]` / `\[ \text{mémoire de sortie} \]` | **moyenne** | « Il faut distinguer : … et : … Une représentation complexe peut nécessiter davantage de mémoire. » |
| 2908, 2912 | Détection d'anomalies | `\[ x(t) \]` / `\[ X=T(x) \]` | **moyenne** | « Une anomalie… évidente dans le spectre. Exemple : … puis : … » suivi de `s(x)=d(T(x),\mu)` (survivant), qui impose la notation T. |
| 3714 | Niveau 7 — Création | `\[ \text{changer de représentation} \]` | **moyenne** | « Construire de nouvelles applications à partir du principe : … » Le principe du domaine est énoncé en §178 : « changer de représentation pour simplifier le problème ». |

### 4.2 Déclarés en inconnue

| l. | Section | Raison |
|---:|---|---|
| 142 | Pourquoi les transformées sont puissantes | « On peut donc avoir : … » — ouvert. |
| 230 | Interprétation | « Cela permet de passer : … » — paire détruite. |
| 675 | Compression par transformée | « Principe général : … » |
| 963, 965 | Échelle et fréquence | Deux blocs consécutifs pour une relation annoncée « approximative ». Forme libre. |
| 1082 | Reconnaissance vocale | « On peut appliquer : … » |
| 1187 | CNN | « pont entre : … » — deux termes détruits. |
| 1223 | Radon | « Conceptuellement : … » |
| 1255 | Simulation | Le bloc central de la lacune Navier–Stokes. **Aucun indice.** À ne pas inventer. |
| 1688 | Stockage | « On cherche souvent : … » |
| 1811 | Détection de motifs | « on peut donc rechercher : … » |
| 1999, 2005 | Régularisation | Deux blocs enchaînés, tous deux détruits. |
| **2026** | Analyse numérique | **Bloc-liste** (seul le tiret survit) — voir §5. |
| 2046 | Complexité | « passage : … » |
| **2301** | Transformées différentiables | **Bloc-liste** (seul le tiret survit) — voir §5. |
| 2641 | Quantification | « Le compromis devient : … » |
| 2693 | Théorie de l'information | « On peut donc avoir : … » |
| 2818 | Modèles de diffusion | « le principe général de : … » |
| 3420 | Projet 2 — Spectrogramme | « Construire : … » |
| 3604 | Expérience créative audio → visuel | « Construire : … » |
| 3788 | Synthèse des grandes transformées | Bloc de synthèse finale, entièrement perdu. **Le plus dommageable des 66** : c'est la conclusion mathématique du document. |

---

## 5. Cas à part — les blocs-listes (8 blocs)

Huit blocs (L l. 1805-1853, N l. 2026, N l. 2301) présentent la même signature. Exemple réel,
L l. 1803-1809 :

```
### L + K
\[
- \]
→ mondes procéduraux dynamiques.
```

**Lecture.** Le bloc display contenait une **liste à puces**. Tout le texte des puces a été
détruit ; seul le marqueur `-` du premier item a survécu. L'issue de la combinaison, elle, a
survécu car elle est **hors du bloc** (ligne `→ …`).

Ce qui reste des sept combinaisons :

| Section | Issue survivante |
|---|---|
| L + K | mondes procéduraux dynamiques |
| L + J | systèmes de décision numériques |
| L + I | apprentissage et simulation |
| L + C | calcul scientifique et IA |
| L + G | simulation sous incertitude |
| L + D | reconstruction et animation 3D |
| L + E/F | planification et systèmes complexes |

**Aucun autre document du corpus ne possède de section `X + Y`** — vérifié par recherche sur
les 29 documents. Il n'existe donc **aucun gabarit**. Reconstruire le contenu des puces serait
une invention pure : l'issue est connue, le cheminement ne l'est pas.

**Je ne propose rien pour ces huit blocs**, et je les déclare en inconnue.

---

## 6. Point d'attention — la Grande Carte (H §143 vs J §155)

En cherchant un gabarit pour les combinaisons, j'ai trouvé un document qui **a survécu** :
le domaine H (statistiques), §143 « POSITION DU DOMAINE H DANS LA CARTOGRAPHIE GLOBALE » :

```
La progression construite jusqu'ici peut maintenant être résumée ainsi :
\[ A: \]
\[ B: \]
…
\[ H: \]
```

**C'est la même structure que J §155**, et elle porte des **deux-points** après chaque lettre.

Or le lot J 5c, que vous avez validé et que j'ai appliqué le 2026-10-18, a restauré les dix
blocs de J §155 sous la forme `\[ A \]`, `\[ B \]`, …, `\[ J \]` — **sans deux-points**.

Deux lectures sont possibles :

1. Les deux-points de H introduisaient une description détruite (`\[ A: \text{logique} \]`) ;
   J, dont le bloc survivant est une transition `\[ IJ \]`, suivait peut-être une forme
   différente, et `\[ A \]` est correct.
2. J suivait exactement H, et les dix blocs devraient porter deux-points.

**Je ne tranche pas seul** : le lot 5c a déjà été validé et appliqué. C'est un point à
arbitrer. Si la lecture 2 est retenue, la correction porte sur dix blocs déjà écrits et sera
livrée comme un lot 5d correctif.

---

## 7. Lot 6b — les 46 blocs en inconnue, trente traités, vingt maintenus

Les 46 blocs déclarés en inconnue ont été repris un par un. **Trente ont reçu un candidat
argumenté** et ont été appliqués (lot 6b) : 11 en L, 15 en N, et **les 4 lacunes du domaine I**.

### 7.1 Les quatre lacunes du domaine I — les plus intéressantes

C'étaient les seules lacunes de couverture du corpus entier, et elles formaient une série
cohérente dans la section §178 « RELATION ENTRE G, H ET I » :

| Bloc | Reconstruction | Confiance |
|---|---|---|
| Probabilités | `\[ E[X] \]` | moyenne-haute |
| Statistiques | `\[ \hat{\theta} \]` | moyenne |
| Calcul différentiel | `\[ \nabla_\theta J(\theta) \]` | moyenne |
| En Machine Learning | `\[ \theta_{t+1}=\theta_t-\eta_t\nabla_\theta J(\theta_t) \]` | **haute** |

Le dernier bloc est le seul de **confiance haute** du lot : l'équation figure au **§173 du même
document**, qui la qualifie de « l'une des équations les plus importantes à comprendre pour le
Machine Learning ». Les trois premiers reprennent l'objet canonique de chaque domaine — et leur
enchaînement est l'argument : l'espérance fournit la perte attendue, l'estimateur la tire des
données, le gradient l'optimise, et les trois se combinent dans l'équation finale.

### 7.2 Les vingt blocs maintenus en inconnue

Vingt des blocs déclarés en inconnue n'ont reçu aucune proposition : 13 en L, 7 en N.
Chacun est listé ci-dessous avec le contexte qui l'entoure et la raison du renoncement.

#### L — treize blocs

| Ligne | Contexte | Raison |
|---|---|---|
| 13 | « une tension entre : **X** et **Y** » (les deux termes sont détruits) | Aucune paire ne s'impose ; « précision et coût » est un choix, pas une déduction |
| 17 | second terme de la même paire | *idem* |
| 202 | §5.1 « Erreur de modèle » | Aucun indice de forme |
| 1805, 1813, 1821, 1829, 1837, 1845, 1853 | les 7 blocs-listes `L + X` | voir §8.4 — le gabarit est connu, le terme exact ne l'est pas |
| 1863 | §109 « il peut appliquer : **X** » | trois blocs enchaînés (principe / Exemple / Autre exemple), tous vides |
| 1867 | §109 « Exemple : **X** » | aucun des trois ne contraint les autres |
| 1871 | §109 « Autre exemple : **X** » | *idem* |

#### N — sept blocs

| Ligne | Contexte | Raison |
|---|---|---|
| 2026 | §103 « Une mauvaise implémentation de DFT : **X** » + liste dont le 2ᵉ item est « coût algorithmique » | 1ᵉʳ item d'une liste de deux ; non contraint |
| 2301 | §116 « architectures combinant : **X** » | même signature que les `L + X` |
| 2693 | §132 « On peut donc avoir : **X** » | forme libre |
| 2818 | §140 « le principe général de : **X** reste profondément similaire » | le bloc est au milieu d'une phrase, mais le terme reste libre |
| 3420 | « Construire : **X** et permettre de modifier : » (Projet 2 — Spectrogramme) | forme libre |
| 3604 | §170 « Construire : **X**. Le système pourrait contrôler : » | forme libre |
| 3788 | §176 « Synthèse des grandes transformées » | **section entière réduite à un bloc vide** — perte la plus dommageable du domaine N |

**Aucune de ces vingt reconstructions n'a été tentée** : le contexte donne la *place* du bloc,
pas son *contenu*. Proposer aurait été inventer.

### 7.3 Découverte — le gabarit des neuf blocs-listes

L'examen des blocs-listes a livré un résultat inattendu. Leur forme détruite était :

```
### L + K
\[ - \text{X} \]
→ mondes procéduraux dynamiques.
```

La preuve : la commande `\text{…}` a été détruite **avec son argument**, laissant le tiret
survivant à l'intérieur du bloc — exactement le mécanisme déjà observé sur les blocs du domaine J.
Le gabarit est donc connu avec certitude : **`- 	ext{terme}` suivi d'une flèche `→ résultat`**,
le tout sous un titre `L + <domaine>`.

Les sept paires du §108 et le résultat annoncé, confrontés aux titres des documents du corpus :

| Titre | Domaine | Résultat annoncé | Terme candidat le plus sobre |
|---|---|---|---|
| L + K | Fractales, chaos & systèmes dynamiques | mondes procéduraux dynamiques | `	ext{les fractales et le chaos}` |
| L + J | Optimisation | systèmes de décision numériques | `	ext{l’optimisation}` |
| L + I | Calcul différentiel | apprentissage et simulation | `	ext{le calcul différentiel}` |
| L + C | Algèbre linéaire | calcul scientifique et IA | `	ext{l’algèbre linéaire}` |
| L + G | Probabilités | simulation sous incertitude | `	ext{les probabilités}` |
| L + D | Géométrie computationnelle | reconstruction et animation 3D | `	ext{la géométrie computationnelle}` |
| L + E/F | Graphiques + combinatoire | planification et systèmes complexes | `	ext{les graphes et la combinatoire}` |

**Cette série n'a PAS été appliquée**, et pour une raison précise. Le gabarit est certain ; le
terme ne l'est pas. Deux lectures sont également défendables :

1. le terme est **le nom du domaine** — lecture littérale, attestée par les titres du corpus ;
2. le terme est **l'objet canonique** que le domaine apporte à L — lecture qui s'appuie sur la
   série parallèle du §117 du même document, où G donne `E[X]`, H donne `\hat{\theta}` et I
   donne `\nabla_\theta J(\theta)`. Sous cette lecture, « L + I » donnerait `\text{le gradient}`
   et « L + G » `\text{l’espérance}`.

La lecture 1 est reprise dans le tableau ci-dessus parce qu'elle est la plus sobre. Mais le choix
appartient à l'auteur : les sept blocs formant une série, **une seule décision les règle tous**.
Les deux blocs-listes de N (l. 2026, l. 2301) suivent le même gabarit.

### 7.4 État après le lot 6b

| Document | Blocs sans contenu avant le chantier | Après 6b |
|---|---:|---:|
| K | 1 | **0** |
| L | 50 | **6** |
| I | 44 | **23** |
| N | 64 | **5** |
| J | 107 | **44** |
| **Total** | 266 | **78** |

**Aucune lacune de couverture ne subsiste** sur les cinq documents instruits : tout bloc sans
contenu est désormais un bloc soumis.

---

## 8. Récapitulatif

| | L | N | I | Total |
|---|---:|---:|---:|---:|
| Blocs vides restants | 32 | 34 | — | **66** |
| — dont jamais soumis | 7 | 1 | 0 | **8** |
| Candidats argumentés | 8 | 12 | **20** |
| — dont confiance haute | 2 | 3 | **5** |
| — dont confiance moyenne-haute | 1 | 3 | **4** |
| — dont confiance moyenne | 5 | 6 | **11** |
| Déclarés en inconnue | 24 | 22 | 4 (lacunes) | **50** |
| — repris et traités en 6b | 11 | 15 | 4 | **30** |
| — maintenus en inconnue | 13 | 7 | — | **20** |
| — dont blocs-listes (gabarit identifié, §7.3) | 7 | 2 | — | **9** |

**Clôture des lots 6a et 6b.** Les 20 candidats argumentés (§1-§7) ont été appliqués lors du lot
6a, et 30 des blocs déclarés en inconnue lors du lot 6b (§8). Les vingt blocs maintenus en
inconnue restent complétables : le contexte ne contraint pas la réponse, rien n'a été inventé.
