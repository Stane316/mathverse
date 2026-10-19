# A9 — COMPARAISON TRANSVERSALE

**Livrable 3 de la phase 2**
**Date d'établissement :** 2026-10-19
**Objet :** croiser les attributs exigés par le cahier des charges avec les plateformes étudiées,
pour établir **qui couvre quoi** et **où se situent les cases vides**.
**Portée :** 18 attributs × 27 plateformes retenues.

---

## 1. Méthode

### 1.1 Les 18 attributs de référence

Le cahier des charges exige, **pour chaque composant** livré : nom, description, catégorie, aperçu
en direct, paramètres réglables, code source, commande CLI, prompt IA réutilisable (13 champs),
explication mathématique, équations et hypothèses, dépendances, installation, configuration
exportable, tests, mesures de performance, licence et attribution, limites connues, exemples
d'intégration.

Ces 18 attributs sont la grille de lecture. Trois d'entre eux sont regroupés ci-dessous sous
l'étiquette **« couche probatoire »** — explication mathématique, équations et hypothèses, et
limites connues — parce qu'ils partagent une fonction : ils disent **pourquoi** ça marche, **sous
quelles conditions**, et **jusqu'où**. C'est la ligne de partage du cahier des charges entre effet
artistique, visualisation explicable et simulation validée.

### 1.2 Notation

| Marque | Signification |
|---|---|
| ✅ | présent et vérifié |
| ⚠️ | présent mais **partiel**, **indirect**, ou **non vérifié** |
| ❌ | absent |
| **?** | **non évalué** — la case n'a pas pu être renseignée |

⚠️ **Les cases `?` sont nombreuses et c'est assumé.** Renseigner une case par inférence violerait
la règle de preuve de A6 §5. Une case `?` signifie « nous ne savons pas », pas « probablement non ».

### 1.3 Périmètre

27 plateformes, retenues parce qu'elles sont observables ou documentées. Sont exclues de la
matrice : les plateformes purement de service sans sortie de code (Desmos, GeoGebra, Wolfram,
CoCalc), traitées au §5, et les projets sans traction ni licence (MathVerse/sadeepas).

---

## 2. La question des quatre attributs — le cœur de la phase 2

Le §1 de A9 pose la question : *existe-t-il une plateforme réunissant **composants visuels +
explication mathématique + prompts + CLI** ?*

| Plateforme | Composants visuels | Explication maths | Prompts | CLI |
|---|:--:|:--:|:--:|:--:|
| React Bits | ✅ | ❌ | ? | ✅ |
| shadcn/ui | ✅ | ❌ | ⚠️ | ✅ |
| Aceternity UI | ✅ | ❌ | ✅ | ⚠️ |
| Shaders | ✅ | ❌ | ✅ | ✅ |
| Uiverse | ✅ | ❌ | ❌ | ❌ |
| Magic UI | ✅ | ❌ | ? | ⚠️ |
| Math-To-Manim | ❌ | ⚠️ | ✅ | ✅ |
| Manim | ❌ | ⚠️ | ❌ | ✅ |
| three.js | ⚠️ | ❌ | ❌ | ❌ |
| p5.js | ⚠️ | ❌ | ❌ | ❌ |
| JSXGraph | ⚠️ | ⚠️ | ❌ | ❌ |
| ExcaliMath | ⚠️ | ⚠️ | ❌ | ❌ |

**Aucune plateforme ne réunit les quatre.** Deux s'en approchent par des chemins opposés :

- **Shaders** a les composants, les prompts et la CLI — **il lui manque l'explication
  mathématique**, et c'est le seul manque.
- **Math-To-Manim** a l'explication, les prompts et la CLI — **il lui manque la sortie composant**,
  puisqu'il produit une vidéo.

**Ce n'est pas une coïncidence, et c'est le résultat central de cette phase :** les deux acteurs
les plus proches de la thèse sont **complémentaires**, et leur complémentaire **est** la thèse de
Mathemirum.

⚠️ **Ce constat ne vaut pas preuve d'absence.** Il repose sur 27 plateformes observables et une
requête de recherche. Une plateforme non observée pourrait réunir les quatre.

---

## 3. Matrice — les 18 attributs

### 3.1 Famille A — bibliothèques de composants web

| Attribut | React Bits | shadcn/ui | Aceternity | Shaders | Uiverse | Magic UI |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| 1. Nom | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2. Description | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| 3. Catégorie | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 4. Aperçu en direct | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5. Paramètres réglables | ✅ | ⚠️ | ⚠️ | **✅** | ❌ | ⚠️ |
| 6. Code source | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ |
| 7. Commande CLI | ✅ | ✅ | ⚠️ | ✅ | ❌ | ⚠️ |
| 8. Prompt IA / agent | ? | ⚠️ | ✅ | ✅ | ❌ | ? |
| 9. **Explication maths** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 10. **Équations et hypothèses** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 11. Dépendances déclarées | ✅ | ✅ | ⚠️ | ✅ | ❌ | ⚠️ |
| 12. Installation | ✅ | ✅ | ⚠️ | ✅ | ❌ | ✅ |
| 13. Configuration exportable | ⚠️ | ⚠️ | ? | **✅** | ❌ | ? |
| 14. Tests | ? | ✅ | ❌ | ? | ❌ | ? |
| 15. **Mesures de performance** | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ |
| 16. Licence et attribution | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| 17. **Limites connues** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 18. Exemples d'intégration | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Lecture :** la couche « distribution » (attributs 1-7, 11-13, 18) est **largement couverte**, et
même très aboutie chez Shaders. La couche « probatoire » (9, 10, 15, 17) est **vide partout**, sans
une seule exception.

### 3.2 Famille B — moteurs et bibliothèques mathématiques

| Attribut | three.js | p5.js | Manim | MathBox | JSXGraph | CindyJS | D3 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 4. Aperçu en direct | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| 5. Paramètres réglables | ⚠️ | ⚠️ | ❌ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| 6. Code source | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7. Commande CLI | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| 8. Prompt IA | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 9. **Explication maths** | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| 10. **Équations et hypothèses** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 11. Dépendances | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 14. Tests | ✅ | ✅ | ✅ | ? | ✅ | ? | ✅ |
| 15. **Mesures de performance** | ⚠️ | ? | ? | ? | ? | ? | ? |
| 16. Licence | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| 17. **Limites connues** | ? | ? | ? | ? | ? | ? | ? |

**Lecture :** ces projets sont **mathématiquement profonds** mais ils sont des **moteurs**, pas des
catalogues. Ils n'ont ni composant, ni prompt, ni CLI d'installation. Leur documentation explique
l'*outil*, jamais le *composant*. Les attributs 9 et 10 sont marqués ⚠️ et non ✅ : la documentation
décrit des concepts mathématiques, mais **aucun n'expose, par effet, ses équations et ses
hypothèses**.

⚠️ **Les cases 15 et 17 sont majoritairement `?`** : la présence de benchmarks et de limites
documentées n'a pas été vérifiée pour ces projets.

### 3.3 Famille C — génération par IA

| Attribut | Math-To-Manim | Manimly | MathViz-E | ExcaliMath | reactive-manim |
|---|:--:|:--:|:--:|:--:|:--:|
| 4. Aperçu en direct | ❌ | ⚠️ | ❌ | ✅ | ❌ |
| 5. Paramètres réglables | ❌ | ⚠️ | ❌ | ⚠️ | ❌ |
| 6. Code source | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7. Commande CLI | **✅** | ? | ? | ❌ | ❌ |
| 8. Prompt IA | **✅** | ✅ | ✅ | ❌ | ❌ |
| 9. **Explication maths** | **⚠️** | ⚠️ | ⚠️ | ❌ | ❌ |
| 10. **Équations et hypothèses** | ⚠️ | ? | ? | ❌ | ❌ |
| 11. Dépendances | ✅ | ✅ | ? | ✅ | ? |
| 14. Tests | ✅ | ? | ? | ? | ? |
| 15. **Mesures de performance** | ? | ? | ? | ? | ? |
| 16. Licence | ✅ | ✅ | ✅ | ✅ | ✅ |
| 17. **Limites connues** | ⚠️ | ? | ? | ? | ? |

**Lecture :** c'est la seule famille où le **prompt** et la **CLI** sont au cœur du produit, et la
seule où une forme d'**explication mathématique** apparaît (le « dossier mathématique » et l'agent
de vérification de Math-To-Manim). Mais la sortie est une vidéo : les attributs de composant
(aperçu paramétrique, installation, intégration) sont absents.

⚠️ Math-To-Manim est marqué ⚠️ et non ✅ sur l'explication mathématique : le pipeline **produit**
un dossier mathématique, mais rien n'indique qu'il soit **exposé à l'utilisateur final** comme
livrable du composant.

---

## 4. Synthèse par attribut — où sont les cases vides

| Attribut | Couverture | Commentaire |
|---|:--:|---|
| 1-4. Nom, description, catégorie, aperçu | 🟢 **large** | acquis du secteur, partout |
| 5. Paramètres réglables | 🟡 **partielle** | aboutie chez Shaders et React Bits ; absente ailleurs |
| 6. Code source | 🟢 **large** | le modèle copier-coller domine |
| 7. Commande CLI | 🟡 **partielle** | shadcn, Shaders, React Bits, Math-To-Manim |
| 8. Prompt IA | 🔴 **rare** | Shaders et Aceternity (MCP) ; shadcn en amorce (`skills/`) |
| **9. Explication maths** | 🔴 **quasi nulle** | ⚠️ chez les moteurs et les générateurs IA, jamais ✅ |
| **10. Équations et hypothèses** | 🔴 **nulle** | ❌ partout, sans exception |
| 11. Dépendances | 🟢 **large** | |
| 12. Installation | 🟢 **large** | |
| 13. Configuration exportable | 🟡 **partielle** | Shaders (éditeur), React Bits (outils) |
| **14. Tests** | 🟡 **inégale** | ✅ chez shadcn et les moteurs matures ; `?` ailleurs |
| **15. Mesures de performance** | 🔴 **quasi nulle** | une seule affirmation non vérifiée (Shaders, 25×) |
| 16. Licence et attribution | 🟡 **ambigüe** | neuf régimes restrictifs — voir le registre des licences |
| **17. Limites connues** | 🔴 **quasi nulle** | la case la plus vide de la matrice |
| 18. Exemples d'intégration | 🟢 **large** | |

**Le motif est net.** Tout ce qui relève de la **mise à disposition** (nom, aperçu, code,
installation, dépendances, exemples) est couvert. Tout ce qui relève de la **preuve** (explication,
équations et hypothèses, mesures, limites connues) est vide.

---

## 5. Les services fermés — hors matrice, et pourquoi

Desmos, GeoGebra, Shadertoy, Wolfram et CoCalc sont profonds mathématiquement, mais **ne livrent
aucun code réutilisable**. Ils sortent donc de la matrice des 18 attributs : il n'existe pas de
« composant » auquel ces attributs pourraient s'appliquer.

| Service | Ce qu'il apporte | Pourquoi il ne compte pas comme composant |
|---|---|---|
| Desmos | tracé de courbes de référence | service incorporé, licence révocable, encadrement interdit |
| GeoGebra | couverture mathématique très large | quatre régimes de licence, co-propriété des productions |
| Shadertoy | le corpus d'effets le plus riche | CC BY-NC-SA par défaut : non commercial et viral |
| Wolfram | la référence de validation | propriétaire, gratuit limité au pré-production |
| CoCalc | environnement de calcul complet | MS-RSL : lecture seule, distribution exclue |

**Leur rôle possible dans Mathemirum est celui de référence**, jamais de dépendance — Wolfram
surtout, dont la fonction de validation est exactement ce que le cahier des charges appelle
« tests » et « mesures de performance ».

---

## 6. Ce que la matrice suggère — hypothèses, non faits

⚠️ **Ce qui suit est une hypothèse.** Elle s'appuie sur 27 plateformes observables, une requête de
recherche, et une matrice dont les cases `?` sont nombreuses.

1. **La place libre n'est pas technique, elle est documentaire.** Les acteurs en place savent
   produire, distribuer et installer des composants. Aucun ne sait — ou ne veut — dire ce que son
   composant **prouve**.
2. **Les deux acteurs les plus proches sont complémentaires**, et leur complémentaire recouvre
   exactement la thèse de Mathemirum : Shaders a la distribution sans la preuve, Math-To-Manim a la
   preuve sans la distribution.
3. ⚠️ **Risque attaché à cette lecture :** une case vide peut être vide **par choix rationnel**.
   Documenter les équations et les limites d'un composant coûte cher et n'attire pas
   nécessairement d'utilisateurs. Que personne ne le fasse peut signifier une opportunité — ou un
   marché qui ne le valorise pas. **Cette question n'est pas instruite et relève de l'étude de
   demande (recommandation R3).**

---

## 7. Limites

- ⚠️ **Les cases `?` ne sont pas des absences.** Elles marquent des attributs non évalués, faute de
  source ou de temps. Elles ne doivent pas être lues comme des ❌.
- ⚠️ **Aucune plateforme n'a été installée ni exécutée** : l'environnement ne dispose ni de GPU ni de
  navigateur. Les affirmations de performance ne sont donc pas vérifiées.
- ⚠️ **La profondeur d'évaluation est inégale** : les plateformes ayant fait l'objet d'une fiche
  (F01 à F11) sont mieux renseignées que celles relevées par métadonnées seules.
- ⚠️ **Aucune preuve d'absence n'est établie.** Le cahier des charges interdit de revendiquer
  l'exhaustivité.

---

## 8. Références

- `A9-plan-phase-2.md` §1 (question posée), §5 (fiche type), §6 (livrables)
- `A9-registre-des-licences.md` — le régime juridique de chaque plateforme
- `annexes/A9-registre-plateformes.md` — les données vérifiées par plateforme
- `../fiches-phase-2/F01` à `F11` — les onze fiches détaillées
- Cahier des charges : les 18 livrables par composant
