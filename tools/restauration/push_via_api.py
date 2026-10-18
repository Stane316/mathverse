#!/usr/bin/env python3
"""Crée une branche sur GitHub via l'API, quand `git push` est refusé.

Écrit pour le dépôt de connaissances, où `git push` renvoie
`403 — Permission to Stane316/my-own-connaissance.git denied`.
**État au 2026-10-18 : l'API renvoie elle aussi 403 — « Resource not accessible by
integration »** (le jeton disponible n'est autorisé que sur `mathverse`). Le script est
conservé pour le jour où l'accès sera accordé, et à titre de preuve de la tentative.

Aucun contournement : GitHub applique ses propres permissions sur l'API comme sur git.
Ce script ne fait qu'utiliser un jeton que vous avez vous-même autorisé.

    python3 push_via_api.py --repo Stane316/my-own-connaissance \
        --branch arena/restauration-equations \
        --root /chemin/vers/clone \
        --message-file msg.txt \
        --path "Maths/... .md" --path RESTAURATION-EQUATIONS.md

Crée un commit unique au-dessus de la branche par défaut et la référence
correspondante. Ne touche à aucune autre branche, ne crée aucune pull request.
"""
import argparse
import base64
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"


def token():
    t = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not t:
        t = subprocess.run(["gh", "auth", "token"], capture_output=True,
                           text=True, check=True).stdout.strip()
    return t


def call(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(f"{API}{path}", data=data, method=method)
    req.add_header("Authorization", f"Bearer {token()}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read() or b"{}")
    except urllib.error.HTTPError as exc:
        print(f"  HTTP {exc.code} sur {method} {path}", file=sys.stderr)
        print("  " + (exc.read().decode()[:600] or ""), file=sys.stderr)
        raise SystemExit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--branch", required=True)
    ap.add_argument("--root", required=True)
    ap.add_argument("--message-file", required=True)
    ap.add_argument("--path", action="append", default=[])
    args = ap.parse_args()

    default = call("GET", f"/repos/{args.repo}")["default_branch"]
    base_sha = call("GET", f"/repos/{args.repo}/git/ref/heads/{default}")["object"]["sha"]
    base_tree = call("GET", f"/repos/{args.repo}/git/commits/{base_sha}")["tree"]["sha"]
    print(f"base : {default} @ {base_sha[:10]}")

    tree = []
    for rel in args.path:
        full = os.path.join(args.root, rel)
        if not os.path.exists(full):
            print(f"  ignoré (absent) : {rel}", file=sys.stderr)
            continue
        with open(full, "rb") as fh:
            content = fh.read()
        blob = call("POST", f"/repos/{args.repo}/git/blobs", {
            "content": base64.b64encode(content).decode(),
            "encoding": "base64",
        })
        tree.append({"path": rel, "mode": "100644", "type": "blob", "sha": blob["sha"]})
        print(f"  blob {blob['sha'][:10]}  {rel}  ({len(content)} o)")

    new_tree = call("POST", f"/repos/{args.repo}/git/trees",
                    {"base_tree": base_tree, "tree": tree})["sha"]
    with open(args.message_file, encoding="utf-8") as fh:
        message = fh.read()
    commit = call("POST", f"/repos/{args.repo}/git/commits",
                  {"message": message, "tree": new_tree, "parents": [base_sha]})
    print("commit :", commit["sha"][:10])

    ref = call("POST", f"/repos/{args.repo}/git/refs",
               {"ref": f"refs/heads/{args.branch}", "sha": commit["sha"]})
    print("branche :", ref["ref"], "créée")
    print(f"https://github.com/{args.repo}/tree/{args.branch}")


if __name__ == "__main__":
    main()
