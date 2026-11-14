#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
mkdir -p runtime workspace/logs workspace/pids

HOST="${RESEARCH_FORGE_HOST:-127.0.0.1}"
PORT="${RESEARCH_FORGE_PORT:-8877}"

if curl -fsS "http://$HOST:$PORT/api/status" >/dev/null 2>&1; then
  echo "[research-forge] already running at http://$HOST:$PORT"
  exit 0
fi

python3 forge_server.py --host "$HOST" --port "$PORT" >>workspace/logs/research-forge.log 2>&1 &
PID=$!
echo "$PID" > workspace/pids/research-forge.pid

for _ in $(seq 1 30); do
  if curl -fsS "http://$HOST:$PORT/api/status" >/dev/null 2>&1; then
    echo "[research-forge] RUNNING http://$HOST:$PORT"
    exit 0
  fi
  sleep 0.2
done

echo "[research-forge] FAIL: server did not become healthy"
tail -n 80 workspace/logs/research-forge.log || true
exit 1
