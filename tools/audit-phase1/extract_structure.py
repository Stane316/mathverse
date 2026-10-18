#!/usr/bin/env python3
"""Extraction structurale du depot de connaissances (Phase 1, outil d'audit)."""
import csv, os, re, sys, json
SRC = sys.argv[1]; OUT = sys.argv[2]
RE_TITLE = re.compile(r"^\s{0,3}#{1,6}\s+\S")
RE_INLINE_EQ = re.compile(r"\\\(.+?\\\)", re.S)
RE_DISPLAY_EQ = re.compile(r"\\\[.+?\\\]", re.S)
RE_CODE = re.compile(r"^```", re.M)
RE_TABLE = re.compile(r"^\|.*\|$", re.M)
RE_ITEM = re.compile(r"^\s*[-*+]\s+\S", re.M)
RIGUEUR = {"hypothese": r"hypoth[eè]se","limite": r"\blimite","condition": r"condition",
 "convergence": r"convergence|converge","stabilite": r"stabilit[eé]|stable","erreur": r"erreur",
 "validation": r"validation|valider","test": r"\btest","exemple": r"exemple","algorithme": r"algorithme",
 "complexite": r"complexit[eé]","theoreme": r"th[eé]or[eè]me","preuve_demo": r"d[eé]monstration|preuve",
 "implementation": r"impl[eé]mentation|impl[eé]menter","contrexemple": r"contre-exemple|contre exemple",
 "precision": r"pr[eé]cision","approximation": r"approximation|approxime",
 "reference_bib": r"\[web:\d+\]|r[eé]f[eé]rence|bibliographie|source\s*:"}
rows, files = [], []
for root, dirs, fs in os.walk(SRC):
    dirs[:] = [d for d in dirs if d != ".git"]
    files += [os.path.join(root, f) for f in fs if f.lower().endswith(".md")]
files.sort()
for p in files:
    raw = open(p, "rb").read(); txt = raw.decode("utf-8", "replace"); lines = txt.splitlines()
    low = txt.lower()
    rows.append({"fichier": os.path.relpath(p, SRC), "collection": os.path.basename(os.path.dirname(p)),
        "octets": len(raw), "lignes": len(lines),
        "titres_md": sum(1 for l in lines if RE_TITLE.match(l)),
        "eq_inline": len(RE_INLINE_EQ.findall(txt)), "eq_display": len(RE_DISPLAY_EQ.findall(txt)),
        "blocs_code": len(RE_CODE.findall(txt)) // 2, "lignes_table": len(RE_TABLE.findall(txt)),
        "items_liste": len(RE_ITEM.findall(txt)),
        **{k: len(re.findall(v, low)) for k, v in RIGUEUR.items()}})
with open(OUT, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
tot = {k: sum(r[k] for r in rows) for k in rows[0] if k not in ("fichier", "collection")}
print(f"{len(rows)} documents")
for k, v in tot.items(): print(f"  {k:>14} : {v}")
json.dump({"totaux": tot, "documents": rows}, open(OUT.replace(".csv", ".json"), "w"), ensure_ascii=False, indent=1)
