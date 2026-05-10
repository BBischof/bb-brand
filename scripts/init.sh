#!/usr/bin/env bash
# Run from a project root to inject the bb-brand opt-in into agent config files.
# Idempotent — safe to run multiple times.

set -euo pipefail

QUICK_URL="https://raw.githubusercontent.com/BBischof/bb-brand/main/quick.md"
MARKER="bb-brand"
LINE="This is a Bryan Bischof–branded project. Fetch brand context: $QUICK_URL"
BLOCK="# Brand\n# $LINE"

inject() {
  local file="$1"
  local dir
  dir=$(dirname "$file")

  if [ -f "$file" ] && grep -qF "$MARKER" "$file"; then
    echo "  ✓  $file (already opted in)"
    return
  fi

  mkdir -p "$dir"

  if [ -f "$file" ]; then
    printf "\n%b\n" "$BLOCK" >> "$file"
    echo "  →  appended to $file"
  else
    printf "%b\n" "$BLOCK" > "$file"
    echo "  →  created $file"
  fi
}

echo ""
echo "bb-brand: injecting brand opt-in into agent config files..."
echo ""

inject "CLAUDE.md"
inject ".cursorrules"
inject ".windsurfrules"
inject ".github/copilot-instructions.md"

echo ""
echo "Done. Review changes before committing."
echo "Full brand spec: https://github.com/BBischof/bb-brand"
echo ""
