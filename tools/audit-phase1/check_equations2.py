#!/usr/bin/env python3
"""Integrite des equations: comptage par heuristique separee (pas de score composite)."""
import os, re, sys, csv
SRC, OUT = sys.argv[1], sys.argv[2]
RE_DISPLAY = re.compile(r"\\\[(.+?)\\\]", re.S)
H = {
 "vide_ou_blanc":   lambda e: len(e.strip()) == 0,
 "commence_par_egal": lambda e: re.match(r"^\s*=", e.strip()) is not None,
 "finit_par_egal":  lambda e: re.search(r"=\s*$", e.strip()) is not None,
 "indice_orphelin": lambda e: re.search(r"(^|\s)_\s*[\{\[]", e) is not None,
 "fragment_commande": lambda e: re.search(r"\\_|_{[a-zA-Z0-9]}_|\\\(|\\\)", e) is not None,
 "parentheses_vides": lambda e: re.search(r"\(\s*\)", e) is not None,
 "courte_ambigue":  lambda e: 0 < len(e.strip()) < 6,
}
rows = []
for root, dirs, fs in os.walk(SRC):
    dirs[:] = [d for d in dirs if d != ".git"]
    for f in sorted(fs):
        if not f.lower().endswith(".md"): continue
        p = os.path.join(root, f)
        txt = open(p, encoding="utf-8", errors="replace").read()
        disp = [m.group(1).strip() for m in RE_DISPLAY.finditer(txt)]
        if not disp: continue
        c = {k: sum(1 for e in disp if fn(e)) for k, fn in H.items()}
        # doublons possibles entre heuristiques: on compte l'union "structurelle"
        struct = sum(1 for e in disp if any(H[k](e) for k in
            ("vide_ou_blanc","commence_par_egal","finit_par_egal","indice_orphelin","fragment_commande","parentheses_vides")))
        rows.append({"fichier": os.path.relpath(p, SRC), "eq_display": len(disp),
                     "structurellement_incompletes": struct,
                     "pct": round(100*struct/len(disp), 1), **c,
                     "exemples": " || ".join(e[:55] for e in disp if any(H[k](e) for k in
                        ("vide_ou_blanc","commence_par_egal","finit_par_egal","indice_orphelin","fragment_commande","parentheses_vides")))[:400]})
with open(OUT, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
T = sum(r["eq_display"] for r in rows); S = sum(r["structurellement_incompletes"] for r in rows)
print(f"TOTAL display: {T} | structurellement incompletes: {S} ({round(100*S/T,1)} %)")
tot = {k: sum(r[k] for r in rows) for k in H}
print("par heuristique:", {k: v for k, v in tot.items()})
print()
for r in sorted(rows, key=lambda x: -x["pct"])[:14]:
    print(f'{r["fichier"][:46]:<48} {r["eq_display"]:>4} eq | {r["structurellement_incompletes"]:>4} incompl. ({r["pct"]:>4} %)')
