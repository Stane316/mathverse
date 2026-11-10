# DOMAINE A — LOT 4 : CALCULABILITÉ, VÉRIFICATION, TYPES, APPLICATIONS (§11–§18, §30)

**Date :** 2026-10-20 — **Statut :** **APPLIQUÉ LE 2026-10-20** (compte rendu en bas de document)
**Document source :** `Maths-vers-Informatiques/DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE.md`
**Inventaire de référence :** `domaine-A-inventaire-fragments.md`
**Contenu du lot :** 13 propositions — **9 T1**, **3 T2**, **1 T3**

> ## ✅ LOT APPLIQUÉ LE 2026-10-20 (compte rendu en bas de document)
>
> **Statut : APPLIQUÉ.** Diff livré : `livrables/domaine-A-lot4.gitdiff` — diff
> **incrémental**, à appliquer **après** les lots 1, 2 et 3 ; éprouvé par
> `git apply --check` sur l'état post-lot 3 reconstruit. Journal :
> `domaine-A-lot4.journal.json`. Générateur : `build_lot_A_4.py`.
>
> **19 substitutions** sur **11 propositions**. Deux n'entraînent volontairement
> **aucune édition** (A4-05, A4-14). Une proposition supplémentaire a été ajoutée
> en cours de route (**A4-15**, §11.1) et une seconde (**A4-16**, §12.2) : deux
> emplacements vides que l'inventaire avait manqués.

**Légende des actions :** **Combler** (emplacement vide explicite) · **Réattribuer** (fragment à déplacer) ·
**Reformater** (contenu en place, structure à reconstituer).

---

## T1 — Palier attesté (9 propositions)

### A4-01 · §11.6 — Notation de la réduction
**Action :** Combler · **Fragment :** #38 (@29377)

**Source.**

> **11.6 Réduction de problèmes** — Selon le type de réduction, cela peut signifier que résoudre _
> permettrait de résoudre _ .

Fragment : `A   ≤   B` · `B` · `A`.

**Proposition.**

| Emplacement | Contenu |
|---|---|
| « résoudre _ » | `A` |
| « permettrait de résoudre _ » | `B` |
| Notation de la réduction | `A ≤ B` |

**Justification.** Deux emplacements vides et une notation, trois tokens dans le fragment. ⚠️ **Réserve :**
l'ordre du fragment (`A ≤ B`, puis `B`, puis `A`) ne suit pas l'ordre du texte (`A`, puis `B`). L'affectation
des deux slots est dictée par le sens (« résoudre A permettrait de résoudre B » est la signification même de
`A ≤ B`), mais l'inversion observée dans le fragment est **signalée et non expliquée**.

---

### A4-02 · §12.3 — Triplet de Hoare
**Action :** Réattribuer · **Fragment :** #39 (@30482)

**Source.** Le triplet apparaît à la fin de la section **12.2** :

> …retourner un élément dont la valeur est maximale. `{ P } C { Q }` `P` `C` `Q`

Or c'est la section **12.3** qui l'introduit :

> **12.3 Logique de Hoare** — La logique de Hoare est un système de raisonnement sur les programmes,
> **notamment à l'aide de triplets de Hoare**.

**Proposition.** Porter `{P} C {Q}` dans le §12.3, accompagné de sa légende : `P` = précondition,
`C` = commande, `Q` = postcondition.

**Justification.** Le §12.3 annonce explicitement les « triplets de Hoare » sans en donner un seul ; le
§12.2, qui traite des préconditions et postconditions, n'a pas vocation à porter le triplet. Le fragment
fournit le triplet **et** les trois lettres qui le composent, dans l'ordre `P C Q`.

⚠️ **Réserve :** les mots « précondition / commande / postcondition » sont attestés dans le document
(§12.2, §12.3) mais leur appariement aux trois lettres est **proposé** — il est conforme à la convention
universelle de la logique de Hoare.

---

### A4-03 · §12.2 — Précondition, commande, postcondition
**Action :** Combler · **Fragment :** #40 (@30636)

**Source.** La phrase du §12.2 présente **trois** emplacements vides :

> Si _ est vrai avant l'exécution de _ , et si celle-ci termine conformément au cadre de raisonnement,
> alors _ est vrai après.

Fragment : `P` · `C` · `Q`.

**Proposition.** Porter `P`, `C`, `Q` dans les trois emplacements, dans cet ordre.

**Justification.** Ordre du fragment conforme à l'ordre des slots, et cohérent avec A4-02. La phrase
décrit exactement la sémantique du triplet `{P} C {Q}`.

---

### A4-04 · §13.5 — Types dépendants
**Action :** Combler · **Fragment :** #41 (@35647)

**Source.**

> **13.5 Types dépendants** — … Une fonction reçoit un vecteur de taille _ et renvoie un vecteur de
> taille _ .

Fragment : `n` · `n`.

**Proposition.** Porter `n` dans les deux emplacements.

**Justification.** Deux emplacements vides, deux tokens, et la phrase décrit une fonction de `n` vers `n`.
⚠️ **Réserve mineure :** le second pourrait être `n + 1` ou `m` ; la source ne permet pas de trancher, mais
`n` est le seul token disponible dans le fragment.

---

### A4-05 · §14.7 — Expression arithmétique
**Action :** **Reformater** · **Fragment :** #42 (@39221)

⚠️ **Ce fragment n'est pas déplacé.** Il est à sa place, à la fin du §14.7.

**Source.** `2 + 3 × 4`

**Proposition.** Aucune restitution de contenu. Signaler uniquement que l'expression illustre la priorité
des opérations — judgement qui relève de l'édition, pas de la restauration.

**Justification.** Classé T1 par prudence de comptage, mais **ne donne lieu à aucune modification**.

---

### A4-06 · §15.3 — Nombre d'affectations
**Action :** Combler · **Fragment :** #43 (@42689)

**Source.**

> **15.3 Énumération exhaustive des affectations** — Pour _ variables propositionnelles, il existe _
> affectations possibles.

Fragment : `n` · `2 n`.

**Proposition.** Porter `n` dans le premier emplacement et `2ⁿ` dans le second.

**Justification.** Deux emplacements vides, deux tokens, et la phrase qui suit — « le nombre d'affectations
croît exponentiellement » — confirme `2ⁿ`. Le second token du fragment est la forme dégradée de l'exposant.

---

### A4-07, A4-08, A4-09 · §16.5 — Règle d'accès
**Action :** Reformater · **Fragments :** #45 (@49040), #46 (@49064), #47 (@49097)

**Source.** En fin de §16.5, avec les accents déplacés :

> `Authentifi   ( u ) ∧ e ˊ   Autoris   ( u ,   r ) → e ˊ   Acc sP ermis ( u ,   r ) e ˋ`

**Proposition.** Recomposer en une seule formule, placée en fin de §16.5 :

```
Authentifié(u) ∧ Autorisé(u, r) → AccèsPermis(u, r)
```

**Justification.** Les trois fragments sont **contigus** et non déplacés : seule la décomposition des
accents les a morcelés. Le recollement est mécanique :
`Authentifi` + `é` → `Authentifié` ; `Autoris` + `é` → `Autorisé` ; `Acc sP ermis` + `è` → `AccèsPermis`.
La structure logique (`∧` puis `→`) est intacte et n'est pas modifiée.

⚠️ **Réserve mineure :** l'orthographe `AccèsPermis` résulte d'un recollement de trois morceaux ; la
casse exacte (espace ou non, majuscule interne) n'est pas attestée.

---

### A4-10 · §11.3 — *[vacat]*

*(Cette position est laissée vacante : le fragment #36/#37, initialement rattaché au §11.3 par sa position,
a été réattribué au §10.7 en A3-06/A3-07 du lot 3.)*

---

## T2 — Palier concordant (3 propositions)

### A4-11 · §15.6 — Exemple d'unification
**Action :** Réattribuer · **Fragment :** #44 (@44843)

**Source.** Le fragment gît à la fin du §15.7 (chaînage), juste avant son schéma :

> Limites : gestion des cycles… `f(x, 3) et f(2, y)` `x = 2` `y = 3` **Faits connus ↓ Règles
> applicables ↓ …**

Or `f(x, 3)` et `f(2, y)` sont l'exemple canonique de l'**unification**, objet du §15.6.

**Proposition.** Déplacer vers le §15.6 « Unification » :

> Exemple : unifier `f(x, 3)` et `f(2, y)` donne la substitution `x = 2`, `y = 3`.

**Justification.** Le §15.6 traite de l'unification ; le §15.7, du chaînage. L'exemple appartient au
premier. Le fragment fournit les deux termes et la substitution complète. ⚠️ **Réserve :** le verbe « unifier
» et le mot « substitution » sont **proposés** — la source ne les porte pas à cet endroit.

---

### A4-12 et A4-13 · §17.5 / §18 — Règle d'accès Web
**Action :** Combler · **Fragments :** #48 (@52638), #49 (@53601)

**Source.** En §17.5 :

> …commande appartient au client ALORS autoriser l'accès à la ressource. **Règle :** _ Étape 2 —
> Reconnaissance — On rencontre : deux conditions booléennes combinées…

et en fin de §18 :

> `A ∧ R → P` **si authentifié ET autorisé : permettre l'accès sinon : refuser l'accès**

Le fragment #48 fournit les trois tokens : `A` · `R` · `P`.

**Proposition.** Porter `A ∧ R → P` dans l'emplacement « Règle : » du §17.5, avec la légende :
`A` = authentifié, `R` = ressource autorisée, `P` = accès permis.

**Justification.** Le §17.5 énonce la règle en prose (« SI l'utilisateur est authentifié ET si la commande
appartient au client ALORS autoriser l'accès ») puis présente un emplacement « Règle : » vide, et le §18
porte la forme `A ∧ R → P` immédiatement suivie du pseudo-code qui l'implémente. Les trois tokens de #48
sont les trois propositions de la règle.

⚠️ **Réserves :**
1. La légende (`A` = authentifié, `R` = autorisé, `P` = permis) est **proposée** ; elle est cohérente avec
   le §16.5 (A4-07) qui utilise le même vocabulaire, mais n'est pas attestée telle quelle.
2. Le fragment #49 pourrait aussi rester en §18, où il joue le rôle d'exemple de l'IA symbolique. **Les deux
   destinations sont plausibles** ; je propose le §17.5 parce que c'est là qu'est l'emplacement vide.

---

## T3 — Non proposé (1 notice d'inconnu)

### A4-14 · §30 — Question de maîtrise
**Action :** **aucune** · **Fragment :** #62 (@71743)

**Source.** Le fragment est inséré entre les questions 18 et 19 de la liste de maîtrise :

> 18. Qu'est-ce que la diagonalisation permet de démontrer ? **`P → Q`** 19. Quelle différence existe-t-il
> entre le théorème de complétude de Gödel et ses théorèmes d'incomplétude ?

**État.** Le fragment `P → Q` ne correspond à aucune des questions encadrantes : la 18 porte sur la
diagonalisation, la 19 sur Gödel. Aucune question de la liste ne porte explicitement sur l'implication.

**Proposition :** **aucune restitution.** Consigner comme inconnu.

**Justification.** L'affectation serait une pure supposition. La liste du §30 comporte au moins vingt
questions : sans indice supplémentaire, attribuer `P → Q` à l'une d'elles reviendrait à inventer.

---

## Récapitulatif du lot 4

| Palier | Nombre | Nature |
|---|---:|---|
| T1 | 9 | 5 comblements (A4-01, A4-03, A4-04, A4-06, A4-07/08/09) · 1 réattribution (A4-02) · 1 vacat (A4-10) · 1 sans modification (A4-05) |
| T2 | 3 | 1 réattribution (A4-11) · 2 comblements avec légende proposée (A4-12, A4-13) |
| T3 | 1 | notice d'inconnu — **aucune restitution** |
| **Total** | **13** | |

⚠️ **Points soumis à l'arbitrage du porteur :**
1. **A4-01** — l'ordre inversé du fragment n'est pas expliqué ; l'affectation proposée repose sur le sens,
   pas sur l'ordre.
2. **A4-02 / A4-03** — la légende « précondition / commande / postcondition » est proposée.
3. **A4-07/08/09** — la casse de `AccèsPermis` n'est pas attestée.
4. **A4-12 / A4-13** — deux destinations plausibles pour `A ∧ R → P` (§17.5 ou §18).

---

**Rien de ce lot n'a été appliqué.**
---

## Compte rendu d'application (2026-10-20)

### Deux réserves de la proposition levées par la source

La proposition présentait comme **proposé** l'appariement des lettres à leur rôle.
C'était trop prudent : **la source porte elle-même la légende**, accolée à chaque
emplacement vide.

| Section | Ce que la source écrit | Conséquence |
|---|---|---|
| §12.2 | « _ : précondition ; _ : commande ou programme ; _ : postcondition. » | `P`/`C`/`Q` **attestés** |
| §17.5 | « _ : utilisateur authentifié ; _ : utilisateur autorisé ; _ : accès permis. » | `A`/`R`/`P` **attestés** |

**Ces propositions passent de T2 à T1. Aucun appariement n'est inventé : il est
donné par le texte.** Le lot est plus solide que la proposition initiale.

### Une proposition ajoutée en cours de route

**A4-15 — §11.1 « Une question typique : » était vide, et l'inventaire l'avait
manqué.** Le §11.3 portait une phrase entière, insérée entre « tandis » et
« que », qui définit la **calculabilité** et non la semi-décidabilité. C'est
exactement la question typique du §11.1. Emplacement vide explicite **et** phrase
coupée en deux : les deux preuves réunies. **Le §11.3 est ressoudé**, ce que le
lot 3 avait laissé en attente précisément parce que cette destination relevait du
§11, donc du lot 4.

### Non-perte : 31 tokens suivis un à un

| Fragment gisant | Tokens | Destination |
|---|---|---|
| §11.3 | une phrase entière | §11.1 |
| §11.6 | `A ≤ B` · `B` · `A` | §11.6 (forme, puis les deux emplacements) |
| §12.2 | `{P} C {Q}` | §12.3 |
| §12.2 | `P` · `C` · `Q` | §12.2 ligne de légende |
| §12.2 | `P` · `C` · `Q` | §12.2 phrase « Si … alors » |
| §13.5 | `n` · `n` | §13.5 |
| §15.3 | `n` · `2ⁿ` | §15.3 |
| §15.7 | `f(x, 3) et f(2, y)` · `x = 2` · `y = 3` | §15.6 |
| §16.5 | formule décomposée | §16.5 (recomposée) |
| §17.5 | `A` · `R` · `P` | §17.5 modélisation |
| §18 | `A ∧ R → P` | §17.5 « Règle : » |

**Un seul token n'a pas de destination établie :** le `n` orphelin du §15.6. Il
pourrait aussi bien revenir au §15.3 (« croît exponentiellement avec _ »). Il est
**conservé et signalé**, non supprimé.

### Réserve maintenue sur A4-13

Deux destinations étaient plausibles pour `A ∧ R → P`. Le §17.5 est retenu parce
que c'est là qu'est l'emplacement vide. **Conséquence assumée :** le pseudo-code du
§18 — « si authentifié ET autorisé : permettre l'accès sinon : refuser l'accès » —
se retrouve séparé de sa formule. Il est conservé tel quel. Si le porteur préfère
laisser la formule au §18, les éditions A4-13 et A4-13b sont à annuler ensemble.

**Hypothèse consignée, non appliquée :** « Étape 3 — Implémentation conceptuelle »
du §17.5 est vide, et ce pseudo-code en serait le contenu naturel. Renvoi au lot 5.

### Aucune restitution, et c'est la conclusion

| Proposition | Raison |
|---|---|
| **A4-05** · `2 + 3 × 4` | **pas déplacé**, il est à sa place. Aucune modification : juger de la priorité des opérations relève de l'édition, pas de la restauration. |
| **A4-14** · `P → Q` au §30 | inséré entre les questions 18 et 19, il ne correspond à aucune des deux. L'attribuer à l'une des vingt questions reviendrait à **inventer**. Rien n'est appliqué. |

### Trois emplacements vides repérés hors périmètre, non traités

§13.3 et §14.2 (« Exemple conceptuel : » vides) et §17.5 « Étape 3 ». Ils sont
consignés pour un lot 5 : les traiter ici aurait supposé des attributions que rien
n'atteste.

### Vérifications

| Contrôle | Résultat |
|---|---|
| Diagnostic préalable (`python3 lot_commun.py build_lot_A_4.py`) | 19/19 sous-chaînes uniques |
| Mojibake | 0 |
| `git apply --check` sur l'état post-lot 3 reconstruit | OK |
| Diff incrémental livré | 62 lignes, `livrables/domaine-A-lot4.gitdiff` |
| Chaîne de volumes | 77 970 → 78 776 → 78 789 → 78 758 → **78 767** |
| Relecture in situ | §11.1, §11.3, §11.6, §12.2, §12.3, §15.6, §16.5, §17.5 relus |
