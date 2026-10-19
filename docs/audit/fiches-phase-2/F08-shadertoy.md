# F08 — SHADERTOY

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** pages publiques des conditions, recherche web
**Motif de cette fiche :** c'est **la** référence de fait en matière de shaders visuels — et son
régime par défaut est **non commercial et à partage à l'identique**. C'est le constat le plus
contraignant de cette phase pour un projet de composants visuels.

---

## 1. Présentation et positionnement

Plateforme communautaire d'écriture, de partage et d'exécution de shaders WebGL dans le
navigateur. Elle constitue, dans les faits, la plus grande bibliothèque publique d'effets visuels
temps réel — et la source d'inspiration première de la plupart des « backgrounds animés » que l'on
voit sur le web.

## 2. Fonctionnalités

- Éditeur de shaders en ligne, exécution WebGL immédiate.
- Catalogue public interrogeable.
- **API publique** : recherche et téléchargement des shaders marqués publics par leurs auteurs.
- Chaque auteur choisit la licence de ses shaders.

## 3. Parcours utilisateur

Navigation et exécution dans le navigateur, ou récupération par l'API. Le code est affiché en
lecture — c'est une plateforme d'apprentissage autant qu'une bibliothèque.

## 4. Architecture technique observable

⚠️ **Non observable.** Shadertoy est un service fermé : pas de dépôt public de la plateforme.
Plusieurs projets tiers s'y connectent (serveurs MCP, convertisseurs, lecteurs), sous des licences
variées (MIT, Apache-2.0, BSD-2-Clause) — **mais aucun n'est la plateforme**.

## 5. Mode de distribution

Service en ligne, avec une API ouverte. L'API elle-même est décrite comme « free and open », sous
réserve du respect des conditions d'utilisation **et de la licence de chaque shader**.

## 6. Prévisualisation et personnalisation

Exécution en direct dans le navigateur — la forme de prévisualisation la plus directe de toutes
les plateformes étudiées. Aucun système de paramètres exportables : la personnalisation passe par
l'édition du code.

## 7. Stratégie documentaire

Page d'aide, conditions, FAQ. La documentation des shaders eux-mêmes incombe aux auteurs.
⚠️ Le contenu n'a pas été évalué en détail.

## 8. Modèle de contribution

Chaque auteur dépose ses shaders et **choisit leur licence**. C'est le point décisif : il n'existe
pas une licence Shadertoy, mais **autant de licences que de shaders**.

## 9. ⚠️ Licences et contraintes de réutilisation — le point central

**La licence par défaut est CC BY-NC-SA 3.0 — et la plupart des shaders ne la changent pas.**

Extrait des conditions officielles :

> « All the shaders you create in Shadertoy are **owned by you**. You decide which license applies
> to every shader you create. We recommend you paste your preferred license on top of your code, if
> you don't place a license on a shader, it will be protected by our **default license**:
> Creative Commons Attribution-**NonCommercial**-**ShareAlike** 3.0 Unported License. »

> « On top of any license you might want to apply to your shaders, you agree to give Shadertoy a
> worldwide license to host, store, reproduce, modify, create derivative works, communicate,
> publish, publicly perform, publicly display such content, for the limited purpose of operating,
> promoting, and improving Shadertoy. »

**Ce que cela implique, concrètement :**

| | Verdict |
|---|---|
| Un shader **sans licence explicite** dans son code | ⚠️ **CC BY-NC-SA 3.0** par défaut |
| Usage **commercial** d'un tel shader | ❌ **interdit** (clause NonCommercial) |
| Intégration dans un projet **open source permissif** | ❌ **incompatible** (clause ShareAlike, virale) |
| Usage d'un shader portant **MIT ou CC0** en en-tête | ✅ autorisé, aux conditions de l'auteur |
| Usage de l'**API** pour télécharger | ✅ ouvert, mais **la licence de chaque shader s'applique** |

**Deux témoignages convergents de praticiens** confirment que la majorité des shaders ne
déclarent rien et tombent donc sous le régime par défaut. Un avertissement explicite figure dans
un projet tiers d'intégration : « YOU CANNOT USE A SHADER COMMERCIALLY WITHOUT PERMISSION FROM THE
AUTHOR ». Un autre projet, qui convertit des shaders vers un format tiers, indique **n'intégrer que
des shaders dont la licence autorise la distribution non commerciale**.

**Conséquence pour Mathemirum — c'est la plus sérieuse de cette phase :**
Un composant visuel « inspiré de Shadertoy » est, par défaut, **non commercial et viral**. Pour une
bibliothèque open source dont l'ambition est d'être utilisée dans des produits, **la vérification
doit se faire shader par shader, et l'absence de mention d'en-tête vaut interdiction**.

**Échappatoire identifiée :** la plateforme **Shaders** (`shaders.com`) déclare explicitement que
« the Shaders engine and components themselves are **open source under the MIT License** and do not
require an account at all », avec export de code pour plusieurs frameworks, gratuit pour un usage
personnel **et commercial**. ⚠️ **Cette plateforme n'a pas encore été étudiée en détail** — elle
devient une candidate prioritaire pour la suite de la collecte.

## 10. Points forts

- Le corpus de référence mondial en effets visuels temps réel.
- Exécution immédiate dans le navigateur : la meilleure prévisualisation du secteur.
- Une API publique ouverte.
- Une valeur pédagogique considérable — le code est lisible par tous.

## 11. Limites

- ⚠️ **Licence par défaut non commerciale et virale**, appliquée à la majorité du corpus.
- ⚠️ **Vérification obligatoire shader par shader** : l'absence d'en-tête ne vaut pas autorisation,
  elle vaut interdiction.
- Aucun système de paramètres exportables.
- Service fermé : pas de garantie de pérennité du catalogue.

## 12. Éléments non vérifiés ⚠️

- La proportion réelle de shaders déclarant une licence ouverte (MIT, CC0).
- Les conditions de l'API en détail (limites de débit, attribution).
- Le contenu de la documentation d'aide.
- La plateforme `shaders.com` : licence réelle, qualité du catalogue, périmètre de l'« open source
  sous MIT » annoncé.

## 13. Idées à retenir

- **L'absence de licence n'est pas une autorisation.** La leçon dépasse Shadertoy : sur toute
  plateforme contributive, le silence vaut restriction.
- **Le « bon défaut » est une décision de conception.** Shadertoy a choisi un défaut restrictif ;
  une plateforme qui veut alimenter l'écosystème ouvert choisirait CC0 ou MIT par défaut.
- **Un corpus immense peut être juridiquement inutilisable.** C'est l'argument le plus fort en
  faveur d'une production propre, même modeste.

## 14. Erreurs à éviter

- ❌ Copier un shader « puisque le code est affiché » : l'affichage n'est pas une licence.
- ❌ Supposer qu'un usage open source échappe à la clause NonCommercial : **un usage commercial
  est un usage commercial**, même si le produit qui en résulte est librement distribué.
- ❌ Sous-estimer ShareAlike : intégrer un shader CC BY-NC-SA contamine l'œuvre dérivée.

## 15. Opportunités de différenciation

Deux directions, et la seconde est inattendue :

1. **Produire des shaders sous licence ouverte, documentés.** Le corpus public est immense mais
   majoritairement fermé ; un corpus restreint, explicitement licencié et accompagné de son
   explication mathématique, répond à un besoin non couvert.
2. **Choisir le bon défaut.** Si Mathemirum publie un registre, la licence par défaut des
   contributions est une décision fondatrice. L'exemple de Shadertoy montre qu'un mauvais défaut
   stérilise un catalogue entier.

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| Licence par défaut CC BY-NC-SA 3.0, propriété par l'auteur, licence mondiale accordée à Shadertoy | `shadertoy.com/terms` (page publique) | 2026-10-19 |
| API « free and open », obligation de respecter la licence de chaque shader | `shadertoy.com/howto` (page publique) | 2026-10-19 |
| Constat que la plupart des shaders ne déclarent rien ; avertissements d'intégrateurs | dépôts tiers et forums (MIT, Apache-2.0, BSD-2-Clause) | 2026-10-19 |
| `shaders.com` : moteur et composants sous MIT, usage commercial gratuit | `shaders.com/terms` (page publique) | 2026-10-19 |

**Limites :** lectures de pages publiques. **Aucune vérification juridique.** Aucun shader
particulier inspecté. La plateforme `shaders.com` n'a pas été étudiée au-delà de sa page de
conditions.
