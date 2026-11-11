# 00 — Vue d'ensemble du projet

**Statut :** ✅ confirmé sauf mention contraire · **Date :** 2026-11-11 · **Commit :** `6f87baf`

---

## 1. Ce qu'est le projet, en une phrase

**Mathemirum** est un projet d'**écosystème open source de composants web et visuels fondés sur les
mathématiques**, dont l'ambition est que chaque composant expose — en plus de son effet — ses
**équations, ses hypothèses, son domaine de validité, ses limites et ses performances mesurées**.

✅ Source de la formule de nature : en-tête de `docs/audit/PHASE-0-rapport-audit-initial.md` —
« *écosystème open source de création web et visuelle fondé sur les mathématiques* ».

---

## 2. Ce que le projet n'est pas

Trois confusions sont à écarter d'emblée, parce qu'elles sont faciles et coûteuses.

| Le projet n'est **pas** | Parce que |
|---|---|
| une application existante | ✅ **aucun code d'application** : ni `package.json`, ni `src/`, ni composant, ni build |
| une bibliothèque publiée | ✅ aucun paquet npm ou PyPI n'a été publié ; les noms ont seulement été **sondés** comme libres |
| un simple dépôt de documentation | ✅ il vise un produit ; la documentation est l'étape actuelle, pas la finalité |

---

## 3. Le nom

| Élément | Valeur |
|---|---|
| Nom de travail | **`mathemirum`** |
| Étymologie | latin *mathematica* + *mirum* — « la merveille des mathématiques » |
| Statut | ✅ **décision approuvée** (2026-10-18), réversible, non déposé |
| Variable technique | `PROJECT_CODENAME = "mathemirum"` |
| Règle | injecté par variable, **jamais écrit en dur** dans le code ni les gabarits |

✅ Source : `docs/decisions/0001-nom-de-travail-mathemirum.md`.

### Les noms écartés, et pourquoi

| Candidat | Raison de l'écart |
|---|---|
| **`mathverse`** | collision majeure : benchmark de mathématiques visuelles (ECCV 2024, MIT), jeu de données Hugging Face, paquet PyPI existant. ⚠️ **C'est néanmoins le nom du dépôt GitHub** — il n'a jamais été le nom du produit |
| **`mathauma`** | choix retenu le 2026-10-18, puis remplacé par `mathemirum` sur décision du porteur |
| **`mathéon`** | second nom figurant au cahier des charges ; non retenu |
| `mathemos` | nomme le domaine sans porter la promesse |
| `wundermath` | occupé par une académie de mathématiques coréenne |
| 58 autres | antériorités commerciales réelles |

Campagne de nommage : **242 sondes**, 175 candidats libres, 58 éliminés. Détail dans
`docs/audit/A1`, `A3`, `A4`, `A5`.

---

## 4. Les deux dépôts du projet

Le projet repose sur **deux dépôts GitHub distincts**, aux rôles strictement séparés.

| Dépôt | Rôle | Contenu | Licence |
|---|---|---|---|
| **`Stane316/my-own-connaissance`** | **corpus source** — la matière première | 29 documents Markdown, 80 330 lignes, 2 354 équations | ❌ **aucune** |
| **`Stane316/mathverse`** | **dépôt de travail** — le présent dépôt | documents d'audit, outils Python, livrables de restauration | ❌ **aucune** |

✅ Mesures : `docs/audit/PHASE-0-rapport-audit-initial.md` §5 et `A2-inventaire-structurel.md` §2.

⚠️ **Les deux dépôts sont publics sans licence.** C'est un défaut juridique, et c'est aussi
exactement le défaut que le projet critique chez ses concurrents — voir
`09-KNOWN-ISSUES-AND-RISKS.md` §1.

---

## 5. La matière première : ce que contient le corpus

Le corpus `my-own-connaissance` est une encyclopédie mathématique personnelle couvrant vingt
domaines (A à U, sans T) plus huit documents de littératie technique.

| Métrique | Total | Ce que cela signifie |
|---|---:|---|
| Lignes / octets | 80 330 / 1 912 005 | corpus volumineux |
| Titres Markdown | 7 240 | structure riche… sauf sur A, B, C, D |
| Équations display `\[…\]` | **2 354** | très dense en énoncés |
| Équations inline `\(…\)` | 5 | quasi inexistantes |
| **Blocs de code** | **0** | ⚠️ **le chaînon manquant** |
| Vocabulaire de rigueur | « hypothèse » 211, « limite » 222, « théorème » 207, « démonstration » 227, « implémentation » 223, « test » 447, « algorithme » 475 | le corpus **parle** de rigueur |

### Le constat structurant

✅ **Vérifié et reproductible** (`tools/audit-phase1/extract_structure.py`) : la chaîne

```
modèle → équation → algorithme → implémentation → tests
```

est documentée **jusqu'à l'algorithme, jamais au-delà**. Zéro bloc de code, zéro pseudocode
formaté, zéro jeu de données, zéro script dans 80 330 lignes.

**C'est la lacune du corpus, et c'est la différenciation possible du produit.** Le projet ne part
pas de rien : il part d'un fonds d'énoncés mathématiques auquel il manque l'exécutable.

---

## 6. Le contenu originel du dépôt de travail

Le dépôt `mathverse` contenait, au premier commit (`bdba473`), **deux documents et rien d'autre** :

| Fichier | Contenu |
|---|---|
| `Equations Mathématiques/equations_courbes_mathematiques.md` | 18 654 octets — panoplie de 29 familles de courbes « artistiques » (cœur, spirale logarithmique, papillon de Fay, rose de Rhodonea, lemniscate, cardioïde, astroïde, deltoïde, Lissajous, superformula…) avec équations polaires, paramétriques et implicites |
| `Equations Mathématiques/equations_courbes_animees_v2.md` | 21 505 octets — seconde édition : les trois niveaux d'animation (manuelle, automatique, temporelle), la méthode universelle en quatre étapes, des ateliers pratiques Desmos / GeoGebra / p5.js, une **bibliothèque de 30 équations animées**, et un comparatif de six logiciels gratuits |

✅ **Ces deux fichiers sont la graine du projet** : ils révèlent l'intention originelle — un
catalogue de courbes mathématiques esthétiques, paramétrables et animables, avec les moyens de les
voir bouger. Le projet actuel en est l'élargissement, de « courbes jolies » à « composants
explicables ».

⚠️ **Signal de qualité du premier commit** : 63 marqueurs `[web:n]` orphelins, sans bibliographie
correspondante (source : `PHASE-0-rapport-audit-initial.md` §5).

---

## 7. La vision, en clair

Le projet veut occuper une place que personne n'occupe. L'étude de 27 plateformes
(`05-EXTERNAL-REFERENCES.md`) a établi que :

- le secteur **livre des effets** et les documente très bien ;
- le secteur **ne documente jamais** les équations sous-jacentes, les hypothèses de validité, les
  limites, ni les performances mesurées.

La case « équations et hypothèses » est vide **sur les 27 plateformes sans une seule exception** —
y compris chez Math-To-Manim, qui produit pourtant un « dossier mathématique ».

⚠️ **Réserve capitale, établie par `A10-etude-de-demande.md` :** « personne ne l'occupe » et
« quelqu'un le demande » sont deux choses différentes. **Aucune demande observable** n'a été
trouvée pour les deux différenciateurs les plus identitaires du projet (D1 équations/hypothèses,
D2 classement tripartite). Voir `01-VISION-AND-PRODUCT.md` §5.

---

## 8. Où en est le projet

| Dimension | État |
|---|---|
| Identité et nom | ✅ arrêtés |
| Vision et différenciateurs | ✅ documentés, ⚠️ partiellement infirmés par l'étude de demande |
| Connaissance du corpus | 🟡 6 fiches sur 29 ; restauration engagée |
| Veille concurrentielle | ✅ 27 plateformes, 11 fiches |
| **Code d'application** | ⬜ **inexistant** |
| Architecture cible | 🔷 esquissée, non arrêtée |
| Licence | ❌ **non établie** — point bloquant |

**Phase en cours : Phase 1** — audit documentaire. Détail complet dans
`07-CURRENT-STATE-AND-AUDIT.md`.

---

## 9. Les cinq familles de composants visées

Le cahier des charges définit cinq familles prioritaires, qui ont déterminé l'ordre de traitement
du corpus (lot 1 du plan `A6`). ✅ Source : `A6-plan-phase-1.md` §4.

| Famille | Domaine du corpus | Fiche |
|---|---|---|
| Fractales, chaos | **K** | ✅ faite |
| Analyse numérique | **L** | ✅ faite |
| Calcul différentiel | **I** | ✅ faite |
| Transformées | **N** | ✅ faite |
| Optimisation | **J** | restauré (232 restitutions), **fiche non faite** |

⚠️ **Incohérence signalée** : le plan annonce « K · D · I · L · N » alors que le document effectivement
restauré à la place de D est **J**. Voir `09-KNOWN-ISSUES-AND-RISKS.md` §6.

---

## 10. Comment lire la suite

| Question | Document |
|---|---|
| Pourquoi ce projet ? | `01-VISION-AND-PRODUCT.md` |
| Que doit-il faire ? | `02-FUNCTIONAL-SPECIFICATION.md` |
| Comment est-il construit ? | `03-TECHNICAL-ARCHITECTURE.md` |
| Avec quelles technologies ? | `04-TECHNOLOGY-AND-DEPENDENCIES.md` |
| Qui fait quoi dans le paysage ? | `05-EXTERNAL-REFERENCES.md` |
| D'où vient-on ? | `06-HISTORY-AND-DECISIONS.md` |
| Où en est-on ? | `07-CURRENT-STATE-AND-AUDIT.md` |
| Où va-t-on ? | `08-ROADMAP-AND-NEXT-STEPS.md` |
| Qu'est-ce qui menace ? | `09-KNOWN-ISSUES-AND-RISKS.md` |
| Comment vérifier ? | `10-SOURCES-AND-EVIDENCE.md` |
