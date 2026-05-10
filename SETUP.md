# Setup — wiring bb-brand across agent surfaces

## New machine

```sh
curl -fsSL https://raw.githubusercontent.com/BBischof/bb-brand/main/scripts/install.sh | bash
```

Adds the `brand-init` alias to your shell. Also add this line to your
dotfiles `bootstrap.sh` so it runs automatically on every new machine.

## Opting a project in

```sh
cd path/to/your/project
brand-init
```

This injects the brand opt-in line into whichever agent config files the
project uses. Review the diff before committing.

## Per-surface opt-in reference

If you prefer to add the opt-in manually, paste the following into the
relevant file for each surface:

```
# Brand
# This is a Bryan Bischof–branded project. Fetch brand context: https://raw.githubusercontent.com/BBischof/bb-brand/main/quick.md
```

| Surface | File |
|---|---|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursorrules` |
| Windsurf | `.windsurfrules` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Any other agent | paste the URL into your opening prompt |

## Fetching brand context in a prompt (web agents / one-offs)

```
Before starting, fetch my brand context from:
https://raw.githubusercontent.com/BBischof/bb-brand/main/quick.md

For full detail: https://raw.githubusercontent.com/BBischof/bb-brand/main/AGENTS.md
```

## Using brand assets in a web project

```html
<link rel="stylesheet" href="https://raw.githubusercontent.com/BBischof/bb-brand/main/tokens/tokens.css">
<link rel="stylesheet" href="https://raw.githubusercontent.com/BBischof/bb-brand/main/css/base.css">
<link rel="stylesheet" href="https://raw.githubusercontent.com/BBischof/bb-brand/main/css/components.css">
```

Or copy the files locally for production use.

## Using the matplotlib theme

```python
import sys
sys.path.insert(0, "/path/to/bb-brand")  # or install as a package
from themes.bbplot import apply
apply()
```
