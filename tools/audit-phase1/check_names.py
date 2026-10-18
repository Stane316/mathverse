#!/usr/bin/env python3
"""Sonde de disponibilite de noms (npm, PyPI, GitHub) — outil d'audit.
Reseau limite aux hotes autorises. Aucune ecriture hors du fichier de sortie.
"""
import json, urllib.request, urllib.error, sys
from concurrent.futures import ThreadPoolExecutor
UA = {"User-Agent": "audit-noms/1.0"}
TIMEOUT = 12
def get(url):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""
def probe(name):
    npm = get(f"https://registry.npmjs.org/{name}")[0]
    pypi = get(f"https://pypi.org/pypi/{name}/json")[0]
    gh = get(f"https://api.github.com/repos/Stane316/{name}")[0]
    return {"nom": name,
            "npm": "libre" if npm == 404 else ("PRIS" if npm == 200 else f"?{npm}"),
            "pypi": "libre" if pypi == 404 else ("PRIS" if pypi == 200 else f"?{pypi}"),
            "gh_stane316": "libre" if gh == 404 else ("PRIS" if gh == 200 else f"?{gh}")}
AXES = json.load(open(sys.argv[1]))
names = [n for axis in AXES.values() for n in axis]
with ThreadPoolExecutor(max_workers=6) as ex:
    res = list(ex.map(probe, names))
libres = [r for r in res if r["npm"] == "libre" and r["pypi"] == "libre" and r["gh_stane316"] == "libre"]
print(f"testes: {len(res)} | libres sur les 3 registres: {len(libres)}\n")
for axe, ns in AXES.items():
    print(f"--- {axe}")
    for n in ns:
        r = next(x for x in res if x["nom"] == n)
        ok = "OK  " if (r["npm"]=="libre" and r["pypi"]=="libre" and r["gh_stane316"]=="libre") else "    "
        print(f" {ok} {n:<16} npm:{r['npm']:<5} pypi:{r['pypi']:<5} gh:{r['gh_stane316']}")
json.dump(res, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
