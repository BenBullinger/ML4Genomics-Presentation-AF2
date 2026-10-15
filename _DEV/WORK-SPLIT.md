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

## Slides after Review Streamlining (15 October 2026)

The main deck was streamlined to 20 talk slides (~1:15 per slide for a comfortable 25:00 min presentation). Redundant CASP14 panels and SI screenshots were folded into the trunk or moved to backups. The AF3 choices and costs are unified into a single comparative verdict slide.

The handover occurs after Slide 9 (Triangle updates), giving an exact 10 / 11 slide balance:
- **Evita (first half, ~12.5 min)**: Problem, CASP14 benchmark, macro pipeline, two representations, Evoformer trunk through Triangle updates.
- **Ben (second half, ~12.5 min)**: Structure module, IPA, FAPE, training, ablations, intermediate structures, confidence, limitations, timeline, AF3 verdict, and summary.

| Slide | Title | Section | Speaker |
|---|---|---|---|
| 1 | Outline | | Evita |
| 2 | The problem: sequence to structure | The problem | Evita |
| 3 | The benchmark: CASP14 | The benchmark | Evita |
| 4 | The pipeline: MSA in, coordinates out | The network | Evita |
| 5 | Four properties, four design choices | The network | Evita |
| 6 | The two representations | The network | Evita |
| 7 | The input: MSA representation | The network | Evita |
| 8 | The input: Pair representation | The network | Evita |
| 9 | The Evoformer block | The network | Evita |
| 10 | Evoformer: triangle updates | The network | Evita |
| 11 | Structure module: residues as rigid bodies | The network | Ben |
| 12 | Invariant point attention (IPA) | The network | Ben |
| 13 | Frame aligned point error (FAPE) | The network | Ben |
| 14 | Training data: PDB and self-distillation | Training | Ben |
| 15 | Ablations: the cost of each component | What makes it work | Ben |
| 16 | Intermediate structures in the trunk | What makes it work | Ben |
| 17 | Confidence: pLDDT against measured lDDT | What makes it work | Ben |
| 18 | Limitations: MSA depth and complexes | What makes it work | Ben |
| 19 | After AlphaFold 2: 2021 to 2025 | Conclusion | Ben |
| 20 | AlphaFold 3: which choices survived | Conclusion | Ben |
| 21 | Summary: four design choices, measured | Conclusion | Ben |
| 22 | Exam question | Questions | shared |
| 23 | Questions for the audience | Questions | shared |

| Backups | Topic |
|---|---|
| backup 1 to 4 | Why is IPA invariant. Why is structure module equivariant. Where does handedness come from. What does FAPE measure. |
| backup 5, 6 | Is AlphaFold 2 a GNN. What does each block compute. |
| backup 7 to 9 | What each ablation removed. How is confidence predicted. How was it trained. |
| backup 10, 14 | AlphaFold 3: further changes, and AF3 architecture diagram (Fig.~1d). |
| backup 11, 13 | MSA row attention with pair bias (Suppl.~Fig.~2) and outer product mean (Suppl.~Fig.~3). |
| backup 12 | Prediction and experiment superposed (CASP14 3-panel). |

Changed on Evita's slides on 14 October, each a one-line change: slide 2 explains backbone and side chain in one clause and names PDB 6Y4F, slides 8 to 12 carry the fact as a subtitle, slide 8 names attention along rows and columns, slide 6 is new, her Suppl. Fig. 2 slide moved to the backup. `git diff` shows all of it.

## Dates

See the schedule in `README.md`. End of the week of 12 October: dry run of the full talk together.

## Open points

- **Slide 11 or 12.** Evita wrote "slides up until 11 included". Slide 11 was FAPE then. Her edit of 13 October moved FAPE into "The network, in detail", so she probably means up to and including FAPE (now slide 12). To confirm with her.
- **Script.** `SCRIPT.md` and `SCREENPLAY.txt` still plan the handover after slide 9 of the old numbering, with the labels FIRST SPEAKER and SECOND SPEAKER. Update them once the handover slide is fixed.
- **Day and time of the dry run.**
