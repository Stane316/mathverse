# 07 — État actuel et diagnostic

**Date :** 2026-11-11 · **Commit :** `6f87baf`
**Mesures reprises de :** `docs/audit/BILAN-ET-MARCHE-A-SUIVRE.md`, `CLOTURE-CHANTIER.md`,
`CLOTURE-DOMAINE-A.md`, `inventorier_fragments.py`, `profil_degradation.py`

---

## 1. Réponse courte

| Phase | Objet | Statut |
|---|---|---|
| **Phase 0** | Vérification des accès et du périmètre | ✅ **terminée** |
| **Phase 1** | Audit documentaire des 29 documents | 🟡 **en cours — 6 fiches sur 29** |
| **Phase 2** | Veille concurrentielle et licences | ✅ **terminée** — une action pendante (**R1**) |
| **Phases 3 et +** | Choix techniques, sécurité, construction | ⬜ **non commencées** — soumises à validation |

**Le projet est en Phase 1.** Elle a été suspendue le 2026-10-19 puis **reprisée intégralement** sur
décision du porteur.

**Un second chantier s'y greffe, la restauration**, que le porteur a décidé d'**entrelacer** :
restaurer d'abord, rédiger la fiche ensuite, sur un document sain. Une seule lecture par document
au lieu de deux.

---

## 2. Tableau de bord fonctionnel

Légende : ✅ terminé et vérifié · 🟡 partiel · 🔷 spécifié non développé · ⬜ envisagé · ❌ bloqué

| Fonctionnalité | État | Preuve | Observation |
|---|---|---|---|
| Nom et identité | ✅ | décision 0001 | `mathemirum`, vérifié libre sur npm/PyPI/GitHub |
| Inventaire du corpus | ✅ | `A2` + CSV/JSON | 29 documents, 80 330 lignes, 2 354 équations |
| Diagnostic d'intégrité | ✅ | `A7` + CSV | 31,4 % des équations dégradées, 3 régimes |
| Plan de la Phase 1 | ✅ | `A6` | 5 lots, 20 documents réels couverts |
| **Fiches de domaine** | 🟡 **6 / 29** | `docs/audit/fiches/` | K, L, I, N, D, A |
| **Restauration régimes 1-2** | ✅ **clos** | `CLOTURE-CHANTIER.md` | 1 137 blocs, **773 restaurations** |
| **Restauration régime 3 — A** | ✅ **clos** | `CLOTURE-DOMAINE-A.md` | **70 substitutions** en 6 lots |
| **Restauration régime 3 — B** | 🟡 **lot 1 proposé** | `domaine-B-lot1.md` | 6 substitutions, **non appliqué** |
| Restauration régime 3 — C, D | ⬜ non commencé | — | méthode fixée et éprouvée |
| Restauration E→U | ⬜ non commencé | — | régimes 1 et 2 |
| Veille concurrentielle | ✅ | 11 fiches F01–F11 | 27 plateformes |
| Synthèse des différenciateurs | ✅ | `A9-synthese-differenciateurs.md` | 7 différenciateurs, ⚠️ 2 infirmés |
| Étude de demande | 🟡 **première passe** | `A10` | ⚠️ résultat défavorable |
| Registre des licences | ✅ | `A9-registre-des-licences.md` | 35 plateformes |
| Recommandation R7 | ✅ | `F11` §17 | Paper Shaders, OpenShaders vérifiés |
| **Licence du projet** | ❌ **bloqué** | décision 0002 | corpus source sans licence |
| Index notion → composant | ⬜ **non commencé** | `A6` §3.4 | prévu |
| **Code d'application** | ⬜ **inexistant** | mesure directe | 0 composant, 0 test |
| Architecture cible | 🔷 esquissée | — | non arrêtée |

---

## 3. La Phase 1 en détail

### 3.1 Les 29 documents

Le corpus compte **28 documents réels** (20 mathématiques + 8 de littératie technique) et **29
fiches attendues**, la 29ᵉ étant la **fiche d'absence de la lettre T**, qui n'existe pas dans le
corpus.

⚠️ **Piège documenté** (`CLOTURE-CHANTIER.md` §7.1) : les deux dénombrements tombent à 29 **sans
compter la même chose**. Ne pas raisonner sur « 29 documents » sans préciser de quoi l'on parle.

### 3.2 Les six fiches produites

| Domaine | Document | Restauré ? |
|---|---|---|
| **K** | Fractales, chaos & systèmes dynamiques | ✅ 40 restitutions |
| **L** | Analyse numérique | ✅ 121 |
| **I** | Calcul différentiel | ✅ 208 |
| **N** | Transformées | ✅ 172 |
| **D** | Géométrie computationnelle | ❌ régime 3, renvoyé au lot 4 |
| **A** | Logique et fondements | ✅ 70 substitutions (régime 3) |

**Reste 23 documents.**

### 3.3 Les cinq lots

| Lot | Domaines | État |
|---|---|---|
| 1 | K ✅ · D ✅ · I ✅ · L ✅ · N ✅ | cinq fiches |
| 2 | C · G · J · M · O | rien de fait |
| 3 | E · F · H · **P** · Q · R · S · U | rien de fait |
| 4 | A ✅ · B · C · D | A faite ; **B en cours** |
| 5 | `Ai Technical Litteracy` 01–08 | rien de fait |

### 3.4 Le modèle de fiche

✅ Les fiches suivent un modèle constant de **10 sections**, étendu à 12 pour le domaine A :

```
1. Identification et volume          7. Relations mathématiques ↔ usages
2. Objectif déclaré et couverture    8. Index — premières notions
3. Ce qui est aligné avec le projet  9. Fiabilité, cohérence, traçabilité
4. Formalisme : état détaillé       10. Niveau de maturité
5. Typologie de la dégradation      [11. Méthode retenue pour B, C et D]
6. Lacunes relevées                 [12. Besoins de documentation complémentaire]
```

⚠️ **Le §11 de la fiche A est la méthode de référence** pour traiter B, C et D. Tout agent qui
reprend la restauration doit le lire.

---

## 4. Le chantier de restauration

### 4.1 Ce qui est clos

| Périmètre | Documents | Travail | État |
|---|---|---|---|
| Régimes 1 et 2 | K, L, I, N, J | **1 137 blocs, 773 restaurations** | ✅ clos |
| Régime 3 | **A** | **70 substitutions** en 6 lots | ✅ clos |

**Total : 843 propositions appliquées**, livrées en **23 diffs** que le porteur applique lui-même.

### 4.2 ⚠️ Deux réserves, qui sont des constats et non des objections

1. ⚠️ **Aucune de ces 843 restitutions n'a été validée bloc par bloc** par le porteur. Elles portent
   chacune un niveau de confiance ; certaines sont *moyennes*.
2. ⚠️ **C'est une reconstruction, pas une récupération.** Les arguments LaTeX détruits n'existent
   nulle part. Ce qui est écrit est une **proposition argumentée**, jamais le texte d'origine.

### 4.3 Ce qui est ouvert

| Document | État |
|---|---|
| **B** | inventaire livré ; **lot 1 proposé** (6 substitutions, haute confiance, non appliqué) |
| **C, D** | régime 3, non commencés |
| **E à U** (sauf I, J, K, L, N) | régimes 1 et 2, non commencés |

### 4.4 Ampleur mesurée des défauts restants

✅ Source : `docs/restauration/annexes/inventaire-defauts.csv` — **724 lignes porteuses de défauts**
sur 13 documents. **458** appartiennent aux cinq documents déjà restaurés (J 166, I 109, N 104,
L 61, K 18). Restent :

| Document | Lignes à défaut |
|---|---:|
| H — Statistiques | 64 |
| G — Probabilités | 60 |
| M — Théorie de l'information | 59 |
| O — Théorie de la complexité | 38 |
| F — Combinatoire | 12 |
| Q — Logique, automates & langages | 11 |
| P — Cryptographie | 2 |
| Littératie 02 (UI/UX) | 20 |

⚠️ **Cet inventaire est partiel et heuristique** : il ne couvre que 13 documents et repose sur des
motifs, non sur une lecture. Il **ne prétend pas à l'exhaustivité** et ne dispense pas d'un relevé
document par document.

### 4.5 Le lot B-1, en attente

| Proposition | Section | Contenu |
|---|---|---|
| B1-01 | §3 | le tableau des propriétés, remis en Markdown |
| B1-02 | §4.1 | les quatre propriétés de divisibilité, numérotées |
| B1-03 | §4.2 | retrait du tas — **les jetons sont conservés en note** |
| B1-04 | §4.3 | `gcd(18,30) = 6` |
| B1-05 | §4.4 | `gcd(a,b) × ppcm(a,b) = ∣ab∣` pour `a, b ≠ 0` |
| B1-06 | §5.1 | `gcd(a,b) = gcd(b, a mod b)` pour `b ≠ 0` |

✅ Vérifié à sec : **65 371 → 65 586 (+215)**, 6/6 sous-chaînes uniques, **0 mojibake**, 0 glyphe
`U+E020` restant, 0 triple saut de ligne.

⚠️ **Rien n'est appliqué. Le document B est intact à 65 371 caractères**, vérifié après commit.

**Découverte structurante sur B :** les tas de B **cascadent vers l'avant** — l'inverse de A. Chaque
tas au §N reçoit les formules des sections **précédentes**. Une formule manquante se cherche donc
dans le tas de la section **suivante**.

⚠️ **Les exposants de B sont des recompositions, pas des récupérations** : le document B ne
contient **0 exposant**. `gˣ ≡ h (mod p)`, `n = ∏ pᵢ^{eᵢ}` et `a^k` ont dû être retapés.

---

## 5. Maturité par domaine

⚠️ **Aucun pourcentage global arbitraire.** Chaque domaine est évalué sur des éléments observables.

| Domaine | Évaluation | Justification |
|---|---|---|
| **Vision et spécifications** | 🟡 **Moyenne** | les 18 attributs par composant sont connus et contraignants ; mais ⚠️ **aucun document de vision ni de spécification produit n'existe**. La vision se déduit, elle n'est pas écrite |
| **Architecture** | 🔴 **Très faible** | aucune architecture applicative ; l'outillage est cohérent mais **sans test** et avec des chemins absolus codés en dur |
| **Implémentation** | 🔴 **Nulle** | ✅ **0 composant, 0 ligne de code d'application** |
| **Fonctionnalités** | 🔴 **Nulles** | aucune fonctionnalité n'est opérationnelle, aucune n'est partiellement développée |
| **Tests** | 🔴 **Nuls** | aucun test applicatif ; ⚠️ et aucun test automatisé des 30 scripts d'outillage |
| **Performance** | ⚪ **Non évaluable** | ❌ ni GPU ni navigateur ; aucun composant à mesurer |
| **Documentation** | 🟢 **Bonne, et c'est le point fort** | 190 fichiers, 2,2 Mio de `docs/` ; le niveau d'exigence documentaire est exceptionnel — c'est cohérent avec le différenciateur D3 |
| **Déploiement** | 🔴 **Nul** | aucun site, aucun paquet publié, aucune CI |
| **Expérience utilisateur** | ⚪ **Non évaluable** | aucune maquette, aucun wireframe, aucun composant |
| **Connaissance du corpus** | 🟡 **26 %** | 6 fiches sur 29 ; la restauration couvre 5 documents + A |
| **Connaissance du marché** | 🟢 **Bonne** | 27 plateformes, 11 fiches, registre des licences, étude de demande |
| **Sécurité juridique** | 🔴 **Nulle** | ❌ deux dépôts publics **sans licence** |

### Synthèse

🔶 **Déduction :** le projet est **très avancé en connaissance et nul en implémentation**. Ce
déséquilibre est normal à ce stade — c'est une phase d'audit — mais il doit être énoncé sans
ambigüité : **rien du produit n'existe**.

---

## 6. Ce qui fonctionne réellement

| Élément | État | Preuve |
|---|---|---|
| ✅ La chaîne d'audit documentaire | opérationnelle | 6 fiches produites, modèle constant |
| ✅ La chaîne de restauration | opérationnelle | 843 propositions, 23 diffs, 3 règles du moteur respectées |
| ✅ La mesure du corpus | reproductible | `extract_structure.py`, `profil_degradation.py` — déterministes, sans réseau |
| ✅ La procédure de reprise après réinitialisation | **éprouvée 7 fois** | `reconstituer_atelier.sh` → 17/17, 6/6, A = 78 756 |
| ✅ La veille concurrentielle | complète | 27 plateformes, 18 attributs |
| ✅ La traçabilité | systématique | journaux JSON, rapports d'application, diff par lot |
| ❌ Tout le reste | inexistant | aucun composant |

---

## 7. Ce qui reste incomplet

| Élément | État | Ce qu'il reste |
|---|---|---|
| Fiches de domaine | 6 / 29 | **23 documents** |
| Restauration B | lot 1 proposé | les lots suivants, après validation |
| Restauration C, D | non commencée | inventaire, puis lots |
| Restauration E→U | non commencée | régimes 1 et 2 |
| Littératie technique | non commencée | 8 documents, ⚠️ **32 équations seulement** — instruction légère |
| Index notion → composant | non commencé | prévu par `A6` §3.4 |
| Registre des licences | ⚠️ 4 points ouverts | réponse écrite des éditeurs |
| Licence du corpus | ❌ en attente | décision du porteur |
| Lot 7 du domaine A | ⏸️ en suspens | décision du porteur |

---

## 8. Les cinq points qui attendent le porteur

| # | Point | Pourquoi c'est à lui |
|---:|---|---|
| **1** | **Appliquer le lot B-1** (6 substitutions, haute confiance) | règle du chantier : rien n'est écrit sans validation |
| **2** | **Rouvrir A pour un lot 7 ?** | correspondance **exacte** trouvée entre les fragments du §3.2 (3 × `P → Q`, 2 × `P`, 2 × `Q`) et les sept emplacements vides du §3.1. Non appliqué : la clôture était décidée avant la découverte |
| **3** | **Lever R1** — les quatre points du registre des licences | seule action restante de la Phase 2 |
| **4** | **L'incohérence D/J du lot 1** | J a 232 restitutions et **aucune fiche** ; D a une fiche et **0 bloc à restaurer** |
| **5** | **La licence du corpus source** | `my-own-connaissance` est public **sans fichier LICENSE** ; publier un composant qui en dérive reproduirait le défaut critique relevé chez GeoGebra |
