# Work split

Talk on Jumper et al. 2021 (AlphaFold 2), 25 minutes plus 10 minutes of questions (see `README.md`). Agreed in chat on 12 October 2026.

## Who does what

| | Evita Bosch Pokunevich | Ben Bullinger |
|---|---|---|
| Part | First half | Second half |
| Content | The problem, the data, the key elements of the network | The network in detail, the training, the analysis of the network, the ablation study |
| Paper sections | Introduction and CASP14 results, The AlphaFold network, Evoformer, End-to-end structure prediction up to FAPE | Training with labelled and unlabelled data, Interpreting the neural network, MSA depth and cross-chain contacts, Related work, Discussion |
| Slides (numbering of 13 October) | 1 to 11 or 12 (see open points) | 12 or 13 to 19 |
| Speaking time in part 1 | about 12.5 minutes | about 12.5 minutes |
| Part 2 | exam question and audience questions: to be split | |

Each of us

- studies their half of the paper and the matching parts of the Supplementary Information,
- edits the slides of their half and adds slides to it where needed,
- writes the script for their half.

## Slides on 13 October

| Slide | Title | Section | Speaker |
|---|---|---|---|
| 1 | Outline | | Evita |
| 2 | Sequence in, structure out | The problem | Evita |
| 3 | CASP14: atomic accuracy, alone | The benchmark | Evita |
| 4 | Predictions on top of experiment | The benchmark | Evita |
| 5 | One pipeline, end to end | The network | Evita |
| 6 | One pipeline, end to end (Supplementary Fig. 2) | The network | Evita |
| 7 | The input: a multiple sequence alignment (MSA) | The data | Evita |
| 8 | The Evoformer block | The network, in detail | Evita |
| 9 | Pairs updated through triangles | The network, in detail | Evita |
| 10 | The structure module: residues as rigid bodies | The network, in detail | Evita |
| 11 | Invariant point attention | The network, in detail | Evita |
| 12 | FAPE: a loss over local frames | The network, in detail | open |
| 13 | Trained beyond the PDB | Training | Ben |
| 14 | Which pieces earn their accuracy | What makes it work | Ben |
| 15 | The structure forms inside the trunk | What makes it work | Ben |
| 16 | The model knows when it is right | What makes it work | Ben |
| 17 | Where it still fails | What makes it work | Ben |
| 18 | What followed | Conclusion | Ben |
| 19 | Summary | Conclusion | Ben |
| 20 | Exam question | Questions | open |
| 21 | Questions for the audience | Questions | open |
| backup | Backup | after `\appendix` | both |

Slides 20, 21 and the backup slide are placeholders, added 13 October from the guidelines.

## Dates

See the schedule in `README.md`. End of the week of 12 October: dry run of the full talk together.

## Open points

- **Slide 11 or 12.** Evita wrote "slides up until 11 included". The deck had one slide fewer then, and slide 11 was FAPE. Her edit of 13 October moved FAPE into "The network, in detail", so she probably means up to and including FAPE (now slide 12). To confirm with her.
- **Script.** `SCRIPT.md` and `SCREENPLAY.txt` still plan the handover after slide 9 of the old numbering, with the labels FIRST SPEAKER and SECOND SPEAKER. Update them once the handover slide is fixed.
- **Day and time of the dry run.**
