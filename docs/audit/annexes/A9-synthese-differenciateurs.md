# A9 — SYNTHÈSE DES DIFFÉRENCIATEURS

**Livrable 4 de la phase 2**
**Date d'établissement :** 2026-10-19
**Objet :** établir ce que Mathemirum peut **légitimement revendiquer** face à l'écosystème étudié,
et — tout aussi important — ce qu'il **ne peut pas** revendiquer.
**Appuis :** `A9-comparaison-transversale.md` (18 attributs × 27 plateformes) et
`A9-registre-des-licences.md` (35 plateformes, 4 statuts d'usage).

---

## 1. Ce qui fait un différenciateur — et ce qui n'en fait pas un

Un différenciateur n'est pas une intention. Pour entrer dans cette synthèse, une revendication doit
satisfaire **quatre conditions** :

| # | Condition | Pourquoi |
|---|---|---|
| **C1** | elle est **vérifiable par un tiers** | sinon c'est une promesse |
| **C2** | elle s'appuie sur une **case vide documentée** de la matrice | sinon elle est déjà occupée |
| **C3** | elle est **tenable dans la durée** | sinon c'est une avance temporaire |
| **C4** | elle découle d'une **exigence du cahier des charges** | sinon c'est une digression |

Chaque différenciateur ci-dessous est donc assorti de **sa preuve** (d'où vient la case vide) et de
**son coût** (ce qu'il en coûte de le tenir).

⚠️ **Une revendication non retenue n'est pas une mauvaise idée.** Elle est simplement déjà occupée,
ou invérifiable. Le §3 les liste explicitement, parce que bâtir une stratégie sur un faux
différenciateur est une erreur coûteuse.

---

## 2. Les différenciateurs retenus

### D1 — Chaque composant porte ses équations, ses hypothèses et son domaine de validité

**Preuve (C2).** Dans la matrice, la ligne « équations et hypothèses » est vide **sans une seule
exception** sur les 27 plateformes. Aucun acteur — ni React Bits, ni Shaders, ni Manim, ni même
Math-To-Manim, qui produit pourtant un « dossier mathématique » — n'expose les hypothèses sous
lesquelles son composant est valide.

**Vérifiabilité (C1).** Totale : pour chaque composant, un tiers peut lire les équations, vérifier
leur cohérence, et contrôler le domaine annoncé.

**Ancrage (C4).** C'est la ligne de partage centrale du cahier des charges entre *effet
artistique*, *visualisation explicable* et *simulation validée*.

**Tenable (C3) ?** Oui, et c'est le point décisif : **c'est un travail que personne ne veut faire**,
donc personne ne le rattrapera par mimétisme rapide.

**Coût.** Élevé. C'est le poste le plus cher du projet, et il suppose de la compétence
mathématique par composant, pas seulement de la compétence d'ingénierie.

---

### D2 — Le classement tripartite assumé, composant par composant

**Preuve (C2).** Aucune plateforme étudiée ne distingue l'effet qui *ressemble* à une simulation de
la simulation *validée*. Le secteur vend du visuel ; il ne qualifie pas ce qu'il vend.

**Vérifiabilité (C1).** Oui, si le classement est accompagné de ses critères : un composant classé
« simulation validée » doit pouvoir montrer sa méthode, ses hypothèses et ses tests.

**Ancrage (C4).** C'est le non-négociable le plus strict du cahier des charges : *jamais présenter
un effet inspiré d'un fluide comme une simulation de Navier–Stokes sans méthode, hypothèses et
validation.*

**Tenable (C3) ?** Oui — à condition d'accepter de classer ses propres composants dans la catégorie
la plus basse quand c'est la vraie. **C'est un différenciateur qui se perd dès le premier mensonge.**

**Coût.** Faible en soi, mais il impose une discipline de rédaction et une honnêteté qui coûte
commercialement.

---

### D3 — Les limites connues, publiées par composant

**Preuve (C2).** C'est **la case la plus vide de la matrice**. Le secteur documente ce que ses
composants font ; il ne documente jamais jusqu'où ils cessent d'être valides.

**Vérifiabilité (C1).** Immédiate, et réfutable : une limite annoncée peut être testée.

**Tenable (C3) ?** Oui, et c'est un différenciateur contre-intuitif : publier ses limites **augmente**
la confiance au lieu de la réduire. Personne ne le fait parce que c'est perçu comme un aveu.

**Coût.** Faible. C'est probablement le meilleur rapport coût/crédibilité de toute cette liste.

⚠️ **Réserve honnête :** ce différenciateur n'a de valeur que si les limites sont **réelles et
spécifiques**. Une section « limites » remplie de généralités est pire que pas de section du tout.

---

### D4 — Des performances **mesurées**, avec méthode et matériel déclarés

**Preuve (C2).** Sur 27 plateformes, **une seule** affirmation de performance a été trouvée —
Shaders annonçant ~25× de gain sur la compilation. ⚠️ Elle n'a pas été vérifiée, et aucune méthode
n'est publiée.

**Vérifiabilité (C1).** Oui, à condition de publier la méthode, le matériel et les conditions.

**Ancrage (C4).** Le cahier des charges exige des « mesures de performance » par composant, et pose
la performance mesurée comme non-négociable aux côtés de la qualité visuelle et de la profondeur
mathématique.

**Tenable (C3) ?** Oui — d'autant que l'environnement de développement impose déjà une contrainte :
⚠️ **ni GPU ni navigateur ne sont disponibles ici.** Les mesures devront être déléguées à vos
machines ou à une intégration continue. C'est une difficulté, mais c'est aussi ce qui garantit que
les mesures seront faites sur du matériel réel et déclaré.

**Coût.** Moyen : il faut une chaîne de mesure reproductible, pas des chiffres isolés.

---

### D5 — Une licence unique, lisible, déclarée dans le dépôt

**Preuve (C2).** Le registre des licences documente **trois mécanismes de présentation trompeuse**,
tous vérifiés :
1. *le titre qui rassure* — « MIT + Commons Clause » chez React Bits ;
2. *l'agrégateur qui répète* — une dizaine d'annuaires annoncent Aceternity UI sous MIT alors que la
   page officielle de l'éditeur décrit une licence propriétaire ;
3. *le dépôt public sans licence* — GeoGebra publie son moteur sans déclarer de licence ;
   le projet `sadeepas` n'en a aucune.

**Vérifiabilité (C1).** Immédiate : un fichier `LICENSE` à la racine, une licence par composant,
et une politique de contribution écrite.

**Ancrage (C4).** Le cahier des charges pose le « libre d'abord » en non-négociable.

**Tenable (C3) ?** Oui, et à coût quasi nul — ce qui en fait un différenciateur **sous-estimé** :
dans un secteur où la moitié des acteurs majeurs ont une licence ambiguë, la clarté est rare.

**Coût.** Faible. ⚠️ **Mais une action est requise en amont :** le corpus source de Mathemirum —
le dépôt de connaissances d'où proviennent les équations — **ne déclare pas non plus de licence**
(constat de la phase 0 : deux dépôts publics, sans LICENSE, sans README). Publier du contenu qui en
dérive sans clarifier ce point **reproduirait exactement le défaut critiqué ici.** Voir §5.

---

### D6 — Un registre à champs étendus, plutôt qu'un catalogue fermé

**Preuve (C2).** shadcn/ui a établi qu'un **article de registre** — un objet décrivant fichiers,
chemins cibles et dépendances — suffit à créer un écosystème interopérable (F02). Ce format est
devenu un standard de fait : React Bits l'émet via `jsrepo`, Shaders l'utilise pour son CLI.

**Vérifiabilité (C1).** Oui : le schéma est public.

**Ancrage (C4).** Le cahier des charges exige, par composant, une « configuration exportable ».

**Tenable (C3) ?** ⚠️ **Partiellement.** C'est une **extension, pas une rupture** : ajouter des
champs (équations, hypothèses, validité, prompt, tests) à un format existant est à la portée de
n'importe quel acteur en place. Ce différenciateur est donc le **plus fragile** des six.

**Coût.** Faible.

---

### D7 — La boucle fermée : prompt → composant → test

**Preuve (C2).** Le secteur fait des moitiés de boucle. **Shaders** a le prompt et la CLI mais
aucun test visible. **Math-To-Manim** a le prompt, la CLI **et** une étape de vérification distincte
— mais il produit une vidéo, qu'on ne peut pas tester. Personne ne ferme la boucle jusqu'au test.

**Vérifiabilité (C1).** Oui : un test qui échoue est une preuve.

**Ancrage (C4).** Le cahier des charges exige à la fois un prompt réutilisable **et** des tests par
composant.

**Tenable (C3) ?** ⚠️ **À vérifier.** C'est le différenciateur le plus dépendant de l'état de
l'art : la génération par IA évolue vite, et un acteur mieux doté peut fermer la boucle avant nous.

**Coût.** Moyen à élevé.

---

## 3. Ce que Mathemirum **ne peut pas** revendiquer

Liste établie explicitement, pour éviter de bâtir sur du sable. Chaque ligne est occupée par un
acteur identifié.

| Revendication tentante | Pourquoi elle est déjà perdue |
|---|---|
| **Le nombre de composants** | Shaders 200+, React Bits 215+, Uiverse 7 456 éléments. Une course perdue d'avance. |
| **La beauté visuelle** | Subjective, invérifiable (violet C1), et le secteur est excellent. |
| **Le WebGPU / la modernité technique** | Shaders est déjà sur WebGPU via TypeGPU, avec cinq frameworks. |
| **Être open source** | shadcn/ui, three.js, Manim, Motion, D3, Shaders : le secteur est majoritairement ouvert, au moins en apparence. |
| **Avoir une CLI** | shadcn, Shaders, React Bits, Math-To-Manim en ont tous une. |
| **L'intégration aux agents IA** | Aceternity annonce le MCP dès son palier gratuit ; Shaders aussi ; shadcn a un répertoire `skills`. |
| **Le multi-framework** | Shaders couvre React, Vue, Svelte, Solid, JS et Framer avec les mêmes propriétés. |
| **L'éditeur visuel qui exporte du code** | Shaders le fait, gratuitement ; React Bits a cinq outils en ligne. |
| **La profondeur mathématique de l'outil** | Desmos, GeoGebra et Wolfram sont infiniment plus profonds. |

⚠️ **La lecture est sévère mais utile :** sur toute la couche *technique* et *distributive*,
Mathemirum arriverait **après** des acteurs mieux dotés. **Les seules cases libres sont des cases de
preuve** — c'est-à-dire des cases que le marché ne valorise peut-être pas (§4).

---

## 4. Le risque central, énoncé sans détour

⚠️ **Tous les différenciateurs retenus sont des centres de coût.** Documenter les équations, écrire
les tests, mesurer les performances, publier les limites : ce sont des dépenses, et **aucun des 27
acteurs étudiés ne les engage**.

Deux explications sont possibles, et elles ont des conséquences opposées :

1. **Personne n'y a pensé, ou personne n'a voulu payer.** → La place est libre et la thèse tient.
2. **Le marché ne valorise pas ces attributs.** → La place est libre *parce qu'elle ne vaut rien*,
   et investir dans la preuve serait une erreur stratégique.

**Ces deux hypothèses ne sont pas départagées par cette phase.** L'étude de demande
(recommandation R3) est le seul moyen de les trancher, et **c'est la dépendance la plus importante
de la phase 2**.

Un élément penche toutefois en faveur de la première : **le cahier des charges lui-même** formule ces
exigences comme des non-négociables. Le projet ne cherche pas à maximiser une audience, il cherche à
satisfaire une exigence de rigueur. **Si c'est bien l'objectif, la question du marché est
secondaire** — mais il faut le dire explicitement, pas le supposer.

---

## 5. Deux actions requises avant de pouvoir tenir ces revendications

### 5.1 Clarifier la licence du corpus source

⚠️ Le dépôt de connaissances d'où proviennent les équations — `Stane316/my-own-connaissance` — est
public **sans fichier LICENSE** (constat de phase 0). Les 773 restaurations appliquées pendant le
chantier, et les 2 354 équations du corpus, en dérivent.

Publier un composant Mathemirum accompagné d'une équation tirée de ce corpus, **sans avoir clarifié
le régime du corpus**, exposerait le projet au reproche même qu'il adresse aux autres.
**→ Action : vous prononcer sur la licence du corpus source.**

### 5.2 Lever les quatre points ouverts du registre des licences

Rappelés ici parce que D5 en dépend directement :
1. le conflit entre le paquet MIT de Shaders et son contrat de plateforme v1.7 ;
2. la qualification d'une « configuration exportable » face à la clause Commons Clause de React Bits;
3. la portée de la clause de co-propriété des productions GeoGebra ;
4. la procédure d'approbation « open-source projects approved by Wolfram ».

---

## 6. Limites de cette synthèse

- ⚠️ **Les différenciateurs D6 et D7 sont les plus fragiles** : l'un est une extension à la portée de
  tout acteur en place, l'autre dépend d'un état de l'art qui bouge vite. Ils sont retenus, mais
  classés en bas de liste pour cette raison.
- ⚠️ **Aucune validation par le marché.** Cette synthèse dit ce qui est *libre*, pas ce qui est
  *demandé*. La différence est entière.
- ⚠️ **Aucune plateforme n'a été installée ni exécutée** : pas de GPU ni de navigateur dans cet
  environnement. Les affirmations techniques adverses sont donc reprises, non vérifiées.
- ⚠️ **Aucune preuve d'absence.** 27 plateformes observables ne sont pas l'écosystème entier.

---

## 7. Références

- `A9-comparaison-transversale.md` — les cases vides qui fondent D1, D3, D4
- `A9-registre-des-licences.md` — les trois mécanismes trompeurs qui fondent D5
- `../fiches-phase-2/F02-shadcn-ui.md` — le format de registre (D6)
- `../fiches-phase-2/F03-math-to-manim.md` et `F11-shaders-et-openshaders.md` — les moitiés de
  boucle (D7)
- `../../restauration/CLOTURE-CHANTIER.md` — l'état du corpus source (§5.1)
- Cahier des charges : non-négociables et livrables par composant
