#!/usr/bin/env python3
"""Draw THE THURSDAY GLOBE — a one-day world news image for 26 Nov 2026.
Built fresh with PIL. Output: entry.png, 1024x1024, under 1 MiB.
Layout: navy masthead, one big lead panel (US tariffs + Nasdaq chart),
then a 2x4 grid of short story panels. Text is short, large, legible.
Fixes: lead headline sized to fit exactly 2 lines; story sublines
shortened to fit one line each; chart bars scaled so the NASDAQ label
clears them; grid sized so the footer never overlaps the last row.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 229)
INK = (26, 26, 26)
NAVY = (22, 35, 63)
GOLD = (217, 164, 65)
RED = (179, 38, 30)
WHITE = (255, 255, 255)
GREY = (90, 90, 90)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, font, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

def draw_icon(d, kind, x, y, s, color):
    """Small simple glyph in a colored square, s = square size."""
    d.rectangle([x, y, x + s, y + s], fill=color)
    cx, cy = x + s // 2, y + s // 2
    if kind == "flame":
        d.polygon([(cx, y + 8), (cx + 13, cy + 6), (cx + 8, y + s - 8),
                   (cx - 8, y + s - 8), (cx - 13, cy + 6)], fill=(255, 255, 255))
        d.polygon([(cx, y + 18), (cx + 6, cy + 4), (cx, y + s - 12),
                   (cx - 6, cy + 4)], fill=(255, 190, 60))
    elif kind == "ship":
        d.polygon([(x + 8, y + s - 14), (x + s - 8, y + s - 14),
                   (x + s - 16, y + s - 6), (x + 16, y + s - 6)], fill=(255, 255, 255))
        d.rectangle([cx - 2, y + 8, cx + 2, y + s - 14], fill=(255, 255, 255))
        d.polygon([(cx + 2, y + 10), (cx + 14, y + 18), (cx + 2, y + 18)], fill=(255, 255, 255))
    elif kind == "plane":
        d.polygon([(x + 8, cy), (x + s - 10, cy - 8), (x + s - 6, cy),
                   (x + s - 10, cy + 8)], fill=(255, 255, 255))
        d.polygon([(cx - 4, cy - 4), (cx + 6, cy - 16), (cx + 10, cy - 4)], fill=(255, 255, 255))
        d.polygon([(cx - 4, cy + 4), (cx + 6, cy + 16), (cx + 10, cy + 4)], fill=(255, 255, 255))
    elif kind == "burst":
        for a in range(0, 360, 45):
            import math
            r1, r2 = 6, 18
            x1 = cx + r1 * math.cos(math.radians(a))
            y1 = cy + r1 * math.sin(math.radians(a))
            x2 = cx + r2 * math.cos(math.radians(a))
            y2 = cy + r2 * math.sin(math.radians(a))
            d.line([x1, y1, x2, y2], fill=(255, 255, 255), width=4)
        d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(255, 255, 255))
    elif kind == "stars":
        d.ellipse([x + 8, y + 8, x + s - 8, y + s - 8], outline=(255, 255, 255), width=3)
        import math
        for a in range(0, 360, 45):
            px = cx + 11 * math.cos(math.radians(a))
            py = cy + 11 * math.sin(math.radians(a))
            d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(255, 220, 80))
    elif kind == "mountain":
        d.polygon([(x + 6, y + s - 8), (cx, y + 8), (x + s - 6, y + s - 8)], fill=(255, 255, 255))
        d.line([x + 8, y + s - 10, x + s - 8, y + s - 10], fill=(120, 200, 255), width=3)
    elif kind == "rocket":
        d.polygon([(cx, y + 6), (cx + 9, cy + 2), (cx + 6, y + s - 10),
                   (cx - 6, y + s - 10), (cx - 9, cy + 2)], fill=(255, 255, 255))
        d.ellipse([cx - 4, cy - 2, cx + 4, cy + 6], fill=color)
        d.polygon([(cx - 6, y + s - 12), (cx - 12, y + s - 4), (cx - 2, y + s - 8)], fill=(255, 190, 60))
        d.polygon([(cx + 6, y + s - 12), (cx + 12, y + s - 4), (cx + 2, y + s - 8)], fill=(255, 190, 60))
    elif kind == "warn":
        d.polygon([(cx, y + 8), (cx + 16, y + s - 8), (cx - 16, y + s - 8)], fill=(255, 255, 255))
        d.rectangle([cx - 2, y + 16, cx + 2, y + s - 18], fill=color)
        d.ellipse([cx - 2, y + s - 14, cx + 2, y + s - 10], fill=color)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 118], fill=NAVY)
f_title = F(SERIF_B, 66)
t = "THE THURSDAY GLOBE"
tw = d.textlength(t, font=f_title)
d.text(((W - tw) / 2, 12), t, font=f_title, fill=WHITE)
f_date = F(SANS_B, 30)
dt = "THURSDAY 26 NOVEMBER 2026"
dw = d.textlength(dt, font=f_date)
d.text(((W - dw) / 2, 82), dt, font=f_date, fill=GOLD)
d.rectangle([0, 118, W, 122], fill=GOLD)

# ---------- lead panel ----------
LX, LY, LW, LH = 16, 134, 992, 268
d.rectangle([LX, LY, LX + LW, LY + LH], fill=WHITE, outline=INK, width=3)
f_kick = F(SANS_B, 21)
d.text((LX + 20, LY + 14), "LEAD  •  TRADE WAR", font=f_kick, fill=RED)
# headline: shrink until it fits exactly 2 lines in 560 px
head = "US SLAPS SWEEPING TARIFFS ON 14 PARTNERS"
size = 42
while True:
    f_head = F(SANS_B, size)
    lines = wrap(d, head, f_head, 560)
    if len(lines) <= 2 or size <= 30:
        break
    size -= 2
for i, line in enumerate(lines):
    d.text((LX + 20, LY + 46 + i * 46), line, font=f_head, fill=INK)
# sublines start below the headline block
sy = LY + 46 + len(lines) * 46 + 8
f_sub = F(SANS, 23)
subs = ["China, EU, Japan, India hit in a crackdown",
        "on factory overcapacity.",
        "Nasdaq falls ~4% as the AI sell-off",
        "rattles markets."]
for i, line in enumerate(subs):
    d.text((LX + 20, sy + i * 28), line, font=f_sub, fill=(60, 60, 60))

# chart on the right of the lead panel (bars scaled so the label clears)
CX0, CY0, CW, CH = LX + 620, LY + 40, 350, 190
d.rectangle([CX0, CY0, CX0 + CW, CY0 + CH], fill=(250, 246, 236), outline=(200, 190, 170), width=2)
bars = [111, 113, 110, 115, 111, 108, 89, 71, 52]
bw = CW // len(bars)
for i, v in enumerate(bars):
    bx = CX0 + 12 + i * bw
    top = CY0 + CH - 24 - v
    col = RED if i >= 6 else (120, 130, 150)
    d.rectangle([bx + 3, top, bx + bw - 3, CY0 + CH - 24], fill=col)
d.line([CX0 + 8, CY0 + CH - 24, CX0 + CW - 8, CY0 + CH - 24], fill=INK, width=2)
f_chart = F(SANS_B, 26)
d.text((CX0 + 14, CY0 + 8), "NASDAQ", font=f_chart, fill=INK)
f_drop = F(SANS_B, 40)
drop = "-4%"
dw2 = d.textlength(drop, font=f_drop)
d.text((CX0 + CW - dw2 - 14, CY0 + 4), drop, font=f_drop, fill=RED)

# ---------- story grid: 2 cols x 4 rows ----------
# sublines shortened so each fits on ONE line inside the panel
stories = [
    ("CAIRO", "TANKER FIRE KILLS AT LEAST 31", "Blaze on the ring road", "flame", (200, 80, 30)),
    ("YEMEN", "HOUTHIS HIT SAUDI PORTS", "Ras Tanura refinery also hit", "ship", (40, 90, 140)),
    ("IRAN", "US TELLS CITIZENS: LEAVE IRAN", "War fears grow as tensions rise", "warn", (150, 40, 40)),
    ("UKRAINE", "UKRAINE HITS RUSSIAN AIRBASE", "Five jets damaged: 3 MiG-31, 2 Su-34", "plane", (60, 70, 110)),
    ("NORTH KOREA", "KIM: MORE TACTICAL NUKES", "Wider deployment of nuclear arms", "burst", (120, 90, 20)),
    ("EUROPE", "EU SPLIT OVER €45BN LOAN", "Leaders clash over Ukraine aid", "stars", (30, 60, 130)),
    ("INDONESIA", "MINE FLOOD KILLS 13 IN BOGOR", "13 more trapped in illegal gold mine", "mountain", (90, 70, 40)),
    ("SPACE", "FIRST PAKISTANI IN SPACE", "Zeeshan Ali boards Tiangong station", "rocket", (50, 80, 130)),
]
GX, GY = 16, 414
GW, GH, GAP = 490, 136, 10
f_tag = F(SANS_B, 17)
f_sh = F(SANS_B, 23)
f_ss = F(SANS, 18)
for idx, (tag, head, sub, icon, color) in enumerate(stories):
    col, row = idx % 2, idx // 2
    x = GX + col * (GW + GAP)
    y = GY + row * (GH + GAP)
    d.rectangle([x, y, x + GW, y + GH], fill=WHITE, outline=INK, width=2)
    d.rectangle([x, y, x + 8, y + GH], fill=color)
    draw_icon(d, icon, x + 20, y + 14, 46, color)
    d.text((x + 78, y + 10), tag, font=f_tag, fill=color)
    lines = wrap(d, head, f_sh, GW - 96)
    for i, line in enumerate(lines[:2]):
        d.text((x + 78, y + 34 + i * 27), line, font=f_sh, fill=INK)
    sy = y + 34 + min(len(lines), 2) * 27 + 4
    d.text((x + 78, sy), sub, font=f_ss, fill=GREY)

# footer line (grid bottom is 414 + 4*136 + 3*10 = 988, so 996 clears it)
f_foot = F(SANS, 18)
foot = "THE THURSDAY GLOBE  •  WORLD NEWS OF THURSDAY 26 NOVEMBER 2026"
fw = d.textlength(foot, font=f_foot)
d.text(((W - fw) / 2, 996), foot, font=f_foot, fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png")
