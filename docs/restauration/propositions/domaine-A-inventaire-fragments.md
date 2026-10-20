# DOMAINE A — INVENTAIRE DES FRAGMENTS DE FORMULES DÉPLACÉES

**Date :** 2026-10-20 — **Chantier :** restauration, phase 1 — **Statut :** **proposition, non appliquée**
**Source :** `Maths-vers-Informatiques/DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE.md` (clone `f0f5e2d`)
**Outil :** `tools/restauration/inventorier_fragments.py`
**Règle :** aucune restitution n'est appliquée sans validation expresse, lot par lot.

---

## 1. Objet

Ce document est l'inventaire complet des 67 fragments de formules détectés dans A. Il ne restaure rien : il
**trie**. Les restitutions elles-mêmes sont proposées dans les quatre lots qui l'accompagnent
(`domaine-A-lot1.md` … `domaine-A-lot4.md`).

Reproduction de l'inventaire :

```
python3 tools/restauration/inventorier_fragments.py <fichier-A.md> --slots
```

---

## 2. Ce que la mesure a établi

### 2.1 Les formules n'ont pas été supprimées, mais déplacées

Trois preuves indépendantes, toutes vérifiées par lecture :

1. **Insertion au milieu d'une phrase** (§10.2) : « …devient automatiquement décidable par cette
   *[ici : les trois formules des §10.1 à 10.3]* méthode. » La phrase est coupée en deux.
2. **Insertion au milieu d'une autre phrase** (§11.3) : « …une procédure qui termine lorsqu'elles sont
   positives, tandis *[ici : `A`, `P(A)`, `|A| < |P(A)|`]* que sur les instances négatives… ».
3. **Insertion au milieu d'un tableau** (§3.2, §6.7) : le fragment s'intercale entre deux lignes dont les
   colonnes sont vides.

### 2.2 Conséquence : la différence de nature avec le chantier précédent

| | Chantier K, L, I, N, J | Documents A, B, C, D |
|---|---|---|
| Ce qui manque | le **contenu** | l'**emplacement** |
| Ce qui est connu | l'emplacement (bloc `\[ \]` vide, numéro de ligne) | le contenu (le fragment existe) |
| Nature de l'opération | **comblement** | **réattribution** |
| Risque principal | inventer une formule | **attribuer une formule au mauvais endroit** |

C'est pourquoi les paliers de confiance du §3 existent, et pourquoi le palier 3 n'est jamais proposé.

### 2.3 Le plan, lui, est intact

Les 35 intitulés de section survivent en texte. La reconstruction du plan est donc totale (voir
`docs/audit/fiches/domaine-A-logique-et-fondements.md` §2). Seules les formules ont bougé.

---

## 3. Paliers de confiance

| Palier | Définition | Nombre | Traitement |
|---|---|---:|---|
| **T1 — Attesté** | La source présente un **emplacement explicitement vide** (par exemple « Initialisation : _ . ») **et** le fragment fournit exactement le ou les tokens manquants. La restitution est une **lecture**, pas une inférence. | **32** | Proposé |
| **T2 — Concordant** | La destination est identifiable avec confiance par le sujet, mais il n'existe pas d'emplacement vide explicite, ou plusieurs emplacements sont en concurrence. La restitution est une **inférence argumentée**. | **18** | Proposé, avec l'argument |
| **T3 — Non proposé** | Destination ambiguë, ou fragment trop dégradé pour être reconstruit sans inventer. | **2** | **Jamais proposé** — consigné comme inconnu |
| **Hors champ** | Artefacts de décomposition d'accents (§27) et flèches de ponctuation dans les titres. Ce ne sont pas des formules. | **18** | Exclu |

**70 propositions, issues de 67 fragments.** Trois fragments (#4, #5, #25) sont **scindés** en deux
propositions, car leurs parties relèvent de paliers différents — d'où 67 + 3 = 70.

**52 propositions sont soumises** (T1 + T2 + T3) ; les 18 éléments hors champ sont exclus.

⚠️ Ces décomptes sont calculés par une source unique de classification, pas recomposés à la main — ce
chantier a déjà été victime de totaux arithmétiques erronés.

---

## 4. Option de validation retenue

Le porteur a demandé la proposition **lot par lot, soumise à validation avant application**, en me laissant
le choix de la modalité de validation. **L'option retenue est la validation par palier de confiance, dans cet
ordre :**

1. **T1 en un seul bloc** — les 28 propositions du palier 1, tous lots confondus.
2. **T2 lot par lot** — par groupe de sections (`lot1` à `lot4`).
3. **T3 jamais soumis** — consigné, non proposé.

### Pourquoi cette option plutôt que la validation lot par lot intégrale

- **Le risque dépend de la preuve, pas du sujet.** Un fragment dont la destination est attestée par une case
  vide porte le même risque nul, qu'il relève de la logique propositionnelle ou de la calculabilité. Les faire
  valider séparément fabrique une précision qui n'existe pas.
- **À l'inverse, T2 demande un jugement**, et ce jugement est propre à chaque section : il doit être rendu
  groupe par groupe.
- **Ne rien proposer en T3** est la seule façon de tenir la règle « jamais une hypothèse pour un fait ». Un
  fragment dont on ne sait pas où il va n'a pas de restitution : il a une notice d'inconnu.

**Ordre recommandé : T1 (un bloc) → T2-lot1 → T2-lot2 → T2-lot3 → T2-lot4.**

---

## 5. Index complet des 67 fragments

Colonnes : **gît** = section où le fragment se trouve aujourd'hui ; **destination** = section à laquelle il
appartient selon l'analyse. Quand les deux diffèrent, le fragment est déplacé.

| # | @ | Gît | Destination | Contenu | Palier |
|---:|---:|---|---|---|---:|
| 1 | 5971 | §2 | §2 | `V F · 1 0 · ∧ ∨ ¬ → ↔ · P(x) · R(x,y) · ∀ ∃ · Γ ⊨ φ` | T2 |
| 2 | 7652 | §2 | §2 | `⊥ · x ∈ A · R(x,y)` | T2 |
| 3 | 7685 | §2 | §2 | `f : A → B · N` | T2 |
| 4a | 8630 | §3.2 | **§3.1** | `¬P · P ∧ Q · P ∨ Q · P → Q · P ↔ Q · ⊤ ⊥` — colonne « Symbole » vide du tableau des connecteurs | **T1** |
| 4b | 8630 | §3.2 | §3.2 | `∀x x` | T2 |
| 5a | 9274 | §3.3 | **§3.2** | `∃x x · ∃!x x · ∀x ∈ R, x² ≥ 0 · ∃x ∈ Z, x² = 9 · ∀ ∃ ∃!` | **T1** |
| 5b | 9274 | §3.3 | §3.3 | `¬(¬P) ≡ P · ¬(P ∧ Q) ≡ ¬P ∨ ¬Q · ¬(P ∨ Q) ≡ ¬P ∧ ¬Q · P → Q ≡ ¬P ∨ Q` | T2 |
| 6 | 10437 | §4.2 | §4.2 | `P → Q ≡ ¬Q → ¬P · P ↔ Q ≡ (P → Q) ∧ (Q → P) · P, Q, R, …` | T2 |
| 7 | 10532 | §4.2 | §4.2 | `P Q · P → Q` (en-tête de table) | T1 |
| 8 | 10558 | §4.2 | §4.2 | `V F / F V` — négation | T1 |
| 9 | 10585 | §4.2 | §4.2 | conjonction (12 valeurs) | T1 |
| 10 | 10652 | §4.2 | §4.2 | disjonction (12 valeurs) | T1 |
| 11 | 10709 | §4.2 | §4.2 | implication (12 valeurs) | T1 |
| 12 | 10856 | §4.2 | §4.2 | `P ¬P · P Q P ∧ Q · P Q P ∨ Q · P Q P → Q` (en-têtes des 5 tables) | T1 |
| 13 | 10935 | §4.2 | §4.2 | équivalence (12 valeurs) | T1 |
| 14 | 11956 | §4.4 | §4.4 | `P Q P ↔ Q · P ∨ ¬P · P ∧ ¬P · P → Q` | T2 |
| 15 | 12863 | §5.1 | §5.1 | `(P ∨ Q) ∧ (¬P ∨ R)` | T2 |
| 16 | 12906 | §5.1 | §5.1 | `Étudiant(x)` — le `É` initial est déplacé en fin de mot | T2 |
| 17 | 12925 | §5.1 | §5.1 | `Inscrit(x, c)` | T2 |
| 18 | 12948 | §5.1 | §5.1 | `Supérieur(x, y)` | T2 |
| 19 | 13905 | §5.4 | §5.4 | `∀x (` | T1 |
| 20 | 13923 | §5.4 | §5.4 | `(x) → É…` | T1 |
| 21 | 13942 | §5.4 | §5.4 | `s(x` | T1 |
| 22 | 13951 | §5.4 | **§5.3** | `è · ¬∀x P(x) ≡ ∃x ¬P(x) · ¬∃x P(x) ≡ ∀x ¬P(x)` | **T1** |
| 23 | 15050 | §6.3 | **§6.2** | `P → Q · P Q · P Q · P → Q · ¬Q → ¬P` (contraposée) | T2 |
| 24 | 16068 | §6.7 | §6.7 | `∀x, P(x) · a · ¬P(a) · P ∨ ¬P · P, P → Q ⊢ Q · ¬Q, P → Q ⊢ ¬P · ∧ · P, Q ⊢ P ∧ Q` | **T1** |
| 25a | 17438 | §7.2 | **§7.1** | `P(n₀) · P(n) → P(n+1) · P(n) pour n ≥ n₀` | **T1** |
| 25b | 17438 | §7.2 | §6.7 | `P ∧ Q ⊢ P · P ⊢ P ∨ Q · P ∨ Q, ¬P ⊢ Q` | T2 |
| 26 | 17572 | §7.2 | §7.1 | `+ 1) · P(n) n ≥ n₀ · P(n) n` | T1 |
| 27 | 18683 | §8 | §8 | code Python `if n = 0:` | T2 |
| 28 | 18719 | §8 | §8 | code Python `n × factorielle(n - 1)` | T2 |
| 29 | 20133 | §8.4 | **§8.2 / §8.3** | `f(a) = f(b) ⇒ a = b · ∀y, ∃x : f(x) = y · N Z Q R N` | **T1** |
| 30 | 21846 | §9.3 | §9.2 | `x ∉ x` — le `∉` est perdu, il ne reste que `n n` | **T3** |
| 31 | 23036 | §10.2 | **§10.1** | `¬(P ∧ Q) ≡ ¬P ∨ ¬Q · ¬(P ∨ Q) ≡ ¬P ∧ ¬Q` | **T1** |
| 32 | 23113 | §10.2 | §10.2 | `(P ∨ A), (¬P ∨ B) ⇒ (A ∨ B)` | **T1** |
| 33 | 26246 | §10.6 | §10.6 | `P · x · P · x · H(P, x) = { 1 / 0` | **T1** |
| 34 | 26290 | §10.6 | §10.6 | `P(x)` | T1 |
| 35 | 26309 | §10.6 | — | `ê` — artefact d'accent | hors champ |
| 36 | 27562 | §11.3 | **§10.7** | `A · P(A) · A · \|A\| < \|P(A)\|` | **T1** |
| 37 | 27588 | §11.3 | **§10.7** | `P(A` | **T1** |
| 38 | 29377 | §11.6 | §11.6 | `A ≤ B · B · A` | **T1** |
| 39 | 30482 | §12.2 | **§12.3** | `{P} C {Q} · P C Q` | **T1** |
| 40 | 30636 | §12.2 | **§12.3** | `P · C · Q` | **T1** |
| 41 | 35647 | §13.5 | §13.5 | `n · n` (vecteur de taille n) | **T1** |
| 42 | 39221 | §14.7 | §14.7 | `2 + 3 × 4` — **en place**, non déplacé | T1 |
| 43 | 42689 | §15.3 | §15.3 | `n · 2ⁿ` | **T1** |
| 44 | 44843 | §15.7 | **§15.6** | `x = 2 · y = 3` (unification de `f(x,3)` et `f(2,y)`) | T2 |
| 45 | 49040 | §16.5 | §16.5 | `Authentifié(u) ∧` | T1 |
| 46 | 49064 | §16.5 | §16.5 | `Autorisé(u, r) →` | T1 |
| 47 | 49097 | §16.5 | §16.5 | `AccèsPermis(u, r)` | T1 |
| 48 | 52638 | §17.5 | §17.5 | `A · R · P` | T2 |
| 49 | 53601 | §18 | §18 | `A ∧ R → P` | T2 |
| 50–61 | 66135–66718 | §27 | — | `v é`, `r é`, `ê t`, `g é n é`… — décomposition d'accents | hors champ |
| 62 | 71743 | §30 | ? | `P → Q` — aucune destination identifiable | **T3** |
| 63 | 75283 | §34 | — | `A À` — ponctuation | hors champ |
| 64–67 | 77576–77665 | §35 | — | `→ B`, `→ C`, `→ D`, `→ V` — flèches de titre | hors champ |

---

## 6. Répartition par lot

| Lot | Sections | Propositions | T1 | T2 | T3 |
|---|---|---:|---:|---:|---:|
| `domaine-A-lot1.md` | §2, §3, §4 | 16 | 9 | 7 | 0 |
| `domaine-A-lot2.md` | §5, §6, §7 | 13 | 7 | 6 | 0 |
| `domaine-A-lot3.md` | §8, §9, §10 | 10 | 7 | 2 | 1 |
| `domaine-A-lot4.md` | §11, §12, §13, §15, §16, §17, §18, §30 | 13 | 9 | 3 | 1 |
| **Total soumis** | | **52** | **32** | **18** | **2** |
| Hors champ (§27, titres, §34) | | 18 | — | — | — |

Les propositions T3 ne sont **pas** des restitutions : ce sont des notices d'inconnu, soumises pour
information mais dont aucune restitution n'est proposée.

---

## 7. Ce que cet inventaire ne dit pas

- Il **ne prouve pas** que A comportait des blocs d'équations display. Aucun délimiteur `\[` ne subsiste ; les
  deux thèses (jamais de display / display supprimé avec ses délimiteurs) restent indistinguables, et il a été
  établi qu'aucune version antérieure de A n'existe.
- Il **ne mesure pas** le nombre total de blocs déplacés : seuls les fragments mathématiques détectables sont
  comptés. Des blocs de prose déplacés existent (§32 → §33, §35) et ne sont pas inventoriés ici.
- Il **ne propose aucune restitution** : celle-ci est dans les lots, et attend la validation.

---

**Références :** `docs/audit/fiches/domaine-A-logique-et-fondements.md` (fiche, §5 typologie de la
dégradation, §11 méthode) · `docs/restauration/CLOTURE-CHANTIER.md` (§6 procédure de reprise, §6.1
validation de la procédure).
