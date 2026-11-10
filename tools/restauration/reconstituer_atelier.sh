#!/usr/bin/env bash
# Reconstitue l'atelier apres une reinitialisation du sandbox.
#
# Le sandbox ne persiste que /home/user/mathverse. Deux choses peuvent
# disparaitre a chaque tour :
#   1. le .git local, ramene au clone d'origine (bdba473) — les fichiers
#      survivent mais deviennent non suivis ;
#   2. /home/user/_audit/ integralement (clone du corpus, sauvegardes).
#
# Rien n'est perdu : origin porte la branche, et le corpus se reclone.
# Ce script rejoue la procedure de CLOTURE-CHANTIER.md §6.
#
# Usage : bash tools/restauration/reconstituer_atelier.sh
# Idempotent : peut etre relance sans risque.

set -u

BRANCHE="arena/2e20eccb-mathverse"
CORPUS="https://github.com/Stane316/my-own-connaissance.git"
COMMIT_CORPUS="f0f5e2d"

# Racine du depot = trois niveaux au-dessus de tools/restauration/
RACINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CLONE="/home/user/_audit/connaissance"
LIVRABLES="$RACINE/docs/restauration/livrables"

echo "=== 1. Branche : recuperation depuis origin ==="
git -C "$RACINE" fetch -q origin "$BRANCHE"
git -C "$RACINE" reset -q --mixed "origin/$BRANCHE"
echo "    HEAD : $(git -C "$RACINE" log --oneline -1)"
echo "    arbre : $(git -C "$RACINE" status --short | wc -l) fichier(s) modifie(s)"

echo
echo "=== 2. Clone du corpus de connaissances ==="
if [ ! -d "$CLONE/.git" ]; then
    git clone -q "$CORPUS" "$CLONE"
fi
git -C "$CLONE" checkout -q "$COMMIT_CORPUS"
echo "    $CLONE @ $(git -C "$CLONE" log --oneline -1)"

echo
echo "=== 3. Reapplication des 17 diffs (ordre NON interchangeable) ==="
# Ordre de CLOTURE-CHANTIER.md §6 : au sein d'un lot, numeros de ligne les
# plus eleves d'abord ; le lot 5c est imbrique dans le lot 5b.
ORDRE="domaine-K-lot1 domaine-K-lot1bis domaine-L domaine-L-lot2bis \
domaine-I-lot3b domaine-I-lot3a domaine-I-lot3c domaine-N-lot4b \
domaine-N-lot4a domaine-J-lot5b domaine-J-lot5c domaine-J-lot5a \
domaine-L-lot6a domaine-N-lot6a domaine-I-lot6b domaine-L-lot6b \
domaine-N-lot6b"

n=0; e=0
for d in $ORDRE; do
    if git -C "$CLONE" apply --check "$LIVRABLES/$d.gitdiff" 2>/dev/null; then
        git -C "$CLONE" apply "$LIVRABLES/$d.gitdiff" && n=$((n+1))
    else
        echo "    ECHEC --check : $d"; e=$((e+1))
    fi
done
echo "    appliques : $n/17  (echecs : $e)"

echo
echo "=== 4. Domaine A : les 6 lots, INCREMENTAUX (ordre 1 -> 6) ==="
n=0; e=0
for d in domaine-A-lot1 domaine-A-lot2 domaine-A-lot3 domaine-A-lot4 \
         domaine-A-lot5 domaine-A-lot6; do
    if git -C "$CLONE" apply "$LIVRABLES/$d.gitdiff" 2>/dev/null; then
        n=$((n+1))
    else
        echo "    ECHEC : $d"; e=$((e+1))
    fi
done
echo "    appliques : $n/6  (echecs : $e)"

echo
echo "=== 5. Verification ==="
python3 - "$CLONE" <<'PY'
import glob, os, sys
racine = sys.argv[1]
mauvais = ('Ã©', 'Ã¨', 'Ã ', 'â€™', 'â€œ', 'â€”', 'Ã§')
souilles = 0
for f in glob.glob(os.path.join(racine, '**', '*.md'), recursive=True):
    t = open(f, encoding='utf-8').read()
    if [s for s in mauvais if s in t]:
        souilles += 1
        print('    MOJIBAKE :', os.path.basename(f))
print('    mojibake :', souilles, 'fichier(s)')

f = glob.glob(os.path.join(racine, '**', 'DOCUMENT MA*.md'), recursive=True)
if f:
    t = open(f[0], encoding='utf-8').read()
    attendu = 78756
    etat = 'OK' if len(t) == attendu else 'ATTENDU %d' % attendu
    print('    A = %d caracteres  (%s)' % (len(t), etat))
PY

echo
echo "=== 6. Point de reprise ==="
mkdir -p /home/user/_audit/sauvegardes
python3 - <<'PY'
import glob, shutil
f = glob.glob('/home/user/_audit/connaissance/**/DOCUMENT MA*.md', recursive=True)
if f:
    shutil.copy(f[0], '/home/user/_audit/sauvegardes/A-apres-domaine-A-lot6.md')
    print('    sauvegarde : A-apres-domaine-A-lot6.md')
PY

echo
echo "Atelier reconstitue."
