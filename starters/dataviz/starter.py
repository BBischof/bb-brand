"""
Bryan Bischof dataviz starter.
Copy this file into a new project and adjust imports once bb-brand is available.
"""
import sys
from pathlib import Path

# Add bb-brand to path if not installed as a package
BB_BRAND = Path(__file__).parent.parent.parent
if str(BB_BRAND) not in sys.path:
    sys.path.insert(0, str(BB_BRAND))

from themes.bbplot import apply, PALETTE, BACKGROUND, TEXT, TEXT_MUTED
apply()

import matplotlib.pyplot as plt
import matplotlib as mpl

# --- your chart below ---

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot([1, 2, 3, 4], [2, 4, 3, 5], label="Primary series")
ax.plot([1, 2, 3, 4], [1, 3, 2, 4], label="Secondary series")

ax.set_title("Chart title", loc="left")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.legend()

plt.tight_layout()
plt.savefig("output.png", dpi=150, bbox_inches="tight")
plt.show()
