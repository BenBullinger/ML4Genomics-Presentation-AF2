"""Measure the boxes of the paper figures that the slides mark, and write boxes.tex.

Every red callout in main.tex is drawn by \callbox{figure/box} around a rectangle that this
script measures on a 600 dpi render of the exact crop used on the slide. Run it after changing
a crop (page or trim) in main.tex, or after adding a box here:

    python3 -I tools/measure_boxes.py

The crops below must match the \begin{marked...}[..]{page}{trim} lines in main.tex; the script
checks that and stops if one does not. Coordinates are fractions of the crop, (0,0) bottom left.
"""
import re, subprocess, sys, pathlib
from collections import deque
import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
LIT = ROOT / "literature"
OUT = ROOT / "boxes.tex"
DPI = 600
ERODE = 20   # px at 600 dpi, about 0.85 mm: wider than any arrow or letter, narrower than any block

# figure: (file, page, trim "l b r t" as in main.tex)
FIGURES = {
    "fig1e": ("_AF2.pdf", 2, "40 419 25 214"),
    "fig3a": ("_AF2.pdf", 4, "40 616 25 52"),
    "fig3d": ("_AF2.pdf", 4, "40 358 302 295"),
    "sfig2": ("_AF2-SI.pdf", 16, "52bp 605bp 38bp 52bp"),
    "sfig8": ("_AF2-SI.pdf", 28, "55bp 501bp 55bp 55bp"),
    "sfig9": ("_AF2-SI.pdf", 37, "158 547 290 45"),   # the GDT columns against the truth and against the mirror
    "af3":   ("AF3.pdf", 2, "44 344 30 329"),
}
# box: (figure, mode, parameters). Modes:
#   fill     (cx, cy): flood fill from a seed inside a filled box, the extent of that fill
#   nonwhite (x0, y0, x1, y1): the solid elements inside the window. Thin strokes (arrows,
#            connectors, text) are removed by an erosion of ERODE pixels before the extent is
#            taken, so a box ends at the block and does not follow an arrow out of it. A fifth
#            number sets a smaller erosion for thin elements such as the frame wedges.
#   window   (x0, y0, x1, y1, thr): everything darker than thr inside the window, no erosion. For
#            an image with its label on a tinted background: thr below the background's luminance
#   dark     (x0, y0, x1, y1): black outlines and text inside the window
#   blue     (x0, y0, x1, y1): blue marks inside the window
BOXES = {
    "fig1e/msa":        ("nonwhite", 0.22, 0.69, 0.37, 1.00),
    "fig1e/templates":  ("window", 0.26, 0.14, 0.33, 0.36, 200),   # the black squares and the word Templates, not the grey background
    "fig1e/evoformer":  ("fill", 0.57, 0.60),
    "fig1e/structure":  ("fill", 0.78, 0.35),
    "fig1e/recycling":  ("fill", 0.60, 0.045),
    "fig1e/output":     ("nonwhite", 0.86, 0.30, 1.00, 0.80, 8),
    "fig3a/rowatt":     ("fill", 0.16, 0.70),
    "fig3a/opm":        ("dark", 0.35, 0.33, 0.44, 0.62),
    "fig3a/triangles":  ("dark", 0.42, 0.03, 0.76, 0.40),
    "fig3d/ipa":        ("fill", 0.39, 0.45),
    "fig3d/update":     ("fill", 0.48, 0.34),
    "fig3d/frames":     ("nonwhite", 0.63, 0.105, 0.83, 0.29, 6),
    "fig3d/atoms":      ("fill", 0.79, 0.66),
    "sfig2/pairbias":   ("nonwhite", 0.30, 0.00, 0.48, 0.33),
    "sfig2/gating":     ("nonwhite", 0.68, 0.575, 0.79, 1.00, 30),
    "sfig2/plus":       ("dark", 0.455, 0.44, 0.48, 0.53),
    "sfig8/pairbias":   ("nonwhite", 0.38, 0.69, 0.48, 0.86),
    "sfig8/dot":        ("nonwhite", 0.35, 0.455, 0.47, 0.595),
    "sfig8/sqdist":     ("nonwhite", 0.35, 0.225, 0.47, 0.352),
    "sfig8/invert":     ("dark", 0.72, 0.08, 0.80, 0.18),
    "sfig8/plus":       ("dark", 0.48, 0.49, 0.51, 0.57),
    "sfig9/lowgroup":   ("blue", 0.33, 0.09, 0.52, 0.38),
    "af3/msa":          ("fill", 0.44, 0.55),
    "af3/pairformer":   ("fill", 0.56, 0.50),
    "af3/diffusion":    ("fill", 0.78, 0.45),
}

def page_size(pdf, page):
    out = subprocess.run(["pdfinfo", "-f", str(page), "-l", str(page), str(pdf)], capture_output=True, text=True).stdout
    m = re.search(r"Page\s+%d size:\s+([\d.]+) x ([\d.]+)" % page, out)
    return float(m.group(1)), float(m.group(2))

def render(fig):
    f, page, trim = FIGURES[fig]
    l, b, r, t = [float(v.replace("bp", "")) for v in trim.split()]
    W, H = page_size(LIT / f, page)
    k = DPI / 72
    w, h = W - l - r, H - t - b
    png = pathlib.Path("/tmp") / f"boxes-{fig}"
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(DPI), "-x", str(round(l * k)), "-y", str(round(t * k)),
                    "-W", str(round(w * k)), "-H", str(round(h * k)), "-png", "-singlefile", str(LIT / f), str(png)], check=True)
    return np.array(Image.open(str(png) + ".png").convert("RGB")).astype(int)

def measure(arr, mode, *a):
    ph, pw = arr.shape[:2]
    if mode == "fill":
        cx, cy = a; px, py = int(cx * pw), int((1 - cy) * ph); c = arr[py, px]
        if c.min() > 248: raise SystemExit(f"seed ({cx},{cy}) is on white")
        mask = np.abs(arr - c).sum(axis=2) < 30
        seen = np.zeros((ph, pw), bool); q = deque([(py, px)]); seen[py, px] = True; ys = [py]; xs = [px]
        while q:
            y, x = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < ph and 0 <= nx < pw and not seen[ny, nx] and mask[ny, nx]:
                    seen[ny, nx] = True; q.append((ny, nx)); ys.append(ny); xs.append(nx)
        X0, X1, Y0, Y1 = min(xs), max(xs), min(ys), max(ys)
    else:
        x0, y0, x1, y1 = a[:4]
        X0w, X1w = int(x0 * pw), int(x1 * pw); Y0w, Y1w = int((1 - y1) * ph), int((1 - y0) * ph)
        sub = arr[Y0w:Y1w, X0w:X1w]; r, g, b = sub[..., 0], sub[..., 1], sub[..., 2]
        lum = 0.3 * r + 0.59 * g + 0.11 * b; sat = np.maximum(np.maximum(abs(r - g), abs(g - b)), abs(r - b))
        if mode == "nonwhite":
            m = lum < 245
            # erosion by a square of ERODE pixels through a summed-area table: a pixel survives
            # only if its whole neighbourhood is non-white
            k = int(a[4]) if len(a) > 4 else ERODE; pad = np.pad(m.astype(np.int32), ((k, k), (k, k)))
            S = pad.cumsum(0).cumsum(1); S = np.pad(S, ((1, 0), (1, 0)))
            h2, w2 = m.shape
            tot = S[k + k:k + k + h2, k + k:k + k + w2] - S[0:h2, k + k:k + k + w2] - S[k + k:k + k + h2, 0:w2] + S[0:h2, 0:w2]
            core = tot == (2 * k) * (2 * k)
            if not core.any(): raise SystemExit(f"{mode} window {a}: nothing survives the erosion")
            # keep every connected piece that is at least 3 % of the largest: arrowheads survive
            # the erosion only as tiny blobs, while the slabs and wedges of a group all stay
            seen = np.zeros_like(core); comps = []
            ys0, xs0 = np.where(core)
            for sy, sx in zip(ys0, xs0):
                if seen[sy, sx]: continue
                q = deque([(sy, sx)]); seen[sy, sx] = True; comp = []
                while q:
                    y, x = q.popleft(); comp.append((y, x))
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < h2 and 0 <= nx < w2 and not seen[ny, nx] and core[ny, nx]:
                            seen[ny, nx] = True; q.append((ny, nx))
                comps.append(comp)
            big = max(len(c) for c in comps)
            keep = [pt for c in comps if len(c) >= 0.03 * big for pt in c]
            ys = np.array([c[0] for c in keep]); xs = np.array([c[1] for c in keep])
            X0, X1, Y0, Y1 = X0w + xs.min() - k, X0w + xs.max() + k, Y0w + ys.min() - k, Y0w + ys.max() + k
        else:
            if mode == "window":
                m = lum < a[4]
                if not m.any(): raise SystemExit(f"window {a}: nothing darker than {a[4]}")
                ys, xs = np.where(m)
                return (X0w + xs.min()) / pw, 1 - (Y0w + ys.max()) / ph, (X0w + xs.max()) / pw, 1 - (Y0w + ys.min()) / ph
            if mode == "dark": m = (lum < 120) & (sat < 60)
            elif mode == "blue": m = (b > r + 40) & (b > g + 20)
            else: raise SystemExit(mode)
            rows = np.where(m.sum(axis=1) > 0.15 * m.sum(axis=1).max())[0]; cols = np.where(m.sum(axis=0) > 0.15 * m.sum(axis=0).max())[0]
            X0, X1, Y0, Y1 = X0w + cols.min(), X0w + cols.max(), Y0w + rows.min(), Y0w + rows.max()
    return X0 / pw, 1 - Y1 / ph, X1 / pw, 1 - Y0 / ph

def check_main():
    main = (ROOT / "main.tex").read_text()
    for fig, (f, page, trim) in FIGURES.items():
        pat = r"\\begin\{marked(?:SI|AFthree)?\}(?:\[[^\]]*\])?\{%d\}\{%s\}" % (page, re.escape(trim))
        if not re.search(pat, main):
            raise SystemExit(f"{fig}: no \\begin{{marked..}}{{{page}}}{{{trim}}} in main.tex, update FIGURES or main.tex")

check_main()
lines = ["% Generated by tools/measure_boxes.py from the figure crops. Do not edit by hand.",
         "% \\definebox{figure/box}{x0}{y0}{x1}{y1}, fractions of the crop, (0,0) bottom left."]
arrays = {}
for name, (mode, *a) in BOXES.items():
    fig = name.split("/")[0]
    if fig not in arrays: arrays[fig] = render(fig)
    x0, y0, x1, y1 = measure(arrays[fig], mode, *a)
    lines.append("\\definebox{%s}{%.4f}{%.4f}{%.4f}{%.4f}" % (name, x0, y0, x1, y1))
    print(f"{name:18s} x {x0:.3f}..{x1:.3f}  y {y0:.3f}..{y1:.3f}")
OUT.write_text("\n".join(lines) + "\n")
# boxes of one figure must not touch: the slides add 1 mm of padding on every side, about
# 0.012 of a figure 85 mm wide, so neighbours need a gap of at least 0.03 in both axes or a
# clear separation in one of them
measured = {}
for ln in lines[2:]:
    name, *v = ln.replace("\\definebox{", "").replace("}", " ").replace("{", " ").split()
    measured[name] = tuple(float(x) for x in v)
names = sorted(measured)
for i, a in enumerate(names):
    for b in names[i + 1:]:
        if a.split("/")[0] != b.split("/")[0]: continue
        ax0, ay0, ax1, ay1 = measured[a]; bx0, by0, bx1, by1 = measured[b]
        gap_x = max(bx0 - ax1, ax0 - bx1); gap_y = max(by0 - ay1, ay0 - by1)
        if max(gap_x, gap_y) < 0.03:
            print(f"WARNING {a} and {b} are closer than the padding: gap x {gap_x:.3f}, y {gap_y:.3f}")
print("wrote", OUT)
