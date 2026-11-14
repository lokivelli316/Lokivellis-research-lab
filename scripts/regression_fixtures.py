#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
errors=[]

def must(path:str):
    p=ROOT/path
    if not p.exists() or (p.is_file() and p.stat().st_size==0):
        errors.append(f"missing/empty: {path}")
    return p

for path in [
    "index.html",
    "apps/throat/index.html",
    "apps/throat-extreme/index.html",
    "research/bulk_interference_v02/WORKBENCH.html",
    "research/bulk_interference_v02/DERIVATION_LEDGER.md",
    "research/bulk_interference_v02/MATRIX_TENSOR_ATTACK.md",
    "federation/DONOR_REGISTER.md",
    "federation/donors.manifest.json",
    "deep-research/NEXT_RUN_BRIEF.md",
    "zenodo/ZENODO_RELEASE_CHECKLIST.md",
    "PUBLIC_BUILD_BOUNDARY.md",
    "config/services.json",
    "config/titans.public.json",
    "forge_server.py",
    "run.sh",
    "stop.sh",
    "verify.sh",
]:
    must(path)

svc=json.loads(must("config/services.json").read_text())
expected={
    "research-forge":8877,
    "generator-forge":8795,
    "solar-lab":8800,
    "ttf-pmae":5000,
    "mclab":8081,
    "playground":8890,
}
actual={x["id"]:x["port"] for x in svc["services"]}
for k,v in expected.items():
    if actual.get(k)!=v:
        errors.append(f"port regression: {k} expected {v}, got {actual.get(k)}")

tit=json.loads(must("config/titans.public.json").read_text())
roles={x["id"]:x["role"] for x in tit["seats"]}
expected_roles={
    "titan-1":"Supervisor / Strategist",
    "titan-2":"Explorer / Mutator",
    "titan-3":"Adversarial Validator",
    "math-seat":"Dedicated Formal Math Check",
}
if roles!=expected_roles:
    errors.append(f"Titan role regression: {roles!r}")
if any(x.get("direct_state_mutation") is not False for x in tit["seats"]):
    errors.append("authority regression: an AI seat can directly mutate scientific state")
if tit["generator_pair"]["default_url"]!="http://127.0.0.1:8795":
    errors.append("Generator Forge pairing regression")
if tit["generator_pair"]["credentials_in_repo"] is not False:
    errors.append("credential boundary regression")

deriv=must("research/bulk_interference_v02/DERIVATION_LEDGER.md").read_text()
for marker in ["1/(6π)","1/(3π)","Fast bulk / slow 3+1","CUT three-state"]:
    if marker not in deriv:
        errors.append(f"derivation regression: missing {marker}")

boundary=must("PUBLIC_BUILD_BOUNDARY.md").read_text()
for marker in ["PRIVATE CHAT / LOCAL-DRIVE EXECUTION","PUBLIC RESEARCH LAB REPOSITORY","secret scan"]:
    if marker not in boundary:
        errors.append(f"public/private boundary regression: missing {marker}")

if errors:
    print("REGRESSION FIXTURES FAIL")
    for e in errors: print(" -",e)
    sys.exit(1)
print("REGRESSION FIXTURES PASS")
print(f"checked {len(expected)} service ports, {len(expected_roles)} seats, keyless boundary, derivation invariants, launch surfaces")
