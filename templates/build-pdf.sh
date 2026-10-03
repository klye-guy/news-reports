#!/usr/bin/env bash
# Build a glanceable letter PDF from a Minder report Markdown file.
# Usage (from anywhere):
#   templates/build-pdf.sh path/to/report.md path/to/report.pdf
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: templates/build-pdf.sh INPUT.md OUTPUT.pdf" >&2
  exit 2
fi

IN=$(realpath "$1")
OUT=$(realpath -m "$2")
HERE=$(cd "$(dirname "$0")" && pwd)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

pandoc "$IN" \
  --from=markdown+yaml_metadata_block \
  --to=html5 \
  --standalone \
  --section-divs \
  --template="$HERE/report.html" \
  --lua-filter="$HERE/report.lua" \
  --css="report.css" \
  --output="$TMP/report.html"

cp "$HERE/report.css" "$TMP/report.css"
node "$HERE/print-pdf.mjs" "$TMP/report.html" "$OUT"

if [[ ! -s "$OUT" ]]; then
  echo "PDF was not written: $OUT" >&2
  exit 1
fi
