# DOMAINE A — LOT 6 : EMPLACEMENTS VIDES SANS TOKEN CATALOGUÉ, ET CORRECTION D'UN LOT ANTÉRIEUR (§7.3, §13.3, §6.7)

**Date :** 2026-10-21 — **Statut :** **APPLIQUÉ LE 2026-10-21** — 4 restitutions + 1 correction (compte rendu en bas de document)
**Document source :** `Maths-vers-Informatiques/DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE.md`
**Inventaire de référence :** `domaine-A-inventaire-fragments.md`
**Contenu du lot :** **4 restitutions appliquées**, **1 correction d'un lot antérieur**, **12 emplacements vides recensés et laissés en l'état**

> ## ⚠️ LOT APPLIQUÉ LE 2026-10-21
>
> **Appliquées :** A6-01 / A6-01b (§7.3), A6-02 / A6-02b (§13.3).
> **Correction :** A5-02c (§6.7) — le lot 5 y avait laissé **deux notes collées**.
>
> Diff livré : `livrables/domaine-A-lot6.gitdiff` — diff **incrémental**, à appliquer
> **après** les lots 1 à 5. **5 substitutions**, 4 haute / 1 moyenne. Journal :
> `domaine-A-lot6.journal.json`. Générateur : `build_lot_A_6.py`.
>
> Ce lot **annule deux décisions antérieures** : A3-08/09 (§7.3) et A5-05 (§13.3).
> Les deux renversements sont argumentés ci-dessous et sont **réversibles**.

**Légende des actions :** **Combler** (emplacement vide explicite) · **Réattribuer** (fragment à déplacer) ·
**Corriger** (réparer une édition des lots précédents).

---

## Ce que ce lot a cherché, et ce qu'il a trouvé

Le lot 5 s'était conclu sur sept points laissés ouverts. La consigne était de les reprendre
**« dans un effet loop de manière structurée et complète »**. La boucle a donc été reprise
depuis le début — non pas en relisant les conclusions du lot 5, mais en **refaisant
l'inventaire du document**.

Trois constats, dans l'ordre où ils sont apparus :

1. **Un scan exhaustif des piles de tokens ne montre plus que deux tas** : `;  n   n` (§9.3)
   et `P   →   Q` (§30). Les 42 triples espaces recensés au lot 5 étaient, pour
   l'écrasante majorité, de la simple mise en page de listes (`1.   Qu'est-ce que c'est ?`).
   **Une quête par les espaces est une impasse** ; une quête par les *formes* (`n   n`,
   `P   →   Q`) est immédiate.
2. **Un emplacement vide peut n'être annoncé par aucune pile.** L'« Exemple conceptuel : » du
   §7.3 était vide, et rien dans le document ne le signalait. Il a fallu **vider la section et
   la lire**. — *Le compte rendu du lot 5 disait « deux emplacements vides au §13.3 » ; il en
   manquait un troisième, ailleurs.*
3. **La position d'une pile ne fait pas foi quand le contenu la contredit.** C'est ce qui
   renverse A5-05.

---

## La méthode retenue : chercher les emplacements, pas les fragments

L'inventaire initial (`inventorier_fragments.py`) rapporte 103 fragments. **Il est inutilisable
en l'état** : l'essentiel de ces « fragments » sont des séparateurs de tableaux (`| |`) ou des
notations parfaitement en place (`f : A → B`). Chercher les gîtes par ce moyen noie le signal.

La méthode substituée, employée pour ce lot :

| Étape | Outil | Résultat |
|---|---|---|
| 1. Recenser les piles | regex ciblée sur les formes connues | **2** tas (`n   n`, `P   →   Q`) |
| 2. Recenser les vides | `:` + 2 espaces + **un autre libellé** dans les 45 caractères | **9** candidats |
| 3. **Vider et lire** le voisinage de chaque candidat | dump de la section | arbitrage |

L'étape 3 est la seule qui décide. **Aucune proposition de ce lot n'a été établie sans avoir lu
la section entière.**

---

## Restitutions appliquées (4)

### A6-01 et A6-01b · §7.3 — L'exemple de la factorielle

**Action :** Réattribuer · **Fragment :** bloc de code `python` égaré en tête du §8
**Confiance : haute** · **Renverse :** A3-08 / A3-09 (lot 3)

**Source.** Le §8 (« ENSEMBLES, FONCTIONS ET DÉNOMBRABILITÉ ») s'ouvrait, après les deux
retraits du lot 5, sur un bloc de code seul :

```python
def factorielle(n):
    if n = 0:
        return 1
    else:
        return n × factorielle(n - 1)
```

Et le §7.3 se lisait :

> 7.3 Récursion informatique  Une fonction récursive se définit en faisant appel à elle-même,
> directement ou indirectement.  **Exemple conceptuel :**  Deux éléments indispensables : un ou
> plusieurs cas de base ; un appel récursif qui progresse vers un cas de base.

**Trois observations.**

1. **L'emplacement « Exemple conceptuel : » du §7.3 est vide.** Ce qui le suit —
   « Deux éléments indispensables : » — est un *autre* libellé : c'est la signature d'emplacement
   vide établie au lot 5.
2. **Le texte qui suit nomme exactement ce que contient le code.** « Un ou plusieurs cas de
   base » = `if n = 0: return 1`. « Un appel récursif qui progresse vers un cas de base » =
   `return n × factorielle(n - 1)`. La section décrit un exemple qu'elle n'a pas.
3. **Le tas du §8 était un débordement de la FIN du §7, pas de son début.** Le lot 5 en a déjà
   tiré la phrase d'invariant du **§7.4**. Il est désormais établi que ce tas portait toute la
   queue du §7 — l'invariant (§7.4) *et* le code (§7.3).

**Proposition.** Porter le bloc de code au §7.3, en bloc `python` délimité :

> **Exemple conceptuel :**
>
> ```python
> def factorielle(n):
>     if n = 0:
>         return 1
>     else:
>         return n × factorielle(n - 1)
> ```
>
> Deux éléments indispensables : un ou plusieurs cas de base ; un appel récursif qui progresse
> vers un cas de base.

**Ce que le §8 devient.** Un titre de section suivi directement de son §8.1. Une section qui ne
traite plus que de son sujet.

**Sur l'erreur `if n = 0`.** Le code porte `if n = 0:` là où Python exige `if n == 0:`.
L'erreur est **conservée telle quelle** : elle est dans la source, et la corriger serait
réécrire l'auteur. Elle est signalée ici, et nulle part dans le document.

**Pourquoi A3-08/09 est renversé.** Le lot 3 traitait ce code comme un simple reformatage sur
place. C'était la conclusion raisonnable **tant que l'emplacement vide du §7.3 n'avait pas été
repéré**. Il l'est désormais. **Réversible** : si le porteur préfère l'ancien montage, A6-01 et
A6-01b sont à annuler ensemble.

---

### A6-02 et A6-02b · §13.3 — L'exemple de type produit

**Action :** Combler · **Fragment :** `Utilisateur = (nom, email, age)`
**Confiance : moyenne** · **Renverse partiellement :** A5-05 (lot 5)

**Source.** Le §13.3 se lisait, *après* la description du type somme :

> 13.3 Types algébriques et types somme/produit  **Type produit**  Regroupe plusieurs
> composants.  **Exemple conceptuel :**  **Type somme**  Représente une valeur choisie parmi
> plusieurs variantes.  `Utilisateur = (nom, email, age)`
>
> **Exemple conceptuel :**  Ces représentations sont utiles pour modéliser des données
> structurées.

**Le conflit.** La pile `Utilisateur = (nom, email, age)` gît **après** le type somme, ce qui
avait conduit le lot 5 à refuser les deux emplacements : la position suggérait le somme, le
contenu dit le produit, et l'indécision avait tranché pour l'abstention.

**Ce qui tranche.** `Utilisateur = (nom, email, age)` est **sans ambiguïté un produit** : c'est
un enregistrement de trois composantes nommées. Un type somme s'écrirait
`Utilisateur = Admin | Invité`. **Le contenu l'emporte sur la position de la pile** — celle-ci
s'est révélée peu fiable à chaque lot (§7.4, §8, §6.5).

**Proposition.** Remplir le **premier** emplacement ; **conserver le second vide**.

**Réserve explicite.** La confiance est *moyenne* et non *haute* : l'attribution au premier
emplacement repose sur le contenu, contre l'indice de position. Aucun second fragment de type
somme n'existe dans le document — le second emplacement restera vide **faute de token
disponible**, ce qui est la conclusion correcte, non un renoncement.

---

## Correction d'un lot antérieur (1)

### A5-02c · §6.7 — La note était en double depuis le lot 5

**Action :** Corriger · **Confiance : haute**

**Ce qui s'est passé.** Le lot 5 (A5-02b) mettait à jour la note du §6.7 : `a` et `¬P(a)` venaient
d'être recasés au §6.5, il n'y avait donc plus lieu de les signaler, et `∀x, P(x)` restait seul
sans destination.

L'édition a été montée avec `entre()`, **qui conserve son marqueur amont**. Le marqueur amont
était la note elle-même. La nouvelle note s'est donc écrite **à la suite de l'ancienne** :

> `*Fragments non rattachés, conservés faute de destination établie :* `∀x, P(x)` · `a` · `¬P(a)`
> `*Fragment non rattaché, conservé faute de destination établie :* `∀x, P(x)``

Deux notes, dont une fausse. Le contrôle de non-perte du lot 5 portait sur les tokens — il
n'avait pas détecté la duplication, car **aucun token n'était perdu** : ils étaient simplement
cités deux fois.

**Détection.** Par un comptage de routine : `` `∀x, P(x)` `` attendu 1 fois, trouvé 2.

**Correction.** La note ne cite plus que `∀x, P(x)` :

> `*Fragment non rattaché, conservé faute de destination établie :* `∀x, P(x)``

**Aucun token n'est supprimé** : `a` et `¬P(a)` sont bien recasés au §6.5, vérifiés présents.

**Leçons consignées.**

1. `entre()` conserve ses deux marqueurs ; `retirer()` supprime aussi l'amont. Le bon montage
   était ici de prendre **la phrase qui précède** la note comme marqueur amont. Les deux
   fonctions sont documentées l'une par rapport à l'autre dans `lot_commun.py`.
2. **Un contrôle de non-perte ne détecte pas une duplication.** Il faut aussi compter les
   occurrences. Le contrôle est désormais systématique.
3. C'est la **troisième** erreur de montage de ce type en six lots. Un commentaire le consigne
   dans `build_lot_A_5.py`.

---

## Emplacements vides recensés et laissés en l'état (12)

Ces emplacements sont **vides dans la source** et **aucun token disponible ne peut les
combler**. Les remplir serait rédiger à la place de l'auteur. Ils sont listés pour que le
porteur sache exactement ce qui reste, et pour que personne n'ait à refaire la revue.

| # | Section | Emplacement vide | Ce qui manque | Pourquoi rien n'est proposé |
|---|---|---|---|---|
| 1 | §30 Q2 | « Que signifie `  ` ? » | une notation | aucun token orphelin ; le `P → Q` du §30 est **un fragment déplacé**, pas le contenu de la question |
| 2 | §3.x | « Si tu rencontres : `  ` » | `P → Q` | le seul `P → Q` disponible est §30, **à 50 000 caractères** — attribution gratuite |
| 3 | §3.x | « l'hypothèse `  ` ? » | `P` | idem |
| 4 | §3.x | « la conclusion `  ` ? » | `Q` | idem |
| 5 | §4.x | propositions « par : `  ` » | `P`, `Q` | idem |
| 6 | §4.5 | « Deux formes classiques sont utiles : `  ` » | les deux formes | aucun token |
| 7 | §5.x | existence / unicité | — | aucun token |
| 8 | §9.3 | `;  n   n` | un symbole relationnel | **un symbole est perdu** : restituer serait inventer |
| 9 | §12.3 | « Trois approches classiques : `  ` » | les trois approches | aucun token |
| 10 | §16.6 | « Règle : `  ` » | la règle | aucun token |
| 11 | §16.6 | « Légende : `  `  Directe : » | la légende | aucun token |
| 12 | §13.3 (2e) | 2e « Exemple conceptuel : » | un exemple de type **somme** | aucun token de type somme dans le document |

**S'y ajoutent**, conservés par principe et déjà documentés : l'étape 3 du §17.5 (relève de la
rédaction), le `∀x, P(x)` du §6.7 (aucune destination établie), l'orphelin `n` du §15.6,
le `2 + 3 × 4` du §14.2 (A4-05), et l'accolade fermante absente du §10.6.

---

## Récapitulatif du lot 6

| ID | Section | Action | Confiance | Effet |
|---|---|---|---|---|
| A6-01 | §7.3 | Réattribuer (bloc de code) | haute | emplacement « Exemple conceptuel » comblé |
| A6-01b | §8 | Réattribuer (retrait) | haute | §8 rendu à son sujet |
| A6-02 | §13.3 | Combler (1er emplacement) | moyenne | `Utilisateur = (nom, email, age)` recasé |
| A6-02b | §13.3 | Réattribuer (retrait) | haute | pile retirée |
| A5-02c | §6.7 | Corriger | haute | note dédoublée |

**Bilan :** 4 restitutions, 1 correction, 0 invention, 0 perte.

---

## Compte rendu d'application (2026-10-21)

### Ce qui a été appliqué

Les cinq éditions, par `build_lot_A_6.py`, sur l'état post-lot 5 restauré depuis
`_audit/sauvegardes/A-avant-domaine-A-lot6.md` (78 849 caractères).

### Une troisième erreur de montage, détectée, corrigée

L'anomalie a été trouvée **après** la première exécution du lot : la note du §6.7 était en
double. Plutôt que de réparer à la main, le choix a été fait de **restaurer la sauvegarde
pré-lot 6 et de rejouer le générateur** avec la correction (A5-02c) ajoutée à la liste. Le
résultat est donc **reproductible depuis la sauvegarde**, et non une réparation manuelle.

C'est la troisième occurrence du même piège — `entre()` conserve son marqueur amont — en six
lots. Le commentaire est consigné dans `build_lot_A_5.py`, au plus près de l'édition fautive.

### Vérifications

| Contrôle | Résultat |
|---|---|
| Diagnostic préalable (`python3 lot_commun.py build_lot_A_6.py`) | 5/5 sous-chaînes uniques |
| Mojibake | 0 |
| Rejeu du générateur depuis la sauvegarde pré-lot 6 | **conforme** |
| Segments appliqués (contrôle positif) | 4/4 présents 1 fois |
| Segments retirés (contrôle négatif) | 2/2 absents |
| Points non retenus, contrôle d'intégrité | §30, §9.3, §17.5, §6.7, §3.2, §15.6 — 6/6 **intacts** |
| Note du §6.7 | 1 occurrence (après correction) |
| Tokens `a` et `¬P(a)` | présents au §6.5 — non supprimés |
| Chaîne de volumes | 77 970 → 78 776 → 78 789 → 78 758 → 78 767 → 78 849 → **78 756** |

### État du document A après six lots

| Lot | Sections | Substitutions | Commit |
|---|---|---:|---|
| 1 | §2–§4 | 11 | `fa45e60` |
| 2 | §5–§7 | 12 | `9828faf` |
| 3 | §8, §10 | 16 | `8ad13bc` |
| 4 | §11–§18 | 19 | `b8ee095` |
| 5 | points ouverts | 7 | `4ae69bf` |
| 6 | vides sans token + correction | 5 | ce commit |
| **Total** | | **70** | |
