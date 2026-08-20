#!/usr/bin/env bash
# Author: Gianni Corona
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
export PYTHONPATH="$SCRIPT_DIR/src"
exec python3 -m lezione1
