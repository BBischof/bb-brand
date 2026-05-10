#!/usr/bin/env bash
# Installs the `brand-init` alias into your shell config.
# Run once on a new machine (or via dotfiles bootstrap).

set -euo pipefail

ALIAS_LINE='alias brand-init="curl -fsSL https://raw.githubusercontent.com/BBischof/bb-brand/main/scripts/init.sh | bash"'
MARKER="bb-brand"

# Detect shell config file
if [ -f "$HOME/.zshrc" ]; then
  SHELL_RC="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
  SHELL_RC="$HOME/.bashrc"
else
  SHELL_RC="$HOME/.profile"
fi

if grep -qF "$MARKER" "$SHELL_RC" 2>/dev/null; then
  echo "brand-init alias already present in $SHELL_RC"
  exit 0
fi

printf "\n# bb-brand\n%s\n" "$ALIAS_LINE" >> "$SHELL_RC"
echo "Added brand-init alias to $SHELL_RC"
echo "Reload your shell or run: source $SHELL_RC"
