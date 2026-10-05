# Background for the AlphaFold 2 presentation

Downloaded on 2026-10-04. Each file was opened and its title page checked against the citation below.

`SLIDE-CHECK.md` in this folder gives the source of every statement on the slides and lists the questions to expect. `SCRIPT.md` in the repo root has the speaker notes and the timing.

Two limits decide what is in the repo:

- **Size.** Overleaf recommends "less than 100 MB if using GitHub sync" (https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits). The repo is at 108 MB since `AF1.pdf` and `AF3.pdf` were added to the root on 2026-10-05, which is over the recommendation. Removing one of the two copies of the AlphaFold 3 paper saves 8.6 MB. Overleaf's hard limits are 50 MB per file and 7 MB of editable text; the largest file here has 21 MB and the text files have 0.2 MB.
- **Licences.** The repository is private. Before it is made public, remove the files that print no open licence: the two Nobel documents, the AlphaFold 1 manuscript, the CASP14 manuscript, the three papers in `4-cited-methods`, and `Petar-EEML.pdf` in the root.

Seven files are therefore not in the repo. They are listed at the end.

## In the repo root

| File | What it is |
|---|---|
| `_AF2.pdf` | Jumper et al., "Highly accurate protein structure prediction with AlphaFold", Nature 596, 583–589 (2021). The slides cut their figures from it. |
| `AF1.pdf` | Senior et al., "Improved protein structure prediction using potentials from deep learning", Nature 577, 706–710 (2020), the published version. The earlier system: a network predicts distance distributions, then a potential built from them is minimized by gradient descent. The authors' submitted manuscript is also in `1-context`. |
| `AF3.pdf` | Abramson et al., "Accurate structure prediction of biomolecular interactions with AlphaFold 3", Nature 630, 493–500 (2024). The same file as `3-after/Abramson2024-AlphaFold3.pdf`. |
| `_AF2-SI.pdf` | Its Supplementary Information, 62 pages: Supplementary Methods 1.1–1.17, Algorithms 1–32, Supplementary Figures 1–15, Tables 1–6. This is the full specification of the method. PDF page = printed page + 1. |

## 1-context: what the paper builds on

| File | What it is | Why it is here |
|---|---|---|
| `Nobel2024-scientific-background.pdf` | Nobel Committee for Chemistry, scientific background to the 2024 prize (17 pages). | A short overview of the history up to AlphaFold 2. Read this first for the biology. |
| `Anfinsen1972-Nobel-lecture.pdf` | Anfinsen's Nobel lecture on protein folding. | Slide 2 cites Anfinsen 1973 (Science), which I could not download. This lecture is on the same subject. |
| `Marks2011-coevolution.pdf` | Marks et al., PLoS ONE 6, e28766 (2011). Reference 23 of the paper. | Cited on slide 5. Shows that couplings between positions, inferred from an alignment alone, predict which residues are close in 3D. |
| `Senior2020-AlphaFold1-submitted-version.pdf` | AlphaFold 1, Nature 577, 706–710 (2020), the authors' submitted manuscript from UCL Discovery. Reference 10. | The earlier system: predicts distance distributions, then minimizes a potential by gradient descent. |
| `Yang2019-trRosetta-preprint.pdf` | bioRxiv preprint of Yang et al., PNAS 117, 1496–1503 (2020). Reference 44. | A method that predicts distances from alignment statistics and then builds coordinates. The SI names it as the example for such inputs (SI 1.13.1). |
| `Kryshtafovych2021-CASP14-overview-accepted-version.pdf` | The CASP organizers' report on CASP14, Proteins (2021), accepted manuscript from the University of Basel's repository. | Explains CASP and gives the organizers' verdict on AlphaFold 2. |
| `Mariani2013-lDDT.pdf` | Mariani et al., Bioinformatics 29, 2722–2728 (2013). Reference 34. | Defines lDDT, the score that the confidence output pLDDT predicts. Its introduction also defines GDT. |

## 2-same-team: two further papers by the AlphaFold authors

| File | What it is | Why it is here |
|---|---|---|
| `Tunyasuvunakool2021-human-proteome.pdf` | Companion paper, Nature (2021). Reference 39. | AlphaFold applied to 98.5% of human proteins. Has the evidence on pLDDT that slide 15 cites. Named on slide 17. |
| `Jumper2021-AF2-at-CASP14.pdf` | "Applying and improving AlphaFold at CASP14", Proteins (2021). | How the system was run during CASP14, including the manual interventions and the story of ORF8. |

## 3-after: what came at the same time and later

| File | What it is | Why it is here |
|---|---|---|
| `Baek2021-RoseTTAFold.pdf` | Baek et al., Science 373, 871–876 (2021), author manuscript from eScholarship. | The academic method first published online on the same day as AlphaFold 2. Named on slide 17. |
| `Lin2022-ESMFold-preprint.pdf` | bioRxiv version of Lin et al., Science (2023). | Structure from one sequence with a protein language model in place of the MSA. Named on slide 17. |
| `Abramson2024-AlphaFold3.pdf`, `-SI.pdf`, `-addendum.pdf` | Abramson et al., Nature 630 (2024), with supplement and code-release addendum. | Named on slide 17. Predicts structures without the frames and the equivariance that slides 9 to 11 present. |
| `Terwilliger2024-predictions-vs-experiment.pdf` | Terwilliger et al., Nature Methods (2024). | Compares predictions with experimental maps. For questions on what predictions cannot replace. |

## 4-cited-methods: methods the paper borrows

| File | What it is |
|---|---|
| `Xie2020-noisy-student.pdf` | Reference 35, cited on slide 12 (self-distillation). |
| `Devlin2019-BERT.pdf` | Reference 37, cited on slide 12 (masked prediction). |
| `Rao2021-MSA-Transformer.pdf` | Reference 38. Pre-trains attention over alignments. AlphaFold 2 trains its masked-MSA loss jointly instead. |

## Downloaded but not in the repo

Ben has these in `HS26/ML4Genomics/AF2-not-in-repo/`, next to the repo. Everyone else can get them from the links.

| File | What it is | Why it is not in the repo | Link |
|---|---|---|---|
| `video1-T1024-LmrP.mp4` to `video4-T1091.mp4` | Supplementary Videos 1–4: the predicted structure after each of the 192 block evaluations (4 passes × 48 Evoformer blocks). Video 3 is ORF8, the hard target on slide 14. Video 2 is the 2,180-residue chain on slide 4. | Size: 22 MB together. | https://doi.org/10.1038/s41586-021-03819-2, section "Supplementary information" |
| `Ahdritz2023-OpenFold-preprint.pdf` | bioRxiv version of Ahdritz et al., Nature Methods (2024). A trainable reimplementation of AlphaFold 2 and what retraining it shows. | Size: 14 MB. | https://doi.org/10.1101/2022.11.20.517210 |
| `Evans2021-AlphaFold-Multimer-preprint.pdf` | AlphaFold 2 retrained for complexes, bioRxiv version of 10 March 2022. Named on slide 17. | Marked "All rights reserved. No reuse allowed without permission." | https://doi.org/10.1101/2021.10.04.463034 |
| `Jumper2021-AF2-reporting-summary.pdf` | Nature's reporting form. | Not needed. It is also pages 11–12 of `_AF2.pdf`. | same page as the videos |

## Not downloaded

These sites block scripted downloads or need the ETH subscription. Open them in a browser on the ETH network. The DOIs are from Europe PMC.

- Anfinsen 1973, Science 181, 223–230: https://doi.org/10.1126/science.181.4096.223
- Zemla 2003, the original definition of GDT (reference 33): https://doi.org/10.1093/nar/gkg571
- Zhang and Skolnick 2004, the TM-score (reference 27): https://doi.org/10.1002/prot.20264 (the formula is also in `_AF2-SI.pdf`, section 1.9.7)
- Pereira et al. 2021, "High-accuracy protein structure prediction in CASP14" (reference 57): https://doi.org/10.1002/prot.26171
- Published versions of files that are here as preprint or manuscript: AlphaFold 1 https://doi.org/10.1038/s41586-019-1923-7, trRosetta https://doi.org/10.1073/pnas.1914677117, CASP14 overview https://doi.org/10.1002/prot.26237, RoseTTAFold https://doi.org/10.1126/science.abj8754, ESMFold https://doi.org/10.1126/science.ade2574, OpenFold https://doi.org/10.1038/s41592-024-02272-z. For AlphaFold-Multimer I found only the preprint.

Code, not downloaded: https://github.com/deepmind/alphafold (from the paper's "Code availability"). The algorithms in `_AF2-SI.pdf` are the better source for the talk.
