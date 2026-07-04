#!/usr/bin/env bash
set -euo pipefail
# Run cspell spell-check against all docs markdown files.
# Usage: ./_scripts/spellcheck.sh [--no-progress]

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

if ! command -v cspell >/dev/null 2>&1; then
  echo "cspell not found. Install it with: npm install -g cspell" >&2
  exit 1
fi

echo "Running cspell..."
cspell --config cspell.json "docs/**/*.md" README.md "$@"
