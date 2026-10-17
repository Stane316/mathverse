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

Le nom définitif n'est pas arrêté. En attendant, la documentation utilise le jeton neutre **« le projet »** et le nom technique sera injecté par une variable `PROJECT_CODENAME`, jamais écrit en dur. Voir `A1-propositions-de-nom.md`.

## 4. Conventions appliquées à ce dossier

- Noms de fichiers en `kebab-case`, sans espace ni accent, pour éviter toute friction d'outillage (convention proposée pour l'ensemble du dépôt, en attente de validation).
- Un livrable = un fichier, avec en-tête daté et section « statut ».
- Les données chiffrées sont conservées en annexe, pas noyées dans la prose.
