Back-row review of the AlphaFold 2 slides
Reviewer role: MSc student, biology background, one introductory ML course, has not read the paper.
Seen: small renderings first (378 px), then the large ones. Backups seen last.
Severity: high = I lose the thread or the slide is broken. medium = I need the speaker to rescue me. low = a polish.

General findings

[high] Three slides are carried by paper figures whose text is unreadable from the back: slides 11, 12 and 24. Only the red overlay labels survive. Fix: keep the overlay labels, drop the figures' inner text or redraw with three to five boxes.
[medium] Every footnote is unreadable from the back. Three blue sentences depend on a footnote: slide 3 (what was measured), slide 18 (what GDT and lDDT are), slide 23 (what the bitter lesson is). Fix: move those three definitions into the body text, keep the citations in the footnotes.
[medium] Several ML words arrive before they are explained and are never explained: attention (slide 6), ablations (6), frame (6, explained on 14), logits (11), inductive bias (13), head (18), trunk (19), equivariance (23), diffusion (23), tokens (24), seeds (25). A biology student with one ML course knows softmax, loss, gradient and perceptron. Fix: a four-word gloss at first use, listed per slide below.
[medium] The numbers in the bar chart of slide 18 are misread from the back. From the small image I read four of ten numbers wrongly. Fix: see slide 18.
[low] "The hand" is used as a metaphor for handedness on slides 23, 25 and 28. I understood it only on 25. Fix: write "handedness (chirality)" once, then "the hand" is fine.

Per-slide notes

Slide 1: Outline
Understood: the talk goes problem, benchmark, network (data, then detail), training, what makes it work, conclusion, questions.
Could not read: nothing.
Used before explained: nothing.
Blue sentence: none.
Problems: [low] The thread of the talk is the four design choices (slide 6 and the discs). The outline does not mention it. Fix: "5. What makes it work: four design choices, measured".

Slide 2: The problem, sequence to structure
Understood: the amino-acid sequence is known for billions of proteins, the 3D structure takes months to years of experiment, and predicting one from the other has been open for 50 years.
Could not read: the footnote (T1049, PDB 6Y4F). The N and C terminus labels on the picture.
Used before explained: "heavy atoms" (I guessed: all atoms but hydrogen). "CASP14" appears in the footnote one slide before it is defined.
Blue sentence: clear. It means people have tried to predict the fold from the sequence since the 1960s.
Problems: [low] "heavy atoms". Fix: "all atoms but hydrogen". [low] The picture is the same as the first panel of slide 4, so slide 4 first looked like a repeat. Fix: use a different view here, or say "the same protein, closer" on slide 4.

Slide 3: The benchmark, CASP14
Understood: CASP14 was a blind contest in 2020. Predictions are submitted before the experimental structures are released, and the error is a distance in angstrom.
Could not read: the footnote "Cα r.m.s.d.95 on 87 domains, with 95% confidence intervals".
Used before explained: "r.m.s.d.95" (footnote, never explained). "backbone" is fine for me.
Blue sentence: clear as words. It means the typical error of the predicted chain is smaller than one atom. But nothing on the slide backs it: no number, no figure.
Problems: [high] The bold line "Show the average prediction hist from the paper" is a to-do note left on the slide, and the footnote "Redrawn from Fig. 1a" describes a figure that is not there. Fix: insert the Fig. 1a bar chart (AlphaFold 0.96 Å, next best 2.8 Å) and delete the note. [medium] The blue claim has no number next to it. Fix: add "median 0.96 Å, a carbon atom is about 1.4 Å wide". [low] The slide is the only text-only slide among the first six. The chart fixes that too.

Slide 4: Prediction and experiment superposed
Understood: the predicted (blue) and experimental (green) structures lie on top of each other, for the backbone, for the side chains, and for a very long chain.
Could not read: the side-chain panel is a blur of sticks from the back. The grey sphere in it is unexplained.
Used before explained: nothing new. "2,180-residue" is fine for a biology student.
Blue sentence: clear.
Problems: [low] The grey sphere. Fix: label it (an ion?) or crop it out.

Slide 5: The pipeline
Understood: the sequence is searched against databases to build an MSA and templates, an Evoformer and a structure module turn them into coordinates, and the whole thing is run four times.
Could not read: all text inside the figure (Input sequence, Genetic database search, MSA representation (s,r,c), Pair representation (r,r,c), Evoformer 48 blocks, Single repr., Structure module 8 blocks, High and Low confidence). Only the five red labels.
Used before explained: "MSA" (expanded in the label, shown only on slide 8). "Templates" (never explained in the talk). "Single repr.", "(s,r,c)", "(r,r,c)" (never explained). "Evoformer" and "Structure module" are names, that is fine.
Blue sentence: half clear. I read it as "the network outputs 3D coordinates directly". Why "itself" matters is not said. I guessed later that earlier methods predicted distances and ran a separate folding step.
Problems: [medium] Figure text illegible. Fix: the five red labels carry the slide, so enlarge the figure to the full width and drop the figure's own small labels, or redraw with five boxes. [medium] "Templates" never explained. Fix: "templates: known structures of related proteins". [low] Blue sentence. Fix: "No separate folding step: the network outputs the coordinates".

Slide 6: Four properties, four design choices
Understood: four facts about proteins and alignments each led to one design decision, and the talk will measure each by removing it.
Could not read: the four icons on the left. From the back I saw lines, a triangle, a smudge and slashes. The large view shows an alignment and a chain, a triangle, two rotated frames, and a mirror.
Used before explained: "attention" (first use). "residue graph". "frame" and "local frames" (explained on slide 14). "ablations" (explained only by the title of slide 18).
Blue sentence: clear. It means each of the four parts matters and the paper measured how much.
Problems: [medium] "frame" and "ablations" are used eight slides before they are explained. Fix: "frame (a local coordinate system per residue, slide 14)" and "The removal experiments (ablations) measure how much". [low] The icons are too small to help. Fix: double their size or drop them. [low] The discs that track these four items start only on slide 10. Fix: show the four empty discs on this slide and say they will follow the four.

Slide 7: The two representations
Understood: the network keeps two tables of numbers, one vector per cell of the alignment and one vector per ordered pair of residues.
Could not read: the subscripts m_si, z_ij, N_seq, N_res. The words query and related sequences were readable.
Used before explained: "query" (slide 8 says "target" for the same thing). "crops" (footnote).
Blue sentence: clear. It means the state of the network is entirely these two arrays.
Problems: [low] "query" here, "target" on slide 8. Fix: one word. [low] The dark cell in the right table is unexplained. Fix: label it "z_ij" or drop it.

Slide 8: The input, MSA representation
Understood: an alignment stacks related sequences column by column, and columns in contact in 3D tend to change together, which the network can read off directly.
Could not read: nothing, the letters are large.
Used before explained: nothing new.
Blue sentence: mostly clear. "themselves" hints at a contrast that is not on the slide. The contrast appears only on slide 18 ("only its statistics").
Problems: [low] Fix: "The network reads the raw alignment, not summary statistics of it".

Slide 9: The input, pair representation
Understood: every ordered pair of residues has a vector that starts from the two amino-acid types and their distance along the chain, picks up template and previous-cycle distances, and at the end yields a distance distribution.
Could not read: the small Fig. 3b (i, j, k, ij, ik, jk labels).
Used before explained: "clipped at 32". "the previous cycle" (recycling was only a label on slide 5). "distogram" is defined in the same sentence, fine.
Blue sentence: clear. It means the geometry lives in the pair table as distances before any coordinates exist.
Problems: [low] Fig. 3b is illegible from the back and slide 13 has a better triangle drawing. Fix: enlarge or drop. [low] "clipped at 32". Fix: "capped at 32 positions".

Slide 10: The Evoformer block
Understood: one block has attention along the rows and columns of the MSA, the MSA writes into the pairs, the pairs are updated by triangle layers and feed back into the MSA, 48 times.
Could not read: every box label of the figure (Row-wise gated self-attention with pair bias, Column-wise gated self-attention, Transition, Outer product mean, the four triangle boxes, 48 blocks no shared weights). Only the red overlays.
Used before explained: "graph inference" (first use, never explained). "Transition" in the figure (slide 12 calls it a two-layer perceptron, the link is not made).
Blue sentence: not clear. "The edges are residues in proximity" reads as if an edge were a residue. I guessed: the pair table is a graph whose edges link residues that are close in space, and the Evoformer infers that graph.
Problems: [medium] Fix the blue sentence: "The pair table is a graph on the residues. Its edges link residues that are close in space." [medium] Figure illegible. Fix: redraw as two rows with five boxes at body-text size, keep the five red labels.

Slide 11: Evoformer, row attention with pair bias
Understood: within one sequence of the alignment, each residue looks at all other residues, and the pair table adds a bias that tells it where to look.
Could not read: the whole figure (Linear, sigmoid, queries, keys, values, gating, softmax, dot-product affinities, the (r_q, r_v, h) shapes). From the back it is a wall of boxes.
Used before explained: "attends". "logits" (I took it as the scores before the softmax). "gating" in the figure.
Blue sentence: half clear. It means the pair values are added to the attention scores, so the pairs decide which residues attend to which.
Problems: [high] The content of the slide is the figure and nothing in it is readable from the back. Fix: a three-box sketch (query row, scores plus pair bias, softmax and weighted sum), or keep only the affinities, plus, pair bias and softmax part, enlarged. [medium] "logits". Fix: "added to the attention scores before the softmax". [low] One sentence on what attention is would carry slides 11 to 15: "attention: a weighted average over residues, the weights come from a softmax over scores".

Slide 12: Evoformer, columns and outer product mean
Understood: at a fixed position the sequences attend to each other, then the outer product of two columns, averaged over the sequences, is added to the pair of those two positions.
Could not read: the whole figure. It is smaller than on slide 11.
Used before explained: "outer product" (I needed a moment). "48 blocks" (the number was only in the illegible figure text of slides 5 and 10).
Blue sentence: clear. It means this is where alignment information enters the pair table, once per block.
Problems: [medium] The figure adds nothing legible. Fix: drop it, draw two columns i and j with an arrow to the cell z_ij. [low] Say "48 blocks" in words on slide 5 or 10.

Slide 13: Evoformer, triangle updates
Understood: the pair ij is updated from the pairs ik and jk through every third residue k, in four variants, because three distances must form a real triangle.
Could not read: the labels and arrows of the four small graphs at the bottom. The big triangle was readable.
Used before explained: "inductive bias" (I have heard it, I am not sure of it). "edge set" is fine.
Blue sentence: half clear. I took it to mean: the update is built around triangles, so the learned distances fit together in 3D, and that built-in assumption helps.
Problems: [medium] Fix the blue sentence: "The update is built around triangles, so the pair table learns distances that fit together in 3D". [low] The four variants are shown but not explained. Fix: one line "two by multiplying the two edges, two by attention over the third node", or drop the four small graphs.

Slide 14: Structure module, residues as rigid bodies
Understood: each residue is a rigid body with its own frame, IPA updates the residues, then all frames move.
Could not read: all figure text (Pair representation, 8 blocks shared weights, IPA module, Single repr., Predict relative rotations and translations, Backbone frames, Predict chi angles). The two drawings on the right (frames, atoms) were readable as pictures.
Used before explained: "Single repr." in the figure, never explained in the talk (backup 6 says it is the first row of the MSA table). "IPA" is defined here, fine. "chi angles" is fine for a biology student.
Blue sentence: not clear at first. I read it as "the residues move independently and nothing keeps the chain bonded". I understood it only after slide 16. The paper calls this a residue gas with a violation loss that encourages bonds.
Problems: [medium] Fix the blue sentence: "Residues move as free rigid bodies. Chain bonds are only encouraged by a violation loss." This also prepares "a violation loss" on slide 25. [medium] The single representation needs one line: "the single representation: the target's row of the MSA table". [low] Figure illegible, the overlays IPA and frames suffice. Fix: crop to the IPA box, the frames box and the arrow between them.

Slide 15: Invariant point attention
Understood: the attention weight between i and j is the usual dot product, plus the pair bias, minus the squared distance between points that i and j place in their own frames, and rotating everything leaves those distances unchanged.
Could not read: the subscripts and the circle operator in the formula. The three underbrace labels and the drawings were readable.
Used before explained: "q, k" (query and key, known if one knows attention). "T_i ∘" as notation (the sentence "Points are placed in the frames" explains it in words). "head" (footnote).
Blue sentence: clear. It means the weights do not change when the whole protein is rotated or moved.
Problems: [low] Add "T_i ∘ x: the point x placed in frame i" under the formula. [low] "usual attention" assumes attention is known. Fix: the one-sentence definition on slide 11.

Slide 16: Frame aligned point error
Understood: the loss looks at every atom i from every frame k, in the prediction and in the experiment, and averages the clamped distance between the two.
Could not read: the subscripts, superscripts and the "true" labels in the formula. The three drawings and the word error were readable.
Used before explained: "clamp" (I guessed: errors above 10 Å count as 10 Å). The inverse frame notation follows from slide 14. "Z" is in the footnote.
Blue sentence: first half clear. Second half not. The slide never says why a mirror image gets a penalty, and a mirror image has all the same distances.
Problems: [medium] Fix: add one line "Frames are right-handed, so a mirrored prediction puts every atom on the wrong side of its frame" (as on backup 3). [low] "clamp". Fix: "errors above 10 Å count as 10 Å".

Slide 17: Training data, PDB and self-distillation
Understood: the network is trained on PDB structures, predicts 350,000 structures for sequences without one, and a new network is trained from scratch on 25% PDB and 75% predicted structures. Some alignment letters are hidden and must be predicted.
Could not read: nothing.
Used before explained: "self-distillation" (explained by the diagram). "masked-MSA loss" (explained by the picture). "BERT" (footnote).
Blue sentence: clear. It means sequences with no experimental structure still teach the model.
Problems: [low] "25%" and "75%" of what. Fix: "of the training samples". [low] The title says data, half the slide is a loss. Fix: "Training: self-distillation and a masked-MSA loss".

Slide 18: Ablations, the cost of each component
Understood: removing each component lowers accuracy, IPA and recycling together cost the most, and the four numbered choices cost 2.2, 4.6 and 2.3 GDT or a mirror image.
Could not read: from the small image I read four of the ten numbers wrongly (I read −0.2, −3.3, −1.5 and shifted rows). The row labels are small. The two panels have different x-scales (−15 to 0 and −3 to 0) and I missed that.
Used before explained: "GDT" and "lDDT-Cα" (axis labels, named in the footnote, what they measure is never said). "head" (distogram head, masked-MSA head). "end-to-end structure gradients". "biasing or gating".
Blue sentence: clear. It means all four choices matter on the benchmark.
Problems: [high] Numbers and labels unreadable from the back. Fix: show only the four numbered rows and the two combined rows, double the font, keep one metric (GDT). [medium] GDT and lDDT need one line of meaning: "GDT: the share of residues placed close to the truth, 0 to 100". [medium] "head". Fix: "an extra output trained alongside". [low] Different x-scales. Fix: say it or use one scale.

Slide 19: Intermediate structures in the trunk
Understood: with a structure module after every Evoformer block, one protein is already solved after a few blocks and another only in the third and fourth pass.
Could not read: nothing important. The names LmrP and ORF8 were readable.
Used before explained: "trunk" (first use, I guessed Evoformer). "frozen" (weights not updated). "run 1 to 4" (I guessed: the four recycling passes).
Blue sentence: clear.
Problems: [medium] "trunk". Fix: "the Evoformer" in the title, or "the trunk (the Evoformer)". [low] "run". Fix: "cycle 1 to 4". [low] Say "two CASP14 proteins" next to the names.

Slide 20: Confidence, pLDDT against measured lDDT
Understood: the model's own per-residue confidence matches the measured accuracy, with slope about one.
Could not read: the tick numbers of the inset. The legend was readable.
Used before explained: "lDDT-Cα" (only named in the footnote of slide 18). "resolved region" (I guessed: the part of the chain seen in the experiment). "r" (correlation).
Blue sentence: half clear. It states a need, not what the plot shows. I read it as "and here it is".
Problems: [medium] Fix: "pLDDT is calibrated: slope one against the measured accuracy". [medium] Question 3 on slide 28 says pLDDT is trained on the model's own errors. That is not on this slide. Fix: add "pLDDT is a prediction of the model's own error, trained on it". [low] "resolved region". Fix: "the part seen in the experiment".

Slide 21: Limitations, MSA depth and complexes
Understood: accuracy drops when the alignment has fewer than about 30 effective sequences, and chains whose shape depends on partners are predicted worse.
Could not read: the dots are faint. The lines and the legend were readable.
Used before explained: "effective sequences (N_eff)". "template coverage".
Blue sentence: clear.
Problems: [medium] Define both legend terms: "N_eff: sequences after removing near-duplicates", "template coverage: the share of the chain covered by a known structure". [low] The title says complexes but nothing on the slide shows it. Fix: drop "complexes" from the title or add the number.

Slide 22: After AlphaFold 2, 2021 to 2025
Understood: a timeline from RoseTTAFold and proteome-scale predictions in 2021 to AlphaFold 3 in 2024, the Nobel Prize, and AlphaGenome in 2025, with three items addressing the limits of AlphaFold 2.
Could not read: the bracket "address the limits" was barely legible.
Used before explained: nothing that matters. "language model", "ligands", "Multimer" are fine.
Blue sentence: clear, but it leaves a cliffhanger. The exception is named only on slide 25.
Problems: [low] Fix: "with one exception, an RNA benchmark", or move the sentence to slide 25. [low] The bracket should say which limit each of the three items addresses.

Slide 23: AlphaFold 3, which choices survived
Understood: AlphaFold 3 kept the triangle updates, shrank the MSA part, and dropped frames, IPA and FAPE for diffusion, with some chirality errors as a result.
Could not read: nothing.
Used before explained: "equivariance" (first use, never defined in the talk). "diffusion" (first use, half explained on the next slide). "random rotations". "chirality violations" is fine for me.
Blue sentence: not clear from the slide. Three short sentences, two of them metaphors (footnotes, the hand), plus a quoted essay in an unreadable footnote. I decoded it only after reading the footnote: built-in knowledge was mostly dropped, except the triangle graph, and the handedness problem came back.
Problems: [high] Fix the blue sentence: "Three of the four built-in choices were dropped and learned from data. The triangles stayed. Mirror-image errors came back." [medium] "equivariance". Fix: "frames, IPA (rotation built in)". [low] "pages 493 to 497" in the subtitle is noise. Fix: drop.

Slide 24: The AlphaFold 3 architecture
Understood: AlphaFold 3 tokenises proteins, nucleic acids, ligands and ions, runs a pairformer, and a diffusion module turns random coordinates into a structure, 25 times, ranked by confidence.
Could not read: all figure text (Template search, Genetic search, Conformer generation, Input embedder, Template module, MSA module, Pairformer 48 blocks, Diffusion module, Confidence module, Recycling, Diffusion iterations). Only the three red labels.
Used before explained: "tokens". "pairformer" (I guessed: the Evoformer without the MSA rows). "diffusion" and "denoises" (not explained beyond "denoises random coordinates"). "sampling".
Blue sentence: half clear. "structure" means two things in this talk (the protein's structure and built-in rules), so I first read "less structure" as "worse structures".
Problems: [medium] Fix the blue sentence: "Fewer built-in rules in the network, more reliance on data and on sampling many candidates". [medium] Figure illegible, the three red labels carry it. Fix: crop to the three boxes. [low] "pairformer: the Evoformer without the MSA rows".

Slide 25: AlphaFold 3, the cost of the removal
Understood: each thing AlphaFold 3 removed shows up as a problem (chirality errors, clashes, hallucinated structure, MSA dependence) that was patched by ranking, more seeds or distillation, and no ablation of the removed parts is reported.
Could not read: nothing.
Used before explained: "the hand in the loss". "a violation loss" (never introduced in the AlphaFold 2 part). "loops for disorder". "seeds". "hallucinated" is fine from chatbots.
Blue sentence: clear. It means AlphaFold 3 beats specialised tools except on one RNA benchmark, and its problems were fixed by workarounds rather than by the network.
Problems: [medium] "violation loss" and "loops for disorder" appear here for the first time. Fix: introduce the violation loss on slide 14, and write "disordered regions drawn as loose loops". [low] "seeds". Fix: "more random starts".

Slide 26: Summary, four design choices, measured
Understood: the four design choices, located in the pipeline figure, cost 2.2, 4.6 and 2.3 GDT or a mirror image when removed, the model is trained end to end, and the final error is below an atom width.
Could not read: the pipeline figure's text. The red numbers 1 to 4 and the table were readable.
Used before explained: "end to end" (roughly clear). "GPU minute".
Blue sentence: clear, and the same as on slide 3, which works as a closing line.
Problems: [medium] "trained end to end, in about one GPU minute per model" reads as if training takes a minute. The paper says one GPU minute is the prediction time for 384 residues and training took days (backup 9 says eleven days). Fix: "Trained end to end. One prediction takes about a GPU minute." [low] The figure is a shrunken copy of slide 5. Fix: a plain outline with the four red marks, or enlarge.

Slide 27: placeholder, not reported.

Slide 28: Questions for the audience
Understood: three discussion questions, built-in symmetry versus learned, folding versus evolution, and trusting pLDDT.
Could not read: nothing.
Used before explained: "rotation equivariance" (never defined). "the hand" (needs "handedness"). "pLDDT is trained on the model's own errors" is new information, it is not on slide 20.
Blue sentence: none.
Problems: [medium] Question 1 wording. Fix: "built rotation symmetry and handedness into the network and the loss". [medium] The premise of question 3 belongs on slide 20. [low] Three open questions is a lot for a short Q&A. Fix: pick one to ask first.

Answers

Where I got lost and stayed lost
Slides 11 and 12. The two supplementary figures are unreadable, and the text under them uses attends, logits and outer product. I recovered on slide 13, whose triangle drawing is simple and legible.
Slide 14's blue sentence and slide 16's "a mirror image is penalised". I did not see why until backup 3, which I would not see in the talk.
Slide 23's blue sentence lost me for a slide. Slide 25 brought me back.

Slides I would drop
Slide 12. Fold its two sentences into slide 10.
The figure of slide 11. Keep its two sentences on slide 10 or on a sketch.
Slide 24. Merge its three red words and two sentences into slide 23.
The four small graphs at the bottom of slide 13.
If time is short, slide 19. It is interesting but not needed for the thread.

The four numbered discs
Yes, they helped once I noticed them on slide 10. From the back the filled disc is visible, the number inside is not. They were not announced: slide 6 lists four items but does not say the discs will track them, and the discs are absent on slides 6 to 9 and 17 to 22, so I first took them for a section counter. Fix: show the four empty discs on slide 6 and say "the discs at the top right follow these four".

The slide I would want for one minute longer
Slide 15. It is the one place where the formula and the drawing match, and a minute would let me see that the third term is just a distance between placed points. Second choice: slide 18, the numbers are the result of the talk.

Three questions I would ask the presenters
1. A mirror image has all the same distances. Why does FAPE punish it?
2. What happens to a protein with no relatives, say a designed protein: does AlphaFold fail silently, or does pLDDT drop?
3. AlphaFold 3 dropped three of the four choices and still won. Were the four ever necessary, or only right for the data and compute of 2020?

Backups, one line each
Backup 1, why IPA is invariant: answers "why do the distances stay the same" with equations. Too dense for me, but yes.
Backup 2, why the structure module is equivariant: the picture (move then update equals update then move) answers "what does equivariance mean" from slide 23 and question 1, if the speaker says so aloud.
Backup 3, where the handedness comes from: answers my first question exactly. One line of it belongs on slide 16.
Backup 4, what FAPE measures: answers "what is d_clamp" and "is FAPE a distance". Yes.
Backup 5, is AlphaFold 2 a graph neural network: answers "what did graph inference mean on slide 10". Too formal for me, but yes.
Backup 6, what each block computes: answers "what is the single representation" and "what is Transition". Yes.
Backup 7, what each ablation removed: answers "what are the statistics and the end-to-end structure gradients on slide 18". Yes.
Backup 8, how confidence is predicted: answers "trained on its own errors" and "resolved". Yes, and the premise of question 3 lives here, not in the talk.
Backup 9, how it was trained: answers my "one GPU minute" confusion (eleven days of training, minutes to hours per prediction). Yes.
Backup 10, AlphaFold 3 further changes: partly answers "what is a pairformer" (sized, not defined). Partly.
Backup 11, row attention figure: a larger copy of slide 11. No new answer.
