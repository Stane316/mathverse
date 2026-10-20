#!/usr/bin/env python3
"""Lot A-3 : ensembles et denominabilite (§8), theoremes (§10), Cantor (§10.7).

Dix propositions du lot 3 du document A, dont une notice d'inconnu (A3-10)
qui n'entraine volontairement AUCUNE edition. Voir `domaine-A-lot3.md`.

Toutes les regions a remplacer sont lues dans le fichier par `entre()` : on
n'en transcrit aucune a la main. Voir `lot_commun.py`.

Usage
-----
    python3 tools/restauration/build_lot_A_3.py
"""

import sys

from lot_commun import H, M, I, appliquer, entre

EDITS = [
    # ------------------------------------------------- §8 introduction
    ("A3-08 + A3-09",
     *entre("8. ENSEMBLES, FONCTIONS ET DÉNOMBRABILITÉ", "Après avoir examiné",
            "\n\n```python\ndef factorielle(n):\n    if n = 0:\n"
            "        return 1\n    else:\n"
            "        return n × factorielle(n - 1)\n```\n\n"),
     M,
     "Le code est entierement present et lisible : seuls les retours a la ligne "
     "et l'indentation ont ete perdus. Le token `n   − 1` qui ouvre la pile est "
     "le `n - 1` de la derniere ligne, deplace en tete ; il est recase dans le "
     "bloc, et non supprime.",
     "TROIS NORMALISATIONS, toutes signalees. (1) Le mot-cle `def` n'est pas "
     "atteste : il est restitue par necessite syntaxique. (2) Les mots de la "
     "source sont FRANCAIS — `si`, `retourner`, `sinon` — et sont ici rendus par "
     "les mots-cles Python `if`, `return`, `else`, conformement a la proposition "
     "validee ; la variante fidele (`si` / `retourner` / `sinon`) reste "
     "disponible si le porteur prefere ne rien normaliser. (3) Le `×` est "
     "CONSERVE tel que la source le porte, alors que l'orthographe Python est "
     "`*` : la proposition l'avait annonce, le bloc livre garde le signe atteste. "
     "L'erreur `n = 0` (comparaison en Python : `==`) est une erreur du document "
     "d'origine, NON de la degradation : elle est conservee et signalee. La "
     "phrase suivante, « Apres avoir examine les premiers elements… », n'appar- "
     "tient pas au §8 : elle est laissee en place, voir le compte rendu."),

    # ------------------------------------------------------------ §8.2
    ("A3-01a",
     *entre("8.2 Injection, surjection, bijection  ", "  Ces notions servent",
            "\n\n| Notion | Définition intuitive | Signature |\n|---|---|---|\n"
            "| Injection | Deux entrées distinctes ne partagent pas la même "
            "sortie | `f(a) = f(b) ⇒ a = b` |\n"
            "| Surjection | Chaque élément du codomaine est atteint | "
            "`∀y, ∃x : f(x) = y` |\n"
            "| Bijection | Injection et surjection | Correspondance un-à-un et "
            "surjective |\n"),
     H,
     "La definition intuitive de l'injection (« deux entrees distinctes ne "
     "partagent pas la meme sortie ») est la glose litterale de "
     "f(a) = f(b) ⇒ a = b ; celle de la surjection (« chaque element du "
     "codomaine est atteint ») est celle de ∀y, ∃x : f(x) = y. Les deux colonnes "
     "vides recoivent donc les deux formules, sans ambiguite. La ligne Bijection "
     "avait deja sa signature et n'est pas touchee.",
     None),

    # ------------------------------------------------------------ §8.3
    ("A3-01b",
     *entre("Exemples classiques : ", " n’est pas dénombrable.",
            "`ℕ` est dénombrable ; `ℤ` est dénombrable ; `ℚ` est dénombrable ; "
            "`ℝ`"),
     H,
     "Le fragment porte cinq tokens (`N Z Q R N`) et le §8.3 presente exactement "
     "cinq emplacements vides : trois ensembles denombrables, un non denombrable, "
     "et l'ensemble de reference de la bijection. La correspondance est bijective "
     "et suit l'ordre du texte. `ℝ` en quatrieme position est le seul des quatre "
     "a ne pas etre denombrable, ce que la source affirme precisement ici.",
     "Les tokens `N Z Q R` sont la forme degradee de `ℕ ℤ ℚ ℝ` : la restitution "
     "des symboles double-struck est une normalisation typographique, pas une "
     "invention de contenu."),

    ("A3-01c",
     *entre("correspondance bijective avec ", " existe.", "`ℕ`"),
     H,
     "Cinquieme et dernier emplacement du §8.3, cinquieme token du fragment. "
     "L'ensemble de reference d'une correspondance bijective avec les entiers "
     "est `ℕ`. Le compte tombe juste : cinq pour cinq, sans reste.",
     None),

    # ------------------------------------------------------------ §8.4
    ("A3-01d",
     *entre("permettant notamment d’établir qu’un ensemble n’est pas dénombrable."
            "  Idée", "Supposons qu’on ait prétendu", "  "),
     H,
     "Le fragment #29 git dans le §8.4, entre le mot « Idee » et le paragraphe "
     "qu'il introduit. Or « Idee » annonce precisement l'argument qui suit : "
     "« Supposons qu'on ait pretendu lister tous les elements… ». Le fragment "
     "avait donc coupe un label de son contenu ; le retirer ressoude la phrase. "
     "Les sept tokens sont integralement recases : deux au §8.2 (A3-01a) et "
     "cinq au §8.3 (A3-01b, A3-01c).",
     None),

    # ----------------------------------------------------------- §10.1
    ("A3-02",
     *entre("10.1 Lois de De Morgan  Énoncé :", "Reconnaissance :",
            " `¬(P ∧ Q) ≡ ¬P ∨ ¬Q` · `¬(P ∨ Q) ≡ ¬P ∧ ¬Q`  "),
     H,
     "L'emplacement « Enonce : » est vide, le fragment contient les deux lois de "
     "De Morgan, et la section porte leur nom. Aucune autre affectation n'est "
     "concevable.",
     None),

    # ----------------------------------------------------------- §10.2
    ("A3-03a",
     *entre("Une règle de résolution classique :",
            "Elle élimine le littéral complémentaire",
            " `(P ∨ A), (¬P ∨ B) ⇒ (A ∨ B)`  "),
     H,
     "L'emplacement est vide, le fragment fournit la regle, et la section porte "
     "son nom.",
     None),

    ("A3-03b",
     *entre("Elle élimine le littéral complémentaire", "dans deux clauses",
            " `P`  "),
     H,
     "La phrase designe elle-meme le token attendu : « Elle elimine le litteral "
     "complementaire _ dans deux clauses ». Le litteral present sous les deux "
     "formes `P` et `¬P` dans la regle est `P`.",
     None),

    ("A3-03c",
     *entre("par cette", "méthode.", " "),
     H,
     "Retrait du fragment #32/#33, recase en A3-02 et A3-03a/A3-03b. La pile "
     "coupait la phrase en deux — « … decidable par cette [pile] methode. » — ; "
     "le retrait la ressoude : « par cette methode. »",
     None),

    # ----------------------------------------------------------- §10.6
    ("A3-04a",
     *entre("On considère un programme", "et une entrée", " `P` "),
     H,
     "Premier des quatre emplacements vides du §10.6. Le fragment fournit les "
     "quatre tokens dans l'ordre du texte (`P`, `x`, `P`, `x`).",
     None),

    ("A3-04b",
     *entre("et une entrée", ". Le problème demande", " `x`"),
     H,
     "Deuxieme emplacement, deuxieme token. Le point qui suit est conserve a sa "
     "place, sans espace devant.",
     None),

    ("A3-05a",
     *entre("si l’exécution de", "finira par s’arrêter", " `P` sur `x` "),
     H,
     "Troisieme et quatrieme emplacements, troisieme et quatrieme tokens : "
     "« l'execution de _ sur _ ». Les deux sont pourvus en une seule edition "
     "pour garantir l'ordre `P` puis `x`.",
     None),

    ("A3-04c",
     *entre("s’arrêter.  Question :", "Le résultat fondamental",
            " `H(P, x) = { 1 si P(x) s’arrête, 0 sinon`  "),
     M,
     "Cinquieme emplacement, la « Question : » vide. Le fragment fournit la forme "
     "de la fonction d'arret. L'accent de `s'arr te` est recompose en `s'arrête` "
     "par le meme artefact de decalage deja verifie en §5 et §8.",
     "DEUX RESERVES. (1) La mise en forme (accolade, alignement) est PROPOSEE, "
     "non attestee ; l'accolade fermante est ABSENTE du fragment et n'a pas ete "
     "ajoutee. (2) L'ordre des tokens dans la pile est `1 · 0 · si … sinon`, alors "
     "que la lecture retenue est `1 si … , 0 sinon`. Le deplacement de `0` est "
     "un artefact de facetage du meme type que celui des accents ; la lecture "
     "conventionnelle est adoptee et signalee."),

    ("A3-04d",
     *entre("Ce que cela ne veut pas dire", "Cela ne signifie pas", "  "),
     H,
     "Retrait du fragment #33/#34, recase en A3-04a a A3-04c. Le fragment cou- "
     "pait la section : il s'etait insere entre l'intitule « Ce que cela ne veut "
     "pas dire » et son paragraphe. Le retrait ressoude les deux.",
     None),

    # ----------------------------------------------------------- §10.7
    ("A3-06 + A3-07",
     *entre("10.7 Théorème de Cantor sur les ensembles  Pour tout ensemble",
            "Reconnaissance :",
            " `A`, son ensemble des parties `P(A)` a une cardinalité strictement "
            "supérieure à celle de `A`.  Forme : `∣A∣ < ∣P(A)∣`  "),
     H,
     "Le fragment est insere AU MILIEU D'UNE PHRASE du §11.3 — « tandis [frag- "
     "ment] que » —, artefact de deplacement manifeste. Le §10.7 presente trois "
     "emplacements vides, et le fragment porte `A`, `P(A)`, `A` dans cet ordre : "
     "trois pour trois. Le quatrieme token, `∣A∣ < ∣P(A)∣`, est l'enonce meme du "
     "theoreme, dont le §10.7 donne la version en prose.",
     "Cas le plus solide du corpus avec A2-07 : emplacements vides explicites ET "
     "phrase coupee en deux, les deux preuves reunis. Le libelle « Forme : » est "
     "AJOUTE pour recevoir le quatrieme token, la source ne presentant pas de "
     "quatrieme emplacement ; il reprend le vocabulaire deja employe par le §6.7. "
     "Les barres sont des U+2223 DIVIDES, exactement comme dans la source."),

    # ----------------------------------------------------------- §11.3
    ("A3-06b + A3-07b",
     *entre("positives, tandis", "Existe-t-il une procédure mécanique", " "),
     H,
     "Retrait des quatre tokens de Cantor, recases au §10.7 (A3-06 + A3-07). "
     "Aucun token n'est perdu.",
     "LA PHRASE RESTE COUPEE, ET C'EST VOLONTAIRE. Le §11.3 porte une SECONDE "
     "intrusion, non cataloguee par l'inventaire : la phrase « Existe-t-il une "
     "procedure mecanique qui, pour chaque entree autorisee, produit la sortie "
     "demandee en un nombre fini d'etapes ? » s'est inseree entre « tandis » et "
     "« que ». Cette phrase definit la DECIDABILITE, pas la semi-decidabilite : "
     "son domicile est donc ailleurs dans le §11, qui releve du LOT 4. Elle est "
     "conserve telle quelle ; le §11.3 sera ressoude au lot 4, une fois la "
     "destination de cette phrase etablie."),
]


def main():
    return appliquer(
        EDITS,
        journal="docs/restauration/propositions/domaine-A-lot3.journal.json",
    )


if __name__ == "__main__":
    sys.exit(main())
