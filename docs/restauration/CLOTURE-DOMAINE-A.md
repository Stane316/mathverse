# CLÔTURE DU DOMAINE A — RESTAURATION

**Date :** 2026-10-21 — **Décision du porteur :** clore A et passer à B
**Document :** `Maths-vers-Informatiques/DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L'INFORMATIQUE.md`
**Lots :** 1 à 6 — **70 substitutions** — chaîne des volumes
77 970 → 78 776 → 78 789 → 78 758 → 78 767 → 78 849 → **78 756**
**Fiche d'audit :** `docs/audit/fiches/domaine-A-logique-et-fondements.md`

---

## 1. Ce que cette clôture est, et ce qu'elle n'est pas

**Ce qu'elle est :** l'arrêt, décidé par le porteur, du travail de restitution sur A. Elle
enregistre ce qui a été fait, ce qui reste, et **pourquoi** ce qui reste reste.

**Ce qu'elle n'est pas :**
- ❌ **Ce n'est pas une validation.** Aucun contenu restitué n'a été approuvé bloc par bloc par
  le porteur. Les 70 substitutions portent chacune un niveau de confiance ; plusieurs sont
  *moyennes*.
- ❌ **Ce n'est pas une récupération.** Les formules déplacées ont été **réattribuées** par
  argument, pas retrouvées. Ce qui est écrit est une proposition argumentée.
- ❌ **Ce n'est pas un constat d'achèvement.** Trente items demeurent, mesurés et lus ci-dessous
  (§4). Un d'entre eux au moins est **réouvrable** (§5).

---

## 2. Ce qui a été fait

| Lot | Sections | Substitutions | Commit | Diff |
|---|---|---:|---|---|
| 1 | §2–§4 | 11 | `fa45e60` | `domaine-A-lot1.gitdiff` |
| 2 | §5–§7 | 12 | `9828faf` | `domaine-A-lot2.gitdiff` |
| 3 | §8, §10 | 16 | `8ad13bc` | `domaine-A-lot3.gitdiff` |
| 4 | §11–§18 | 19 | `b8ee095` | `domaine-A-lot4.gitdiff` |
| 5 | points ouverts | 7 | `4ae69bf` | `domaine-A-lot5.gitdiff` |
| 6 | vides sans token + correction | 5 | `fdb9aa5` | `domaine-A-lot6.gitdiff` |
| **Total** | | **70** | | |

**Nature du travail.** A est aplati : 119 lignes pour 78 Kio, **0 titre, 0 bloc d'équation, 0
puce**. Les formules n'ont pas été supprimées mais **déplacées** hors de leur emplacement. Le
chantier a donc consisté à **réattribuer** des fragments à des emplacements vides, jamais à
rédiger.

**Le plan a été reconstruit par détection** (« `NN. TITRE` » en texte) : **35 sections sur 35**,
sans perte.

**Le risque dominant n'était pas l'invention mais la mauvaise attribution.** C'est pourquoi
chaque lot a été soumis avant application, et pourquoi les confiances sont graduées.

### Vérifications

| Contrôle | Résultat |
|---|---|
| Mojibake | **0** |
| Rejeu intégral depuis les sauvegardes | conforme, lot 6 rejoué debout après correction |
| Couverture des autres documents | 1 146 blocs, 78 sans contenu, **écart nul** |
| Reconstitution du clone après réinitialisation | 17/17 diffs + 6/6, A = 78 756, **reproduit** |

---

## 3. Les trois leçons de méthode que A laisse

**3.1 Un emplacement vide peut n'être annoncé par aucune pile.** L'« Exemple conceptuel : » du
§7.3 était vide et rien ne le signalait. Il a fallu vider la section et la lire. Aucun scan ne
l'a trouvé.

**3.2 La position d'une pile ne fait pas foi quand le contenu la contredit.** `Utilisateur =
(nom, email, age)` gisait après la description du type somme ; c'est un **produit**. Le contenu a
tranché (lot 6). La position s'était révélée peu fiable à chaque lot.

**3.3 Le comptage par les espaces est une impasse dans ce document.** Mesuré ici :
**425** séquences de 3 espaces, **1 452** trous inter-phrases de 2 espaces. Le signal est noyé
dans la mise en page — le document est aplati, ses paragraphes et ses listes sont séparés par des
espaces doubles. **Aucun de ces deux comptages n'a servi à une seule décision.** Tout ce qui est
établi ci-dessous l'a été par lecture.

> ⚠️ C'est la **cinquième** occurrence, dans ce chantier, d'une figure publiée sans la règle qui
> l'a produite. Une mesure qui ne dit pas sa règle n'est pas une mesure.

---

## 4. Le résidu — mesuré, lu, et non rappelé

**Trente items** : 28 emplacements vides et 2 tas de tokens. Ce chiffre **corrige** une estimation
antérieure de 12, établie par motif et non par lecture.

| # | Section | Emplacement | Ce qui manque |
|---:|---|---|---|
| 1–7 | **§3.1** | « Si tu rencontres : · l'hypothèse ? · la conclusion ? · démontrer , sa réciproque · Attention : ne signifie pas que cause . » | `P → Q` ×3, `P` ×2, `Q` ×2 |
| 8–10 | **§3.2** | « penser à . » ×3 | `∀`, `∃`, `∃!` |
| 11 | **§3.2** | « Exemples :  Signification : » | un exemple |
| 12–15 | **§4.1** | « propositions par : · Exemple : : « …authentifié. » · : « …page privée. » · Une règle pourrait être : » | `P`, `Q`, `P → Q` |
| 16–18 | **§4.4** | « Exemples :  est une tautologie / contradiction / contingence » | 3 formules-exemples |
| 19 | **§4.5** | « Exemple de FNC :  Un littéral est… » | une forme normale conjonctive |
| 20 | **§7.2** | « pas seulement de . » | `n − 1` |
| 21 | **§9.3** | `n   n` | ⚠️ **le symbole relationnel est perdu** |
| 22–23 | **§10.2** | « distinguer la  correction partielle … de la  correction totale » | 2 tokens |
| 24 | **§10.6** | « une  fonction de terminaison » | 1 token |
| 25 | **§13.3** | 2ᵉ « Exemple conceptuel : » | un exemple de type **somme** |
| 26–27 | **§15.3** | « exponentiellement avec , · Limite :  devient coûteuse » | `n` et un sujet |
| 28 | **§17.5** | Étape 3 — Implémentation conceptuelle | ⚠️ relève de la **rédaction** |
| 29 | **§30** Q2 | « Que signifie ? » | 1 token |
| 30 | **§30** | `P   →   Q` | tas conservé, destination non établie |

**Fragments conservés par principe**, signalés dans le document même :
`∀x, P(x)` (§6.7) · `n` (§15.6) · `2 + 3 × 4` (§15) · `P → Q` · `P Q P → Q P → Q P Q` · `∀x …` (§3.2).

**Pertes définitives.** Le §9.3 : le symbole qui reliait les deux `n` ne figure dans aucun
fragment. Le restituer serait une **invention** — A3-10 est confirmé.

---

## 5. ⚠️ Un item réouvrable : §3.1 et §3.2, correspondance exacte

**C'est le seul point de cette clôture qui n'est pas une conclusion mais une question laissée au
porteur.**

Le lot 1 avait laissé en §3.2 une note de fragments non rattachés :

> *Fragments non rattachés, conservés faute de destination établie :* `P → Q` · `P Q P → Q P → Q P Q` · `∀x …`

**Or le §3.1 réclame exactement le compte de ces fragments.**

Le tas `P Q P → Q P → Q P Q` se décompose en **six tokens** — `P`, `Q`, `P → Q`, `P → Q`, `P`,
`Q` — auxquels s'ajoute le `P → Q` isolé de la note, soit **sept tokens** :
**3 × `P → Q`, 2 × `P`, 2 × `Q`**.

Le §3.1 présente **sept emplacements vides** qui demandent exactement :
**3 × `P → Q`, 2 × `P`, 2 × `Q`**.

| Ordre | Emplacement du §3.1 | Token |
|---:|---|---|
| 1 | « Si tu rencontres : » | `P → Q` |
| 2 | « l'hypothèse ? » | `P` |
| 3 | « la conclusion ? » | `Q` |
| 4 | « démontrer , sa réciproque » | `P → Q` |
| 5 | « Attention :  ne signifie pas que » | `P → Q` |
| 6 | « cause » (sujet) | `P` |
| 7 | « cause  » (objet) | `Q` |

**Les deux multisembles coïncident exactement.** Deux réserves, énoncées avant toute proposition :

1. **L'ordre de la pile ne suit pas l'ordre des emplacements.** La pile commence par `P`, `Q` ;
   le premier emplacement veut `P → Q`. La correspondance est donc **par le contenu**, non par la
   position — ce que la doctrine du chantier admet explicitement (§3.2 ci-dessus).
2. **Les trois « penser à . » du §3.2** demandent `∀`, `∃`, `∃!`, que **la table immédiatement
   au-dessus dicte** (« Pour tout » → `∀`, « Il existe au moins un » → `∃`, « Un unique » → `∃!`).
   Le rattachement serait ici fondé sur une évidence interne au document, non sur un fragment
   déplacé — ce qui le rapproche d'une **restitution déduite**, à valider comme telle.

**Pourquoi ce n'est pas appliqué.** La clôture a été décidée ; ce point n'avait pas été identifié
quand elle l'a été. Il est **inscrit ici pour ne pas être perdu**, et soumis : il constituerait un
**lot 7 d'une dizaine de propositions**, dont sept de confiance *haute* par correspondance de
compte, et trois de confiance *moyenne*.

---

## 6. État final et transmission

A est **clos** au sens du §1 : le travail s'arrête, il n'est pas achevé. Le document est
**utilisable** — 35 sections reconstruites, les tables de vérité relues et correctes, le
vocabulaire de la couche de preuve présent.

**La méthode fixée au §11 de la fiche A est validée sur un document** et s'applique désormais
identiquement à **B, C et D** :

1. profiler d'abord (`profil_degradation.py`), jamais juger par impression ;
2. reconstruire le plan par **détection** des intitulés, jamais par échantillonnage ;
3. lire les sections porteuses, pas le document linéairement ;
4. séparer les trois mécanismes récupérables du déplacement des formules ;
5. vérifier les objets contrôlables et dire lesquels l'ont été ;
6. **ne jamais compter les blocs pour juger de l'intégrité.**

**Documents de référence :** fiches `domaine-A-logique-et-fondements.md` (§11 méthode) ·
inventaire `domaine-A-inventaire-fragments.md` · propositions `domaine-A-lot1.md` … `lot6.md` ·
journaux `domaine-A-lot*.journal.json` · diffs et messages `livrables/domaine-A-lot*`.

---

## 7. Procédure de reconstitution — troisième épreuve

Le clone du corpus ayant été détruit deux fois par des réinitialisations du sandbox, la procédure
est désormais **scriptée** :

```
bash tools/restauration/reconstituer_atelier.sh
```

Restaure la branche depuis origin, recloune le corpus à `f0f5e2d`, réapplique les 17 diffs dans
l'ordre non interchangeable, puis les 6 lots de A en séquentiel, vérifie l'absence de mojibake et
le volume de A, et pose un point de reprise. **Éprouvé : 17/17, 6/6, A = 78 756, écart nul.**
