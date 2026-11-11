# 09 — Problèmes, risques et incohérences

**Date :** 2026-11-11 · **Commit :** `6f87baf`

---

## 1. Le blocage n°1 : la licence du corpus source

| | |
|---|---|
| **Gravité** | 🔴 **critique** |
| **Nature** | ❌ **blocage avéré** |
| **Origine** | `Stane316/my-own-connaissance` est public **sans fichier LICENSE**, sans README, sans description |
| **Conséquence juridique** | un dépôt public sans licence = **tous droits réservés**. Le contenu est *visible*, il n'est pas *réutilisable* |
| **Conséquence pour le projet** | les 2 354 équations du corpus et les 843 restaurations en dérivent. Publier un composant accompagné d'une de ces équations **reposerait sur une base juridique non établie** |
| **Aggravation** | ⚠️ c'est **exactement le défaut que le projet critique** chez GeoGebra (moteur publié sans licence) et chez `sadeepas` |
| **Ce qu'il faut pour résoudre** | une décision du porteur |
| **Statut** | ⚠️ décision 0002 **soumise, en attente** |

✅ Vérifié par l'API GitHub le 2026-10-19. Précision utile : ❌ **les faits mathématiques ne sont
pas protégeables** — une équation, un théorème, une valeur ne sont pas couverts. Ce qui l'est,
c'est la **mise en forme** et le **choix d'agencement**.

---

## 2. R1 — Les quatre points ouverts du registre des licences

| Gravité | 🔴 haute |
|---|---|
| **Nature** | ❌ blocage avéré — c'est **la seule action restante de la Phase 2** |
| **Dépendance** | ⚠️ **les éditeurs** — hors de portée de l'agent |
| **Ce qu'il faut** | une réponse écrite des éditeurs |

| # | Point ouvert |
|---:|---|
| 1 | le conflit entre le **paquet MIT de Shaders** et son **contrat de plateforme v1.7**, qui interdit de vendre ou redistribuer le contenu créé |
| 2 | la qualification d'une **« configuration exportable »** face à la **clause Commons Clause** de React Bits |
| 3 | la portée de la **clause de co-propriété des productions GeoGebra** |
| 4 | la procédure d'approbation **« open-source projects approved by Wolfram »** |

⚠️ **Conséquence sur D5** (licence claire comme différenciateur) : ce différenciateur **ne peut pas
être tenu** tant que le registre comporte quatre points ouverts.

---

## 3. Le risque stratégique central

| Gravité | 🔴 haute |
|---|---|
| **Nature** | ⚠️ **risque partiellement vérifié** |

✅ Source : `A9-synthese-differenciateurs.md` §4, confirmé par `A10`.

**Tous les sept différenciateurs sont des centres de coût, et aucun des 27 acteurs étudiés ne les
engage.** Deux explications s'opposent :

1. **personne n'a voulu payer** → la place est libre, la thèse tient ;
2. **le marché ne valorise pas ces attributs** → la place est libre *parce qu'elle ne vaut rien*.

**L'étude de demande a tranché partiellement, et pas dans le sens favorable :**

| Différenciateur | Verdict |
|---|---|
| D3, D4, D5 | ✅ hypothèse 1 — demande établie et mesurée |
| **D1, D2** | ⚠️ **hypothèse 2 non réfutée** — aucune demande observable trouvée |
| D6, D7 | la demande est réelle mais porte sur autre chose |

⚠️ **Conséquence : D1 et D2 — les deux différenciateurs les plus identitaires du projet — doivent
être assumés comme une exigence de rigueur, pas présentés comme un avantage concurrentiel.**

**Ce qu'il faut pour lever le risque :** un choix explicite du porteur entre les deux voies
décrites dans `08-ROADMAP-AND-NEXT-STEPS.md` §7.

---

## 4. Les risques ouverts de la Phase 2

✅ Source : `A9-rapport-fin-de-phase-2.md` §9. ⚠️ **Attention au piège de numérotation** : le
rapport numérote **séparément** les risques (§9) et les recommandations (§10). **R1 ne désigne pas
la même ligne selon la table.**

| # | Risque | Gravité |
|---|---|---|
| **R1** | La couche de preuve est un centre de coût **sans demande mesurée** | 🔴 **élevée** |
| **R2** | Les deux audiences du cahier des charges **peuvent ne pas se recouvrir** | 🟠 moyenne |
| **R3** | L'aptitude à l'IA est peut-être **un effet de mode 2026** | 🟠 moyenne |
| **R4** | Quatre points juridiques ouverts, dont un conflit documenté chez Shaders | 🔴 **élevée** |
| **R5** | Le corpus source n'a pas de licence — **la base de Mathemirum n'est pas établie** | 🔴 **élevée** |
| **R6** | Les cases `?` de la matrice peuvent être lues comme des absences | 🟢 faible |

---

## 5. Incohérence : D et J dans le lot 1

| Gravité | 🟠 moyenne |
|---|---|
| **Nature** | ❌ **incohérence avérée, non tranchée** |

| Source | Ce qu'elle dit |
|---|---|
| `A6-plan-phase-1.md` §4 | le lot 1 couvre « **K · D · I · L · N** » |
| `CLOTURE-CHANTIER.md` §2 | les cinq documents **effectivement restaurés** sont « **K, L, I, N, J** » |

| Document | Fiche | Restauration |
|---|---|---|
| **D** — Géométrie computationnelle | ✅ **faite** | ❌ **rien** — 0 bloc display, aplatissement intégral → renvoyé au lot 4 |
| **J** — Optimisation | ❌ **aucune** | ✅ **232 restitutions** |

⚠️ **Ce n'est pas à l'agent de corriger cela silencieusement.** C'est une décision du porteur :
soit le plan A6 est corrigé pour nommer J, soit une fiche de J est produite.

---

## 6. Risque : les 843 restaurations ne sont pas validées une à une

| Gravité | 🟠 moyenne |
|---|---|
| **Nature** | ⚠️ **constat, pas objection** |

- ⚠️ **Aucune des 843 restitutions n'a été validée bloc par bloc** par le porteur. Elles portent
  chacune un niveau de confiance ; certaines sont *moyennes*.
- ⚠️ **C'est une reconstruction, pas une récupération.** Les arguments LaTeX détruits n'existent
  nulle part. Ce qui est écrit est une **proposition argumentée**, jamais le texte d'origine.

**Atténuation apportée par le dispositif :** les trois règles du moteur
(`03-TECHNICAL-ARCHITECTURE.md` §4.2) — unicité, **non-perte**, vérifiabilité — et le marquage
systématique des fragments non rattachés. Un fragment dont la destination n'est pas établie **reste
dans le document et est signalé**, jamais supprimé.

---

## 7. Risque d'environnement : les réinitialisations du sandbox

| Gravité | 🟠 moyenne — ⚠️ **récurrent, 7 occurrences** |
|---|---|
| **Nature** | ❌ **avéré, et il se reproduira** |

Le `.git` local et `/home/user/_audit/` (clone du corpus, sauvegardes) peuvent disparaître à chaque
tour. À chaque fois, `git log` local retombe à `bdba473 first commit`.

**Atténuation :** `tools/restauration/reconstituer_atelier.sh` — idempotent, éprouvé sept fois.
✅ Vérifié le 2026-11-11 : `17/17`, `6/6`, mojibake `0`, **A = 78 756**.

⚠️ **Conséquence pratique, à répéter :** tout livrable doit être commité dans le dépôt. Ce qui
reste dans `/home/user/_audit/` est par nature provisoire. `/tmp` ne survit pas.

---

## 8. Problèmes techniques de l'outillage

| # | Problème | Gravité | Conséquence |
|---:|---|---|---|
| 1 | ⚠️ **Aucun test automatisé** des 30 scripts | 🟠 moyenne | la non-régression repose sur la relecture |
| 2 | ⚠️ **Chemins absolus codés en dur** (`/home/user/_audit/connaissance`) | 🟠 moyenne | l'outillage ne fonctionne que dans ce sandbox |
| 3 | ⚠️ **Ordre d'application manuel** des 23 diffs | 🔴 **haute** | un ordre faux corrompt le corpus reconstitué |
| 4 | ⚠️ Les 6 lots de A sont **incrémentaux** : `domaine-A-lot2..6.gitdiff` **échouent** légitimement `git apply --check` sur un clone vierge | 🟠 moyenne | ⚠️ ce n'est pas un bug : appliquer 1→6 dans l'ordre |
| 5 | ⚠️ Aucune gestion de version de schéma des journaux JSON | 🟢 faible | pas de rétro-compatibilité par construction |
| 6 | 🔶 Deux moteurs concurrents (`apply_patch.py`, `lot_commun.py`) | 🟢 faible | justifié par la différence de nature des régimes |

---

## 9. Limites de l'environnement

| Limite | Conséquence |
|---|---|
| ❌ **Pas de GPU** | aucune mesure de performance réelle possible → D4 devra être déporté |
| ❌ **Pas de navigateur** | ⚠️ **aucune plateforme étudiée n'a été vue fonctionner**. Leurs qualités visuelles n'ont jamais été évaluées |
| ⚠️ Réseau restreint à 6 hôtes | `curl` direct bloqué vers la plupart des sites ; `fetch_page` requis |
| ⚠️ `git push` refusé (403) sur le dépôt de connaissances | le porteur applique les diffs lui-même — c'est une décision, pas un bug |

---

## 10. Incohérences et corrections internes assumées

Le projet a corrigé publiquement plusieurs de ses propres chiffres. ⚠️ **Reprendre un ancien chiffre
serait une erreur.**

| Ancien chiffre | Correction |
|---|---|
| « 12 emplacements vides » sur A | ❌ faux — le chiffre réel est **30** |
| « 100 % de défauts » sur E, R, S, U | ❌ faux — artefacts d'échappement ; taux réel **31,4 %** |
| « 41 lignes à runs » pour C | ❌ faux — **62**. B = 52, D = 67 |
| « 1 137 blocs » sans règle | ⚠️ exact **sous la règle `\[` en début de ligne** ; 1 146 avec la règle large |
| P non assigné à un lot | ❌ lacune du plan, **corrigée** le 2026-10-21 |

---

## 11. Ce qui n'a jamais été vérifié

⚠️ Liste explicite des angles morts. Ces éléments ne sont **ni confirmés ni réfutés**.

| Élément | Statut |
|---|---|
| ❓ Les registres de marques (INPI, EUIPO, USPTO) pour `mathemirum` | **non consultés** — hors portée technique |
| ❓ Le cahier des charges originel | **non retrouvé** dans le dépôt ; connu par citation indirecte |
| ❓ La qualité visuelle réelle des plateformes étudiées | **jamais observée** — pas de navigateur |
| ❓ Les performances réelles de quoi que ce soit | **jamais mesurées** — pas de GPU |
| ❓ L'existence d'une demande pour D1 et D2 | ⚠️ **recherche ciblée négative**, indice faiblement défavorable, **pas une preuve d'absence** |
| ❓ Le contenu des documents non encore audités (23 sur 29) | **non lu** |
| ❓ Les deux audiences du cahier des charges se recouvrent-elles ? | **non tranché** (risque R2) |
| ❓ Quatre points de licence | **en attente des éditeurs** |
| ❓ L'orthographe du nom (`MATHIRUM` apparaît une fois dans un prompt de continuité) | ⚠️ signalé ; la forme retenue est **MATHEMIRUM** |
