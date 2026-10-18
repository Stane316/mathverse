#!/usr/bin/env python3
"""Inventaire des equations defectueuses du corpus (chantier de restauration).

Deux modes :
  inventaire  : CSV compact (fichier, ligne, heuristique, texte de l'equation)
  contexte    : affiche, pour un fichier, chaque defaut avec son contexte avant/apres

Deterministe, sans reseau, aucune ecriture dans la source.
"""
import os, re, sys, csv, json

RE_DISPLAY = re.compile(r"\\\[(.+?)\\\]", re.S)
H = {
 "vide_ou_blanc":     lambda e: len(e.strip()) == 0,
 "commence_par_egal": lambda e: re.match(r"^\s*=", e.strip()) is not None,
 "finit_par_egal":    lambda e: re.search(r"=\s*$", e.strip()) is not None,
 "indice_orphelin":   lambda e: re.search(r"(^|\s)_\s*[\{\[]", e) is not None,
 "fragment_commande": lambda e: re.search(r"\\_|_{[a-zA-Z0-9]}_|\\\(|\\\)", e) is not None,
 "parentheses_vides": lambda e: re.search(r"\(\s*\)", e) is not None,
}

def defects(path):
    txt = open(path, encoding="utf-8", errors="replace").read()
    lines = txt.splitlines()
    out = []
    for m in RE_DISPLAY.finditer(txt):
        ligne = txt[:m.start()].count("\n") + 1
        eq = m.group(1).strip()
        hits = [k for k, fn in H.items() if fn(eq)]
        if hits:
            out.append({"ligne": ligne, "heuristiques": "+".join(hits),
                        "equation": eq[:160], "bloc": m.group(0)[:200],
                        "avant": " / ".join(l.strip() for l in lines[max(0, ligne-4):ligne-1] if l.strip())[-220:],
                        "apres": " / ".join(l.strip() for l in lines[ligne:ligne+3] if l.strip())[:220]})
    return out

def walk(src):
    for root, dirs, fs in os.walk(src):
        dirs[:] = [d for d in dirs if d != ".git"]
        for f in sorted(fs):
            if f.lower().endswith(".md"):
                yield os.path.join(root, f)

if __name__ == "__main__":
    src, mode = sys.argv[1], sys.argv[2]
    if mode == "inventaire":
        out = sys.argv[3]
        rows = []
        for p in walk(src):
            for d in defects(p):
                rows.append({"fichier": os.path.relpath(p, src), **d})
        with open(out, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        par_h = {}
        for r in rows:
            for h in r["heuristiques"].split("+"):
                par_h[h] = par_h.get(h, 0) + 1
        print(f"defauts: {len(rows)}")
        print("par heuristique:", json.dumps(par_h, ensure_ascii=False))
        par_f = {}
        for r in rows:
            par_f[r["fichier"]] = par_f.get(r["fichier"], 0) + 1
        for f, n in sorted(par_f.items(), key=lambda x: -x[1]):
            print(f"  {n:>4}  {f[:64]}")
    elif mode == "contexte":
        cible = sys.argv[3]
        lim = int(sys.argv[4]) if len(sys.argv) > 4 else 20
        n = 0
        for p in walk(src):
            if cible.lower() not in os.path.basename(p).lower():
                continue
            print(f"##### {os.path.relpath(p, src)}")
            for d in defects(p):
                n += 1
                if n > lim:
                    print(f"  … ({len(defects(p)) - lim} autres)"); break
                print(f"--- L{d['ligne']} [{d['heuristiques']}]")
                print(f"    bloc   : {d['bloc']}")
                print(f"    avant  : {d['avant']}")
                print(f"    apres  : {d['apres']}")
