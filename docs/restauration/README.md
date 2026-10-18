# CHANTIER DE RESTAURATION DU CORPUS — CADRE ET MÉTHODE

**Date d'ouverture :** 2026-10-18 — **Décision :** lancée par le porteur du projet
**Dépôt concerné :** `Stane316/my-own-connaissance` (jamais modifié sans validation explicite)
**Pilote :** agent, sous réserve des points de contrôle ci-dessous
**Référence :** `docs/audit/A7-integrite-des-equations.md` (état des lieux)

---

## 1. Nature réelle du chantier — à lire avant tout

**Il ne s'agit pas d'une récupération, mais d'une reconstruction.**

Les analyses montrent que le contenu détruit **n'est pas présent ailleurs dans les fichiers** : les arguments des commandes LaTeX supprimées ont disparu avec elles. Exemples vérifiés :

- `\[ D= \]` — la formule `log N / log(1/r)` n'existe nulle part dans le document ;
- `\[ =(y-x) \]` — les paramètres σ, ρ, β du système de Lorenz ont disparu, et la liste « où : » qui suit est vide ;
- `\[ _{n}_ {i=0}^{n-1} |f'(x_i)| \]` — il ne reste que des fragments de la formule de Lyapunov.

Autrement dit : **on ne restaure pas, on réécrit.** Chaque équation reconstruite sera donc :

- **marquée comme reconstruction**, jamais présentée comme le texte d'origine ;
- **accompagnée de sa justification** (fragment survivant + forme canonique attendue) ;
- **soumise à votre validation** avant toute écriture dans le dépôt de connaissances.

## 2. Périmètre

| Catégorie | Volume | Traitement |
|---|---|---|
| Équations display structurellement incomplètes | **724** | reconstruction proposée, par domaine |
| Blocs display vides ou quasi vides | 365 | reconstruction ou suppression selon le contexte |
| Fragments de commandes (`\_`, `_{n}_`) | 205 | reconstruction |
| Parenthèses vides `()` | 73 | reconstruction à partir du contexte |
| Membres gauche ou droit manquants | 110 | reconstruction |
| **Titres et équations des documents A, B, C, D** | 4 documents | **chantier distinct** (§6) — voir le régime 3 ci-dessous |
| Artefacts d'échappement de crochets (E, R, S, U) | 48 blocs | correction de l'échappement, pas du contenu |

### Trois régimes de dégradation, pas un seul

Les documents n'ont pas tous été atteints de la même façon. Trois régimes distincts
ont été identifiés, et ils n'appellent pas la même méthode :

| | Régime | Documents | Ce qui subsiste | Méthode |
|---|---|---|---|---|
| 1 | Commandes LaTeX détruites **avec leurs arguments** | E à U | le bloc, son squelette, des fragments (`\_`, `_{}`, `( )`) | reconstruction |
| 2 | Lettres grecques détruites | E à U | idem, sans résidu | reconstruction |
| 3 | **Blocs `\[…\]` supprimés, formules aplaties en texte inline** | **A à D** (vérifié sur A, B, C, D) | **les variables, l'ordre des opérations** | **recomposition** |

Le régime 3 a été découvert sur le document D (fiche `domaine-D-…`, 2026-10-18) : les
formules y ont été réécrites en texte, chaque symbole séparé par des doubles espaces, et
rejetées en fin de paragraphe. Exemple, section 24 (intersection rayon/plan) :

```
R ( t ) =   O   +   td   n   ⋅   X   +   c   = 0   t   = −   n   ⋅   d n   ⋅   O   +   c
n   ⋅   d   =   0   ∥ P   −   C ∥   = 2   r 2
```

soit `R(t)=O+td`, `n·X+c=0`, `t=−(n·O+c)/(n·d)`, `n·d≠0`, `‖P−C‖²=r²`. La barre de
fraction disparaît, mais numérateur et dénominateur restent **adjacents et dans l'ordre** :
la recomposition est donc déterministe, et **plus sûre** que la reconstruction des
documents E à U, qui part de résidus.

Ce régime détruit en revanche les lettres grecques (sans laisser le résidu `\_`),
les exposants et indices, et quelques glyphes (`≠` est perdu).

Mesures sur D : **22 lignes** portent des runs recomposables, **212 slots** « :  »
marquent des formules dont il ne reste que l'annonce.

### Régime 3 — vérification achevée sur A, B, C (2026-10-18)

Le régime 3 a été **confirmé sur les quatre documents** A, B, C et D. Le tableau suivant
est entièrement mesuré :

| Doc | Lignes | Octets | Oct./ligne | Titres `^#` | Blocs `\[…\]` | Parties | Sections | Slots « :  » | Grecques | Exposants | Lignes à run |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** — logique | 119 | 81 681 | 686 | **0** | **0** | 0 | 101 (décimales) | 132 | 2 | **0** | 10 |
| **B** — nombres | 103 | 68 220 | 662 | **0** | **0** | 0 | 95 (décimales) | 155 | 19 | **0** | 22 |
| **C** — algèbre linéaire | 123 | 76 998 | 626 | **0** | **0** | 22 | 31 (décimales) | 169 | **80** | **0** | **41** |
| **D** — géométrie | 133 | 58 287 | 438 | **0** | **0** | 30 | 122 (« N — ») | 212 | 27 | **0** | 23 |
| **Total A–D** | **478** | **284 186** | — | **0** | **0** | 52 | 349 | **668** | 128 | **0** | **96** |

**Ce qui est établi :**

1. **Le régime 3 est universel sur A–D.** Zéro titre Markdown, zéro bloc `\[…\]`, zéro
   mathématique inline `$…$`, zéro bloc de code — dans les quatre documents, sans
   exception. La notation y est aplatie en texte ou absente.
2. **La structure, elle, existe et est comptable** : 349 sections au total, mais **invisible
   à tout outil** faute de balisage. `extract_domain.py` ne peut rien en extraire ; tout
   relevé se fait à la main.
3. **Les exposants sont universellement détruits** (`² ³ ⁿ` : 0 occurrence dans les quatre
   documents). C'est la seule perte vraiment systématique.
4. **Les lettres grecques survivent partiellement** — 128 occurrences au total, très
   inégalement réparties (C en concentre 80, A seulement 2). Une affirmation antérieure
   de la fiche D, selon laquelle elles auraient été supprimées, a été **rectifiée**.
5. **96 lignes portent des runs recomposables**, contre **668 slots vides**. La
   recomposition ne résout donc qu'une partie du chantier A–D — mais elle la résout
   **mieux** que la reconstruction pratiquée sur E–U, puisqu'elle part de variables
   conservées et non de résidus.

**Conséquence sur le chantier A–D :** il se divise désormais en deux travaux distincts —
une **recomposition** (96 lignes, confiance élevée) et une **reconstruction** (668 slots,
confiance à établir). À ces deux travaux s'ajoute le **rétablissement des titres**, qui ne
touche pas au fond et conditionne tout le reste.

## 3. Inventaire

**`annexes/inventaire-defauts.csv`** — 724 lignes : fichier, numéro de ligne, heuristique, texte actuel du bloc, bloc exact, contexte avant/après.

Répartition : J 166 · I 109 · N 104 · H 64 · L 61 · G 60 · M 59 · O 38 · UI/UX 20 · **K 18** · F 12 · Q 11 · P 2.

**État au 2026-10-18 : 706 défauts.** Le document K est traité (18 signalés + 12 découverts
à la lecture = 30 restaurations, 0 défaut restant). Le document L est instruit : 131 défauts
recensés (61 signalés + 70 découverts), 87 propositions prêtes, 44 blocs en attente de l'auteur. Les décomptes par document ci-dessus
sont des **planchers** : sur K, la relecture bloc par bloc a révélé 55 % de défauts
supplémentaires. Il faut s'attendre à la même proportion ailleurs.

**Mesure directe du sous-comptage (N, 2026-10-18).** Sur le domaine N : 146 blocs restaurés,
alors que l'inventaire n'en signalait que 104 — et seuls 72 des 104 ont effectivement été
résorbés par les 146 restaurations. Autrement dit **74 blocs (51 %) étaient dégradés sans
être détectés** par les six heuristiques. La cause est connue : un bloc dont le résidu
ressemble à une notation complète — `\[ F(\omega) \]` — ne déclenche aucune des six règles,
alors que l'équation a bien été détruite. **Le chiffre 724 est donc un minimum strict.**
Tout bloc non encore relu doit être considéré comme potentiellement dégradé, signalé ou non.

L'inventaire est **régénérable à volonté** : `python3 tools/restauration/extract_defects.py <source> inventaire <sortie.csv>`, et consultable lot par lot avec le mode `contexte`.

## 4. Protocole de reconstruction

Pour chaque équation :

1. **Lire le contexte** (3 lignes avant, 3 après) pour identifier la notion.
2. **Reconstruire** à partir du fragment survivant et de la forme canonique connue.
3. **Classer la confiance** :
   - **haute** — le fragment survivant et la forme canonique ne laissent pas d'autre lecture raisonnable (ex. `=(y-x)` → `dx/dt = σ(y−x)`) ;
   - **moyenne** — forme canonique probable, mais un choix de notation ou de normalisation subsiste ;
   - **inconnue** — l'intention de l'auteur est requise (bloc vide dont le contenu ne se déduit pas).
4. **Proposer un test de validation** : valeur de référence, invariance, ou comparaison numérique permettant de vérifier la formule reconstruite.
5. **Ne rien écrire** dans le dépôt de connaissances avant votre validation du lot.

## 5. Format de livraison

Chaque lot est livré dans `propositions/<domaine>.md`, sous forme de **tableau applicable** :

| Ligne | Bloc actuel | Reconstruction proposée | Confiance | Justification | Validation proposée |

Les propositions sont réunies dans un **fichier correctif** (`propositions/<domaine>.patch.json`) : liste de remplacements exacts (ligne → ancien bloc → nouveau bloc), applicable par un script. Le script d'application (`tools/restauration/apply_patch.py`) **vérifie chaque bloc attendu avant d'écrire quoi que ce soit** : à la première discordance, rien n'est écrit. Il n'est **pas** exécuté sur le dépôt de connaissances sans votre accord explicite, lot par lot.

Une fois un lot validé, il est livré dans `livrables/` sous trois formes : un **diff unifié**
(`<domaine>.gitdiff`, applicable par `git apply`), le **message de commit** correspondant, et
le fichier de traçabilité `RESTAURATION-EQUATIONS.md` destiné à la racine du dépôt de
connaissances.

## 6. Le cas A, B, C, D — chantier distinct

Ces quatre documents ont perdu **leur arborescence de titres et leurs équations** (103 à 133 lignes pour 58 à 82 Kio : le texte a été aplati). Deux voies :

- **Voie 1 (préférable) — récupération d'une version antérieure.** Si vous détenez un brouillon, un export d'origine ou un historique d'outil, la restauration est immédiate et fidèle. **C'est une question à laquelle vous seul pouvez répondre.**
- **Voie 2 — reconstruction.** Échantillonnage du texte, détection des marqueurs de section, reconstruction d'un plan, puis restructuration du Markdown. Long, partiel, et jamais fidèle à l'original.

**Réponse de l'auteur (2026-10-18) : non, il n'existe pas de version antérieure de A, B, C, D.**
La voie 1 est donc fermée. Le lot 7 sera une **restructuration par reconstruction** (voie 2) :
échantillonnage du texte, détection des marqueurs de section, reconstruction d'un plan. Ce
lot est le plus incertain du chantier, et le dernier.

## 7. Application effective — procédure

**Constat (2026-10-18).** L'envoi git vers `my-own-connaissance` est refusé depuis
l'environnement de travail : `403 — Permission to Stane316/my-own-connaissance.git denied`,
et `403 — Resource not accessible by integration` via l'API (le jeton disponible n'est
autorisé que sur le dépôt `mathverse`). **Aucune tentative de contournement n'est faite.**

Le travail est donc préparé dans un clone local (branche `arena/restauration-equations`, un
commit par lot) puis livré sous forme de diff. Deux façons de procéder :

**A. Vous appliquez localement** (recommandé, ~30 s) :

```bash
cd my-own-connaissance
git switch -c restauration-equations               # jamais sur main

# lot 1 — domaine K
git apply --check ../chemin/domaine-K-lot1.gitdiff      # vérification, n'écrit rien
git apply ../chemin/domaine-K-lot1.gitdiff
cp ../chemin/RESTAURATION-EQUATIONS.md .
git add -A && git commit -F ../chemin/domaine-K-lot1.message-commit.txt

# lot 1 bis — même document, À APPLIQUER ENSUITE (les numéros de ligne en dépendent)
git apply --check ../chemin/domaine-K-lot1bis.gitdiff
git apply ../chemin/domaine-K-lot1bis.gitdiff
git add -A && git commit -F ../chemin/domaine-K-lot1bis.message-commit.txt
```

Si un `git apply` échoue, c'est que le lot précédent n'a pas été appliqué, ou que le fichier
a bougé entre-temps : **ne forcez pas**, signalez-le.

**B. Vous autorisez l'accès en écriture** au dépôt `my-own-connaissance` pour la connexion
GitHub utilisée ici ; les lots suivants sont alors poussés directement sur une branche
dédiée, sans jamais ouvrir de pull request.

Dans les deux cas : **un commit par lot**, pour pouvoir relire ou refuser un lot sans
toucher aux autres.

## 8. Sécurité et gouvernance

1. **Aucune écriture dans `my-own-connaissance`** sans votre validation explicite d'un lot.
2. **Aucune modification en place** : les corrections sont d'abord produites dans ce dépôt, sous forme de correctifs reproductibles.
3. **Traçabilité totale** : chaque correction porte sa ligne d'origine, son ancien bloc, son nouveau bloc, sa confiance et sa justification.
4. **Réversibilité** : tout lot appliqué peut être annulé ligne par ligne à partir du correctif.
5. **Aucune suppression** de contenu existant sans signalement explicite.
6. Le dépôt de connaissances restant sur **un seul commit**, une **sauvegarde indépendante** doit être réalisée avant toute écriture — à votre initiative, l'agent n'ayant pas la main sur vos copies locales.

## 9. Priorisation

| Ordre | Lot | Pourquoi |
|---:|---|---|
| 1 | **K** — 18 défauts signalés, **30 traités** | domaine le plus utile au produit, équations canoniques — **terminé, 0 défaut restant** (lots 1 et 1 bis) |
| 2 | **L** — analyse numérique | socle des critères de validation ; 61 signalés, **131 au total**, 102 appliqués — **33 blocs en attente de l'auteur** |
| 3 | **I** — calcul différentiel | 109 signalés, 318 blocs lus — **lots 3a (62), 3b (133) et 3c (9) : 204 restaurations appliquées**, blocs vides 44 → 27 — **28 blocs en attente de l'auteur** |
| 4 | **N** — transformées | 104 signalés, **245 blocs display** recensés — **lots 4a (62) et 4b (84) : 146 restaurations appliquées**, défauts détectés 104 → 32, blocs vides 71 → 34 — **33 blocs en attente de l'auteur** |
| 5 | **J** — optimisation | 166 signalés, **119 observés** (lecture intégrale des 332 blocs — le plus gros document) — **lots 5a (102 entrées) et 5b (186) proposés, en attente de validation** — **document entièrement parcouru** |
| 6-9 | H, G, M, O, F, Q, P, UI/UX, E/R/S/U, « Ai Technical Litteracy » | voir `PLAN-ACHEVEMENT.md` |
| 10 | A, B, C, D | restructuration (voie 2) — **chantier distinct, périmètre confirmé dans le périmètre d'achèvement** |

> **Décision du porteur (2026-10-18) : le chantier doit être ACHEVÉ avant d'ouvrir la phase 2.**
> L'ordre ci-dessous est donc devenu un plan d'achèvement, détaillé dans
> **`PLAN-ACHEVEMENT.md`** : définition de sortie, mesure du reste à faire (~659 défauts
> signalés, ~1 200 estimés), deux flux (reconstructions autonomes / blocs à arbitrer) et
> protocole de validation par lot. Le facteur limitant est le flux B, qui dépend de vous.

La priorisation suit l'utilité pour le produit, pas l'ordre alphabétique : les domaines qui alimenteront les premiers composants sont restaurés en premier.

**Les décomptes ci-dessus sont des planchers.** Ils proviennent de l'inventaire automatique. La relecture bloc par bloc du document K a révélé **10 dégradations supplémentaires** invisibles aux heuristiques (55 % de défauts en plus sur ce document). Il faut donc considérer que chaque lot comportera, en plus des défauts signalés, une proportion comparable de défauts découverts à la lecture.

## 10. Critères d'acceptation d'un lot

1. Chaque défaut du lot a une proposition, ou une raison explicite de non-reconstruction.
2. Aucune proposition de confiance « moyenne » ou « inconnue » n'est présentée comme certaine.
3. Chaque reconstruction de confiance haute est accompagnée d'un test de validation.
4. Le correctif est applicable par script et réversible.
5. Le lot est validé par vous avant application.

## 11. Risques

| Risque | Gravité | Parade |
|---|---|---|
| Introduire une formule fausse dans le corpus | **Haute** | confiance déclarée, justification, test de validation, validation humaine |
| Reconstruction « plausible » mais différente de l'intention de l'auteur | Haute | traçabilité de l'origine, marquage « reconstruction », votre arbitrage |
| Perte de l'original par écrasement | **Haute** | aucune écriture sans sauvegarde confirmée et validation de lot |
| Dérive du périmètre (tout réécrire) | Moyenne | lots bornés, critères d'arrêt par lot |
