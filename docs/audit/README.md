# Audit initial — mode d'emploi et statut

**Dépôt :** `Stane316/mathverse` — **Branche :** `arena/2e20eccb-mathverse` (branche de travail dédiée)
**Date de création :** 2026-10-17
**Nature :** documents d'audit, **à valeur probante**, pas encore des documents produit.

---

## 1. Ce dossier

Ce dossier contient les livrables **validés** de l'audit initial (Phase 0 et suivantes), déposés ici sur décision de l'utilisateur (arbitrage « brouillons hors dépôt, versions validées dans le dépôt »).

Les brouillons et copies de travail restent **hors dépôt**, dans `/home/user/audit/`, jusqu'à ce qu'ils soient considérés comme validés.

| Fichier | Contenu |
|---|---|
| `PHASE-0-rapport-audit-initial.md` | Rapport de Phase 0 : accès vérifiés, périmètre, résultats, lacunes, risques, recommandations, plans des Phases 1 et 2 |
| `A1-propositions-de-nom.md` | Shortlist de noms dont la disponibilité a été mesurée (npm, PyPI, GitHub) |
| `annexes/A0-inventaire-acces-et-preuves.md` | Inventaire chiffré des deux dépôts, des accès réseau, des capacités de l'environnement, et journal des opérations |

## 2. Règles appliquées

1. **Jamais d'écriture sur `main`.** Tous les commits vont sur la branche de travail. La branche `main` n'est ni modifiée ni poussée.
2. **Jamais de pull request.** L'intégration dans `main` reste une décision humaine.
3. **Aucune opération destructive.** Pas de suppression, pas de renommage, pas de réécriture d'historique.
4. **Séparation des rôles.** Le dépôt de connaissances (`Stane316/my-own-connaissance`) n'est lu que par clone en lecture seule, jamais modifié sans autorisation explicite.
5. **Distinction des statuts.** Chaque affirmation est étiquetée : *vérifié*, *hypothèse* ou *non vérifié*. Aucune hypothèse n'est présentée comme un fait.
6. **Traçabilité.** Chaque observation est datée et, quand c'est possible, associée à une commande reproductible.

## 3. Convention de nommage du projet

**Nom de travail retenu : `mathemirum`** — décision approuvée le 2026-10-18, consignée dans `docs/decisions/0001-nom-de-travail-mathemirum.md`.

Le nom reste provisoire et non déposé. Il est injecté par une variable `PROJECT_CODENAME`, **jamais écrit en dur** dans le code ni dans les gabarits ; la prose peut employer le jeton neutre « le projet » tant que l'interface n'est pas figée.

Campagne de nommage : `A1-propositions-de-nom.md` → `A3-noms-axes-semantiques.md` → `A4-noms-merveille-mathematique.md` → **`A5-noms-math-merveille.md`** (famille retenue et vérification de `mathauma`). 242 sondes au total, 175 candidats libres sur les trois registres, 58 éliminés par une antériorité réelle.

## 4. Conventions appliquées à ce dossier

- Noms de fichiers en `kebab-case`, sans espace ni accent, pour éviter toute friction d'outillage (convention proposée pour l'ensemble du dépôt, en attente de validation).
- Un livrable = un fichier, avec en-tête daté et section « statut ».
- Les données chiffrées sont conservées en annexe, pas noyées dans la prose.
