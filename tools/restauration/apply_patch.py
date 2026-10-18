#!/usr/bin/env python3
"""Applique un correctif de restauration (JSON) sur un dépôt de connaissances.

Principe : **vérification stricte**. Chaque entrée indique un numéro de ligne et le
bloc exact attendu (`ancien`). Si le bloc ne correspond pas, l'application est
interrompue et rien n'est écrit : on corrige le correctif, jamais le fichier à
l'aveugle.

Entrées à appliquer dans l'ordre DÉCROISSANT des lignes, afin que les numéros de
ligne des entrées non encore appliquées restent valides.

Usage :
    python3 apply_patch.py --patch propositions/domaine-K.patch.json \
                           --root /chemin/my-own-connaissance            # vérification seule
    python3 apply_patch.py --patch ... --root ... --apply                # écriture
    python3 apply_patch.py --patch ... --root ... --apply --rapport r.md # + rapport

Le script n'écrit rien hors des fichiers listés dans le correctif, sauf le
rapport demandé. Aucun accès réseau.
"""
import argparse
import json
import sys
from collections import defaultdict
from datetime import date


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def check(entries, root, apply_changes):
    """Vérifie (et éventuellement applique) les entrées. Retourne (rapport, erreurs)."""
    by_file = defaultdict(list)
    for e in entries:
        by_file[e["fichier"]].append(e)

    errors, report = [], []

    for fichier, ents in by_file.items():
        path = f"{root}/{fichier}"
        try:
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
        except OSError as exc:
            errors.append(f"{fichier} : lecture impossible ({exc})")
            continue

        lines = content.split("\n")
        pending = [e for e in ents if e.get("nouveau")]
        skipped = [e for e in ents if not e.get("nouveau")]

        for e in sorted(pending, key=lambda x: -x["ligne"]):
            n = e["ligne"] - 1
            old = e["ancien"].split("\n")
            got = lines[n:n + len(old)]
            if got != old:
                errors.append(
                    f"{fichier} l.{e['ligne']} : le bloc attendu ne correspond pas.\n"
                    f"    attendu : {old!r}\n    trouvé  : {got!r}"
                )
                continue
            new = e["nouveau"].split("\n")
            lines[n:n + len(old)] = new
            report.append({
                "fichier": fichier,
                "ligne_avant": e["ligne"],
                "confiance": e.get("confiance", "?"),
                "ancien": e["ancien"],
                "nouveau": e["nouveau"],
                "delta": len(new) - len(old),
            })

        if errors:
            continue  # rien n'est écrit si la moindre entrée échoue

        # numéros de ligne après application
        for r in report:
            if r["fichier"] != fichier:
                continue
            r["ligne_apres"] = r["ligne_avant"] + sum(
                o["delta"] for o in report
                if o["fichier"] == fichier and o["ligne_avant"] < r["ligne_avant"]
            )

        if apply_changes:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("\n".join(lines))

        for e in skipped:
            report.append({
                "fichier": fichier,
                "ligne_avant": e["ligne"],
                "confiance": e.get("confiance", "?"),
                "ancien": e["ancien"],
                "nouveau": None,
                "delta": 0,
                "ligne_apres": e["ligne"],
                "statut": e.get("statut", "non_applique"),
            })

    report.sort(key=lambda r: (r["fichier"], r["ligne_avant"]))
    return report, errors


def render(report, entries, patch, apply_changes):
    out = [f"# Rapport d'application — {patch}", "",
           f"**Date :** {date.today().isoformat()} — "
           f"**Mode :** {'écriture' if apply_changes else 'vérification seule'}", "",
           f"Entrées du correctif : {len(entries)} — appliquées : "
           f"{sum(1 for r in report if r['nouveau'])}", "",
           "| Fichier | L. avant | L. après | Confiance | Ancien | Nouveau |",
           "|---|---:|---:|---|---|---|"]
    for r in report:
        old = r["ancien"].replace("\n", " âµ ").replace("|", "\\|")[:60]
        new = (r["nouveau"] or "—").replace("\n", " âµ ").replace("|", "\\|")[:80]
        out.append(f"| {r['fichier'].split('/')[-1]} | {r['ligne_avant']} | "
                   f"{r.get('ligne_apres', '')} | {r['confiance']} | `{old}` | `{new}` |")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--patch", required=True)
    ap.add_argument("--root", required=True, help="racine du dépôt de connaissances")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--rapport")
    args = ap.parse_args()

    entries = load(args.patch)
    report, errors = check(entries, args.root, args.apply)

    if errors:
        print("ÉCHEC — aucune écriture. Anomalies :", file=sys.stderr)
        for e in errors:
            print("  - " + e, file=sys.stderr)
        return 2

    print(f"OK — {len(entries)} entrées vérifiées, "
          f"{sum(1 for r in report if r['nouveau'])} à appliquer "
          f"({'ÉCRIT' if args.apply else 'vérification seule'}).")
    for r in report:
        flag = "" if r["nouveau"] else "  [non appliqué]"
        print(f"  l.{r['ligne_avant']:>5} -> {r.get('ligne_apres','')!s:>5}  "
              f"{r['confiance']:<9} {r['ancien'][:40]!r} -> {str(r['nouveau'])[:50]!r}{flag}")

    if args.rapport:
        with open(args.rapport, "w", encoding="utf-8") as fh:
            fh.write(render(report, entries, args.patch, args.apply))
        print(f"rapport : {args.rapport}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
