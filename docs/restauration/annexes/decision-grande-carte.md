# Décision — la Grande Carte des domaines : deux-points ou pas ?

**Date :** 2026-10-19
**Objet :** la question soulevée le 2026-10-18 à propos du lot J 5c, qui a restauré les dix
blocs de la section 155 du domaine J sous la forme `\[ A \]`, `\[ B \]`, …, `\[ J \]`.
Le domaine H, §143, présente le même motif **avec des deux-points** (`\[ A: \]`). Fallait-il
corriger J ?

**Décision : non. La forme sans deux-points est conservée.**

---

## 1. La recherche

Le motif n'apparaît pas deux fois dans le corpus, mais **quatre**. Toutes les occurrences ont
été relevées par recherche automatique sur les 21 documents mathématiques :

| Document | Section | Blocs | Étendue | Forme | Deux-points |
|---|---|---:|---|---|---|
| G — probabilités | §140 POSITION DU DOMAINE G DANS LA CARTOGRAPHIE GLOBALE | 7 | A…G | `\[ A: \]` | **7/7** |
| H — statistiques | §143 POSITION DU DOMAINE H DANS LA CARTOGRAPHIE GLOBALE | 8 | A…H | `\[ A: \]` | **8/8** |
| I — calcul différentiel | §177 SYNTHÈSE DES DOMAINES PRÉCÉDENTS | 9 | A…I | `\[ A \]` | **0/9** |
| J — optimisation | §155 LA GRANDE CARTE DES DOMAINES | 10 | A…J | détruit | **?** |

Contenu brut vérifié caractère par caractère (`cat -A`) :

- **G et H** : `\[ A: \]` — lettre, deux-points, **espace**. L'espace après le deux-points
  indique qu'une description suivait, détruite avec son argument.
- **I** : `\[ A \]` — lettre seule, **ni deux-points ni espace**.

Les deux formes sont donc réellement distinctes, et non une variante de dégradation.

---

## 2. Le raisonnement

Quatre arguments, du plus fort au plus faible :

1. **I est le voisin immédiat de J** (9ᵉ et 10ᵉ documents) et sa section est le même motif,
   avec une formulation quasi identique : « La progression mathématique construite jusqu'ici
   peut être résumée ainsi » (I) / « La progression construite jusqu'ici peut être comprise
   comme » (J). **Neuf blocs sans deux-points, intacts.**
2. **G et H forment un couple** : même titre de section au mot près
   (« POSITION DU DOMAINE … DANS LA CARTOGRAPHIE GLOBALE »), même forme. I et J portent des
   titres différents. La forme à deux-points est attachée à ce couple, pas à la série
   entière.
3. **J ne porte aucun deux-points sur son seul bloc survivant** : `\[ IJ \]`.
4. La forme à deux-points appartient à deux documents **plus anciens dans la série** (7ᵉ et
   8ᵉ) ; la forme sans, au plus récent avant J (9ᵉ).

---

## 3. Ce que cette décision ne résout pas — à dire clairement

**Un fait reste gênant et n'est pas éludé.**

Dans I, les lettres ont **survécu** (`\[ A \]`). Dans J, les dix blocs étaient
**intégralement vides**, alors que le onzième bloc du même paragraphe, `\[ IJ \]`, a survécu.
Si les blocs de J avaient été de simples lettres comme ceux de I, **elles auraient survécu
elles aussi** — la dégradation n'a pas frappé ce paragraphe uniformément, puisque le bloc
suivant est intact.

L'explication la plus plausible est que **les blocs de J contenaient davantage qu'une lettre** :
un contenu placé dans une commande (`\text{…}`), donc détruit avec son argument — alors que
`IJ` était du texte nu, donc préservé. Dans ce cas, la notation exacte d'origine n'est pas
récupérable.

**Conséquence, assumée :** ce qui est solidement établi, c'est **le nombre et l'ordre** —
dix blocs, A jusqu'à J, le corpus comptant exactement dix documents jusqu'à J, et le onzième
bloc mettant en avant la transition terminale I → J. Ce qui ne l'est pas, c'est la
**notation exacte** : lettre nue `\text{…}`-enveloppée, liste, ou autre.

La reconstruction retenue (`\[ A \]` … `\[ J \]`) est donc la **plus minimale et la plus
défendable** : elle restitue l'information certaine (le domaine désigné) sans inventer un
habillage non attesté.

---

## 4. Statut

- **Aucun lot correctif n'est produit.** Le lot 5c reste appliqué tel quel.
- La confiance de ces dix blocs est **moyenne**, et non haute. Elle était annoncée
  « moyenne » dans le lot 5c ; le présent document en donne la raison complète.
- Si vous préférez suivre la forme de G et H, le lot correctif **5d** est prêt à produire :
  dix blocs, changement mécanique, aucune autre conséquence.

---

## 5. Effet de bord utile

Cette recherche a révélé que **le domaine G possède lui aussi une Grande Carte**, en sept
blocs (A…G), avec deux-points. Elle n'avait jamais été recensée. G n'est pas encore instruit
ni restauré ; sa section §140 est intacte et fournira un point de comparaison de plus quand
son tour viendra.
