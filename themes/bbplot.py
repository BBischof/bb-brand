"""
Bryan Bischof matplotlib theme — standalone, no bbplot dependency required.

Usage:
    from bb_brand.themes.bbplot import apply
    apply()

Or directly via matplotlib:
    import matplotlib as mpl
    from bb_brand.themes.bbplot import RC_PARAMS
    mpl.rcParams.update(RC_PARAMS)
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

PALETTE = [
    "#1A1A18",  # black (structural emphasis)
    "#D97A32",  # orange (curated / featured / editorial)
    "#5F8A3B",  # green (interaction / focus)
    "#7A4FB3",  # violet (analytic / computational)
    "#B6423C",  # red (critical / alert)
    "#9B3D73",  # rose (taxonomy variety)
]

BACKGROUND = "#F5F4F1"
TEXT       = "#1A1A18"
TEXT_MUTED = "#6D6A64"
GRID       = "#D1CCC4"
FONT       = "Geist Mono"

RC_PARAMS = {
    # Canvas
    "figure.facecolor": BACKGROUND,
    "axes.facecolor":   BACKGROUND,
    "savefig.facecolor": BACKGROUND,

    # Text
    "text.color":       TEXT,
    "axes.labelcolor":  TEXT,
    "xtick.color":      TEXT_MUTED,
    "ytick.color":      TEXT_MUTED,

    # Font
    "font.family":      "monospace",
    "font.monospace":   [FONT, "Consolas", "monaco", "monospace"],
    "axes.titlesize":   16,
    "axes.labelsize":   9,
    "xtick.labelsize":  9,
    "ytick.labelsize":  9,
    "legend.fontsize":  9,
    "figure.titlesize": 16,

    # Grid
    "axes.grid":           True,
    "grid.color":          GRID,
    "grid.linewidth":      0.6,
    "grid.alpha":          0.58,
    "grid.linestyle":      "-",

    # Spines
    "axes.spines.top":    False,
    "axes.spines.right":  False,
    "axes.spines.left":   True,
    "axes.spines.bottom": True,
    "axes.linewidth":     1.4,
    "axes.edgecolor":     GRID,

    # Ticks
    "xtick.major.width":  1.2,
    "ytick.major.width":  1.2,
    "xtick.major.size":   0,
    "ytick.major.size":   0,

    # Lines and markers
    "lines.linewidth":       2.2,
    "lines.markersize":      5.0,
    "lines.markeredgewidth": 1.0,

    # Scatter
    "scatter.marker": "o",

    # Bars
    "patch.linewidth": 0.0,

    # Legend
    "legend.frameon":      True,
    "legend.edgecolor":    GRID,
    "legend.facecolor":    BACKGROUND,

    # Color cycle
    "axes.prop_cycle": mpl.cycler(color=PALETTE),
}


def apply() -> None:
    """Apply the Bryan Bischof theme to the current matplotlib session."""
    mpl.rcParams.update(RC_PARAMS)
