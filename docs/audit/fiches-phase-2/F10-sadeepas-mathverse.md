# F10 — MATHVERSE (sadeepas)

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** API GitHub (arborescence et README intégral)
**Motif de cette fiche :** demandée explicitement par le porteur. C'est le **seul projet trouvé
dont l'intitulé recouvre exactement l'objet de Mathemirum** : « une suite interactive
d'applications web mathématiques ».

---

## 1. Présentation et positionnement

> « **MathVerse** is a comprehensive collection of powerful, interactive, and beautifully designed
> web applications built to make complex mathematical concepts intuitive and engaging. From
> advanced calculus and probability simulation to trigonometric analysis, each tool is crafted to
> be a feature-complete and enjoyable experience for students, educators, and enthusiasts. »

Le projet revendique une **démonstration en ligne** : `sadeepas.github.io/MathVerse/mathsweb.html`.

⚠️ **Collision de nom.** Ce projet s'appelle **MathVerse** — le nom de travail retenu pour le
produit (`docs/decisions/0001-nom-de-travail-mathemirum.md` a tranché en faveur de *Mathemirum*).
Cette collision, déjà documentée en phase 0 avec `ZrrSkywalker/MathVerse`, se trouve ici doublée
d'une **collision de sujet**.

## 2. Fonctionnalités

Quatre applications, accessibles depuis un **hub central** (`mathsweb.html`) :

| Application | Fichier | Taille | Contenu déclaré |
|---|---|---|---|
| **Ultimate Dice Lab** | `dice.html` | 55 Ko | simulateur de probabilités et de statistiques |
| **Aura Graph Plotter** | `plotter.html` | 60 Ko | calculatrice graphique multi-mode |
| *Calculus* | `calculas.html` | 139 Ko | analyse (contenu non détaillé dans le README) |
| *Trigonométrie* | `trigo.html` | 93 Ko | trigonométrie (contenu non détaillé) |

**Ultimate Dice Lab** — le plus documenté :
- dés personnalisables (d4 à d20), jusqu'à 5 dés, thèmes visuels (Classic, Neon, Metallic) ;
- animations 3D à physique réaliste ;
- statistiques en temps réel (essais, moyenne, mode) ;
- **test d'équité du χ² (chi-deux)** déclenché après 100 essais ;
- mode casino (mises sur somme, pair/impair, haut/bas, solde persistant) ;
- simulation à grande vitesse (milliers d'essais) ;
- portabilité des données : export CSV, sauvegarde et chargement de l'état en JSON.

**Aura Graph Plotter** :
- modes **Standard (cartésien)**, **Polaire**, **Transformation** ;
- recherche automatique des **intersections** de deux fonctions ;
- analyse de calcul (détail non lisible — le README est tronqué dans la portion consultée).

## 3. Parcours utilisateur

Ouverture du hub → choix de l'application → interaction directe dans le navigateur. Aucune
installation : **chaque application est un fichier HTML autonome**.

## 4. Architecture technique observable

- **Vanilla JavaScript, CSS moderne, et un ensemble de bibliothèques open source** (déclaré, non
  détaillé).
- **Cinq fichiers HTML monolithiques**, de 36 Ko à 139 Ko, totalisant ~383 Ko. Le plus gros
  (`calculas.html`, 139 Ko) concentre à lui seul plus de tiers du code.
- **Aucun système de construction** : pas de `package.json`, pas de bundler, pas d'arborescence de
  sources. Le dépôt est plat : 5 HTML, 5 images, 1 README.
- Aucun test, aucune configuration d'intégration continue.

## 5. Mode de distribution

Hébergement statique via GitHub Pages. Aucun paquet, aucun registre, aucune CLI.

## 6. Prévisualisation et personnalisation

Prévisualisation par ouverture du fichier : c'est l'application elle-même. Personnalisation par
les contrôles de chaque application (type de dé, thème, mode de tracé). ⚠️ Aucun système de
paramètres exportables n'est déclaré, hors la sauvegarde d'état JSON du Dice Lab.

## 7. Stratégie documentaire

Un README de 6,8 Ko, structuré et illustré (captures d'écran pour chaque application), avec
démonstration en ligne et liste de fonctionnalités détaillée pour les deux premières applications.
**C'est un README de bonne qualité pour un projet de cette taille.**

⚠️ Les applications 3 et 4 (calcul, trigonométrie) ne sont pas décrites dans la portion du README
consultée — déséquilibre documentaire notable.

## 8. Modèle de contribution

⚠️ **Aucun.** Pas de `CONTRIBUTING`, pas de licence, pas d'historique de contributions. 2 étoiles,
un seul contributeur visible.

## 9. ⚠️ Licences et contraintes de réutilisation — le point décisif

**Aucune licence déclarée.** Ni fichier `LICENSE`, ni mention dans le README, ni champ côté API.

**Conséquence juridique :** en l'absence de licence, le droit d'auteur s'exerce par défaut —
**tous droits réservés**. Le code est visible sur un dépôt public, mais **rien n'autorise à le
copier, le modifier ou le redistribuer**. La visibilité publique n'est pas une licence.

⚠️ **Corollaire immédiat pour Mathemirum : ce projet ne peut servir de base, même partiellement.**
Et le risque n'est pas théorique : le sujet, le nom et même certaines fonctionnalités (tracé
polaire, analyse de calcul, test du χ²) recoupent le projet. **Toute reprise devrait être
documentée comme indépendante**, ce qui est plus difficile à établir après coup qu'avant.

**Le dépôt déclare en outre employer « un ensemble de bibliothèques open source puissantes »** —
sans les nommer. Ces bibliothèques conservent leurs propres licences ⚠️ **non identifiées**.

## 10. Points forts

- **Une vraie profondeur mathématique**, rare dans le corpus étudié : test d'équité du χ², analyse
  de calcul, tracé polaire et par transformation, recherche d'intersections. Rien de tel chez
  React Bits, Aceternity ou Magic UI.
- **La portabilité des données** (export CSV, état JSON) — une préoccupation que peu de
  visualisations en ligne ont.
- **Un README soigné**, avec captures et démonstration.
- **L'adéquation de l'intention** : c'est le seul projet trouvé qui veuille rendre « des concepts
  mathématiques complexes intuitifs et engageants » par des applications web.

## 11. Limites

- ⚠️ **Aucune licence** — blocage absolu pour toute réutilisation.
- ⚠️ **Aucune composabilité** : cinq fichiers HTML monolithiques, sans module, sans paquet, sans
  registre. On ne peut pas « importer » une application.
- ⚠️ **Aucune explication mathématique exposée** : le χ² est calculé, pas expliqué ; les courbes
  sont tracées, sans hypothèses ni domaine de validité. C'est la différence exacte avec le cahier
  des charges de Mathemirum.
- ⚠️ **Aucun test, aucune mesure de performance**, aucune CLI.
- Traction nulle : 2 étoiles, dernière activité le 25 novembre 2025.

## 12. Éléments non vérifiés ⚠️

- Le contenu effectif des applications *Calculus* et *Trigonométrie*.
- **Les bibliothèques open source employées et leurs licences** — déclarées en bloc, non nommées.
- Le fonctionnement réel : ⚠️ **aucune application n'a été ouverte ni testée.**
- L'exactitude des mathématiques affichées.
- La paternité : un seul contributeur visible, mais rien ne garantit l'originalité du code.

## 13. Idées à retenir

- **L'intention juste ne suffit pas.** Ce projet veut exactement ce que veut Mathemirum, et il n'a
  convaincu personne (2 étoiles). La différence ne tient donc pas à l'idée, mais à **l'exécution** :
  composabilité, documentation de la méthode, confiance.
- **Un fichier HTML autonome est une impasse pour la réutilisation.** C'est pratique à publier,
  impossible à composer.
- **Déclarer ses dépendances fait partie de la licence.** « Un ensemble de bibliothèques open
  source » sans les nommer est une impasse juridique pour qui voudrait réutiliser.

## 14. Erreurs à éviter

- ❌ S'inspirer du code, même partiellement : le nom, le sujet et l'absence de licence font de ce
  dépôt le **pire point de départ possible** pour Mathemirum sur le plan juridique.
- ❌ Confondre « dépôt public » et « code réutilisable » : ici, l'absence de licence rend la
  réutilisation **illicite par défaut**.
- ❌ Négliger la collision de nom : deux projets s'appellent déjà MathVerse. La décision
  *Mathemirum* en est d'autant plus justifiée.

## 15. Opportunités de différenciation

Ce projet est **le cas d'école de ce que Mathemirum doit faire différemment**, point par point :

| MathVerse (sadeepas) | Mathemirum |
|---|---|
| aucun fichier de licence | licence choisie, déclarée, par composant |
| 5 fichiers HTML monolithiques | composants modulaires, installables |
| mathématiques calculées, non expliquées | équations, hypothèses, domaine de validité |
| dépendances non nommées | dépendances déclarées |
| aucun test | tests par composant |
| aucune mesure | mesures de performance par composant |
| pas de prompt | prompt de régénération par composant |

**La place est donc libre, et ce projet montre pourquoi elle l'est encore** : l'intention ne
manque pas, l'infrastructure oui.

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| Absence de licence, 2 ★, HTML, activité 2025-11-25 | `GET /repos/sadeepas/-MathVerse-…` | 2026-10-19 |
| 12 fichiers : 5 HTML (36–139 Ko), 5 images, README 6,8 Ko | `GET /repos/sadeepas/-MathVerse-…/contents/` | 2026-10-19 |
| Description, démonstration, Dice Lab, Aura Plotter, pile technique | `GET /repos/sadeepas/-MathVerse-…/contents/README.md` (intégral) | 2026-10-19 |

**Limites :** ⚠️ **aucune application ouverte ni testée** ; le README est tronqué avant la
description des applications 3 et 4 ; les bibliothèques employées ne sont pas identifiées. Aucune
vérification juridique.
