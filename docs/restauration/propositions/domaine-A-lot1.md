# DOMAINE A — LOT 1 : VOCABULAIRE, NOTATIONS, TABLES DE VÉRITÉ (§2, §3, §4)

**Date :** 2026-10-20 — **Statut :** **PROPOSITION — non appliquée, en attente de validation**
**Document source :** `Maths-vers-Informatiques/DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE.md`
**Inventaire de référence :** `domaine-A-inventaire-fragments.md`
**Contenu du lot :** 16 propositions — **9 T1**, **7 T2**, 0 T3

**Légende des actions :**
- **Combler** — la source présente un emplacement vide explicite ; on y porte le fragment.
- **Réattribuer** — le fragment n'est pas à sa place ; on le déplace vers sa section d'origine.
- **Reformater** — le contenu est déjà à sa place ; seule la structure (tableau) est à reconstituer.

---

## T1 — Palier attesté (9 propositions)

### A1-01 · §3.1 — Colonne « Symbole » du tableau des connecteurs
**Action :** Combler · **Fragment :** #4a (@8630)

**Source.** Le tableau de la section 3.1 conserve ses colonnes « Nom » et « Lecture » mais sa colonne
« Symbole » est vide :

> Négation · Non · Conjonction · et · Disjonction inclusive · ou · Implication · Si …, ·
> alors · Équivalence · … si et seulement si

Le fragment #4a fournit exactement les valeurs manquantes, dans le même ordre :

> `¬P` · `P ∧ Q` · `P ∨ Q` · `P → Q` · `P ↔ Q` · `⊤` · `⊥`

**Proposition.**

| Nom | Lecture | Symbole |
|---|---|---|
| Négation | Non | `¬P` |
| Conjonction | et | `P ∧ Q` |
| Disjonction inclusive | ou | `P ∨ Q` |
| Implication | Si …, alors | `P → Q` |
| Équivalence | … si et seulement si | `P ↔ Q` |

Les deux tokens restants du fragment, `⊤` et `⊥`, ne trouvent pas de ligne dans ce tableau. Ils sont
proposés en **A1-02**.

**Justification.** Le fragment est inséré entre les lignes « Universel · Pour tout » et
« Existentiel · Il existe au moins un » du tableau **3.2** : il n'appartient donc pas au 3.2. Or le 3.1
possède une colonne vide et le fragment énumère exactement cinq connecteurs dans l'ordre du tableau 3.1.
Ordre, nombre et nature concordent.

---

### A1-02 · §3.1 — Constantes `⊤` et `⊥`
**Action :** Combler · **Fragment :** #4a (reste)

**Proposition.** Ajouter en fin du tableau 3.1 deux lignes :

| Nom | Lecture | Symbole |
|---|---|---|
| Vrai (top) | toujours vrai | `⊤` |
| Faux (bottom) | toujours faux | `⊥` |

**Justification.** `⊤` et `⊥` sont présents dans le fragment et ne correspondent à aucune des cinq lignes
du tableau 3.1. La section 3.1 est « Les connecteurs propositionnels » ; y ranger les deux constantes est
l'affectation la plus économique. ⚠️ **Réserve :** les libellés « toujours vrai / toujours faux » ne sont
attestés nulle part dans la source. Ils sont **proposés**, et devront être validés comme tels — ce sont les
seuls mots que ce lot introduit de toutes pièces.

---

### A1-03 · §3.2 — Exemples des quantificateurs
**Action :** Combler · **Fragment :** #5a (@9274)

**Source.** Le tableau 3.2 énumère « Universel · Pour tout », « Existentiel · Il existe au moins un »,
« Existence et unicité · Il existe exactement un », puis :

> Exemples : **Signification :** tout réel a un carré positif ou nul. **Signification :** il existe au moins
> un entier dont le carré vaut 9.

Deux emplacements « Exemples : » sont vides, et les deux « Signification : » qui suivent décrivent
précisément des exemples sans les énoncer. Par ailleurs §3.1 subsistent trois emplacements vides :
« « Pour tout », « chaque », « quel que soit » → penser à _ . ».

Le fragment #5a fournit, dans l'ordre :

> `∃x x` · `∃!x x` · `∀x ∈ R, x² ≥ 0` · `∃x ∈ Z, x² = 9` · `∀` · `∃` · `∃!`

**Proposition.**

| Nom | Symbole | Exemple |
|---|---|---|
| Universel | `∀` | `∀x ∈ R, x² ≥ 0` |
| Existentiel | `∃` | `∃x ∈ Z, x² = 9` |
| Existence et unicité | `∃!` | `∃!x x` |

et combler les trois réflexes de reconnaissance du §3.1 par `∀`, `∃`, `∃!` respectivement.

**Justification.** Les deux phrases « Signification » décrivent exactement `∀x ∈ R, x² ≥ 0` (« tout réel a
un carré positif ou nul ») et `∃x ∈ Z, x² = 9` (« il existe au moins un entier dont le carré vaut 9 »).
L'appariement est dicté par le texte lui-même.

**Note sur `∃x x` et `∃!x x`.** Ces deux tokens sont des formes tronquées — il manque le prédicat. La
restitution complète relève du palier T2 et n'est **pas** proposée ici ; ils sont portés en A1-10 comme
inconnus partiels.

---

### A1-04 à A1-09 · §4.2 — Les cinq tables de vérité
**Action :** **Reformater** · **Fragments :** #7, #8, #9, #10, #11, #12, #13

⚠️ **Ces fragments ne sont pas déplacés.** Le contenu des cinq tables est à sa place dans le §4.2 : la
dégradation a supprimé la grille, pas les valeurs. La proposition porte donc sur la **structure**, non sur
l'emplacement.

**Source.** En-têtes puis valeurs, dans l'ordre :

> `P ¬P` · `P Q P ∧ Q` · `P Q P ∨ Q` · `P Q P → Q` · *(équivalence : en-tête absent)*
> Négation `V F / F V` · Conjonction `VVV / VFF / FVF / FFF` · Disjonction `VVV / VFV / FVV / FFF` ·
> Implication `VVV / VFF / FVV / FFV` · Équivalence `VVV / VFF / FVF / FFV`

**Proposition.**

**Négation**

| P | ¬P |
|---|---|
| V | F |
| F | V |

**Conjonction**

| P | Q | P ∧ Q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

**Disjonction inclusive**

| P | Q | P ∨ Q |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

**Implication**

| P | Q | P → Q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

**Équivalence**

| P | Q | P ↔ Q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

**Justification.** Les soixante valeurs ont été relues une à une et confrontées aux définitions : les cinq
tables sont **exactes**, y compris l'implication matérielle — piège classique que la source évite
correctement. Seul l'en-tête de la table d'équivalence (`P Q P ↔ Q`) est absent ; il est restitué par
symétrie avec les quatre autres.

⚠️ **C'est une vérification, pas une restitution.** Aucune valeur n'a été modifiée. Le lot se borne à
proposer de rendre à ces tables leur forme tabulaire.

---

## T2 — Palier concordant (7 propositions)

### A1-10 · §3.2 — Formes tronquées `∃x x` et `∃!x x`
**Action :** Combler · **Fragment :** #5a (reste)

**État.** Le prédicat a été perdu. La source ne permet pas de le rétablir.

**Proposition :** **aucune restitution.** Consigner comme inconnu partiel, avec la mention
« forme tronquée, prédicat perdu ».

**Justification.** Inventer un prédicat violerait la règle fondamentale du chantier. La trace est conservée
pour mémoire.

---

### A1-11 · §2 — Notations du vocabulaire
**Action :** Combler · **Fragment :** #1 (@5971)

**Source.** Insertion au milieu du tableau de vocabulaire du §2, entre les entrées « Déduction » et
« Axiome ». Fragment :

> `V F` · `1 0` · `∧, ∨, ¬, →, ↔` · `P(x)` · `R(x, y)` · `∀, ∃` · `Γ ⊨ φ`

**Proposition.** Reconstituer une entrée de vocabulaire :

| Notion | Notation |
|---|---|
| Valeurs de vérité | `V` / `F` (ou `1` / `0`) |
| Connecteurs | `∧, ∨, ¬, →, ↔` |
| Prédicat unaire | `P(x)` |
| Prédicat binaire | `R(x, y)` |
| Quantificateurs | `∀, ∃` |
| Conséquence logique | `Γ ⊨ φ` |

**Justification.** Le §2 est intitulé « Vocabulaire fondamental » et procède par paires
notion / définition. Le fragment énumère des notations, dont aucune n'a d'entrée dans le §2 restant.
⚠️ **Réserve :** les libellés de la colonne « Notion » sont **proposés** ; seules les notations sont
attestées. L'ordre des lignes suit l'ordre du fragment.

---

### A1-12 · §2 — Relation
**Action :** Combler · **Fragment :** #2 (@7652)

**Source.** Entrée de vocabulaire : « Relation — Association entre objets ». Fragment : `⊥` · `x ∈ A` ·
`R(x, y)`.

**Proposition.** Porter `R(x, y)` comme notation de l'entrée « Relation », et `x ∈ A` comme notation de
l'entrée « Ensemble ». Le `⊥` reste **non attribué** (voir A1-13).

**Justification.** `R(x, y)` est la notation canonique d'une relation binaire et le fragment a été trouvé
dans la zone du vocabulaire. L'entrée « Relation » du §2 n'a pas de notation. ⚠️ L'attribution de `x ∈ A` à
« Ensemble » est une inférence par similarité, non une lecture.

---

### A1-13 · §2 — Le symbole `⊥`
**Action :** — · **Fragment :** #2 (reste)

**Proposition :** **aucune restitution.** `⊥` apparaît deux fois dans A (#2 @7652 et #4a @8630). Sa
destination d'origine ne peut être établie. Consigner.

---

### A1-14 · §2 — Fonction
**Action :** Combler · **Fragment :** #3 (@7685)

**Source.** Entrée de vocabulaire : « Fonction — Association … ». Fragment : `f : A → B` · `N`.

**Proposition.** Porter `f : A → B` comme notation de l'entrée « Fonction ». Le `N` (probablement `ℕ`)
reste **non attribué**.

**Justification.** Même raisonnement qu'en A1-12. ⚠️ Le `N` isolé pourrait appartenir au §8.3
(dénombrabilité) : destination non tranchée.

---

### A1-15 · §4.2 — Contraposée et équivalence
**Action :** Réattribuer · **Fragment :** #6 (@10437)

**Source.** Fragment trouvé dans le §4.2, à la fin de la définition de la table de vérité :

> `P → Q ≡ ¬Q → ¬P` · `P ↔ Q ≡ (P → Q) ∧ (Q → P)` · `P, Q, R, …`

**Proposition.** Déplacer les deux équivalences vers la **§3.3 « Équivalences logiques essentielles »**,
qui énumère précisément « Double négation · Lois de De Morgan · Implication · Contraposée · Équivalence »
sans énoncé. Laisser `P, Q, R, …` dans le §4.2, où il désigne l'ensemble des propositions d'une formule.

**Justification.** La contraposée est un objet du §3.3, pas du §4.2 ; le §4.2 traite des tables de vérité.
⚠️ **Réserve :** cette affectation est une inférence thématique. Le fragment pourrait tout aussi bien
appartenir au §6.2 « Contraposée », qui est lui aussi vide. Les deux destinations sont plausibles ; je
propose le §3.3 parce que le §4.2 est immédiatement contigu et que le §6.2 reçoit déjà la proposition
A2-07 du lot 2. **Ce point mérite l'arbitrage du porteur.**

---

### A1-16 · §4.4 — Exemples de satisfaisabilité
**Action :** Combler · **Fragment :** #14 (@11956)

**Source.** Fin du §4.4 « Satisfaisabilité et validité ». Fragment :

> `P Q P ↔ Q` · `P ∨ ¬P` · `P ∧ ¬P` · `P → Q`

**Proposition.** Reconstituer le tableau d'exemples du §4.4 :

| Notion | Exemple | Statut |
|---|---|---|
| Contingence | `P → Q` | ni tautologie ni contradiction |
| Équivalence | `P ↔ Q` | contingente |
| Tautologie | `P ∨ ¬P` | toujours vraie |
| Contradiction | `P ∧ ¬P` | toujours fausse |

**Justification.** `P ∨ ¬P` est une tautologie et `P ∧ ¬P` une contradiction : l'appariement est certain.
⚠️ **Réserve :** la colonne « Statut » est **proposée** — les mots « Contingence », « Tautologie »,
« Contradiction » figurent bien dans le §4.3, mais leur appariement aux exemples du fragment est une
inférence. Les tokens `P Q` en tête sont les en-têtes de colonnes d'un tableau dont on ne connaît pas la
forme.

---

## Récapitulatif du lot 1

| Palier | Nombre | Dont restitutions de contenu | Dont reformatage | Dont inconnus |
|---|---:|---:|---:|---:|
| T1 | 9 | 3 (A1-01, A1-02, A1-03) | 6 (A1-04 → A1-09) | 0 |
| T2 | 7 | 4 (A1-11, A1-12, A1-14, A1-15, A1-16) | 0 | 3 (A1-10, A1-13, A1-14 partiel) |
| **Total** | **16** | | | |

⚠️ **Deux points soumis à l'arbitrage du porteur :**
1. **A1-02** introduit deux libellés que la source n'atteste pas (« toujours vrai / toujours faux »).
2. **A1-15** hésite entre deux destinations (§3.3 ou §6.2).

---

**Rien de ce lot n'a été appliqué.** Le clone de travail `/home/user/_audit/connaissance` reste disponible
pour l'application après validation.
