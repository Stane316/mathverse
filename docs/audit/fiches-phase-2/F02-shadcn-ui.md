# F02 — SHADCN/UI

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** API publique GitHub
**Priorité de cette fiche :** la **mécanique de registre** — c'est l'origine déclarée du modèle
que Mathemirum veut reprendre, et elle est sous licence MIT.

---

## 1. Présentation et positionnement

« Composants composables et accessibles, avec des valeurs par défaut réfléchies. Construisez
votre propre bibliothèque de composants avec du code. » 125 966 étoiles, TypeScript, dépôt actif
au jour de l'observation. shadcn/ui n'est pas une bibliothèque de composants : **c'est une
méthode de distribution**. Cette distinction est la raison d'être de cette fiche.

## 2. Fonctionnalités

- Composants d'interface (Radix UI + Tailwind), accessibles.
- **CLI `shadcn`** : `add`, `init`, et la résolution de dépendances.
- Registre : un format JSON décrivant des composants, leurs fichiers et leurs dépendances.
- Modèles de projet (`templates`), moteur React (`packages/react`).

## 3. Parcours utilisateur

`npx shadcn@latest init` → configuration (`components.json`) → `npx shadcn@latest add <composant>`
→ **le code source est écrit dans le projet de l'utilisateur**. Rien n'est installé comme
dépendance. L'utilisateur possède le code et peut le modifier.

## 4. Architecture technique observable

Le dépôt est un **monorepo**. Les paquets observés :

| Paquet | Rôle présumé |
|---|---|
| `shadcn` | la CLI |
| `registry` | le registre (application et/ou format) |
| `react` | le moteur côté React |
| `helpers` | utilitaires |
| `tests` | tests |
| `templates`, `apps` | modèles de projet et applications de démonstration |

Le répertoire `skills` et les configurations `.claude`, `.cursor-plugin` à la racine indiquent une
**intégration explicite aux assistants de code** — signal intéressant pour un projet qui veut
embarquer des prompts.

## 5. Mode de distribution — le point central

Le modèle est **« copier le code, ne pas installer la dépendance »**. Conséquences :

- pas de conflit de versions avec la bibliothèque ;
- le composant est modifiable localement, sans fork ;
- **la mise à jour n'est pas automatique** : c'est le prix assumé du modèle.

Le format d'échange est un **article de registre** : un objet JSON décrivant le nom, les fichiers,
leurs chemins cibles et les dépendances. C'est ce format qui rend l'écosystème interopérable —
au point qu'un tiers (React Bits, fiche F01) peut *émettre* des articles compatibles via
l'adaptateur `@jsrepo/shadcn` sans utiliser la CLI shadcn.

## 6. Prévisualisation et personnalisation

Prévisualisation sur le site ; personnalisation par **thème** (variables CSS) et par modification
directe du code copié. Le modèle ne cherche pas le réglage fin de chaque paramètre à la
prévisualisation — c'est React Bits qui pousse cet aspect (F01 §6).

## 7. Stratégie documentaire

Site de documentation intégré au dépôt ; `CONTRIBUTING.md`, `RELEASING.md`, `SECURITY.md` présents
— **les trois documents de gouvernance que Mathemirum devra produire**. ⚠️ Le contenu n'a pas été
lu en détail — voir §12.

## 8. Modèle de contribution

`CONTRIBUTING.md` présent, `.changeset` pour le versionnage, `kodiak.toml` pour l'automatisation
des fusions, `commitlintrc` pour la normalisation des messages. **L'infrastructure de contribution
est industrialisée.** ⚠️ Le processus effectif n'a pas été observé.

## 9. Licences et contraintes de réutilisation

**MIT.** Aucune clause additionnelle détectée. Le modèle de distribution lui-même — le format de
registre, l'idée du copier-coller, le CLI — est donc **librement réutilisable et réimplémentable**.

C'est le résultat le plus utile de cette phase : là où le concurrent direct (React Bits) est
fermé, **l'infrastructure qu'il utilise est ouverte**.

## 10. Points forts

- Le plus gros acteur du secteur (125 966 ★) et le plus adopté : l'écosystème d'outils, de
  modèles et d'extensions s'est construit autour.
- MIT, sans clause.
- Un format d'échange (l'article de registre) devenu un standard de fait.
- Gouvernance outillée : changesets, commitlint, automatisation des fusions, politique de
  sécurité publiée.

## 11. Limites

- ⚠️ **Aucune explication mathématique**, et ce n'est pas son objet : ce sont des composants
  d'interface, pas des visualisations.
- Le modèle du copier-coller **ne gère pas les mises à jour** : un composant copié reste à la
  version copiée.
- La personnalisation suppose de lire et modifier du code ; elle n'est pas paramétrique.

## 12. Éléments non vérifiés ⚠️

- Le schéma exact d'un article de registre (champs obligatoires, resolution des dépendances).
- Le fonctionnement précis du paquet `registry` (application ou simple format ?).
- Le contenu de `CONTRIBUTING.md`, `RELEASING.md`, `SECURITY.md`.
- L'usage concret du répertoire `skills` et des configurations d'assistants.
- Le nombre de composants et la politique de dépréciation.

## 13. Idées à retenir

- **Le format de registre est la vraie trouvaille.** Un objet JSON décrivant fichiers, chemins
  cibles et dépendances suffit à créer un écosystème interopérable. C'est l'infrastructure
  minimale que Mathemirum doit se donner avant d'écrire le moindre composant.
- **Posséder le code plutôt que dépendre d'un paquet** : c'est ce qui rend le modèle acceptable
  pour des composants que chacun veut adapter.
- **Les fichiers de gouvernance font partie du livrable.** `CONTRIBUTING`, `RELEASING`, `SECURITY`
  ne sont pas de la décoration : sans eux, une bibliothèque communautaire ne démarre pas.
- **L'intégration aux assistants de code est déjà un sujet** (`skills`, `.claude`,
  `.cursor-plugin`). Mathemirum prévoit un prompt par composant : le terrain est balisé.

## 14. Erreurs à éviter

- ❌ Confondre « utiliser le registre shadcn » et « dépendre de shadcn/ui ». Mathemirum peut
  adopter le **format** sans adopter les composants.
- ❌ Croire que le modèle du copier-coller résout la maintenance : il la déplace chez
  l'utilisateur. Si Mathemirum veut des mises à jour, il faut le prévoir explicitement.
- ❌ Sous-estimer le coût d'un registre : c'est une infrastructure, avec schéma, versionnage et
  résolution de dépendances.

## 15. Opportunités de différenciation

Le format de registre shadcn décrit **des fichiers et des dépendances**. Rien n'empêche d'y
ajouter des champs : equations, hypothèses, domaine de validité, références, prompt de
régénération, tests, mesures de performance. **Un registre « à champs étendus » est une
extension, pas une rupture** — et c'est exactement ce que le cahier des charges de Mathemirum
demande.

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| MIT, 125 966 ★, TypeScript, activité | `GET /repos/shadcn-ui/ui` | 2026-10-19 |
| Paquets `helpers, react, registry, shadcn, tests` | `GET /repos/shadcn-ui/ui/contents/packages` | 2026-10-19 |
| Arborescence, fichiers de gouvernance, `.claude`, `.cursor-plugin`, `skills` | `GET /repos/shadcn-ui/ui/contents/` | 2026-10-19 |

**Limite :** lecture de l'arborescence et des métadonnées seules. Aucun fichier de schéma ni de
documentation n'a été lu en détail à ce stade.
