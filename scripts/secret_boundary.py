#!/usr/bin/env python3
from __future__ import annotations
import pathlib,re,sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
SKIP={".git","runtime","node_modules"}
patterns=[
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}",re.I),
]
hits=[]
for p in ROOT.rglob("*"):
    if not p.is_file() or any(part in SKIP for part in p.parts):
        continue
    if p.name==".env.example":
        continue
    try: text=p.read_text(encoding="utf-8")
    except Exception: continue
    for pat in patterns:
        if pat.search(text):
            hits.append(str(p.relative_to(ROOT)))
            break
if hits:
    print("SECRET BOUNDARY FAIL:", *hits, sep="\n - ")
    sys.exit(1)
print("SECRET BOUNDARY PASS")
