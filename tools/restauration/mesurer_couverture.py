#!/usr/bin/env python3
"""Mesure directe de la couverture d'un document restaure.

Lit les fichiers, ne recompose jamais un total par arithmetique.
Compare le resultat a une table de reference fournie en argument optionnel.

Usage : python3 mesurer_couverture.py <racine_du_clone> [--reference tabelle.json]
"""
import re, sys, json, os

BLOC = re.compile(r'\\\[(.*?)\\\]', re.S)
DOCUMENTS = {
    'K': 'DOCUMENT K — FRACTALES, CHAOS & SYSTÈMES DYNAMIQUES.md',
    'L': 'DOCUMENT L — ANALYSE NUMÉRIQUE.md',
    'I': 'Domaine I - Calcul différentiel — Cartographie complète pour le machine learning.md',
    'N': 'DOCUMENT N — TRANSFORMÉES.md',
    'J': 'Domaine J — Optimisation.md',
}
RACINE_MATHS = 'Maths-vers-Informatiques'
# La table publiee dans CLOTURE-CHANTIER.md §3 (mesuree apres le lot 6b)
REFERENCE = {'K': 0, 'L': 6, 'I': 23, 'N': 5, 'J': 44}


def mesurer(chemin):
    with open(chemin, encoding='utf-8') as f:
        texte = f.read()
    blocs = BLOC.findall(texte)
    vide = point = lettre = 0
    for b in blocs:
        c = b.strip()
        if c == '':
            vide += 1
        elif c == '.':
            point += 1
        elif len(c) == 1:
            lettre += 1
    return {'blocs': len(blocs), 'vide': vide, 'point': point,
            'lettre': lettre, 'sans_contenu': vide + point}


def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    racine = sys.argv[1]
    print(f"{'Doc':<5} {'Blocs':>6} {'Vides':>6} {'Point':>6} {'Lettre':>7} "
          f"{'Ss contenu':>11} {'Attendu':>8}  Ecart")
    print('-' * 66)
    tot = {'blocs': 0, 'sans_contenu': 0}
    ecarts = []
    for cle, nom in DOCUMENTS.items():
        chemin = os.path.join(racine, RACINE_MATHS, nom)
        if not os.path.exists(chemin):
            print(f"{cle:<5} ABSENT : {chemin}"); ecarts.append(cle); continue
        r = mesurer(chemin)
        attendu = REFERENCE.get(cle)
        ecart = '' if attendu is None or r['sans_contenu'] == attendu \
            else f"  <<< {r['sans_contenu'] - attendu:+d}"
        if ecart:
            ecarts.append(cle)
        print(f"{cle:<5} {r['blocs']:>6} {r['vide']:>6} {r['point']:>6} "
              f"{r['lettre']:>7} {r['sans_contenu']:>11} {attendu:>8}{ecart}")
        tot['blocs'] += r['blocs']
        tot['sans_contenu'] += r['sans_contenu']
    print('-' * 66)
    print(f"{'TOT':<5} {tot['blocs']:>6} {'':>6} {'':>6} {'':>7} "
          f"{tot['sans_contenu']:>11} {sum(REFERENCE.values()):>8}")
    print()
    if ecarts:
        print(f"⚠️  {len(ecarts)} document(s) en ecart avec la table publiee : "
              f"{', '.join(ecarts)}")
        return 1
    print("OK — la mesure reproduit exactement la table publiee.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
