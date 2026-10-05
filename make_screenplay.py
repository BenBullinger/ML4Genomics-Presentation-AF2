"""Write SCREENPLAY.txt from SCRIPT.md: the spoken text of the talk as plain text.

Usage, in the repo root:  python3 make_screenplay.py
Edit SCRIPT.md, not SCREENPLAY.txt.
"""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
END_OF_SPOKEN_TEXT = "## What could be cut"
HANDOVER = "*Handover to the second speaker.*"

# Symbols and names, written the way they are spoken. Longer patterns come first.
SPOKEN = [
    ("lDDT-Cα", "L D D T C alpha"),
    ("pLDDT", "p L D D T"),
    ("lDDT", "L D D T"),
    ("Cα", "C alpha"),
    ("ångström", "angstrom"),
    ("r.m.s.d. 95", "R M S D 95"),
    ("RoseTTAFold", "Rosetta Fold"),
    ("ESMFold", "E S M Fold"),
    ("CASP14", "CASP 14"),
    ("ORF8", "ORF 8"),
    ("T1024", "T 10 24"),
    ("T1064", "T 10 64"),
    ("LmrP", "L M R P"),
    ("IPA", "I P A"),
]


def spoken(text: str) -> str:
    for written, said in SPOKEN:
        text = text.replace(written, said)
    return text


def end_time(clock: str) -> str:
    """'10:30' -> 'minute 10 and a half'."""
    minutes, seconds = (int(part) for part in clock.split(":"))
    if minutes == 0:
        return f"{seconds} seconds"
    return f"minute {minutes}" + (" and a half" if seconds == 30 else "")


def main() -> None:
    script = (HERE / "SCRIPT.md").read_text(encoding="utf-8")

    # The time table: slide number -> clock time at which the slide ends.
    ends = {}
    for slides, clock in re.findall(r"^\| ([^|]+) \| [^|]+ \| [\d.]+ \| (\d+:\d\d) \|$", script, flags=re.M):
        ends[slides.split(",")[-1].strip()] = clock

    body = script[script.index("## Title"):script.index(END_OF_SPOKEN_TEXT)]
    out = [
        "HIGHLY ACCURATE PROTEIN STRUCTURE PREDICTION WITH ALPHAFOLD",
        "A talk on the paper by Jumper and co-authors, 2021. 30 minutes, 18 slides, two speakers.",
        "",
        "This is the text of SCRIPT.md, written the way it is spoken, for reading or for a text-to-speech app.",
        "Lines in square brackets name the slide. Lines in round brackets are directions. Everything else is spoken.",
        "",
    ]
    speaker = "FIRST SPEAKER"
    for section in re.split(r"^## ", body, flags=re.M)[1:]:
        heading, _, text = section.partition("\n")
        number = re.match(r"Slide (\d+): ", heading)
        if number:
            title = spoken(heading[number.end():])
            cue = f"[SLIDE {number.group(1)}. {title}. Ends at {end_time(ends[number.group(1)])}.]"
        else:
            cue = "[TITLE SLIDE.]"
        out += ["", cue, "", speaker]
        for paragraph in (p.strip() for p in text.split("\n\n")):
            if not paragraph:
                continue
            if paragraph == HANDOVER:
                speaker = "SECOND SPEAKER"
                out += ["", "[HANDOVER. The second speaker continues.]"]
            elif paragraph.startswith("*") and paragraph.endswith("*"):
                out += ["", "(" + spoken(paragraph.strip("*")) + ")"]
            else:
                out += ["", spoken(paragraph)]
    out += ["", "[END. Thirty minutes.]", ""]

    screenplay = "\n".join(out)
    screenplay.encode("ascii")  # fails if a symbol is left that a text-to-speech app could misread
    (HERE / "SCREENPLAY.txt").write_text(screenplay, encoding="ascii")
    lines_after_header = out[out.index("[TITLE SLIDE.]"):]
    words = sum(len(line.split()) for line in lines_after_header if line and line[0] not in "[(" and not line.isupper())
    print(f"SCREENPLAY.txt written: {words} spoken words, about {words / 130:.0f} minutes at 130 words per minute")


if __name__ == "__main__":
    main()
