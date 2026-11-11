# 01 — Vision, mission et positionnement

**Date :** 2026-11-11 · **Commit :** `6f87baf`
**Sources principales :** `docs/audit/PHASE-0-rapport-audit-initial.md`,
`annexes/A9-synthese-differenciateurs.md`, `docs/audit/A10-etude-de-demande.md`,
`annexes/A9-comparaison-transversale.md`

---

## 1. Vision

🔶 **Déduit** de l'ensemble des documents d'audit — aucune « déclaration de vision » formelle
n'existe dans le dépôt.

> Rendre la beauté des mathématiques **visible et vérifiable** sur le web : produire des composants
> visuels qui ne se contentent pas de *ressembler* à une simulation, mais qui **disent** ce qu'ils
> calculent, sous quelles hypothèses, jusqu'où ils sont valides, et à quelle vitesse ils tournent.

Cette formulation repose sur trois éléments ✅ confirmés :

1. le nom retenu, *mathematica* + *mirum*, porte explicitement « la merveille des mathématiques »
   (`docs/decisions/0001`) ;
2. les deux documents originels du dépôt sont un catalogue de courbes **esthétiques** et animables
   (`Equations Mathématiques/`) ;
3. le cahier des charges exige, par composant, l'explication mathématique, les équations et
   hypothèses, les tests, les mesures de performance et les limites connues
   (`A9-comparaison-transversale.md` §1.1).

---

## 2. Mission

✅ **Confirmé** par la synthèse des différenciateurs (`A9-synthese-differenciateurs.md` §1–§2).

La mission se formule comme une **exigence de rigueur** : combler la case que les 27 plateformes
étudiées laissent vide — la **couche probatoire**.

Les trois attributs de cette couche, tels que définis par la grille de lecture :

| Attribut | Question à laquelle il répond |
|---|---|
| Explication mathématique | **pourquoi** ça marche |
| Équations et hypothèses | **sous quelles conditions** |
| Limites connues | **jusqu'où** |

La ligne de partage du cahier des charges est celle-ci :

```
effet artistique   →   visualisation explicable   →   simulation validée
```

🔶 **Déduit** : le projet s'interdit de présenter un effet inspiré d'un fluide comme une simulation
de Navier–Stokes sans méthode, hypothèses et validation. Cette règle est citée comme
« le non-négociable le plus strict » du cahier des charges.

---

## 3. Le problème adressé

### 3.1 Le problème du corpus source

✅ **Confirmé** (`A2-inventaire-structurel.md` §3).

La chaîne de production du savoir mathématique est **rompue après l'algorithme** :

```
modèle  →  équation  →  algorithme  →  ❌ implémentation  →  ❌ tests
    ✅          ✅            ✅              absent              absent
```

Sur 80 330 lignes et 2 354 équations : **zéro bloc de code**, zéro pseudocode formaté, zéro jeu de
données. Le corpus énonce « implémentation » 223 fois et « test » 447 fois — il en parle, il ne les
contient pas.

### 3.2 Le problème du secteur

✅ **Confirmé** sur 27 plateformes (`A9-comparaison-transversale.md`).

| Constat | Preuve |
|---|---|
| Personne n'expose les équations et hypothèses de ses composants | case vide **sans exception** sur 27 plateformes |
| Personne ne publie ses limites | c'est **la case la plus vide** de la matrice |
| Personne ne publie de performances mesurées | **une seule** affirmation trouvée (Shaders, ~25× sur la compilation), non vérifiée, sans méthode |
| Les licences sont fréquemment trompeuses | **trois mécanismes** documentés (titre qui rassure, agrégateur qui répète, dépôt public sans licence) |
| La boucle prompt → composant → test n'est jamais fermée | Shaders a le prompt sans test ; Math-To-Manim a le test mais produit une vidéo |

### 3.3 Le problème de l'utilisateur

🔶 **Déduit**, et partiellement étayé par l'étude de demande.

Le développeur qui intègre un composant visuel **copie sans comprendre** : il ne sait pas ce que le
composant calcule, ni quand il cesse d'être valide, ni ce qu'il coûte. Le discours « comprendre
plutôt que copier » est attesté — mais ⚠️ **dans la sphère jeu vidéo et apprentissage des shaders,
pas dans celle des composants web** (`A10-etude-de-demande.md` §1).

---

## 4. Proposition de valeur

### 4.1 Les sept différenciateurs retenus

✅ Source : `A9-synthese-differenciateurs.md` §2. Chacun doit satisfaire quatre conditions :
vérifiable par un tiers (C1), appuyé sur une case vide documentée (C2), tenable dans la durée (C3),
découlant d'une exigence du cahier des charges (C4).

| # | Différenciateur | Preuve (C2) | Coût | Demande |
|---|---|---|---|---|
| **D1** | Chaque composant porte ses **équations, hypothèses et domaine de validité** | case vide sur 27/27 plateformes | **élevé** | ❌ non observée |
| **D2** | **Classement tripartite** assumé, composant par composant (effet / visualisation / simulation validée) | aucune plateforme ne qualifie ce qu'elle vend | faible | ❌ non observée |
| **D3** | Les **limites connues**, publiées par composant | **la case la plus vide** de la matrice | faible | ✅ directe (indirecte) |
| **D4** | Des **performances mesurées**, méthode et matériel déclarés | 1 seule affirmation trouvée, non vérifiée | moyen | ✅ directe |
| **D5** | Une **licence unique, lisible**, déclarée dans le dépôt | 3 mécanismes trompeurs vérifiés | faible | ✅ directe |
| **D6** | Un **registre à champs étendus** plutôt qu'un catalogue fermé | le format shadcn/ui est un standard de fait | faible | ⚠️ indirecte |
| **D7** | La **boucle fermée** : prompt → composant → test | le secteur fait des moitiés de boucle | moyen à élevé | ⚠️ émergente |

### 4.2 ⚠️ Le verdict de demande — la révision défavorable

**C'est le résultat le plus important de toute la phase 2, et il est défavorable.**

`A10-etude-de-demande.md` (2026-10-19) a confronté les sept différenciateurs aux signaux de demande
observés. Le classement qui en résulte **n'est pas celui du §4.1** :

| Différenciateur | Verdict | Fondement |
|---|---|---|
| **D5** licence claire | ✅ **direct** | la licence figure comme critère de choix dans les guides |
| **D4** performances mesurées | ✅ **direct** | le **profilage** est la douleur n°1 des développeurs de shaders (Khronos 2026, 400+ répondants, 53 % en top 3) |
| **D3** limites connues | ✅ **direct (indirectement)** | documentation = 1ᵉʳ critère (93 %) ; les guides d'évaluation demandent explicitement « edge cases » et « common pitfalls » |
| **D7** boucle prompt → test | ⚠️ **émergent** | critère apparu en 2026, avec risque de cycle de mode |
| **D6** registre étendu | ⚠️ **indirect** | la demande porte sur le modèle copier-coller, pas sur les champs |
| **D1** équations et hypothèses | ❌ **non observé** | aucun des ~20 guides consultés ne mentionne ces attributs |
| **D2** classement tripartite | ❌ **non observé** | aucun signal, dans aucune source |

**Conséquence, énoncée sans détour par la source :**

> **D1 et D2 — les deux différenciateurs les plus identitaires du projet — sont ceux dont la demande
> est la moins établie.** Ils restent, parce qu'ils découlent d'exigences non négociables du cahier
> des charges, mais ils doivent être défendus comme **une exigence de rigueur assumée**, **pas comme
> un avantage concurrentiel**. Prétendre le contraire serait faux.

### 4.3 Le risque central

⚠️ **Tous les différenciateurs retenus sont des centres de coût**, et aucun des 27 acteurs étudiés
ne les engage. Deux explications s'opposent :

1. **personne n'a voulu payer** → la place est libre, la thèse tient ;
2. **le marché ne valorise pas ces attributs** → la place est libre *parce qu'elle ne vaut rien*.

L'étude de demande a tranché partiellement, **pas dans le sens favorable** : hypothèse 1 pour D3,
D4, D5 ; ⚠️ **hypothèse 2 non réfutée** pour D1 et D2.

🔶 **Déduction de la source elle-même** : le cahier des charges formule ces exigences comme des
non-négociables. Le projet ne cherche donc pas à maximiser une audience, il satisfait une exigence
de rigueur. **Si c'est bien l'objectif, la question du marché est secondaire — mais il faut le dire
explicitement, pas le supposer.**

### 4.4 Ce que le projet **ne peut pas** revendiquer

✅ Source : `A9-synthese-differenciateurs.md` §3. Liste établie pour éviter de bâtir sur du sable.

| Revendication tentante | Pourquoi elle est perdue d'avance |
|---|---|
| Le nombre de composants | Shaders 200+, React Bits 215+, Uiverse 7 456 éléments |
| La beauté visuelle | subjective, invérifiable, et le secteur est excellent |
| Le WebGPU / la modernité | Shaders est déjà sur WebGPU via TypeGPU |
| Être open source | le secteur est majoritairement ouvert, au moins en apparence |
| Avoir une CLI | shadcn, Shaders, React Bits, Math-To-Manim en ont tous une |
| L'intégration aux agents IA | Aceternity et Shaders annoncent le MCP ; shadcn a un répertoire `skills` |
| Le multi-framework | Shaders couvre React, Vue, Svelte, Solid, JS, Framer |
| L'éditeur visuel qui exporte du code | Shaders le fait gratuitement |
| La profondeur mathématique de l'outil | Desmos, GeoGebra et Wolfram sont infiniment plus profonds |

> ⚠️ **Lecture sévère mais utile :** sur toute la couche *technique* et *distributive*, Mathemirum
> arriverait **après** des acteurs mieux dotés. **Les seules cases libres sont des cases de preuve.**

---

## 5. Public cible

🔶 **Déduit** du cahier des charges et de l'étude de demande ; le positionnement n'a pas fait l'objet
d'une décision formalisée.

| Public | Statut | Fondement |
|---|---|---|
| **Développeurs front-end** intégrant des composants visuels | 🔶 principal | les guides de choix de bibliothèques sont la source de la demande mesurée |
| Développeurs créatifs / creative coders | 🔶 secondaire | les deux documents originels du dépôt leur sont directement adressés |
| Développeurs de shaders | ✅ douleur documentée | enquête Khronos 2026, 400+ répondants |
| Designers interactifs | 🔷 envisagé | non instruit |
| Artistes numériques | 🔷 envisagé | non instruit |
| Apprenants en mathématiques | 🔷 envisagé | le discours « comprendre plutôt que copier » existe dans la sphère apprentissage, **pas** dans celle des composants web |

⚠️ **Le cahier des charges distingue deux audiences** dont le recouvrement n'est pas établi (risque
R2, `A9-rapport-fin-de-phase-2.md` §9). La question n'a pas été tranchée.

---

## 6. Positionnement

```
                    profondeur mathématique de l'outil
                                ▲
              Wolfram Alpha     │
                    GeoGebra    │
                       Desmos   │
                                │        ← Mathemirum vise ici :
                                │          profondeur **documentée**,
                                │          pas profondeur de calcul
      ──────────────────────────┼──────────────────────────► richesse
                                │            d'intégration web
                                │   shadcn/ui · React Bits
                                │   Aceternity · Uiverse
                                │   Shaders
                                │
```

🔶 **Déduit.** Mathemirum ne gagne ni sur la profondeur de calcul (Desmos, GeoGebra, Wolfram) ni sur
la richesse d'intégration (shadcn, React Bits, Shaders). Il se place **sur un troisième axe** : la
qualité de la preuve attachée au composant.

⚠️ C'est un positionnement dont **la demande n'est pas établie** (§4.2).

---

## 7. Ce que la vision implique concrètement

| Implication | Conséquence |
|---|---|
| Documenter les équations de chaque composant | compétence **mathématique** par composant, pas seulement d'ingénierie — c'est le poste le plus cher |
| Publier les limites | accepter de classer ses propres composants dans la catégorie la plus basse quand c'est la vraie. **Un différenciateur qui se perd dès le premier mensonge** |
| Mesurer les performances | une chaîne de mesure reproductible, sur matériel déclaré — impossible dans cet environnement (ni GPU ni navigateur) |
| Licence claire | clarifier d'abord la licence du corpus source, sinon le projet reproduit le défaut qu'il critique |

---

## 8. État de la vision

| Élément | Statut |
|---|---|
| Vision formulée dans un document dédié | ❌ **n'existe pas** — reconstruite ici par déduction |
| Différenciateurs | ✅ sept, documentés et argumentés |
| Validité de la thèse | ⚠️ **partiellement infirmée** par l'étude de demande sur D1 et D2 |
| Public cible | 🔶 non formalisé, deux audiences non départagées |
| Positionnement | 🔶 déduit, non écrit |

**Lacune à combler :** le projet n'a nulle part écrit sa vision. Elle se déduit du nom, des
documents originels et du cahier des charges, mais aucune déclaration ne la fixe. C'est une
fragilité : chaque nouvel intervenant la reconstruit.
