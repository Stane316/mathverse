# Lot 3c — Domaine I, section 177 (SYNTHÈSE DES DOMAINES PRÉCÉDENTS)

**Source :** `Maths-vers-Informatiques/Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md`
**Périmètre :** les neuf blocs vides des lignes **3024 à 3040** du fichier restauré
**Statut :** propositions issues d'une analogie **transposée du domaine J**, où l'hypothèse correspondante a été validée par l'auteur le 2026-10-18. À confirmer. **Rien n'a été écrit dans votre copie locale.**

## Ce que ces neuf blocs sont

La section 177 ouvre sur « La progression mathématique construite jusqu'ici peut être
résumée ainsi : », puis enchaîne **neuf blocs vides**.

Le domaine J, rédigé par le même auteur, contient une section du **même type** :

> §155 — « La progression construite jusqu'ici peut être **comprise** comme : » … **dix**
> blocs vides … « La transition : `\[ IJ \]` est particulièrement importante. »

L'hypothèse A→…→J y a été soumise, puis **validée par l'auteur le 2026-10-18**.

Le domaine I étant le **neuvième** document du corpus et son §177 comptant exactement
**neuf** blocs, la même lecture s'applique : A, B, C, D, E, F, G, H, I.

## Pourquoi ces neuf blocs n'avaient jamais été soumis

Après application des lots 3a et 3b, 37 blocs du document restaient dégradés. Une
vérification croisée a montré que **28 avaient déjà été soumis comme inconnues** et que
**9 n'avaient jamais été vus** — ceux-ci.

Deux pièges avaient masqué l'écart, et ils valent d'être notés pour la suite :

1. **Les remplacements multi-lignes décalent les numéros de ligne.** Un bloc de trois
   lignes remplacé par une seule décale tout ce qui suit. Comparer un numéro de ligne
   « avant » avec un bloc « après » ne prouve rien.
2. **Des blocs identiques sont indiscernables par leur contenu.** Le document contenait
   cinq blocs réduits à `\[ = \]`. Vérifier qu'« un bloc `=` existe encore » ne dit pas
   *lequel*. Seule la ligne de contexte suivante permet de les distinguer.

La vérification a donc été refaite bloc par bloc, sur le contenu **et** le contexte.

## Une confirmation indépendante, au passage

En reprenant le document pour ce contrôle, j'ai re-dérivé de zéro les quatre blocs
`\[ = \]` des lignes 800, 824, 1350 et 1668 — quatre règles de chaîne. Les quatre
avaient déjà été restaurés par les lots 3a et 3b, **avec exactement les reconstructions
auxquelles j'aboutissais** : `dz/dx=(dz/du)(du/dx)`, la chaîne `∂L/∂W`, sa variante en
`y`, et `∇_θ L=(∂L/∂ŷ)(∂ŷ/∂θ)`. Deux lectures indépendantes du même contexte
aboutissant à la même formule est le meilleur contrôle disponible ici.

## Réserve

Chaque résidu est vide : aucun caractère ne subsiste pour confirmer la lettre bloc par
bloc. Et l'argument est une **analogie entre deux documents**, non une preuve interne au
domaine I. Confiance **moyenne**. Si l'analogie ne vous convient pas pour I, les neuf
lignes se retirent d'un seul geste.

---

**Correctif :** `domaine-I-lot3c.patch.json` — 9 entrées : 0 haute, 9 moyenne, 0 inconnue — **9 applicables**

### Confiance moyenne (9)

| Ligne | Actuel | Reconstruction | Validation |
|---:|---|---|---|
| 3024 | `\[ \]` | `\[ A \]` | Domaine A — DOCUMENT MAÎTRE A — LOGIQUE ET FONDEMENTS DE L’INFORMATIQUE. Analogie avec le §155 du domaine J (même formule d'introd |
| 3026 | `\[ \]` | `\[ B \]` | Domaine B — DOCUMENT B — THÉORIE DES NOMBRES. Analogie avec le §155 du domaine J (même formule d'introduction, dix blocs pour dix  |
| 3028 | `\[ \]` | `\[ C \]` | Domaine C — DOCUMENT C — ALGÈBRE LINÉAIRE. Analogie avec le §155 du domaine J (même formule d'introduction, dix blocs pour dix dom |
| 3030 | `\[ \]` | `\[ D \]` | Domaine D — DOCUMENT D — GÉOMÉTRIE COMPUTATIONNELLE. Analogie avec le §155 du domaine J (même formule d'introduction, dix blocs po |
| 3032 | `\[ \]` | `\[ E \]` | Domaine E — DOCUMENT E — THÉORIE DES GRAPHES. Analogie avec le §155 du domaine J (même formule d'introduction, dix blocs pour dix  |
| 3034 | `\[ \]` | `\[ F \]` | Domaine F — DOCUMENT F — COMBINATOIRE ET OPTIMISATION COMBINATOIRE. Analogie avec le §155 du domaine J (même formule d'introductio |
| 3036 | `\[ \]` | `\[ G \]` | Domaine G — Document G — Probabilités. Analogie avec le §155 du domaine J (même formule d'introduction, dix blocs pour dix domaine |
| 3038 | `\[ \]` | `\[ H \]` | Domaine H — Document H — Statistiques. Analogie avec le §155 du domaine J (même formule d'introduction, dix blocs pour dix domaine |
| 3040 | `\[ \]` | `\[ I \]` | Domaine I — Domaine I — Calcul différentiel (le présent document). Analogie avec le §155 du domaine J (même formule d'introduction |

