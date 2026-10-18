#!/usr/bin/env python3
"""Rendu markdown d'un lot de restauration a partir de son correctif JSON.

    python3 render_lot.py domaine-L.patch.json > propositions/domaine-L.md   (corps technique)

Le script ne fait qu'assembler : le contenu (justifications, validations,
candidats) vient du correctif. Aucune ecriture hors de la sortie standard.
"""
import json
import sys


def cell(s, n=999):
    if s is None:
        return "—"
    return s.replace("\n", " ⏎ ").replace("|", "\\|")[:n]


def main():
    path = sys.argv[1]
    d = json.load(open(path, encoding="utf-8"))
    doc = sys.argv[2] if len(sys.argv) > 2 else path
    tiers = ["haute", "moyenne", "inconnue"]
    print(f"**Correctif :** `{doc.split('/')[-1]}` — {len(d)} entrées : "
          + ", ".join(f"{sum(1 for e in d if e['confiance'] == t)} {t}"
                      for t in tiers)
          + f" — **{sum(1 for e in d if e['nouveau'])} applicables**")
    print()
    for t in tiers:
        rows = [e for e in d if e["confiance"] == t]
        if not rows:
            continue
        titre = {"haute": "Confiance haute", "moyenne": "Confiance moyenne",
                 "inconnue": "Confiance inconnue — décision requise"}[t]
        print(f"### {titre} ({len(rows)})")
        print()
        if t == "inconnue":
            print("| Ligne | Bloc actuel | Ce que le bloc contenait |")
            print("|---:|---|---|")
            for e in rows:
                just = e["justification"].replace(
                    "Bloc vide ou ininterpretable : ", "").replace(
                    ". Le contenu d'origine n'existe plus dans le fichier.", "")
                print(f"| {e['ligne']} | `{cell(e['ancien'], 40)}` | {cell(just, 160)} |")
        else:
            print("| Ligne | Actuel | Reconstruction | Validation |")
            print("|---:|---|---|---|")
            for e in rows:
                print(f"| {e['ligne']} | `{cell(e['ancien'], 46)}` | `{cell(e['nouveau'], 62)}` "
                      f"| {cell(e['validation'], 130)} |")
        print()


if __name__ == "__main__":
    main()
