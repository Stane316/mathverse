# F04 — ACETERNITY UI

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** API GitHub, pages publiques du site officiel, recherche web
**Motif de cette fiche :** la licence annoncée partout comme « MIT » est **contredite par la page
de licence officielle** de l'éditeur.

---

## 1. Présentation et positionnement

« Composants animés gratuits pour React et Next.js. Copiez-collez des composants d'interface
construits avec Tailwind CSS et Motion : fonds, cartes, carrousels, effets de texte et éléments
3D. » Acteur majeur du secteur, aux côtés de React Bits et Magic UI. Built with **Next.js, React,
Tailwind CSS et Motion (ex-Framer Motion)**.

## 2. Fonctionnalités

- Composants animés : fonds, cartes, carrousels, effets de texte, éléments 3D.
- **Blocs et gabarits** : côté payant, des blocs et modèles de pages complets.
- **Accès MCP** (Model Context Protocol) pour Claude Code, Codex, Devin, Cursor — une
  intégration explicite aux assistants de code, y compris sur le palier gratuit.
- Copier-coller, sans installation de paquet.

⚠️ **Les volumes annoncés divergent fortement selon les sources** : le site officiel indique
« 100+ composants gratuits » sur sa page de tarifs ; d'autres pages du même site ou des tiers
avancent 70+, 89, 200+, ou « 278 composants indexés ». **Aucun de ces chiffres n'a été vérifié par
 comptage.** Voir §12.

## 3. Parcours utilisateur

Navigation → aperçu en direct → copie du code, ou installation par CLI (mentionnée par des tiers).
Le modèle est celui du copier-coller, identique dans son principe à shadcn/ui et React Bits.

## 4. Architecture technique observable

⚠️ **La bibliothèque de composants n'est pas publiée sur GitHub.** L'organisation `aceternity` ne
comporte que deux dépôts : `saasternity` (gabarit SaaS, 107 ★, actif jusqu'en 2024) et
`nextjs-boilerplate` (archivé). **Il n'existe donc pas de dépôt public de la bibliothèque
elle-même**, contrairement à React Bits et Magic UI.

Conséquence méthodologique : **l'architecture n'est pas observable**. Impossible d'inspecter le
versionnage, la structure des métadonnées ou le processus de contribution réel.

Un paquet npm `aceternity-ui` existe (licence MIT déclarée), mais sa **dernière publication remonte
à deux ans** : il n'est pas la voie de distribution actuelle.

## 5. Mode de distribution

Copier-coller depuis le site, assisté par CLI et par MCP. Palier gratuit + **All-Access payant en
paiement unique**. ⚠️ Les montants relevés varient selon les sources et les dates : 199 $, 249 $,
169 $/an, 1 590 $ en licence d'équipe. **Ces chiffres n'ont pas été vérifiés sur la page de tarifs
au jour de l'observation** — voir §12.

## 6. Prévisualisation et personnalisation

Aperçu en direct par composant ; personnalisation par le code copié et par la configuration
Tailwind. Des tiers signalent que chaque composant est présenté avec sa liste de dépendances avant
installation.

## 7. Stratégie documentaire

Site de documentation propre, exemples inclus. Une activité éditoriale notable : le site publie
des comparatifs (« alternatives à shadcn/ui ») et **déclare explicitement son absence de lien avec
shadcn/ui** — « Aceternity UI n'est pas un projet shadcn et n'a aucun lien avec lui ».

## 8. Modèle de contribution

⚠️ **Non observable.** Aucun dépôt public de composants : pas de `CONTRIBUTING`, pas d'historique
de contributions, pas de gouvernance visible. C'est une différence structurante avec shadcn/ui et
React Bits, dont tout le développement est public.

## 9. ⚠️ Licences et contraintes de réutilisation — le point central

**Deux récits contradictoires coexistent.**

*Le récit répandu* : de nombreux sites tiers — annuaires d'alternatives open source, articles de
blog, fiches techniques — présentent Aceternity UI comme **MIT**, libre pour un usage personnel et
commercial.

*La page de licence officielle* (`ui.aceternity.com/licence`) décrit une **licence Aceternity
propre**, distincte du MIT :

> **Usages autorisés** — créer un nombre illimité de produits finis pour soi ou ses clients ; les
> produits finis peuvent être vendus, licenciés, sous-licenciés ou distribués librement ;
> modification et combinaison autorisées ; usage multiple.

> **Usages interdits** — « You cannot re-distribute the Item as a stock image or its source files,
> **regardless of modifications** » ; interdiction de vendre ou distribuer l'Item ou ses œuvres
> dérivées **sur quelque place de marché que ce soit** ; interdiction de créer des thèmes,
> gabarits ou produits dérivés destinés à la vente sur une place de marché.

> **Propriété** — « The author retains ownership of the Item. »

**Analyse :** il ne s'agit pas du MIT. Les usages autorisés sont larges (produits finis vendables,
y compris commerciaux), mais **la redistribution du code est interdite, même modifié**, et la
revente sur place de marché est exclue. Les deux récits peuvent coexister parce que le palier
gratuit et le palier payant pourraient relever de régimes différents — **la page de licence
officielle ne distingue pas clairement les deux dans les extraits consultés**.

**Conséquence pour Mathemirum :** une bibliothèque de composants est par construction une
entreprise de redistribution. **Le code d'Aceternity UI ne peut pas servir de base**, quel que
soit le palier. En revanche, rien n'interdit d'en étudier les effets et de les réimplémenter — sous
réserve que la réimplémentation soit réelle et non dérivée. ⚠️ **Cette frontière est juridique et
n'est pas tranchée ici.**

## 10. Points forts

- Une esthétique d'animation reconnaissable, largement adoptée.
- L'intégration **MCP** dès le palier gratuit : c'est le signal le plus intéressant — l'exposition
  du catalogue aux assistants de code devient un argument de distribution.
- Un palier gratuit réellement utilisable en production commerciale pour des produits finis.
- Documentation et exemples soignés.

## 11. Limites

- **Aucun dépôt public des composants** : pas de transparence, pas de contribution communautaire,
  pas d'audit.
- **Licence propriétaire interdisant la redistribution**, contrairement au MIT annoncé par de
  nombreuses sources tierces.
- ⚠️ **Aucune explication mathématique** : ce sont des composants d'interface animés.
- Le périmètre exact du gratuit est flou : les volumes annoncés varient du simple au triple selon
  les sources.

## 12. Éléments non vérifiés ⚠️

- Le texte intégral de la page de licence officielle (seuls des extraits ont été consultés).
- Le régime exact du palier gratuit : MIT ? licence Aceternity ? les deux selon l'élément ?
- Les tarifs réels à la date d'observation.
- Le nombre réel de composants gratuits.
- L'existence et le fonctionnement effectif du serveur MCP officiel.
- Le modèle de contribution, s'il en existe un.

## 13. Idées à retenir

- **L'exposition aux assistants de code est devenue un argument de distribution.** MCP pour Claude
  Code, Codex, Devin, Cursor, annoncé en tête des avantages du palier gratuit. Mathemirum prévoit
  un prompt par composant : ce mouvement confirme l'intuition, et il est déjà industrialisé.
- **Déclarer publiquement sa non-affiliation** (« nous ne sommes pas un projet shadcn ») : une
  pratique de transparence simple, que Mathemirum devra appliquer vis-à-vis de shadcn/ui.
- Les annuaires tiers répètent les licences sans les vérifier. **La source de vérité est la page de
  licence de l'éditeur, jamais un agrégateur.**

## 14. Erreurs à éviter

- ❌ Se fier aux annuaires qui annoncent « MIT » : la page officielle décrit autre chose.
- ❌ Croire que « utilisation commerciale autorisée » implique « redistribution autorisée ». Ce sont
  deux droits distincts, et seule la seconde concerne une bibliothèque de composants.
- ❌ Supposer qu'un paquet npm au nom de la marque est la voie officielle : ici, il date de deux ans.

## 15. Opportunités de différenciation

Identiques à celles de React Bits (F01 §15), avec un angle supplémentaire : **Aceternity n'a pas de
dépôt public**. Un projet qui publie tout — code, métadonnées, gouvernance, licence claire —
dispose d'un avantage de confiance réel et vérifiable. C'est un différenciateur que le cahier des
charges de Mathemirum rend naturel : documentation, tests et mesures de performance par composant
ne peuvent pas être simulés dans un dépôt fermé.

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| Organisation `aceternity` : 2 dépôts, aucun pour les composants | `GET /search/repositories?q=aceternity+ui`, page de l'organisation | 2026-10-19 |
| Usages autorisés et interdits, clause de propriété | page publique `ui.aceternity.com/licence` | 2026-10-19 |
| Palier gratuit, MCP, pile technique | page publique `ui.aceternity.com/pricing` | 2026-10-19 |
| Absence d'affiliation avec shadcn/ui | page publique `ui.aceternity.com/shadcn-blocks` | 2026-10-19 |
| Paquet npm `aceternity-ui` : MIT, publication il y a 2 ans | fiche npm publique | 2026-10-19 |
| Volumes et tarifs divergents selon les sources | recherche web, sources tierces multiples | 2026-10-19 |

**Limites :** lecture d'extraits de pages publiques, non du texte intégral des conditions. Aucune
vérification juridique. Aucun composant inspecté dans un dépôt, puisqu'il n'en existe pas.
