#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

FAIL=0
HOLD=0

echo "== Regression fixtures =="
python3 scripts/regression_fixtures.py || FAIL=1

echo "== Public secret boundary =="
python3 scripts/secret_boundary.py || FAIL=1

echo "== Front door =="
if curl -fsS http://127.0.0.1:8877/api/status >/tmp/research_forge_status.json 2>/dev/null; then
  python3 - <<'PY'
import json
p=json.load(open('/tmp/research_forge_status.json'))
assert p['service']=='lokivelli-research-forge'
assert p['keyless_public_mode'] is True
print('front door PASS')
for s in p['services']:
    print(f"{s['id']}: listening={s['listening']} health={s['health'].get('ok')}")
PY
else
  echo "front door FAIL: run bash run.sh first"
  FAIL=1
fi

echo "== Environment-gated donor status =="
for port in 8795 8800 5000 8081 8890; do
  if python3 - "$port" <<'PY'
import socket,sys
p=int(sys.argv[1])
s=socket.socket(); s.settimeout(.25)
try:
    s.connect(('127.0.0.1',p)); print(f'{p}: live')
except OSError:
    raise SystemExit(1)
finally:
    s.close()
PY
  then :; else
    echo "$port: HOLD (external donor not live in this environment)"
    HOLD=1
  fi
done

if [[ "$FAIL" -ne 0 ]]; then
  echo "VERIFY FAIL"
  exit 2
fi
if [[ "$HOLD" -ne 0 ]]; then
  echo "VERIFY PASS WITH ENVIRONMENT HOLDS"
  exit 0
fi
echo "VERIFY PASS: integrated shell + donor validations"
