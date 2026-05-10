"""Generate README preview images using the bb-brand token and theme files."""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib import font_manager

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

# Load fonts before applying theme
font_manager.fontManager.addfont(str(ROOT / "fonts/GeistMono-Regular.ttf"))
font_manager.fontManager.addfont(str(ROOT / "fonts/GeistMono-Bold.ttf"))

from themes.bbplot import apply, PALETTE, BACKGROUND, TEXT, TEXT_MUTED, GRID

ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

FONT = "Geist Mono"

LIGHT = {
    "background": "#F5F4F1", "surface":  "#ECE9E4", "surface2": "#E3DFD8",
    "border":     "#D1CCC4", "text":     "#1A1A18", "textMuted":"#6D6A64",
    "accent":     "#D97A32", "interactive":"#5F8A3B","analytic": "#7A4FB3",
    "critical":   "#B6423C",
}
DARK = {
    "background": "#141412", "surface":  "#1C1C19", "surface2": "#262521",
    "border":     "#3A3832", "text":     "#E8E2D8", "textMuted":"#A7A093",
    "accent":     "#E08A43", "interactive":"#91B85A","analytic": "#A47DDB",
    "critical":   "#E06A63",
}

# ── 1. Palette ─────────────────────────────────────────────────────────────────

def make_palette():
    semantic = [
        ("accent",      "Accent\nfeatured / curated"),
        ("interactive", "Interactive\nlive UI"),
        ("analytic",    "Analytic\ndata / math"),
        ("critical",    "Critical\nerrors / warnings"),
    ]
    neutrals = [
        ("background",  "Background"),
        ("surface",     "Surface"),
        ("surface2",    "Surface 2"),
        ("border",      "Border"),
        ("textMuted",   "Text muted"),
        ("text",        "Text"),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 4),
                             gridspec_kw={"hspace": 0.08, "wspace": 0.04})
    fig.patch.set_facecolor(LIGHT["background"])

    def draw_row(ax, theme, swatches, label):
        ax.set_facecolor(theme["background"])
        ax.set_xlim(0, len(swatches))
        ax.set_ylim(0, 1)
        ax.axis("off")
        for i, (key, name) in enumerate(swatches):
            color = theme[key]
            rect = mpatches.FancyBboxPatch(
                (i + 0.08, 0.28), 0.84, 0.56,
                boxstyle="square,pad=0",
                facecolor=color,
                edgecolor=theme["border"],
                linewidth=0.8,
            )
            ax.add_patch(rect)
            # hex label inside swatch
            lum = int(color[1:3], 16) * 0.299 + int(color[3:5], 16) * 0.587 + int(color[5:], 16) * 0.114
            label_color = theme["background"] if lum > 128 else theme["text"]
            ax.text(i + 0.5, 0.56, color.upper(),
                    ha="center", va="center",
                    fontfamily=FONT, fontsize=6.5, color=label_color)
            # name below
            ax.text(i + 0.5, 0.14, name.split("\n")[0],
                    ha="center", va="center",
                    fontfamily=FONT, fontsize=6.5, color=theme["textMuted"])

        ax.text(-0.02, 0.56, label, ha="right", va="center",
                fontfamily=FONT, fontsize=7, color=theme["textMuted"],
                rotation=0)

    draw_row(axes[0, 0], LIGHT, semantic,  "semantic")
    draw_row(axes[0, 1], DARK,  semantic,  "")
    draw_row(axes[1, 0], LIGHT, neutrals,  "neutrals")
    draw_row(axes[1, 1], DARK,  neutrals,  "")

    # Mode labels
    for ax, mode, theme in [(axes[0,0], "light", LIGHT), (axes[0,1], "dark", DARK)]:
        ax.set_title(mode, fontfamily=FONT, fontsize=8,
                     color=theme["textMuted"], pad=4, loc="left")
        ax.set_facecolor(theme["background"])
    axes[1, 0].set_facecolor(LIGHT["background"])
    axes[1, 1].set_facecolor(DARK["background"])

    fig.savefig(ASSETS / "palette.png", dpi=180, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  → assets/palette.png")


# ── 2. Typography specimen ─────────────────────────────────────────────────────

def make_typography():
    fig, ax = plt.subplots(figsize=(12, 3.2))
    fig.patch.set_facecolor(LIGHT["background"])
    ax.set_facecolor(LIGHT["background"])
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    entries = [
        (0.82, "bold",   32, "H1 / 32px",  "Warm terminal."),
        (0.60, "bold",   20, "H2 / 20px",  "Research notebook."),
        (0.40, "normal", 16, "Body / 16px", "Mono-first. No blue. Color carries meaning."),
        (0.22, "normal", 12, "Meta / 12px", "GeistMono-Regular — labels, tags, UI, metadata."),
    ]

    for y, weight, size, label, sample in entries:
        ax.text(0.13, y, label,
                ha="right", va="baseline",
                fontfamily=FONT, fontsize=7.5,
                color=LIGHT["textMuted"], transform=ax.transAxes)
        ax.text(0.15, y, sample,
                ha="left", va="baseline",
                fontfamily=FONT, fontsize=size * 0.72,
                fontweight=weight,
                color=LIGHT["text"], transform=ax.transAxes)

    # Vertical rule between label and specimen
    from matplotlib.lines import Line2D
    ax.add_line(Line2D([0.135, 0.135], [0.08, 0.95],
                       transform=ax.transAxes,
                       color=LIGHT["border"], linewidth=0.8))

    fig.savefig(ASSETS / "typography.png", dpi=180, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  → assets/typography.png")


# ── 3. Chart specimen ──────────────────────────────────────────────────────────

def make_chart():
    apply()

    rng = np.random.default_rng(42)
    x = np.linspace(0, 12, 120)

    primary  = np.cumsum(rng.normal(0.06, 0.4, 120))
    featured = np.cumsum(rng.normal(0.10, 0.3, 120))
    context  = np.cumsum(rng.normal(0.02, 0.5, 120))

    fig, ax = plt.subplots(figsize=(12, 4))

    ax.plot(x, context,  color=LIGHT["border"],   linewidth=1.4,
            label="context", zorder=1)
    ax.plot(x, primary,  color=PALETTE[3],         linewidth=2.2,
            label="analytic series", zorder=2)
    ax.plot(x, featured, color=PALETTE[1],         linewidth=2.2,
            label="featured series", zorder=3)

    # Shade uncertainty band
    band_lo = featured - rng.uniform(0.2, 0.5, 120)
    band_hi = featured + rng.uniform(0.2, 0.5, 120)
    ax.fill_between(x, band_lo, band_hi, color="#DDD2E8", alpha=0.55, zorder=0)

    ax.set_title("Chart specimen", loc="left",
                 fontfamily=FONT, fontsize=13, color=LIGHT["text"])
    ax.set_xlabel("index", fontfamily=FONT)
    ax.set_ylabel("value", fontfamily=FONT)
    ax.legend(frameon=True)

    fig.savefig(ASSETS / "chart.png", dpi=180, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  → assets/chart.png")


if __name__ == "__main__":
    print("Generating preview images...")
    make_palette()
    make_typography()
    make_chart()
    print("Done.")
