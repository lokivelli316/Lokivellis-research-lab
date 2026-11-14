#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

echo "[research-forge] Termux install — public keyless build"
pkg update -y
pkg install -y python git curl tmux

mkdir -p runtime workspace/logs workspace/pids workspace/receipts workspace/experiments workspace/notebooks workspace/exports
chmod 700 runtime workspace/logs workspace/pids workspace/receipts workspace/experiments workspace/notebooks workspace/exports

python3 scripts/regression_fixtures.py
echo "[research-forge] install contract PASS"
echo "[research-forge] keys are intentionally not required for public/keyless launch"
