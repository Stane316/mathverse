# DOMAINE A — LOT 3 : ENSEMBLES, PARADOXES, THÉORÈMES (§8, §9, §10)

**Date :** 2026-10-20 — **Statut :** **APPLIQUÉ LE 2026-10-20** (compte rendu en bas de document)
**Document source :** `Maths-vers-Informatiques/DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE.md`
**Inventaire de référence :** `domaine-A-inventaire-fragments.md`
**Contenu du lot :** 10 propositions — **7 T1**, **2 T2**, **1 T3**

> ## ✅ LOT APPLIQUÉ LE 2026-10-20 (compte rendu en bas de document)
>
> **Statut : APPLIQUÉ.** Diff livré : `livrables/domaine-A-lot3.gitdiff` — diff
> **incrémental**, à appliquer **après** les lots 1 et 2 ; éprouvé par
> `git apply --check` sur l'état post-lot 2 reconstruit. Journal :
> `domaine-A-lot3.journal.json`. Générateur : `build_lot_A_3.py`, sur le moteur
> partagé `lot_commun.py`.
>
> **16 substitutions** sur **9 propositions**. La dixième — **A3-10**, paradoxe de
> Russell — n'entraîne volontairement **aucune édition**. Deux trouvailles faites
> en route sont **renvoyées** aux lots 4 et 5, voir le compte rendu.

**Légende des actions :** **Combler** (emplacement vide explicite) · **Réattribuer** (fragment à déplacer) ·
**Reformater** (contenu en place, structure à reconstituer).

---

## T1 — Palier attesté (7 propositions)

### A3-01 · §8.2 et §8.3 — Signatures et dénombrabilité
**Action :** Réattribuer · **Fragment :** #29 (@20133)

**Source.** Le fragment gît dans le §8.4, après le mot « Idée » :

> 8.4 Diagonalisation de Cantor — … **Idée** `f(a) = f(b) ⇒ a = b` `∀y, ∃x : f(x) = y` `N Z Q R N`

Or le §8.4 traite de la diagonalisation : l'injectivité et la surjectivité n'y ont pas leur place. Deux
sections en amont, le §8.2 possède une colonne **vide** :

> **8.2 Injection, surjection, bijection**
> Notion · Définition intuitive · Signature
> Injection · Deux entrées distinctes ne partagent pas la même sortie · _
> Surjection · Chaque élément du codomaine est atteint · _
> Bijection · Injection et surjection · Correspondance un-à-un et surjective

Et le §8.3 possède **cinq** emplacements vides :

> **8.3 Ensembles dénombrables** — Exemples classiques : _ est dénombrable ; _ est dénombrable ;
> _ est dénombrable ; _ n'est pas dénombrable.
> … ou si une correspondance bijective avec _ existe.

**Proposition.**

| Destination | Emplacement | Formule |
|---|---|---|
| §8.2 | Signature — Injection | `f(a) = f(b) ⇒ a = b` |
| §8.2 | Signature — Surjection | `∀y, ∃x : f(x) = y` |
| §8.3 | Exemples classiques (1) | `ℕ` est dénombrable |
| §8.3 | Exemples classiques (2) | `ℤ` est dénombrable |
| §8.3 | Exemples classiques (3) | `ℚ` est dénombrable |
| §8.3 | Exemples classiques (4) | `ℝ` n'est pas dénombrable |
| §8.3 | correspondance bijective avec _ | `ℕ` |

**Justification.** Deux séries d'appariements, toutes deux complètes :

1. **§8.2** — la définition intuitive de l'injection (« deux entrées distinctes ne partagent pas la même
   sortie ») est la glose littérale de `f(a) = f(b) ⇒ a = b`, et celle de la surjection (« chaque élément du
   codomaine est atteint ») celle de `∀y, ∃x : f(x) = y`. Les deux colonnes vides reçoivent donc les deux
   formules du fragment, sans ambiguïté.
2. **§8.3** — le fragment porte **cinq** tokens (`N Z Q R N`), et le §8.3 présente **exactement cinq**
   emplacements vides : trois ensembles dénombrables, un non dénombrable, et l'ensemble de référence de la
   bijection. La correspondance est bijective. L'ordre du fragment suit l'ordre du texte, et `ℝ` en
   quatrième position est le seul des quatre à ne pas être dénombrable — ce que la source affirme
   précisément à cet endroit.

⚠️ **Réserve mineure :** les tokens `N Z Q R` sont la forme dégradée de `ℕ ℤ ℚ ℝ`. La restitution des
symboles double-struck est une normalisation typographique, pas une invention de contenu.

---

### A3-02 · §10.1 — Lois de De Morgan
**Action :** Combler · **Fragment :** #31 (@23036)

**Source.** Le §10.1 présente un énoncé vide :

> **10.1 Lois de De Morgan**
> Énoncé : _  Reconnaissance : négation d'une condition composée.

Fragment : `¬(P ∧ Q) ≡ ¬P ∨ ¬Q` · `¬(P ∨ Q) ≡ ¬P ∧ ¬Q`.

**Proposition.** Porter les deux équivalences dans l'emplacement « Énoncé : ».

**Justification.** L'emplacement est vide, le fragment contient les deux lois de De Morgan, et la section
porte leur nom. Aucune autre affectation n'est concevable.

---

### A3-03 · §10.2 — Règle de résolution propositionnelle
**Action :** Combler · **Fragment :** #32 (@23113)

**Source.**

> **10.2 Principe de résolution propositionnelle**
> Une règle de résolution classique : _  Elle élimine le littéral complémentaire _ dans deux clauses.

Fragment : `( P   ∨   A ),   (¬ P   ∨   B )   ⇒   ( A   ∨   B )` · `P`.

**Proposition.** Porter `(P ∨ A), (¬P ∨ B) ⇒ (A ∨ B)` dans le premier emplacement, et `P` dans le second
(« le littéral complémentaire `P` »).

**Justification.** Les deux emplacements sont vides ; le fragment fournit la règle et le nom du littéral
éliminé, dans cet ordre. La phrase qui suit — « Elle élimine le littéral complémentaire » — désigne
exactement le `P` présent dans les deux clauses sous les formes `P` et `¬P`.

---

### A3-04 et A3-05 · §10.6 — Problème de l'arrêt
**Action :** Combler · **Fragments :** #33 (@26246), #34 (@26290)

**Source.**

> **10.6 Problème de l'arrêt**
> Formulation — On considère un programme _ et une entrée _ . Le problème demande si l'exécution de _
> sur _ finira par s'arrêter. Question : _

Soit **quatre** emplacements vides (deux fois « programme » et « entrée »), plus une « Question : » vide.

Fragment recomposé : `P` · `x` · `P` · `x` · `H(P, x) = { 1 si P(x) s'arrête, 0 sinon` · `P(x)`.

**Proposition.**

| Emplacement | Contenu |
|---|---|
| « un programme _ » | `P` |
| « une entrée _ » | `x` |
| « l'exécution de _ sur _ » | `P` sur `x` |
| « Question : _ » | `H(P, x) = 1 si P(x) s'arrête, 0 sinon` |

**Justification.** Le fragment fournit les quatre tokens dans l'ordre du texte (`P`, `x`, `P`, `x`), puis la
forme de la fonction d'arrêt. Le fragment a été trouvé **entre l'intitulé « Ce que cela ne veut pas dire » et
son paragraphe** : il coupe donc la section, ce qui confirme le déplacement.

⚠️ **Réserve :** la notation `H(P, x)` est attestée dans le fragment ; la formulation « 1 si … s'arrête,
0 sinon » est attestée mais sa mise en forme (accolade, alignement) est **proposée**. Le fragment porte
`s'arr te e ˆ` — recomposé en `s'arrête` par recollement de l'accent.

---

### A3-06 et A3-07 · §10.7 — Théorème de Cantor
**Action :** Réattribuer · **Fragments :** #36 (@27562), #37 (@27588)

**Source.** Le fragment est inséré **au milieu d'une phrase** du §11.3 :

> …une procédure qui termine lorsqu'elles sont positives, **tandis** [ `A` `P(A)` `A` `|A| < |P(A)|` ]
> **que** sur les instances négatives elle peut ne pas terminer.

Or le §10.7 présente **trois** emplacements vides :

> **10.7 Théorème de Cantor sur les ensembles**
> Pour tout ensemble _ , son ensemble des parties _ a une cardinalité strictement supérieure à celle de _ .

**Proposition.**

| Emplacement | Contenu |
|---|---|
| « Pour tout ensemble _ » | `A` |
| « son ensemble des parties _ » | `P(A)` |
| « à celle de _ » | `A` |

et porter `|A| < |P(A)|` comme forme du théorème.

**Justification.** Le fragment fournit `A`, `P(A)`, `A` — trois tokens, dans l'ordre des trois emplacements
du §10.7 — suivis de l'inégalité qui est l'énoncé même du théorème. La phrase coupée du §11.3 est un
artefact de déplacement manifeste : « tandis … que » n'admet aucune insertion mathématique.

⚠️ **C'est le cas le plus solide du corpus avec A2-07** : emplacements vides explicites *et* phrase coupée
en deux, les deux preuves réunies.

---

## T2 — Palier concordant (2 propositions)

### A3-08 et A3-09 · §8 — Fonction factorielle (code)
**Action :** Reformater · **Fragments :** #27 (@18683), #28 (@18719)

**Source.** Du code Python aplati dans le §8 :

> `n − 1  factorielle(n): si n = 0: retourner 1 sinon: retourner n × factorielle(n - 1)`

**Proposition.** Reconstituer le bloc de code :

```python
def factorielle(n):
    if n = 0:
        return 1
    else:
        return n × factorielle(n - 1)
```

**Justification.** Le texte est entièrement présent et lisible ; seuls les retours à la ligne et
l'indentation ont été perdus, ainsi que le mot-clé `def`. ⚠️ **Réserves :**
1. Le `def` initial n'est pas attesté — il est restitué par nécessité syntaxique.
2. Le `×` du fragment est un artefact : la source orthographique est `*` en Python. La restitution en `*`
   est **proposée**.
3. Le code porte `if n = 0` — en Python, la comparaison s'écrit `==`. **L'erreur est dans la source**, non
   dans la dégradation. Je la conserve telle quelle et la **signale** : c'est une erreur du document
   d'origine, à corriger ou non selon l'arbitrage du porteur.

---

## T3 — Non proposé (1 notice d'inconnu)

### A3-10 · §9.2 — Paradoxe de Russell
**Action :** **aucune** · **Fragment :** #30 (@21846)

**Source.** Le fragment est inséré **dans une liste à puces** du §9.3, entre deux items :

> Ils sont pertinents pour comprendre : les définitions autoréférentielles ; [ `n` `n` ] les systèmes
> formels ; …

**État.** Le fragment se réduit à deux occurrences de la lettre `n`. Le symbole qui les reliait —
vraisemblablement `∉` — a été **perdu** : il ne figure dans aucun fragment du document, et l'inventaire des
symboles survivants confirme son absence.

**Proposition :** **aucune restitution.** Consigner comme inconnu, avec la mention « symbole relationnel
perdu ; forme probable `x ∉ x`, non attestée ».

**Justification.** Rétablir `x ∉ x` reviendrait à **inventer** le symbole manquant. La règle du chantier
l'interdit. Le paradoxe de Russell est par ailleurs correctement décrit en prose au §9.2 (« l'ensemble des
ensembles qui ne se contiennent pas eux-mêmes ») : **la perte est formelle, elle n'est pas conceptuelle.**

---

## Récapitulatif du lot 3

| Palier | Nombre | Nature |
|---|---:|---|
| T1 | 7 | 4 comblements dictés par la glose (A3-01 §8.2, A3-02, A3-03, A3-04/05) · 1 réattribution à double preuve (A3-06/07) |
| T2 | 2 | reformatage de code, avec 3 réserves |
| T3 | 1 | notice d'inconnu — **aucune restitution** |
| **Total** | **10** | |

⚠️ **Points soumis à l'arbitrage du porteur :**
1. **A3-08/09** — faut-il corriger l'erreur `if n = 0` du document d'origine, ou la conserver ?
2. **A3-08/09** — restitution de `def` et de `*` : acceptée ou refusée ?
3. **A3-10** — confirmation qu'aucune restitution n'est tentée sur le symbole perdu.

---

**Rien de ce lot n'a été appliqué.**
---

## Compte rendu d'application (2026-10-20)

### Non-perte, vérifiée token par token

Les **24 tokens** déplacés ont été suivis un à un et retrouvés à leur nouvelle
demeure. Aucun n'a été supprimé, aucun n'a été complété par invention.

| Fragment gisant | Tokens | Destination |
|---|---|---|
| §8.4 | `f(a) = f(b) ⇒ a = b` · `∀y, ∃x : f(x) = y` | §8.2 |
| §8.4 | `N` · `Z` · `Q` · `R` · `N` | §8.3 (5 emplacements) |
| §8 intro | `n − 1` | bloc de code (dernière ligne) |
| §10.2 | `¬(P ∧ Q) ≡ ¬P ∨ ¬Q` · `¬(P ∨ Q) ≡ ¬P ∧ ¬Q` | §10.1 |
| §10.2 | `(P ∨ A), (¬P ∨ B) ⇒ (A ∨ B)` · `P` | §10.2 |
| §10.6 | `P` · `x` · `P` · `x` · `H(P, x) = { 1 si P(x) s'arrête, 0 sinon` | §10.6 |
| §11.3 | `A` · `P(A)` · `A` · `∣A∣ < ∣P(A)∣` | §10.7 |

### Trois phrases ressoudées au passage

Le retrait d'un fragment lui rend sa continuité. Trois sections en ont profité :

| Section | État | Après |
|---|---|---|
| §8.4 | « Idée [pile] Supposons qu'on ait prétendu… » | « Idée  Supposons qu'on ait prétendu… » |
| §10.2 | « … décidable par cette [pile] méthode. » | « … décidable par cette méthode. » |
| §10.6 | « Ce que cela ne veut pas dire [pile] Cela ne signifie pas… » | « Ce que cela ne veut pas dire  Cela ne signifie pas… » |

### Deux trouvailles faites en route, NON appliquées

**1. Le §11.3 porte une seconde intrusion — renvoyée au lot 4.** La phrase
« Existe-t-il une procédure mécanique qui, pour chaque entrée autorisée, produit la
sortie demandée en un nombre fini d'étapes ? » s'est insérée entre « tandis » et
« que ». Elle définit la **décidabilité**, pas la semi-décidabilité : son domicile
est donc ailleurs dans le §11, **qui relève du lot 4**. Le §11.3 reste coupé après
ce lot ; il sera ressoudé au lot 4, une fois la destination établie.

**2. Le §8 porte une phrase qui n'est pas à sa place — renvoyée au lot 5.**
« Après avoir examiné les _ premiers éléments, la variable max contient le maximum
de ces éléments. », suivie du token `i` orphelin. C'est **l'invariant de la
recherche du maximum d'un tableau**, c'est-à-dire l'exemple intuitif du §7.4 — dont
l'emplacement est précisément vide, et qui nomme exactement cela : « Dans une
recherche du maximum d'un tableau, l'invariant peut affirmer : _ ». Le §7.4 relevant
du lot 2, déjà livré, cette restitution est renvoyée à un **lot 5**.

### A3-10 — aucune restitution, et c'est la conclusion

Le fragment du §9.3 se réduit à deux occurrences de la lettre `n` ; le symbole qui
les reliait — vraisemblablement `∉` — est **perdu**, il ne figure dans aucun fragment
du document. Rétablir `x ∉ x` reviendrait à **inventer**. Rien n'est appliqué, rien
n'est ajouté au document. Le paradoxe est décrit correctement en prose au §9.2 :
**la perte est formelle, elle n'est pas conceptuelle.**

### Réserves signalées

| Point | Situation |
|---|---|
| `def` du bloc factorielle | non attesté, restitué par nécessité syntaxique |
| `si` / `retourner` / `sinon` → `if` / `return` / `else` | normalisation **validée** ; la variante fidèle reste disponible |
| `×` conservé | l'orthographe Python est `*` ; le signe attesté est gardé |
| `if n = 0` | **erreur du document d'origine**, conservée et signalée |
| `H(P, x) = { …` | accolade fermante **absente** du fragment, non ajoutée ; ordre des tokens `1 · 0 · si …` signalé |
| libellé « Forme : » au §10.7 | **ajouté** pour recevoir le 4ᵉ token, la source n'ayant pas de 4ᵉ emplacement |

### Vérifications

| Contrôle | Résultat |
|---|---|
| Diagnostic préalable (`python3 lot_commun.py build_lot_A_3.py`) | 16/16 sous-chaînes uniques |
| Mojibake | 0 |
| `git apply --check` sur l'état post-lot 2 reconstruit | OK |
| Diff incrémental livré | 42 lignes, `livrables/domaine-A-lot3.gitdiff` |
| Chaîne de volumes | 77 970 → 78 776 → 78 789 → **78 758** |
| Relecture in situ | §8, §10.1, §10.2, §10.6, §10.7 relus après application |
