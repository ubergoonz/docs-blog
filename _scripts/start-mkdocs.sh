#!/usr/bin/env bash
set -euo pipefail
# This script is used to start the application in local development mode.
# Usage: ./_scripts/start-mkdocs.sh

# Move to repo root (script lives in _scripts/)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

VENV_DIR=".venv"
REQ_FILE="requirements.txt"

# Choose python executable
if command -v python3 >/dev/null 2>&1; then
	PYTHON=python3
elif command -v python >/dev/null 2>&1; then
	PYTHON=python
else
	echo "No python interpreter found (python3 or python). Install Python and retry." >&2
	exit 1
fi

# Create virtualenv if missing
if [ ! -d "$VENV_DIR" ]; then
	echo "Creating virtualenv at $VENV_DIR using $PYTHON"
	$PYTHON -m venv "$VENV_DIR"
fi

# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

# Upgrade installer tooling
python -m pip install --upgrade pip wheel >/dev/null

# Always sync project requirements so the venv matches pinned plugin versions.
# This avoids stale environments where mkdocs exists but a required dependency
# (such as setuptools providing pkg_resources) is missing or incompatible.
if [ -f "$REQ_FILE" ]; then
	echo "Installing Python requirements from $REQ_FILE"
	python -m pip install -r "$REQ_FILE"
elif ! command -v mkdocs >/dev/null 2>&1; then
	echo "Requirements file $REQ_FILE not found; attempting to install mkdocs"
	python -m pip install mkdocs
else
	echo "Using existing mkdocs in virtualenv"
fi

echo "Starting mkdocs serve..."
mkdocs serve