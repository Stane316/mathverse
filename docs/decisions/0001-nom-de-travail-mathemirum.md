# DÉCISION 0001 — Nom de travail du projet : `mathemirum`

**Date :** 2026-10-18
**Statut :** **DÉCISION APPROUVÉE** par le porteur du projet (réversible)
**Nature :** nom de travail, non définitif, non déposé
**Références :** `docs/audit/A1`, `A3`, `A4`, `A5` (campagne de nommage, 242 sondes)

---

## 1. Décision

Le nom de travail du projet est **`mathemirum`**.

- **Variable technique :** `PROJECT_CODENAME = "mathemirum"`
- **Écriture :** toujours en minuscules dans les identifiants techniques (`mathemirum`, `@mathemirum/core`, `create-mathemirum`) ; libre dans la prose.
- **Règle :** le nom est injecté par la variable de configuration, **jamais écrit en dur** dans le code ni dans les gabarits. Un changement de nom doit rester une opération locale.

## 2. Contexte et intention

Le cahier des charges demande un nom provisoire et non dispersé. Après exploration, la directive a évolué : le nom ne doit pas décrire un axe technique (géométrie, mouvement, lumière), mais **porter la promesse du projet** — montrer que les mathématiques sont belles, sublimes et spectaculaires.

`mathemirum` est un composé latin : *mathematica* + *mirum*, « la merveille des mathématiques ». Il dit le domaine **et** l'émotion, dans une langue qui est celle de la tradition scientifique européenne.

## 3. État de la vérification (2026-10-18)

| Sonde | Résultat |
|---|---|
| `registry.npmjs.org/mathemirum` | **libre** (404) |
| `registry.npmjs.org/mathemirum-core` | **libre** (404) |
| `registry.npmjs.org/create-mathemirum` | **libre** (404) |
| `pypi.org/pypi/mathemirum/json` | **libre** (404) |
| `github.com/Stane316/mathemirum` | **libre** (404) |
| Recherche de dépôts homonymes (`mathemirum`) | **0 résultat** |
| Recherche web exacte « mathemirum » | **0 occurrence** — la requête ne renvoie que des résultats sur « Mathnasium », par similarité |
| Registres de marques (INPI, EUIPO, USPTO) | **non vérifié** — hors périmètre technique de cet audit |

**Limite assumée :** cette vérification couvre npm, PyPI, GitHub et la recherche web grand public. Elle **ne constitue pas une recherche d'antériorité de marque** (INPI, EUIPO, USPTO). Aucune marque n'est déposée à ce jour sous ce nom par le projet.

## 4. Alternatives écartées

| Candidat | Raison |
|---|---|
| `mathauma` (choix précédent, 2026-10-18) | remplacé par `mathemirum` sur décision du porteur du projet |
| `mathemos` | le plus propre techniquement et sur le web, mais il nomme le domaine sans porter la promesse |
| `magnificentia`, `mirabilitas`, `sublimitas`, `thaumasios` | mots latins ou grecs justes, mais plus longs et moins mémorisables |
| `wundermath` | occupé par une académie de mathématiques coréenne (분더수학, wundermath.com) |
| `mathverse` | collision majeure : benchmark universitaire (ECCV 2024), dataset HuggingFace, paquet PyPI |
| `thauma`, `sublima`, `venustas`, `kallos`, `aetheria`, `lucentia`, `decus`, `iridesca`, `geodesica`, `parametra`, `fractalia`, `vertexia`, `mobia`, `fluxia`… | antériorités commerciales réelles (voir `A3`, `A4`) |

## 5. Conséquences

1. Toute la documentation produite à partir de cette date utilise `mathemirum` ou, tant que l'interface n'est pas figée, le jeton neutre « le projet ».
2. Les documents d'audit antérieurs restent valides : ils portent sur des candidats, pas sur le nom retenu.
3. Le nom du dépôt GitHub, du paquet npm et du produit peuvent diverger si nécessaire ; cette décision ne les fige pas.

## 6. Conditions de révision

Cette décision sera révisée si : une antériorité de marque est découverte, le positionnement du projet change substantiellement, ou le porteur du projet décide d'un autre nom avant toute communication publique ou publication de paquet.
