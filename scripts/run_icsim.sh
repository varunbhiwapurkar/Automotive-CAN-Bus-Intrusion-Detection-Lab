#!/usr/bin/env bash
set -euo pipefail

if ! command -v icsim >/dev/null 2>&1 || ! command -v controls >/dev/null 2>&1; then
  echo "ICSim binaries not found in PATH. Install from https://github.com/zombieCraig/ICSim"
  exit 1
fi

icsim vcan0 &
controls vcan0
