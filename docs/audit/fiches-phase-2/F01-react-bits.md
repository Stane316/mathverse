# F01 — REACT BITS

**Fiche d'étude de plateforme — phase 2**
**Date d'observation :** 2026-10-19 · **Mode d'accès :** API publique GitHub, fichiers du dépôt public
**Priorité de cette fiche :** la licence — le concurrent le plus direct du projet.

---

## 1. Présentation et positionnement

React Bits se présente comme « la plus grande bibliothèque open source de composants React et
Next.js animés, interactifs et personnalisables ». 49 719 étoiles, JavaScript, dépôt actif au
jour de l'observation. C'est l'acteur dominant du secteur des composants visuels animés pour le
web, et le concurrent le plus direct de Mathemirum sur le terrain du composant.

## 2. Fonctionnalités

- Composants d'animation et d'effets visuels (fonds, textures, formes, texte).
- **Outils en ligne** dans le dépôt : `Background Studio`, `Texture Lab`, `Shape Magic`,
  `Center Stage`, `Sound Lab` — un atelier de création livré avec la bibliothèque.
- Une bibliothèque de sons, exportée sous forme de code par `src/tools/sound-lab/export/code`.
- Composants déclinés en variantes de langage : le registre génère des fichiers `.js` et `.ts`.

## 3. Parcours utilisateur

Le modèle est celui du **copier-coller**, pas de l'installation de paquet : on parcourt, on
prévisualise, on règle, on copie le code — ou on l'ajoute via un outil en ligne de commande.

## 4. Architecture technique observable

Le dépôt est une application (React + Vite) qui sert à la fois de site vitrine et d'atelier.
Points notables :

- **`jsrepo.config.ts`** à la racine : la distribution est construite avec **jsrepo**, et non
  avec la CLI shadcn. La nomenclature du registre est `@react-bits`.
- **L'adaptateur `@jsrepo/shadcn`** est importé : React Bits **émet donc des articles de registre
  au format shadcn**, tout en utilisant jsrepo comme outil de construction. C'est une nuance
  importante, mal documentée dans les présentations habituelles.
- `src/constants/Information` : chaque composant porte des métadonnées (catégorie, variante) qui
  pilotent la génération du registre. **C'est le point le plus instructif pour Mathemirum** : les
  métadonnées sont une source structurée, pas du texte libre.
- Un répertoire `worker` et un répertoire `scripts` : une partie du traitement est déportée.

## 5. Mode de distribution

Deux canaux : le site (copier-coller assisté) et le registre (résolution par un outil CLI).
`package.json` porte `"private": true` et `version 0.0.0` — **le dépôt n'est pas publié comme
paquet npm**.

## 6. Prévisualisation et personnalisation

C'est le point fort du modèle : chaque composant est accompagné d'un aperçu en direct et de
paramètres réglables, avant la récupération du code. Les outils en ligne (Background Studio,
Texture Lab…) poussent cette logique jusqu'à la génération assistée.

## 7. Stratégie documentaire

Documentation intégrée au site, organisée par catégorie ; `CONTRIBUTING.md` présent. ⚠️ Le
niveau d'explication technique par composant n'a **pas** été évalué composant par composant —
voir §12.

## 8. Modèle de contribution

`CONTRIBUTING.md` présent au dépôt. ⚠️ Le processus effectif (délais d'acceptation, gouvernance,
qui tranche) n'a **pas** été observé — voir §12.

## 9. ⚠️ Licences et contraintes de réutilisation — le point central

**Ce n'est pas une licence open source.** GitHub ne la reconnaît pas (`spdx_id = NOASSERTION`).
Le fichier `LICENSE.md` porte le titre « **MIT + Commons Clause License Condition v1.0** »,
copyright 2026 David Haz. Le `package.json` ne déclare aucun champ `license`.

Extraits textuels consultés le 2026-10-19 :

> « You may use this Software, including for any commercial purpose, **so long as you do not sell,
> sublicense, or redistribute the components themselves** — whether alone, in a bundle, or as a
> ported version. »

> « The same restriction covers the React Bits tools (Background Studio, Texture Lab, Shape Magic,
> Center Stage, Sound Lab and any tools added later) and the sounds in the sound library.
> **You may not sell, sublicense, or redistribute the tools or the sounds themselves, or offer the
> tools or a substantially similar copy of them as a hosted service** — whether alone, in a bundle,
> or as a ported version. »

> « What you make with the tools is yours to use. You can use exported code, images, videos, and
> audio files in any personal or commercial application, website, or product, including paid ones.
> **You may not sell or redistribute the exports on their own**, either individually or as the
> product itself, such as a sound, texture, background, or template pack. »

**Conséquences pour Mathemirum :**

| | Verdict |
|---|---|
| Redistribuer les composants, seuls ou dans un registre | ❌ **interdit** |
| Porter un composant (React → autre framework) | ❌ **interdit** |
| Héberger un service « substantiellement similaire » aux outils | ❌ **interdit** |
| Vendre les exports (pack de fonds, de textures, de gabarits) | ❌ **interdit** |
| Utiliser les composants dans un produit final, y compris payant | ✅ autorisé |
| Réutiliser le code exporté par les outils dans une application | ✅ autorisé |
| Reprendre la *mécanique* (aperçu, paramètres, copier-coller, registre) | ✅ non couvert par la clause |

**La clause vise exactement le modèle de Mathemirum** : une bibliothèque de composants publiée
sous registre. Elle n'est donc pas contournable par un argument d'usage interne.

⚠️ **Un point reste à qualifier juridiquement**, et il touche directement le cahier des charges :
Mathemirum prévoit par composant une « **configuration exportable** ». Si cette configuration est
un simple jeu de paramètres, elle n'est pas un export au sens de la clause. Si elle constituait
un *pack de gabarits* distribué pour lui-même, elle pourrait l'être. **La frontière n'est pas
tranchée ici et ne doit pas l'être sans avis juridique.**

## 10. Points forts

- Le modèle d'expérience : aperçu en direct + paramètres réglables avant récupération du code.
- Les métadonnées structurées par composant (`src/constants/Information`) — c'est ce qui rend la
  distribution automatisable.
- La génération multi-variantes (JS/TS) depuis une même source.
- Une traction très forte (49 719 ★), signe d'un besoin réel.

## 11. Limites

- **Licence non ouverte**, et explicitement hostile au modèle de redistribution.
- ⚠️ **Aucune explication mathématique** observée : les composants sont des effets visuels. Ce
  n'est pas un défaut de leur part, c'est simplement un autre objet.
- Le dépôt est `private` et en version `0.0.0` : pas de publication npm, donc pas de versionnage
  sémantique opposable.

## 12. Éléments non vérifiés ⚠️

- Le nombre exact de composants (les « 215+ » annoncés par le site n'ont pas été comptés ici).
- La profondeur réelle de la documentation par composant.
- Le processus de contribution effectif.
- L'existence d'une activité commerciale (services, abonnement) autour du projet.
- L'interprétation juridique précise de la clause vis-à-vis d'une configuration exportable.

## 13. Idées à retenir

- **Séparer la mécanique du code.** Ce qui fait la valeur de React Bits — aperçu, réglages,
  copier-coller, registre — n'est pas couvert par la clause, et son origine (shadcn/ui) est MIT.
- **Les métadonnées structurées sont l'infrastructure invisible.** Un fichier de métadonnées par
  composant, qui pilote la génération, est ce qui permet de publier à grande échelle.
- **Multi-variantes depuis une source unique** : écrire une fois, générer JS et TS.

## 14. Erreurs à éviter

- ❌ Partir du code de React Bits, même « juste pour voir » puis le réécrire : le risque
  juridique est sur la redistribution, et la frontière du « substantiellement similaire » est
  floue.
- ❌ Croire que « MIT » dans le titre de la licence suffit : c'est la clause qui porte.
- ❌ Reproduire les outils en ligne (Background Studio & cie) : ils sont nommément couverts.

## 15. Opportunités de différenciation

React Bits couvre le **visuel** ; il ne couvre ni l'explication mathématique, ni les équations et
hypothèses, ni la validation, ni le prompt de régénération, ni les tests. **C'est précisément le
territoire de Mathemirum.** L'opportunité n'est pas de faire de meilleurs effets, mais de
livrer des composants *démontrables* — dont on peut dire pourquoi ils fonctionnent, sous quelles
hypothèses, et comment les régénérer.

## 16. Sources, dates et preuves

| Donnée | Source | Date |
|---|---|---|
| Licence (`NOASSERTION`), 49 719 ★, activité | `GET /repos/DavidHDev/react-bits` | 2026-10-19 |
| Texte intégral de la licence | `GET /repos/DavidHDev/react-bits/contents/LICENSE.md` | 2026-10-19 |
| `private: true`, pas de champ `license` | `GET /repos/DavidHDev/react-bits/contents/package.json` | 2026-10-19 |
| jsrepo + `@jsrepo/shadcn`, registre `@react-bits`, métadonnées | `GET /repos/DavidHDev/react-bits/contents/jsrepo.config.ts` | 2026-10-19 |
| Arborescence, `CONTRIBUTING.md`, outils | `GET /repos/DavidHDev/react-bits/contents/` | 2026-10-19 |

**Limite :** aucune vérification auprès d'un registre de marques ni d'un conseil juridique.
