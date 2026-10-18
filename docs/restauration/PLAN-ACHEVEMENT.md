# PLAN D'ACHÈVEMENT DU CHANTIER DE RESTAURATION

**Identifiant :** R-PLAN · **Date :** 2026-10-18 · **Statut :** proposition en revue
**Décision du porteur (2026-10-18) :** « le chantier de restauration continue et nous devons
l'achever avant de débuter la phase 2 ».
**Conséquence :** la phase 2 (étude d'écosystème) ne démarrera qu'après la clôture de ce chantier.

---

## 1. Ce que « achever » veut dire

Le chantier ne sera pas « terminé » au sens où les fichiers retrouveraient leur état d'origine :
c'est impossible, le contenu détruit n'existe nulle part. La définition de fin retenue est donc :

> **Le chantier est achevé lorsque, pour chacun des 29 documents, tout bloc dégradé a reçu soit
> une reconstruction validée, soit une mention explicite « contenu perdu, non reconstruit »,
> et que cette décision est consignée et traçable.**

Cette définition est importante : elle rend la fin **atteignable**. Exiger une reconstruction
complète rendrait le chantier infini, parce qu'une part des blocs ne peut pas être devinée.

## 2. Mesure du reste à faire (relevé du 2026-10-18)

| Document | Défauts signalés | Blocs d'affichage | Lignes | Estimation réelle¹ |
|---|---:|---:|---:|---:|
| J — Optimisation | 166 | 338 | 3 542 | ~300 |
| I — Calcul différentiel | 109 | 320 | 3 177 | ~200 |
| N — Transformées | 104 | 274 | 3 947 | ~190 |
| H — Statistiques | 64 | 130 | 2 662 | ~115 |
| G — Probabilités | 60 | 278 | 3 072 | ~110 |
| M — Théorie de l'information | 59 | 256 | 4 276 | ~105 |
| O — Complexité | 38 | 248 | 3 618 | ~70 |
| **L — Analyse numérique** | **~14** | 178 | 2 349 | **33 blocs en attente** |
| UI/UX (document 02) | 20 | 20 | 3 202 | ~35 |
| F — Combinatoire | 12 | 120 | 2 945 | ~20 |
| Q — Logique, automates | 11 | 79 | 3 142 | ~20 |
| P — Cryptographie | 2 | 66 | 4 120 | ~5 |
| E, R, S, U | 0 | 48 | 10 482 | à vérifier (lecture) |
| Documents « Ai Technical Litteracy » 01-08 | 0 | 12 | 27 275 | à vérifier (lecture) |
| **Total** | **~659** | **~2 370** | | **~1 200** |

¹ L'inventaire automatique sous-estime : **+55 %** de défauts découverts à la lecture sur K,
**+115 %** sur L, **+105 %** sur I. Le facteur 1,8 retenu dans ce tableau est donc trop bas ; voir
le recalibrage du §2 bis.

## 2 bis. Recalibrage — mesuré sur le document I (2026-10-18)

Le document I est le premier à avoir été lu **bloc par bloc en intégralité**, et non à partir du
seul inventaire. La mesure corrige l'estimation ci-dessus :

| Grandeur | Mesure sur I |
|---|---:|
| Blocs d'affichage | 318 |
| Défauts signalés par l'inventaire | 109 |
| **Blocs réellement dégradés (lecture intégrale)** | **223** |
| Sous-estimation de l'inventaire | **× 2,05** |
| **Part des blocs dégradés** | **70 %** |

Deux conséquences, à prendre comme des faits et non comme des opinions :

1. **Le total restant est plus élevé que les ~1 200 annoncés.** En appliquant le ratio de 70 % aux
   ~2 060 blocs restants des documents à équations, on obtient **1 100 à 1 600 blocs** à traiter,
   selon la densité mathématique de chaque document. I en est l'un des plus denses ; les documents
   « Ai Technical Litteracy » en sont les moins denses. L'intervalle sera resserré à mesure que
   chaque document sera mesuré.
2. **L'inventaire automatique ne peut servir qu'à ordonner le travail, jamais à le chiffrer.** Il
   reste utile pour désigner les sections à lire en priorité.

## 3. Les deux flux

Le chantier se divise en deux flux de nature différente. Les confondre est ce qui bloquerait
l'achèvement.

### Flux A — reconstructions possibles (autonome)

Blocs dont le fragment survivant ou la forme canonique impose la lecture : équations, sommes,
intégrales, dérivées, définitions standard. Je les produis, je les justifie, je fournis un test
de validation. **Votre charge : une validation par lot**, pas ligne par ligne.

### Flux B — blocs à arbitrer (dépend de vous)

Blocs vides qui contenaient des **termes, des énoncés ou des chaînes de mots**. Rien ne subsiste.
Sur le document L, ils représentaient **34 %** des blocs dégradés. Il y en aura des centaines sur
le corpus.

**Protocole proposé pour tenir la cadence** : je soumets les candidats **par document, en un seul
tableau**, avec un candidat recommandé par ligne. Vous répondez soit « lot accepté », soit
« lot accepté sauf les lignes X, Y », soit votre propre texte pour certaines lignes. Un échange
par document, pas par ligne.

**Repli « contenu perdu » — validé par le porteur (2026-10-18).** Pour tout bloc que ni vous ni
moi ne pouvons restituer, la mention « contenu perdu » est l'issue retenue, et elle est
préférable à une invention. Procédure :

1. le bloc reste **vide dans le fichier** — on n'écrit rien qui ressemble à du contenu ;
2. il est enregistré dans le **registre des blocs non restitués** (annexe du chantier) avec son
   numéro de ligne, son contexte, et la mention « non restituable » ;
3. il est **décompté du compteur de défauts** sans être compté comme restauré : les deux colonnes
   sont séparées dans les rapports ;
4. il reste complétable plus tard, si vous retrouvez l'original ou si vous décidez d'un contenu.

Ce repli est la soupape qui rend l'achèvement atteignable.

## 4. Ordre proposé

| Ordre | Document | Pourquoi cet ordre |
|---:|---|---|
| 1 | **I — Calcul différentiel** | alimente directement les fiches de phase 1 et les composants de courbes, champs et flux |
| 2 | **N — Transformées** | idem ; socle des composants de signal et de spectre |
| 3 | **J — Optimisation** | le plus gros lot ; socle des réglages et de l'exploration scientifique |
| 4 | H, G, M | statistiques, probabilités, information : socle des bruits, aléas et mesures |
| 5 | O, F, Q, P | complexité, combinatoire, logique, cryptographie : apport indirect |
| 6 | UI/UX (02) | périmètre site, DX, performance, accessibilité |
| 7 | E, R, S, U | zéro défaut signalé mais lecture nécessaire (48 blocs) |
| 8 | « Ai Technical Litteracy » 01-08 | 12 blocs seulement : vérification rapide |
| 9 | **A, B, C, D** | restructuration — **dans le périmètre** (§5) |

La clôture de L (33 blocs) est faite en priorité, en parallèle de l'ouverture de I.

### Entrelacement avec les fiches de phase 1 — décidé par le porteur (2026-10-18)

Les deux chantiers ne sont pas concurrents, ils se nourrissent : **je restaure d'abord, je
rédige la fiche ensuite**, sur un document sain. Une seule lecture par document au lieu de deux.

| Rang | Restauration | Fiche immédiatement après |
|---|---|---|
| 0 | L (33 blocs en attente d'arbitrage) | **L** |
| 1 | **I** — Calcul différentiel | **I** |
| 2 | **N** — Transformées | **N** |
| 3 | J — Optimisation | *(hors lot courant)* |
| … | suite du plan | — |

Le porteur demandait le lot de fiches **D, I, L, N** ; D n'a rien à restaurer (0 bloc, document
aplatissement intégral) et relève du rang 10 du présent plan.

## 5. Le cas A, B, C, D — décision à prendre

Ces quatre documents ont perdu **leur arborescence de titres et leurs équations** (103 à 133
lignes chacun) : le texte a été aplati. Vous avez confirmé qu'aucune version antérieure n'existe.
Restent donc une **restructuration par reconstruction** : échantillonnage, détection des marqueurs
de section, reconstruction d'un plan. Ce n'est pas une restauration d'équations, et son résultat
ne sera jamais fidèle à l'original.

**Décision du porteur (2026-10-18) : ce chantier FAIT PARTIE de l'achèvement exigé avant la
phase 2.** Il est donc inscrit en fin de plan (rang 10), avec les réserves suivantes, qui sont
des constats et non des objections :

1. le résultat ne sera **jamais fidèle à l'original** : on ne peut pas retrouver un plan détruit,
   seulement en proposer un qui rende le texte utilisable ;
2. la méthode est différente : échantillonnage des 478 lignes, détection des marqueurs de section
   (numérotations, majuscules, changements de registre), reconstruction d'une arborescence
   **proposée**, jamais présentée comme restituée ;
3. chaque titre reconstruit portera la mention « reconstruit » — un plan inventé silencieusement
   serait pire que pas de plan du tout ;
4. c'est le dernier rang : rien d'autre ne l'attend.

## 6. Le chemin critique, c'est vous

Le flux B est le facteur limitant. Sur le document L, 44 blocs ont demandé 11 arbitrages ; au
rythme observé, le corpus en demandera **plusieurs centaines**. Avec le protocole « un échange par
document », la charge devient tenable : une quinzaine de réponses de votre part sur la durée du
chantier, chacune portant sur un tableau.

Sans ce protocole, le chantier peut durer indéfiniment. C'est le point à valider en priorité.

## 7. Risques

| Risque | Gravité | Parade |
|---|---|---|
| Le flux B s'accumule plus vite qu'il ne se résorbe | **Haute** | protocole par lot (§3) + repli « contenu perdu » |
| Le volume réel dépasse l'estimation (mesuré : ×2 sur I) | **Haute** | mesure dès l'ouverture de chaque document ; l'estimation est révisée à chaque lot, jamais figée |
| Les sections de synthèse concentrent les blocs non restituables | Moyenne | elles sont traitées en fin de document, en une seule salve d'arbitrage |
| Introduire une reconstruction fausse | Haute | confiance déclarée, test de validation, validation par lot |
| Fatigue de relecture → baisse de rigueur | Moyenne | un document à la fois ; rejeu systématique de l'inventaire après application |
| Réinitialisation de l'environnement | Moyenne | tout lot validé est commité immédiatement ; les diffs sont régénérables |
| Volume : ~2 370 blocs à lire | Moyenne | lecture ciblée sur les régions contenant des blocs, éprouvée sur L |

## 8. Définition de sortie, par document

Un document est déclaré **traité** lorsque :

1. tous ses blocs d'affichage ont été lus un par un ;
2. chaque bloc dégradé a une proposition (flux A) ou une décision (flux B) ;
3. le correctif a été vérifié à sec puis appliqué ;
4. l'inventaire a été rejoué et le compteur du document est à zéro ;
5. le diff et le rapport d'application sont livrés ;
6. les blocs non restituables sont inscrits au registre, pas laissés dans l'oubli.

C'est ainsi que K et L ont été traités, et leurs compteurs sont effectivement à zéro — à
l'exception des blocs explicitement laissés en attente.
