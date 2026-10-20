# DOMAINE A — LOT 5 : POINTS LAISSÉS OUVERTS PAR LES LOTS 1 À 4 (§6.5, §7.4, §9.3, §13.3, §14.2, §17.5)

**Date :** 2026-10-20 — **Statut :** **PARTIELLEMENT APPLIQUÉ LE 2026-10-20** — 3 restitutions sur 6 (compte rendu en bas de document)
**Document source :** `Maths-vers-Informatiques/DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE.md`
**Inventaire de référence :** `domaine-A-inventaire-fragments.md`
**Contenu du lot :** 6 points — **3 restitutions proposées**, **1 hypothèse soumise**, **2 constats d'impossibilité**

> ## ⚠️ LOT APPLIQUÉ LE 2026-10-20 — TROIS POINTS SUR SIX
>
> **Appliquées :** A5-01 (§7.4), A5-02 / A5-03 (§6.5), A5-04 (§14.2).
> **Non appliquées, et c'est la conclusion :** A5-05 (§13.3), A5-06 (§17.5),
> A5-07 (§9.3).
>
> Diff livré : `livrables/domaine-A-lot5.gitdiff` — diff **incrémental**, à appliquer
> **après** les lots 1 à 4 ; éprouvé par `git apply --check` sur l'état post-lot 4
> reconstruit. **7 substitutions**, 5 haute / 2 moyenne. Journal :
> `domaine-A-lot5.journal.json`. Générateur : `build_lot_A_5.py`.
>
> Ce lot porte **autant sur ce qu'il refuse que sur ce qu'il applique** : deux points
> relèvent de la rédaction, une du pur inventement. Voir le compte rendu.

**Légende des actions :** **Combler** (emplacement vide explicite) · **Réattribuer** (fragment à déplacer) ·
**Reformater** (contenu en place, structure à reconstituer).

---

## Ce lot est différent des quatre premiers

Les lots 1 à 4 traitaient les 52 propositions validées. Celui-ci traite six points que
**l'investigation des lots précédents a fait apparaître**, et qui n'avaient pas été catalogués.

Ils ne se valent pas. Trois sont des restitutions que la source dicte ; une est une hypothèse
séduisante mais non établie ; deux sont des constats d'impossibilité, où **la seule conclusion
honnête est de ne rien faire**. Le lot les distingue explicitement.

---

## Ce qui a été vérifié avant de proposer quoi que ce soit

### Comment reconnaître un emplacement vide dans ce document

La question s'est posée au §6.5 : ce texte est-il vide, ou son contenu suit-il simplement ?

**Test empirique mené sur tout le document.** Toutes les suites d'espaces suivant un deux-points
ont été extraites et classées : **69 occurrences de 2 espaces, 42 de 3 espaces**. Puis ce qui suit
chaque occurrence a été lu.

| Signature | Ce qui suit | Interprétation |
|---|---|---|
| `Libellé :` + **2 espaces** + **un autre libellé** (`Énoncé :  Reconnaissance :`) | un second label | **EMPLACEMENT VIDE** |
| `Libellé :` + **2 espaces** + **une prose incohérente** avec le libellé | une phrase qui ne peut être le contenu | **EMPLACEMENT VIDE** |
| `Libellé :` + **2 espaces** + **un contenu cohérent** (liste, paragraphe) | le contenu annoncé | libellé suivi de son contenu — **pas un vide** |
| **3 espaces en pleine phrase** (`trouver un   tel que`) | — | **EMPLACEMENT VIDE** |
| `Libellé :` + **3 espaces** + **un contenu cohérent** | le contenu annoncé | libellé suivi de son contenu — **pas un vide** |

Cette grille est celle qui a déjà validé, sans le dire, les §10.1, §11.1, §17.5 et §7.4.
**Elle confirme que le §6.5 possède DEUX emplacements vides et non trois** — ce que
l'inventaire initial, trop rapide, avait laissé incertain.

---

## Restitutions proposées (3)

### A5-01 · §7.4 — L'invariant du maximum
**Action :** Réattribuer · **Fragment :** phrase égarée en tête du §8

**Source.** Le §8 s'ouvre sur une pile contenant, après le bloc de code factorielle :

> Après avoir examiné les `  ` premiers éléments, la variable `  ` max `  ` contient le maximum
> de ces éléments. `i`

Trois observations :

1. **Le §8 est « ENSEMBLES, FONCTIONS ET DÉNOMBRABILITÉ ».** Une phrase sur le maximum d'un
   tableau n'y a rien à faire.
2. **Le `i` est en fin de pile**, séparé de la phrase : c'est la signature d'un token déplacé,
   et sa place est le vide « les `  ` premiers éléments ».
3. **Le §7.4 présente l'emplacement vide correspondant** :
   « Dans une recherche du maximum d'un tableau, l'invariant peut affirmer : `  ` »
   — suivi de « Cet invariant permet de raisonner sur la correction du programme. », phrase
   distincte qui ne peut pas être le contenu de « peut affirmer : ».

**Proposition.** Porter la phrase au §7.4, avec le `i` remis à sa place :

> Dans une recherche du maximum d'un tableau, l'invariant peut affirmer :
> **« Après avoir examiné les `i` premiers éléments, la variable max contient le maximum de ces
> éléments. »**

**Justification.** L'emplacement vide nomme exactement le contenu : une *recherche du maximum
d'un tableau*, et un *invariant*. La phrase est verbatim dans la source — **rien n'est rédigé**.
`max` est en place dans la phrase (encadré d'espaces, non déplacé) ; seul `i` l'était.
Les sept tokens de la pile du §8 sont donc intégralement recasés.

---

### A5-02 et A5-03 · §6.5 — Le contre-exemple
**Action :** Combler · **Fragments :** orphelins conservés au §6.7

**Source.**

> **6.5 Contre-exemple** — Pour réfuter une affirmation universelle : il suffit de trouver un
> `   ` tel que : `  ` Réflexe : `   ` pour montrer qu'une propriété n'est pas toujours vraie,
> un seul contre-exemple suffit.

Appliquée à ce passage, la grille ci-dessus donne **deux emplacements vides** :

| Emplacement | Signature | Verdict |
|---|---|---|
| « trouver un `   ` tel que » | 3 espaces en pleine phrase | **vide** |
| « tel que : `  ` Réflexe : » | 2 espaces puis un autre libellé | **vide** |
| « Réflexe : `   ` pour montrer… » | 3 espaces puis un contenu cohérent | contenu — **pas un vide** |

**Proposition.** Porter `a` dans le premier et `¬P(a)` dans le second :

> il suffit de trouver un **`a`** tel que : **`¬P(a)`**

**Justification.** Ces deux tokens sont actuellement conservés comme non rattachés au §6.7,
section des règles d'inférence, où ils n'ont aucune place : ni `a` ni `¬P(a)` ne sont une règle.
Le §6.5 est la section du contre-exemple, et sa phrase décrit exactement le schéma dont ils sont
les termes. La source elle-même désigne le second : « tel que : `  ` » appelle une propriété
niée.

⚠️ **Réserve, et elle est maintenue.** Le troisième orphelin, **`∀x, P(x)`, n'a pas d'emplacement**.
Le compte est donc *deux tokens pour deux emplacements* — il tombe juste — mais **un token reste
sans destination**. Il demeure conservé et signalé. On ne le case pas en force : l'insérer
devant « universelle : » reviendrait à supposer un vide que la grille n'atteste pas.

---

### A5-04 · §14.2 — L'exemple de grammaire
**Action :** Réattribuer · **Fragment :** productions grammaticales égarées en fin de §14.3

**Source.**

> **14.2 Grammaires formelles** — … **Exemple conceptuel :** `  ` Une grammaire réelle doit aussi
> préciser ses symboles terminaux…
>
> **14.3 Automates finis** — … Ils servent notamment à reconnaître des langages réguliers.
> `Expression → Expression + Terme Expression → Terme Terme   → nombre`

**Proposition.** Porter les trois productions dans l'emplacement « Exemple conceptuel : » du §14.2 :

```
Expression → Expression + Terme
Expression → Terme
Terme → nombre
```

**Justification.** Trois raisons convergent :

1. **L'emplacement du §14.2 est vide** : « Exemple conceptuel : » est suivi d'une *mise en garde*
   (« Une grammaire réelle doit aussi préciser… »), non d'un exemple — la grille classe ce cas
   comme vide.
2. **Le contenu est une grammaire** : trois productions, avec leurs symboles terminaux et non
   terminaux — c'est la définition même de l'exemple que §14.2 appelle.
3. **Il est égaré dans la section des automates finis**, où il coupe le paragraphe avant
   « Comment les reconnaître ? ». Rien de ce qui précède n'annonce des productions.

⚠️ **Réserve mineure :** la mise en forme (une production par ligne) est **proposée**. Le
fragment est à plat sur une ligne ; le retour à la ligne par production est le rendu usuel
d'une grammaire, il n'est pas attesté.

---

## Hypothèse soumise, non retenue (1)

### A5-05 · §13.3 — Les exemples de type produit et de type somme
**Action :** **aucune pour l'instant** · **Fragments :** §13.3 (pile) et §13.5 (en place)

**Source.**

> **13.3 Types algébriques** — Type produit : Regroupe plusieurs composants.
> **Exemple conceptuel :** `  ` Type somme : Représente une valeur choisie parmi plusieurs
> variantes. `Utilisateur = (nom, email, age)`
> **Exemple conceptuel :** `  ` Ces représentations sont utiles…
>
> **13.5 Types dépendants** — … **Exemple conceptuel :** `Résultat = Succès(valeur) | Échec(erreur)`
> Une fonction reçoit un vecteur de taille `n`…

**Ce qui est établi.** Le §13.3 possède **deux** emplacements vides (deux-espaces-puis-libellé,
et deux-espaces-puis-prose-incohérente). Et `Utilisateur = (nom, email, age)` est bien **en pile**
— il est suivi du marqueur de fin de pile.

**Ce qui ne l'est pas.** `Utilisateur = (nom, email, age)` est un **type produit**, mais la pile
où il gît se trouve **après** la description du type somme. Rien ne permet de trancher entre :

- (hypothèse A) il est l'exemple du type *produit*, et le second emplacement attendait un
  exemple de type *somme* ;
- (hypothèse B) il est l'exemple du type *somme*, et le premier emplacement attendait autre chose.

Une hypothèse séduisante existe — `Résultat = Succès(valeur) | Échec(erreur)`, qui est bien un
type **somme**, occupe l'emplacement « Exemple conceptuel : » du §13.5 *types dépendants*, où il
n'a guère de rapport, tandis que le §13.5 a reçu son vrai exemple (le vecteur de taille `n`)
depuis sa propre pile. Les deux exemples auraient donc dérivé. **Mais** : déplacer
`Résultat = …` viderait l'emplacement qu'il occupe actuellement, et rien n'atteste qu'il y soit
déplacé plutôt qu'à sa place.

**Décision : aucune restitution.** Consigner l'hypothèse. Deux emplacements vides restent vides
plutôt que d'être remplis par une supposition.

---

## Constats d'impossibilité (2)

### A5-06 · §17.5 — « Étape 3 — Implémentation conceptuelle »
**Action :** **aucune**

**Source.** L'étape 3 du §17.5 est vide. Son contenu naturel serait le pseudo-code qui se
trouve au §18 :

> `A ∧ R → P` **si authentifié ET autorisé: permettre l'accès sinon: refuser l'accès**

**Pourquoi rien n'est proposé.** Ce pseudo-code **ne porte aucune signature de déplacement** :
il est en prose continue, espacement normal, et **il est cohérent là où il est** — le §18
l'utilise comme illustration du raisonnement symbolique, immédiatement après avoir refusé
d'interpréter « SPA ». Le déplacer reviendrait à **appauvrir le §18 pour combler le §17.5**, sur
la seule foi d'une ressemblance.

**Consigné, non appliqué.** Si le porteur estime que l'étape 3 doit être remplie, la décision
lui revient : c'est alors une **rédaction**, pas une restauration.

---

### A5-07 · §9.3 — Les deux `n` du paradoxe de Russell
**Action :** **aucune** — confirme A3-10

**Source.** Le fragment est inséré dans une liste à puces du §9.3, entre « les définitions
autoréférentielles ; » et « les systèmes formels ; » :

> … les définitions autoréférentielles ; `n   n` les systèmes formels ; …

**État.** Le fragment se réduit à deux occurrences de la lettre `n`. Le symbole qui les reliait
— vraisemblablement `∉` — **est perdu** : il ne figure dans aucun fragment du document.

**Aucune restitution.** Rétablir `x ∉ x` reviendrait à inventer le symbole manquant, ce que la
règle du chantier interdit. **La perte est formelle, elle n'est pas conceptuelle** : le paradoxe
est correctement décrit en prose au §9.2 (« l'ensemble des ensembles qui ne se contiennent pas
eux-mêmes »).

---

## Récapitulatif du lot 5

| Point | Nature | Décision |
|---|---|---|
| A5-01 · §7.4 | réattribution — emplacement vide nommant son contenu | **restitution** |
| A5-02 / A5-03 · §6.5 | comblement — 2 emplacements, 2 tokens | **restitution** |
| A5-04 · §14.2 | réattribution — grammaire égarée chez les automates | **restitution** |
| A5-05 · §13.3 | deux emplacements, affectation non tranchable | **hypothèse, non retenue** |
| A5-06 · §17.5 | contenu plausible mais non déplacé | **aucune — ce serait une rédaction** |
| A5-07 · §9.3 | symbole relationnel perdu | **aucune — ce serait une invention** |

⚠️ **Points soumis à l'arbitrage du porteur :**
1. **A5-04** — la mise en forme une-production-par-ligne est proposée, non attestée.
2. **A5-05** — trancher ou non l'hypothèse des deux exemples dérivés.
3. **A5-06** — souhaite-t-on *rédiger* l'étape 3 du §17.5 ? Ce n'est plus de la restauration.

---

**Rien de ce lot n'a été appliqué.**
---

## Compte rendu d'application (2026-10-20)

### Ce qui a été appliqué

| Point | Section | Effet |
|---|---|---|
| **A5-01** | §7.4 ← §8 | l'invariant du maximum d'un tableau, dont la phrase avait dérivé en tête du §8 |
| **A5-02 / A5-03** | §6.5 | `a` et `¬P(a)` dans les deux emplacements du contre-exemple |
| **A5-04** | §14.2 ← §14.3 | les productions grammaticales, égarées chez les automates finis |

**7 substitutions, 5 haute / 2 moyenne.** Volume : 78 767 → **78 849** caractères.
Mojibake 0. Diagnostic préalable 7/7.

### Ce qui n'a PAS été appliqué, et pourquoi c'est la conclusion

| Point | Raison |
|---|---|
| **A5-05** · §13.3 | Deux emplacements vides, **affectation non tranchable**. `Utilisateur = (nom, email, age)` est un type *produit* mais gît dans une pile située **après** la description du type *somme*. L'hypothèse d'un double dérapage — le type somme attendant `Résultat = Succès(valeur) \| Échec(erreur)`, aujourd'hui au §13.5 — est séduisante, mais la déplacer viderait l'emplacement qu'elle occupe. **Rien n'est tranché, rien n'est appliqué.** |
| **A5-06** · §17.5 | Le pseudo-code du §18 **ne porte aucune signature de déplacement** : prose continue, espacement normal, et il est **cohérent là où il est**. Le déplacer appauvrirait le §18 pour combler le §17.5. Ce serait une **rédaction**, pas une restauration. |
| **A5-07** · §9.3 | Le symbole qui reliait les deux `n` est **perdu**. Rétablir `x ∉ x` serait une **invention**. Confirme A3-10. |

Ces trois points restent donc **en l'état dans le document**. Les deux emplacements
vides du §13.3, l'étape 3 du §17.5 et le fragment `n   n` du §9.3 sont intacts —
vérifié après application.

### La grille qui a permis de compter les emplacements vides

La question se posait au §6.5 : le texte après un deux-points est-il un contenu, ou
manque-t-il ? **Test empirique sur tout le document** : toutes les suites d'espaces
suivant un deux-points ont été extraites — **69 occurrences de 2 espaces, 42 de 3** —
et ce qui suit chacune a été lu.

| Signature | Verdict |
|---|---|
| `Libellé :` + 2 espaces + **un autre libellé** | **emplacement vide** |
| `Libellé :` + 2 espaces + **une prose incohérente** avec le libellé | **emplacement vide** |
| `Libellé :` + 2 espaces + **un contenu cohérent** | libellé suivi de son contenu |
| **3 espaces en pleine phrase** | **emplacement vide** |
| `Libellé :` + 3 espaces + **un contenu cohérent** | libellé suivi de son contenu |

**Conséquence : le §6.5 possède DEUX emplacements vides, pas trois.** L'inventaire
initial, trop rapide, était resté incertain ; l'estimation « trois tokens pour deux
emplacements » est confirmée, et le troisième orphelin `∀x, P(x)` demeure conservé
et signalé. Cette grille a déjà validé, sans être formulée, les §10.1, §11.1, §17.5
et §7.4 des lots précédents.

### Deux erreurs commises, détectées, corrigées

L'édition A5-01b a été montée deux fois de travers avant d'être correcte :

1. **`entre()` conserve ses deux marqueurs.** En prenant « Après avoir examiné »
   comme marqueur amont, la phrase restait en tête du §8, collée au titre de section.
2. **`retirer()`, ajoutée au moteur pour ce cas, supprime AUSSI le marqueur amont.**
   Elle a emporté la fin du bloc de code factorielle.

La zone a été **réparée à la main**, puis le constructeur a été **rejoué debout**
depuis la sauvegarde pré-lot-5 et **comparé octet par octet** à l'état réparé :
**identiques**. Le montage retenu est `entre()` avec un marqueur amont qui doit
survivre. Les deux fonctions sont désormais documentées l'une par rapport à l'autre
dans `lot_commun.py`.

### Vérifications

| Contrôle | Résultat |
|---|---|
| Diagnostic préalable (`python3 lot_commun.py build_lot_A_5.py`) | 7/7 sous-chaînes uniques |
| Mojibake | 0 |
| `git apply --check` sur l'état post-lot 4 reconstruit | OK |
| Diff incrémental livré | 54 lignes, `livrables/domaine-A-lot5.gitdiff` |
| Chaîne de volumes | 77 970 → 78 776 → 78 789 → 78 758 → 78 767 → **78 849** |
| **Rejeu intégral** depuis la sauvegarde | **identique à l'octet près** |
| Points non retenus | §13.3, §17.5, §9.3 vérifiés **intacts** |
| Couverture des autres documents | 1 146 blocs, 78 sans contenu, **écart nul** |

### État du document A après cinq lots

| Lot | Sections | Substitutions | Commit |
|---|---|---:|---|
| 1 | §2–§4 | 11 | `fa45e60` |
| 2 | §5–§7 | 12 | `9828faf` |
| 3 | §8, §10 | 16 | `8ad13bc` |
| 4 | §11–§18 | 19 | `b8ee095` |
| 5 | points ouverts | 7 | ce commit |
| **Total** | | **65** | |

Il reste, volontairement en l'état : deux emplacements vides au §13.3, l'étape 3 du
§17.5, le fragment `n   n` du §9.3, le `P → Q` du §30, le `∀x, P(x)` du §6.7, et
divers emplacements vides sans token disponible (§15.3, §6.7).
