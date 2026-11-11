# 02 — Spécification fonctionnelle

**Date :** 2026-11-11 · **Commit :** `6f87baf`
**Avertissement de lecture :** ce document décrit ce que le produit **doit** permettre.
✅ **Aucune de ces fonctionnalités n'est implémentée.** Le projet n'a aucun code d'application.

---

## 1. Ce qui est spécifié

La spécification fonctionnelle du projet ne provient pas d'un document de spécification — il n'en
existe aucun dans le dépôt — mais de la **grille de lecture à 18 attributs** que le cahier des
charges impose à chaque composant livré.

✅ Source : `docs/audit/annexes/A9-comparaison-transversale.md` §1.1.
⚠️ Le cahier des charges lui-même **n'a pas été retrouvé** dans le dépôt. Les 18 attributs sont
connus par cette grille, qui les cite textuellement comme « exigés pour chaque composant livré ».
Leur existence est ✅ confirmée ; la formulation exacte du cahier des charges est 🔶 déduite.

### 1.1 Les 18 attributs par composant

| # | Attribut | Ce qu'il doit contenir |
|---:|---|---|
| 1 | Nom | identifiant du composant |
| 2 | Description | ce qu'il fait |
| 3 | Catégorie | son classement |
| 4 | Aperçu en direct | démonstration exécutable |
| 5 | Paramètres réglables | les constantes exposées |
| 6 | Code source | le code du composant |
| 7 | Commande CLI | installation en une commande |
| 8 | Prompt IA réutilisable | **13 champs** permettant de le régénérer |
| 9 | **Explication mathématique** | 〔couche probatoire〕 pourquoi ça marche |
| 10 | **Équations et hypothèses** | 〔couche probatoire〕 sous quelles conditions |
| 11 | Dépendances | ce qu'il embarque |
| 12 | Installation | comment l'ajouter |
| 13 | Configuration exportable | réglages exportables |
| 14 | **Tests** | preuve de fonctionnement |
| 15 | **Mesures de performance** | chiffres, méthode et matériel déclarés |
| 16 | Licence et attribution | régime juridique |
| 17 | **Limites connues** | 〔couche probatoire〕 jusqu'où ça cesse d'être valide |
| 18 | Exemples d'intégration | cas d'usage |

Les attributs 9, 10 et 17 forment la **couche probatoire** — le cœur de la différenciation
(voir `01-VISION-AND-PRODUCT.md` §2).

---

## 2. Le classement tripartite

Le cahier des charges impose une distinction que le secteur ne fait pas :

| Classe | Définition | Ce qui est exigé pour y prétendre |
|---|---|---|
| **Effet artistique** | ressemble à un phénomène, ne le simule pas | rien de plus que la documentation usuelle |
| **Visualisation explicable** | calcule réellement ce qu'il montre | équations, paramètres, algorithme |
| **Simulation validée** | résout un modèle physique ou mathématique | **méthode, hypothèses, validation** |

✅ Source : `A9-synthese-differenciateurs.md` §2 (D2). La règle non-négociable citée est :
*jamais présenter un effet inspiré d'un fluide comme une simulation de Navier–Stokes sans méthode,
hypothèses et validation.*

⚠️ **Conséquence opérationnelle, soulignée par la source :** l'honnêteté du classement est le
différenciateur. Il « se perd dès le premier mensonge ».

---

## 3. Les cinq familles de composants prioritaires

✅ Source : `A6-plan-phase-1.md` §4. Ces cinq familles ont déterminé la composition du lot 1 de
l'audit documentaire.

| Famille | Domaine corpus | Fiche | Restauration | Composants identifiés dans la fiche |
|---|---|---|---|---|
| Fractales, chaos & systèmes dynamiques | **K** | ✅ | 40 restitutions | — |
| Analyse numérique | **L** | ✅ | 121 | — |
| Calcul différentiel | **I** | ✅ | 208 | **quatre cahiers des charges déjà rédigés** : visualisateur de dérivée (§154), visualisateur de gradient (§155), visualisation de Hessienne (§160), optimisation sous contrainte (§161) |
| Transformées | **N** | ✅ | 172 | pipeline **Microphone → Web Audio API → FFT → Canvas/WebGL** (§109), mapping de `\|X_k\|` vers 8 attributs visuels (§111), fenêtrage comme paramètre réglable (§95) |
| Optimisation | **J** | ❌ | 232 | la section 155 « Grande Carte des domaines » |

✅ Source des composants identifiés : `A8-synthese-et-point-de-reprise.md` §3.3.

🔶 **Déduction notable :** les fiches I et N ne se contentent pas d'inventorier. Elles contiennent
**des cahiers des charges de composants déjà rédigés**, et le domaine N décrit un pipeline web
complet et implémentable. Ce sont les deux documents du corpus jugés « les plus directement
exploitables ».

⚠️ **Lacune mesurée sur I et N** : les marqueurs `navier` et `CFL` y valent **0 occurrence**.
La cinquième famille — simulation d'équations aux dérivées partielles — **reste à sourcer hors
corpus**.

---

## 4. Le registre à champs étendus (D6)

🔷 **Envisagé**, fondé sur un standard de fait ✅ confirmé.

shadcn/ui a établi qu'un **article de registre** — un objet décrivant fichiers, chemins cibles et
dépendances — suffit à créer un écosystème interopérable. Ce format est devenu un standard : React
Bits l'émet via `jsrepo`, Shaders l'utilise pour sa CLI, Paper Shaders publie un `registry.json` au
schéma shadcn.

**Ce que Mathemirum y ajouterait** : les champs équations, hypothèses, domaine de validité, prompt,
tests et limites.

⚠️ **Fragilité assumée par la source** : c'est une **extension, pas une rupture**. Tout acteur en
place peut ajouter ces champs. C'est le **plus fragile** des sept différenciateurs.

---

## 5. La boucle prompt → composant → test (D7)

🔷 **Envisagé**, appuyé sur une case vide ✅ confirmée.

| Acteur | Prompt | CLI | Test |
|---|---|---|---|
| Shaders | ✅ | ✅ | ❌ aucun test visible |
| Math-To-Manim | ✅ | ✅ | ✅ étape de vérification distincte — mais produit une **vidéo**, qu'on ne peut pas tester |
| **Mathemirum (cible)** | ✅ | ✅ | ✅ **sur un composant web, donc testable** |

⚠️ Risque : c'est le différenciateur le plus dépendant de l'état de l'art. Un acteur mieux doté
peut fermer la boucle avant le projet.

---

## 6. Tableau de bord fonctionnel

Légende : ✅ terminé et vérifié · 🟡 partiel · 🔷 spécifié, non développé · ⬜ envisagé · ❌ abandonné

| Fonctionnalité | Description | État | Preuve | Observation |
|---|---|---|---|---|
| Catalogue de composants | ensemble de composants visuels publiés | 🔷 spécifié | cahier des charges (18 attributs) | ⬜ **aucun composant n'existe** |
| Registre à champs étendus | format de registre enrichi | 🔷 spécifié | D6, `A9-synthese-differenciateurs.md` | dépend d'un premier composant |
| CLI d'installation | installation en une commande | 🔷 spécifié | attribut 7 | le secteur en a tous une |
| Prompt IA réutilisable (13 champs) | régénération par IA | 🔷 spécifié | attribut 8 | — |
| Couche probatoire par composant | équations, hypothèses, validité | 🔷 spécifié | D1, attributs 9-10 | **le cœur**, et le plus coûteux |
| Classement tripartite | effet / visualisation / simulation | 🔷 spécifié | D2 | exige une discipline d'étiquetage |
| Publication des limites | section « limites » par composant | 🔷 spécifié | D3, attribut 17 | meilleur rapport coût/crédibilité |
| Mesures de performance | chiffres + méthode + matériel | 🔷 spécifié | D4, attribut 15 | ⚠️ impossible dans cet environnement |
| Boucle de test | prompt → composant → test | 🔷 spécifié | D7, attribut 14 | — |
| Licence claire | `LICENSE` + politique de contribution | 🔷 spécifié | D5, attribut 16 | ❌ **bloqué** — corpus source sans licence |
| Site de découverte | vitrine et navigation | ⬜ envisagé | mentionné dans le plan Phase 0 §13.2 | non instruit |
| Index notion → composant | table de correspondance | 🟡 **en cours partiel** | `A6` §3.4 | prévu, **non commencé** |
| Audit documentaire | fiches par domaine | 🟡 **en cours** | 6 fiches / 29 | Phase 1 |
| Restauration du corpus | reconstruction des équations détruites | 🟡 **en cours** | 843 propositions, 23 diffs | hors produit, prérequis |

---

## 7. Ce qui n'est **pas** spécifié

Lacunes de spécification constatées lors de l'audit :

| Manque | Conséquence |
|---|---|
| ❓ Aucun document de vision | la vision est reconstruite par déduction à chaque reprise |
| ❓ Aucun document de spécification produit | les 18 attributs viennent du cahier des charges, pas d'un cahier produit |
| ❓ Aucune maquette, aucun wireframe | l'expérience utilisateur n'est décrite nulle part |
| ❓ Aucun choix de framework | React est dominant (83 %, State of JS 2025) mais **aucune décision n'est prise** |
| ❓ Aucun critère de sélection des premiers composants | les cinq familles sont définies, pas les composants |
| ❓ Aucune stratégie de test arrêtée | attribut 14 exigé, méthode non définie |
| ❓ Aucun protocole de benchmark | recommandé par la Phase 0 (C5), **non défini** |

⚠️ **Ces manques ne sont pas des oublis à corriger pendant cet audit.** Ils sont signalés pour être
traités au moment de l'ouverture de la construction — qui, rappelons-le, est soumise à validation.
