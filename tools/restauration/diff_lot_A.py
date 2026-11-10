#!/usr/bin/env python3
"""Produit le diff incremental d'un lot du document A.

Pourquoi un outil
-----------------
Le depot de connaissances n'a qu'un seul commit (`f0f5e2d`) : les
restaurations n'y existent pas, elles ne vivent que dans les diffs de
`livrables/`. Le porteur les applique donc lui-meme, DANS L'ORDRE. Chaque
lot doit par consequent etre livre en diff INCREMENTAL — applicable sur
l'etat issu du lot precedent — et non en diff contre `f0f5e2d`.

L'outil entretient un depot temoin (`/home/user/_audit/diff-lotA`) qui
reconstruit la chaine :

    f0f5e2d -> + lot 1 -> + lot 2 -> + lot 3 -> ...

et en tire le diff du dernier lot. Il verifie ensuite que ce diff
s'applique bien sur l'etat precedent (`git apply --check`).

Usage
-----
    python3 tools/restauration/diff_lot_A.py 3

Le fichier cible est relu depuis le clone de travail ; l'outil ne modifie
que le depot temoin.
"""

import os
import shutil
import subprocess
import sys

CLONE = "/home/user/_audit/connaissance"
REPO = "/home/user/_audit/diff-lotA"
REL = ("Maths-vers-Informatiques/DOCUMENT MAÎTRE A — "
       "LOGIQUE ET FONDEMENTS DE L’INFORMATIQUE.md")
# memo : tools/restauration/diff_lot_A.py -> trois niveaux jusqu'a la racine
RACINE_DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
G = ["git", "-c", "user.name=restauration", "-c", "user.email=restauration@local"]


def run(*args):
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode:
        sys.exit("ECHEC : %s\n%s" % (" ".join(args[:5]), r.stderr.strip()[:500]))
    return r.stdout


def amorcer():
    """Cree le depot temoin et le cale sur f0f5e2d."""
    shutil.rmtree(REPO, ignore_errors=True)
    os.makedirs(os.path.dirname(os.path.join(REPO, REL)), exist_ok=True)
    run(*G, "init", "-q", REPO)
    pristine = run("git", "-C", CLONE, "show", f"HEAD:{REL}")
    open(os.path.join(REPO, REL), "w", encoding="utf-8").write(pristine)
    run(*G, "-C", REPO, "add", "-A")
    run(*G, "-C", REPO, "commit", "-qm", "A a f0f5e2d")
    return len(pristine)


def chaine(numero):
    """Amene le temoin a l'etat « lot `numero`-1 applique ».

    Les lots deja livres sont REJOUES depuis leurs diffs : c'est leur seule
    trace, le clone de travail etant deja au lot courant. L'ordre n'est pas
    interchangeable — chaque diff n'est applicable que sur son predecesseur.
    """
    if not os.path.isdir(os.path.join(REPO, ".git")):
        n = amorcer()
        print("temoin cree a f0f5e2d (%d caracteres)" % n)
    present = int(run(*G, "-C", REPO, "rev-list", "--count", "HEAD")) - 1
    for k in range(present + 1, numero):
        chemin = os.path.join(
            RACINE_DEPOT,
            "docs/restauration/livrables/domaine-A-lot%d.gitdiff" % k)
        if not os.path.exists(chemin):
            sys.exit("diff du lot %d introuvable : %s" % (k, chemin))
        run(*G, "-C", REPO, "apply", chemin)
        run(*G, "-C", REPO, "add", "-A")
        run(*G, "-C", REPO, "commit", "-qm", "A + lot %d" % k)
        print("lot %d rejoue depuis son diff" % k)
    if present > numero - 1:
        sys.exit("le temoin est en avance (%d lots) sur le lot demande (%d). "
                 "Detruire %s pour repartir de zero." % (present, numero, REPO))


def main(numero):
    chaine(numero)

    # Le lot courant : etat reel du clone de travail.
    shutil.copy2(os.path.join(CLONE, REL), os.path.join(REPO, REL))
    run(*G, "-C", REPO, "add", "-A")
    run(*G, "-C", REPO, "commit", "-qm", "A + lot %d" % numero)

    diff = run(*G, "-C", REPO, "diff", "HEAD~1", "HEAD", "--", REL)
    sortie = os.path.join(
        RACINE_DEPOT,
        "docs/restauration/livrables/domaine-A-lot%d.gitdiff" % numero)
    open(sortie, "w", encoding="utf-8").write(diff)

    # Verification : le diff s'applique sur l'etat du lot precedent.
    run(*G, "-C", REPO, "checkout", "-q", "HEAD~1", "--", REL)
    r = subprocess.run(G + ["-C", REPO, "apply", "--check", sortie],
                       capture_output=True, text=True)
    run(*G, "-C", REPO, "checkout", "-q", "HEAD", "--", REL)

    avant = open(os.path.join(REPO, REL), encoding="utf-8").read()
    print("diff lot %d : %d lignes" % (numero, diff.count("\n")))
    print("git apply --check sur l'etat lot %d : %s"
          % (numero - 1, "OK" if r.returncode == 0 else "ECHEC"))
    print("volume : %d caracteres" % len(avant))
    print("ecrit : docs/restauration/livrables/domaine-A-lot%d.gitdiff" % numero)
    return 0 if r.returncode == 0 else 1


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit("usage : python3 tools/restauration/diff_lot_A.py <numero_du_lot>")
    sys.exit(main(int(sys.argv[1])))
