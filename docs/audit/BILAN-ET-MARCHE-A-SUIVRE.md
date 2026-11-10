# BILAN EXHAUSTIF ET MARCHE À SUIVRE

**Date :** 2026-10-21 — **Branche :** `arena/2e20eccb-mathverse` — **HEAD :** `1da8ece`
**Objet :** où nous sommes, ce qui a été fait, ce qui reste, et dans quel ordre nous avançons.

---

## 1. Réponse courte : où nous en sommes

| Phase | Objet | Statut |
|---|---|---|
| **Phase 0** | Vérification des accès et du périmètre | ✅ **terminée** |
| **Phase 1** | Audit documentaire des 29 documents | 🟡 **en cours — 6 fiches sur 29** |
| **Phase 2** | Veille concurrentielle et licences | ✅ **terminée** — un point ouvert (**R1**) |
| **Phase 3 et +** | Choix techniques, sécurité, construction | ⬜ **non commencées** — soumises à validation |

**Nous sommes en Phase 1.** Elle a été suspendue le 2026-10-19 puis **reprisée intégralement**
sur votre décision (voie *b*, ni suspension, ni réduction, ni clôture en l'état).

**À la Phase 1 se greffe un second chantier, la restauration**, que vous avez décidé
d'**entrelacer** : je restaure d'abord, je rédige la fiche ensuite, sur un document sain.
Une seule lecture par document au lieu de deux.

---

## 2. La Phase 1 — où elle en est exactement

### 2.1 Les 29 documents

Le corpus compte **28 documents réels** (20 mathématiques + 8 de littératie technique) et
**29 fiches attendues**, la 29ᵉ étant la *fiche d'absence* de la lettre **T**, qui n'existe pas
dans le corpus. Les deux dénombrements tombent à 29 sans compter la même chose — piège déjà
documenté dans `CLOTURE-CHANTIER.md` §7.1.

### 2.2 Fiches produites : 6 sur 29

| Domaine | Document | Fiche |
|---|---|---|
| **K** | Fractales, chaos & systèmes dynamiques | `domaine-K-fractales-chaos-systemes-dynamiques.md` |
| **L** | Analyse numérique | `domaine-L-analyse-numerique.md` |
| **I** | Calcul différentiel | `domaine-I-calcul-differentiel.md` |
| **N** | Transformées | `domaine-N-transformees.md` |
| **D** | Géométrie computationnelle | `domaine-D-geometrie-computationnelle.md` |
| **A** | Logique et fondements | `domaine-A-logique-et-fondements.md` |

**Reste 23 documents**, dont **P — Cryptographie**, que le plan A6 §4 n'assignait à aucun lot.
Corrigé le 2026-10-21 : **P est désormais au lot 3**, et les cinq lots couvrent
**20 documents réels sur 20**.

### 2.3 L'ordre de traitement

Le plan A6 §4 répartit les domaines en cinq lots. L'ordre de reprise que vous avez fixé est
**A → U** pour les mathématiques, puis les 8 documents de littératie.

| Lot | Domaines | État |
|---|---|---|
| 1 | K ✅ · D ✅ · I ✅ · L ✅ · N ✅ | cinq fiches faites |
| 2 | C · G · J · M · O | rien de fait |
| 3 | E · F · H · **P** · Q · R · S · U | rien de fait |
| 4 | A ✅ · B · C · D | A faite ; **B en cours** ; C et D à venir |
| 5 | `Ai Technical Litteracy` 01–08 | rien de fait |

⚠️ **Une incohérence du lot 1, signalée et non tranchée.** Le plan annonce « K · D · I · L · N »,
mais la clôture nomme les cinq documents effectivement restaurés **K, L, I, N, J** : **D n'a rien
à restaurer** (0 bloc, aplatissement intégral) et relève du lot 4. **J** a bien été restauré
(232 restitutions) mais n'a **pas de fiche**. Cette incohérence est la vôtre à trancher, pas la
mienne à corriger silencieusement.

---

## 3. Le chantier de restauration — où il en est

### 3.1 Ce qui est clos

| Périmètre | Documents | Travail | État |
|---|---|---|---|
| **Régimes 1 et 2** | K, L, I, N, J | **1 137 blocs**, **773 restaurations** | ✅ **clos** (`CLOTURE-CHANTIER.md`) |
| **Régime 3 (aplatissement)** | **A** | **70 substitutions** en 6 lots | ✅ **clos** (`CLOTURE-DOMAINE-A.md`) |

**Total : 843 propositions appliquées**, livrées en **23 diffs** que vous appliquez vous-même.

⚠️ **Deux réserves, qui sont des constats et non des objections :**
- **Aucune de ces 843 restitutions n'a été validée bloc par bloc** par vous. Elles portent
  chacune un niveau de confiance ; certaines sont *moyennes*.
- **C'est une reconstruction, pas une récupération.** Les arguments LaTeX détruits
  (régimes 1 et 2) n'existent nulle part. Ce qui est écrit est une proposition argumentée.

### 3.2 Ce qui est ouvert

| Document | État |
|---|---|
| **B** | **inventaire livré**, lot 1 proposé (6 substitutions, non appliqué) |
| **C, D** | régime 3, non commencés — la méthode est fixée (fiche A §11), éprouvée sur A et B |
| **E à U** (sauf I, J, K, L, N) | régimes 1 et 2, non commencés |

**Ampleur mesurée des défauts restants.** L'inventaire automatique
(`annexes/inventaire-defauts.csv`) relève **724 lignes porteuses de défauts** sur 13 documents.
**458** appartiennent aux cinq documents déjà restaurés (J 166, I 109, N 104, L 61, K 18).
Restent donc, sur ce seul inventaire :

| Document | Lignes à défaut |
|---|---:|
| H — Statistiques | 64 |
| G — Probabilités | 60 |
| M — Théorie de l'information | 59 |
| O — Complexité | 38 |
| F — Combinatoire | 12 |
| Q — Logique & automates | 11 |
| P — Cryptographie | 2 |
| Littératie 02 (UI/UX) | 20 |

⚠️ **Cet inventaire est partiel et heuristique** : il ne couvre que 13 documents et repose sur
des motifs, non sur une lecture. **Il ne prétend pas à l'exhaustivité** et ne dispense pas d'un
relevé document par document.

---

## 4. La Phase 2 — terminée, un point pendant

**Livrée :** 11 fiches de plateforme (`F01` à `F11`), un registre des licences, un registre des
plateformes, une synthèse des différenciateurs, une étude de demande (`A10`), et un rapport de
fin de phase au format des 16 points (`A9-rapport-fin-de-phase-2.md`).

Le rapport porte **six recommandations** (`A9-rapport-fin-de-phase-2.md` §10) et **six risques**
(§9). Les deux séries sont numérotées séparément, ce qui prête à confusion : **R1 n'est pas le
même selon la table**. Voici les recommandations, telles qu'elles figurent au §10 :

| # | Recommandation | État |
|---|---|---|
| **R7** | Vérifier Paper Shaders et OpenShaders | ✅ **faite le 2026-10-21** — fiche F11 §17 |
| **R1** | Lever les **quatre points ouverts du registre des licences** | ❌ **ouvert — la seule action restante de la phase 2** |
| **R3.3** | Compléter l'étude de demande | ⚠️ **première passe seulement** — `A10-etude-de-demande.md` |
| **R3.1** | Présenter la couche de preuve par ses bénéfices, jamais comme argument premier | ⬜ à l'ouverture de la construction |
| **R3.2** | Faire de l'aptitude à l'IA le cheval de Troie | ⬜ idem — dépend de D1, D3 |
| **R3.4** | Instrumenter dès le premier composant | ⬜ idem — dépend d'un premier composant |

Les six **risques** du §9, eux, restent ouverts par nature : R1 couche de preuve sans demande
mesurée (**élevée**), R4 quatre points juridiques (**élevée**), R5 corpus source sans licence
(**élevée**), R2 audiences disjointes (moyenne), R3 effet de mode (moyenne), R6 cases `?`
(faible).

### Ce que R7 a trouvé, en deux phrases

**Paper Shaders** est le meilleur acteur ouvert trouvé depuis shadcn/ui : Apache-2.0 sans piège,
3 793 ★, 30 effets, zéro dépendance **vérifiée sur npm**, `llms.txt` déployé, registre au schéma
shadcn — mais `0.0.x`, et **aucune explication mathématique**.

**OpenShaders n'existe pas encore** : 277 ★, un dépôt contenant `LICENSE` et `README.md` et
rien d'autre, arrêté depuis 42 jours, aucun paquet npm. Ses 277 étoiles récompensent une
promesse adossée à la notoriété de React Bits. Et son régime est défavorable :
« *the platform being open is a promise about the platform, not a claim on what you make with
it* » — **la même structure de risque que Shadertoy**.

**Conclusion utile :** le meilleur acteur du secteur s'arrête exactement là où Mathemirum
commence.

---

## 5. Comment nous allons poursuivre

### 5.1 La boucle, inchangée

Pour chaque document, **deux passages entrelacés** :

```
1. reconstituer l'atelier   ← bash tools/restauration/reconstituer_atelier.sh
2. profiler                 ← profil_degradation.py  (mesure, jamais impression)
3. inventorier              ← plan reconstruit + piles + slots
4. proposer un lot          ← soumis, jamais appliqué sans votre accord
5. appliquer                ← sur validation, par générateur, avec journal
6. livrer                   ← .gitdiff + .message-commit.txt + .journal.json
7. rédiger la fiche         ← sur un document sain
```

### 5.2 L'ordre des prochains documents

| Rang | Document | Pourquoi |
|---:|---|---|
| **1** | **B** — lot 1 appliqué, puis les lots suivants | en cours ; la méthode est rodée |
| **2** | **fiche B** | entrelacement |
| 3 | **C** — algèbre linéaire | régime 3, **80 lettres grecques** (la plus touchée) |
| 4 | **D** — géométrie computationnelle | régime 3, fiche déjà faite, 0 bloc à restaurer |
| 5 | puis E → U dans l'ordre du plan A6 | régimes 1 et 2 |
| 6 | les 8 documents de littératie | lot 5 |

**B, puis C, puis D** : c'est l'ordre alphabétique de votre directive « A → U ». Aucune
priorisation tactique n'est à plaider par-dessus.

À titre d'information, les trois documents du régime 3 se comparent ainsi — mesures prises le
2026-10-21 par `profil_degradation.py` et un comptage Unicode, non par échantillonnage :

| Document | Caractères | Lignes | Titre/blocs/`**`/puces | Grecques | Lignes à runs |
|---|---:|---:|---|---:|---:|
| **B** — Théorie des nombres | 65 371 | 103 | **0 · 0 · 0 · 0** | 19 (toutes `φ`) | 52 |
| **C** — Algèbre linéaire | 73 453 | 123 | **0 · 0 · 0 · 0** | **80** (`α` 30, `λ` 29, `θ` 10) | 62 |
| **D** — Géométrie computationnelle | 55 452 | 133 | **0 · 0 · 0 · 0** | 27 | 67 |

C porte **trois fois plus de lettres grecques** que D : c'est celui dont la restitution
devrait mobiliser le plus de propositions. D est le plus court et le plus pauvre en grecques.

### 5.3 Les critères de sortie, par document

Un document est **traité** lorsque :

1. son plan a été reconstruit par détection, jamais par échantillonnage ;
2. chaque fragment dégradé a une proposition *ou* une décision argumentée de ne rien faire ;
3. le correctif a été vérifié à sec puis appliqué ;
4. le diff et le rapport d'application sont livrés ;
5. **les blocs non restituables sont inscrits au registre, pas laissés dans l'oubli** ;
6. la fiche est rédigée sur le document sain.

---

## 6. Ce qui attend votre décision

| # | Point | Pourquoi c'est à vous |
|---:|---|---|
| **1** | **Appliquer le lot B-1** (6 substitutions, haute confiance) | règle du chantier : rien n'est écrit sans validation |
| **2** | **Rouvrir A pour un lot 7 ?** | j'ai trouvé une correspondance **exacte** entre les fragments conservés du §3.2 (3 × `P → Q`, 2 × `P`, 2 × `Q`) et les sept emplacements vides du §3.1. Non appliqué : la clôture était décidée avant que je ne le voie |
| **3** | **Lever R1** — les quatre points du registre des licences | seule action restante de la phase 2 ; demande un écrit des éditeurs |
| **4** | **L'incohérence D/J du lot 1** | J a 232 restitutions et aucune fiche ; D a une fiche et rien à restaurer |
| **5** | **La licence du corpus source** | `Stane316/my-own-connaissance` est public **sans fichier LICENSE** ; publier un composant qui en dérive reproduirait le défaut critique relevé chez GeoGebra |

---

## 7. Ce que je ne peux pas faire seul

- **Aucune vérification juridique.** Le registre des licences n'est pas un avis de juriste.
- **Aucun test d'exécution.** Pas de GPU, pas de navigateur : la qualité visuelle des
  composants étudiés n'a jamais été évaluée, seules leurs caractéristiques déclarées l'ont été.
- **Aucune preuve d'absence.** Le cahier des charges interdit de revendiquer l'exhaustivité :
  une recherche sans résultat n'est pas une démonstration.
- **Aucune modification du dépôt de connaissances.** Toutes les écritures vous sont livrées en
  diffs ; vous les appliquez.

---

## 8. L'environnement — un fait à connaître

Le sandbox est réinitialisé régulièrement : **cinq fois** depuis le début du chantier.
Le `.git` local et `/home/user/_audit/` (clone, sauvegardes) peuvent disparaître à chaque tour.

**Rien n'est perdu** : la branche est poussée et le corpus se reclône. La procédure est
désormais scriptée et éprouvée :

```
bash tools/restauration/reconstituer_atelier.sh
```

→ branche restaurée, corpus recloné à `f0f5e2d`, **17/17 diffs** réappliqués dans l'ordre non
interchangeable, **6/6 lots de A** en séquentiel, mojibake vérifié, **A = 78 756**, écart nul.

**Conséquence pratique :** tout livrable doit être commité dans le dépôt. Ce qui reste dans
`/home/user/_audit/` est, par nature, provisoire.
