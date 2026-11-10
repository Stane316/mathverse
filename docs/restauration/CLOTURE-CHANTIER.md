# CLÔTURE DU CHANTIER DE RESTAURATION — PÉRIMÈTRE VALIDÉ

**Date :** 2026-10-19
**Statut :** chantier **clos sur le périmètre défini au §2**, sur décision du porteur.
**Nature du document :** acte de clôture et procédure de reprise. Il ne valide pas le contenu
restauré — il constate l'état atteint et permet de le retrouver.

---

## 1. Décision du porteur (2026-10-19)

Interrogé sur le point de savoir si le chantier devait être mené à son terme avant l'ouverture de
la phase 2 — règle arrêtée le 2026-10-18 —, le porteur a choisi :

> **Réduire le périmètre et basculer.** Le chantier est déclaré clos sur les cinq documents
> instruits. La phase 2 est ouverte. Les quinze autres documents mathématiques et les huit
> documents de littératie sont différés ; lors de la reprise, ils seront traités **tous, dans
> l'ordre A → U**.

Cette décision **remplace** la règle du 2026-10-18 (« le chantier doit être complété avant la
phase 2 ») sans la contredire dans son esprit : elle en redéfinit le terme. Le chantier n'est pas
abandonné, il est **suspendu à un périmètre explicitement validé**.

Ce qui a rendu la clôture acceptable : **la couverture des cinq documents est complète.** Aucun
bloc sans contenu n'y est une lacune — tous ont été soumis au moins une fois, et ceux qui restent
vides le sont par décision argumentée, non par oubli (§4).

---

## 2. Périmètre clos

Cinq documents, choisis par le porteur au lot 1 du plan A6 parce qu'ils couvrent directement les
cinq familles de composants prioritaires :

| Domaine | Document | Blocs display | Restaurations appliquées |
|---|---|---:|---:|
| **K** | Fractales, chaos & systèmes dynamiques | 64 | 40 |
| **L** | Analyse numérique | 178 | 121 |
| **I** | Calcul différentiel | 318 | 208 |
| **N** | Transformées | 245 | 172 |
| **J** | Optimisation | 332 | 232 |
| **Total** | | **1 137** | **773** |

Le domaine **D** (géométrie computationnelle) possède une fiche mais **n'a pas été restauré** :
il relève du régime de dégradation 3 (formules aplaties en texte, `\[…\]` supprimés), dont le
traitement fait l'objet du lot 4 du plan A6 avec A, B et C. **Il sort donc du périmètre clos.**

---

## 3. État chiffré au moment de la clôture

Mesuré le 2026-10-19 après le lot 6b, puis **vérifié le 2026-10-19** sur un clone neuf après
réapplication des 17 diffs (§6.1).

> ⚠️ **DÉFINITION DU COMPTAGE — à lire avant tout usage de ce tableau.**
> Un « bloc display » est ici compté par la règle **`\[` en début de ligne**. Cette règle donne
> **1 137** blocs. Une règle plus large — toute paire `\[…\]`, y compris lorsque le délimiteur
> ouvrant n'ouvre pas la ligne — donne **1 146**. **Les deux chiffres sont exacts sous leur
> définition**, et ils diffèrent parce que 9 blocs n'ouvrent pas leur ligne. La figure de 1 137
> publiée jusqu'ici ne précisait pas sa règle : c'est un défaut, désormais corrigé.
> **Ne jamais comparer deux chiffres obtenus sous des définitions différentes.**

| Document | Blocs display | Sans contenu avant | Sans contenu après | Inconnues | Lacunes |
|---|---:|---:|---:|---:|---:|
| K | 64 | 1 | **0** | 1 | 0 |
| L | 178 | 50 | **6** | 44 | 0 |
| I | 318 | 44 | **23** | 28 | **0** |
| N | 245 | 64 | **5** | 33 | 0 |
| J | 332 | 107 | **44** | 66 | 0 |
| **Total** | **1 137** | **266** | **78** | **172** | **0** |

Définitions retenues (rappel, elles ont fait l'objet de deux corrections) :

- **sans contenu** = bloc vide **ou** ne contenant qu'un point. Un bloc contenant une seule
  lettre n'est **pas** vide : il est restauré.
- **inconnue** = bloc soumis, pour lequel aucune proposition n'a été retenue.
- **lacune** = bloc sans contenu n'ayant jamais été soumis dans aucun lot.

**Les 4 lacunes qui subsistaient ont toutes été traitées par le lot 6b.** Elles se trouvaient dans
le domaine I et formaient une série unique au §178 « RELATION ENTRE G, H ET I ». La quatrième a
été retrouvée textuellement au §173 du même document.

> ✅ **Provenance des chiffres — levée le 2026-10-19.** La réserve qui figurait ici
> (impossibilité de re-mesurer après la destruction du clone) **a été levée** : le clone a été
> reconstitué et les 17 diffs réappliqués (§6.1). **La mesure directe reproduit la table à
> l'identique** : 78 blocs sans contenu, écart nul sur les cinq documents.
>
> ⚠️ **Une correction subsiste** : le total de **1 137 blocs** annoncé au §2 est exact sous la règle
> « délimiteur en début de ligne », mais la règle n'était pas précisée. Sous la règle large, le
> total est **1 146** (N comptant 254 blocs et non 245). Les deux figures sont désormais énoncées
> avec leur définition.

---

## 4. Ce qui reste sans contenu — registre du « contenu perdu »

Le fallback « contenu perdu », validé par le porteur, s'applique : **78 blocs restent vides,
intacts et complétables**. Ils se répartissent ainsi :

| Document | Blocs sans contenu | dont blocs-listes |
|---|---:|---:|
| L | 6 | (7 hors décompte) |
| I | 23 | 0 |
| N | 5 | (2 hors décompte) |
| J | 44 | 0 |

S'y ajoutent **9 blocs-listes** (7 en L, 2 en N) dont seul un tiret a survécu.

### 4.1 La découverte du lot 6b

Ces neuf blocs-listes ont livré un résultat inattendu. Leur forme détruite était :

```
### L + K
\[ - \text{X} \]
→ mondes procéduraux dynamiques.
```

La preuve : la commande `\text{…}` a été détruite **avec son argument**, laissant le tiret
survivant à l'intérieur du bloc — mécanisme déjà observé sur les blocs du domaine J. Le gabarit
est donc **certain** : `- \text{terme}` suivi d'une flèche `→ résultat`, sous un titre `L + <domaine>`.

Le terme manquant n'est en revanche pas déductible de façon unique. Deux lectures également
défendables :

1. le terme est **le nom du domaine** — lecture littérale, attestée par les titres du corpus ;
2. le terme est **l'objet canonique** que le domaine apporte à L — lecture appuyée sur la série
   parallèle du §117 du même document, où G donne `E[X]`, H donne `\hat{\theta}` et I donne
   `\nabla_\theta J(\theta)`.

Les sept blocs formant une série, **une seule décision du porteur les règle tous**. Rien n'a été
écrit en attendant. Détail complet au §7.3 de `propositions/domaine-L-N-blocs-restants.md`.

### 4.2 Le point absorbé — règle acquise

Onze blocs du domaine L portaient le résidu `\[ . \]`. Le point ayant survécu à la destruction,
le bloc d'origine **se terminait par un point**. Ce point est restitué dans les reconstructions.
L est le seul document du corpus à présenter ce phénomène ; N n'en a aucun.

---

## 5. Documents différés

### 5.1 Corpus mathématique — 15 documents

Traités lors de la reprise, **tous, dans l'ordre A → U** :

| Lettre | Titre | Lignes | Éq. affichées |
|---|---|---:|---:|
| A | Logique et fondements de l'informatique (maître) | 119 | 0 |
| B | Théorie des nombres | 103 | 0 |
| C | Algèbre linéaire | 123 | 0 |
| D | Géométrie computationnelle | 133 | 0 |
| E | Théorie des graphes et algorithmes | 2 858 | 11 |
| F | Combinatoire et optimisation combinatoire | 2 945 | 118 |
| G | Probabilités | 3 072 | 236 |
| H | Statistiques | 2 662 | 125 |
| M | Théorie de l'information | 4 276 | 251 |
| O | Théorie de la complexité | 3 618 | 248 |
| P | Cryptographie | 4 120 | 66 |
| Q | Logique, automates & langages | 3 142 | 79 |
| R | Algèbre abstraite | 2 706 | 6 |
| S | Topologie | 2 524 | 8 |
| U | Logique floue | 2 394 | 23 |
| **Total** | | **34 795** | **1 171** |

**A, B, C, D** relèvent du traitement spécial du lot 4 (régime 3 : ni titres ni équations,
103 à 133 lignes pour 58 à 82 Kio). Leur restructuration reste dans le périmètre, sur décision
validée du porteur.

### 5.2 Littératie technique — 8 documents

`Ai Technical Litteracy` 01–08 : 27 075 lignes, **32 équations affichées seulement**. Leur
instruction est beaucoup plus légère : le formalisme n'y est presque pas dégradé.

---

## 6. Procédure de reprise

Le clone du dépôt de connaissances étant détruit, la reprise commence par le reconstituer.

1. **Recloner** `Stane316/my-own-connaissance` en lecture seule.
2. **Vérifier** l'état de départ : le dépôt a été écrasé par un squashing le 2026-10-19
   (HEAD ramené à `f0f5e2d`). Les restaurations livrées n'y sont donc **pas** présentes ; elles
   existent uniquement dans les diffs de `livrables/`.
3. **Appliquer les diffs dans l'ordre ci-dessous.** L'ordre n'est pas interchangeable : au sein
   d'un lot, les numéros de ligne les plus élevés d'abord, et le lot 5c est **imbriqué** dans le
   lot 5b.

| Ordre | Document | Fichier à appliquer |
|---:|---|---|
| 1 | K | `domaine-K-lot1.gitdiff` |
| 2 | K | `domaine-K-lot1bis.gitdiff` |
| 3 | L | `domaine-L.gitdiff` |
| 4 | L | `domaine-L-lot2bis.gitdiff` |
| 5 | I | `domaine-I-lot3b.gitdiff` |
| 6 | I | `domaine-I-lot3a.gitdiff` |
| 7 | I | `domaine-I-lot3c.gitdiff` |
| 8 | N | `domaine-N-lot4b.gitdiff` |
| 9 | N | `domaine-N-lot4a.gitdiff` |
| 10 | J | `domaine-J-lot5b.gitdiff` |
| 11 | J | `domaine-J-lot5c.gitdiff` |
| 12 | J | `domaine-J-lot5a.gitdiff` |
| 13 | L | `domaine-L-lot6a.gitdiff` |
| 14 | N | `domaine-N-lot6a.gitdiff` |
| 15 | I | `domaine-I-lot6b.gitdiff` |
| 16 | L | `domaine-L-lot6b.gitdiff` |
| 17 | N | `domaine-N-lot6b.gitdiff` |

4. **Vérifier** après chaque document : `git apply --check`, puis contrôle de l'absence de
   mojibake — recherche de la séquence « A tilde + deux-points-suscrit » (trace classique d'un
   UTF-8 relu en latin-1) ; le comptage doit renvoyer 0.
5. **Re-mesurer** le tableau du §3 sur les fichiers. Ne jamais recomposer un total par
   arithmétique : les recouvrements entre lots sont intentionnels.

Chaque `.gitdiff` est accompagné d'un `.message-commit.txt` : l'historique du dépôt de
connaissance reste ainsi reproductible document par document.

---

## 6.1 La procédure a été éprouvée — résultats

Exécutée le 2026-10-19 sur un clone neuf (`f0f5e2d`), dans l'ordre du §6, avec `git apply --check`
avant chaque application.

| Vérification | Résultat |
|---|---|
| Diffs appliqués | **17 / 17**, sans erreur |
| Contrôle d'absence de mojibake | **0** sur les cinq documents |
| Table « sans contenu » du §3 | **reproduite à l'identique** — 78, écart nul sur K, L, I, N et J |
| Équilibre des délimiteurs `\[` / `\]` | **0** sur les cinq documents — aucune structure cassée |

**La procédure est donc valide.** L'outil `tools/restauration/mesurer_couverture.py` permet de la
rejouer : il compare la mesure à la table publiée et signale tout écart.

### Une anomalie expliquée

La réapplication a fait apparaître une différence de comptage : **N perdait 4 blocs et J 1 bloc**
entre l'état avant et l'état après restauration. L'explication a été trouvée, et elle est
rassurante : les lignes supprimées contenaient des **délimiteurs imbriqués**, résidus de la
dégradation — par exemple `\[ {xp_} \[f_(x)\] \]` ou `\[ DP\[s\] = s \]`.

Autrement dit : **ces « blocs perdus » n'étaient pas des blocs, mais des artefacts que les
restaurations ont supprimés à juste titre.** L'équilibre des délimiteurs, vérifié à zéro sur les
cinq documents, confirme qu'aucune structure n'a été endommagée.

---

## 7. Corrections de chiffres publiés

Trois figures diffusées pendant le chantier se sont révélées fausses ou ambiguës. Elles sont
corrigées ici parce que des décisions en dépendent.

### 7.1 Le compte de « 29 documents » était exact, mais par un autre chemin

L'inventaire A2 liste 29 fichiers : 20 documents mathématiques, le `README.md` de la collection,
et 8 documents de littératie. Le plan A6 attend pour sa part **21 fiches mathématiques**
(domaines A à U, la lettre **T n'existe pas** et donne lieu à une *fiche d'absence*) plus 8 fiches
de littératie — soit **29 fiches**.

Les deux dénombrements tombent juste à 29, mais ne comptent pas la même chose. **Le nombre de
fiches attendues est 29 ; le nombre de documents réels est 28** (20 + 8), la 29ᵉ fiche étant celle
de l'absence de T.

**Conséquence : 5 fiches produites, 24 restantes** — et non 23 comme annoncé à l'ouverture de la
présente séance.

### 7.2 P n'est assigné à aucun lot

Le plan A6 §4 répartissait les domaines en cinq lots. Le domaine **P — Cryptographie** (4 120 lignes,
66 équations affichées, soit le 4ᵉ document le plus volumineux du corpus) **n'apparaissait dans
aucun**. Les lots couvraient 19 des 20 documents réels. — **Corrigé le 2026-10-21** : P est désormais
assigné au **lot 3** du plan A6 §4 (apports indirects), avec la justification et le décompte
**20 documents réels sur 20**. La lettre **T**, qui n'existe pas, reste hors lot : elle donne lieu à
la fiche d'absence. Le renvoi « §5.1 » figurant ici à l'origine était orphelin — ce numéro de
section n'existe dans aucun livrable.

### 7.3bis Le total de 1 137 blocs était exact, mais sa règle n'était pas énoncée

Vérifié le 2026-10-19 (§6.1) : 1 137 blocs sous la règle « délimiteur en début de ligne »,
**1 146** sous la règle large. La figure publiée n'était pas fausse — elle était **sans
définition**, ce qui la rendait incomparable. C'est la quatrième occurrence du même défaut dans ce
chantier : un chiffre publié sans la règle qui l'a produit.

### 7.3 Le test « moins de deux caractères » n'est pas une mesure

Rappelé ici parce que la leçon vaut pour la phase 2 : une heuristique de longueur sur un résidu
avait fait compter comme vides 44 blocs sains ne tenant qu'une seule lettre, et fait annoncer
18 lacunes de couverture là où il y en avait **4**. Toute figure publiée doit être relue sur le
fichier, jamais recomposée.

---

## 8. Ce que la clôture ne dit pas

- **La clôture n'est pas une validation.** Aucun contenu restauré n'a été approuvé bloc par bloc
  par le porteur. Les 773 restaurations appliquées portent chacune un niveau de confiance ;
  vingt des trente propositions du lot 6b sont de confiance **moyenne**.
- **La restauration est une reconstruction, pas une récupération.** Les arguments LaTeX détruits
  n'existent nulle part. Ce qui est écrit est une proposition argumentée, pas l'original.
- **Le dépôt de connaissances n'a jamais été modifié directement** : toutes les écritures ont été
  livrées en diffs, à appliquer par le porteur.

---

## 9. Références

- `README.md` — méthode, gouvernance, tableau de couverture
- `PLAN-ACHEVEMENT.md` — plan général du chantier
- `annexes/inventaire-defauts.csv` — 724 défauts (plancher, non total)
- `annexes/rapport-application-*.md` — 16 rapports, un par lot appliqué
- `propositions/domaine-*.patch.json` — propositions sources, avec confiance et justification
- `annexes/decision-grande-carte.md` — décision motivée sur la forme à deux-points (lot 5d non écrit)
- `../audit/A8-synthese-et-point-de-reprise.md` — synthèse de la phase 1
- `../audit/A6-plan-phase-1.md` — lots 1 à 5, critères de validation
