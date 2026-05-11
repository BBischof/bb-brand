#!/usr/bin/env python3
"""
Wordmark — tagline bounds from left-of-A to right-of-h in name string.
"""
import base64, re, subprocess
from pathlib import Path
from fontTools.ttLib import TTFont

FONTS_DIR  = Path("/Users/bryanbischof/dev_other/bb-brand/fonts")
ASSETS_DIR = Path("/Users/bryanbischof/dev_other/bb-brand/assets")

ORANGE_LIGHT = "#D97A32"
GREEN_LIGHT  = "#5F8A3B"
ORANGE_DARK  = "#E08A43"
GREEN_DARK   = "#91B85A"
BG_LIGHT     = "#F5F4F1"
BG_DARK      = "#141412"
INK_LIGHT    = "#1A1A18"
INK_DARK     = "#E8E2D8"
MUT_LIGHT    = "#6D6A64"
MUT_DARK     = "#A7A093"


def load_font(font_path):
    font  = TTFont(str(font_path))
    cmap  = font.getBestCmap()
    hmtx  = font["hmtx"]
    upm   = font["head"].unitsPerEm
    return font, cmap, hmtx, upm


def char_left_x(font, cmap, hmtx, upm, text, idx, font_size, letter_spacing):
    """X position of the left edge of character at index idx (text starts at 0)."""
    scale = font_size / upm
    x = 0.0
    for i in range(idx):
        gname = cmap.get(ord(text[i]), ".notdef")
        x += hmtx.metrics[gname][0] * scale + letter_spacing
    return x


def char_visual_right_x(font, cmap, hmtx, upm, text, idx, font_size, letter_spacing):
    """X position of the visual right edge of character at index idx."""
    scale = font_size / upm
    left  = char_left_x(font, cmap, hmtx, upm, text, idx, font_size, letter_spacing)
    gname = cmap.get(ord(text[idx]), ".notdef")
    if "glyf" in font:
        g    = font["glyf"][gname]
        xmax = getattr(g, "xMax", None)
        if xmax is not None:
            return left + xmax * scale
    return left + hmtx.metrics[gname][0] * scale


def measure_text_tight(font, cmap, hmtx, upm, text, font_size, letter_spacing):
    """Left-edge of first char to visual right-edge of last char."""
    return char_visual_right_x(font, cmap, hmtx, upm, text, len(text)-1, font_size, letter_spacing)


def b64_font(name):
    return base64.b64encode((FONTS_DIR / name).read_bytes()).decode()


def get_mark_path():
    svg = (ASSETS_DIR / "mark.svg").read_text()
    m   = re.search(r'<path[^>]+\bd="([^"]+)"', svg, re.DOTALL)
    return m.group(1)


NAME       = "BRYAN BISCHOF  Ph.D."
TAGLINE    = "AI   ·   MATH   ·   SIDEQUESTS"
FONT_SIZE  = 30
LETTER_SPC = 4
TAG_SIZE   = 14
TAG_SPC    = 2

reg_font_path = FONTS_DIR / "GeistMono-Regular.ttf"
font, cmap, hmtx, upm = load_font(reg_font_path)

# "A" is index 3 in "BRYAN BISCHOF  Ph.D."
# "h" is index 16
IDX_A = NAME.index("A")          # first A = index 3
IDX_H = NAME.index("h")          # first h = index 16

tag_left  = char_left_x(font, cmap, hmtx, upm, NAME, IDX_A, FONT_SIZE, LETTER_SPC)
tag_right = char_visual_right_x(font, cmap, hmtx, upm, NAME, IDX_H, FONT_SIZE, LETTER_SPC)
tag_cx    = (tag_left + tag_right) / 2

rule_w = round(measure_text_tight(font, cmap, hmtx, upm, NAME, FONT_SIZE, LETTER_SPC))

MARK_PX  = 88
MARK_OFF = 24
H        = 130
mark_top = (H - MARK_PX) // 2
gap_mark = 22
tx       = MARK_OFF + MARK_PX + gap_mark
pad_r    = 24
W        = tx + rule_w + pad_r

name_y = 50
rule_y = 70
tag_y  = 92


def make_svg(dark=False):
    orange = ORANGE_DARK if dark else ORANGE_LIGHT
    green  = GREEN_DARK  if dark else GREEN_LIGHT
    bg     = BG_DARK     if dark else BG_LIGHT
    ink    = INK_DARK    if dark else INK_LIGHT
    muted  = MUT_DARK    if dark else MUT_LIGHT

    bold_b64 = b64_font("GeistMono-Bold.ttf")
    reg_b64  = b64_font("GeistMono-Regular.ttf")
    mark_d   = get_mark_path()
    scale    = MARK_PX / 1254
    tag_abs  = tx + tag_cx   # absolute x centre of tagline

    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <style>
      @font-face {{
        font-family: 'GM';
        font-weight: 700;
        src: url('data:font/truetype;base64,{bold_b64}') format('truetype');
      }}
      @font-face {{
        font-family: 'GM';
        font-weight: 400;
        src: url('data:font/truetype;base64,{reg_b64}') format('truetype');
      }}
    </style>
    <linearGradient id="mg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="{orange}"/>
      <stop offset="100%" stop-color="{green}"/>
    </linearGradient>
  </defs>

  <rect width="{W}" height="{H}" fill="{bg}"/>

  <g transform="translate({MARK_OFF},{mark_top}) scale({scale:.6f})">
    <path d="{mark_d}" fill="url(#mg)" fill-rule="evenodd"/>
  </g>

  <text x="{tx}" y="{name_y}" font-family="GM" font-weight="400" font-size="{FONT_SIZE}"
        fill="{ink}" dominant-baseline="middle" letter-spacing="{LETTER_SPC}">{NAME}</text>

  <line x1="{tx}" y1="{rule_y}" x2="{tx + rule_w}" y2="{rule_y}"
        stroke="{orange}" stroke-width="1"/>

  <text x="{tag_abs:.1f}" y="{tag_y}" font-family="GM" font-weight="400"
        font-size="{TAG_SIZE}" fill="{muted}" dominant-baseline="middle"
        letter-spacing="{TAG_SPC}" text-anchor="middle">{TAGLINE}</text>
</svg>"""


for variant, dark in [("light", False), ("dark", True)]:
    out = ASSETS_DIR / f"wordmark-{variant}.svg"
    out.write_text(make_svg(dark=dark))
    print(f"Saved → {out}  (W={W}, rule_w={rule_w}, tag_left={tag_left:.1f}, tag_right={tag_right:.1f})")
    subprocess.run(["qlmanage", "-t", "-s", str(W), "-o", "/tmp", str(out)], capture_output=True)
    print(f"Rendered → /tmp/wordmark-{variant}.svg.png")
