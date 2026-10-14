# Work split

Talk on Jumper et al. 2021 (AlphaFold 2), 25 minutes plus 10 minutes of questions (see `README.md`). Agreed in chat on 12 October 2026.

## Who does what

| | Evita Bosch Pokunevich | Ben Bullinger |
|---|---|---|
| Part | First half | Second half |
| Content | The problem, the data, the key elements of the network | The network in detail, the training, the analysis of the network, the ablation study |
| Paper sections | Introduction and CASP14 results, The AlphaFold network, Evoformer, End-to-end structure prediction up to FAPE | Training with labelled and unlabelled data, Interpreting the neural network, MSA depth and cross-chain contacts, Related work, Discussion |
| Slides (numbering of 14 October) | 1 to 11 or 12 (see open points) | 12 or 13 to 19 |
| Speaking time in part 1 | about 12.5 minutes | about 12.5 minutes |
| Part 2 | exam question and audience questions: to be split | |

Each of us

- studies their half of the paper and the matching parts of the Supplementary Information,
- edits the slides of their half and adds slides to it where needed,
- writes the script for their half.

## Slides on 14 October, after the revision

The deck follows four facts about proteins, each answered by one design choice (slide 6). The architecture slides repeat the fact they answer as a grey subtitle. The ablation slide and the summary come back to the four.

| Slide | Title | Section | Speaker |
|---|---|---|---|
| 1 | Outline | | Evita |
| 2 | Sequence in, structure out | The problem | Evita |
| 3 | CASP14: atomic accuracy, alone | The benchmark | Evita |
| 4 | Predictions on top of experiment | The benchmark | Evita |
| 5 | One pipeline, end to end | The network | Evita |
| 6 | Four facts about proteins, four design choices | The network | Evita, drafted by Ben |
| 7 | Input: a multiple sequence alignment (MSA) | The data | Evita |
| 8 | Evoformer block, fact 1 | The network, in detail | Evita |
| 9 | Pairs updated through triangles, fact 2 | The network, in detail | Evita |
| 10 | Structure module: residues as rigid bodies, fact 3 | The network, in detail | Evita |
| 11 | Invariant point attention, fact 3 | The network, in detail | Evita |
| 12 | FAPE: a loss over local frames, fact 4 | The network, in detail | open |
| 13 | Trained beyond the PDB | Training | Ben |
| 14 | Which pieces earn their accuracy, the four facts checked | What makes it work | Ben |
| 15 | The structure forms inside the trunk | What makes it work | Ben |
| 16 | The model knows when it is right | What makes it work | Ben |
| 17 | Where it still fails | What makes it work | Ben |
| 18 | What followed | Conclusion | Ben |
| 19 | Summary, the four facts with their ablation cost | Conclusion | Ben |
| 20 | Exam question | Questions | open |
| 21 | Questions for the audience | Questions | open |
| backup 1 to 4 | Why is the attention invariant. Why is the structure module equivariant. Where does the handedness come from. What does FAPE measure. | geometry, one question per slide | Evita 1 and 2, Ben 3 and 4 |
| backup 5, 6 | Is AlphaFold 2 a graph neural network. What does each block compute. | | both |
| backup 7 to 9 | What exactly did each ablation remove. How does the network predict its own accuracy. How was it trained. | | Ben |
| backup 10 | MSA row attention with pair bias, Suppl. Fig. 2 | | Evita, moved from the main deck on 14 October |

Changed on Evita's slides on 14 October, each a one-line change: slide 2 explains backbone and side chain in one clause and names PDB 6Y4F, slides 8 to 12 carry the fact as a subtitle, slide 8 names attention along rows and columns, slide 6 is new, her Suppl. Fig. 2 slide moved to the backup. `git diff` shows all of it.

## Dates

See the schedule in `README.md`. End of the week of 12 October: dry run of the full talk together.

## Open points

- **Slide 11 or 12.** Evita wrote "slides up until 11 included". Slide 11 was FAPE then. Her edit of 13 October moved FAPE into "The network, in detail", so she probably means up to and including FAPE (now slide 12). To confirm with her.
- **Script.** `SCRIPT.md` and `SCREENPLAY.txt` still plan the handover after slide 9 of the old numbering, with the labels FIRST SPEAKER and SECOND SPEAKER. Update them once the handover slide is fixed.
- **Day and time of the dry run.**
