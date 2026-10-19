# F05 — UNIVERSE

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** API GitHub, pages publiques du site
**Rappel :** partiellement étudié en phase 0 — 7 456 éléments d'interface recensés, gratuits pour
un usage personnel et commercial.

---

## 1. Présentation et positionnement

« La plus grande bibliothèque d'interface open source ! Créée par la communauté et libre
d'utilisation. » Plateforme communautaire d'éléments d'interface — boutons, chargements,
interrupteurs, cases à cocher — réalisés en **CSS pur ou avec Tailwind**. Le dépôt miroir
`uiverse-io/galaxy` comptabilise 13 585 étoiles au jour de l'observation.

## 2. Fonctionnalités

- Éléments d'interface élémentaires (boutons, animations de chargement, interrupteurs, cases à
  cocher, champs de saisie).
- **Deux variantes par élément** : CSS pur et Tailwind.
- Recherche, filtrage par catégorie, copie du code.
- Contributions de la communauté.

Le positionnement est celui de la **brique élémentaire**, non du composant composé : c'est un
niveau d'abstraction en dessous de React Bits ou d'Aceternity.

## 3. Parcours utilisateur

Recherche → aperçu en direct → choix de la variante (CSS / Tailwind) → copie du code. Pas
d'installation, pas de CLI mentionnée. Le parcours est le plus simple de toutes les plateformes
étudiées.

## 4. Architecture technique observable

Le site est accessible en HTTP ; le dépôt `uiverse-io/galaxy` est en HTML, publié sous MIT.
⚠️ **L'architecture du site lui-même n'a pas été inspectée** : la relation exacte entre le site
`uiverse.io` et le dépôt miroir n'a pas été établie à ce stade.

## 5. Mode de distribution

Copier-coller depuis le site. Le dépôt miroir est sous **MIT**. Le site annonce la gratuité pour
un usage personnel **et commercial**.

## 6. Prévisualisation et personnalisation

Aperçu en direct pour chaque élément, avec les deux variantes de langage. Personnalisation par
modification directe du code copié — pas de paramètres réglables.

## 7. Stratégie documentaire

Documentation minimale : chaque élément se suffit à lui-même et se lit dans son code. C'est une
conséquence du niveau d'abstraction, pas une lacune.

## 8. Modèle de contribution

⚠️ **Modèle communautaire annoncé, processus non vérifié.** Le dépôt miroir est public, mais le
flux effectif entre le site et le dépôt, les critères d'acceptation et la gouvernance n'ont pas
été observés.

## 9. Licences et contraintes de réutilisation

**MIT** pour le dépôt `uiverse-io/galaxy`. Le site annonce un usage gratuit, personnel et
commercial.

⚠️ Deux réserves méthodologiques, et elles sont sérieuses :
1. **MIT sur un dépôt miroir ne garantit pas la licence de chaque élément.** Uiverse est une
   plateforme de contribution : chaque élément est déposé par un tiers. Le régime applicable à un
   élément donné dépend de son auteur. ⚠️ **Le site ne semble pas afficher de licence par
   élément** — ce point n'a pas pu être vérifié.
2. **Le dépôt est inactif depuis le 2 septembre 2024**, soit plus de deux ans au jour de
   l'observation (2026-10-19). Le décalage entre un site actif et un miroir figé mérite d'être
   éclairci avant tout usage.

## 10. Points forts

- **Le plus grand catalogue du secteur en volume** (7 456 éléments) — l'ordre de grandeur dépasse
  largement les autres plateformes étudiées.
- **Double variante CSS / Tailwind**, ce qui élargit l'audience au-delà des utilisateurs de Tailwind.
- Pas de dépendance : des éléments autonomes, copiables dans n'importe quel projet.
- MIT sur le miroir.

## 11. Limites

- ⚠️ **Dépôt inactif depuis plus de deux ans** : le risque d'abandon est réel, et la pérennité du
  site elle-même n'est pas garantie.
- ⚠️ **Aucune explication mathématique** : ce sont des éléments d'interface courants.
- **Licence par élément non vérifiable** dans l'état actuel de la collecte.
- Le niveau d'abstraction est bas : un bouton animé n'est pas une visualisation.

## 12. Éléments non vérifiés ⚠️

- La licence applicable à chaque élément, et l'existence d'un affichage par élément.
- La relation entre le site et le dépôt miroir (lequel fait foi ?).
- L'activité réelle du site, indépendamment du dépôt.
- Le processus de contribution et de modération.
- Le nombre exact d'éléments à la date d'observation (les 7 456 datent de la phase 0, 2026-10-17).

## 13. Idées à retenir

- **La double variante de langage est une bonne idée, déjà éprouvée** (CSS pur *et* Tailwind).
  React Bits génère JS et TS ; Uiverse CSS et Tailwind. Le principe — une source, plusieurs
  variantes — est une constante du secteur.
- **Un catalogue volumineux n'est pas un gage de pérennité** : le plus gros catalogue étudié
  (7 456 éléments) repose sur le dépôt le plus anciennement inactif (2 ans).
- Le niveau « brique élémentaire » a une valeur réelle : c'est ce qui manque souvent aux
  bibliothèques de composants composés.

## 14. Erreurs à éviter

- ❌ Prendre le MIT du dépôt miroir pour une couverture de l'ensemble du catalogue : sur une
  plateforme contributive, la licence se vérifie **élément par élément**.
- ❌ Bâtir une dépendance sur un dépôt inactif depuis deux ans sans vérifier la pérennité du site.

## 15. Opportunités de différenciation

Uiverse occupe le bas de l'échelle : des briques, sans explication, sans profondeur. Mathemirum
n'a rien à y gagner directement, mais **le précédent est instructif sur un point** : une
plateforme contributive de grande taille ne garantit ni la licence, ni la pérennité, ni la
qualité. C'est un argument pour un catalogue plus restreint et mieux spécifié.

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| MIT, 13 585 ★, HTML, dernière activité **2024-09-02** | `GET /repos/uiverse-io/galaxy` | 2026-10-19 |
| 7 456 éléments, gratuité personnelle et commerciale | relevé de la phase 0 (pages publiques du site) | 2026-10-17 |
| Tentative de dépôt `uiverse-io/uiverse` : introuvable | `GET /repos/uiverse-io/uiverse` | 2026-10-19 |

**Limite :** le site n'a pas été parcouru lors de cette session ; seules les données de la phase 0
et les métadonnées du dépôt miroir sont mobilisées.
