#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

expected_repo='https://github.com/hiagokinlevi/OpenCyberAcademy.git'
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
if ! npx wrangler secret list | python3 -c 'import json,sys; sys.exit(0 if any(item.get("name") == "AUTH_HMAC_KEY" for item in json.load(sys.stdin)) else 1)'; then
  echo 'AUTH_HMAC_KEY must be configured as a Worker secret before deployment.' >&2
  exit 1
fi

npm ci
uv sync --frozen
npm run build
uv run pytest -q
npx wrangler d1 execute open-cyber-academy-progress --remote --file=migrations/0002_chapter_tests.sql
npx wrangler d1 execute open-cyber-academy-progress --remote --file=migrations/0003_student_auth.sql
uv run pywrangler deploy

curl_options=(--connect-timeout 12)
if ! curl --fail --silent --output /dev/null https://opencyber.academy/api/health; then
  # A newly created custom domain can be visible at Cloudflare while this
  # computer still has a cached negative DNS answer. Verify through public DNS.
  public_ip="$(dig @1.1.1.1 +short A opencyber.academy | head -n 1)"
  if [[ -z "$public_ip" ]]; then
    echo 'The public OpenCyber Academy domain does not resolve.' >&2
    exit 1
  fi
  curl_options=(--resolve "opencyber.academy:443:$public_ip")
fi
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/api/health
[[ "$(curl --silent --output /dev/null --write-out '%{http_code}' "${curl_options[@]}" https://opencyber.academy/auth/me)" == 401 ]]
[[ "$(curl --silent --output /dev/null --write-out '%{http_code}' "${curl_options[@]}" https://opencyber.academy/student/progress)" == 401 ]]
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/ | grep -F 'OpenCyber Academy' > /dev/null
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/levels/ | grep -F 'Browse by level' > /dev/null
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/subjects/ | grep -F 'Browse by subject' > /dev/null
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/courses/rapid-1-month/incident-response-resilience/ | grep -F 'incident-response-resilience' > /dev/null
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/courses/rapid-1-month/incident-response-resilience/lessons/en/1/ | grep -F '<meta name="robots" content="index,follow' > /dev/null
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/sitemap.xml | grep -F '/courses/rapid-1-month/incident-response-resilience/lessons/en/1/' > /dev/null
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/about/ | grep -F 'Hiago Kin Levi' > /dev/null
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/tests/ | grep -F 'Test yourself' > /dev/null
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/api/tests/catalog | grep -F 'professional-6-months/ot-iot-security/en' > /dev/null
curl --fail --show-error --silent "${curl_options[@]}" https://opencyber.academy/analytics.js | grep -F 'G-7KDGFR12FS' > /dev/null
curl --fail --show-error --silent "${curl_options[@]}" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  --data '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' \
  https://opencyber.academy/mcp | grep -F 'protocolVersion' > /dev/null

public_ip="${public_ip:-$(dig @1.1.1.1 +short A opencyber.academy | head -n 1)}"
for language in pt es he fr ru de zh ja; do
  host="${language}.opencyber.academy"
  host_options=(--connect-timeout 12 --resolve "${host}:443:${public_ip}")
  curl --fail --show-error --silent "${host_options[@]}" "https://${host}/api/health" > /dev/null
  curl --fail --show-error --silent "${host_options[@]}" "https://${host}/robots.txt" | grep -F "https://${host}/sitemap.xml" > /dev/null
  curl --fail --show-error --silent "${host_options[@]}" "https://${host}/analytics.js" | grep -F 'G-7KDGFR12FS' > /dev/null
  if [[ "$language" == pt || "$language" == es ]]; then
    curl --fail --show-error --silent "${host_options[@]}" "https://${host}/" | grep -F "<html lang=\"${language}\"" > /dev/null
    curl --fail --show-error --silent "${host_options[@]}" "https://${host}/about/" | grep -F 'Hiago Kin Levi' > /dev/null
    curl --fail --show-error --silent "${host_options[@]}" "https://${host}/sitemap.xml" | grep -F "https://${host}/courses/" > /dev/null
  else
    curl --fail --show-error --silent "${host_options[@]}" "https://${host}/" | grep -F 'noindex,follow' > /dev/null
  fi
done

echo "OpenCyber Academy deployed and verified from GitHub main $local_sha"
