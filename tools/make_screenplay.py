"""Generate SCREENPLAY.txt from SCRIPT.tex.

SCRIPT.tex is the single source of the spoken text. This script reads the macros
\\slide{number}{title}{speaker}{end}, \\cue{...}, \\stage{...}, \\evita{...}, \\ben{...} and
\\both{...}, strips the little LaTeX they contain, and writes the plain-text screenplay for
rehearsal and text-to-speech. It also counts the words of every slide, converts them to time at 140 words per minute, and
rewrites the timing table in SCRIPT.tex between the lines "% timing-begin" and "% timing-end".

    python3 -I tools/make_screenplay.py
"""
import pathlib, re, textwrap

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "SCRIPT.tex"
OUT = ROOT / "SCREENPLAY.txt"
WPM = 140

HEADER = """HIGHLY ACCURATE PROTEIN STRUCTURE PREDICTION WITH ALPHAFOLD
A presentation of Jumper et al., Nature 2021 (AlphaFold 2).
Machine Learning for Genomics (263-5351-00L), ETH Zurich, fall 2026.
Presenters: Evita Bosch Pokunevich (slides 1 to 10) and Ben Bullinger (slides 11 to 20).

Generated from SCRIPT.tex by tools/make_screenplay.py. Edit SCRIPT.tex, not this file.

Timing: 25 minutes for the talk, then 10 minutes for the exam question and the discussion.
The handover is after slide 10 at about 12 minutes. The end times are computed from the word
counts at 140 words per minute and leave about half a minute of reserve.

Format: lines in square brackets name the slide, the speaker and the time at which the slide
ends. Lines in round brackets are stage directions. All other lines are spoken as written.
Symbols are written as they are said: C alpha, angstrom, q transposed k, N eff.
"""

def balanced(s, i):
    """s[i] == '{'. Return (content, index after the closing brace)."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{": depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0: return s[i + 1:j], j + 1
    raise SystemExit("unbalanced braces")

def plain(t):
    t = re.sub(r"\\emph\{([^}]*)\}", r"\1", t)
    t = t.replace("\\%", "%").replace("\\&", "&").replace("\\,", " ").replace("~", " ")
    t = t.replace("\\\"u", "ü").replace("\\ldots", "...").replace("``", '"').replace("''", '"')
    t = re.sub(r"\s+", " ", t).strip()
    if "\\" in t: raise SystemExit(f"LaTeX left in spoken text: {t[:80]}")
    return t

src = SRC.read_text()
tokens = []   # (kind, parts)
for m in re.finditer(r"\\(slide|cue|stage|evita|ben|both)\{", src):
    kind = m.group(1); i = m.end() - 1; parts = []
    n = 4 if kind == "slide" else 1
    for _ in range(n):
        content, i = balanced(src, i); parts.append(content)
        while i < len(src) and src[i] in " \n": i += 1
    tokens.append((kind, parts))

out = [HEADER]; counts = []; slide = None; words = 0; speaker = None
def close():
    if slide is not None: counts.append((slide, words))
for kind, parts in tokens:
    if kind == "slide":
        close(); slide = (parts[0], plain(parts[1]), plain(parts[2])); words = 0; speaker = None
        label = "TITLE SLIDE" if parts[0] == "Title" else ("BACKUP " + parts[0][1:] if parts[0].startswith("B") else "SLIDE " + parts[0])
        timing = plain(parts[3]); timing = timing[0].upper() + timing[1:]
        out.append(f"\n[{label}. {plain(parts[1])}. {plain(parts[2])}. {timing}.]\n")
        # the speaker's name comes right after the header, before any stage direction
        for k2, p2 in tokens[tokens.index((kind, parts)) + 1:]:
            if k2 == "slide": break
            if k2 in ("evita", "ben", "both"):
                speaker = {"evita": "EVITA", "ben": "BEN", "both": "EVITA AND BEN"}[k2]; out.append(f"{speaker}\n"); break
    elif kind == "cue":
        out.append(f"\n[{plain(parts[0])}]\n")
    elif kind == "stage":
        out.append(f"({plain(parts[0])})\n")
    else:
        name = {"evita": "EVITA", "ben": "BEN", "both": "EVITA AND BEN"}[kind]
        if name != speaker: out.append(f"{name}\n"); speaker = name
        text = plain(parts[0]); words += len(text.split())
        out.append(textwrap.fill(text, 100) + "\n")
close()
OUT.write_text("\n".join(out))
print(f"wrote {OUT}")
total = 0; rows = []; t = 0.0
for (num, title, who), w in counts:
    sec = w / WPM * 60
    if not num.startswith("B") and num not in ("21", "22"):
        total += w; t += sec
        end = f"{int(t // 60)}:{int(round(t % 60)):02d}"
        rows.append(f"{num} & {title} & {who} & {end} & {w} \\\\")
        if num == "10": rows.append("\\midrule")
    print(f"{num:>5}  {w:4d} words  {sec:5.0f} s  {title}")
print(f"talk total {total} words, {total / WPM:.1f} min at {WPM} words per minute")
rows.append("\\midrule")
rows.append("21 & Exam question & both & about 27:30 & \\\\")
rows.append("22 & Questions for the audience & both & about 35:00 & \\\\")
tex = SRC.read_text()
for (num, title, who), w in counts:
    if num.startswith("B") or num in ("21", "22"): continue
    t_end = next(r for r in rows if r.startswith(f"{num} & ")).split(" & ")[3]
    tex, n = re.subn(r"(\\slide\{" + num + r"\}\{[^}]*\}\{[^}]*\}\{)[^}]*\}", lambda m: m.group(1) + "ends at " + t_end + "}", tex)
    assert n == 1, num
a = tex.index("% timing-begin\n") + len("% timing-begin\n"); b = tex.index("% timing-end")
SRC.write_text(tex[:a] + "\n".join(rows) + "\n" + tex[b:])
print("timing table in SCRIPT.tex updated")
