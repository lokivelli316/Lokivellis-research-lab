#!/usr/bin/env python3
from __future__ import annotations
import argparse, os, pathlib, re, stat, sys

ALLOW = {
    "NVIDIA_API_KEY",
    "OPENAI_API_KEY",
    "XAI_API_KEY",
    "GROQ_API_KEY",
    "QWEN_API_KEY",
    "FAL_KEY",
    "FAL_API_KEY",
    "OMNIROUTE_API_KEY",
}
ROOT = pathlib.Path(__file__).resolve().parents[1]
TARGET = ROOT / ".env"

def parse_env(path: pathlib.Path) -> dict[str,str]:
    out={}
    try:
        text=path.read_text(encoding="utf-8")
    except Exception:
        return out
    for raw in text.splitlines():
        line=raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k,v=line.split("=",1)
        k=k.strip()
        if k not in ALLOW:
            continue
        v=v.strip()
        if len(v)>=2 and v[0]==v[-1] and v[0] in "'\"":
            v=v[1:-1]
        if v:
            out[k]=v
    return out

def main() -> int:
    ap=argparse.ArgumentParser(description="Import supported provider keys into local ignored .env")
    ap.add_argument("sources", nargs="*", help="Explicit .env files or directories to inspect")
    ap.add_argument("--scan-root", action="append", default=[], help="Recursively inspect *.env/.env files under this root")
    ns=ap.parse_args()

    candidates=[]
    for s in ns.sources:
        p=pathlib.Path(os.path.expanduser(s))
        if p.is_dir():
            candidates += [p/".env"] + list(p.glob("*.env"))
        else:
            candidates.append(p)
    for root in ns.scan_root:
        r=pathlib.Path(os.path.expanduser(root))
        if r.exists():
            candidates += list(r.rglob(".env"))
            candidates += list(r.rglob("*.env"))

    # preserve order, remove dupes, never print values
    seen=set(); uniq=[]
    for p in candidates:
        try: key=str(p.resolve())
        except Exception: key=str(p)
        if key in seen: continue
        seen.add(key); uniq.append(p)

    imported={}
    origins={}
    for p in uniq:
        if not p.is_file(): continue
        vals=parse_env(p)
        for k,v in vals.items():
            if k not in imported:
                imported[k]=v
                origins[k]=str(p)

    existing=parse_env(TARGET) if TARGET.exists() else {}
    merged={**imported, **existing}  # existing local values win
    lines=[
        "# Local/private runtime credentials. This file is gitignored.",
        "# Values are never printed by this tool.",
    ]
    for k in sorted(merged):
        safe=merged[k].replace("\\","\\\\").replace('"','\\"')
        lines.append(f'{k}="{safe}"')
    TARGET.write_text("\n".join(lines)+"\n",encoding="utf-8")
    os.chmod(TARGET, stat.S_IRUSR | stat.S_IWUSR)

    print(f"LOCAL SECRET CONFIG PASS: {TARGET}")
    print(f"mode={oct(TARGET.stat().st_mode & 0o777)} imported={len(imported)} total={len(merged)}")
    for k in sorted(merged):
        src="existing local .env" if k in existing else origins.get(k,"unknown")
        print(f"{k}: configured from {src}")
    missing=sorted(ALLOW-set(merged))
    if missing:
        print("not configured:", ", ".join(missing))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
