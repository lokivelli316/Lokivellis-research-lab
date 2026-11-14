#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,zipfile

ROOT=pathlib.Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
DIST.mkdir(exist_ok=True)
NAME="Lokivelli_Research_Forge_PUBLIC_0.2.0_20261114"
ZIP=DIST/f"{NAME}.zip"
MANIFEST=DIST/f"{NAME}.SHA256_MANIFEST.json"

skip_parts={".git","dist","runtime","node_modules","__pycache__"}
skip_prefixes=("workspace/logs/","workspace/pids/","workspace/exports/private/")
files=[]
for p in sorted(ROOT.rglob("*")):
    if not p.is_file():
        continue
    rel=p.relative_to(ROOT).as_posix()
    if any(part in skip_parts for part in p.parts):
        continue
    if any(rel.startswith(prefix) for prefix in skip_prefixes):
        continue
    data=p.read_bytes()
    files.append({
        "path":rel,
        "bytes":len(data),
        "sha256":hashlib.sha256(data).hexdigest(),
    })

MANIFEST.write_text(json.dumps({
    "schema":"lokivelli.research_forge.public_release_manifest.v1",
    "release":NAME,
    "keyless_public_build":True,
    "file_count":len(files),
    "files":files,
},indent=2)+"\n",encoding="utf-8")

with zipfile.ZipFile(ZIP,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for item in files:
        z.write(ROOT/item["path"],f"{NAME}/{item['path']}")
    z.write(MANIFEST,f"{NAME}/SHA256_MANIFEST.json")

zip_hash=hashlib.sha256(ZIP.read_bytes()).hexdigest()
(DIST/f"{NAME}.zip.sha256").write_text(f"{zip_hash}  {ZIP.name}\n",encoding="utf-8")
print(f"PUBLIC RELEASE PACKAGE PASS: {ZIP}")
print(f"files={len(files)} sha256={zip_hash}")
