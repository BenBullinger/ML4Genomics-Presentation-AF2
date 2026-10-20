# Working notes, not for release

Everything in `_DEV/` stays out of the public repository. The deck and the note are one level up.

Jumper et al., Nature 596 (2021), presented by Evita Bosch Pokunevich and Ben Bullinger in Machine Learning for Genomics (263-5351-00L), fall 2026. Guidelines: `guidelines.pdf` in this folder.

## Format, from the guidelines

| | |
|---|---|
| Part 1 | 25 minutes. A reminder one minute before the end, cut off at 25. |
| Part 2 | 10 minutes. Our answer to the exam question, then at least two questions for the audience and a moderated discussion. |
| Exam question | Sent to us about seven days before the talk. A TA may be asked once about the answer. |
| Upload | Slides as `PP<i>.<name>.<family name>.pdf` to https://cloud.inf.ethz.ch/s/tBRxHGbXZeQ3Jzr by the day before the talk. |
| Backup slides | Recommended for follow-up questions. In the deck after `\appendix`, not counted in the slide total. |

## Schedule

| When | What | Done |
|---|---|---|
| TODO date | Presentation | |
| the day before, TODO date | Upload `PP<i>.TODO.pdf` | |
| about seven days before, TODO date | Exam question arrives. Fill slide "Exam question". | |
| end of the week of 12 October | Dry run | |
| 13 October | Work split agreed, see `WORK-SPLIT.md` | x |

Open: the index `<i>` and whose name the file carries when two people present. Ask the head TA, Lovro Rabuzin.

## Files

| | |
|---|---|
| `../main.tex` | The deck. Build from the repo root with `latexmk -pdf main.tex`. The exam question and the questions for the audience are placeholders. Eleven backup slides after `\appendix`, one question per slide with the source as subtitle, at most three lines of derivation, the answer in blue. |
| `SCRIPT.md`, `SCREENPLAY.txt` | Speaker notes and the rehearsal text, `python3 make_screenplay.py` makes the second from the first. Written for 30 minutes, to be cut to 25. |
| `WORK-SPLIT.md` | Who presents which slides. |
| `../SYMMETRY.tex` | Three pages on invariance, equivariance and chirality in the structure module and the loss, with the SI's equations. Blue headings are Evita's slides, red Ben's. |
| `background/` | The sources, `README.md` lists them, `SLIDE-CHECK.md` gives the source of each slide statement and the questions to expect. |
| `../_AF2.pdf`, `../_AF2-SI.pdf`, `../AF3.pdf` | The articles and the supplement. The slides cut their figures from them. |

Upload copy, from the repo root: `cp main.pdf PP<i>.<name>.<family name>.pdf`.

Before the public release: nothing in `_DEV/` goes public. The theme files, the ETH logo, the course guidelines, Petar's tutorial, AF1 and the background papers without an open licence all live here. Publish a fresh repository with the files one level up.
