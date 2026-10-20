#!/usr/bin/env python3
"""Lot A-4 : calculabilite (§11), verification (§12), types (§13),
algorithmes (§15), cybersecurite (§16), IA symbolique (§17, §18).

Treize propositions du lot 4 du document A, dont deux qui n'entrainent
volontairement aucune edition (A4-05, A4-14). Voir `domaine-A-lot4.md`.

Toutes les regions sont lues par `entre()` ; la phrase egarée du §11.3 est
meme relue telle quelle pour etre recasée au §11.1, sans transcription.

Usage
-----
    python3 tools/restauration/build_lot_A_4.py
"""

import sys

from lot_commun import H, M, I, appliquer, entre, _lire

# ---------------------------------------------------------------- §11.3
# La phrase egarée est RELUE dans le fichier, jamais recopiée : elle va être
# déplacée mot pour mot.
_DEB, _FIN = "positives, tandis", "que sur les instances négatives"
_t = _lire()
_i, _j = _t.find(_DEB), _t.find(_FIN)
PHRASE_EGAREE = _t[_i + len(_DEB):_j].strip()

EDITS = [
    # ============================================ §11.1 <- §11.3 (NOUVEAU)
    ("A4-15",
     *entre("Une question typique :", "11.2 Décidabilité",
            " " + PHRASE_EGAREE + "\n\n"),
     H,
     "TROUVAILLE, non cataloguee par l'inventaire. Le §11.1 annonce « Une "
     "question typique : » et s'arrete : l'emplacement est vide. Or le §11.3 "
     "portait une phrase entiere, inseree entre « tandis » et « que », qui "
     "definit la CALCULABILITE et non la semi-decidabilite : c'est exactement "
     "la question typique du §11.1. Emplacement vide explicite ET phrase "
     "coupee en deux : les deux preuves reunis, comme A3-06/A3-07. La phrase "
     "est deplacee MOT POUR MOT, relue dans le fichier sans transcription.",
     "Le lot 3 avait laisse le §11.3 coupe, precisement parce que cette "
     "destination etait a etablir et relevait du §11, donc du lot 4. Elle "
     "l'est desormais, et le §11.3 est ressoude par A4-15b."),

    ("A4-15b",
     *entre(_DEB, _FIN, " "),
     H,
     "Retrait de la phrase egarée, recasée au §11.1 (A4-15). « tandis … que » "
     "n'admet aucune insertion : la phrase est ressoudée.",
     None),

    # ================================================= §11.6 (A4-01)
    ("A4-01a",
     *entre("Forme schématique :", "Selon le type", " `A ≤ B`  "),
     H,
     "L'emplacement « Forme schematique : » est vide, et le fragment porte "
     "`A ≤ B`, qui est la forme schematique de la reduction.",
     None),

    ("A4-01b",
     *entre("que résoudre", "permettrait de résoudre", " `A` "),
     H,
     "Second emplacement. Le sens impose l'affectation : « resoudre A "
     "permettrait de resoudre B » est la signification meme de `A ≤ B`.",
     "L'ordre du fragment (`A ≤ B`, puis `B`, puis `A`) ne suit pas l'ordre du "
     "texte (`A`, puis `B`). L'inversion est REELLE et NON EXPLIQUEE ; "
     "l'affectation repose sur le sens, pas sur la position."),

    ("A4-01c",
     *entre("permettrait de résoudre", ".  Comment reconnaître une réduction",
            " `B`"),
     H,
     "Troisieme emplacement, troisieme token. Meme reserve que A4-01b sur "
     "l'ordre du fragment.",
     None),

    ("A4-01d",
     *entre("les réponses pertinentes.", "Les réductions sont centrales", "  "),
     H,
     "Retrait du fragment #38, recase en totalite : `A ≤ B` en A4-01a, `A` en "
     "A4-01b, `B` en A4-01c.",
     None),

    # ============================================= §12.2 (A4-03 + NOUVEAU)
    ("A4-16",
     *entre("On peut écrire un triplet de Hoare :", "Lecture :",
            " `P` : précondition ; `C` : commande ou programme ; "
            "`Q` : postcondition.  "),
     H,
     "TROUVAILLE, non cataloguée. Le §12.2 porte TROIS emplacements vides "
     "accompagnes de leur legende : « _ : précondition ; _ : commande ou "
     "programme ; _ : postcondition. ». La legende n'est donc PAS proposée, "
     "elle est ATTESTEE par la source elle-meme : c'est le document qui "
     "apparie chaque emplacement a son role. Les trois tokens `P`, `C`, `Q` "
     "les remplissent dans l'ordre, qui est l'ordre meme du triplet.",
     "Ceci leve la reserve 2 de la proposition : l'appariement "
     "P/precondition, C/commande, Q/postcondition n'est plus une proposition, "
     "il est donne par le texte."),

    ("A4-02 + A4-03",
     *entre("retourner un élément dont la valeur est maximale.",
            "12.3 Logique de Hoare",
            "  Si `P` est vrai avant l’exécution de `C`, et si celle-ci "
            "termine conformément au cadre de raisonnement, alors `Q` est "
            "vrai après.\n\n"),
     H,
     "Une seule edition, parce que trois operations s'y enchainent et que "
     "l'ordre importe. (1) Le fragment #39 — le triplet `{P} C {Q}` suivi de "
     "`P`, `C`, `Q` — gisait ici, apres l'exemple du maximum : le triplet part "
     "au §12.3 (A4-02), les trois lettres vont a la ligne de legende (A4-16). "
     "(2) Les trois emplacements de la phrase « Si _ est vrai avant "
     "l'execution de _ …, alors _ est vrai apres » recoivent `P`, `C`, `Q`, "
     "qui est la semantique meme du triplet. (3) Le fragment #40 — `P`, `C`, "
     "`Q` — qui trainait apres cette phrase est retire, ses tokens etant "
     "recases en A4-16 et A4-02.",
     "SEPT tokens pour SEPT destinations : le triplet va au §12.3 ; les trois "
     "lettres de #39 a la ligne de legende du §12.2 ; les trois lettres de #40 "
     "a la phrase « Si … alors ». Aucun token n'est perdu."),

    ("A4-02",
     *entre("notamment à l’aide de triplets de Hoare.",
            "Comment la reconnaître ?", " `{P} C {Q}`\n\n"),
     H,
     "Le §12.3 annonce explicitement « les triplets de Hoare » sans en donner "
     "un seul ; le §12.2, qui traite des preconditions et postconditions, n'a "
     "pas vocation a porter le triplet. Le fragment fournit le triplet, "
     "recase ici.",
     "La legende n'est pas repetee au §12.3 : elle est deja attestee au §12.2 "
     "par A4-16, et la doubler serait une invention redondante."),

    # ================================================= §13.5 (A4-04)
    ("A4-04",
     *entre("Une fonction reçoit un vecteur de taille",
            "Dans les systèmes qui prennent",
            " `n` et renvoie un vecteur de taille `n`.\n\n"),
     H,
     "Deux emplacements vides, deux tokens `n`, et la phrase decrit une "
     "fonction de `n` vers `n`.",
     "Le second emplacement pourrait etre `n + 1` ou `m` : la source ne "
     "permet pas de trancher, et `n` est le seul token disponible dans le "
     "fragment. La reserve est maintenue."),

    # ================================================= §15.3 (A4-06)
    ("A4-06",
     *entre("15.3 Énumération exhaustive des affectations  Pour",
            "La méthode teste chacune d’elles.",
            " `n` variables propositionnelles, il existe `2ⁿ` affectations "
            "possibles.\n\n"),
     H,
     "Deux emplacements vides, deux tokens, et la phrase qui suit — « le "
     "nombre d'affectations croit exponentiellement » — confirme `2ⁿ`. Le "
     "second token du fragment, `2 n`, est la forme degradee de l'exposant.",
     "Deux emplacements vides restent sans token disponible : « Complexité "
     "indicative : _ » et « croît exponentiellement avec _ ». Ils sont laisses "
     "tels quels."),

    # ============================================= §15.6 <- §15.7 (A4-11)
    ("A4-11a",
     *entre("15.6 Unification  L’unification cherche une substitution de "
            "variables qui rend deux expressions identiques.  "
            "Exemple conceptuel :", "Reconnaissance :",
            " `f(x, 3) et f(2, y)`\n\nUne substitution possible est : "
            "`x = 2`, `y = 3`\n\n"
            "*Fragment non rattaché, conservé faute de destination établie :* "
            "`n`  "),
     M,
     "Le §15.6 traite de l'unification ; le §15.7, du chainage. Les termes "
     "`f(x, 3)` et `f(2, y)` avec leur substitution sont l'exemple canonique "
     "de l'unification, et le §15.6 presente deux emplacements vides : "
     "« Exemple conceptuel : » et « Une substitution possible est : ».",
     "REGLE DE NON-PERTE : un token `n` occupait l'emplacement « Exemple "
     "conceptuel : ». Il n'a aucune destination etablie — il pourrait aussi "
     "bien revenir au §15.3 (« croît exponentiellement avec _ »). Il est "
     "CONSERVE et signale, non supprime. Le verbe « unifier » et le mot "
     "« substitution » n'apparaissent pas dans le fragment : les libelles "
     "« Exemple conceptuel » et « Une substitution possible est » sont ceux de "
     "la source, le reste est laisse tel quel."),

    ("A4-11b",
     *entre("de la stratégie de recherche.", "Faits connus ↓", "  "),
     H,
     "Retrait du fragment #44, recase au §15.6 (A4-11a). Le fragment coupait "
     "le paragraphe « Limites » des schemas de chainage qui le suivent ; le "
     "retrait les ressoude.",
     None),

    # ================================================ §16.5 (A4-07/08/09)
    ("A4-07 + A4-08 + A4-09",
     *entre("Exemple de règle d’accès :", "Cette formule décrit une règle.",
            " `Authentifié(u) ∧ Autorisé(u, r) → AccèsPermis(u, r)`  "),
     H,
     "Les trois fragments #45 a #47 sont CONTIGUS et non deplaces : seule la "
     "decomposition des accents les a morceles. Le recollement est mecanique "
     "— `Authentifi` + `é`, `Autoris` + `é`, `Acc sP ermis` + `è` — et la "
     "structure logique (`∧` puis `→`) est intacte.",
     "L'orthographe `AccèsPermis` resulte d'un recollement de trois morceaux ; "
     "la casse exacte (espace ou non, majuscule interne) n'est pas attestée."),

    ("A4-07b",
     *entre("ses chemins d’exécution.", "16.6 Architecture système et Linux",
            "\n\n"),
     H,
     "Retrait du fragment decompose, recompose et recase en A4-07 + A4-08 + "
     "A4-09, juste au-dessus. Aucun token n'est perdu.",
     None),

    # ============================================ §17.5 <- §17.5/§18 (A4-12)
    ("A4-12a",
     *entre("Étape 1 — Modélisation", "Si le paiement est confirmé",
            " `A` : utilisateur authentifié ; `R` : utilisateur autorisé ; "
            "`P` : accès permis.  "),
     H,
     "Comme au §12.2 : les TROIS emplacements vides du §17.5 portent leur "
     "legende — « _ : utilisateur authentifié ; _ : utilisateur autorisé ; "
     "_ : accès permis. ». La legende est donc ATTESTEE, et non proposée. "
     "Les trois tokens `A`, `R`, `P` du fragment #48 les remplissent dans "
     "l'ordre.",
     "Ceci leve la reserve 1 de la proposition : l'appariement "
     "A/authentifie, R/autorise, P/acces permis est donne par le texte."),

    ("A4-12b",
     *entre("autoriser l’accès à la ressource.", "Règle :", "  "),
     H,
     "Retrait du fragment #48, recase en A4-12a et A4-13. Le fragment "
     "coupait l'enonce en prose de la regle qui suit ; le retrait les "
     "ressoude.",
     None),

    ("A4-13",
     *entre("Règle :", "Étape 2 — Reconnaissance", " `A ∧ R → P`  "),
     M,
     "L'emplacement « Regle : » est vide, et le §18 porte `A ∧ R → P` "
     "immediatement suivi du pseudo-code qui l'implemente. Le §17.5 est "
     "« Exemple complet : validation d'un acces Web », c'est-a-dire exactement "
     "cette regle.",
     "La reserve 2 de la proposition subsiste : le fragment #49 pourrait "
     "AUSSI rester au §18, ou il joue le role d'exemple d'IA symbolique, et "
     "ou il est suivi de son pseudo-code. Deux destinations plausibles ; le "
     "§17.5 est retenu parce que c'est la qu'est l'emplacement vide. "
     "CONSEQUENCE : le pseudo-code du §18 — « si authentifié ET autorisé : "
     "permettre l'accès sinon : refuser l'accès » — se retrouve separe de sa "
     "formule. Il est conserve tel quel. A noter aussi : « Étape 3 — "
     "Implémentation conceptuelle » du §17.5 est vide, et ce pseudo-code en "
     "serait le contenu naturel ; l'hypothese est consignee pour un lot 5, "
     "elle n'est pas appliquee ici."),

    ("A4-13b",
     *entre("Je ne vais donc pas lui attribuer une signification arbitraire.",
            "si authentifié ET autorisé", "  "),
     M,
     "Retrait du fragment #49, recase au §17.5 (A4-13).",
     "Le pseudo-code qui suit reste en place. Voir la reserve de A4-13 : si "
     "le porteur prefere laisser la formule au §18, cette edition et A4-13 "
     "sont a annuler ensemble."),
]


def main():
    return appliquer(
        EDITS,
        journal="docs/restauration/propositions/domaine-A-lot4.journal.json",
    )


if __name__ == "__main__":
    sys.exit(main())
