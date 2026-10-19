# RAPPORT DE FIN DE PHASE 2 — ÉTUDE D'ÉCOSYSTÈME ET DE CONCURRENCE

**Établi le :** 2026-10-19 · **Format :** les 16 points du §16 du cahier des charges
**Phase ouverte le :** 2026-10-19, sur décision du porteur de réduire le périmètre du chantier de
restauration
**Statut :** livrables **établis** ; phase **non close** — trois points exigent votre approbation
(§16).

---

## 1. Résumé exécutif

La phase 2 a étudié **35 plateformes**, dont **11 en fiches détaillées** selon les 16 champs, et
produit **cinq livrables**. Elle a répondu à la question posée en ouverture, et la réponse est
double :

- **Sur l'offre :** aucune plateforme ne réunit les quatre attributs. Les deux plus proches —
  **Shaders** et **Math-To-Manim** — sont **complémentaires**, et leur complémentaire recouvre
  exactement la thèse de Mathemirum. La place est libre.
- **Sur la demande :** ⚠️ **la demande pour la couche de preuve n'est pas établie.** Elle l'est pour
  la documentation, la mesure et l'aptitude à l'IA. Elle ne l'est pour les équations et les
  hypothèses dans **aucune** des sources consultées.

**C'est le résultat à retenir, et il est moins confortable que ce que laissaient espérer les
premiers constats :** ce qui est libre n'est pas nécessairement ce qui est demandé.

Le résultat le plus durable de la phase est sans doute le **registre des licences** : 9 plateformes
sur 35 relèvent d'un régime fermé ou restrictif, dont les deux géants du secteur des composants
(React Bits, Aceternity UI), et **trois mécanismes de présentation trompeuse** ont été documentés.

## 2. Question posée à l'ouverture, et réponse

> *Existe-t-il déjà une plateforme réunissant composants visuels + explication mathématique +
> prompts + CLI, et quelles sont les places libres ?*

**Réponse sur les quatre attributs :** non, aucune. **Shaders** a les composants, les prompts et la
CLI — l'explication mathématique est son seul manque. **Math-To-Manim** a l'explication, les prompts
et la CLI — c'est la sortie composant qui lui manque.

⚠️ **Cette réponse ne vaut pas preuve d'absence.** Elle porte sur 35 plateformes observables et
quelques requêtes. Une plateforme non observée pourrait réunir les quatre.

**Réponse sur les places libres :** la matrice 18 attributs × 27 plateformes montre que **la ligne
de partage ne passe pas entre le visuel et le mathématique, mais entre la mise à disposition et la
preuve.** Tout ce qui relève de la mise à disposition est couvert partout ; tout ce qui relève de la
preuve est vide. Deux cases extrêmes : les *équations et hypothèses*, vides **sans une seule
exception**, et les *limites connues*, la case la plus vide de la matrice.

## 3. Périmètre effectivement traité

| Famille | Plateformes | Dont fiches détaillées |
|---|---:|---:|
| Bibliothèques de composants web | 9 | F01, F02, F04, F05 |
| Moteurs et bibliothèques mathématiques | 10 | — |
| Génération par IA | 7 | F03 |
| Services fermés | 5 | F06, F07, F09 |
| Shaders et écosystème | 4 | F08, F11 |
| **Total** | **35** | **11 fiches** |

Non traités : Shaders approfondi (Paper Shaders, OpenShaders), GLSL Sandbox au-delà d'une source
indirecte.

## 4. Ressources et sources examinées

API publique GitHub (métadonnées et contenus de fichiers), pages publiques de licence et de
conditions des éditeurs, recherche web générale. **Aucun contournement d'accès, aucune extraction
de contenu privé, aucun secret.** Voir `annexes/A9-registre-plateformes.md` §6 pour le détail des
requêtes et la consommation du quota.

## 5. Méthode

Celle du §13.2 du rapport de phase 0, appliquée sans modification : `fetch_page` pour le parcours,
API GitHub pour les faits observables, clone **uniquement** si le dépôt est public **et** la licence
perméable, `web_search` pour le reste. Règle de preuve de A6 §5 : toute affirmation s'appuie sur une
mesure ou un extrait situé ; ce qui n'est pas lu est marqué ⚠️ ; ce qui est absent ❌ ; **aucune case
n'est remplie par inférence silencieuse.**

## 6. Résultats vérifiés

1. **Aucune plateforme ne réunit les quatre attributs** (§2).
2. **Sur 35 plateformes, 9 sont sous régime fermé ou restrictif** — React Bits (MIT + Commons
   Clause), Aceternity (propriétaire), Shadertoy (CC BY-NC-SA par défaut), GeoGebra (4 régimes),
   Desmos (non commercial), Wolfram (propriétaire), CoCalc (**MS-RSL**, lecture seule), GLSL Sandbox
   (rien par défaut), MathVerse/sadeepas (aucune licence).
3. **Trois mécanismes de présentation trompeuse documentés** : le titre de licence qui rassure,
   l'agrégateur qui répète sans vérifier, le dépôt public sans licence.
4. **Une seule plateforme du secteur est ouverte, massive et sans restriction de redistribution :
   shadcn/ui (MIT).** La couche infrastructurelle est libre ; la couche catalogue ne l'est pas.
5. **Rectification d'une affirmation de la phase 0** : React Bits ne construit pas son registre avec
   shadcn, mais avec **jsrepo** et l'adaptateur `@jsrepo/shadcn`.
6. **Le corpus d'effets le plus riche du secteur (Shadertoy) est fermé par défaut** — CC BY-NC-SA,
   non commercial et viral, la plupart des auteurs ne déclarant rien.
7. **Une clause de co-propriété des productions** chez GeoGebra restreint l'usage commercial de toute
   figure qui en provient.
8. **La documentation est le premier critère de choix** d'un paquet (93 % d'accord), et **l'aptitude
   à l'IA** est un critère apparu en 2026.

## 7. Hypothèses et inférences

⚠️ Toutes sont des hypothèses, aucune n'est un fait établi.

- **H1** — La ligne de partage passe entre la mise à disposition et la preuve, non entre le visuel et
  le mathématique. *(Corrige l'hypothèse initiale de A9 §8.1.)*
- **H2** — L'aptitude à l'IA est le meilleur cheval de Troie de la couche de preuve : c'est le seul
  critère émergent, et c'est par lui que des équations *structurées* prennent de la valeur.
- **H3** ⚠️ — Les deux audiences (composants web / apprentissage des shaders) **peuvent ne pas se
  recouvrir**. Le discours « comprendre plutôt que copier » est vif dans la seconde, absent de la
  première. **Rien n'indique le contraire.**
- **H4** ⚠️ — Pour D1 (équations et hypothèses) et D2 (classement tripartite), l'hypothèse
  « le marché ne valorise pas » **n'est pas réfutée**.

## 8. Lacunes et points non vérifiés

⚠️ Liste longue.

- **Aucune plateforme installée ni exécutée** : ni GPU ni navigateur dans cet environnement. Toute
  affirmation de performance adverse est reprise, non vérifiée.
- **Aucune vérification juridique.** Aucun registre de marques consulté.
- **Licences par élément non vérifiées** sur les plateformes contributives (Uiverse, Shadertoy,
  OpenShaders, GLSL Sandbox).
- **GLSL Sandbox** repose sur une source indirecte.
- **Paper Shaders et OpenShaders** : découverts, non étudiés.
- **Étude de demande : première passe** — trois requêtes, sources majoritairement éditoriales, aucun
  volume de recherche, aucune disposition à payer.
- **Les tarifs** n'ont pas été vérifiés et ne figurent dans aucun livrable.

## 9. Risques

| # | Risque | Gravité |
|---|---|---|
| **R1** | La couche de preuve est un centre de coût **sans demande mesurée** (D1, D2) | **élevée** |
| **R2** | Les deux audiences peuvent ne pas se recouvrir (H3) | moyenne |
| **R3** | L'aptitude à l'IA est peut-être un effet de mode 2026 | moyenne |
| **R4** | Quatre points juridiques ouverts, dont un conflit documenté chez Shaders | **élevée** |
| **R5** | Le corpus source n'a pas de licence — la base de Mathemirum n'est pas établie | **élevée** |
| **R6** | Les cases `?` de la matrice peuvent être lues comme des absences | faible |

## 10. Recommandations argumentées

| # | Recommandation | Impact | Urgence | Coût | Risque | Dépendance |
|---|---|---|---|---|---|---|
| **R3.1** | Présenter la couche de preuve par ses bénéfices observés, jamais comme argument premier | **élevé** | **haute** | faible | faible | aucune |
| **R3.2** | Faire de l'aptitude à l'IA le cheval de Troie (`llms.txt`, champs structurés, MCP) | **élevé** | **haute** | moyen | **moyen** | D1, D3 |
| **R7** | Vérifier Paper Shaders (Apache 2.0) et OpenShaders (MIT) | **élevé** | moyenne | faible | faible | aucune |
| **R1** | Lever les quatre points ouverts du registre des licences | **élevé** | **haute** | faible | moyen | éditeurs |
| **R3.3** | Compléter l'étude de demande | **élevé** | moyenne | moyen | faible | aucune |
| **R3.4** | Instrumenter dès le premier composant | **élevé** | moyenne | faible | faible | aucun composant |

## 11. Inventaire des livrables

| # | Livrable | Fichier | Statut |
|---|---|---|---|
| 1 | Registre des plateformes | `annexes/A9-registre-plateformes.md` | ✅ 35 plateformes |
| 2 | Fiches détaillées (16 champs) | `fiches-phase-2/F01` → `F11` | ✅ 11 fiches |
| 3 | Comparaison transversale | `annexes/A9-comparaison-transversale.md` | ✅ 18 × 27 |
| 4 | Synthèse des différenciateurs | `annexes/A9-synthese-differenciateurs.md` | ✅ **révisée** |
| 5 | Registre des licences | `annexes/A9-registre-des-licences.md` | ✅ 35 plateformes, 4 statuts |
| — | Étude de demande (R3) | `A10-etude-de-demande.md` | ⚠️ première passe |
| — | Licence du corpus source | `../decisions/0002-licence-du-corpus-source.md` | ⚠️ **proposition soumise** |
| — | Plan et suivi | `A9-plan-phase-2.md` | ✅ |

## 12. Critères de validation — verdict

Les cinq livrables de A9 §6 sont **établis**. ⚠️ **Deux réserves empêchent de déclarer la phase
close :**

1. **R3 n'est qu'une première passe**, et ses résultats ont **invalidé une partie de la synthèse des
   différenciateurs** — ce qui montre que la clôture prématurée aurait figé une affirmation fausse.
2. **Quatre points juridiques restent ouverts**, dont un conflit documenté.

**Verdict : livrables complets, phase non close.**

## 13. Fichiers créés ou modifiés

15 fichiers : 11 fiches, 4 annexes/livrables, le plan A9, l'étude A10, la décision 0002 ; A8 §9
corrigé (section périmée).

## 14. Tests exécutés et résultats

Aucun test automatisé. Requêtes API GitHub (limite de débit respectée), lectures de pages
publiques, trois requêtes de recherche. **Aucune plateforme installée ni exécutée.**

## 15. Prochaine étape

Décision du porteur du 2026-10-19 : **reprendre la phase 1** — 24 fiches, 15 documents à instruire
**dans l'ordre A → U**, puis les 8 documents de littératie.

Préalable technique : le clone du dépôt de connaissances a été détruit par une réinitialisation du
sandbox. La reprise exigera de **recloner puis réappliquer les 17 diffs** selon la procédure de
`../restauration/CLOTURE-CHANTIER.md` §6 — ce qui valid du même coup cette procédure, jamais encore
éprouvée.

## 16. Points exigeant votre approbation

1. **La licence du corpus source** — proposition `CC BY 4.0` en `../decisions/0002`. ⚠️ Je ne peux
   pas l'appliquer (push refusé, 403 ; aucun contournement tenté). **Sans votre dépôt du fichier, la
   base juridique de Mathemirum reste non établie.**
2. **L'investissement dans D1 et D2 sachant que leur demande n'est pas établie.** C'est le choix que
   vous aviez renvoyé à l'étude de demande ; l'étude répond « *adjacente, pas directe* ». **Il faut
   maintenant décider : investir au nom de la rigueur, ou conditionner.**
3. **Les quatre points ouverts du registre des licences**, dont la confirmation écrite à demander à
   Shader Effects.
