# Bryan Bischof Brand — Agent Spec

You are reading this because the project you're working in has explicitly
opted into Bryan's brand. Do not apply this aesthetic to projects that
haven't opted in.

## Typography

GeistMono-Regular everywhere. No serif, no sans-serif fallback in UI.

| Token           | Value                                          |
|-----------------|------------------------------------------------|
| Font (regular)  | `'GeistMono-Regular', Consolas, monaco, monospace` |
| Font (bold)     | `'GeistMono-Bold', Consolas, monaco, monospace`    |
| h1              | 32px                                           |
| h2              | 20px                                           |
| body            | 16px                                           |
| meta / ui / tag | 12px                                           |
| line-height UI  | 1.25 (dense)                                   |
| line-height prose | 1.42                                         |

Spacing unit: `1ch` horizontal, `rem` vertical. Align to the character grid.

## Colors

No blue or cyan, anywhere. Color signals semantic meaning, not decoration.
Default to neutrals; use semantic colors only when the meaning applies.

### Light theme
| Token           | Hex       | Role                                  |
|-----------------|-----------|---------------------------------------|
| background      | `#F5F4F1` | default page/app surface              |
| surface         | `#ECE9E4` | cards, panels                         |
| surface-2       | `#E3DFD8` | alternating rows, nested panels       |
| border          | `#D1CCC4` | all borders and dividers              |
| text            | `#1A1A18` | primary body copy                     |
| text-muted      | `#6D6A64` | secondary labels, metadata            |
| text-faint      | `#98938A` | tertiary, disabled                    |
| accent          | `#D97A32` | featured / curated / authored         |
| interactive     | `#5F8A3B` | live UI / explicit active states      |
| analytic        | `#7A4FB3` | data / math / comparison              |
| critical        | `#B6423C` | errors / warnings / destructive       |

### Dark theme
| Token           | Hex       |
|-----------------|-----------|
| background      | `#141412` |
| surface         | `#1C1C19` |
| surface-2       | `#262521` |
| border          | `#3A3832` |
| text            | `#E8E2D8` |
| text-muted      | `#A7A093` |
| text-faint      | `#7C766C` |
| accent          | `#E08A43` |
| interactive     | `#91B85A` |
| analytic        | `#A47DDB` |
| critical        | `#E06A63` |

### Data viz shades (layering fills)
| Token            | Hex       | Use                              |
|------------------|-----------|----------------------------------|
| shade-panel      | `#ECE9E4` | small-multiple surface           |
| shade-alternate  | `#E3DFD8` | alternating row/column fill      |
| shade-ref-band   | `#D1CCC4` | threshold, regime, period band   |
| shade-uncertainty| `#DDD2E8` | confidence interval, forecast    |
| shade-context    | `#EAE6DE` | subdued background context       |
| shade-highlight  | `#F1D8C4` | restrained warm emphasis area    |

## Accessibility

Full contrast ratio tables: [accessibility.md](accessibility.md)

Key constraints agents must respect:

- **Accent as text color fails WCAG AA in light mode** (2.82:1). Use accent as a fill, border, or mark — not as body text.
- **In light mode on semantic fills**: use `text` (#1A1A18) on accent/interactive/critical fills; use `background` (#F5F4F1) on analytic fills.
- **In dark mode on semantic fills**: always use `background` (#141412), never `text` (#E8E2D8) — light text on these colors fails.
- `text-faint` fails AA on all surfaces in both themes — restrict to non-essential decorative labels only, never primary content.
- `text-muted` passes AA on `background` in light mode but drops to AA Large on `surface` and `surface-2` — avoid for small body copy in those contexts.

## Semantic usage rules

**Accent (orange) ≠ primary action.** It means "Bryan featured/chose/authored
this." Use neutral backgrounds for generic interactive elements. Hover and
focus rings should not be orange by default.

**Interactive (green) is rare.** Reserve it for live systems and explicitly
active UI states. Not for hover effects or default buttons.

**Analytic (violet)** is for data overlays, secondary series, computational
or mathematical context.

**Neutrals by default.** When in doubt, reach for the warm gray surface and
border tokens rather than adding color.

## Tag / categorical palette

Post tags, genres, and small data categories use HSL hues biased away from
blue and cyan:

```
hues: 0, 10, 18, 28, 38, 75, 95, 115, 135, 270, 285, 300, 315, 335, 345
```

Formula: solid `hsl(hue, 55%, 42%)` · chip bg `hsla(hue, 45%, 55%, 0.06)` ·
chip border `hsla(hue, 35%, 45%, 0.25)`

## Data visualization

Apply the `bryan_bischof` theme from bbplot. Same color semantics apply:
orange for featured/curated series, green for active/live, violet for
analytical overlays. Avoid blue/cyan in any categorical palette.

## Implementation files (fetch only what you need)

| File                  | Use                                         |
|-----------------------|---------------------------------------------|
| `tokens/tokens.css`   | CSS custom properties, drop into any web project |
| `tokens/tokens.py`    | Python dict for notebooks and scripts       |
| `themes/bbplot.py`    | Standalone matplotlib theme                 |
| `css/base.css`        | Reset + GeistMono + type scale, ready to import |
| `css/components.css`  | Card, badge, tag, button, table, alert      |
| `starters/web/`       | Minimal on-brand HTML/CSS project scaffold  |
| `starters/dataviz/`   | Minimal Python notebook starter             |
