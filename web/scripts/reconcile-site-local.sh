#!/usr/bin/env bash
# Run only in a disposable clone. No GitHub Actions or primary-checkout writes.
set -euo pipefail

cd "$(dirname "$0")/.."
repo_root="$(git rev-parse --show-toplevel)"
expected_repo='https://github.com/hiagokinlevi/OpenCyberAcademy.git'
if [[ "${OCA_DISPOSABLE_CLONE:-}" != 1 || "$repo_root" == '/Users/hiagokinlevi/OpenCyberAcademy' ]]; then
  echo 'Run this only in an explicitly disposable clone, never the primary checkout.' >&2
  exit 1
fi
if [[ "$(git remote get-url origin)" != "$expected_repo" || "$(git branch --show-current)" != main ]]; then
  echo 'Unexpected repository or branch. Refusing to synchronize.' >&2
  exit 1
fi
if [[ -n "$(git status --porcelain)" ]]; then
  echo 'The disposable clone must start clean.' >&2
  exit 1
fi

state_file="${OCA_SITE_SYNC_STATE:-$HOME/.codex/opencyber-site-sync/state.json}"
previous=''
if [[ -f "$state_file" ]]; then
  previous="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("git_sha", ""))' "$state_file")"
fi

for attempt in 1 2 3; do
  git fetch --quiet origin main
  # This clone is disposable and was clean before the run. A failed competing
  # push can leave only generated index changes or an unpublished index commit.
  git reset --hard --quiet origin/main
  npm run catalog

  python3 - <<'PY'
import re
import subprocess
import sys

paths = subprocess.check_output(["git", "status", "--porcelain", "-z"]).decode().split("\0")
paths = [entry[3:] for entry in paths if entry]
allowed = re.compile(r"web/public/(?:catalog|lesson-index|test-index)\.json|web/public/sitemap(?:-[a-z]{2}(?:-pages)?)?\.xml")
unexpected = [path for path in paths if not allowed.fullmatch(path)]
if unexpected:
    sys.exit("Unexpected generated changes: " + ", ".join(unexpected))
PY

  git add -- public/catalog.json public/lesson-index.json public/test-index.json public/sitemap*.xml
  if ! git diff --cached --quiet; then
    git commit -m 'Refresh Academy site indexes from published content'
    if ! git push origin HEAD:refs/heads/main; then
      echo "GitHub main changed during index publication; retrying ($attempt/3)." >&2
      continue
    fi
  fi

  local_sha="$(git rev-parse HEAD)"
  local_tree="$(git rev-parse HEAD:web)"
  remote_sha="$(git ls-remote origin refs/heads/main | cut -f1)"
  if [[ "$remote_sha" != "$local_sha" ]]; then
    echo "GitHub main advanced during reconciliation; retrying ($attempt/3)." >&2
    continue
  fi

  live_release="$(curl --fail --silent --show-error --connect-timeout 12 --max-time 30 \
    "https://opencyber.academy/site-release.json?check=$(date +%s)" 2>/dev/null || true)"
  live_tree="$(python3 -c 'import json,sys; data=sys.stdin.read(); print(json.loads(data).get("web_tree_sha", "") if data else "")' \
    <<< "$live_release" 2>/dev/null || true)"
  if [[ "$live_tree" != "$local_tree" ]]; then
    if ! ./scripts/deploy-local.sh; then
      remote_sha="$(git ls-remote origin refs/heads/main | cut -f1)"
      if [[ "$remote_sha" == "$local_sha" ]]; then
        echo 'Local Cloudflare deployment or its public verification failed.' >&2
        exit 1
      fi
      echo "GitHub main advanced during deployment; retrying ($attempt/3)." >&2
      continue
    fi
  fi

  verify_from="$previous"
  if [[ -z "$verify_from" && -n "$live_release" ]]; then
    verify_from="$(python3 -c 'import json,sys; data=sys.stdin.read(); print(json.loads(data).get("git_sha", "") if data else "")' \
      <<< "$live_release" 2>/dev/null || true)"
  fi
  python3 scripts/verify_site_sync.py --previous "$verify_from"
  remote_sha="$(git ls-remote origin refs/heads/main | cut -f1)"
  if [[ "$remote_sha" != "$local_sha" ]]; then
    echo "GitHub main advanced after public verification; retrying ($attempt/3)." >&2
    continue
  fi

  mkdir -p "$(dirname "$state_file")"
  python3 - "$state_file" "$local_sha" "$local_tree" <<'PY'
import json
import os
import sys
from datetime import datetime, timezone

path, sha, tree = sys.argv[1:]
temporary = path + ".tmp"
with open(temporary, "w", encoding="utf-8") as output:
    json.dump({"git_sha": sha, "web_tree_sha": tree,
               "verified_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}, output)
    output.write("\n")
os.replace(temporary, path)
PY
  echo "Academy site checked against GitHub main $local_sha"
  exit 0
done

echo 'GitHub main changed repeatedly; no stale deployment was accepted.' >&2
exit 1
