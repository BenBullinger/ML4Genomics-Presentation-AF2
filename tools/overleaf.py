"""Manual transfer between the repository and Overleaf, which is not linked.

    python3 -I tools/overleaf.py out   fills to_overleaf/ with the deck, the script and the screenplay:
                                      main.tex, boxes.tex, literature/, SCRIPT.tex, SCREENPLAY.txt
    python3 -I tools/overleaf.py in    takes main.tex, boxes.tex and SCRIPT.tex from from_overleaf/ (files or a
                                      downloaded zip), copies them into the repository and prints what changed.
                                      SCREENPLAY.txt is not taken back, it is generated from SCRIPT.tex

Both folders are in .gitignore. Drag the content of to_overleaf/ into the Overleaf project. Download the
Overleaf project (Menu, Download, Source) into from_overleaf/ when Evita has edited there.
"""
import pathlib, shutil, subprocess, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
TO, FROM = ROOT / "to_overleaf", ROOT / "from_overleaf"
FILES = ["main.tex", "boxes.tex", "SCRIPT.tex"]
OUT_ONLY = ["SCREENPLAY.txt"]
FOLDERS = ["literature"]

def out():
    if TO.exists(): shutil.rmtree(TO)
    TO.mkdir()
    for f in FILES + OUT_ONLY: shutil.copy2(ROOT / f, TO / f)
    for d in FOLDERS: shutil.copytree(ROOT / d, TO / d)
    print("to_overleaf/ holds:", ", ".join(FILES + OUT_ONLY + [d + "/" for d in FOLDERS]))

def take_in():
    FROM.mkdir(exist_ok=True)
    for z in FROM.glob("*.zip"):
        with zipfile.ZipFile(z) as zf: zf.extractall(FROM / z.stem)
        print("unpacked", z.name)
    changed = False
    for f in FILES:
        hits = sorted(FROM.rglob(f))
        if not hits: print(f, "not found in from_overleaf/"); continue
        src = hits[0]
        if src.read_bytes() == (ROOT / f).read_bytes(): print(f, "unchanged"); continue
        shutil.copy2(src, ROOT / f); changed = True
        print(f, "updated from", src.relative_to(FROM))
        subprocess.run(["git", "--no-pager", "diff", "--stat", "--", f], cwd=ROOT)
    if changed: print("compile and check the changed slides, then commit on dev")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    {"out": out, "in": take_in}.get(cmd, lambda: print(__doc__))()
