# Work split

Talk on Jumper et al. 2021 (AlphaFold 2), 25 minutes plus 10 minutes of questions (see `README.md` in this folder). Agreed in chat on 12 October 2026, handover moved to after the triangle slide on 16 October.

## Who does what

| | Evita Bosch Pokunevich | Ben Bullinger |
|---|---|---|
| Part | Slides 1 to 9 | Slides 10 to 20 |
| Content | The problem, the benchmark, the pipeline, the four properties, the alignment, the two representations, the Evoformer block, the row attention, the triangles | The structure module, IPA, FAPE, training, ablations, intermediate structures, confidence, limitations, what followed, AlphaFold 3, summary |
| Paper sections | Introduction and CASP14 results, The AlphaFold network, Evoformer | End-to-end structure prediction, Training with labelled and unlabelled data, Interpreting the neural network, MSA depth and cross-chain contacts, Related work, Discussion |
| Speaking time | about 12.5 minutes | about 12.5 minutes |
| Part 2 | exam question and audience questions, shared | |

Each of us studies their half of the paper and the matching parts of the Supplementary Information, and writes the script for their half.

## Slides on 16 October

The deck follows four properties of the problem, each answered by one design choice (slide 5). The architecture slides repeat their property as a grey subtitle, the ablation slide and the summary come back to the four.

| Slide | Title | Speaker |
|---|---|---|
| 1 | The problem: sequence to structure | Evita |
| 2 | The benchmark: CASP14 | Evita |
| 3 | Confidence: pLDDT against measured lDDT (Fig. 2c) | Evita |
| 4 | The network: inputs, Evoformer, structure module (Fig. 1e) | Evita |
| 5 | The design: four constraints built into the network | Evita |
| 6 | The input: the multiple sequence alignment | Evita |
| 7 | The representations: MSA array and pair array | Evita |
| 8 | Evoformer: one block (Fig. 3a) | Evita |
| 9 | Evoformer: row attention with pair bias (Suppl. Fig. 2) | Evita |
| 10 | Evoformer: triangle updates (Fig. 3c) | Evita |
| 11 | Structure module: residues as rigid bodies (Fig. 3d) | Ben |
| 12 | Structure module: invariant point attention (IPA) (Suppl. Fig. 8) | Ben |
| 13 | The loss: frame aligned point error (FAPE) (Fig. 3f) | Ben |
| 14 | Training: self-distillation, masked MSA, total loss | Ben |
| 15 | Ablations: the cost of each component (Fig. 4a and Suppl. Fig. 9, labels re-set) | Ben |
| 16 | Interpretation: intermediate structures in the Evoformer (Fig. 4b) | Ben |
| 17 | Limitations: MSA depth and complexes (Fig. 5a) | Ben |
| 18 | After AlphaFold 2: 2021 to 2025 | Ben |
| 19 | AlphaFold 3: the four constraints revisited (AF3 Fig. 1d) | Ben |
| 20 | Summary: the four constraints and their cost | Ben |
| 21 | Exam question (placeholder until the question arrives) | shared |
| 22 | Questions for the audience, in order of difficulty | shared |
| 23, 24 | References | |

Order rule (Ben, 16 October): the talk runs forward in time, no term is used before the slide that defines it, checked by a script over `main.tex` that lists the first slide of every technical term. The confidence slide stays at the front (Ben and Evita's decision) and defines lDDT and pLDDT itself; the properties slide no longer points forward to the ablations. Text rule: a figure, at most two short lines and one key line per slide.

Backups, five since 16 October (Ben: "you can have 5 backup slides and that is it"): 1 IPA: invariance and equivariance (SI eqs. 3 to 6), 2 Chirality: where the handedness comes from (SI 1.9.3), 3 Generalisation: recent PDB structures (Fig. 2a and 2b), 4 AlphaFold 3: the reported failures (Fig. 5b and 5e, the wrong-handed ligand and the overlapping chains). Suppl. Fig. 9 moved onto the ablation slide on 17 October, the AlphaFold 3 architecture figure moved onto slide 19 on 19 October. Backups 1 to 3 belong to Ben's half, 4 to the AlphaFold 3 slide. Evita's half needs none, the Evoformer figures are on the main slides.

## Changes on 16 October

Ben's pass over the whole deck after the review in `reviews/REVIEW-2026-10-16.md`. On Evita's slides: slide 5 was rewritten so that property 1 is the evolutionary fact and the MSA is the design answer (agreed with Evita on 16 October); slide 9 shows Fig. 3a with the three red callouts and names the algorithms of the block; slide 10 is new, Supplementary Fig. 2 with Algorithm 7 beside it; slide 11 shows Algorithms 11 and 13 beside Fig. 3c; all key lines were rewritten as short sentences without colons; the pipeline slide got its callouts back; every footer names the figure and the paper.

Evening of 16 October, after Ben and Evita found the own drawings on the IPA and FAPE slides unreadable ("we could not relate them to the architecture layer directly"): slides 9 to 14 now present the architecture at the level of the Supplementary Information. Each shows the paper's or the supplement's own figure of the layer with red callouts that carry the line numbers of the algorithm, and the algorithm's equations or a line-by-line walk beside it. The own drawings are gone from the main deck. The derivations stay in backups 1 to 4.

## Open points

- Day and time of the dry run.
- The exam question (arrives about seven days before the talk).


Title rule (Ben, 17 October, "make everything consistent in style and professional"): every title is "Part: content", a noun phrase that names what is on the slide, no slogans, no paired phrases, acronyms in parentheses at first use (IPA, FAPE). The four properties are called constraints, the paper's word (p. 584). Backups follow the same pattern instead of questions.

Script (17 October): `SCRIPT.tex` was rewritten for the current deck, slide by slide, with the source of every statement and the answers we prepared for questions. `SCREENPLAY.txt` is generated from it (`python3 -I tools/make_screenplay.py`), which also recomputes the timing table at 140 words per minute: Evita ends at about 12 minutes, Ben at about 24 and a half. Each of us rehearses their half from the screenplay and tells the other where the wording does not fit their way of speaking.

Term rule (Ben, 17 October, "terms are either technical standard in the lecture, or defined"): a term may appear on a slide without definition only if Lecture 5 of the course (`Lecture5_Folding.pdf`) uses it: contact and contact map (defined there with the 8 Å Cβ rule), multiple sequence alignment (MSA) of homologous proteins, co-evolution and co-mutation, residue, secondary structure (helix, strand, coil), backbone torsion angles, Å, PDB and the experimental methods, template-free prediction, query, key, value, softmax, heads, gating, CNN, 3D coordinates. Everything else is defined in the sentence where it first appears (residue and side chain, CASP14 and domain, lDDT and pLDDT, frame, IPA, FAPE, chirality, ablation, GDT, N_eff, distogram, ligand) or is replaced by a plain phrase (heavy atom, clash). "Family" became "homologous proteins", the lecture's word. The alignment's first row is called the input sequence, not the query, because the lecture uses query for attention.
