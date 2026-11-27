"""Preview sheet: every icon at 48px (2x) with name, light and dark panels, plus a 24px row."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from icons import ICONS

src = sys.argv[1]; out = sys.argv[2]
names = []
for n, s in ICONS.items():
    names.append(n)
    if 'active' in s:
        names.append(n + '-active')

COLS, CW, CH, PAD = 9, 120, 104, 32


def inner(name):
    t = open(f'{src}/{name}.svg').read()
    return re.sub(r'^<svg[^>]*>', '', t.strip())[:-6]


def panel(x0, y0, bg, fg, label_fg, accent):
    rows = -(-len(names) // COLS)
    h = rows * CH + PAD * 2 + 30
    parts = [f'<rect x="{x0}" y="{y0}" width="{COLS*CW+PAD*2}" height="{h}" rx="16" fill="{bg}"/>']
    for i, n in enumerate(names):
        r, c = divmod(i, COLS)
        x = x0 + PAD + c * CW + (CW - 48) / 2
        y = y0 + PAD + 30 + r * CH
        col = accent if n.endswith('-active') else fg
        parts.append(f'<svg x="{x}" y="{y}" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                     f'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" style="color:{col}" color="{col}">{inner(n)}</svg>')
        parts.append(f'<text x="{x+24}" y="{y+70}" text-anchor="middle" font-family="Figtree, sans-serif" font-size="12" fill="{label_fg}">{n}</text>')
    return parts, h


W = COLS * CW + PAD * 2
p1, h1 = panel(0, 60, '#FFFFFF', '#17192A', '#555B6E', '#5141D7')
p2, h2 = panel(0, 60 + h1 + 24, '#171923', '#F7F8FC', '#B6BCD0', '#A69AFF')
# 24px actual-size strip
y3 = 60 + h1 + h2 + 48
strip = [f'<text x="0" y="{y3}" font-family="Figtree, sans-serif" font-size="14" font-weight="600" fill="#17192A">Actual size, 24 px</text>']
for i, n in enumerate([n for n in names if not n.endswith('-active')]):
    r, c = divmod(i, 33)
    x = c * 32; y = y3 + 16 + r * 36
    strip.append(f'<svg x="{x}" y="{y}" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" style="color:#17192A" color="#17192A">{inner(n)}</svg>')
H = y3 + 16 + 2 * 36 + 16
head = (f'<text x="0" y="36" font-family="Figtree, sans-serif" font-size="24" font-weight="700" fill="#17192A">Yuhshi UI icons v1</text>'
        f'<text x="{W}" y="36" text-anchor="end" font-family="Figtree, sans-serif" font-size="13" fill="#555B6E">24 px grid · 1.75 stroke · round · dot = person · tint = selected</text>')
doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 -4 {W} {H+4}">'
       f'<rect x="-40" y="-40" width="{W+80}" height="{H+80}" fill="#F6F7FB"/>{head}{"".join(p1)}{"".join(p2)}{"".join(strip)}</svg>')
open(out, 'w').write(doc)
print(W, H)
