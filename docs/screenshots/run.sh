#!/usr/bin/env bash
# Take the lecture-step screenshots inside a Docker container (never on the host
# desktop, see framework/process/gui-testing.md). Run from the repository root.
# The repository is mounted read-only; the PNG files are written to docs/images/.
set -euo pipefail
repo="$(pwd -W 2>/dev/null || pwd)"
mkdir -p docs/images
MSYS_NO_PATHCONV=1 docker run --rm \
  -v "${repo}:/work:ro" \
  -v "${repo}/docs/images:/out" \
  -e PYTHONPATH=/work/src \
  mcr.microsoft.com/playwright/python:v1.54.0-noble \
  bash -c "python -m pip install -q --root-user-action=ignore flask requests playwright==1.54.0 && python /work/docs/screenshots/capture.py /out"
