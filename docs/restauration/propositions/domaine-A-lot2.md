# DOMAINE A — LOT 2 : PRÉDICATS, DÉMONSTRATION, INDUCTION (§5, §6, §7)

**Date :** 2026-10-20 — **Statut :** **PROPOSITION — non appliquée, en attente de validation**
**Document source :** `Maths-vers-Informatiques/DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE.md`
**Inventaire de référence :** `domaine-A-inventaire-fragments.md`
**Contenu du lot :** 13 propositions — **7 T1**, **6 T2**, 0 T3

**Légende des actions :** **Combler** (emplacement vide explicite) · **Réattribuer** (fragment à déplacer) ·
**Reformater** (contenu en place, structure à reconstituer).

---

## T1 — Palier attesté (7 propositions)

### A2-01 · §5.2 — Exemple du quantificateur universel
**Action :** Combler · **Fragments :** #19, #20, #21 (@13905, @13923, @13942)

**Source.** Le §5.2 présente un emplacement vide suivi de sa propre glose :

> **5.2 Quantificateurs et portée**
> Exemple : _  Lecture : **tout étudiant possède la propriété « avoir accès »**, selon l'interprétation
> donnée.

Le fragment, trouvé deux sections plus loin à la fin du §5.4, se lit — une fois recomposés les caractères
accentués déplacés (`tudiant` + `E ˊ` → `Étudiant`, `AAcc s` + `e ˋ` → `Accès`) :

> `∀x (` · `(x) → E ˊ` · `s ( x` · `e ˋ` → soit `∀x (Étudiant(x) → Accès(x))`

**Proposition.** Porter `∀x (Étudiant(x) → Accès(x))` dans l'emplacement « Exemple : » du §5.2.

**Justification.** La glose qui suit l'emplacement vide — « tout étudiant possède la propriété « avoir accès
» » — est la traduction littérale de `∀x (Étudiant(x) → Accès(x))`. **Le texte de la source dicte
l'appariement** : ce n'est pas une inférence. La recomposition des accents est mécanique (`É` déplacé en
fin de mot, `è` déplacé de même), et le même artefact se vérifie ailleurs dans le document (§5.1, §16.5).

⚠️ **Seule réserve :** les noms de prédicats sont reconstitués par recollement des accents. La forme
`Étudiant(x) → Accès(x)` est certaine ; l'orthographe exacte des deux noms l'est très hautement mais
repose sur ce recollement.

---

### A2-02 · §5.3 — Loi de négation du quantificateur universel
**Action :** Combler · **Fragment :** #22 (@13951)

**Source.** Le §5.3 énonce la loi **en prose** mais n'en donne pas la forme :

> **5.3 Négation des quantificateurs**
> Exemple : « Tous les fichiers sont valides » est nié par : « Il existe au moins un fichier qui n'est pas
> valide. »

Fragment : `¬∀x P(x) ≡ ∃x ¬P(x)`.

**Proposition.** Porter `¬∀x P(x) ≡ ∃x ¬P(x)` dans le §5.3, comme forme de l'exemple énoncé en prose.

**Justification.** L'exemple en prose est l'instanciation exacte de la loi : « tous les fichiers sont
valides » = `∀x P(x)`, nié = `∃x ¬P(x)`. La forme est déterminée par le texte.

---

### A2-03 · §5.3 — Loi de négation du quantificateur existentiel
**Action :** Combler · **Fragment :** #22 (@13951)

**Proposition.** Porter `¬∃x P(x) ≡ ∀x ¬P(x)` dans le §5.3, comme loi duale de A2-02.

**Justification.** La forme est présente dans le fragment et constitue la duale exacte de A2-02. ⚠️ **Réserve :**
contrairement à A2-02, la source ne l'instancie pas en prose. Sa présence dans le §5.3 est une inférence par
symétrie — très forte, mais une inférence. Si le porteur préfère la réserve, elle peut être renvoyée en T2.

---

### A2-04 · §6.7 — Forme du modus ponens
**Action :** Combler · **Fragment :** #24 (@16068)

**Source.** Le tableau du §6.7 possède une colonne « Forme » **systématiquement vide** :

| Règle | Forme | Lecture |
|---|---|---|
| Modus ponens | _ | Si P et si P implique Q, alors Q |
| Modus tollens | _ | Si Q est faux, P ne peut être vrai |
| Introduction de ∧ | _ | Établir les deux |
| Élimination de ∧ | _ | Extraire une composante |
| Introduction de ∨ | _ | Une proposition vraie suffit |
| Élimination de ∨ | _ | …, avec les deux cas traités — Raisonner par cas |

Fragment : `P ,   P   →   Q   ⊢   Q`.

**Proposition.** Porter `P, P → Q ⊢ Q` dans la colonne « Forme » de la ligne « Modus ponens ».

**Justification.** La colonne est vide, la lecture est donnée, et le fragment fournit la forme canonique
correspondante. Appariement certain.

---

### A2-05 · §6.7 — Forme du modus tollens
**Action :** Combler · **Fragment :** #24

Fragment : `¬ Q ,   P   →   Q   ⊢ ¬ P`.

**Proposition.** Porter `¬Q, P → Q ⊢ ¬P` dans la colonne « Forme » de la ligne « Modus tollens ».

**Justification.** Identique à A2-04. La lecture « Si Q est faux, P ne peut être vrai » est la glose exacte
de cette forme.

---

### A2-06 · §6.7 — Forme de l'introduction de la conjonction
**Action :** Combler · **Fragment :** #24

Fragment : `∧   P   ,   Q   ⊢   P   ∧   Q`.

**Proposition.** Porter `P, Q ⊢ P ∧ Q` dans la colonne « Forme » de la ligne « Introduction de ∧ », et
combler l'en-tête vide « Introduction de _ » par `∧`.

**Justification.** La lecture « Établir les deux » est la glose de l'introduction de la conjonction ; le
fragment porte le `∧` qui manque à l'en-tête et la forme correspondante.

---

### A2-07 · §7.1 — Principe de récurrence
**Action :** Combler · **Fragments :** #25a, #26 (@17438, @17572)

**Source.** Le §7.1 énonce le principe avec **trois emplacements vides** :

> 7.1 Principe de récurrence (induction mathématique)
> Pour démontrer une propriété _ pour tout entier _ , on établit :
> 1. Initialisation : _ .
> 2. Hérédité : _ .
> 3. Conclusion : _ est vraie pour tout _ .

Fragment (recomposé à partir de #25a et #26, qui se suivent) :

> `P(n)` `n ≥ n₀` · `P(n₀)` · `P(n) → P(n + 1)` · `P(n)` `n ≥ n₀` · `P(n)` `n`

**Proposition.**

| Emplacement | Formule |
|---|---|
| « une propriété _ pour tout entier _ » | `P(n)` … `n` |
| 1. Initialisation | `P(n₀)` |
| 2. Hérédité | `P(n) → P(n + 1)` |
| 3. Conclusion | `P(n)` est vraie pour tout `n ≥ n₀` |

**Justification.** Les trois emplacements sont explicitement vides, et le fragment contient exactement les
trois formules attendues par le principe d'induction — initialisation, hérédité, conclusion — plus la clause
de portée `n ≥ n₀`. Aucune autre répartition n'est possible : les formules sont typées par leur position
dans l'énoncé.

⚠️ **Note de méthode.** C'est le cas d'école du palier T1 : le contenu manque, l'emplacement est connu et
structuré. La restitution est une lecture.

---

## T2 — Palier concordant (6 propositions)

### A2-08 · §5.1 — Exemple de prédicat unaire
**Action :** Combler · **Fragment :** #16 (@12906)

**Source.** « 5.1 Qu'est-ce que c'est ? … Exemples : _ » suivi d'un fragment dégradé :

> `tudiant ( x ) E ˊ`

**Proposition.** Porter `Étudiant(x)` dans l'emplacement « Exemples : » du §5.1.

**Justification.** Recollement des accents (`tudiant` + `É` → `Étudiant`). Le même prédicat réapparaît en
§5.2 (proposition A2-01), ce qui confirme le vocabulaire. ⚠️ **Réserve :** l'emplacement « Exemples : » du
§5.1 pourrait tout aussi bien recevoir les trois prédicats A2-08 à A2-10.

---

### A2-09 · §5.1 — Exemple de prédicat binaire
**Action :** Combler · **Fragment :** #17 (@12925)

Fragment : `Inscrit ( x ,   c )` (non dégradé).

**Proposition.** Porter `Inscrit(x, c)` dans l'emplacement « Exemples : » du §5.1.

**Justification.** Prédicat binaire, non dégradé, contigu aux deux autres. ⚠️ Même réserve qu'en A2-08.

---

### A2-10 · §5.1 — Exemple de prédicat binaire (second)
**Action :** Combler · **Fragment :** #18 (@12948)

Fragment : `Sup rieur ( x ,   y ) e ˊ`.

**Proposition.** Porter `Supérieur(x, y)` dans l'emplacement « Exemples : » du §5.1.

**Justification.** Recollement de l'accent (`Sup rieur` + `é` → `Supérieur`). ⚠️ Même réserve.

---

### A2-11 · §5.1 — Formule propositionnelle composée
**Action :** Combler · **Fragment :** #15 (@12863)

Fragment : `( P   ∨   Q ) ∧ (¬ P   ∨   R )`.

**Proposition.** Porter `(P ∨ Q) ∧ (¬P ∨ R)` dans l'emplacement « Exemples : » du §5.1, comme illustration
d'une formule composée.

**Justification.** La formule est intacte et non dégradée. ⚠️ **Réserve :** elle pourrait appartenir au §4.5
« Formes normales » — c'est une conjonction de clauses, c'est-à-dire une forme normale conjonctive. Les deux
destinations sont plausibles ; je propose le §5.1 par contiguïté.

---

### A2-12 · §6.2 — Contraposée
**Action :** Réattribuer · **Fragment :** #23 (@15050)

**Source.** Le fragment gît à la fin du §6.3, après « Signature : « Supposons le contraire… » » :

> `P   →   Q` · `P   Q` · `P   Q` · `P   →   Q` · `¬ Q   → ¬ P`

**Proposition.** Déplacer l'ensemble vers le **§6.2 « Contraposée »**, dont l'énoncé est privé de forme :

> 6.2 Contraposée — _ est logiquement équivalente à l'implication initiale.

Soit : `P → Q` ≡ `¬Q → ¬P`.

**Justification.** Le fragment se termine par `¬Q → ¬P`, qui est la contraposée : il appartient donc au
§6.2, et non au §6.3 où il a échoué. Le §6.2 possède un emplacement vide en tête d'énoncé, que `P → Q`
vient combler. ⚠️ **Réserve :** les tokens intermédiaires `P Q` `P Q` sont les en-têtes de colonnes d'une
petite table de vérité comparant `P → Q` et `¬Q → ¬P` ; leur restitution tabulaire est proposée mais la
forme exacte de cette table n'est pas attestée.

---

### A2-13 · §6.7 — Formes restantes des règles d'inférence
**Action :** Réattribuer · **Fragment :** #25b (@17438)

**Source.** Trois formes ont été entraînées avec le fragment d'induction jusqu'à la fin du §7.2 :

> `∧   P   ∧   Q   ⊢   P` · `∨   P   ⊢   P   ∨   Q` · `∨   P   ∨   Q   ⊢`

**Proposition.** Ramener au §6.7 et combler les lignes restantes du tableau :

| Règle | Forme | Lecture |
|---|---|---|
| Élimination de ∧ | `P ∧ Q ⊢ P` | Extraire une composante |
| Introduction de ∨ | `P ⊢ P ∨ Q` | Une proposition vraie suffit |
| Élimination de ∨ | `P ∨ Q, ¬P ⊢ Q` | …, avec les deux cas traités — Raisonner par cas |

**Justification.** Les trois règles manquantes du tableau §6.7 sont exactement l'élimination de ∧,
l'introduction de ∨ et l'élimination de ∨ ; le fragment fournit les trois formes, dans cet ordre.
⚠️ **Réserve :** la troisième forme est **tronquée** dans la source (`P ∨ Q ⊢` sans second membre). Je
propose `⊢ Q` par analogie avec la règle classique d'élimination de la disjonction, mais **c'est une
restitution partielle** : le second membre n'est pas attesté. Si le porteur la refuse, elle doit être
consignée comme inconnue plutôt que complétée.

---

## Récapitulatif du lot 2

| Palier | Nombre | Nature |
|---|---:|---|
| T1 | 7 | 3 comblements dictés par la glose de la source (A2-01, A2-02, A2-07) · 3 comblements de colonnes vides (A2-04 → A2-06) · 1 loi duale (A2-03) |
| T2 | 6 | 4 comblements par contiguïté (A2-08 → A2-11) · 2 réattributions (A2-12, A2-13) |
| **Total** | **13** | |

⚠️ **Trois points soumis à l'arbitrage du porteur :**
1. **A2-03** — la loi duale n'est pas instanciée dans la source ; T1 ou T2 à arbitrer.
2. **A2-13** — la troisième forme est tronquée ; compléter par la règle classique, ou consigner comme
   inconnue ?
3. **A2-08 à A2-11** — quatre candidats pour un seul emplacement « Exemples : » du §5.1 ; l'ordre et la
   répartition sont proposés, non attestés.

---

**Rien de ce lot n'a été appliqué.**
