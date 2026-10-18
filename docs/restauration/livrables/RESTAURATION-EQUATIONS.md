# RESTAURATION DES ÉQUATIONS — branche `arena/restauration-equations`

> **Lire ceci avant de fusionner quoi que ce soit dans `main`.**

## Ce qu'est cette branche

Un certain nombre d'équations du corpus ont été **détruites** lors d'un traitement
automatique : les commandes LaTeX (`\frac`, `\sum`, `\lim`, `\log`, `\mathbf`) ont été
supprimées **avec leurs arguments**, ainsi que les lettres grecques. Exemple réel,
dans le document K avant restauration :

```
Le système de Lorenz est donné par :

\[ =(y-x) \]

\[ =x(-z)-y \]

\[ =xy-z \]

où :

- () ;
- () ;
- ()

sont des paramètres.
```

Cette branche contient les **reconstructions** de ces équations, validées lot par lot.

## Ce que cette branche n'est PAS

**Ce n'est pas une récupération.** Le contenu détruit n'existe plus nulle part dans les
fichiers : il n'a pas été déplacé, il a été effacé. Chaque équation de cette branche a
donc été **réécrite** à partir des fragments survivants et de la forme canonique connue
du modèle mathématique. Une équation reconstruite est **indistinguable d'une équation
d'origine** une fois le texte fusionné — c'est pourquoi ce fichier existe.

Conséquence pratique : **ne citez pas une équation restaurée comme une source
autorisée.** Vérifiez-la contre une référence externe, comme n'importe quelle
reconstruction.

## Échelle de confiance

| Niveau | Signification |
|---|---|
| **haute** | le fragment survivant et la forme canonique n'autorisent pas d'autre lecture raisonnable |
| **moyenne** | forme canonique probable, mais un choix de notation ou de normalisation subsiste |
| **inconnue** | l'intention de l'auteur est requise ; **non appliqué** |

Chaque proposition porte sa justification et un **test de validation** (une propriété
vérifiable qui doit être satisfaite si la reconstruction est correcte).

## État des lots

| Lot | Document | Défauts traités | Confiance | Statut |
|---|---|---:|---|---|
| 1 | K — Fractales, chaos & systèmes dynamiques | 19 / 20 | 14 haute, 5 moyenne, 1 en attente | **appliqué** (2026-10-18) |

Un défaut reste en attente dans K : la section 166 « FORMULE DE RÉFÉRENCE » (bloc vide),
qui demande l'intention de l'auteur.

Défauts restants dans le corpus au 2026-10-18 : **707** (le décompte initial était de
724, dont 18 dans le document K).

## Détail et suivi

Le dossier de référence — inventaire complet des 724 défauts, justifications, tests de
validation, correctifs JSON applicables par script — est dans le dépôt `mathverse`,
branche de travail, sous `docs/restauration/`. Cette branche-ci ne contient que les
modifications de texte.

## Comment relire

```bash
git diff main..arena/restauration-equations --stat
git diff main..arena/restauration-equations -- Maths-vers-Informatiques/
```

Chaque lot correspond à un commit distinct, ce qui permet de relire ou de refuser un lot
sans toucher aux autres.
