# A6 — PLAN DE LA PHASE 1 : AUDIT DOCUMENTAIRE

**Date :** 2026-10-18 — **Statut :** plan validé, exécution en cours
**Objet :** cadrer l'audit des 29 documents du dépôt de connaissances selon la méthode exigée (question, sources, preuves, critères, limites d'arrêt).

---

## 1. Question à résoudre

Que contient réellement la collection, qu'est-ce qui est utilisable pour produire des composants **explicables**, et où sont les lacunes ? Plus précisément :

1. Quelles notions sont réellement traitées, et à quelle profondeur ?
2. Pour chaque notion utile : le modèle est-il énoncé ? l'équation est-elle complète ? les paramètres sont-ils identifiés ? l'algorithme est-il décrit ? les hypothèses et limites sont-elles posées ?
3. Où le corpus est-il dégradé, et que faut-il réécrire avant de s'en servir ?
4. Quelles notions se prêtent à un composant, et lesquelles ne doivent pas être présentées comme des simulations ?

## 2. Sources

- **Source primaire :** clone en lecture seule de `Stane316/my-own-connaissance` (commit `f0f5e2d`), 29 documents, 80 330 lignes. Aucune autre source du dépôt n'est utilisée.
- **Sources secondaires :** uniquement pour vérifier une équation perdue ou une valeur de référence. Toute référence externe sera citée et datée ; aucune valeur ne sera reprise d'une source non citée.

## 3. Méthode

1. **Mesurer d'abord.** Comptages automatiques et reproductibles (`tools/extract_structure.py`, `tools/extract_domain.py`, `tools/check_equations2.py`) avant toute lecture : plan, volume, densité d'équations, intégrité du formalisme.
2. **Lire ensuite, de façon ciblée.** Les outils désignent les sections à lire ; la lecture porte sur ces sections, pas sur l'intégralité des 80 330 lignes.
3. **Une fiche par domaine**, modèle constant (10 sections, voir `fiches/domaine-K-…`).
4. **Un index unique**, alimenté au fil des fiches : notion → modèle → équations → paramètres → algorithme → moteur → rendu → composant potentiel → tests et validation, avec dépendances, source et niveau de maturité.
5. **Un registre des équations à réécrire**, alimenté par `A7`.
6. **Aucune modification du dépôt de connaissances** sans autorisation explicite.

## 4. Ordre de traitement et lots

| Lot | Domaines | Justification |
|---|---|---|
| **Lot 1** | **K** (fait) · D · I · L · N | couverture directe des cinq familles de composants prioritaires |
| **Lot 2** | C · G · J · M · O | socles transverses : algèbre linéaire, probabilités, optimisation, information, complexité |
| **Lot 3** | E · F · H · Q · R · S · U | apports indirects (graphes, combinatoire, statistiques, logiques) |
| **Lot 4** | A (maître) · B · C · D | **traitement spécial** : structure et équations détruites, méthode dédiée à définir |
| **Lot 5** | `Ai Technical Litteracy` 01–08 | périmètre décidé par vous : documents utiles au site, à la DX, à la performance et à l'accessibilité |

**Traitement spécial pour A, B, C, D :** ces quatre documents n'ont ni titres ni équations (103 à 133 lignes pour 58 à 82 Kio). Une lecture par extraction d'arborescence est impossible. Deux options, à trancher : (i) échantillonnage par blocs + reconstruction manuelle du plan ; (ii) recherche d'une version antérieure non dégradée auprès de vous (solution préférable si elle existe).

## 5. Éléments de preuve exigés pour chaque fiche

- Toute affirmation s'appuie sur un extrait situé (fichier + numéro de ligne) ou sur une mesure reproductible.
- Toute équation est classée : complète / partielle / perdue, avec la formule attendue quand elle est perdue.
- Tout ce qui n'a pas été lu est marqué ⚠️ ; tout ce qui est absent est marqué ❌. Aucune case n'est remplie par inférence silencieuse.

## 6. Critères de validation de la Phase 1

1. Les 21 domaines A–U disposent d'une fiche (T : fiche d'absence).
2. L'index couvre les cinq familles de composants prioritaires.
3. Chaque lacune est typée : absence, imprécision, incohérence, ou non-traçabilité.
4. Le registre des équations à réécrire est complet pour les notions retenues.
5. Aucune modification du dépôt de connaissances n'a été effectuée.
6. Les 8 documents de littératie technique sont traités selon le périmètre que vous avez fixé.

## 7. Critères d'arrêt

La Phase 1 s'arrête lorsque les critères ci-dessus sont satisfaits, **ou** lorsque les documents accessibles ont été épuisés, **ou** lorsqu'une limite d'accès empêche de progresser — avec, dans ce dernier cas, une liste explicite des inconnues restantes et de ce qui permettrait de les lever.

## 8. Limites connues d'emblée

- **Le formalisme est dégradé** (30,8 % des équations display incomplètes, 4 documents sans équation) : la Phase 1 dresse un état des lieux et un registre, elle ne répare pas.
- **Aucune vérification d'exactitude mathématique** n'est faite sur les équations complètes pendant cette phase : elle viendra notion par notion, au moment de construire les composants.
- **Le sandbox peut être réinitialisé** (incident du 2026-10-18) : tous les livrables validés sont donc commités dans `docs/audit/`, et les outils sont versionnés avec eux.
