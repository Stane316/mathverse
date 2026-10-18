# LOT 2 bis — DOMAINE L : 10 BLOCS À TRANCHER

**Date :** 2026-10-18 — **Statut :** **candidats soumis à votre arbitrage** — non appliqués
**Numéros de ligne :** valides **après** application du lot 2 (`domaine-L.gitdiff`)
**Rappel :** ces blocs étaient vides. Leur contenu n'existe plus nulle part ; ce qui suit est
une **proposition argumentée**, pas une restitution.

---

## 1. Ce que la recherche croisée a appris

Avant de vous soumettre ces candidats, j'ai cherché dans les autres documents les **sections
homologues** — elles y sont parfois intactes, et leur forme éclaire ce qui manque ici.

| Section | Ce que montrent les autres documents |
|---|---|
| « FORMULE MENTALE » | Dans **N** : une chaîne de phrases courtes (« Transformer pour voir. / Voir pour comprendre. / Comprendre pour simplifier. / Simplifier pour calculer. / Calculer pour construire. »). Dans **P** et **Q** : un arbre ASCII. Donc : **ni l'un ni l'autre n'est une équation**. |
| « SYNTHÈSE FINALE » | Dans **I** : « Son idée fondamentale est : `\[ \]` » — **le même bloc vide**, même structure qu'en L. La dégradation est systématique sur ce type de section. |
| Blocs « objet → objet » | Dans **I**, section 180 : « À une variable : `\[ f(x) f’(x) \]`, Pour la courbure : `\[ f(x) H_f(x) \]` ». La flèche a été supprimée, laissant deux termes voisins. **Cela confirme** la restauration de la ligne 2221 en `(x_i,y_i) → f(x)`. |
| « Principe directeur » | Dans **R**, **S** et **U** : c'est un **paragraphe de prose**, sans bloc mathématique. Le bloc vide de la ligne 61 est donc une entorse à l'habitude de l'auteur — ce qui rend sa reconstruction plus incertaine. |

Conclusion : dans ce document, les blocs vides des sections de synthèse contenaient
majoritairement des **chaînes de mots** ou des **énoncés**, pas des formules. C'est pourquoi
ces 44 blocs ne peuvent pas être devinés : ils relèvent de votre formulation.

## 2. Les dix blocs les plus structurants

Chaque ligne propose un **candidat recommandé** et une **alternative**. Un mot de vous suffit :
« candidat 1 », « candidat 2 », ou votre propre texte.

| Ligne | Contexte | Candidat 1 (recommandé) | Candidat 2 (alternative) |
|---:|---|---|---|
| **61** | « ### Principe directeur » | `\[ \text{un résultat n'a de sens qu'avec son erreur} \]` | `\[ \text{exactitude} \neq \text{précision} \]` |
| **115** | « On peut représenter la chaîne : » (suivi de la liste A → L) | `\[ A\to B\to C\to \cdots \to L \]` | la liste des domaines en toutes lettres |
| **343** | « Ces trois notions sont différentes. » (stabilité, conditionnement, convergence) | `\[ \text{stabilité} \neq \text{conditionnement} \neq \text{convergence} \]` | `\[ \text{erreur directe} \leq \text{conditionnement} \times \text{erreur rétrograde} \]` |
| **1597** | « Un solveur sérieux peut être structuré ainsi : » | `\[ \text{modèle} \to \text{discrétisation} \to \text{solveur} \to \text{validation} \]` | `\[ \text{entrée} \to \text{préconditionnement} \to \text{itération} \to \text{critère d'arrêt} \to \text{sortie} \]` |
| **2184** | « le développeur doit conserver la capacité de vérifier : » | `\[ \text{la validité du résultat} \]` | `\[ \text{le résidu et la convergence} \]` |
| **2301** | « Le domaine L enseigne une idée fondamentale : » | `\[ \text{un calcul juste peut produire un résultat faux} \]` | `\[ \text{entre la formule et le résultat, il y a la machine} \]` |
| **2305** | « Entre le modèle et le résultat existe toute une chaîne : » | `\[ \text{modèle} \to \text{discrétisation} \to \text{algorithme} \to \text{flottant} \to \text{résultat} \]` | `\[ \text{modèle} \to \text{erreur de troncature} \to \text{erreur d'arrondi} \to \text{erreur totale} \]` |
| **2333** | « Pour tout problème numérique : » (§120, formule mentale) | `\[ \text{erreur} = \text{conditionnement} \times \text{stabilité} \]` | une chaîne de phrases comme dans le document N : « Poser le problème. / Choisir la discrétisation. / Mesurer l'erreur. / Valider. » |
| **2337** | « lorsqu'une IA doit transformer un concept mathématique en logiciel : » | `\[ \text{concept} \to \text{modèle} \to \text{algorithme} \to \text{implémentation} \to \text{tests} \]` | `\[ \text{concept} \to \text{équation} \to \text{code} \to \text{vérification} \]` |
| **2343** | « Il permet de passer de : » … « à : » | de `\[ \text{formule mathématique} \]` | de `\[ \text{modèle} \]` |

Le pendant de la ligne 2343 est la ligne **2347** (« à : »), dont le bloc est `\[ . \]` :
`\[ \text{système exploitable}. \]`, ou `\[ \text{résultat fiable}. \]`. La phrase qui précède
(« C'est cette seconde question qui transforme une formule mathématique en système informatique
exploitable ») donne presque mot pour mot les deux termes.

## 3. Note sur la notation

Le document L n'emploie jamais `\text{…}` : tous ses blocs affichés contiennent des symboles.
Pour les chaînes de mots proposées ci-dessus, `\text{…}` est la seule façon correcte de les
écrire en LaTeX. Si vous préférez rester dans l'esprit du document, la version **sans** bloc
mathématique (chaîne en Markdown, avec des flèches `→`) est tout aussi défendable — et c'est
d'ailleurs ce que font les documents P et Q pour leurs arbres. Dites-moi votre préférence, elle
s'appliquera aux 44 blocs.

## 4. Les 34 autres blocs

Les blocs restants sont listés dans `domaine-L.md`, §4, table « Confiance inconnue ». La plupart
sont des termes isolés (lignes 13, 17, 55, 146, 154, 158, 202, 875, 1017, 1148, 1281, 1285, 1364,
1870, 1874, 1878, 2106, 2201, 2205, 2241, 2282, 2302…) ou des énoncés de synthèse (1193, 1197,
1770, 1812-1860, 2191…). Je peux vous soumettre des candidats pour ceux-là aussi, par groupes de
dix, quand vous voulez.
