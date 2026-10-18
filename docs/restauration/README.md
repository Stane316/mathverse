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
| **Titres et équations des documents A, B, C, D** | 4 documents | **chantier distinct** (§6) |
| Artefacts d'échappement de crochets (E, R, S, U) | 48 blocs | correction de l'échappement, pas du contenu |

## 3. Inventaire

**`annexes/inventaire-defauts.csv`** — 724 lignes : fichier, numéro de ligne, heuristique, texte actuel du bloc, bloc exact, contexte avant/après.

Répartition : J 166 · I 109 · N 104 · H 64 · L 61 · G 60 · M 59 · O 38 · UI/UX 20 · **K 18** · F 12 · Q 11 · P 2.

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
git switch -c restauration-equations          # jamais sur main
git apply --check /chemin/domaine-K-lot1.gitdiff   # vérification, n'écrit rien
git apply /chemin/domaine-K-lot1.gitdiff
cp /chemin/RESTAURATION-EQUATIONS.md .
git add -A && git commit -F /chemin/domaine-K-lot1.message-commit.txt
```

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
| 1 | **K** — 18 défauts signalés, **28 traités** | domaine le plus utile au produit, équations canoniques — **lot 1 appliqué** (19), complément de 10 propositions en attente |
| 2 | **L** — analyse numérique | socle des critères de validation ; 61 défauts |
| 3 | **I** — calcul différentiel | 109 défauts, socle des systèmes continus |
| 4 | **N** — transformées | 104 défauts, utile aux composants de signal |
| 5 | J, H, G, M, O | 387 défauts, utilité indirecte |
| 6 | F, Q, P, UI/UX | 45 défauts |
| 7 | A, B, C, D | selon la réponse sur la voie 1 |

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
