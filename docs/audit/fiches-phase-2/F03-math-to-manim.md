# F03 — MATH-TO-MANIM

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** API publique GitHub, recherche web
**Priorité de cette fiche :** c'est le projet qui réunit le plus explicitement **mathématiques +
invite IA + CLI** — trois des quatre attributs de la question posée en phase 2.

---

## 1. Présentation et positionnement

« Créez des animations et des notes d'étude épiques en maths et physique à partir de texte et
d'images. » 2 787 étoiles, Python, MIT, dépôt actif au jour de l'observation. Le projet se
présente comme une **chaîne d'agents IA** qui transforme une question en scène Manim rendue.

## 2. Fonctionnalités

- Pipeline multi-agents : intention → carte de connaissances → programme → dossier mathématique →
  liste de plans → spécification de scène → rendu.
- **Vérification** : un agent distinct (« Jev ») évalue chaque point de contrôle ; une étape
  d'audit des preuves est mentionnée.
- Plusieurs backends d'IA, un répertoire chacun : `astra`, `mythos`, `sol`, `grok`, `glm`, `mimo`,
  `argon`.
- Sortie : vidéo. Le projet revendique une démonstration phare de ~200 secondes et ~160 animations.

## 3. Parcours utilisateur

```
math-to-manim setup
math-to-manim login
math-to-manim doctor
math-to-manim run "Expliquer une idée mathématique par la géométrie 3D" -q m
```

L'utilisateur formule une intention en langage naturel ; le système planifie, rend, et propose
une révision.

## 4. Architecture technique observable

| Élément | Observation |
|---|---|
| `pyproject.toml` | nom du paquet `math-to-manim` |
| CLI | **un point d'entrée par backend** |
| Répertoires `astra/ mythos/ sol/ grok/ glm/ mimo/ argon/` | une implémentation par fournisseur d'IA |
| `docs/ examples/ tests/ papers/ experiments/ archive/ legacy/` | documentation, exemples, tests, articles |
| `.mcp.json`, `AGENTS.md`, `CLAUDE.md` | configuration d'agents explicite |
| `web/` | présence d'une interface web |
| `deployment/`, `docker-compose.base44.yml` | déploiement conteneurisé |

**La CLI** — c'est l'élément le plus instructif pour Mathemirum :

```
math-to-manim        = astra.cli:main
math-to-manim-astra  = astra.cli:main
math-to-manim-mythos = mythos.cli:main
math-to-manim-sol    = sol.cli:main
math-to-manim-grok   = grok.cli:main
math-to-manim-glm    = glm.cli:main
math-to-manim-mimo   = mimo.cli:main
m2m                  = astra.cli:main
m2m-sol              = sol.cli:main
```

Le même nom de commande, suffixé par le backend, avec des alias courts. **L'abstraction est
mince et lisible** : une CLI, plusieurs moteurs.

## 5. Mode de distribution

Paquet Python installable (une commande `pip install` documentée par un tiers). Un répertoire
`web/` et une configuration de déploiement suggèrent **une offre en ligne en plus du paquet**.
⚠️ Le modèle économique n'a pas été vérifié — voir §12.

## 6. Prévisualisation et personnalisation

Le rendu est contrôlé par un paramètre de qualité (`-q m`) et par un mécanisme de révision
(`--review-mode`). La personnalisation se fait **par le prompt et par la révision**, pas par des
paramètres réglables sur une prévisualisation en direct : on relance, on ne règle pas.

## 7. Stratégie documentaire

Répertoire `docs/`, `README` détaillé avec installation et démonstration, `AGENTS.md` et
`CLAUDE.md` pour cadrer le travail des agents. ⚠️ La profondeur de la documentation mathématique
n'a pas été évaluée.

## 8. Modèle de contribution

Dépôt public avec `tests/`. ⚠️ Le processus de contribution effectif n'a pas été observé.

## 9. Licences et contraintes de réutilisation

**MIT**, sans clause additionnelle détectée. Le référentiel est donc réutilisable et
réimplémentable.

Dépendance de fait : **Manim** (Communauté, MIT — 41 698 ★) pour le rendu, et des API d'IA
commerciales pour la génération. ⚠️ Le projet suppose donc **des clés d'API payantes** et une
connexion (`math-to-manim login`).

## 10. Points forts

- **Le couplage prompt + CLI + maths est explicite et abouti** : c'est le plus proche voisin de la
  thèse de Mathemirum trouvé à ce jour.
- **Une étape de vérification distincte** dans le pipeline (un agent qui conteste chaque étape, un
  auditeur de preuves). C'est une réponse sérieuse au risque « l'IA affirme n'importe quoi ».
- **MIT**, donc réutilisable.
- Abstraction multi-backends lisible, un répertoire par fournisseur.

## 11. Limites — la plus importante de cette phase

⚠️ **La sortie est une vidéo (MP4).** Ni composant web, ni objet réutilisable avec des
propriétés, ni aperçu paramétrique en direct, ni intégration dans une application. Le livrable se
regarde, il ne s'intègre pas.

Autres limites observables :
- dépendance à des API d'IA commerciales et à une authentification ;
- la personnalisation passe par une relance complète du rendu, coûteuse en temps ;
- le répertoire `legacy/` et `archive/` suggère une dette d'organisation.

## 12. Éléments non vérifiés ⚠️

- Le modèle économique exact et l'existence d'une offre payante (le répertoire `deployment/` et
  `web/` le suggèrent sans le prouver).
- La qualité mathématique effective des sorties — **non testée** : aucune animation n'a été
  générée ni visionnée.
- Le contenu réel des invites (le cahier des charges de Mathemirum en prévoit 13 champs : rien
  n'indique que ce projet en documente la structure).
- Le rôle précis de chaque backend.
- Les performances (temps de rendu, coût par animation).

## 13. Idées à retenir

- **Un point d'entrée CLI par backend**, avec alias courts : une abstraction simple qui évite la
  multiplication des outils.
- **Une étape de vérification séparée de la génération.** C'est la réponse au risque d'erreur, et
  elle est structurante : Mathemirum devrait prévoir, par composant, une étape qui *conteste*
  l'explication mathématique — pas seulement qui la produit.
- **`AGENTS.md` / `CLAUDE.md` comme documents de cadrage** : les instructions aux agents sont
  versionnées avec le code, pas dispersées dans les discussions.
- **Le pipeline est découpé en étapes nommées** (intention → carte → programme → dossier → plans →
  scène), chacune produisant un artefact intermédiaire. C'est ce qui rend la reprise possible.

## 14. Erreurs à éviter

- ❌ Prendre ce projet pour un précédent qui valide la thèse de Mathemirum : il valide le
  couplage prompt + maths, **pas** la sortie composant web.
- ❌ Supposer que la vérification par agent garantit l'exactitude mathématique : un agent qui
  conteste n'est pas une preuve. Le cahier des charges exige des hypothèses et une validation
  explicites.
- ❌ Ignorer le coût : chaque itération consomme des appels d'API payants.

## 15. Opportunités de différenciation

Math-To-Manim démontre qu'un **pipeline IA → maths → visuel** est réalisable et que le marché
existe (2 787 ★). Mais il s'arrête à la vidéo. Deux directions se dégagent pour Mathemirum :

1. **Le médium.** Produire un composant web avec propriétés réglables, au lieu d'un fichier vidéo.
   Le composant s'intègre, se teste, se versionne ; la vidéo non.
2. **La traçabilité.** Le pipeline de Math-To-Manim garde ses artefacts intermédiaires en interne.
   Les *exposer* — équations, hypothèses, domaine de validité, références — est ce qui distingue
   une démonstration d'un effet. C'est la ligne de partage du cahier des charges entre « effet
   artistique », « visualisation explicable » et « simulation validée ».

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| MIT, 2 787 ★, Python, activité | `GET /repos/HarleyCoops/Math-To-Manim` | 2026-10-19 |
| Points d'entrée CLI, nom du paquet | `GET /repos/HarleyCoops/Math-To-Manim/contents/pyproject.toml` | 2026-10-19 |
| Arborescence (backends, `docs/`, `web/`, `AGENTS.md`, `CLAUDE.md`) | `GET /repos/HarleyCoops/Math-To-Manim/contents/` | 2026-10-19 |
| Description du pipeline, commandes, étape de vérification | recherche web (page du dépôt, fiche tierce) | 2026-10-19 |
| Manim Communauté : MIT, 41 698 ★ | `GET /repos/ManimCommunity/manim` | 2026-10-19 |

**Limites :** aucune animation générée ni visionnée ; aucun contenu d'invite lu ; le modèle
économique n'est pas vérifié.
