# 03 — Architecture technique

**Date :** 2026-11-11 · **Commit :** `6f87baf`

---

## 1. Avertissement liminaire

✅ **Confirmé par mesure directe : il n'existe aucune architecture applicative.**

```
$ find . -name "package.json" -o -name "*.tsx" -o -name "*.jsx" -o -name "index.html"
(aucun résultat)
```

Le dépôt ne contient **ni application, ni composant, ni framework, ni build, ni test applicatif**.
Toute description d'une architecture de composants, d'un système de rendu ou d'un pipeline de
données serait une invention.

Ce document décrit donc deux choses distinctes, clairement séparées :

1. **l'architecture réelle** — celle de l'outillage d'audit et de restauration, qui est le seul code
   du dépôt ;
2. **l'architecture cible** — ce que les documents laissent entrevoir pour le produit, en la
   marquant explicitement comme non arrêtée.

---

## 2. Architecture réelle : l'outillage

### 2.1 Cartographie

```
mathverse/
├── .gitignore
├── Equations Mathématiques/          ← les deux documents originels (40 Kio)
│   ├── equations_courbes_mathematiques.md
│   └── equations_courbes_animees_v2.md
├── docs/                             ← 2,2 Mio : la connaissance produite
│   ├── audit/                        ← Phase 0, 1, 2
│   │   ├── fiches/                      6 fiches de domaine (Phase 1)
│   │   ├── fiches-phase-2/              11 fiches de plateforme (F01–F11)
│   │   ├── annexes/                     registres, CSV, comparaisons
│   │   └── A1…A10, PHASE-0, BILAN       rapports
│   ├── decisions/                    ← 2 décisions formalisées (ADR)
│   ├── restauration/                 ← le chantier de reconstruction
│   │   ├── propositions/                 fiches de lots + patchs JSON + journaux
│   │   ├── livrables/                    23 .gitdiff + messages de commit
│   │   └── annexes/                      14 rapports d'application
│   └── project-knowledge/            ← le présent dossier
└── tools/                            ← 408 Kio : l'outillage Python
    ├── audit-phase1/                 6 scripts de mesure
    └── restauration/                 24 scripts + 1 script shell
```

### 2.2 Responsabilités

| Dossier | Rôle | Dépendances | Statut |
|---|---|---|---|
| `Equations Mathématiques/` | **graine du projet** — contenu originel, jamais modifié depuis le premier commit | aucune | figé (`bdba473`) |
| `docs/audit/` | connaissance produite sur le corpus et le marché | outils | actif |
| `docs/decisions/` | décisions formalisées et opposables | aucune | actif |
| `docs/restauration/` | propositions, livrables et journaux de la reconstruction | `tools/restauration/` | actif |
| `tools/audit-phase1/` | **mesure** du corpus source, sans jamais l'écrire | Python stdlib | stable |
| `tools/restauration/` | reconstruction, application et diffusion des correctifs | Python stdlib, `git` | actif |

### 2.3 Le principe architectural commun

✅ **Vérifié sur les 30 scripts** : l'outillage est conçu selon quatre règles constantes.

```
1. DÉTERMINISME     — aucun script ne dépend du réseau pour produire sa mesure
2. NON-ÉCRITURE     — aucun script n'écrit dans le corpus source sans validation explicite
3. MESURE D'ABORD   — tout script compte avant de conclure ; aucune estimation
4. JOURNALISATION   — toute application produit un journal opposable (.journal.json)
```

Concrètement : `tools/audit-phase1/*` est **entièrement en lecture seule** sur le clone.
`tools/restauration/*` n'écrit qu'après une vérification stricte.

---

## 3. Les scripts d'audit (`tools/audit-phase1/`)

| Script | Lignes | Rôle | Sortie |
|---|---:|---|---|
| `extract_structure.py` | 38 | inventaire structurel : lignes, titres, équations, marqueurs de rigueur | CSV + JSON |
| `profil_degradation.py` | 184 | **distingue les documents aplanis des documents intacts par la mesure** | tableau |
| `check_equations.py` | 58 | détection des équations tronquées | rapport |
| `check_equations2.py` | 41 | intégrité, comptage par heuristique séparée (pas de score composite) | CSV |
| `extract_domain.py` | 81 | digest d'un document : plan, équations par section, marqueurs | texte |
| `check_names.py` | 38 | sonde de disponibilité de noms (npm, PyPI, GitHub) | rapport |

**Le script central est `profil_degradation.py`.** C'est lui qui a établi la distinction entre les
trois régimes de dégradation et permis de détecter les quatre documents aplanis (A, B, C, D) — dont
la signature est univoque : `0` titre, `0` bloc, `0` gras, `0` puce, avec 1 000+ caractères par
ligne.

---

## 4. Les scripts de restauration (`tools/restauration/`)

### 4.1 Deux moteurs, pas un

🔶 **Déduction confirmée par les docstrings** : les scripts se répartissent en deux générations,
parce que les deux chantiers ne travaillent pas sur la même chose.

#### Génération 1 — `apply_patch.py` : travail **ligne à ligne**

✅ Source : `apply_patch.py`, docstring.

Les blocs vides des régimes 1 et 2 occupent **une ligne**. Le principe est la vérification stricte :
chaque entrée indique un numéro de ligne et le bloc **exact** attendu (`ancien`). Si le bloc ne
correspond pas, l'application est **refusée**.

Scripts associés : `build_lot_L.py`, `build_lot_I_a/b/c.py`, `build_lot_J_a/b/c.py`,
`build_lot_N_a/b.py`, `build_lot_K*.py` — 10 générateurs de lots.

#### Génération 2 — `lot_commun.py` : travail **en sous-chaînes**

✅ Source : `lot_commun.py`, docstring.

Le document A est « aplani » : un paragraphe entier tient sur une seule ligne et les formules ont
été **déplacées**, parfois au milieu d'une phrase. Les restitutions portent donc sur des
sous-chaînes qui enjambent les sauts de paragraphe. Le moteur travaille en sous-chaînes et tient un
journal.

### 4.2 Les trois règles du moteur

✅ Source : `lot_commun.py`, docstring — les règles que le moteur **fait respecter**, pas seulement
recommande.

| # | Règle | Mécanisme |
|---|---|---|
| 1 | **Unicité** | chaque sous-chaîne source doit apparaître **exactement une fois** ; sinon le lot échoue sans rien écrire |
| 2 | **Non-perte** | un fragment ne peut être retiré que si **chacun de ses tokens** est recasé. Tout token sans destination établie **reste** dans le document, signalé par la mention « Fragments non rattachés » |
| 3 | **Vérifiabilité** | le journal porte, pour chaque substitution : l'ancien, le nouveau, la confiance, la justification et la validation |

C'est le mécanisme anti-invention du chantier. La règle de non-perte interdit de supprimer un
fragment dont on ne sait pas quoi faire : on le laisse et on le signale.

### 4.3 Les générateurs de lots

| Générateur | Document | Lot | Lignes |
|---|---|---|---:|
| `build_lot_A_1.py` … `_6.py` | A (régime 3) | 6 lots, 70 substitutions | 128–266 |
| `build_lot_B_1.py` | B (régime 3) | **lot 1, 6 substitutions — proposé, non appliqué** | 242 |
| `build_lot_L.py` | L | lot 2 | 462 |
| `build_lot_I_a/b/c.py` | I | lots 3a, 3b, 3c | 80–649 |
| `build_lot_N_a/b.py` | N | lots 4a, 4b | 333–431 |
| `build_lot_J_a/b/c.py` | J | lots 5a, 5b, 5c | 77–504 |

### 4.4 Les utilitaires

| Script | Rôle |
|---|---|
| `extract_blocks.py` | extraction compacte de tous les blocs d'affichage — permet la relecture exhaustive « un bloc à la fois » |
| `extract_defects.py` | inventaire des équations défectueuses (CSV) |
| `mesurer_couverture.py` | **mesure directe** de la couverture d'un document restauré — « lit les fichiers, ne recompose jamais un total par arithmétique » |
| `inventorier_fragments.py` | inventaire des formules déplacées dans un document aplani |
| `diff_lot_A.py` | produit le diff incrémental d'un lot |
| `render_lot.py` | rendu Markdown d'un lot à partir de son correctif JSON |
| `apply_patch.py` | application stricte (génération 1) |
| `lot_commun.py` | moteur sous-chaînes (génération 2) |
| `push_via_api.py` | création de branche via l'API quand `git push` est refusé (403 sur le dépôt de connaissances) |
| `reconstituer_atelier.sh` | **reconstruction complète de l'atelier** après réinitialisation |

---

## 5. Le script critique : `reconstituer_atelier.sh`

⚠️ **À connaître absolument avant de travailler.** L'environnement de développement se réinitialise
— au moins **sept fois** depuis l'ouverture du chantier. À chaque reset, le `.git` local et le clone
du corpus sont détruits.

Le script est **idempotent** et reconstruit tout :

```bash
bash tools/restauration/reconstituer_atelier.sh
```

| Étape | Action | Résultat attendu |
|---|---|---|
| 1 | `fetch` + `reset --mixed origin/arena/2e20eccb-mathverse` | branche restaurée |
| 2 | re-clonage du corpus à `f0f5e2d` | `/home/user/_audit/connaissance` |
| 3 | réapplication des **17 diffs** (régimes 1-2) | `17/17` — ⚠️ **ordre non interchangeable** |
| 4 | réapplication des **6 lots de A** (régime 3) | `6/6` — ⚠️ **incrémentaux, ordre 1→6** |
| 5 | vérification | mojibake `0`, **A = 78 756 caractères** |
| 6 | sauvegarde de reprise | `/home/user/_audit/sauvegardes/A-apres-domaine-A-lot6.md` — ⚠️ **hors dépôt**, donc provisoire |

✅ Vérifié le 2026-11-11 : `17/17`, `6/6`, mojibake `0`, A = 78 756.

⚠️ **Conséquence architecturale :** tout livrable doit être commité dans le dépôt. Ce qui reste
hors dépôt (`/home/user/_audit/`) est par nature provisoire.

---

## 6. Architecture cible du produit

🔷 **Envisagé** — aucune décision n'est prise. Ce qui suit est la synthèse de ce que les documents
laissent entrevoir, **pas** une architecture arrêtée.

### 6.1 Ce que le corpus suggère

Le domaine N contient la description d'un pipeline complet et implémentable
(`A8-synthese-et-point-de-reprise.md` §3.3) :

```
Microphone → Web Audio API → FFT → Canvas/WebGL
```

avec un mapping de `|X_k|` vers **8 attributs visuels** (§111) et le fenêtrage comme paramètre
réglable (§95). Le domaine I fonde les SDF et le raymarching sur le gradient comme normale à
`F(x,y,z)=0` (§109).

### 6.2 Les contraintes héritées des analyses

| Contrainte | Origine |
|---|---|
| Composant accompagné de ses équations, hypothèses, validité, limites, tests, performances | cahier des charges, 18 attributs |
| Registre à champs étendus, au format shadcn/ui | D6 |
| Installation par CLI, comme le secteur | attribut 7 |
| `llms.txt` et champs structurés pour les agents IA | R3.2, critère de choix 2026 |
| Mesures de performance **déléguées** (ni GPU ni navigateur ici) | D4 |
| **Ne pas** viser WebGPU comme différenciateur | Shaders y est déjà |

### 6.3 Ce qui reste à décider

| Décision | Statut |
|---|---|
| Framework (React dominant à 83 %, State of JS 2025) | ⬜ non décidé |
| Moteur de rendu (Canvas 2D / WebGL / WebGPU) | ⬜ non décidé |
| Format du registre | 🔷 le schéma shadcn est candidat |
| Stratégie de test | ⬜ non décidée |
| Hébergement et CI | ⬜ non instruit |
| Base de données | 🔷 **Supabase/PostgreSQL était une préférence initiale du porteur**, à comparer objectivement — aucune migration, aucun service payant sans autorisation |

---

## 7. Dette technique de l'outillage

| Problème | Gravité | Conséquence |
|---|---|---|
| ⚠️ **Aucun test automatisé** des 30 scripts | moyenne | la non-régression repose sur la relecture |
| ⚠️ **Chemins absolus** codés en dur (`RACINE = "/home/user/_audit/connaissance"`) | moyenne | l'outil ne fonctionne que dans ce sandbox |
| ⚠️ **Ordre d'application manuel** des 23 diffs | **haute** | un ordre faux corrompt le corpus reconstitué — d'où le script |
| 🔶 **Deux moteurs concurrents** (`apply_patch.py` et `lot_commun.py`) | faible | justifié par la différence de nature des régimes |
| ⚠️ **Aucune gestion de version de schéma** des journaux JSON | faible | les journaux ne sont pas rétro-compatibles par construction |
| ⚠️ `push_via_api.py` existe parce que `git push` renvoie 403 sur le dépôt de connaissances | moyenne | le porteur applique les diffs lui-même ; c'est une décision, pas un bug |

⚠️ **Aucune de ces corrections n'a été faite pendant cet audit** : la mission est documentaire.
