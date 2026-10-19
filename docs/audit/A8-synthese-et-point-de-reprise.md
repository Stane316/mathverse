# A8 — SYNTHÈSE ET POINT DE REPRISE

**Identifiant :** A8 · **Date :** 2026-10-18 · **Statut :** en revue
**Objet :** état vérifié du travail accompli, lacunes restantes, point de reprise pour la
continuation de la phase 1 et l'engagement de la phase 2.
**Auteur :** agent (Arena) · **Validation :** requise

---

## 1. Méthode de cette synthèse

Chaque affirmation ci-dessous a été **revérifiée sur le dépôt de travail le 2026-10-18**, avant
rédaction : `git log`, `git status`, présence des fichiers, et rejeu de l'outil d'inventaire sur
le clone de connaissances. Les chiffres cités sont donc des mesures du jour, pas des reprises
d'une note antérieure.

Sont distingués, conformément aux règles du projet : **faits vérifiés**, **déductions**,
**hypothèses**, **décisions validées**, **recommandations non validées**.

## 2. Le nom

| Élément | État |
|---|---|
| Nom de travail retenu | `mathemirum` (latin *mathematica* + *mirum*) |
| Décision | consignée dans `docs/decisions/0001-nom-de-travail-mathemirum.md` |
| Vérifications | npm (`mathemirum`, `mathemirum-core`, `create-mathemirum`), PyPI, GitHub : libres ; 0 homonyme ; 0 occurrence indexée |
| Limite connue | **aucun registre de marques consulté** — hors portée technique de l'environnement |
| Anciens noms dans les documents | **aucune occurrence** de l'ancien nom provisoire (`mathauma`) dans `docs/`. `mathverse` n'apparaît que comme **nom du dépôt**, jamais comme nom de produit |
| Point à trancher | le prompt de continuité écrit « MATHIRUM » dans le titre de sa section 2 et « Mathirum » une fois ; l'orthographe retenue jusqu'ici est **MATHEMIRUM** |

Recommandation : conserver **Mathemirum**, et ne pas introduire de variante. Le nom ne doit pas
être figé dans le code avant la phase 5 ; les documents d'audit emploient le neutre « le projet ».

## 3. Travaux réalisés — faits vérifiés

### 3.1 Phase 0 (terminée, commit `c1f035d`)

| Livrable | Contenu |
|---|---|
| `PHASE-0-rapport-audit-initial.md` | accès, périmètre, risques, 14 points exigés |
| `annexes/A0-inventaire-acces-et-preuves.md` | preuves d'accès, dates, limites de collecte |

Constats : les deux dépôts sont publics, sans LICENSE, sans README, à un seul commit. Le dépôt
produit ne contient que deux fichiers Markdown (~40 Kio) et 63 marqueurs `[web:n]` orphelins.

### 3.2 Nommage (terminé, commits `c1f035d` → `240d126`)

242 sondes de disponibilité, 175 noms libres, 58 éliminés par antériorité. Vagues documentées
dans A1, A3, A4, A5. Un jeu de repli est conservé si `mathemirum` devait être écarté.

### 3.3 Phase 1 — audit documentaire (en cours)

| Livrable | État | Contenu |
|---|---|---|
| `A2-inventaire-structurel.md` + annexes CSV/JSON | **terminé** | 29 documents, 80 330 lignes, 7 240 titres, 2 354 équations affichées |
| `A6-plan-phase-1.md` | **validé** | méthode, lots, ordre |
| `A7-integrite-des-equations.md` + annexe CSV | **terminé** (rectifié) | nature et étendue de la dégradation |
| `fiches/domaine-K-…md` | **terminée** | fiche 1 sur 29 |
| `fiches/domaine-L-analyse-numerique.md` | **terminée** | fiche 2 sur 29 — **rédigée sur le document restauré** (102 écritures appliquées) ; ordre d'entrelacement L → I → N → J |
| `fiches/domaine-D-geometrie-computationnelle.md` | **terminée** | fiche 3 sur 29 — document **non restauré** (chantier A–D) ; révèle un **troisième régime de dégradation** : formules aplaties en texte inline, variables conservées |
| `fiches/domaine-N-transformees.md` | **terminée** | fiche 4 sur 29 — **rédigée sur le document restauré** (lots 4a + 4b, 146 écritures) ; 3 941 lignes, 180 sections, 245 blocs ; **le plus directement exploitable du corpus** : pipeline web Microphone → Web Audio API → FFT → Canvas/WebGL (§109), mapping de `|X_k|` vers 8 attributs visuels (§111), fenêtrage comme paramètre réglable (§95). `navier` = 0, `CFL` = 0 — la famille 5 reste à sourcer hors corpus |
| Index notion → composant | **non commencé** | prévu par A6 §3.4 |

**Constats A2 (vérifiés, reproductibles par `tools/audit-phase1/extract_structure.py`) :**
2 354 équations affichées mais **0 bloc de code et 0 mathématiques en ligne `$…$`**. La chaîne
« modèle → équation → algorithme → implémentation → tests » s'arrête à l'algorithme : c'est la
couche manquante, et c'est là que se situe la différenciation possible du produit.

**Constats A7 (vérifiés, rectifiés le 2026-10-18) :** les commandes LaTeX ont été détruites
**avec leurs arguments**, ainsi que les lettres grecques. Taux mesuré : **31,4 %** des 2 306 blocs
qui sont de véritables équations (48 blocs d'échappement de crochets exclus du dénominateur).
Une affirmation antérieure (« 100 % de défauts » sur E, R, S, U) a été **rectifiée** : il
s'agissait d'artefacts d'échappement, sans défaut structurel.

### 3.4 Chantier de restauration (chantier parallèle, validé le 2026-10-18)

Décision du porteur : restaurer **tout le corpus**, pas seulement ce dont les premiers composants
ont besoin. Cadré par `docs/restauration/README.md` : c'est une **reconstruction**, pas une
récupération — le contenu détruit n'existe plus dans les fichiers.

| Lot | État | Résultat |
|---|---|---|
| K — lot 1 | **appliqué** | 19 blocs (14 haute, 5 moyenne) |
| K — lot 1 bis | **appliqué** | 11 blocs (10 découverts à la lecture + 1 tranché par vous) |
| L — lot 2 | **appliqué** | 91 blocs (58 haute, 29 moyenne, 4 corrections d'échappement) |
| L — 44 blocs inconnus | **en attente** | 10 candidats argumentés soumis (`domaine-L-blocs-a-trancher.md`) |

Mesure du jour sur le clone : **669 défauts signalés restants** (724 au départ), dont **24 dans L
et 0 dans K**.

## 4. Déductions et hypothèses

**Déduction (confirmée sur deux documents) :** l'inventaire automatique sous-estime fortement le
nombre réel de dégradations. Document K : +55 % de défauts découverts à la lecture (18 → 30).
Document L : **+115 %** (61 → 131). Le chiffre de 669 est donc un **plancher** ; le total réel se
situe probablement entre **1 000 et 1 300 blocs**, à confirmer document par document.

**Hypothèse (non vérifiée) :** la dégradation semble systématique sur certains types de sections
— les sections de synthèse (« SYNTHÈSE FINALE », « CE QU'IL FAUT ABSOLUMENT RETENIR ») présentent
le même bloc vide au même endroit dans plusieurs documents. Cela oriente la restaurationfuture
mais ne dispense pas de relire chaque document.

**Hypothèse (non vérifiée) :** les blocs d'affichage vides contenaient majoritairement des
**termes ou des chaînes de mots**, non des équations — d'où l'impossibilité de les reconstruire.
Appui : la « FORMULE MENTALE » du document N est une chaîne de phrases, celles de P et Q sont des
arbres ASCII ; aucune n'est une équation.

## 5. Décisions validées par le porteur

1. Nom de travail : `mathemirum` (et non `mathauma`).
2. Livrables d'audit : brouillons hors dépôt **et** versions validées commitées sur la branche de travail.
3. Phase 1 : **les 29 documents**, pas un échantillon.
4. Licence : stratégie **reportée après la phase 2**.
5. Restauration : **chantier global**, en parallèle de la phase 1.
6. Ordre des fiches du lot courant : **D, I, L, N**.
7. Application des restaurations : **branche dédiée du dépôt de connaissances, jamais de PR**, intégration par le porteur.
8. A, B, C, D : **aucune version antérieure n'existe** → reconstruction, lot placé en dernier.
9. Lots K et L : validés et appliqués ; les 4 artefacts d'échappement de L sont corrigés.

## 6. Recommandations non encore validées

| # | Recommandation | Statut |
|---|---|---|
| R1 | Passer à la phase 2 sans attendre les 28 fiches restantes, en gardant le lot D, I, L, N comme priorité | à valider |
| R2 | Adopter la structure de dossier documentaire proposée (§7 ci-dessous) | à valider |
| R3 | Créer 4 documents complémentaires (contrat de composant, stratégie de tests, benchmarking, exploration scientifique) en plus des 8 obligatoires | à valider |
| R4 | Maintenir le chantier de restauration en toile de fond, sans qu'il retarde les phases | à valider |
| R5 | Ne pas évaluer Supabase avant la phase 3 (le besoin réel de base de données n'est pas encore établi) | à valider |

## 7. Lacunes restantes en phase 1

1. **25 fiches sur 29** à produire (**K, L, D, N** existent). Le lot ordonné D → I → L → N est
   achevé à trois quarts : **reste I** (document déjà restauré — 204 écritures, 3 lots), puis
   l'ordre se poursuit sur J. I et N étant tous deux assainis, leurs fiches sont rédigeables
   sans attendre.
2. **Index notion → modèle → équation → paramètres → algorithme → moteur → composant → tests** :
   non commencé. C'est le livrable qui rend les fiches exploitables.
3. **Registre des équations à réécrire** : alimenté par A7, mais pas encore consolidé par domaine.
4. **Les 8 documents « Ai Technical Litteracy »** (lot 5 du plan A6) : non traités.
5. **A, B, C, D** : arborescence et équations détruites, méthode à définir (voie 2 confirmée).
6. **Blocs en attente de votre arbitrage** : 33 sur L, 28 sur I, 33 sur N — soit 94 blocs
   laissés en « contenu perdu » (fallback validé), tous intacts et complétables plus tard.
7. **Le décompte de 724 défauts est un plancher, pas un total** : sur N, 51 % des blocs
   restaurés n'étaient signalés par aucune heuristique (mesure directe, voir §3 du README
   de restauration).

## 8. Obstacles rencontrés

| Obstacle | Conséquence | Traitement |
|---|---|---|
| `git push` vers `my-own-connaissance` refusé (`403 denied`, puis `403 Resource not accessible by integration` sur l'API) | les restaurations ne peuvent pas être poussées | livraison en diffs vérifiés (`git apply --check`) + instructions d'application locale. **Aucune tentative de contournement** |
| Réinitialisation du sandbox en cours de séance (2 fois) | perte du clone et de l'état git local | tout livrable validé est commité immédiatement ; l'état a été restauré depuis l'origine sans perte |
| Pas de GPU ni de navigateur dans l'environnement | aucun benchmark WebGL/WebGPU possible ici | à déléguer à vos machines ou à une CI (à prévoir en phase 3) |
| Registres de marques inaccessibles | disponibilité du nom non vérifiée juridiquement | signalé, à traiter par vous avant toute publication |

## 9. Prochaines actions

1. Produire la fiche **I** (document restauré) — dernière du lot ordonné validé.
2. Alimenter l'index au fil des fiches.
3. Clôturer la phase 1 par un rapport au format des 14 points.
4. Engager la phase 2 (étude d'écosystème) selon la méthode du §10 de `A6`, enrichie des plateformes déjà identifiées.
5. Soumettre les documents du dossier de référence au fil des phases 2 et 3, avec un statut explicite chacun.

## 10. Références

- `docs/decisions/0001-nom-de-travail-mathemirum.md`
- `docs/audit/A2-inventaire-structurel.md`, `A6-plan-phase-1.md`, `A7-integrite-des-equations.md`
- `docs/restauration/README.md` (méthode, gouvernance), `propositions/domaine-K.md`,
  `propositions/domaine-L.md`, `propositions/domaine-L-blocs-a-trancher.md`
- Outils : `tools/audit-phase1/`, `tools/restauration/` (déterministes, sans réseau, aucune écriture dans la source)
