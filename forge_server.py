#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import pathlib
import socket
import subprocess
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent
CONFIG = ROOT / "config" / "services.json"
RUNTIME = ROOT / "runtime"
RUNTIME.mkdir(exist_ok=True)

def load_services() -> dict[str, Any]:
    return json.loads(CONFIG.read_text(encoding="utf-8"))

def tcp_open(host: str, port: int, timeout: float = 0.3) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False

def http_probe(url: str, timeout: float = 0.8) -> dict[str, Any]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            body = r.read(2048).decode("utf-8", "replace")
            return {"ok": 200 <= r.status < 400, "status": r.status, "body": body}
    except Exception as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}"}

def service_status() -> list[dict[str, Any]]:
    cfg = load_services()
    out = []
    for svc in cfg["services"]:
        item = dict(svc)
        item["listening"] = tcp_open(svc["host"], svc["port"])
        probe = svc.get("health_url")
        item["health"] = http_probe(probe) if probe and item["listening"] else {"ok": item["listening"]}
        out.append(item)
    return out

class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        original = super().translate_path(path)
        rel = pathlib.Path(original).relative_to(pathlib.Path.cwd())
        return str(ROOT / rel)

    def do_GET(self):
        if self.path == "/api/status":
            payload = {
                "service": "lokivelli-research-forge",
                "version": "0.2.0-federated-public",
                "front_door": "127.0.0.1:8877",
                "keyless_public_mode": True,
                "services": service_status(),
            }
            data = json.dumps(payload, indent=2).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        if self.path == "/api/titans":
            cfg = json.loads((ROOT / "config" / "titans.public.json").read_text(encoding="utf-8"))
            data = json.dumps(cfg, indent=2).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        return super().do_GET()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default=os.environ.get("RESEARCH_FORGE_HOST", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(os.environ.get("RESEARCH_FORGE_PORT", "8877")))
    ns = ap.parse_args()
    os.chdir(ROOT)
    httpd = ThreadingHTTPServer((ns.host, ns.port), Handler)
    print(f"Lokivelli Research Forge public front door: http://{ns.host}:{ns.port}", flush=True)
    httpd.serve_forever()

if __name__ == "__main__":
    raise SystemExit(main())
