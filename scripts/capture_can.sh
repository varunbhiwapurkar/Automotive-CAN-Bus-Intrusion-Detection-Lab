#!/usr/bin/env bash
set -euo pipefail

mkdir -p logs
candump -L vcan0 > logs/capture.asc
