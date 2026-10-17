# A1 — PROPOSITIONS DE NOM (shortlist vérifiée)

**Date de vérification :** 2026-10-17
**Objet :** fournir des candidats de nom dont la disponibilité technique a été **mesurée**, et écarter ceux qui présentent une collision.
**Statut :** proposition — en attente de votre arbitrage. Tant que le nom n'est pas arrêté, la documentation utilise le jeton neutre « le projet » et une variable `PROJECT_CODENAME`.

---

## 1. Méthode de vérification

Pour chaque candidat, quatre sondes ont été exécutées le 2026-10-17 :

1. `https://registry.npmjs.org/<nom>` → 404 = libre ; 200 = pris.
2. `https://pypi.org/pypi/<nom>/json` → 404 = libre ; 200 = pris.
3. `https://api.github.com/repos/Stane316/<nom>` → 404 = nom disponible sous votre compte.
4. `https://api.github.com/search/repositories?q=<nom>+in:name` → dépôts homonymes existants (avec nombre d'étoiles).

Une recherche web complémentaire a été menée sur les deux meilleurs candidats pour détecter d'éventuelles marques ou services homonymes.

**Limite de cette vérification :** elle couvre npm, PyPI, GitHub et la recherche web générale. Elle **ne constitue pas une recherche d'antériorité de marque** (INPI, EUIPO, USPTO). Une vérification juridique restera nécessaire avant tout dépôt de marque ou toute communication publique durable.

## 2. Candidats recommandés

| Rang | Candidat | npm | PyPI | GitHub `Stane316/…` | Dépôts homonymes | Commentaire |
|---:|---|---|---|---|---|---|
| 1 | **mathemos** | libre | libre | libre | **aucun** | Le plus propre des candidats testés : aucune occupation sur les trois registres, aucun dépôt homonyme. Se prononce en français comme en anglais. Réserve : proximité phonétique avec la marque britannique « Mathmos » (fabricant de lampes à lave), à évaluer. |
| 2 | **mathoria** | libre | libre | libre | 3 dépôts, 0 ★ | Sonorité de « territoire / théoria ». Occurrences homonymes mineures et inactives. |
| 3 | **parametra** | libre | libre | libre | 2 dépôts, 0–1 ★ | Très cohérent avec le projet : le paramètre est l'unité centrale du produit (paramètres ajustables en direct, export de configuration). |
| 4 | **euclidia** | libre | libre | libre | 1 compte GitHub homonyme (0 ★) | Référence claire à la géométrie ; évocateur pour un écosystème visuel. Réserve : un compte GitHub `euclidia` existe déjà. |
| 5 | **matheon** | libre | libre | libre | 3 dépôts (0, 0, 8 ★) | Votre nom de la section 2 du cahier des charges. Disponible partout. Réserve : un gabarit HTML5 « matheon » existe (8 ★) dans un domaine éloigné. |

Candidats également libres sur les trois registres, mais jugés moins pertinents ou trop proches d'un projet existant :

| Candidat | Réserve |
|---|---|
| `morphomat` | trop proche de `morphomatics/morphomatics` (57 ★, bibliothèque de traitement de géométrie) |
| `numerion`, `mathemata`, `isomorpha`, `curvata`, `attracta`, `fractalys`, `noetica` | libres, mais sémantique ou mémorisation jugées plus faibles ; homonymes mineurs présents |

## 3. Candidats écartés — raisons

| Candidat | Motif de rejet (vérifié) |
|---|---|
| **mathverse** | Paquet PyPI `mathverse` **existant** ; benchmark universitaire « MathVerse » (ECCV 2024, dépôt MIT, 184 ★) ; jeu de données Hugging Face `AI4Math/MathVerse` ; suite d'applications web mathématiques homonyme. Risque de confusion maximal dans le domaine « mathématiques + vision ». |
| **matheia** | Libre sur npm/PyPI/GitHub, **mais** occupé commercialement : `matheia.com` (plateforme de tutorat), *Matheia School* (Seattle), *Matheia Society*. Écarté. |
| **apeiron** | npm **et** PyPI déjà pris ; dépôts `microsoft/apeiron`, `eouzoe/Apeiron` (17 ★). |
| **axiomos** | PyPI déjà pris ; dépôts `AxiomOS` actifs (17 ★, 14 ★). |
| **topograph** | npm déjà pris ; dépôt homonyme 193 ★. |
| **symplecta** | PyPI déjà pris. |

## 4. Recommandation

**Recommandé : `mathemos`**, sous réserve d'une vérification de la proximité avec la marque « Mathmos ».
**Alternative la plus thématique : `parametra`**, si vous privilégiez la cohérence sémantique avec le produit (paramètres, réglages, exploration).

**Mesure transitoire appliquée immédiatement :** tous les livrables utilisent le jeton neutre « le projet ». Le nom définitif sera injecté via une variable de configuration (`PROJECT_CODENAME`) et non écrit en dur dans le code ou la documentation — conformément à votre consigne.

## 5. Points exigeant votre arbitrage

1. Choisir un nom dans cette liste, ou demander une nouvelle génération de candidats sur un axe sémantique précis (géométrie, mouvement, lumière, exploration…).
2. Indiquer si une recherche d'antériorité de marque doit être prévue (elle sort du périmètre technique de cet audit).
