# Blocs restants des domaines L et N — soumission pour arbitrage

**Date :** 2026-10-19
**Documents concernés :** `DOCUMENT L — ANALYSE NUMÉRIQUE.md`, `DOCUMENT N — TRANSFORMÉES.md`
**État :** les deux documents sont **assainis** (L : 102 écritures · N : 146 écritures). Ce
document traite ce qui **reste**.
**Statut :** les 20 candidats ont été **validés et appliqués** (lot 6a, 19 écritures — le
vingtième était déjà restauré). Les 46 blocs déclarés en inconnue restent **à trancher** ;
rien n'a été écrit pour eux.

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

## 7. Récapitulatif

| | L | N | Total |
|---|---:|---:|---:|
| Blocs vides restants | 32 | 34 | **66** |
| — dont jamais soumis | 7 | 1 | **8** |
| Candidats argumentés | 8 | 12 | **20** |
| — dont confiance haute | 2 | 3 | **5** |
| — dont confiance moyenne-haute | 1 | 3 | **4** |
| — dont confiance moyenne | 5 | 6 | **11** |
| Déclarés en inconnue | 24 | 22 | **46** |
| — dont blocs-listes | 7 | 2 | **9** |

**En attente de votre arbitrage.** Trois décisions sont possibles par bloc : valider la
proposition, la corriger, ou laisser en inconnue. Rien n'est écrit tant que vous n'avez pas
tranché.
