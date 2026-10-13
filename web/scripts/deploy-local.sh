#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

expected_repo='https://github.com/hiagokinlevi/CyKin.git'
expected_account='1e04c78c6d0084600ddb4589c4e3327c'
if [[ "$(git remote get-url origin)" != "$expected_repo" ]]; then
  echo 'Unexpected GitHub origin. Refusing deployment.' >&2
  exit 1
fi
if [[ -n "$(git status --porcelain)" ]]; then
  echo 'Commit and push all changes before deployment.' >&2
  exit 1
fi
local_sha="$(git rev-parse HEAD)"
remote_sha="$(git ls-remote origin refs/heads/main | cut -f1)"
if [[ "$local_sha" != "$remote_sha" ]]; then
  echo 'The checkout must match the published GitHub main commit.' >&2
  exit 1
fi
if ! npx wrangler whoami | grep -q "$expected_account"; then
  echo 'Unexpected Cloudflare account. Refusing deployment.' >&2
  exit 1
fi

npm ci
uv sync --frozen
npm run build
uv run pytest -q
uv run pywrangler deploy

curl_options=()
if ! curl --fail --silent --output /dev/null https://cykin.org/api/health; then
  # A newly created custom domain can be visible at Cloudflare while this
  # computer still has a cached negative DNS answer. Verify through public DNS.
  public_ip="$(dig @1.1.1.1 +short A cykin.org | head -n 1)"
  if [[ -z "$public_ip" ]]; then
    echo 'The public CyKin domain does not resolve.' >&2
    exit 1
  fi
  curl_options=(--resolve "cykin.org:443:$public_ip")
fi
curl --fail --show-error --silent "${curl_options[@]}" https://cykin.org/api/health
curl --fail --show-error --silent "${curl_options[@]}" https://cykin.org/ | grep -q 'CyKin'
curl --fail --show-error --silent "${curl_options[@]}" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  --data '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' \
  https://cykin.org/mcp | grep -q 'protocolVersion'

echo "CyKin deployed and verified from GitHub main $local_sha"
