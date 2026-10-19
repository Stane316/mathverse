# DÉCISION 0002 — LICENCE DU CORPUS SOURCE

**Date :** 2026-10-19
**Statut :** ⚠️ **PROPOSITION SOUMISE — en attente de votre décision.** Rien n'a été appliqué.
**Objet :** clarifier le régime juridique de `Stane316/my-own-connaissance`, le corpus d'où
proviennent les équations et les explications mathématiques de Mathemirum.

---

## 1. L'état constaté

Vérifié le 2026-10-19 par l'API publique GitHub :

| Champ | Valeur |
|---|---|
| Dépôt | `Stane316/my-own-connaissance` |
| **Licence** | **AUCUNE** |
| Fichiers `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` | **tous absents (404)** |
| README | **absent** |
| Description, page d'accueil, étiquettes | **vides** |
| Visibilité | **public** |
| Étoiles / forks | 0 / 0 |
| Créé le | **2026-10-17** |
| Contenu | deux répertoires : `Ai Technical Litteracy`, `Maths-vers-Informatiques` |

**Ce que cela signifie juridiquement :** un dépôt public **sans licence** est soumis au droit
d'auteur par défaut — **tous droits réservés**. Le contenu est *visible*, il n'est pas
*réutilisable*. Personne ne peut légalement le copier, le modifier ou le redistribuer.

## 2. Pourquoi c'est bloquant — et pourquoi maintenant

C'est le **même défaut que j'ai critiqué chez les autres**, et c'est ce qui rend la situation
urgente à traiter :

- **GeoGebra** publie son moteur sur GitHub sans y déclarer de licence — noté dans la fiche F07
  comme « le contre-modèle de ce que Mathemirum doit faire ».
- **`sadeepas`** (MathVerse) n'a aucune licence — noté dans la fiche F10 comme « tous droits
  réservés », avec l'avertissement que la réutilisation en devient illicite par défaut.
- **Le corpus source de Mathemirum est dans le même cas.**

La conséquence concrète : **un composant Mathemirum accompagné d'une équation tirée du corpus
reposerait sur une base juridique non établie.** Le projet se présenterait comme rigoureux sur les
licences des autres tout en ayant la sienne en suspens. C'est le point que la synthèse des
différenciateurs (D5) a identifié comme une action requise.

## 3. Deux précisions utiles avant de choisir

### 3.1 Ce que le droit d'auteur couvre — et ce qu'il ne couvre pas

- ❌ **Les faits mathématiques ne sont pas protégeables.** Une équation, un théorème, une valeur
  numérique : personne n'en est propriétaire.
- ✅ **L'expression l'est** : la structure des documents, la prose, le choix et l'agencement des
  notions, la formulation des explications.

**Conséquence :** la licence du corpus porte sur la **forme rédigée**, pas sur les mathématiques
elles-mêmes. Mathemirum reste libre d'utiliser n'importe quelle équation. Ce qui est en cause,
c'est la **réutilisation du texte et de la structure**.

### 3.2 Le corpus est votre œuvre — vous pouvez donc le licencier

Le dépôt a été créé le 2026-10-17, il n'a aucun fork, et il n'y a aucune trace d'apport externe.
⚠️ **Une réserve tout de même :** je n'ai pas vérifié que les 29 documents ne contiennent pas des
passages repris d'ailleurs. **Si c'est le cas, ces passages conservent le régime de leur source**, et
la licence que vous choisirez ne les couvrira pas. Ce point n'a pas été instruit.

## 4. Les options, et ce qu'elles impliquent

Le corpus est du **contenu**, pas du code : la famille Creative Commons est donc l'outil adapté.

| Option | Commercial | Attribution | Viralité | Verdict |
|---|:--:|:--:|:--:|---|
| **CC BY 4.0** | ✅ | requis | ❌ | ⭐ **recommandée** |
| **CC0 1.0** | ✅ | non requis | ❌ | ✅ alternative, si l'attribution vous importe peu |
| **CC BY-SA 4.0** | ✅ | requis | ✅ **oui** | ⚠️ **à éviter** — voir ci-dessous |
| **CC BY-NC 4.0** | ❌ | requis | ❌ | ❌ **exclue** — incompatible avec le « libre d'abord » |
| **CC BY-ND 4.0** | ✅ | requis | ❌ (mais pas de modification) | ❌ **exclue** — interdirait les dérivés, donc Mathemirum |
| **Aucune licence** | ❌ | — | — | ❌ **statu quo** : le problème subsiste |

### Pourquoi CC BY-SA est à éviter ici

Le partage à l'identique s'applique aux **« Adapted Material »** — c'est-à-dire aux œuvres dérivées.
Or l'explication mathématique d'un composant Mathemirum **serait** un matériau adapté du corpus.
⚠️ **La question de savoir jusqu'où s'étend cette contagion est juridiquement débattue** et dépend de
la façon dont le texte est repris. **Ne pas prendre ce risque sans nécessité** : CC BY 4.0 offre la
même ouverture commerciale sans la viralité.

### Pourquoi pas CC0

CC0 est parfaitement valable et encore plus ouvert. Elle présente un inconvénient : **elle dispense
d'attribution**, ce qui permet à quiconque de reprendre le corpus sans jamais citer Mathemirum. Si
le corpus est un actif de notoriété, CC BY 4.0 est préférable. Si vous voulez le maximum de liberté
de réutilisation, CC0 est le choix.

## 5. Recommandation

### 5.1 Licence du corpus : **CC BY 4.0**

**Motif :** elle autorise l'usage commercial (indispensable pour un projet « libre d'abord »),
n'impose qu'une attribution (facile à satisfaire), et **n'a aucune viralité** — ce qui laisse
Mathemirum libre de choisir sa propre licence pour le code des composants.

**Attribution à reproduire** dans tout document dérivé — à placer dans une section « Sources » de
chaque composant :

> Contenu mathématique dérivé de *my-own-connaissance* par Stane316,
> sous licence CC BY 4.0 — https://github.com/Stane316/my-own-connaissance

### 5.2 Ajouter un README au corpus

Le dépôt n'en a aucun. C'est l'occasion d'en écrire un court, qui devrait au minimum indiquer : ce
qu'est le corpus, son état (formalisme partiellement dégradé), le fait qu'il serve de source à
Mathemirum, et le régime de licence. ⚠️ **Le README doit dire que le formalisme est dégradé** —
sinon un tiers croira lire des équations vérifiées alors que 31,4 % des blocs étaient incomplets
avant restauration, et que les 773 restaurations sont des **reconstructions argumentées, pas des
originaux retrouvés**.

### 5.3 ⚠️ Point d'attention — les restaurations ne sont pas dans le dépôt

Les 773 restaurations appliquées pendant le chantier **existent uniquement dans les diffs livrés**
(`docs/restauration/livrables/*.gitdiff`), que vous appliquez localement. **Le dépôt public contient
donc la version non restaurée.** Si vous appliquez les diffs puis publiez sous CC BY 4.0, les
restaurations seront couvertes. Si vous ne les appliquez pas, elles ne le seront pas — et elles ne
seront sous aucun régime.

## 6. Ce que je ne peux pas faire

⚠️ **Je ne peux pas appliquer cette décision moi-même.** Pousser vers `my-own-connaissance` a été
refusé (`403`), comme documenté depuis le début du chantier. **Aucune tentative de contournement
n'a été faite et ne sera faite.**

Les fichiers sont donc **préparés** ci-dessous ; c'est vous qui les déposez.

## 7. Comment l'appliquer — sans recopier de texte juridique

⚠️ **Je n'ai pas reproduit le texte intégral de la licence, volontairement.** Un texte juridique
recopié de mémoire risque d'être inexact, et une licence inexacte est pire qu'une licence absente.

**Deux méthodes sûres :**

1. **Par l'interface GitHub** — sur la page du dépôt, « Add file » → « Create new file » → nommer le
   fichier `LICENSE` → un bouton « Choose a license template » apparaît → sélectionner
   **Creative Commons Attribution 4.0**. GitHub insère le texte canonique et renseigne le champ
   licence du dépôt.
2. **Par téléchargement** — récupérer le texte depuis `creativecommons.org/licenses/by/4.0/` et le
   déposer tel quel.

Une fois le fichier ajouté, l'API GitHub remontera `cc-by-4.0` au lieu de « aucune ».

## 8. Références

- `../audit/A9-registre-des-licences.md` — les trois mécanismes trompeurs ; le statut de base
- `../audit/annexes/A9-synthese-differenciateurs.md` §5.1 — l'action requise d'où vient ce document
- `../audit/fiches-phase-2/F07-geogebra.md` — le contre-modèle (code public, licence non déclarée)
- `../audit/fiches-phase-2/F10-sadeepas-mathverse.md` — l'absence de licence, et ses effets
- `../restauration/CLOTURE-CHANTIER.md` — l'état des restaurations et leur mode de livraison
- `../audit/A7-integrite-des-equations.md` — le taux de dégradation (31,4 %)
