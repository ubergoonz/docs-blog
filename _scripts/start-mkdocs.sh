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

# Upgrade pip and tools
python -m pip install --upgrade pip setuptools wheel >/dev/null

# Install requirements if mkdocs not available in venv
if ! command -v mkdocs >/dev/null 2>&1; then
	if [ -f "$REQ_FILE" ]; then
		echo "Installing Python requirements from $REQ_FILE"
		pip install -r "$REQ_FILE"
	else
		echo "Requirements file $REQ_FILE not found; attempting to install mkdocs"
		pip install mkdocs
	fi
else
	echo "Using existing mkdocs in virtualenv"
fi

echo "Starting mkdocs serve..."
mkdocs serve