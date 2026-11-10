# DOMAINE B — INVENTAIRE DES FRAGMENTS DE FORMULES DÉPLACÉES

**Date :** 2026-10-21 — **Chantier :** restauration, phase 1 — **Statut :** **mesure et lecture. Aucune restitution appliquée**
**Source :** `Maths-vers-Informatiques/DOCUMENT B — THÉORIE DES NOMBRES.md` (clone `f0f5e2d`)
**Outils :** `tools/audit-phase1/profil_degradation.py`, relevés ciblés
**Règle :** aucune restitution n'est appliquée sans validation expresse, lot par lot.

---

## 1. Objet

Ce document est l'inventaire de ce que la dégradation a fait au document B. Il ne restaure rien :
il **mesure et trie**. Les restitutions seront proposées dans des lots séparés, soumis un par un.

Il fait pour B ce que `domaine-A-inventaire-fragments.md` a fait pour A — et il en reprend la
méthode, y compris ses leçons.

---

## 2. Profil mesuré

```
python3 tools/audit-phase1/profil_degradation.py "<fichier-B.md>"
```

| Mesure | Valeur | Comparaison A |
|---|---:|---|
| Caractères / octets | 65 371 / 68 220 | 78 756 / 82 523 |
| Lignes | **103** | 119 |
| Caractères par ligne non vide | **1 257** | 686 |
| Titres Markdown `^#` | **0** | 0 |
| Blocs `\[…\]` | **0** | 0 |
| Gras `**` | **0** | 0 |
| Puces | **0** | 0 |
| Backslashes / backticks / pipes | **0 / 0 / 2** | — |
| Runs de 2 espaces | 1 281 | — |
| Runs de 3 espaces et plus | 949 | 425 (sur un texte plus long) |
| **Diagnostic** | **aplanie** | aplanie |

**Lecture :** B est **plus densément aplati que A** — 1 257 caractères par ligne contre 686. Le
régime est le même (régime 3), le degré est plus sévère.

**Différence importante avec A : B ne porte aucun résidu LaTeX** (0 backslash, 0 backtick). Les
formules n'ont pas laissé de délimiteurs ; elles ont été **réécrites en texte**. La restauration
ne pourra donc pas s'appuyer sur des délimiteurs retrouvés, seulement sur l'ordre et le contenu
des tokens.

**Vocabulaire de preuve** (occurrences pour 10 000 caractères) : `algorithme` 63 (9,6) ·
`test` 30 (4,6) · `limite` 22 (3,4) · `complexité` 18 (2,8) · `preuve` 8 (1,2) ·
`hypothèse` 7 (1,1) · `erreur` 3 · `validation` 1 · `contre-exemple` **0**.

---

## 3. Le plan reconstruit

La numérotation `N. TITRE` survit en texte. Elle est **invisible à tout outil** faute de
balisage, mais elle est détectable et complète.

### 3.1 Trente-six sections de niveau 1

| N° | Section | N° | Section |
|---:|---|---:|---|
| 0 | Objectif du document | 18 | Cartographie des théorèmes et propriétés phares |
| 1 | Carte générale du domaine B | 19 | Répertoire des algorithmes phares |
| 2 | Vocabulaire fondamental | 20 | Cryptographie : des fondements aux protocoles |
| 3 | Les formules de reconnaissance essentielles | 21 | Application informatique générale |
| 4 | Divisibilité et arithmétique élémentaire | 22 | Application au Web |
| 5 | Algorithme d'Euclide et Euclide étendu | 23 | Connexions avec les autres domaines A → V |
| 6 | Identité et théorème de Bézout | 24 | Matrice centrale |
| 7 | Congruences et arithmétique modulaire | 25 | Algorithmes et méthodes : fiches de reconnaissance |
| 8 | Inverses modulaires | 26 | Catalogue des futures fiches individuelles |
| 9 | Nombres premiers | 27 | Projets d'application du domaine B |
| 10 | Principaux algorithmes liés aux nombres premiers | 28 | Expérimentations personnelles |
| 11 | Théorèmes de Fermat et d'Euler | 29 | Ordre d'apprentissage recommandé |
| 12 | Théorème des restes chinois | 30 | Questions de maîtrise du domaine B |
| 13 | Exponentiation rapide et exponentiation modulaire | 31 | Challenge sans IA et avec IA |
| 14 | Équations diophantiennes | 32 | Checklist de reconnaissance |
| 15 | Groupes, classes modulo et lien avec R | 33 | Références et ressources |
| 16 | Logarithme discret | 34 | Ce que tu dois retenir du domaine B |
| 17 | Courbes elliptiques et arithmétique | 35 | Suite logique du parcours |

**95 sous-sections** `N.N` détectées.

⚠️ **Un piège, rencontré et levé.** Une extraction naïve par « `N.` suivi d'une majuscule »
donne 88 candidats, dont une trentaine sont des **listes numérotées internes** (« 1. choisir deux
grands nombres premiers ; 2. calculer… »). Le plan n'a été établi qu'en suivant la suite
croissante 0 → 35. C'est le même piège que les listes numérotées d'A.

### 3.2 Concordance

Le README (`docs/restauration/README.md` §2) annonçait pour B : **95 sections**, **155 slots**,
**22 lignes à runs**, **19 grecques**, **0 exposant**.
→ **95 sous-sections : confirmé. 155 slots : confirmé. 0 exposant : confirmé. 19 grecques :
confirmé** (toutes sont `φ`, l'indicatrice d'Euler).

---

## 4. Les piles de formules — 14 runs porteurs de mathématique

Relevé par recherche de runs contenant au moins deux opérateurs et deux séparateurs d'espaces,
puis **lecture de chacun**.

| # | @ | Section | Contenu du run |
|---:|---:|---|---|
| 1 | 5 495 | §2 Vocabulaire | `, n  a b  a ∣ b  k  b = a…` — divisibilité |
| 2 | 6 561 | §3 Formules | `a = bq + r , 0 ≤ r < b` — division euclidienne |
| 3 | 7 882 | **§4.2 Critères de divisibilité** | **la pile majeure — voir §5** |
| 4 | 7 920 | §4.2 | `≤ r < b  g` — suite |
| 5 | 8 158 | §4.1 Propriétés | `e i  a ∣ b  b ∣ c  a ∣ c` — transitivité |
| 6 | 8 199 | §4.1 | `a ∣ b  a ∣ c  a ∣` — combinaison linéaire |
| 7 | 8 255 | §4.1 | `a ∣ b  a ∣ b` |
| 8 | 8 282 | §4.1 | `a ∣ b  b =` — avec glyphe perdu |
| 9 | 14 038 | §7 Congruences | `a + c ≡ b + d (mod n)` · `ac ≡ bd (mod n)` |
| 10 | 17 401 | §9 Nombres premiers | `2 ≤ d ≤ n` · `n` |
| 11 | 20 719 | §11 Fermat / Euler | `p ∤ a  a ≡` · `a ≡` |
| 12 | 21 540 | §11 | `1 ≤ k ≤ n` |
| 13 | 21 576 | §11 | `φ` |
| 14 | 21 617 | §11 | `= p −` |

**Constat :** les runs 3 à 8 sont **un seul et même tas**, que le découpage automatique a
fractionné. Il n'y a donc pas 14 piles mais **7 zones**, dont une majeure (§4.2).

---

## 5. ⚠️ Découverte structurante : la pile du §4.2 suit l'ordre de la table du §3

**C'est le fait le plus important de cet inventaire.**

Le §3 « Les formules de reconnaissance essentielles » est un tableau à trois colonnes —
« Si tu rencontres… » · « Pense à… » · « Formule ou caractérisation » — dont **la troisième
colonne est vide** pour la plupart des lignes.

Le §4.2 « Critères de divisibilité usuels » se termine par un tas de formules.

**Ces deux objets sont dans le même ordre.**

| # | Ligne du §3 (« Pense à… ») | Colonne 3 attendue | Fragment du tas, dans l'ordre |
|---:|---|---|---|
| 1 | Divisibilité | `a ∣ b` | `a   b` · `b = ak, k ∈ Z` |
| 2 | Division euclidienne | `a = bq + r, 0 ≤ r < b` | `a = bq + r , 0 ≤ r < b` |
| 3 | PGCD | `gcd(a, b)` | `gcd( a ,   b )` · `a   b` |
| 4 | Bézout | `ax + by = gcd(a, b)` | `ax + by = gcd( a ,   b )` |
| 5 | Coprimalité | `gcd(a, n) = 1` | `a   n` · `gcd( a ,   n ) = 1` |
| 6 | Congruence | `a ≡ b (mod n)` | `n` · `a ≡ b (mod n )` |
| 7 | Inverse modulaire | `ax ≡ 1 (mod n)` | `n` · `ax ≡ 1 (mod n )` |
| 8 | Primalité | *présent* : « ses seuls diviseurs positifs sont 1 et p » | `p p` |
| 9 | Exponentiation modulaire | *à établir* | `n` · `a mod k` · `n` · `k > 0` · `a = k` |
| 10 | Fermat ou Euler | *à établir* | `e g ≡ x   h (mod p )` |
| 11 | Restes chinois | *présent* : « compatibilité et reconstruction » | — |
| 12 | Théorie des groupes | *partiel* : « plus petit k tel que… » | — |
| 13 | Logarithme discret | *présent* : « recherche d'un exposant » | — |
| 14 | Factorisation | `n = ∏ p_i^{e_i}` | `n = p ∏   i e   i` |

**Le tas se poursuit** au-delà de la table par les propriétés de la divisibilité —
transitivité `a∣b, b∣c ⟹ a∣c`, combinaison linéaire `a∣(ub + vc)`, et `a∣b, b ≠ 0 ⟹ |a| ≤ |b|`
— qui relèvent du **§4.1 « Propriétés fondamentales »**, section immédiatement **avant** le §4.2
qui les héberge.

**Deux réserves, énoncées avant toute proposition :**

1. **Les lignes 9 et 10** (exponentiation modulaire, Fermat/Euler) sont les seules dont
   l'appariement n'est pas évident : les fragments correspondants du tas sont lacunaires
   (`a mod k`, `k > 0`, `a = k`, `e g ≡ x h (mod p)`). Leur recomposition exigera une lecture
   serrée des §11 et §13, qui traitent ces notions en détail.
2. **Les exposants sont détruits** dans tout le document (0 occurrence de `² ³ ⁿ`). La
   factorisation `n = ∏ p_i^{e_i}` et le petit théorème de Fermat `a^{p−1} ≡ 1` ne peuvent donc
   être restitués **qu'avec des exposants re-composés** — c'est-à-dire avec une part
   d'interprétation, à signaler comme telle.

---

## 6. Les pertes définitives

### 6.1 Trois glyphes perdus — tous identifiables

La zone à usage privé Unicode (U+E000–U+F8FF) compte **3 occurrences**, toutes `U+E020`, toutes
dans un contexte qui lève l'ambiguïté :

| @ | Contexte | Glyphe |
|---|---|---|
| 8 300 | `a   ∣   b   b   =   0   ∣ a ∣ ≤ ∣ b ∣` | **`≠`** |
| 10 562 | `ppcm( a ,   b )  a ,   b   =   0` | **`≠`** |
| 10 657 | `gcd( a ,   b ) = gcd( b ,   a   mod   b )  b   =   0` | **`≠`** |

Les trois sont `b ≠ 0` (ou `a, b ≠ 0`), condition de validité usuelle de la division euclidienne
et du PGCD. Le README l'annonçait (« `≠` est perdu ») ; l'inventaire le **localise et le compte**.

⚠️ Restituer `≠` ici n'est pas une invention : c'est la levée d'une perte d'encodage, dont le
contexte dicte le glyphe. Ce point sera proposé au lot 1, avec les trois localisations.

### 6.2 Les exposants

**0 occurrence** de `² ³ ⁿ` dans les 65 371 caractères. Toute restitution d'un exposant est une
**recomposition**, pas une récupération. Elle doit être signalée comme telle.

### 6.3 Les lettres grecques

19 occurrences, **toutes `φ`**. Aucune autre grecque ne survit. Un document de théorie des
nombres sans `φ` ailleurs que dans l'indicatrice d'Euler est cohérent avec le sujet ; il n'y a
donc pas lieu de supposer une perte massive ici, contrairement au document C (80 grecques).

---

## 7. Ce que l'inventaire ne fait pas

- Il ne **propose** aucune restitution. Les propositions viendront par lots.
- Il ne **compte pas les blocs** pour juger de l'intégrité : B n'a aucun bloc. Comme pour A, le
  comptage serait trompeur.
- Il ne prétend pas à l'**exhaustivité** des 155 slots : seules les zones porteuses ont été lues
  en détail (§2, §3, §4.1, §4.2, §7, §9, §11). Les sections 12 à 35 n'ont pas encore été lues
  slot par slot.

**Prochaine étape :** lot B-1 — la table du §3 et les propriétés du §4.1, soit quatorze lignes
de tableau plus trois glyphes, à partir d'un tas dont l'ordre est établi.
