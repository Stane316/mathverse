#!/usr/bin/env python3
"""Digest d'un document du depot de connaissances, pour redaction de fiche Phase 1.
Sortie: plan (titres + lignes), equations par section, marqueurs de rigueur par section.
Deterministe, sans reseau, aucune ecriture dans la source.
"""
import re, sys, os

SRC = sys.argv[1]
OUTDIR = sys.argv[2]
MAX_EQ = int(sys.argv[3]) if len(sys.argv) > 3 else 60

txt = open(SRC, encoding="utf-8", errors="replace").read()
lines = txt.splitlines()
name = os.path.splitext(os.path.basename(SRC))[0]

RE_TITLE = re.compile(r"^\s{0,3}(#{1,6})\s+(.*\S)")
RE_DISPLAY = re.compile(r"\\\[(.+?)\\\]", re.S)
RE_INLINE = re.compile(r"\\\((.+?)\\\)", re.S)
MARQUEURS = ["hypoth", "limite", "condition", "paramètre", "paramètre", "algorithme",
             "exemple", "validation", "test", "erreur", "convergence", "implément", "implément"]

# plan
plan = []
for i, l in enumerate(lines, 1):
    m = RE_TITLE.match(l)
    if m:
        plan.append((i, len(m.group(1)), m.group(2).strip()))

def section_of(n):
    cur = "(hors titre)"
    for ln, lvl, t in plan:
        if ln <= n:
            cur = t
        else:
            break
    return cur

# equations display avec leur section + position
eqs = []
for m in RE_DISPLAY.finditer(txt):
    ligne = txt[:m.start()].count("\n") + 1
    # ignorer le faux positifLine pour les blocs contenant \begin
    eqs.append((ligne, m.group(1).strip().replace("\n", " ")[:220], section_of(ligne)))

# decoupage du texte par sections pour le comptage de marqueurs
bounds = [(ln, t) for ln, lvl, t in plan] + [(len(lines) + 1, "__FIN__")]
sec_stats = {}
for idx in range(len(bounds) - 1):
    a, titre = bounds[idx]
    b = bounds[idx + 1][0]
    bloc = "\n".join(lines[a - 1:b - 1]).lower()
    if len(bloc.strip()) < 40:
        continue
    n_eq = sum(1 for (l, e, s) in eqs if a <= l < b)
    stats = {k: len(re.findall(k, bloc)) for k in MARQUEURS}
    sec_stats[titre] = (b - a, n_eq, stats)

out = []
out.append(f"# DIGEST — {name}")
out.append(f"source: {os.path.basename(SRC)} | lignes: {len(lines)} | titres: {len(plan)} | equations display: {len(eqs)}")
out.append("")
out.append("## 1. Plan")
for ln, lvl, t in plan:
    out.append(f"{'  ' * (lvl - 1)}- L{ln} [h{lvl}] {t[:110]}")
out.append("")
out.append("## 2. Sections > 40 lignes : volume, equations, marqueurs")
out.append("| section | lignes | eq | " + " | ".join(MARQUEURS) + " |")
out.append("|---" * (3 + len(MARQUEURS)) + "|")
for titre, (n, neq, st) in sec_stats.items():
    out.append(f"| {titre[:70]} | {n} | {neq} | " + " | ".join(str(st[k]) for k in MARQUEURS) + " |")
out.append("")
out.append(f"## 3. Equations display ({min(len(eqs), MAX_EQ)} premieres)")
for l, e, s in eqs[:MAX_EQ]:
    out.append(f"- L{l} [{s[:60]}] : `{e}`")
if len(eqs) > MAX_EQ:
    out.append(f"- … et {len(eqs) - MAX_EQ} autres equations non listees")

os.makedirs(OUTDIR, exist_ok=True)
slug = re.sub(r"[^a-z0-9]+", "-", name.lower())
open(os.path.join(OUTDIR, f"{slug}.md"), "w").write("\n".join(out))
print(f"{name}: {len(plan)} titres, {len(eqs)} equations, {len(sec_stats)} sections > 40 lignes")
