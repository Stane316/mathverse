# F06 — DESMOS

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** pages publiques des conditions d'utilisation, recherche web
**Motif de cette fiche :** c'est la plateforme de calcul mathématique **la plus facilement
intégrable** — et son régime gratuit exclut explicitement l'usage commercial en production.

---

## 1. Présentation et positionnement

Calculatrice graphique en ligne, devenue une référence de fait dans l'enseignement. Desmos Studio
propose les outils grand public (calculatrice, calculatrice 3D) et une **API d'intégration**
destinée aux organisations qui veulent embarquer les outils dans leur propre produit.

## 2. Fonctionnalités

- Calculatrice graphique (fonctions, tableaux, régressions, curseurs).
- Calculatrice 3D.
- **API d'intégration** : incorporation des outils dans une application tierce, avec clé d'API.
- Outils pour l'enseignement (activités de classe).

## 3. Parcours utilisateur

Deux parcours distincts :
- **Utilisateur final** : ouvre la calculatrice dans le navigateur, gratuitement.
- **Intégrateur** : crée un compte, obtient une clé depuis `desmos.com/my-api`, choisit une
  formule, intègre l'API dans son application.

## 4. Architecture technique observable

⚠️ **Non observable.** Desmos est un service fermé : pas de dépôt public, pas de code source
accessible. Un dépôt d'exemple existe (`desmosinc/desmos-sample-cms`, sous MIT) — une application
de démonstration montrant comment utiliser l'API pour créer un système de gestion de contenu.
**Ce dépôt est un exemple d'intégration, pas le moteur.**

## 5. Mode de distribution

Service en ligne propriétaire, avec deux paliers d'API :

| Palier | Conditions |
|---|---|
| **Trial** (gratuit) | usage **personnel non commercial** uniquement, **ou** essai interne de **90 jours** en vue d'un usage commercial |
| **Commercial** (payant) | requis dès qu'une application en production est accessible aux utilisateurs finaux |

## 6. Prévisualisation et personnalisation

Personnalisation par l'API (paramètres de l'application incorporée). Aucune prévisualisation de
composants au sens des bibliothèques étudiées par ailleurs : Desmos n'est pas une bibliothèque.

## 7. Stratégie documentaire

Documentation d'API publique, guides d'intégration, aide en ligne. ⚠️ Le contenu n'a pas été évalué
en détail.

## 8. Modèle de contribution

⚠️ **Sans objet.** Service fermé, pas de contribution externe au moteur.

## 9. ⚠️ Licences et contraintes de réutilisation — le point central

**Deux jeux de conditions, et ils sont restrictifs.**

**API Terms of Service :**
- L'usage gratuit est limité à l'usage personnel non commercial, ou à un essai de 90 jours.
- « Commercial use includes any use of the API in an Application that is accessed by End Users in
  production, **or any internal use of the API for a business purpose**. »
- La licence accordée est « non-exclusive, **revocable**, non-transferable, non-sublicensable ».

**Conditions générales des outils :**
- Usage personnel non commercial, ou usage scolaire par une école en classe.
- « **You may not frame or mirror the Desmos Tools without our prior consent.** »
- **Clause sur les contenus déposés** : l'utilisateur accorde à Desmos une licence
  « **irrevocable, perpetual**, non-exclusive, fully-paid, worldwide license, **with the right to
  sublicense through multiple tiers** », pour utiliser, distribuer, reproduire, modifier, adapter,
  publier et afficher ses soumissions — sans compensation ni notification.

**Conséquence pour Mathemirum :**

| | Verdict |
|---|---|
| Intégrer l'API Desmos dans une bibliothèque open source distribuée | ❌ **palier commercial requis** dès qu'un utilisateur final y accède |
| Encadrer ou mettre en miroir les outils | ❌ **interdit sans accord écrit préalable** |
| Étudier le comportement et réimplémenter les courbes | ⚠️ non tranché — question de fait, pas de licence |
| Déposer des contenus sur la plateforme puis les reprendre | ⚠️ **à éviter** : la licence accordée à Desmos est perpétuelle et irrévocable |

**La clause d'encadrement est la plus contraignante à court terme.** Un composant web qui
afficherait Desmos dans une iframe relèverait de l'encadrement — interdit sans accord.

## 10. Points forts

- La meilleure ergonomie du secteur sur le tracé de courbes : la référence que tout le monde connaît.
- Une API d'intégration réelle, documentée, avec gestion de clé en libre-service.
- Un palier gratuit suffisant pour l'expérimentation et l'enseignement.

## 11. Limites

- ⚠️ **Service fermé et révocable** : une dépendance à Desmos est une dépendance à un tiers qui peut
  révoquer l'accès.
- ⚠️ **Aucune sortie de code** : on intègre un service, pas un composant. Rien à versionner, rien à
  tester localement, rien à distribuer.
- L'usage commercial en production est payant dès le premier utilisateur final.
- La clause sur les contenus déposés est très large.

## 12. Éléments non vérifiés ⚠️

- Les tarifs du palier commercial.
- Les limites d'usage techniques du palier Trial (hors limite de 90 jours).
- Le contenu réel de la documentation d'API.
- La politique de conservation des données et l'absence de dépendance réseau en mode hors ligne.
- La position de Desmos sur l'intégration par iframe dans un produit open source.

## 13. Idées à retenir

- **Une dépendance révocable n'est pas une fondation.** « Revocable » figure explicitement dans la
  licence : un projet qui bâtit dessus n'a aucune garantie de continuité.
- **Encadrer un service tiers est juridiquement distinct de l'intégrer.** Cette distinction
  technique (iframe contre API) a une conséquence légale directe.
- **La clause sur les contenus déposés est un avertissement général** : déposer son travail sur une
  plateforme peut transférer des droits perpétuels. Vaut pour Desmos, vaut pour d'autres.

## 14. Erreurs à éviter

- ❌ Compter sur le palier gratuit pour un projet destiné au public : la définition du commercial
  inclut tout usage en production, même gratuit.
- ❌ Encadrer la calculatrice dans une iframe « puisque l'API existe » : l'encadrement est un acte
  juridique distinct, soumis à consentement préalable.
- ❌ Déposer sur la plateforme des matériaux que Mathemirum voudrait réutiliser ailleurs.

## 15. Opportunités de différenciation

Desmos démontre la demande pour le tracé mathématique interactif. Mais son modèle est **un service
incorporé, pas un composant possédé**. Deux différences de nature, exploitables :

1. **La propriété.** Un composant Mathemirum s'installe, se versionne, se teste, fonctionne hors
   ligne. Un service incorporé se loue et se révoque.
2. **L'explicabilité.** Desmos trace la courbe ; il n'expose ni la méthode, ni les hypothèses, ni le
   domaine de validité. C'est précisément la ligne de partage du cahier des charges entre
   « visualisation » et « simulation validée ».

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| Paliers Trial / Commercial, limite de 90 jours, licence révocable | `desmos.com/api-terms` (page publique) | 2026-10-19 |
| Usage non commercial, interdiction d'encadrer, clause sur les contenus | `desmos.com/terms` §5 et §6 (pages publiques) | 2026-10-19 |
| Formules API, clé en libre-service | `help.desmos.com` (page publique) | 2026-10-19 |
| `desmosinc/desmos-sample-cms` sous MIT — exemple d'intégration | fiche du dépôt, recherche web | 2026-10-19 |

**Limite :** lecture des pages publiques de conditions, non des contrats commerciaux. Aucune
vérification juridique. Le service n'a pas été testé.
