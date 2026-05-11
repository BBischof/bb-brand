#!/usr/bin/env python3
"""
Generate canonical mark variants from mark.svg:
  mark-light.svg  — black silhouette on light background
  mark-dark.svg   — white silhouette on dark background
  mark-color.svg  — orange→green gradient on transparent background
"""
import re, subprocess
from pathlib import Path

ASSETS = Path("/Users/bryanbischof/dev_other/bb-brand/assets")

BG_LIGHT  = "#F5F4F1"
BG_DARK   = "#141412"
INK_LIGHT = "#1A1A18"
INK_DARK  = "#E8E2D8"
ORANGE    = "#D97A32"
GREEN     = "#5F8A3B"
SIZE      = 600


def get_mark_path():
    text = (ASSETS / "mark.svg").read_text()
    m = re.search(r'<path[^>]+\bd="([^"]+)"', text, re.DOTALL)
    return m.group(1)


def make_svg(bg, fill, gradient=False):
    d = get_mark_path()
    grad = ""
    fill_attr = fill
    if gradient:
        grad = f"""
    <linearGradient id="mg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="{ORANGE}"/>
      <stop offset="100%" stop-color="{GREEN}"/>
    </linearGradient>"""
        fill_attr = "url(#mg)"

    bg_rect = f'<rect width="{SIZE}" height="{SIZE}" fill="{bg}"/>' if bg else ""

    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}">
  <defs>{grad}
  </defs>
  {bg_rect}
  <g transform="scale({SIZE/1254:.6f})">
    <path d="{d}" fill="{fill_attr}" fill-rule="evenodd"/>
  </g>
</svg>"""


variants = [
    ("mark-light.svg", BG_LIGHT, INK_LIGHT, False),
    ("mark-dark.svg",  BG_DARK,  INK_DARK,  False),
    ("mark-color.svg", "none",   None,      True),
]

for filename, bg, fill, gradient in variants:
    out = ASSETS / filename
    out.write_text(make_svg(bg, fill, gradient))
    print(f"Saved → {out}")
    subprocess.run(["qlmanage", "-t", "-s", str(SIZE), "-o", "/tmp", str(out)],
                   capture_output=True)
    print(f"Rendered → /tmp/{filename}.png")
