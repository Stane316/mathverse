#!/usr/bin/env python3
"""Construit le correctif du lot A-1 (§2 vocabulaire, §3 notations, §4 propositions).

Difference de nature avec les lots precedents
---------------------------------------------
Les lots K, L, I, N, J comblaient des blocs d'affichage vides : le contenu
manquait, l'emplacement etait connu et reperable par un numero de ligne ou un
delimiteur `\\\\[`. Le document A, lui, a ete « aplani » : plus aucun titre, plus
aucune liste, plus aucun delimiteur. Ses formules n'ont pas ete effacees mais
DEPLACEES — retirees de leur emplacement, concatenees, puis reinserees ailleurs,
parfois au milieu d'une phrase.

Ce script traite donc des remplacements de SOUS-CHAINES a l'interieur de
paragraphes, et non des remplacements de lignes entieres. Il emet toutefois un
`patch.json` au schema habituel (ligne / ancien / nouveau / confiance /
justification), ou `ancien` est la ligne complete relue dans le fichier et
`nouveau` la ligne transformee : le format reste ainsi compatible avec
`apply_patch.py`.

Regle de securite
-----------------
Chaque sous-chaine source doit apparaitre EXACTEMENT UNE fois dans le fichier.
Sinon le script echoue sans rien ecrire.

Usage
-----
    python3 tools/restauration/build_lot_A_1.py
"""

import json
import sys

ROOT = "/home/user/_audit/connaissance"
FICHIER = ("Maths-vers-Informatiques/DOCUMENT MAÎTRE A — "
           "LOGIQUE ET FONDEMENTS DE L’INFORMATIQUE.md")

H = "haute"
M = "moyenne"
I = "inconnue"

# (identifiant, sous-chaine source, sous-chaine remplacement, confiance,
#  justification, validation)
EDITS = [
    # ------------------------------------------------------------ §2
    ("A1-11",
     "Déduction à partir de règles admises  V   F   1 0 ∧, ∨, ¬, →, ↔  P   ( x )   R ( x ,   y ) ∀, ∃ Γ ⊨   φ\n\nAxiome",
     "Déduction à partir de règles admises\n\n**Notations du vocabulaire**\n\n"
     "| Notation | Signification |\n|---|---|\n"
     "| `V`, `F` | valeurs de vérité |\n"
     "| `1`, `0` | valeurs de vérité (codage binaire) |\n"
     "| `∧`, `∨`, `¬`, `→`, `↔` | connecteurs logiques |\n"
     "| `P(x)` | prédicat unaire |\n"
     "| `R(x, y)` | prédicat binaire |\n"
     "| `∀`, `∃` | quantificateurs |\n"
     "| `Γ ⊨ φ` | conséquence logique |\n\nAxiome",
     M,
     "Fragment #1 insere au milieu du tableau de vocabulaire du §2, entre les entrees "
     "« Demonstration » et « Axiome ». Le §2 procede par paires notion/definition ; "
     "le fragment enumere des notations dont aucune n'a d'entree dans le §2 restant.",
     "Libelles de la colonne « Signification » proposes, non attestes : ils suivent "
     "l'usage standard et l'ordre du fragment."),

    ("A1-12",
     "Ensemble   Collection d’objets  Relation   Association entre objets   ,  Fonction   Association déterministe d’une entrée à une sortie",
     "Ensemble   Collection d’objets (appartenance : `x ∈ A`)  Relation   Association entre objets `R(x, y)`, aussi notée `xRy` ,  Fonction   Association déterministe d’une entrée à une sortie, notée `f : A → B`",
     M,
     "Fragments #2 et #3. L'entree « Relation » presente un emplacement vide avant la "
     "virgule (« Association entre objets   , ») ; `R(x, y)` et sa forme infixe `xRy` "
     "l'un et l'autre y trouvent place. `f : A → B` est la notation de l'entree "
     "« Fonction ». `x ∈ A` est porte a l'entree « Ensemble ».",
     "L'attribution de `x ∈ A` a « Ensemble » est une inference par similarite. "
     "La place exacte de `f : A → B` dans la definition n'est pas attestee."),

    ("A1-13",
     "Preuve, model checking, analyse formelle  ⊥  x   ∈   A R ( x ,   y )   xRy f   :   A   →   B  N\n\n3. NOTATIONS",
     "Preuve, model checking, analyse formelle  N\n\n3. NOTATIONS",
     H,
     "Retrait des tokens deja recases en A1-12. `⊥` est un doublon du §3.1 "
     "(ligne « Faux logique ») et n'est pas recase ici. Le `N` isole reste en "
     "place : sa destination n'est pas etablie.",
     "Le `N` restant est signale comme non resolu ; il pourrait appartenir au §8.3."),

    # ------------------------------------------------------------ §3.1
    ("A1-01",
     "3.1 Les connecteurs propositionnels  Symbole   Nom   Lecture  Négation   Non  Conjonction   et  Disjonction inclusive   ou   , ou les deux  Implication   Si   , alors  Équivalence   si et seulement si  Vrai logique   Toujours vrai  Faux logique   Contradiction",
     "3.1 Les connecteurs propositionnels\n\n"
     "| Symbole | Nom | Lecture |\n|---|---|---|\n"
     "| `¬P` | Négation | Non |\n"
     "| `P ∧ Q` | Conjonction | et |\n"
     "| `P ∨ Q` | Disjonction inclusive | ou , ou les deux |\n"
     "| `P → Q` | Implication | Si … , alors |\n"
     "| `P ↔ Q` | Équivalence | … si et seulement si |\n"
     "| `⊤` | Vrai logique | Toujours vrai |\n"
     "| `⊥` | Faux logique | Contradiction |",
     H,
     "Le tableau 3.1 conserve ses colonnes « Nom » et « Lecture » mais sa colonne "
     "« Symbole » est vide. Le fragment #4a fournit exactement sept tokens "
     "(¬P, P∧Q, P∨Q, P→Q, P↔Q, ⊤, ⊥) et le tableau comporte sept lignes, "
     "dans le meme ordre — dont « Vrai logique · Toujours vrai » et "
     "« Faux logique · Contradiction » qui accueillent ⊤ et ⊥.",
     "CORRIGE PAR RAPPORT A LA PROPOSITION INITIALE : les libelles « toujours vrai / "
     "toujours faux » avaient ete proposes comme inventes alors qu'ils sont ATTESTES "
     "dans la source (« Toujours vrai », « Contradiction »). Le palier passe "
     "donc de T2 a T1 et aucun libelle n'est invente."),

    ("A1-01b",
     "Universel   Pour tout  ¬ P   P P   ∧   Q   P   Q P   ∨   Q   P   Q P   →   Q   P   Q P   ↔   Q   P   Q  ⊤ ⊥  P   →   Q",
     "Universel   Pour tout  P   →   Q",
     H,
     "Retrait des sept tokens de §3.1 du fragment #4, qui git dans le tableau §3.2.",
     None),

    # ------------------------------------------------------------ §3.2
    ("A1-03",
     "3.2 Les quantificateurs  Symbole   Nom   Lecture  Universel   Pour tout  P   →   Q  P Q P   →   Q P   →   Q   P   Q  ∀ x   x\n\nExistentiel   Il existe au moins un  Existence et unicité   Il existe exactement un  Exemples :",
     "3.2 Les quantificateurs\n\n"
     "| Symbole | Nom | Lecture | Exemple |\n|---|---|---|---|\n"
     "| `∀` | Universel | Pour tout | `∀x ∈ R, x² ≥ 0` |\n"
     "| `∃` | Existentiel | Il existe au moins un | `∃x ∈ Z, x² = 9` |\n"
     "| `∃!` | Existence et unicité | Il existe exactement un | `∃!x …` |\n\n"
     "*Fragments non rattachés, conservés faute de destination établie :* "
     "`P → Q` · `P Q P → Q P → Q P Q` · `∀x …`\n\n"
     "Existentiel   Il existe au moins un  Existence et unicité   Il existe exactement un  Exemples :",
     M,
     "Le tableau 3.2 a sa colonne « Symbole » vide ; le fragment #5 porte `∀ ∃ ∃!`, "
     "trois tokens pour trois lignes. Les deux exemples sont dictees par les gloses de "
     "la source : « tout reel a un carre positif ou nul » = ∀x ∈ R, x² ≥ 0 et "
     "« il existe au moins un entier dont le carre vaut 9 » = ∃x ∈ Z, x² = 9.",
     "L'exemple de ∃! reste tronque dans la source (« ∃! x   x », predicat perdu) : "
     "il est laisse en l'etat et signale, non complete. REGLE DE NON-PERTE : les "
     "tokens du fragment qui n'ont pas de destination etablie (`P → Q`, "
     "`P Q P → Q P → Q P Q`, le second `x` de `∀x x`) sont CONSERVES dans le "
     "document, signales comme non rattaches. Aucun contenu n'est supprime."),

    ("A1-03b",
     "Double négation  Lois de De Morgan  Implication  Contraposée  ∃ x   x  ∃! x   x  ∀ x   ∈   R ,   x   ≥ 2   0  ∃ x   ∈   Z ,   x   = 2   9  ∀ ∃ ∃!  ¬(¬ P   ) ≡   P",
     "Double négation  Lois de De Morgan  Implication  Contraposée  ¬(¬ P   ) ≡   P",
     H,
     "Retrait des tokens de §3.2 du fragment #5, qui git dans le §3.3.",
     None),

    # ------------------------------------------------------------ §3.3
    ("A1-15",
     "3.3 Équivalences logiques essentielles  Double négation  Lois de De Morgan  Implication  Contraposée  ¬(¬ P   ) ≡   P  ¬( P   ∧   Q ) ≡ ¬ P   ∨ ¬ Q  ¬( P   ∨   Q ) ≡ ¬ P   ∧ ¬ Q  P   →   Q   ≡ ¬ P   ∨   Q\n\nÉquivalence  Ces relations",
     "3.3 Équivalences logiques essentielles\n\n"
     "| Nom | Équivalence |\n|---|---|\n"
     "| Double négation | `¬(¬P) ≡ P` |\n"
     "| Lois de De Morgan | `¬(P ∧ Q) ≡ ¬P ∨ ¬Q` · `¬(P ∨ Q) ≡ ¬P ∧ ¬Q` |\n"
     "| Implication | `P → Q ≡ ¬P ∨ Q` |\n"
     "| Contraposée | `P → Q ≡ ¬Q → ¬P` |\n"
     "| Équivalence | `P ↔ Q ≡ (P → Q) ∧ (Q → P)` |\n\n"
     "Ces relations",
     H,
     "Le §3.3 est une liste de CINQ equivalences nommees (Double negation, Lois de "
     "De Morgan, Implication, Contraposée, Équivalence) dont aucune n'a de formule. "
     "Trois formules viennent du fragment #5 (sur place) et deux du fragment #6 "
     "(deplace depuis le §4.2) : les cinq sont ainsi pourvues, sans reste.",
     "TRANCHE : la proposition initiale hesitait entre §3.3 et §6.2. La presence "
     "d'une liste de cinq equivalences nommees, et la couverture exacte des cinq par "
     "les deux fragments, designent le §3.3 sans ambiguite."),

    ("A1-15b",
     "affectations possibles de ses propositions.  P   →   Q   ≡ ¬ Q   → ¬ P  P   ↔   Q   ≡ ( P   →   Q ) ∧ ( Q   →   P   )  P   ,   Q ,   R , …  P Q  P   →   Q\n\nNégation",
     "affectations possibles de ses propositions (`P`, `Q`, `R`, …).\n\nNégation",
     H,
     "Retrait du fragment #6 du §4.2, reattribue au §3.3 en A1-15.",
     None),

    # ------------------------------------------------------------ §4.4
    ("A1-16",
     "« Les contraintes se contredisent-elles ? » → recherche de satisfaisabilité / contradiction.  P   Q   P   ↔   Q  P   ∨ ¬ P P   ∧ ¬ P P   →   Q\n\n4.5 Formes normales",
     "« Les contraintes se contredisent-elles ? » → recherche de satisfaisabilité / contradiction.\n\n"
     "| Notion | Exemple | Statut |\n|---|---|---|\n"
     "| Contingence | `P → Q` | ni tautologie ni contradiction |\n"
     "| Contingence | `P ↔ Q` | ni tautologie ni contradiction |\n"
     "| Tautologie | `P ∨ ¬P` | toujours vraie |\n"
     "| Contradiction | `P ∧ ¬P` | toujours fausse |\n\n"
     "4.5 Formes normales",
     M,
     "Fin du §4.4. `P ∨ ¬P` est une tautologie et `P ∧ ¬P` une contradiction : "
     "l'appariement est certain. Les deux autres exemples sont contingents.",
     "La colonne « Statut » est proposee : les mots figurent au §4.3 mais leur "
     "appariement aux exemples est une inference."),
]

# --- E10 : les cinq tables de verite -----------------------------------------
# Contenu EN PLACE et VERIFIE EXACT (les 60 valeurs ont ete relues et confrontees
# aux definitions). Seule la grille est reconstituee : aucune valeur n'est modifiee.
# La region est delimitee par deux marqueurs plutot que transcrite en clair.
MARQUEUR_DEBUT = "Négation  V   F"
MARQUEUR_FIN = "4.3 Tautologie"

E10_NOUVEAU = (
    "**Négation**\n\n| P | ¬P |\n|---|---|\n| V | F |\n| F | V |\n\n"
    "**Conjonction**\n\n| P | Q | P ∧ Q |\n|---|---|---|\n"
    "| V | V | V |\n| V | F | F |\n| F | V | F |\n| F | F | F |\n\n"
    "**Disjonction inclusive**\n\n| P | Q | P ∨ Q |\n|---|---|---|\n"
    "| V | V | V |\n| V | F | V |\n| F | V | V |\n| F | F | F |\n\n"
    "**Implication**\n\n| P | Q | P → Q |\n|---|---|---|\n"
    "| V | V | V |\n| V | F | F |\n| F | V | V |\n| F | F | V |\n\n"
    "L’implication matérielle n’est donc fausse que lorsque l’hypothèse est vraie "
    "et la conclusion fausse.\n\n"
    "**Équivalence**\n\n| P | Q | P ↔ Q |\n|---|---|---|\n"
    "| V | V | V |\n| V | F | F |\n| F | V | F |\n| F | F | V |\n\n"
)


def main():
    """Applique le lot au clone de travail et emet le journal des substitutions.

    Le lot A-1 travaille en SOUS-CHAINES, pas en lignes : le document est
    aplani, un paragraphe entier tient sur une seule ligne et les
    remplacements enjambent les sauts de paragraphe. Le format ligne-a-ligne
    de `apply_patch.py` ne convient donc pas ici ; le script ecrit directement
    le fichier et produit un JOURNAL (et non un patch applicable), qui sert de
    piece de tracabilite. Le livrable opposable est le .gitdiff tire du depot.
    """
    texte = open(f"{ROOT}/{FICHIER}", encoding="utf-8").read()
    avant = len(texte)
    journal = []

    for ident, ancien, nouveau, conf, just, val in EDITS:
        n = texte.count(ancien)
        if n != 1:
            raise SystemExit(f"ECHEC [{ident}] : sous-chaine trouvee {n} fois "
                             f"(attendu 1) : {ancien[:70]!r}")
        texte = texte.replace(ancien, nouveau, 1)
        journal.append({"identifiant": ident, "confiance": conf,
                        "ancien": ancien, "nouveau": nouveau,
                        "justification": just, "validation": val})

    # --- les cinq tables de verite (A1-04 a A1-09) ----------------------
    ia, ib = texte.find(MARQUEUR_DEBUT), texte.find(MARQUEUR_FIN)
    if ia < 0 or ib <= ia:
        raise SystemExit(f"ECHEC [A1-04..09] : marqueurs introuvables ({ia}, {ib})")
    journal.append({
        "identifiant": "A1-04..A1-09", "confiance": H,
        "ancien": texte[ia:ib], "nouveau": E10_NOUVEAU.rstrip("\n"),
        "justification": "Les cinq tables de verite du §4.2 sont EN PLACE et "
                         "EXACTES : les 60 valeurs ont ete relues et confrontees aux "
                         "definitions, y compris l'implication materielle. Seule la "
                         "grille est reconstituee ; aucune valeur n'est modifiee. "
                         "L'en-tete de la table d'equivalence (P Q P ↔ Q) est absent "
                         "et restitue par symetrie avec les quatre autres.",
        "validation": "Verification, non restitution : le lot ne fait que rendre "
                      "leur forme tabulaire a des valeurs deja correctes."})
    texte = texte[:ia] + E10_NOUVEAU + texte[ib:]

    open(f"{ROOT}/{FICHIER}", "w", encoding="utf-8").write(texte)

    path = "docs/restauration/propositions/domaine-A-lot1.journal.json"
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(journal, fh, ensure_ascii=False, indent=1)

    n_h = sum(1 for e in journal if e["confiance"] == H)
    n_m = sum(1 for e in journal if e["confiance"] == M)
    print(f"{len(journal)} substitutions appliquees — {n_h} haute, {n_m} moyenne")
    print(f"{avant} -> {len(texte)} caracteres ({len(texte) - avant:+d})")
    print(f"journal : {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
