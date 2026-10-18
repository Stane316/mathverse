#!/usr/bin/env python3
"""Detection des equations tronquees dans le corpus (Phase 1, outil d'audit).
Heuristiques: reste d'une commande LaTeX supprimee, membre de gauche absent,
equation vide ou reduite a un symbole. Deterministe, sans reseau.
"""
import os, re, sys, json, csv

SRC = sys.argv[1]; OUT = sys.argv[2]
RE_DISPLAY = re.compile(r"\\\[(.+?)\\\]", re.S)
RE_INLINE = re.compile(r"\\\((.+?)\\\)", re.S)

# motifs d'equation manifestement incomplete
PAT = [
    ("membre gauche absent (commence par =)", re.compile(r"^\s*=")),
    ("termine par = (membre droit vide)", re.compile(r"=\s*$")),
    ("indice orphelin '_ {' ou '_{' sans base", re.compile(r"(^|\s|_{})\s*_\s*[\{\[]")),
    ("longueur < 6 caracteres", None),
    ("fragment de commande (\\_ , _{n}_)", re.compile(r"\\_|_{[a-zA-Z0-9]}_")),
    ("parentheses vides", re.compile(r"\(\s*\)|\\\(\s*\\\)")),
]

def suspect(e):
    e2 = e.strip()
    r = []
    for label, pat in PAT:
        if label.startswith("longueur"):
            if len(e2) < 6:
                r.append(label)
        elif pat.search(e2):
            r.append(label)
    return r

rows = []
for root, dirs, fs in os.walk(SRC):
    dirs[:] = [d for d in dirs if d != ".git"]
    for f in sorted(fs):
        if not f.lower().endswith(".md"):
            continue
        p = os.path.join(root, f)
        txt = open(p, encoding="utf-8", errors="replace").read()
        disp = [m.group(1) for m in RE_DISPLAY.finditer(txt)]
        inl = [m.group(1) for m in RE_INLINE.finditer(txt)]
        susp = [(e, suspect(e)) for e in disp]
        susp = [(e, r) for e, r in susp if r]
        rows.append({"fichier": os.path.relpath(p, SRC), "eq_display": len(disp),
                     "eq_suspectes": len(susp), "pct": round(100 * len(susp) / len(disp), 1) if disp else 0.0,
                     "eq_inline": len(inl),
                     "exemples": " || ".join(f"{e[:60]} [{'; '.join(r)}]" for e, r in susp[:4])})

with open(OUT, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

tot = sum(r["eq_display"] for r in rows); tot_s = sum(r["eq_suspectes"] for r in rows)
print(f"TOTAL equations display: {tot} | suspectes: {tot_s} ({round(100*tot_s/tot,1)} %)")
print()
print(f"{'fichier':<52} {'eq':>5} {'susp':>5} {'%':>6}")
for r in sorted(rows, key=lambda x: -x["pct"]):
    print(f"{r['fichier'][:50]:<52} {r['eq_display']:>5} {r['eq_suspectes']:>5} {r['pct']:>6}")
