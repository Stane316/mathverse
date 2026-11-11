# 10 — Sources et traçabilité

**Date :** 2026-11-11 · **Dépôt :** `Stane316/mathverse`
**Branche :** `arena/2e20eccb-mathverse` · **Commit audité :** `6f87baf`
**Arbre :** 188 fichiers, 39 316 lignes ajoutées, 0 suppression

---

## 1. Comment vérifier ce dossier

Chaque affirmation importante de la documentation renvoie à une source. Trois natures de source :

| Nature | Comment la vérifier |
|---|---|
| **Mesure reproductible** | rejouer le script cité ; il est déterministe et sans réseau |
| **Document du dépôt** | ouvrir le chemin cité, au commit `6f87baf` |
| **Source externe** | la date et l'origine sont indiquées ; ⚠️ l'accès depuis cet environnement est restreint |

### Commandes de vérification de base

```bash
# État et identité du commit audité
git log --oneline -1
git rev-parse HEAD                    # → 6f87baf

# Le projet n'a aucun code d'application (aucun résultat attendu)
find . -name "package.json" -o -name "*.tsx" -o -name "*.jsx" -o -name "index.html"

# Reconstruire l'atelier après une réinitialisation
bash tools/restauration/reconstituer_atelier.sh
#   attendu : 17/17 diffs, 6/6 lots de A, mojibake 0, A = 78 756

# Profiler un document
python3 tools/audit-phase1/profil_degradation.py <chemin.md>

# Lignes et équations du corpus
wc -l  /home/user/_audit/connaissance/Maths-vers-Informatiques/*.md
```

---

## 2. Table des chiffres du dossier

Chaque chiffre, sa valeur, sa source et sa reproductibilité.

| Chiffre | Valeur | Source exacte | Reproductible |
|---|---:|---|---|
| Fichiers du dépôt | 190 | mesure directe | ✅ `find . -type f` |
| Documents du corpus | 29 (28 réels + absence de T) | `A2-inventaire-structurel.md` §2 | ✅ |
| Lignes du corpus | 80 330 | idem | ✅ `extract_structure.py` |
| Octets du corpus | 1 912 005 | idem | ✅ |
| Titres Markdown | 7 240 | idem | ✅ |
| Équations display | 2 354 | idem | ✅ |
| Équations inline | 5 | idem | ✅ |
| **Blocs de code** | **0** | idem §3 | ✅ |
| Marqueurs de rigueur | « algorithme » 475, « test » 447, « limite » 222, « hypothèse » 211 | idem §2 | ✅ |
| Taux de dégradation des équations | **31,4 %** de 2 306 blocs | `A7-integrite-des-equations.md`, rectifié | ✅ |
| Fiches de domaine | **6 / 29** | `docs/audit/fiches/` | ✅ |
| Blocs display (régimes 1-2) | **1 137** | `CLOTURE-CHANTIER.md` §3 | ✅ sous la règle `\[` en début de ligne |
| Restaurations (régimes 1-2) | **773** | `CLOTURE-CHANTIER.md` §2 | ✅ |
| Substitutions (domaine A) | **70** | `CLOTURE-DOMAINE-A.md` | ✅ |
| **Total des propositions appliquées** | **843** | 773 + 70 | ✅ |
| Diffs livrés | **23** | `docs/restauration/livrables/*.gitdiff` | ✅ |
| Résidus du domaine A | **30** | `CLOTURE-DOMAINE-A.md` §4 | ✅ |
| Lignes à défaut dans le corpus | **724** sur 13 documents | `annexes/inventaire-defauts.csv` | ✅ |
| Plateformes étudiées | **27** | `A9-comparaison-transversale.md` | ⚠️ reprises de documentations |
| Attributs de la grille | **18** | idem §1.1 | ✅ |
| Fiches de plateforme | 11 (F01–F11) | `docs/audit/fiches-phase-2/` | ✅ |
| Scripts Python | 30 | `tools/` | ✅ |
| Campagne de nommage | 242 sondes, 175 libres, 58 éliminés | `docs/audit/README.md` §3 | ✅ |
| Caractères du document A restauré | **78 756** | mesure directe | ✅ |
| Caractères du document B intact | **65 371** | mesure directe | ✅ |
| Grecques : B / C / D | 19 / **80** / 27 | comptage `unicodedata`, 2026-11-11 | ✅ |
| Lignes à runs : B / C / D | 52 / 62 / 67 | idem | ✅ |
| Réinitialisations du sandbox | **7** | observation | ⚠️ non reproductible |

---

## 3. Sources par document du dossier

### `00-PROJECT-OVERVIEW.md`

| Affirmation | Source |
|---|---|
| Formule de nature du projet | `PHASE-0-rapport-audit-initial.md`, en-tête |
| Nom et étymologie | `docs/decisions/0001-nom-de-travail-mathemirum.md` |
| Noms écartés | idem §4 |
| Deux dépôts, sans licence | `PHASE-0` §5 ; `docs/decisions/0002` §1 |
| Statistiques du corpus | `A2-inventaire-structurel.md` §2 |
| Chaîne rompue après l'algorithme | idem §3 |
| Contenu originel du dépôt | `Equations Mathématiques/*.md` |
| Cinq familles de composants | `A6-plan-phase-1.md` §4 |

### `01-VISION-AND-PRODUCT.md`

| Affirmation | Source |
|---|---|
| Les sept différenciateurs | `annexes/A9-synthese-differenciateurs.md` §2 |
| Conditions C1–C4 | idem §1 |
| Verdict de demande | idem §2.0 ; `A10-etude-de-demande.md` §1 |
| Documentation = 1ᵉʳ critère (93 %) | `A10` §5.1, étude Concordia |
| Douleur n°1 = débogage/profilage (53 %) | `A10` §3, enquête Khronos 2026 |
| Ce que le projet ne peut pas revendiquer | `A9-synthese-differenciateurs.md` §3 |
| Risque central, deux hypothèses | idem §4 |

### `02-FUNCTIONAL-SPECIFICATION.md`

| Affirmation | Source |
|---|---|
| Les 18 attributs | `A9-comparaison-transversale.md` §1.1 |
| Classement tripartite | `A9-synthese-differenciateurs.md` §2 (D2) |
| Composants identifiés dans I et N | `A8-synthese-et-point-de-reprise.md` §3.3 |
| `navier` = 0, `CFL` = 0 dans I et N | idem |
| Registre à champs étendus (D6) | `A9-synthese-differenciateurs.md` §2 (D6) ; `F02-shadcn-ui.md` |
| Boucle prompt → test (D7) | idem (D7) ; `F03`, `F11` |

### `03-TECHNICAL-ARCHITECTURE.md`

| Affirmation | Source |
|---|---|
| Absence de code d'application | mesure directe |
| Responsabilités des dossiers | lecture de l'arbre |
| Les quatre règles de l'outillage | docstrings des 30 scripts |
| Deux moteurs de génération | `apply_patch.py` et `lot_commun.py`, docstrings |
| Les trois règles du moteur | `lot_commun.py`, docstring |
| Script de reconstitution | `tools/restauration/reconstituer_atelier.sh` |

### `04-TECHNOLOGY-AND-DEPENDENCIES.md`

| Affirmation | Source |
|---|---|
| Aucune dépendance | mesure directe : aucun manifeste |
| Contraintes d'environnement | `PHASE-0` §3, §5 |
| Licences des plateformes | `annexes/A9-registre-des-licences.md` |
| Paper Shaders et OpenShaders | `fiches-phase-2/F11-shaders-et-openshaders.md` §17 |
| Signaux de marché (React 83 %, Khronos, Concordia) | `A10-etude-de-demande.md` |

### `05-EXTERNAL-REFERENCES.md`

| Affirmation | Source |
|---|---|
| Registre des plateformes | `annexes/A9-registre-plateformes.md` |
| Matrice 18 attributs × familles | `annexes/A9-comparaison-transversale.md` §3 |
| Trois mécanismes de licence trompeurs | `annexes/A9-registre-des-licences.md` |
| `MathVerse` homonyme | `fiches-phase-2/F10-sadeepas-mathverse.md` |
| Deux dépôts du porteur | `PHASE-0` §5 ; `docs/decisions/0002` |

### `06-HISTORY-AND-DECISIONS.md`

| Affirmation | Source |
|---|---|
| Chronologie | `git log --reverse --date=short` (57 commits) |
| Décisions 0001 et 0002 | `docs/decisions/` |
| Décisions de restauration | `restauration/README.md`, `CLOTURE-CHANTIER.md` |
| Trois régimes de dégradation | `restauration/README.md` §2 |
| Règles de méthode acquises | docstrings, messages de commit, `CLOTURE-CHANTIER.md` §7 |
| Corrections de chiffres | `CLOTURE-CHANTIER.md` §7 ; `A7` |

### `07-CURRENT-STATE-AND-AUDIT.md`

| Affirmation | Source |
|---|---|
| État des phases | `docs/audit/BILAN-ET-MARCHE-A-SUIVRE.md` |
| Tableau de bord | idem ; fiches ; livrables |
| Six fiches | `docs/audit/fiches/` |
| Restaurations | `CLOTURE-CHANTIER.md` §2 ; `CLOTURE-DOMAINE-A.md` |
| Défauts restants | `annexes/inventaire-defauts.csv` |
| Lot B-1 | `propositions/domaine-B-lot1.md` |

### `08-ROADMAP-AND-NEXT-STEPS.md`

| Affirmation | Source |
|---|---|
| Décisions déjà prises | `CLOTURE-CHANTIER.md` ; `CLOTURE-DOMAINE-A.md` ; décisions du porteur rapportées |
| Ordre des documents | directive « A → U » du porteur |
| Mesures B/C/D | `profil_degradation.py` + comptage `unicodedata`, 2026-11-11 |
| Recommandations R3.1–R3.4, R7, R1 | `A9-rapport-fin-de-phase-2.md` §10 |

### `09-KNOWN-ISSUES-AND-RISKS.md`

| Affirmation | Source |
|---|---|
| Licence du corpus | `docs/decisions/0002` |
| Quatre points ouverts | `annexes/A9-registre-des-licences.md` §7.4 |
| Risque stratégique | `A9-synthese-differenciateurs.md` §4 ; `A10` |
| Six risques | `A9-rapport-fin-de-phase-2.md` §9 |
| Incohérence D/J | `A6` §4 vs `CLOTURE-CHANTIER.md` §2 |
| Corrections de chiffres | `CLOTURE-CHANTIER.md` §7 |

---

## 4. ⚠️ Les pièges de traçabilité connus

Cinq pièges ont déjà causé des erreurs. **Les connaître avant de citer un chiffre.**

| # | Piège | Ce qu'il faut faire |
|---:|---|---|
| 1 | ⚠️ **Deux séries R** : `A9-rapport-fin-de-phase-2.md` numérote séparément les risques (§9) et les recommandations (§10). **R1 ne désigne pas la même ligne selon la table** | toujours préciser « §9 » ou « §10 » |
| 2 | ⚠️ **`grep -o` compte des octets** pour les caractères grecs : 2 992 au lieu de 80 pour le document C | utiliser `unicodedata.name(c)` en Python |
| 3 | ⚠️ **Ne pas compter les résidus par regex** : 3+ espaces → 425 faux positifs sur A ; double espace intra-phrase → 1 452 | seule la lecture tranche |
| 4 | ⚠️ **« 29 documents » et « 29 fiches »** ne comptent pas la même chose : 28 documents réels + la fiche d'absence de T | préciser de quoi l'on parle |
| 5 | ⚠️ **Les diffs de A sont incrémentaux** : `domaine-A-lot2..6.gitdiff` échouent légitimement `git apply --check` sur un clone vierge | appliquer 1→6 dans l'ordre |

---

## 5. Sources externes citées

⚠️ Aucune de ces sources n'a été vérifiée par l'exécution. Elles sont reprises de leurs
documentations officielles ou d'études publiées.

| Source | Nature | Date | Usage |
|---|---|---|---|
| Enquête Khronos, écosystème des shaders 2026 | **primaire**, 400+ répondants | publiée 2026-07-21 | douleur n°1 = débogage/profilage (53 %) ; GLSL 60 %, HLSL 41 % ; Linux 74 % ; adaptation multiplateforme 64 % |
| Étude Concordia sur la sélection de paquets npm | **primaire**, universitaire | consultée 2026-10-19 | documentation = 1ᵉʳ critère (93 %) |
| State of JS 2025 | enquête | 2025 | React 83 %, satisfaction 62 % |
| ~20 guides de choix de bibliothèques de composants | ⚠️ **secondaires, éditoriales** | 2026-01 à 2026-10 | aucun ne mentionne les équations comme critère |
| Discours communautaire sur l'apprentissage des shaders | forums, cours | 2010–2026 | le discours « comprendre plutôt que copier » existe — **hors sphère composants web** |
| Documentations officielles des 27 plateformes | ⚠️ **déclaratives** | 2026-10 à 2026-11 | attributs, licences, étoiles |

⚠️ **Limite de méthode énoncée par `A10` elle-même** : les guides de choix sont du contenu de
marketing éditorial. Ils décrivent ce que les rédacteurs estiment important, pas nécessairement ce
que les développeurs font.

---

## 6. Ce qui reste sans preuve

| Information | Statut |
|---|---|
| ❓ Registres de marques pour `mathemirum` | **non consultés** |
| ❓ Cahier des charges originel | **non retrouvé** dans le dépôt |
| ❓ Qualité visuelle réelle des plateformes | **jamais observée** |
| ❓ Performances réelles | **jamais mesurées** |
| ❓ Demande pour D1 et D2 | recherche ciblée **négative** — ⚠️ **pas une preuve d'absence** |
| ❓ Contenu des 23 documents non audités | **non lu** |
| ❓ Recouvrement des deux audiences | **non tranché** |
| ❓ Réponses des quatre éditeurs | **en attente** |

---

## 7. Où trouver quoi — index des chemins

| Besoin | Chemin |
|---|---|
| Le bilan exhaustif | `docs/audit/BILAN-ET-MARCHE-A-SUIVRE.md` |
| Rapport de Phase 0 | `docs/audit/PHASE-0-rapport-audit-initial.md` |
| Inventaire du corpus | `docs/audit/A2-inventaire-structurel.md` + `annexes/*.csv` |
| Intégrité des équations | `docs/audit/A7-integrite-des-equations.md` |
| Plan de la Phase 1 | `docs/audit/A6-plan-phase-1.md` |
| Synthèse et point de reprise | `docs/audit/A8-synthese-et-point-de-reprise.md` |
| Étude de demande | `docs/audit/A10-etude-de-demande.md` |
| Rapport de fin de Phase 2 | `docs/audit/A9-rapport-fin-de-phase-2.md` |
| Différenciateurs | `docs/audit/annexes/A9-synthese-differenciateurs.md` |
| Registre des licences | `docs/audit/annexes/A9-registre-des-licences.md` |
| Registre des plateformes | `docs/audit/annexes/A9-registre-plateformes.md` |
| Fiches de domaine | `docs/audit/fiches/` |
| Fiches de plateforme | `docs/audit/fiches-phase-2/` |
| Décisions | `docs/decisions/` |
| Cadre de la restauration | `docs/restauration/README.md` |
| Clôture des régimes 1-2 | `docs/restauration/CLOTURE-CHANTIER.md` |
| Clôture du domaine A | `docs/restauration/CLOTURE-DOMAINE-A.md` |
| Proposition en attente | `docs/restauration/propositions/domaine-B-lot1.md` |
| Diffs livrés | `docs/restauration/livrables/` |
| Outils | `tools/audit-phase1/`, `tools/restauration/` |
