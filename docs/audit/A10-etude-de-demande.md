# A10 — ÉTUDE DE DEMANDE (recommandation R3, phase 2)

**Date :** 2026-10-19 · **Statut :** **première passe**, à compléter
**Objet :** instruire la question que la synthèse des différenciateurs a laissée ouverte —
*les sept différenciateurs sont tous des centres de coût que personne n'engage : est-ce parce que
personne n'a voulu payer, ou parce que le marché ne les valorise pas ?*

---

## 1. Résumé exécutif

**Le résultat est nuancé, et il n'est pas celui qu'on espérait.**

- ✅ **La documentation est le premier critère de choix** d'un paquet, mesuré à 93 % d'accord dans
  une étude universitaire sur la sélection de paquets npm. Ce n'est pas une opinion.
- ✅ **« L'aptitude à l'IA » est un critère de choix apparu en 2026** : serveur MCP, `llms.txt`,
  documentation lisible par un assistant. Plusieurs sources le traitent comme un critère à part
  entière.
- ✅ **La douleur numéro un des développeurs de shaders est le débogage et le profilage**, pas le
  manque d'effets (enquête Khronos 2026, 400+ répondants).
- ❌ **Mais aucun des ~20 guides de choix de bibliothèque de composants consultés ne mentionne
  l'explication mathématique, les équations, les hypothèses ou le domaine de validité** comme
  critère de sélection. Pas un seul.

**Conclusion provisoire :** la demande pour la couche de preuve est **adjacente et indirecte, pas
directe**. Elle existe dans le discours (les gens se plaignent de copier sans comprendre) et dans
des critères voisins (documentation, IA), mais **elle n'existe pas comme critère de choix formulé**.

**Le levier le plus solide n'est donc pas la preuve pour elle-même, mais la preuve rendue lisible
par une machine** : c'est là qu'elle rencontre un critère de choix observé en 2026.

⚠️ **Ce résultat est une première passe**, fondée sur trois requêtes et des sources secondaires. Il
ne clôt pas la question — il la déplace.

## 2. Périmètre effectivement traité

Trois questions, et rien de plus :

1. La documentation est-elle un critère de choix mesuré ?
2. Existe-t-il une demande observable pour la *compréhension* (par opposition au copiage) ?
3. L'explication mathématique apparaît-elle comme critère de choix quelque part ?

**Hors périmètre :** volumes de recherche, taille de marché, disposition à payer, analyse de la
concurrence directe (déjà traitée en A9). Ces points restent ouverts.

## 3. Ressources et sources examinées

| Source | Nature | Date |
|---|---|---|
| Enquête Khronos sur l'écosystème des shaders 2026 | enquête, **400+ répondants**, 16 juin – 10 juillet 2026 | publiée 2026-07-21 |
| Étude Concordia sur la sélection de paquets npm | étude universitaire à grande échelle | consultée 2026-10-19 |
| ~20 guides de choix de bibliothèques de composants (2026) | sources éditoriales et professionnelles | 2026-01 à 2026-10 |
| Discours communautaire sur l'apprentissage des shaders | forums, cours, articles | 2010 à 2026 |

⚠️ **Limite de méthode :** ce sont des **sources secondaires et éditoriales**, sauf l'enquête Khronos
et l'étude Concordia qui sont primaires. Les guides de choix sont des contenus de marketing
éditorial — ils décrivent ce que les rédacteurs estiment important, pas nécessairement ce que les
développeurs font.

## 4. Méthode

Recherche web ciblée sur trois axes, puis confrontation des résultats aux sept différenciateurs de
`A9-synthese-differenciateurs.md`. Chaque signal est classé : **favorable**, **défavorable**, ou
**non concluant**. Aucun signal n'est retenu sans source datée.

## 5. Résultats vérifiés

### 5.1 ✅ La documentation est le premier critère — mesuré

Étude Concordia sur la sélection de paquets npm : « Developers look for packages that are
**well-documented**, receive a high number of stars, have a large number of downloads, and do not
suffer from security vulnerabilities. **Documentation was the most important factor.** In fact,
**93 % of the responses agreed** that the GitHub repository of an npm package should have some form
of documentation. »

Ce signal est **favorable aux différenciateurs D1, D3 et D4**, mais avec une réserve décisive :
⚠️ « documentation » dans cette étude désigne de la documentation générale, **pas** des équations et
des hypothèses. **Ne pas surinterpréter.**

### 5.2 ✅ « L'aptitude à l'IA » est un critère apparu en 2026

- *Telerik (2026-09-14)* : « Does the library offer an **official MCP server, llms.txt
  documentation** or AI-powered tooling that helps coding assistants generate correct, current
  code ? »
- *DreamHost (2026-08-25)* : « New for 2026 : how well a library works with **AI coding assistants
  like Cursor, Claude Code, and v0 is a real selection criterion**. Copy-paste libraries have an
  edge here because the component code lives in your own repository, where an assistant can read and
  modify it. »
- shadcn/ui se présente lui-même comme « AI-ready », avec du code ouvert « for LLMs to read,
  understand, and improve ».

Ce signal est **favorable à D7** (boucle prompt → composant → test) **et, de façon moins évidente, à
D1 et D3** : des équations et des limites *structurées* sont précisément ce qu'un assistant peut
lire pour générer du code correct. **C'est le pont le plus solide entre la couche de preuve et un
critère de choix observé.**

### 5.3 ✅ La première douleur des développeurs de shaders est le débogage, pas le manque d'effets

Enquête Khronos 2026 (400+ répondants) :
- **le débogage et le profilage des shaders sont la douleur numéro un**, cités par 53 % comme un
  problème du top 3 (score moyen de douleur 52/100) ;
- **40 %** des répondants situent leur douleur de débogage dans la plage haute (61–100), dont 13 au
  maximum absolu ;
- **64 %** consacrent un effort à adapter des shaders entre plateformes, API ou outils ; ~10 % y
  voient l'un de leurs plus gros coûts d'ingénierie ;
- Linux à 74 % — **une base de développeurs qui dépasse largement le jeu vidéo**.

Ce signal est **favorable à D4** (mesures de performance) et, indirectement, à D1 : un développeur
qui souffre de débogage a besoin de **comprendre**, pas d'un effet de plus.

### 5.4 ❌ Aucun guide de choix ne mentionne l'explication mathématique

Sur une vingtaine de guides de sélection de bibliothèques de composants publiés en 2026, les
critères récurrents sont :

| Critère | Fréquence |
|---|---|
| Accessibilité (WCAG 2.2) | quasi systématique — « *baseline requirement* » |
| Personnalisation et thématisation | quasi systématique |
| Documentation | quasi systématique |
| Taille du paquet et performance | systématique |
| TypeScript | systématique |
| Compatibilité SSR / Next.js / RSC | fréquente |
| Signaux de maintenance | fréquente |
| **Aptitude à l'IA (MCP, llms.txt)** | **émerge en 2026** |
| **Explication mathématique / équations / hypothèses / domaine de validité** | **❌ AUCUNE OCCURRENCE** |

**C'est le résultat le plus important de cette étude, et il est défavorable.** La couche de preuve
n'est pas un critère de choix formulé nulle part.

### 5.5 ✅ Le discours « copier sans comprendre » est ancien et récurrent

- *r/gamedev (2018)* : « Shaders are voodoo black magic. Change my mind. »
- *polycount (2010)* : « pure shader programmer artists also tend to just copy paste bits without
  understanding the math. »
- Cours et tutoriels 2026 : « **Stop blindly copying shader nodes!** Learn the core math behind game
  shaders » ; « stop downloading someone else's materials and start building your own ».
- *GDQuest* : « you should always type the shader yourself (don't just copy and paste) ».

⚠️ **Signal favorable mais faible.** Ce discours est ancien, récurrent, et **situé dans la sphère
 jeu vidéo / apprentissage des shaders — pas dans celle des bibliothèques de composants web.** Rien
 ne prouve que l'audience des composants React partage cette frustration.

## 6. Hypothèses et inférences

⚠️ **Ce qui suit est une inférence, pas un résultat.**

**H1 — La couche de preuve a une demande indirecte, pas directe.** Les développeurs ne cherchent pas
des équations ; ils cherchent de la documentation, de la performance prévisible et la capacité à
déboguer. **La couche de preuve est un moyen de satisfaire ces trois besoins, pas un besoin en
soi.** Si cette lecture est juste, la présentation compte autant que le fond : vendre des équations
ne marchera pas ; vendre *« un composant que votre équipe peut déboguer et que votre assistant peut
comprendre »* s'appuie sur des critères observés.

**H2 — L'aptitude à l'IA est le meilleur cheval de Troie.** C'est le seul critère émergent en 2026,
et c'est précisément celui par lequel des équations et des limites **structurées** prennent de la
valeur : un assistant qui lit les hypothèses et le domaine de validité génère du code plus sûr.

**H3 — Le marché des composants et celui de l'apprentissage des shaders sont deux marchés.** Le
discours « comprendre plutôt que copier » est vif dans le second, absent du premier. ⚠️ **Rien
n'indique qu'ils se recouvrent**, et supposer le contraire serait une erreur coûteuse.

## 7. Lacunes et points non vérifiés

⚠️ Liste longue, et c'est le signe que cette étude est une **première passe** :

- **Aucun volume de recherche mesuré** (tendances de recherche inaccessibles depuis cet
  environnement).
- **Aucune disposition à payer évaluée.**
- **Aucune donnée sur l'audience réelle** des bibliothèques de composants vs celle des contenus
  d'apprentissage mathématique.
- **Les sources éditoriales ne sont pas des données de comportement** : elles disent ce que les
  rédacteurs jugent important.
- **L'étude Concordia mesure la documentation en général**, pas la documentation mathématique.
- **Aucun entretien utilisateur**, aucun sondage propre.
- **Les chiffres npm sont connus pour être gonflés par l'intégration continue** — les sources
  elles-mêmes le signalent explicitement.

## 8. Risques et décisions à prendre

| # | Risque | Décision à prendre |
|---|---|---|
| **R1** | La couche de preuve est un centre de coût **sans demande mesurée** | Investir quand même au nom de l'exigence de rigueur, ou conditionner l'investissement à des signaux supplémentaires ? |
| **R2** | Les deux audiences (composants / apprentissage) peuvent ne pas se recouvrir | Cibler l'une, l'autre, ou les deux ? |
| **R3** | « Aptitude à l'IA » est peut-être une mode de 2026 | Construire dessus suppose d'accepter ce risque de cycle |

## 9. Recommandations argumentées

Classées selon les critères du §15 du cahier des charges : **impact, urgence, coût, risque,
dépendance**.

| # | Recommandation | Impact | Urgence | Coût | Risque | Dépendance |
|---|---|---|---|---|---|---|
| **R3.1** | **Présenter la couche de preuve par ses bénéfices observés**, pas par son contenu : « débogable », « mesuré », « compréhensible par un assistant » — jamais « documenté mathématiquement » comme argument premier | **élevé** | **haute** | faible | faible | aucune |
| **R3.2** | **Faire de l'aptitude à l'IA le cheval de Troie** : publier `llms.txt`, structurer équations/hypothèses/limites pour qu'une machine les lise, fournir un serveur MCP | **élevé** | **haute** | moyen | **moyen** (cycle de mode) | D1, D3 |
| **R3.3** | **Compléter cette étude** avant d'investir lourdement : volumes de recherche, taille des audiences, disposition à payer | **élevé** | moyenne | moyen | faible | aucune |
| **R3.4** | **Instrumenter dès le premier composant** : mesurer ce que les utilisateurs lisent réellement (la page d'équations est-elle consultée ?) — c'est la seule donnée de demande qu'un projet peut produire lui-même | **élevé** | moyenne | faible | faible | aucun composant publié |
| **R3.5** | Ne pas construire sur l'hypothèse que les deux audiences se recouvrent sans la tester | moyen | moyenne | faible | faible | R3.3 |

## 10. Critères de validation de cette étude

Cette première passe sera considérée comme suffisante lorsque : au moins une source de volume de
recherche aura été consultée ; les deux audiences auront été comparées sur une donnée observable ;
et la recommandation R3.4 aura été traduite en instrumentation concrète.

## 11. Fichiers créés ou modifiés

- `docs/audit/A10-etude-de-demande.md` — le présent document
- `docs/audit/A9-plan-phase-2.md` — R3 marquée « engagée », résultats résumés

## 12. Tests exécutés et résultats

Aucun test automatisé. Trois requêtes de recherche, neuf sources retenues, confrontation aux sept
différenciateurs. Aucune plateforme installée ni exécutée.

## 13. Prochaine étape

Compléter l'étude (R3.3) puis **revenir sur la synthèse des différenciateurs** pour la réviser à la
lumière de ce résultat : les sept différenciateurs y sont présentés comme des atouts, alors que
**leur demande n'est établie que pour trois d'entre eux** (documentation, IA, mesure).

## 14. Points exigeant votre approbation

1. **Investir dans la couche de preuve sans demande directe mesurée** — c'est la question que vous
   avez renvoyée à cette étude, et l'étude n'y répond pas par oui : elle répond « *la demande est
   adjacente, et elle passe par l'IA et la documentation* ».
2. **Compléter l'étude ou s'en tenir là** — les lacunes du §7 sont nombreuses.
3. **L'orientation par l'aptitude à l'IA** (R3.2) suppose d'accepter un risque de cycle de mode.
