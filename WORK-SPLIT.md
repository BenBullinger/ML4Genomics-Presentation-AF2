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
| 2 | The problem: sequence to structure | The problem | Evita |
| 3 | The benchmark: CASP14 | The benchmark | Evita |
| 4 | Prediction and experiment superposed | The benchmark | Evita |
| 5 | The pipeline: MSA in, coordinates out | The network | Evita |
| 6 | Four properties, four design choices | The network | Evita |
| 7 | The two representations | The network | Evita, drafted by Ben on 14 October |
| 8 | The input: MSA representation | The network | Evita |
| 9 | The input: Pair representation | The network | Evita, drafted by Ben on 14 October |
| 10 | The Evoformer block | The network | Evita |
| 11 | Evoformer: row attention with pair bias | The network | Evita, drafted by Ben on 14 October |
| 12 | Evoformer: columns and outer product mean | The network | Evita, drafted by Ben on 14 October |
| 13 | Evoformer: triangle updates | The network | Evita |
| 14 | Structure module: residues as rigid bodies | The network | Evita |
| 15 | Invariant point attention | The network | Evita |
| 16 | Frame aligned point error (FAPE) | The network | open |
| 17 | Training data: PDB and self-distillation | Training | Ben |
| 18 | Ablations: the cost of each component | What makes it work | Ben |
| 19 | Intermediate structures in the trunk | What makes it work | Ben |
| 20 | Confidence: pLDDT against measured lDDT | What makes it work | Ben |
| 21 | Limitations: MSA depth and complexes | What makes it work | Ben |
| 22 | After AlphaFold 2: 2021 to 2025 | Conclusion | Ben |
| 23 | AlphaFold 3: which choices survived | Conclusion | Ben |
| 24 | The AlphaFold 3 architecture | Conclusion | Ben |
| 25 | AlphaFold 3: the cost of the removal | Conclusion | Ben |
| 26 | Summary: four design choices, measured | Conclusion | Ben |
| 27 | Exam question | Questions | open |
| 28 | Questions for the audience | Questions | open |

| backup 1 to 4 | Why is IPA invariant to rigid motions. Why is the structure module equivariant. Where does the handedness come from. What does FAPE measure. | geometry, one question per slide | Evita 1 and 2, Ben 3 and 4 |
| backup 5, 6 | Is AlphaFold 2 a graph neural network. What does each block compute. | | both |
| backup 7 to 9 | What exactly did each ablation remove. How is confidence predicted. How was it trained. | | Ben |
| backup 10 | AlphaFold 3: further changes | | Ben |
| backup 11 | MSA row attention with pair bias, Suppl. Fig. 2 | | Evita, moved from the main deck on 14 October |

Changed on Evita's slides on 14 October, each a one-line change: slide 2 explains backbone and side chain in one clause and names PDB 6Y4F, slides 8 to 12 carry the fact as a subtitle, slide 8 names attention along rows and columns, slide 6 is new, her Suppl. Fig. 2 slide moved to the backup. `git diff` shows all of it.

## Dates

See the schedule in `README.md`. End of the week of 12 October: dry run of the full talk together.

## Open points

- **Slide 11 or 12.** Evita wrote "slides up until 11 included". Slide 11 was FAPE then. Her edit of 13 October moved FAPE into "The network, in detail", so she probably means up to and including FAPE (now slide 12). To confirm with her.
- **Script.** `SCRIPT.md` and `SCREENPLAY.txt` still plan the handover after slide 9 of the old numbering, with the labels FIRST SPEAKER and SECOND SPEAKER. Update them once the handover slide is fixed.
- **Day and time of the dry run.**
