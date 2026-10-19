# F07 — GEOGEBRA

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** API GitHub, pages publiques de licence, recherche web
**Motif de cette fiche :** le régime de licence est **le plus complexe de toutes les plateformes
étudiées** — quatre régimes distincts coexistent, et une clause de co-propriété des productions est
signalée.

---

## 1. Présentation et positionnement

« Les outils mathématiques gratuits préférés dans le monde, utilisés par plus de 100 millions
d'élèves et d'enseignants. » Suite logicielle de mathématiques (géométrie, algèbre, calcul,
statistiques, 3D), déclinée en applications web et installables, et largement utilisée dans
l'enseignement.

## 2. Fonctionnalités

- Applications mathématiques : géométrie, algèbre, calcul, statistiques, tableur, 3D, CAS.
- **Intégration web** : une bibliothèque JavaScript permettant d'incorporer les applications dans
  n'importe quel site (`geogebra/integration`).
- **API JavaScript** pour piloter les applications incorporées.
- Plateforme de matériaux pédagogiques partagés.

## 3. Parcours utilisateur

Deux parcours : utilisation directe des applications (navigateur ou installable), ou incorporation
dans un site tiers via la bibliothèque d'intégration.

## 4. Architecture technique observable

| Dépôt | Licence déclarée | ★ | Langue | Activité |
|---|---|---|---|---|
| `geogebra/geogebra` (le moteur) | **aucune** (`NONE`) | 2 352 | Java | 2026-10-19 |
| `geogebra/integration` (bibliothèque d'intégration) | **aucune** (`NONE`) | 28 | HTML | 2026-10-19 |
| `geogebra/legal` | — | — | — | — |

⚠️ **Aucun des deux dépôts ne porte de licence reconnue par GitHub.** Le code source est publié,
mais le régime applicable est déclaré ailleurs, sur le site de l'éditeur.

## 5. Mode de distribution

Applications web et installables (Linux, macOS, Windows, Android, iOS), plus une bibliothèque
d'intégration web. Usage gratuit **pour un usage non commercial** ; usage commercial soumis à une
licence et à un accord de collaboration spécifiques.

## 6. Prévisualisation et personnalisation

L'intégration permet de personnaliser les applications incorporées ( dimensions, barre d'outils,
état initial ) et de les piloter par API. ⚠️ Le détail des options n'a pas été évalué.

## 7. Stratégie documentaire

Documentation d'intégration publiée sur `geogebra.github.io` (guide d'incorporation, guide d'API).
Dépôt `geogebra/legal` contenant les textes juridiques. ⚠️ La profondeur n'a pas été évaluée.

## 8. Modèle de contribution

⚠️ **Non vérifié.** Les dépôts sont publics et actifs, mais le processus d'acceptation des
contributions externes n'a pas été observé.

## 9. ⚠️ Licences et contraintes de réutilisation — le point central

**Quatre régimes distincts coexistent**, ce qui rend toute décision d'usage délicate :

| Composant | Régime | Source |
|---|---|---|
| **Code source** | **EUPL v1.2** (la page officielle actuelle) — ⚠️ des sources tierces et une discussion ancienne évoquent **GPL-3.0** | `geogebra.org/license` ; Wikipédia ; Open Source SE (2019) |
| **Installateurs et services web** | **licence propre non commerciale** — usage non commercial uniquement, avec attribution | `geogebra.org/license` |
| **Fichiers de langue, documentation, images et styles d'interface** | **CC BY-NC-SA** (la page officielle indique 4.0 ; Wikipédia indique 3.0) | `geogebra.org/license`, `geogebra.org/tos` |
| **Usage commercial** | licence spécifique + accord de collaboration, payants | `geogebra.org/license` |

⚠️ **Une divergence est documentée sur le code source** : la page officielle actuelle déclare
l'EUPL v1.2, tandis que des sources tierces et des discussions anciennes évoquent la GPL-3.0. La
page officielle fait foi **sous réserve de vérification au moment de l'usage**.

**La clause la plus lourde, et elle est facile à manquer — la co-propriété des productions :**

> « Materials generated using GeoGebra are a derived product of the GeoGebra software and thus are
> **under the copyright of both GeoGebra and the party who generated the materials**. Use of the
> materials generated using GeoGebra are restricted to the terms of this agreement and protected
> from commercial use by others. »

Autrement dit : **un graphique, une figure ou un matériau produit avec GeoGebra est co-détenu par
GeoGebra**, et son usage commercial est restreint. Pour un projet qui produirait des visualisations
mathématiques, c'est une contrainte majeure.

**Conséquences pour Mathemirum :**

| | Verdict |
|---|---|
| Réutiliser le code source dans un composant | ⚠️ EUPL — copyleft **fort, et compatible à titre de réciprocité** : à vérifier contre la licence cible |
| Incorporer les applications web dans un produit destiné au public | ❌ usage non commercial uniquement ; licence commerciale requise |
| Réutiliser les images, icônes et styles d'interface | ❌ CC BY-NC-SA — non commercial **et** partage à l'identique |
| Publier des figures produites avec GeoGebra, puis les exploiter commercialement | ⚠️ **co-propriété GeoGebra** — à éviter sans accord |

**EUPL contre MIT :** l'EUPL est une licence copyleft forte avec une clause de réciprocité
étendue au réseau. Si Mathemirum adopte une licence permissive, **l'intégration de code EUPL est
incompatible**. C'est un point dur, pas une nuance. ⚠️ La qualification précise demande une
vérification juridique.

## 10. Points forts

- Une couverture fonctionnelle exceptionnelle (géométrie, algèbre, calcul, statistiques, 3D, CAS).
- Une bibliothèque d'intégration web documentée, avec API JavaScript.
- Une adoption massive dans l'enseignement.
- Le code source est publié — on peut étudier les algorithmes.

## 11. Limites

- ⚠️ **Quatre régimes de licence superposés**, dont deux non commerciaux.
- ⚠️ **La clause de co-propriété des productions** est un piège pour tout projet qui génère des
  figures.
- ⚠️ **Aucune licence déclarée sur les dépôts GitHub**, contrairement à toutes les autres
  plateformes étudiées : il faut aller la chercher sur le site.
- Divergence documentée sur le régime du code source (EUPL contre GPL).
- Applications lourdes, pensées pour l'enseignement, pas pour l'intégration dans une page de
  composants.

## 12. Éléments non vérifiés ⚠️

- Le régime exact du code source : EUPL v1.2 ou GPL-3.0 — **divergence non résolue**.
- La version exacte de la licence CC (3.0 ou 4.0).
- Les tarifs et conditions de la licence commerciale.
- Le contenu détaillé de la documentation d'intégration.
- La portée réelle de la clause de co-propriété sur une figure exportée.

## 13. Idées à retenir

- **Publier son code ne suffit pas à le rendre réutilisable.** GeoGebra publie son moteur sur
  GitHub sans y déclarer de licence : le geste technique est ouvert, le geste juridique ne l'est
  pas. C'est le contre-modèle de ce que Mathemirum doit faire.
- **Une licence par composant peut coexister** : code, installateurs, et ressources graphiques
  relèvent ici de trois régimes. Toute décision d'usage doit donc être prise **par type de bien**,
  jamais globalement.
- **Le copyleft fort est une contrainte d'architecture**, pas une préférence : choisir l'EUPL
  interdit de fait une redistribution sous licence permissive.

## 14. Erreurs à éviter

- ❌ Lire « GeoGebra est open source » et en déduire qu'on peut l'intégrer : le **code** est sous
  EUPL, mais les **installateurs et services web** sont non commerciaux.
- ❌ Générer des figures avec GeoGebra puis les publier comme si elles appartenaient au projet :
  la clause de co-propriété s'applique aux productions.
- ❌ Mélanger des images d'interface (CC BY-NC-SA) dans un produit : le partage à l'identique est
  viral.

## 15. Opportunités de différenciation

GeoGebra est la preuve qu'un outil mathématique peut atteindre 100 millions d'utilisateurs — **la
demande est établie, ce n'est pas une hypothèse**. Mais son régime ferme la porte à
l'intégration dans un produit tiers. La place est donc doublement libre : sur le plan technique
(composant possédé plutôt que service incorporé) et sur le plan juridique (une licence unique,
claire, déclarée dans le dépôt, là où GeoGebra en superpose quatre).

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| Dépôts sans licence déclarée, étoiles, activité | `GET /repos/geogebra/geogebra`, `GET /repos/geogebra/integration` | 2026-10-19 |
| EUPL v1.2 pour le code ; installateurs et services web non commerciaux ; CC BY-NC-SA pour les ressources | `geogebra.org/license` (page publique) | 2026-10-19 |
| CC BY-NC-SA 4.0 pour le contenu du site | `geogebra.org/tos` (page publique) | 2026-10-19 |
| Co-propriété des productions, licence commerciale, durées | dépôt `geogebra/legal` (extraits, recherche web) | 2026-10-19 |
| Divergence EUPL / GPL-3.0 | Wikipédia, Open Source Stack Exchange (2019) | 2026-10-19 |

**Limites :** lectures de pages publiques et d'extraits du dépôt `legal`, non des contrats complets.
**Aucune vérification juridique.** La divergence EUPL/GPL n'est pas résolue.
