#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
PIDFILE="workspace/pids/research-forge.pid"
if [[ ! -f "$PIDFILE" ]]; then
  echo "[research-forge] no pid file"
  exit 0
fi
PID="$(cat "$PIDFILE")"
if kill -0 "$PID" 2>/dev/null; then
  kill "$PID"
  for _ in $(seq 1 20); do
    kill -0 "$PID" 2>/dev/null || break
    sleep 0.1
  done
fi
rm -f "$PIDFILE"
echo "[research-forge] stopped"
