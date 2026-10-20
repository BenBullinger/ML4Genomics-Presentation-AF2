# Release layout

Decided with Ben on 17 October 2026.

- `dev`: the working branch with everything: deck, script, screenplay, tools, `_DEV/`. One commit, named `init`. Deleted after the presentation.
- `main`: the final release only, one commit named `init`: `main.tex`, `main.pdf`, `boxes.tex`, `tools/measure_boxes.py`, `literature/`, `README.md`, `.gitignore`. No script, no screenplay, no `_DEV/`. The exam question slide is not built until the question arrives (`\examslidefalse` in `main.tex`).
- Overleaf is unlinked since 17 October. Ben uploads the deck to Overleaf by hand: `python3 -I tools/overleaf.py out` fills `to_overleaf/`, Overleaf downloads go into `from_overleaf/` and `python3 -I tools/overleaf.py in` copies `main.tex` and `boxes.tex` back. Both folders are ignored by git. The two `overleaf-2026-10-15-*` branches are Overleaf's old conflict branches and can be deleted.
- Every other branch is deleted.

The lecturer's `Lecture5_Folding.pdf` was moved out of the repository to `HS26/ML4Genomics/` and is in `.gitignore`. The symmetry note was deleted on 17 October. Both branches sit in one GitHub repository, so a public repository shows `dev` as well.

## Commands (Ben runs them)

Both branches are reset to one commit named `init` whenever Ben asks for it (last on 20 October 2026). Every block starts by changing into the repository and printing the remote, which must be `BenBullinger/ML4Genomics-Presentation-AF2`, and the commands are chained with `&&` so that a failure stops the block. On 20 October 2026 the unguarded version was run from the parent folder, where git found the home-directory repository, and rewrote that repository's `main` on Bitbucket; it was restored from `ad221cd`.

    cd ~/Library/CloudStorage/OneDrive-ETHZurich/HS26/ML4Genomics/ML4Genomics-Presentation-AF2 && git remote get-url origin

    git checkout --orphan dev-init && git add -A && git commit -m "init" && git branch -D dev && git branch -M dev && git push --force -u origin dev

    git checkout --orphan main-init && git rm -r --cached . && git add main.tex main.pdf boxes.tex tools/measure_boxes.py literature README.md .gitignore && git commit -m "init" && git branch -D main && git branch -M main && git push --force origin main

    git checkout -f dev && git log --oneline origin/main origin/dev

## Releasing again later

Commit on `dev` and push it. Then take the release files from `dev` onto `main`:

    cd ~/Library/CloudStorage/OneDrive-ETHZurich/HS26/ML4Genomics/ML4Genomics-Presentation-AF2 && git remote get-url origin
    git checkout main && git checkout dev -- main.tex main.pdf boxes.tex tools/measure_boxes.py literature README.md .gitignore && git commit -m "<what changed>" && git push origin main && git checkout dev

Switching to `main` removes the dev-only files (script, screenplay, `_DEV/`) from the folder; switching back restores them. The ignored folders `to_overleaf/` and `from_overleaf/` stay.
