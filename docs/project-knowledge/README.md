# Base de connaissance du projet — index général

**Date de l'audit :** 2026-11-11
**Dépôt audité :** `Stane316/mathverse`
**Branche auditée :** `arena/2e20eccb-mathverse`
**Commit audité :** `6f87baf` — *Bilan exhaustif + lot B-1 propose (non applique)*
**Arbre du commit :** 188 fichiers, 39 316 lignes ajoutées, 0 suppression
**Nature de l'audit :** lecture seule. Aucun fichier source n'a été modifié.

---

## 1. Rôle de cette documentation

Ce dossier reconstruit **tout ce que le projet sait de lui-même** : son identité, sa vision, les
analyses déjà menées, les décisions prises, l'état réel d'avancement et la direction à suivre.

Il a été écrit pour être **autonome** : un lecteur — humain ou agent — qui n'a jamais participé à ce
projet doit pouvoir le comprendre, reprendre le travail et **ne pas refaire les analyses déjà
faites**. Aucune phrase de ce dossier ne suppose la connaissance d'une conversation antérieure.

Il est aussi **opposable** : chaque affirmation porte une source, et les statuts
*confirmé / déduit / envisagé / non vérifié / inconnu* sont employés de façon stricte.

### Conventions de statut

| Statut | Signification |
|---|---|
| ✅ **Confirmé** | observé directement dans le dépôt, ou mesure reproductible |
| 🔶 **Déduit** | conclusion tirée de plusieurs éléments observés |
| 🔷 **Envisagé** | piste ouverte, non adoptée |
| ⚠️ **Non vérifié** | information ni confirmée ni réfutée |
| ❓ **Inconnu** | information indisponible |

---

## 2. Identité du projet en cinq lignes

| | |
|---|---|
| **Nom de travail** | **`mathemirum`** (latin *mathematica* + *mirum*, « la merveille des mathématiques ») |
| **Nature** | écosystème open source de **création web et visuelle fondée sur les mathématiques** |
| **Idée directrice** | chaque composant visuel porte ses **équations, ses hypothèses et son domaine de validité** — là où le secteur ne livre que l'effet |
| **Stade réel** | ✅ **aucun code d'application n'existe** ; le dépôt contient exclusivement des documents d'audit et des outils Python d'analyse |
| **Phase en cours** | **Phase 1** — audit documentaire, 6 fiches produites sur 29 |

⚠️ **Le point le plus important à ne pas se tromper :** `mathemirum` n'est pas encore un produit.
C'est un projet **en phase d'audit et de reconstruction de connaissance**. Le dépôt `mathverse` ne
contient ni `package.json`, ni répertoire `src/`, ni composant, ni test, ni configuration de build.
Toute description qui laisserait croire le contraire serait fausse.

---

## 3. Contenu du dossier

| Fichier | Contenu | À lire pour… |
|---|---|---|
| **[`00-PROJECT-OVERVIEW.md`](00-PROJECT-OVERVIEW.md)** | Vue d'ensemble en une passe | comprendre le projet en 15 minutes |
| **[`01-VISION-AND-PRODUCT.md`](01-VISION-AND-PRODUCT.md)** | Mission, problème, proposition de valeur, public, positionnement | savoir **pourquoi** le projet existe |
| **[`02-FUNCTIONAL-SPECIFICATION.md`](02-FUNCTIONAL-SPECIFICATION.md)** | Les 18 attributs par composant, les familles, ce qui est spécifié vs rien | savoir **ce que** le produit doit faire |
| **[`03-TECHNICAL-ARCHITECTURE.md`](03-TECHNICAL-ARCHITECTURE.md)** | Architecture réelle (outillage) et architecture cible | savoir **comment** c'est structuré |
| **[`04-TECHNOLOGY-AND-DEPENDENCIES.md`](04-TECHNOLOGY-AND-DEPENDENCIES.md)** | Technologies utilisées, étudiées, écartées | savoir **avec quoi** |
| **[`05-EXTERNAL-REFERENCES.md`](05-EXTERNAL-REFERENCES.md)** | Les 27 plateformes étudiées, les deux dépôts du projet | connaître **le paysage** |
| **[`06-HISTORY-AND-DECISIONS.md`](06-HISTORY-AND-DECISIONS.md)** | Chronologie 2026-10-17 → 2026-11-10, décisions, pistes abandonnées | savoir **d'où** l'on vient |
| **[`07-CURRENT-STATE-AND-AUDIT.md`](07-CURRENT-STATE-AND-AUDIT.md)** | État réel, tableau de bord, maturité par domaine | savoir **où** l'on est |
| **[`08-ROADMAP-AND-NEXT-STEPS.md`](08-ROADMAP-AND-NEXT-STEPS.md)** | Feuille de route, priorités, ce qu'il ne faut **pas** faire | savoir **où** l'on va |
| **[`09-KNOWN-ISSUES-AND-RISKS.md`](09-KNOWN-ISSUES-AND-RISKS.md)** | Problèmes, risques, blocages, incohérences | savoir **ce qui menace** |
| **[`10-SOURCES-AND-EVIDENCE.md`](10-SOURCES-AND-EVIDENCE.md)** | Traçabilité : chaque chiffre et sa source | **vérifier** n'importe quelle affirmation |

---

## 4. Ordre de lecture recommandé

### Pour un nouvel agent qui doit reprendre le travail

```
00-PROJECT-OVERVIEW.md      ← départ obligatoire, 15 minutes
        ↓
07-CURRENT-STATE-AND-AUDIT.md   ← où en est-on exactement, ce qui est fait
        ↓
08-ROADMAP-AND-NEXT-STEPS.md    ← quoi faire maintenant
        ↓
09-KNOWN-ISSUES-AND-RISKS.md    ← les pièges avant de toucher à quoi que ce soit
```

Puis, selon la tâche :

| Tâche | Lire ensuite |
|---|---|
| Reprendre la restauration d'un document | `06-HISTORY-AND-DECISIONS.md` §4 (les trois régimes) |
| Écrire une fiche de domaine | `02-FUNCTIONAL-SPECIFICATION.md` + le modèle de fiche en §7 de `07` |
| Travailler sur l'outillage | `03-TECHNICAL-ARCHITECTURE.md` |
| Décider d'une licence | `09-KNOWN-ISSUES-AND-RISKS.md` §1 (le point bloquant) |
| Reprendre la veille | `05-EXTERNAL-REFERENCES.md` |

### Pour un lecteur humain qui veut tout comprendre

Suivre l'ordre numérique `00` → `10`.

---

## 5. Les trois documents à connaître absolument

Indépendamment de ce dossier, trois fichiers du dépôt font autorité et **ne sont pas remplacés** par
la présente documentation :

| Fichier | Pourquoi |
|---|---|
| `docs/audit/BILAN-ET-MARCHE-A-SUIVRE.md` | le **bilan exhaustif** : phase en cours, ce qui est fait, ce qui reste, comment poursuivre |
| `docs/restauration/CLOTURE-CHANTIER.md` | la clôture du chantier de restauration des régimes 1 et 2 |
| `docs/restauration/propositions/domaine-B-lot1.md` | la proposition **en attente de validation** au moment de l'audit |

---

## 6. Limites connues de cet audit

1. ⚠️ **Aucune exécution.** Aucun composant n'a été construit, installé ou testé — il n'en existe
   aucun. Les affirmations techniques sur les plateformes tierces sont **reprises de leurs
   documentations officielles**, non vérifiées par l'exécution : l'environnement ne dispose ni de
   GPU ni de navigateur.
2. ⚠️ **Aucune vérification juridique.** Le registre des licences (`annexes/A9-registre-des-licences.md`)
   consigne ce que les éditeurs déclarent. Il ne constitue pas un avis juridique. Quatre points
   restent ouverts et nécessitent une réponse écrite des éditeurs.
3. ⚠️ **Aucune preuve d'absence.** Les 27 plateformes étudiées ne sont pas l'écosystème entier.
   Une case vide dans la matrice comparative est une observation sur 27 acteurs, pas une
   démonstration.
4. ⚠️ **Le cahier des charges originel n'est pas dans le dépôt.** Il est connu par les documents
   d'audit qui le citent (18 attributs par composant, non-négociables, cinq familles de
   composants). Il n'a pas été retrouvé sous forme de fichier autonome. Ses dispositions sont donc
   restituées par citation indirecte — statut 🔶 **déduit** pour la formulation exacte,
   ✅ **confirmé** pour l'existence des exigences.
5. ⚠️ **Le corpus source n'est pas dans ce dépôt.** `Stane316/my-own-connaissance` est un dépôt
   distinct, cloné en lecture seule. Ses mesures sont reprises des outils du dépôt `mathverse`.
6. ⚠️ **L'environnement se réinitialise.** Le sandbox a été réinitialisé au moins sept fois depuis
   l'ouverture du chantier. Tout ce qui n'est pas commité dans le dépôt est perdu.
   Voir `03-TECHNICAL-ARCHITECTURE.md` §5.

---

## 7. Résumé chiffré

| Grandeur | Valeur | Source |
|---|---:|---|
| Fichiers dans le dépôt | 190 | mesure directe |
| Documents du corpus source | 29 (28 réels + la fiche d'absence de T) | `A2-inventaire-structurel.md` |
| Lignes du corpus source | 80 330 | idem |
| Équations display du corpus | 2 354 | idem |
| **Blocs de code du corpus** | **0** | idem — le chaînon manquant |
| Fiches de domaine produites | **6 / 29** | `docs/audit/fiches/` |
| Propositions de restauration appliquées | **843** | 773 (régimes 1-2) + 70 (domaine A) |
| Diffs livrés | 23 | `docs/restauration/livrables/` |
| Plateformes tierces étudiées | 27 | `A9-comparaison-transversale.md` |
| Fiches de plateforme | 11 (F01–F11) | `docs/audit/fiches-phase-2/` |
| Scripts Python d'outillage | 30 | `tools/` |
| Lignes de code d'application | **0** | mesure directe |
