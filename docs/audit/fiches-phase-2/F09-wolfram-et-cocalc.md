# F09 — WOLFRAM ET COCALC

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** API GitHub, pages publiques, recherche web
**Note :** deux plateformes réunies dans une même fiche, parce que ni l'une ni l'autre n'est un
acteur du composant web. Elles sont étudiées ici comme **références de calcul**, c'est-à-dire
commes des sources d'algorithmes et de validation, non comme des concurrents.

---

## 1. Présentation et positionnement

**Wolfram** réunit Mathematica (calcul formel), le langage Wolfram, Wolfram|Alpha (moteur de
connaissance computationnelle) et Wolfram Engine. C'est la référence historique du calcul
mathématique assisté par ordinateur. **Propriétaire.**

**CoCalc** (Collaborative Calculation in the Cloud) est un environnement de calcul collaboratif en
ligne — tableaux de bord Jupyter, SageMath, LaTeX, R — orienté enseignement et recherche. Le dépôt
principal `sagemathinc/cocalc` compte 1 288 étoiles ; ⚠️ **il porte la mention « moved to
https://github.com/sagemathinc/cocalc-ai »**, signalant une réorientation du projet vers l'IA.

## 2. Fonctionnalités

**Wolfram :** calcul formel, calcul numérique, visualisation, statistiques, création
d'interfaces ; Wolfram|Alpha en ligne et par API ; Wolfram Engine appelable par d'autres
programmes.

**CoCalc :** calcul collaboratif dans le navigateur (Jupyter, Sage, R, LaTeX), partage de fichiers
en temps réel, gestion de cours.

## 3. Parcours utilisateur

**Wolfram :** achat de licence, ou accès web à Wolfram|Alpha, ou appel d'API avec une clé
d'application. Wolfram Engine s'installe et s'appelle depuis un programme.

**CoCalc :** inscription, création d'un projet, travail dans le navigateur. ⚠️ Le parcours exact
n'a pas été observé.

## 4. Architecture technique observable

**Wolfram :** ⚠️ fermée, non observable. Aucun dépôt public du moteur.

**CoCalc :** dépôt public en TypeScript, actif au 15 octobre 2026. Licence **non reconnue par
GitHub** (`NOASSERTION`). ⚠️ Le modèle économique (hébergement commercial, auto-hébergement) n'a
pas été vérifié.

## 5. Mode de distribution

**Wolfram :** licences commerciales ; Wolfram|Alpha en freemium ; API commerciale avec quota
gratuit non commercial ; Wolfram Engine Community Edition gratuite pour le pré-production.

**CoCalc :** service en ligne ; le dépôt permet un auto-hébergement, sous réserve de la licence.

## 6. Prévisualisation et personnalisation

Sans objet au sens des bibliothèques de composants : ce sont des environnements de calcul, pas des
catalogues d'éléments réutilisables.

## 7. et 8. Documentation et contribution

⚠️ **Non évaluées** pour l'une et l'autre. Voir §12.

## 9. ⚠️ Licences et contraintes de réutilisation

### Wolfram — un éventail de régimes, tous restrictifs

| Composant | Régime |
|---|---|
| **Mathematica** | **propriétaire** |
| **Wolfram\|Alpha** (site) | gratuit pour un usage **personnel non commercial** ; abonnement Pro au-delà |
| **Wolfram\|Alpha API** | gratuit jusqu'à **2 000 appels non commerciaux par mois** ; ensuite 25 $ à 50 $ par millier de requêtes |
| **Wolfram Engine Community Edition** | gratuite, **usage de pré-production uniquement** |

Les conditions de la Wolfram Engine gratuite sont explicites :

> **Autorisé** — « pre-production/pre-distribution development of a product for Yourself or Your
> organization ; undertaking non-commercial projects for personal use ; exploring the Wolfram
> Language […] ; **Open-source projects approved by Wolfram**. »

> **Interdit** — « running the Free Engine in a **production software application** ; running the
> Free Engine expressly to **produce output for commercial or organizational use** ;
> decompiling, disassembling or **reverse engineering** ; **modifying the Free Engine in any
> manner** ; distributing, publishing, transferring, sublicensing, lending, leasing, renting or
> otherwise making available any portion of the Free Engine. »

**Ce qui mérite attention pour Mathemirum :** la mention « **open-source projects approved by
Wolfram** » dans les usages autorisés. Il existe donc une voie — **soumise à approbation
explicite**. ⚠️ Ni les critères d'approbation ni la procédure n'ont été vérifiés.

**Conséquence :** Wolfram peut servir de **référence de validation** (comparer un résultat) mais
pas d'infrastructure. L'interdiction de « produire des sorties à usage commercial ou
organisationnel » exclut de fait un moteur Wolfram gratuit derrière un composant distribué.

### CoCalc

Licence **non identifiée** par GitHub. ⚠️ **Non vérifiée :** le fichier de licence du dépôt n'a pas
été lu. Un `NOASSERTION` ne signifie pas « fermé », mais impose de lire le fichier avant tout usage.

## 10. Points forts

- **Wolfram :** la profondeur mathématique de référence, et un moteur de validation sans équivalent
  pour vérifier une équation ou une dérivée.
- **CoCalc :** un environnement complet pour l'enseignement, avec SageMath et Jupyter, publié en
  source ouverte.
- Les deux couvrent un spectre mathématique bien plus large que n'importe quelle bibliothèque web.

## 11. Limites

- ⚠️ **Wolfram est propriétaire** : aucune réutilisation de code, et l'usage gratuit exclut la
  production et l'usage commercial.
- ⚠️ **L'interdiction de décompiler et de modifier le Free Engine est explicite.** Toute
  rétro-ingénierie est proscrite.
- ⚠️ **CoCalc : licence non identifiée**, et réorientation annoncée du projet vers l'IA
  (`cocalc-ai`) — la pérennité de la plateforme de calcul mérite vigilance.
- Ni l'un ni l'autre ne produit de composant web.

## 12. Éléments non vérifiés ⚠️

- **CoCalc :** le fichier de licence du dépôt, le modèle économique, le parcours utilisateur, la
  portée réelle de la réorientation vers `cocalc-ai`.
- **Wolfram :** les critères et la procédure d'approbation des projets open source ; les conditions
  complètes de Wolfram|Alpha ; la politique sur l'affichage des résultats dans un produit tiers.
- Pour les deux : la documentation, la contribution, les performances.

## 13. Idées à retenir

- **Une référence n'est pas une dépendance.** Wolfram est inestimable pour *vérifier* qu'une
  équation est juste, et inutilisable pour *l'exécuter* dans un composant distribué. Les deux rôles
  sont distincts et doivent être tenus par des outils distincts.
- **« Open-source projects approved by Wolfram » existe.** Même les éditeurs fermés prévoient par
 fois une brèche pour l'open source : la demander est une action concrète, pas une hypothèse.
- **Un `NOASSERTION` est un signal d'arrêt, pas un détail.** CoCalc illustre la règle déjà
  appliquée à React Bits et GeoGebra : sans licence lisible, pas d'usage.

## 14. Erreurs à éviter

- ❌ Utiliser Wolfram Engine gratuit pour générer les sorties d'un composant en production.
- ❌ Croire qu'un quota d'API gratuit autorise un usage commercial : les 2 000 appels sont
  explicitement **non commerciaux**.
- ❌ Considérer CoCalc comme utilisable avant d'avoir lu sa licence.

## 15. Opportunités de différenciation

Aucune sur le terrain du composant : ces deux plateformes n'y sont pas. En revanche, elles
**balisent le rôle de validation** que le cahier des charges impose à Mathemirum
(hypothèses, validation, tests par composant). Savoir qu'un résultat est juste parce qu'on l'a
comparé à une référence est une discipline que ni React Bits ni Aceternity ne pratiquent — et que
Wolfram rend possible, à condition de rester du côté de la référence.

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| Mathematica : licence propriétaire | fiche Wikipédia | 2026-10-19 |
| API : 2 000 appels non commerciaux/mois ; 25–50 $/1 000 requêtes | `products.wolframalpha.com/api` et `/api/pricing` (pages publiques) | 2026-10-19 |
| Wolfram\|Alpha gratuit pour usage personnel non commercial | `wolframalpha.com/faqs` (page publique) | 2026-10-19 |
| Wolfram Engine : usages autorisés et interdits, projets open source soumis à approbation | `wolfram.com/legal/terms/wolfram-engine.html` (page publique) | 2026-10-19 |
| CoCalc : `NOASSERTION`, 1 288 ★, TypeScript, mention de déplacement vers `cocalc-ai` | `GET /repos/sagemathinc/cocalc` | 2026-10-19 |

**Limites :** lectures de pages publiques. **Aucune vérification juridique.** Le fichier de licence
de CoCalc n'a pas été lu ; la procédure d'approbation Wolfram n'a pas été consultée.
