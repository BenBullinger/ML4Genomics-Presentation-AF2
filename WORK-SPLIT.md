# Work split

Talk on Jumper et al. 2021 (AlphaFold 2), 25 minutes plus 10 minutes of questions (see `README.md`). Agreed in chat on 12 October 2026.

## Who does what

| | Evita Bosch Pokunevich | Ben Bullinger |
|---|---|---|
| Part | First half | Second half |
| Content | The problem, the data, the key elements of the network | The network in detail, the training, the analysis of the network, the ablation study |
| Paper sections | Introduction and CASP14 results, The AlphaFold network, Evoformer, End-to-end structure prediction up to FAPE | Training with labelled and unlabelled data, Interpreting the neural network, MSA depth and cross-chain contacts, Related work, Discussion |
| Slides (numbering of 14 October) | 1 to 12 or 13 (see open points) | 13 or 14 to 20 |
| Speaking time in part 1 | about 12.5 minutes | about 12.5 minutes |
| Part 2 | exam question and audience questions: to be split | |

Each of us

- studies their half of the paper and the matching parts of the Supplementary Information,
- edits the slides of their half and adds slides to it where needed,
- writes the script for their half.

## Slides on 14 October

| Slide | Title | Section | Speaker |
|---|---|---|---|
| 1 | Outline | | Evita |
| 2 | Sequence in, structure out | The problem | Evita |
| 3 | CASP14: atomic accuracy, alone | The benchmark | Evita |
| 4 | Predictions on top of experiment | The benchmark | Evita |
| 5 | One pipeline, end to end | The network | Evita |
| 6 | One pipeline, end to end (Supplementary Fig. 2) | The network | Evita |
| 7 | AlphaFold 2 is message passing on a geometric graph | The network | draft by Ben, 14 October |
| 8 | Input: a multiple sequence alignment (MSA) | The data | Evita |
| 9 | Evoformer block | The network, in detail | Evita |
| 10 | Pairs updated through triangles | The network, in detail | Evita |
| 11 | Structure module: residues as rigid bodies | The network, in detail | Evita |
| 12 | Invariant point attention | The network, in detail | Evita |
| 13 | FAPE: a loss over local frames | The network, in detail | open |
| 14 | Trained beyond the PDB | Training | Ben |
| 15 | Which pieces earn their accuracy | What makes it work | Ben |
| 16 | The structure forms inside the trunk | What makes it work | Ben |
| 17 | The model knows when it is right | What makes it work | Ben |
| 18 | Where it still fails | What makes it work | Ben |
| 19 | What followed | Conclusion | Ben |
| 20 | Summary | Conclusion | Ben |
| 21 | Exam question | Questions | open |
| 22 | Questions for the audience | Questions | open |
| backup | Backup | after `\appendix` | both |

Slides 21, 22 and the first backup slide are placeholders, added 13 October from the guidelines. The second backup slide lists the whole network as residual updates.

## Dates

See the schedule in `README.md`. End of the week of 12 October: dry run of the full talk together.

## Open points

- **Slide 12 or 13.** Evita wrote "slides up until 11 included". The deck had two slides fewer then, and slide 11 was FAPE. Her edit of 13 October moved FAPE into "The network, in detail", so she probably means up to and including FAPE (now slide 13). To confirm with her.
- **Script.** `SCRIPT.md` and `SCREENPLAY.txt` still plan the handover after slide 9 of the old numbering, with the labels FIRST SPEAKER and SECOND SPEAKER. Update them once the handover slide is fixed.
- **Day and time of the dry run.**
