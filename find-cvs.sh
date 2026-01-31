#!/usr/bin/env bash

# ================================================================
# CV PDF Collector
# Copies all PDF files containing "cv" (case-insensitive) from
# Downloads folder to a dedicated CV_PDFs folder
# ================================================================

set -euo pipefail

# Configuration ────────────────────────────────────────────────
SRC_DIR="${SRC_DIR:-"$HOME/Downloads"}"
DEST_DIR="${DEST_DIR:-"$HOME/CV_PDFs"}"

# ──────────────────────────────────────────────────────────────

echo "🔍 Source folder     : $SRC_DIR"
echo "📂 Destination folder : $DEST_DIR"
echo ""

if [[ ! -d "$SRC_DIR" ]]; then
    echo "❌ Error: Source directory does not exist: $SRC_DIR"
    exit 1
fi

mkdir -p "$DEST_DIR"

echo "Searching for files matching *cv*.pdf (case-insensitive)..."

# shellcheck disable=SC2016
find "$SRC_DIR" -type f -iname '*cv*.pdf' -print0 | while IFS= read -r -d '' file; do
    filename=$(basename "$file")
    echo "  → found: $filename"
    cp -v "$file" "$DEST_DIR/"
done

echo ""
echo "✅ Finished."
echo "   Files copied to → $DEST_DIR"
ls -lAh "$DEST_DIR" | grep -i cv || echo "   (no files were copied)"
