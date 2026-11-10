# DOMAINE B — LOT 1 : TABLE DU §3, PROPRIÉTÉS DU §4.1, ET LES TROIS GLYPHES PERDUS

**Date :** 2026-10-21 — **Statut :** **PROPOSITION — NON APPLIQUÉE**
**Document source :** `Maths-vers-Informatiques/DOCUMENT B — THÉORIE DES NOMBRES.md` (clone `f0f5e2d`)
**Inventaire de référence :** `domaine-B-inventaire-fragments.md`
**Contenu du lot :** **6 substitutions, toutes de confiance haute**
**Générateur :** `tools/restauration/build_lot_B_1.py` — diagnostic **6/6 sous-chaînes uniques**

> ⚠️ **Ce lot n'est pas appliqué.** Conformément à la règle du chantier, aucune
> restitution n'est écrite sans validation expresse, lot par lot. Le générateur
> est prêt et éprouvé à sec : il suffit d'un mot pour l'appliquer.
> Effet mesuré à sec : **65 371 → 65 586 caractères (+215)**, **0 mojibake**,
> **0 glyphe U+E020 restant**.

---

## 1. Ce que le lot fait

| ID | Section | Opération | Confiance |
|---|---|---|---:|
| **B1-01** | §3 | Le tableau des formules de reconnaissance est rendu en Markdown ; neuf lignes sur quatorze reçoivent leur formule | **haute** |
| **B1-02** | §4.1 | Les quatre propriétés de la divisibilité sont complétées et numérotées | **haute** |
| **B1-03** | §4.2 | Le tas est retiré ; les tokens sans destination demeurent en note | **haute** |
| **B1-04** | §4.3 | L'exemple du PGCD reçoit `gcd(18, 30) = 6` | **haute** |
| **B1-05** | §4.4 | La relation PGCD × PPCM est restituée avec sa condition | **haute** |
| **B1-06** | §5.1 | La propriété fondatrice d'Euclide est restituée | **haute** |

**Les trois glyphes `≠` perdus sont consommés** par B1-02 (§4.1), B1-05 (§4.4) et B1-06 (§5.1).

---

## 2. Le fait qui fonde le lot : les piles de B débordent vers l'avant

C'est la différence structurale avec A, et elle a été établie en lisant, pas en supposant.

Dans A, le tas du §8 était un débordement de la **fin** du §7 : les formules avaient reculé.
**Dans B, c'est l'inverse : chaque tas reçoit les formules des sections qui le précèdent.**

Trois constats à l'appui :

| Tas situé en… | contient d'abord… | puis… |
|---|---|---|
| §4.2 | les formules du **§3** (table) | les propriétés du **§4.1** |
| §5.1 | la relation du **§4.4** | la propriété du **§5.1** |
| §12.2 | l'énoncé d'Euler du **§11.3** | l'exemple du **§12.1** |
| §13.2 | les formules des restes chinois du **§12.2** | les identités du **§13.2** |

**Conséquence :** une formule manquante ne se cherche pas dans la section qui la porte,
mais **dans le tas de la section suivante**. C'est la clé de lecture de tout le document B,
et elle vaudra pour les lots suivants.

---

## 3. B1-01 — La table du §3

### Ce que la source montre

Le §3 est un tableau à trois colonnes — « Si tu rencontres… » · « Pensé à… » ·
« Formule ou caractérisation » — dont **la troisième colonne est vide pour neuf lignes
sur quatorze**. La première colonne a, elle aussi, des slots vides (les variables).

### Le tas du §4.2, dans l'ordre

```
a  b | b = ak, k ∈ Z | a = bq + r, 0 ≤ r < b | gcd(a, b) | a  b
   | ax + by = gcd(a, b) | a  n | gcd(a, n) = 1 | n | a ≡ b (mod n)
   | n | ax ≡ 1 (mod n) | p  p
```

### La correspondance, ligne à ligne

| # | Ligne | Colonne 1 (variables) | Colonne 3 (formule) |
|---:|---|---|---|
| 1 | Divisibilité | `a`, `b` | `b = ak`, `k ∈ Z` |
| 2 | Division euclidienne | — | `a = bq + r`, `0 ≤ r < b` |
| 3 | PGCD | — | `gcd(a, b)` |
| 4 | Bézout | `a`, `b` | `ax + by = gcd(a, b)` |
| 5 | Coprimalité | `a`, `n` | `gcd(a, n) = 1` |
| 6 | Congruence | `n` | `a ≡ b (mod n)` |
| 7 | Inverse modulaire | `n` | `ax ≡ 1 (mod n)` |
| 8 | Primalité | `p` | Ses seuls diviseurs positifs sont 1 et `p` |

**Huit lignes, dans l'ordre, sans reste et sans inversion.** Le tas s'ouvre sur `a b`,
qui sont les deux slots de la première ligne — ce qui confirme que la correspondance
commence bien là et pas ailleurs.

### Ce qui est proposé

La table est rendue en Markdown (même opération que A1-01 et A1-03 sur A, déjà validée),
avec :

- les huit premières lignes complétées ;
- la ligne 13, dont le déclencheur « résoudre [ ] » reçoit `gˣ ≡ h (mod p)` — ver-batim dans
  le tas, immédiatement après le segment lacunaire ;
- la ligne 14, dont la colonne 3 reçoit `n = ∏ pᵢ^{eᵢ}`.

### ⚠️ Deux réserves

1. **Les exposants sont re-composés, pas récupérés.** `n = ∏ pᵢ^{eᵢ}` et `gˣ ≡ h (mod p)`
   portent des exposants. Or le document n'en contient **aucun** (0 occurrence de `² ³ ⁿ`
   dans 65 371 caractères). Les restituer est une **recomposition**, fondée sur le nom de
   la notion et la forme usuelle de l'énoncé — pas une lecture. C'est la seule part
   d'interprétation de ce lot, et elle est signalée comme telle.
2. **Les lignes 9 et 12 restent vides.** Voir §6.

---

## 4. B1-02 — Les quatre propriétés de la divisibilité (§4.1)

Le §4.1 énonce quatre propriétés, chacune avec ses slots vides :

> « Si [ ] et [ ], alors [ ]. Si [ ] et [ ], alors [ ] pour tous entiers [ ].
> Si [ ], alors [ ] pour tout entier [ ]. Si [ ] et [ ], alors [ ]. »

Et le tas du §4.2 **se poursuit**, après les huit lignes du tableau, par quatre groupes :

| Groupe du tas | Propriété restituée |
|---|---|
| `a ∣ b` `b ∣ c` `a ∣ c` | Si `a ∣ b` et `b ∣ c`, alors `a ∣ c` |
| `a ∣ b` `a ∣ c` `a ∣ (ub + vc)` `u, v` | Si `a ∣ b` et `a ∣ c`, alors `a ∣ (ub + vc)` pour tous entiers `u, v` |
| `a ∣ b` `a ∣ bc` `c` | Si `a ∣ b`, alors `a ∣ bc` pour tout entier `c` |
| `a ∣ b` `b =   0` `∣a∣ ≤ ∣b∣` | Si `a ∣ b` et `b ≠ 0`, alors `∣a∣ ≤ ∣b∣` |

**Quatre groupes, quatre propriétés, même ordre, sans reste.**

⚠️ **Un point a demandé arbitrage.** La troisième propriété ne présente **qu'un seul** slot
de condition (« Si [ ], alors [ ] pour tout entier [ ] »). La lecture classique serait
« si `a ∣ bc` et `pgcd(a,b) = 1`, alors `a ∣ c` » — mais elle exige **deux** conditions, et
le tas ne fournit pas `pgcd`. La seule lecture compatible avec un seul slot est
« si `a ∣ b`, alors `a ∣ bc` pour tout entier `c` », qui est une propriété usuelle et que
les tokens `a ∣ b`, `a ∣ bc`, `c` confirment exactement. **C'est la lecture retenue.**

**Le glyphe U+E020** de la quatrième propriété est restitué en `≠` : le contexte
« `b =  0` » ne laisse aucune autre lecture. Ce n'est pas une invention mais la réparation
d'une perte d'encodage.

---

## 5. B1-04, B1-05, B1-06 — Les trois sections suivantes

Ces trois éditions sont plus simples et suivent toutes le même mécanisme.

**B1-04 — §4.3, l'exemple du PGCD.** Le slot « Exemple : » est suivi de trois groupes.
Le dernier, `gcd(18, 30) = 6`, est l'exemple annoncé : il est immédiatement après le slot
et c'est le seul qui soit une égalité entre nombres. Les deux premiers, `10 k` et
`d = gcd(a, b)`, n'ont pas de destination établie et **demeurent en note**.

**B1-05 — §4.4, la relation PGCD × PPCM.** Le §4.4 annonce une « relation importante »
dont la formule est absente. Elle se trouve **en tête du tas du §5.1** :
`ppcm(a, b)` · `a, b =   0` · `gcd(a, b) ppcm(a, b) = ∣ab∣`. Les trois groupes y sont,
dans l'ordre. Restituée : `gcd(a, b) × ppcm(a, b) = ∣ab∣` pour `a, b ≠ 0`.

**B1-06 — §5.1, la propriété d'Euclide.** Le §5.1 annonce « la propriété : [ ] pour [ ] ».
Son tas porte, après les tokens du §4.4 déjà réclamés, `gcd(a, b) = gcd(b, a mod b)` et
`b =   0` — exactement les deux slots. Restituée :
`gcd(a, b) = gcd(b, a mod b)` pour `b ≠ 0`.

⚠️ **Un token renonce à être rattaché** : le `n` qui ouvre le tas du §5.1. Il demeure en note.

---

## 6. ⚠️ Ce que le lot ne fait PAS : les lignes 9 et 12

Vous m'aviez demandé de résoudre les deux lignes lacunaires. **Je n'y parviens pas, et je
préfère le dire que le forcer.**

Entre les tokens de la ligne 8 (`p p`) et ceux de la ligne 13 (`gˣ ≡ h (mod p)`), le tas
porte ce segment :

```
n   a   mod k   n k   > 0   a   = k   e
```

Il devrait couvrir la ligne 9 (« puissance modulo `n` » → exponentiation modulaire) et
la ligne 12 (« ordre d'un élément » → plus petit `k` tel que …). **Il ne s'y prête pas :**

| Obstacle | Détail |
|---|---|
| **Tokens surnuméraires** | `a = k` et `e` ne trouvent aucune place dans les deux slots attendus |
| **Ordre incompatible** | `a   mod k   n` se lit `a mod k` puis `n`, alors que la ligne 9 attend `a^k mod n` |
| **Exposants détruits** | toute restitution de `a^k` ou de `a^k ≡ 1` est une recomposition |
| **§13 en désaccord** | les identités d'exponentiation sont `a^{2k} = (a^k)^2` et `a^{2k+1} = a(a^k)^2`, qui ne correspondent pas à ce segment |

**Conclusion : les deux lignes restent vides, et les sept tokens demeurent en note.**
Un emplacement dont l'affectation n'est pas démontrable se laisse vide ; c'est la règle
que A a établie et que je ne transige pas ici.

**Ce qui permettrait de lever :** une lecture complète des §9, §13, §15 et §16, qui
traitent respectivement la primalité, l'exponentiation, les groupes et le logarithme
discret. Leurs tas n'ont pas encore été inventoriés en détail (l'inventaire ne couvrait
que sept zones). **C'est le travail du lot B-2.**

---

## 7. Vérification à sec

| Contrôle | Résultat |
|---|---|
| Diagnostic d'unicité (`python3 lot_commun.py build_lot_B_1.py`) | **6/6 sous-chaînes uniques** |
| Volume | 65 371 → **65 586** (+215) |
| Mojibake | **0** |
| Glyphes U+E020 restants | **0** (les trois consommés) |
| Sauts de ligne triples | **0** |
| Non-perte | tout token non rattaché demeure en note — aucun n'est supprimé |
| Non-régression du moteur | les générateurs de A passent toujours leur diagnostic |

**Le moteur a été généralisé** pour accepter une cible : `lot_commun.py` expose désormais
`FICHIER_B`, et `entre()`, `retirer()`, `diagnostiquer()` et `appliquer()` prennent un
paramètre `fichier` (défaut : A, donc **aucun lot existant n'est modifié**). Les
sauvegardes sont préfixées par la lettre du document, pour que B n'écrase pas celles de A.

---

## 8. Ce qu'il faut valider

Six substitutions, toutes de confiance haute. Deux points méritent votre attention
particulière :

1. **Les exposants re-composés** (lignes 13 et 14 du §3). C'est la seule part
   d'interprétation du lot. Si vous préférez qu'ils soient laissés vides ou marqués
   explicitement comme reconstitués, il suffit de le dire.
2. **La troisième propriété du §4.1**, où j'ai retenu « si `a ∣ b`, alors `a ∣ bc` »
   plutôt que la forme classique à deux conditions, contraint par le nombre de slots.
