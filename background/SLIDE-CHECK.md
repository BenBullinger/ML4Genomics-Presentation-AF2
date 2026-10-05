# Slide check and questions to expect

This file follows the deck of 2026-10-05: the title slide and 18 numbered slides. For every slide it gives the place in the paper that supports each statement, and the questions to expect with answers. `SCRIPT.md` in the repo root has what to say and the timing.

How sources are cited here:

- "p. 587" is a printed page of the article (`_AF2.pdf`). "Methods" is the unnumbered Methods section after p. 589.
- "SI 1.9.2" is a section of the Supplementary Information (`_AF2-SI.pdf`). "Alg. 28" is an algorithm in it.
- Slide numbers are the numbers printed on the slides. Slide 1 is the outline.
- I read the article and the Supplementary Information in full. Of all other papers I read only the passages cited.
- The paper prints no numbers for Fig. 4. The numbers given here for the ablations (Fig. 4a) are means over the three training runs per row. They and the numbers for the trajectories (Fig. 4b) are measured on the vector graphics of the figure.
- Independent readers compared this file with the sources. Their corrections are included.

History: the version of this file from 2026-10-04 listed nine statements on the slides that contradicted the paper or were stronger than it, and figure crops that cut off content. All of them were corrected in `presentation.tex`. On 2026-10-05 three slides were added (5, 10 and 17), which moved the numbers of the later slides, and the highlighted line of slide 15 was reworded because it claimed more than its source.

## 1. Open points

**Course guidelines.** The deck has not been checked against the course's instructions for the presentation, because I do not have them.

**Figures of speech.** These titles and lines on the slides are figures of speech or slogans. A test listener who had not read the paper named them. Their content is supported. Proposed literal wording:

| Slide | Now | Proposal |
|---|---|---|
| 2, title | "Sequence in, structure out" | "The task: from the sequence to the 3D structure" |
| 2, highlighted line | "Fifty years of the protein folding problem, scored blind at CASP." | "The problem has been open for more than 50 years. CASP tests methods on unpublished structures." |
| 3, title | "CASP14: atomic accuracy, alone" | "CASP14: AlphaFold and the other groups" |
| 3, highlighted line | "Error at the scale of the atoms themselves." | "The median error is smaller than the width of a carbon atom." |
| 4, highlighted line | "Backbone, side chains, and a 2,180-residue chain, without intervention." | "An accurate backbone, accurate side chains, and a chain of 2,180 residues." |
| 9, first line | "Each residue is a rotation and a translation --- a residue gas, refined all at once." | "Each residue has one rotation and one translation. All residues are updated at the same time." |
| 12, title | "Trained beyond the PDB" | "Training with sequences that have no structure" |
| 12, highlighted line | "The unlabelled sequence universe becomes training data." | "Sequences without an experimental structure are used for training." |
| 13, title | "Which pieces earn their accuracy" | "Ablations: what each component contributes" |
| 13, highlighted line | "No single trick; a stack of compounding ones." | "Many components contribute to the accuracy." |
| 14, title | "The structure forms inside the trunk" | "Intermediate structures inside the network" |
| 15, title | "The model knows when it is right" | "The network predicts its own accuracy" |
| 16, highlighted line | "The evolutionary record is still an input, not an option." | "Without enough related sequences the accuracy falls." |
| 18, second line | "…; recycling throughout." | "…; the network is applied four times in a row." |

**Old build in the repo.** `presentation.pdf` in the repo root is still the build with 15 slides. The slide numbers in this file follow `presentation.tex`.

## 2. Slide by slide: what is supported, and questions to expect

### Slide 2: Sequence in, structure out

Supported: "3D coordinates of all heavy atoms" (p. 585). "Months" of effort per structure ("months to years", p. 583). "The structures of around 100,000 unique proteins have been determined" and "billions of known protein sequences" (p. 583). Fifty years ("more than 50 years", p. 583). CASP is held "biennially" and is a blind test (p. 583–584).

- **What does "the protein folding problem" mean here?** The abstract restricts the claim to "the structure prediction component" of the problem: the 3D structure for a given sequence. The intermediate structures on slide 14 are described as "the belief of the network of the most likely structure at that block" (p. 587).
- **Is the sequence really the only input?** No. The inputs are the sequence, an alignment of related sequences (MSA) found by database search, and up to four template structures (Methods, "Inputs and data sources"; SI 1.2.2–1.2.3). Slide 5 explains the alignment.
- **Are hydrogens predicted?** No. Hydrogens are added in the final relaxation (SI 1.8.6).

### Slide 3: CASP14: atomic accuracy, alone

Supported: 0.96 Å against 2.8 Å (p. 584; 95% confidence intervals 0.85–1.16 Å and 2.7–4.0 Å; 87 domains; the figure shows the top 15 of 146 entries). Carbon atom about 1.4 Å (p. 584). CASP14 ran from May to July 2020 (p. 583). For the assessment the targets "were split into domains" (Kryshtafovych 2021).

- **What is r.m.s.d.95?** The Cα root-mean-square deviation after dropping the worst 5% of residues. Align on all Cα atoms, keep the 95% with the lowest error, repeat five times (Methods, "Metrics"). The paper states that the dropped 5% sometimes "contain genuine modelling errors".
- **And for all atoms?** 1.5 Å against 3.5 Å for the next best method (p. 584).
- **Does this hold outside CASP?** On 3,144 recent PDB chains without a close template the median is 1.46 Å (Fig. 2a).
- **What is GDT?** The score CASP uses for domains (Methods, "Metrics"). GDT-TS is the average fraction of atoms that can be superposed on the experimental structure within 1, 2, 4 and 8 Å, with the best superposition for each threshold (Mariani 2013, introduction). The CASP organizers treat values above about 90 as competitive with experiment; about two thirds of the CASP14 targets reached that (Kryshtafovych 2021).
- **Was anything done by hand?** Almost all submissions came from the automated system. Interventions on three targets changed the score, by 1.14 GDT overall at the time and by 0.01 GDT against the final automated system. Seven further interventions had no effect on the top-ranked models (Jumper et al., Proteins 2021). The numbers in the Nature paper are from the automated system re-run: mean GDT 87.65 against 87.66 for the actual submissions (SI 1.12.2).

### Slide 4: Predictions on top of experiment

Supported: the three panels are Fig. 1b–d. "Without intervention" is stated for the 2,180-residue chain T1044 only (Fig. 1 legend).

- **How can the side chains around the zinc ion be right if the ion is not modelled?** The network is trained to produce the structure "most likely to appear as part of a PDB structure". Where an ion or ligand is predictable from the sequence, the prediction tends to respect it implicitly (p. 588).
- **How does a network trained on crops of 256 and 384 residues handle 2,180?** Position along the chain enters only as a relative offset clipped at ±32, which lets the network run on much longer chains than it was trained on (SI 1.5). Long chains first collapsed; fine-tuning on crops of 384 residues "addressed the problem" (Jumper et al., Proteins 2021). Memory is handled by computing layers in chunks (SI 1.11.8).

### Slide 5: The input: a multiple sequence alignment (MSA)

Supported: the input contains "sequences from evolutionarily related proteins in the form of a MSA" (Methods, "Inputs and data sources"). Rows are sequences and columns are residues of the target (p. 585). "May change together": "to maintain energetically favorable interactions, residues in spatial proximity may co-evolve across a protein family" (Marks 2011, introduction). The network reads the sequences themselves: "The MSA representation is initialized with the raw MSA" (p. 585). The drawing is a made-up example, not data from the paper.

- **Why does an MSA contain structural information?** Marks et al. 2011 inferred couplings between pairs of positions from an MSA alone and found that their strength "is an excellent predictor of residue-residue proximity", enough to compute the fold (their abstract). The reverse does not always hold: "correlated residue pairs within a protein are not necessarily close in 3D space" (their introduction).
- **How is the alignment built?** JackHMMER searches MGnify and UniRef90, HHBlits searches Uniclust30 and BFD (SI 1.2.2). BFD has 65,983,866 families with 2,204,359,010 sequences (Methods, "Inputs and data sources"). The paper gives no sizes for the other databases.
- **How much do these databases matter?** Removing BFD costs 0.4 GDT, removing MGnify 0.7, removing both 6.1 (Methods, "Inputs and data sources").
- **What did earlier methods give to the network?** First- and second-order statistics of the MSA are "commonly used in the literature, e.g. by the trRosetta pipeline", usually after fitting a statistical model such as a Potts model (SI 1.13.1). Not all earlier work did this: the paper cites rawMSA (reference 30), which used raw alignments. Giving AlphaFold only such statistics costs 2.2 GDT on CASP14 and 1.3 lDDT-Cα on PDB chains (Fig. 4a, row "No raw MSA").
- **Does the network see every sequence?** Not individually. Random sequences are chosen as cluster centres, and every other sequence is summarized in the profile of its nearest centre (SI 1.2.7). A random sample of the sequences that are not cluster centres also goes through a small "extra MSA stack" of 4 blocks that only updates the pair representation (SI 1.2.7, SI 1.7.2).

### Slide 6: One pipeline, end to end

Supported: MSA and templates in, coordinates out (Fig. 1e). "Recycled three times" (Fig. 1e): the network runs 4 times with the same weights (Alg. 2, N_cycle = 4).

- **What is recycled?** Three outputs of the previous run: the pair representation, the first row of the MSA representation, and the predicted Cβ positions as a binned distance map (SI 1.10, Alg. 32).
- **How is that trained?** The number of runs is drawn uniformly from 1 to 4, and gradients flow only through the last run (Alg. 31). This costs 37.5% extra training time instead of 300% (SI 1.10).
- **How many models and samples at prediction time?** Five models, ranked by their mean pLDDT (SI 1.12.2). Averaging over several MSA samples ("ensembling") adds 0.1 GDT at 8 times the cost (SI 1.12.2). The CASP14 numbers in the paper use 3 samples; "we turn off ensembling for most inference" (Methods, "Inference regimen").
- **How much do templates matter?** Removing them changes CASP14 accuracy by −0.3 GDT, and the interval of every run includes zero (Fig. 4a).

- **How did AlphaFold 1 get from the network to a structure?** Its network predicted distance distributions for residue pairs from MSA features that include "the parameters of a regularized pseudolikelihood-trained Potts model". A potential built from them was minimized by gradient descent; "In CASP13, we obtained 5,000 optimization runs for each chain". In CASP13 it reached a TM-score of 0.7 or more for 24 of 43 free-modelling domains, and its authors wrote that the accuracy "can still not be relied on for the detailed understanding of hard structures" (Senior 2020, `AF1.pdf`, abstract and Methods).

### Slide 7: The Evoformer block

Supported: two representations that exchange information (p. 585). 48 blocks without shared weights (Fig. 3a, Alg. 6).

- **How do they exchange information?** MSA to pair: an outer product of two MSA columns, averaged over sequences, in every block (Alg. 10). Pair to MSA: the pair representation is added as a bias to the logits of the row-wise MSA attention (Alg. 7, line 3).
- **What are the two attentions on the MSA?** Row-wise attention works along one sequence, across residues. Column-wise attention works at one residue position, across sequences (SI 1.6.1–1.6.2).
- **How large are the representations?** 256 channels per MSA entry and 128 per residue pair (SI 1.5). In fine-tuning: 512 sequences, 5,120 extra sequences, crops of 384 residues (SI Table 4).
- **What does it cost?** The Evoformer cost grows with N_seq² × N_res (SI 1.2.7). The logits of the triangle attention grow with N_res³ (SI 1.11.8).

### Slide 8: Pairs updated through triangles

Supported: every edge ij is updated from the two other edges of each triangle (SI 1.6.5). The triangle inequality is the motivation: "On the basis of this intuition, we arrange the update operations … in terms of triangles" (p. 586). The SI calls the design "the triangle inductive bias" (SI 1.13.1). My reading of Alg. 11–14: no step enforces the inequality.

- **What is the difference between the two kinds of update?** The multiplicative update sums, over the third node k, the product of the two other edges (Alg. 11 and 12). The triangle attention lets edge ij attend to the edges ik that start at the same node, and adds a bias from the third edge jk to the logit (Alg. 13; Alg. 14 is the mirror image).
- **Why both?** The multiplicative update was developed as a cheaper replacement for the attention. Either alone gives high accuracy; "the combination of the two updates is more accurate" (p. 586).
- **How much do triangles contribute?** The ablation replaces the triangle updates by plain axial attention and also removes the pair bias and the gating. It costs 4.6 GDT on CASP14 and 1.7 lDDT-Cα on PDB chains (Fig. 4a; SI 1.13.1).

### Slide 9: The structure module: residues as rigid bodies

Supported: one rotation and one translation per residue, "representing the geometry of the N-Cα-C atoms", all refined simultaneously (p. 585–586; SI 1.8). The update is equivariant (SI 1.8.2). The chain constraint is not enforced inside the module (p. 586).

- **How are side chains built?** The module predicts seven torsion angles per residue as 2D vectors. Atoms are then placed with ideal bond lengths and bond angles (Alg. 20, line 14; SI 1.8.4).
- **Where do the residues start?** All at the origin with the same orientation. The SI calls this "black hole initialization" (SI 1.8). The module has 8 layers with shared weights (Alg. 20).
- **When is the chain made physically correct?** A violation loss in fine-tuning encourages correct peptide bonds, and the final Amber relaxation enforces them (p. 586; SI 1.9.11, SI 1.8.6). The relaxation "does not improve the accuracy" (p. 586–587).

### Slide 10: Invariant point attention

Supported: the formula is line 7 of Alg. 22 for one attention head. The head index and the scaling constants w_L, w_C, γ and 1/√c are left out, as the footnote on the slide says. Each residue produces its points "in its local frame", and they are "projected into the global frame using the backbone frame of the residue" (Methods, "IPA"). Invariance: a global rigid transformation cancels in the squared distance (SI 1.8.2, equations 3–4).

- **What are the constants that the slide leaves out?** w_L = √(1/3) and w_C = √(2/(9 · 4)) for 4 query points. They are set so that the three terms contribute equally at initialization. γ is learned, one value per head (SI 1.8.2; Alg. 22, lines 5–6).
- **How many heads and points?** 12 heads, 4 query points and 8 value points per head, in nanometres (Alg. 22).
- **What does the layer output?** For each residue, three weighted sums with the same attention weights: over the pair entries, over the usual values, and over value points. The value points are summed in the global frame and mapped back into the frame of residue i (Alg. 22, lines 8–10). Line 11 concatenates the three sums and the norms of the output points and applies a linear layer.
- **Why is the structure update equivariant?** The frame update is applied in each residue's own frame. If all frames are moved by the same rigid motion, the updated structure moves by the same motion. Reflections are excluded (SI 1.8.2).
- **Is the equivariance necessary?** The paper says no: "equivariance in the network is not essential as the single ablation of IPA, which removes all equivariant components, is still a very accurate structure prediction network" (SI 1.13.3). AlphaFold 3 later predicted structures without frames and without equivariance (slide 17).
- **How does the pair representation enter?** It "augments both the logits and the values of the attention process, which is the primary way in which the pair representation controls the structure generation" (Methods, "IPA").

### Slide 11: FAPE: a loss over local frames

The drawing is my own illustration of Alg. 28 (one frame k, one atom i, the prediction rotated as a whole with two atoms displaced); it is not data and it is flat, so it cannot show a mirror image. Supported: the formula is Alg. 28 with Z = d_clamp = 10 Å. The final loss uses all backbone and side-chain frames (SI 1.9.2). Invariant to rotation and translation of the prediction, not to reflection (SI 1.9.2). "The main source of chirality" (p. 587).

- **Why not a loss on pairwise distances?** A model trained with the dRMSD loss frequently produced mirror structures (SI 1.9.3, Supplementary Fig. 9). dRMSD is "the distance-based equivalent of RMSD" (Mariani 2013, introduction). The score lDDT-Cα "cannot distinguish molecules of the opposite chirality" either (SI 1.9.3).
- **Why the clamp?** Errors are cut off at 10 Å. For the backbone this is done in 90% of the mini-batches and not in the other 10%. For side chains it is always done (Alg. 28; SI 1.11.5).
- **What is the full loss?** 0.5 FAPE + 0.5 auxiliary structure loss + 0.3 distogram + 2.0 masked MSA + 0.01 confidence. Fine-tuning adds 0.01 "experimentally resolved" + 1.0 violation (SI 1.9, equation 7).
- **Does the network use a physical energy?** Training uses no force field. Fine-tuning adds a penalty on wrong bond lengths, wrong bond angles and clashes (SI 1.9.11). The Amber force field is used only in the final relaxation. The paper notes that the network "builds hydrogen bonds effectively without a hydrogen bond score function" (p. 588).

### Slide 12: Trained beyond the PDB

Supported: around 350,000 sequences from Uniclust30, "filtered to a high-confidence subset", then training "again from scratch" (p. 587; exactly 355,993 sequences, SI 1.3). 75% predicted and 25% PDB structures (Methods, "Training regimen"). The masked-MSA loss is trained jointly "and is not pre-trained", and works "without hardcoding a particular correlation statistic into the features" (p. 587).

- **What exactly is kept as "confident"?** The SI describes the filter per residue: "At training time we mask out residues with c_i < 0.5". The confidence c_i is computed from the predicted distance distributions; pLDDT did not exist yet (SI 1.3).
- **Why does the student not just copy the teacher?** The training examples are cropped and their MSAs are subsampled, which makes it "challenging for the network to recapitulate the previously predicted structures" (p. 587; SI 1.3).
- **How much does self-distillation add?** 2.2 GDT on CASP14 and 1.9 lDDT-Cα on PDB chains (Fig. 4a).
- **How is the MSA masked?** 15% of positions. Of these, 70% become a mask token, 10% a random amino acid, 10% an amino acid drawn from the profile, 10% stay. The same masking is applied at prediction time (SI 1.2.7).
- **What data and compute?** PDB structures released up to 30 April 2018. About 10 million samples on crops of 256 residues in about one week on 128 TPU v3 cores, then about 4 days of fine-tuning on crops of 384 (Methods, "Training regimen"; SI Table 4).

### Slide 13: Which pieces earn their accuracy

Supported: the sentence holds on the CASP14 set for all four components it names. Many components contribute (p. 587; SI 1.13.3).

Differences to the baseline in Fig. 4a (GDT on 87 CASP14 domains, lDDT-Cα on 2,261 PDB chains). The baseline is the model without self-distillation (SI 1.13.1).

| Row of the figure | CASP14 | PDB chains |
|---|---|---|
| With self-distillation (added, not removed) | +2.2 | +1.9 |
| No templates | −0.3 | −0.4 |
| No distogram head | −1.2 | −0.3 |
| No raw MSA | −2.2 | −1.3 |
| No IPA | −2.3 | −0.3 |
| No masked-MSA head | −2.4 | −1.8 |
| No recycling | −4.5 | −1.8 |
| No triangles, biasing or gating | −4.6 | −1.7 |
| No end-to-end structure gradients | −6.2 | −2.6 |
| No IPA and no recycling | −16.3 | −3.1 |

- **Does IPA matter or not?** On CASP14 its removal costs 2.3 GDT, as much as self-distillation adds. On the larger PDB set it "has only a tiny effect", while removing IPA and recycling together "has a much larger effect than removing recycling alone" (SI 1.13.3).
- **Does every component matter?** No. Removing the templates has no measurable effect on CASP14, and "a surprisingly small role is played by the distogram head" (SI 1.13.3).
- **How reliable are these?** The authors name two limits: the hyperparameters were not re-tuned for the ablations, and the components interact non-linearly (SI 1.13.3). Each ablation was trained with 3 or 4 seeds, without the distillation set (SI 1.13.2).
- **What does "no end-to-end structure gradients" mean?** The structure losses stay, but their gradients are stopped before the Evoformer, which is then trained by the distogram and the other auxiliary losses only (SI 1.13.1).

### Slide 14: The structure forms inside the trunk

Supported: the main network is frozen and a separate structure module is trained for each of the 48 blocks (p. 587, SI 1.14). The axis runs to 192, which is 4 runs through the 48 blocks. Both domains of LmrP "obtain the correct structure early in the network"; ORF8 "requires nearly the full depth of the network" (Fig. 4b legend).

- **What do the curves say in numbers?** At the last block of each run, ORF8 is at about 35, 42, 66 and 81 GDT. The curve drops by a few points at the start of each new run. The two domains of LmrP pass 90 GDT at x = 25 and x = 27 on the axis, in the first run (Fig. 4b).
- **Why is ORF8 hard?** Its first MSA had only 19 sequences and gave a low-confidence prediction (Jumper et al., Proteins 2021). It has 106 residues (caption of Supplementary Video 3 on the paper's web page).
- **Can we show it?** Supplementary Video 3 is the same trajectory as a video. It is not in the repo because of its size; `README.md` says where it is.
- **Is this how a protein folds?** The paper describes the intermediate structures as "the belief of the network of the most likely structure at that block" (p. 587).

### Slide 15: The model knows when it is right

Supported: pLDDT is predicted per residue from the last single representation of the structure module, in 50 bins (SI 1.9.6). The figure plots chain averages: lDDT-Cα = 0.997 × pLDDT − 1.17, Pearson r = 0.76, 10,795 chains (Fig. 2c). The highlighted sentence is from the companion paper, cited on the slide: "For the resulting predictions to be practically useful, they must come with a well-calibrated and sequence-resolved confidence measure" (Tunyasuvunakool 2021, p. 591).

- **What is lDDT?** The fraction of inter-atomic distances, among atoms within 15 Å of each other in the experimental structure, that the model reproduces within 0.5, 1, 2 and 4 Å, averaged over the four thresholds. No superposition is needed (Mariani 2013).
- **How is pLDDT trained?** After each prediction, the true lDDT-Cα of every residue is computed against the experimental structure. A small head is trained to predict it with a cross-entropy loss, only on structures with resolution between 0.1 and 3.0 Å (SI 1.9.6). Its weight in the total loss is 0.01 (SI 1.9, equation 7).
- **How should the values be read?** The companion paper uses pLDDT > 90 as the cut-off for high accuracy and > 70 for a generally correct backbone (Tunyasuvunakool 2021).
- **Is there a confidence for the whole chain?** Yes, pTM, a predicted TM-score: TM-score = 0.98 × pTM + 0.07, r = 0.85 (Fig. 2d; SI 1.9.7).

### Slide 16: Where it still fails

Supported: accuracy "decreases substantially" below a median alignment depth of around 30 sequences, and gains are small above around 100 (p. 588). Weak when most contacts are with other chains (p. 588). The paper gives no cause for this; it expects that "a future system" for full complexes "will remove the difficulty" (p. 588). AlphaFold "was trained on individual protein chains" (Evans 2021).

- **What are "effective sequences"?** The number of sequences that are not gaps at a position, weighted by "the Neff scheme" with "a threshold of 80% sequence identity" (Methods, "Test set of recent PDB sequences"). In that scheme the weight of a sequence is the inverse of the number of sequences that share at least 80% identity with it (Yang 2019, Methods). The plot uses the median over positions (Fig. 5a legend).
- **Does it work on folds it has never seen?** On 24 structures chosen as novel the median lDDT-Cα is 90.3. Almost all outliers have fewer than 20 sequences in the MSA (SI 1.15).
- **Can one do without the MSA?** ESMFold replaces it by a protein language model. It reaches a TM-score of 0.83 on CAMEO and 0.68 on CASP14; AlphaFold 2 with MSAs reaches 0.88 and 0.85 (Lin et al., preprint of 2022).
- **What else does a prediction not give?** Predictions "do not take into account ligands, covalent modifications or other environmental factors" (Terwilliger 2024, abstract).

### Slide 17: What followed

Supported, row by row:

- RoseTTAFold: information at "the 1D sequence level, the 2D distance map level, and the 3D coordinate level" (Baek 2021, abstract). First published online on 15 July 2021 (Europe PMC record; the Science issue is dated 20 August 2021), the day the AlphaFold paper was published online (p. 583).
- Human proteome: "covers 98.5% of human proteins with a full chain prediction" (Tunyasuvunakool 2021, p. 591; published online 22 July 2021).
- AlphaFold-Multimer: "an AlphaFold model trained specifically for multimeric inputs" (Evans 2021, abstract; first posted on 4 October 2021 according to Europe PMC).
- ESMFold: structure "directly from the primary protein sequence", without multiple sequence alignments (Lin et al., preprint of 2022).
- AlphaFold 3: a "diffusion-based architecture" for "complexes including proteins, nucleic acids, small molecules, ions and modified residues" (Abramson 2024, abstract).
- AlphaFold 3, benefit: "In all but one category, it achieves a substantially higher performance than strong methods that specialize in just the given task", and it "has also improved in protein complex accuracy relative to AlphaFold-Multimer (v.2.3)" (Abramson 2024, `AF3.pdf`, p. 493 and p. 497). The exception is RNA in CASP15, where a submission aided by human experts was better (p. 497).
- Nobel Prize in Chemistry 2024 to David Baker, Demis Hassabis and John Jumper for computational protein design and protein structure prediction (`1-context/Nobel2024-scientific-background.pdf`).
- Highlighted line: the diffusion module of AlphaFold 3 works "without rotational frames or any equivariant processing" (Abramson 2024, p. 495). Frames are still used in one place: "While we no longer use rigid frames for the core prediction task, we do use frames for the PAE confidence head" (its supplement, section 7). So the line says "predicts structures without frames", not "has no frames".

Questions:

- **How does AlphaFold 2 differ from AlphaFold 1?** AlphaFold 1 trained a network to "predict the distances between pairs of residues", built a potential from them and minimized it by gradient descent (Senior 2020, abstract). AlphaFold 2 is "a completely different model" (p. 583) that outputs coordinates directly and is trained end to end.
- **How good is RoseTTAFold?** By its own account it "was still not as good as AlphaFold2" on the CASP14 targets. It was built after DeepMind's CASP14 talk (Baek 2021).
- **How good is AlphaFold-Multimer?** It predicts 70% of heteromeric interfaces successfully and 26% with high accuracy. These numbers are from the version of 10 March 2022, the only one I have (Evans 2021, abstract).
- **How does ESMFold compare?** It reaches a TM-score of 0.83 on CAMEO and 0.68 on CASP14; AlphaFold 2 reaches 0.88 and 0.85. It is "up to 60x faster" (Lin et al., preprint of 2022).
- **Why did AlphaFold 3 drop the frames and the equivariance?** It replaces the Evoformer by a simpler "pairformer" and the structure module by a diffusion module on raw atom coordinates. The authors "had observed in AF2 that removing most of the complexity of the structure module had only a modest effect". Among its limits the paper reports a chirality violation rate of 4.4% on one benchmark, and invented structure in disordered regions, which it attributes to the switch to a generative model (Abramson 2024). The step from AlphaFold 2's ablation to AlphaFold 3's design is the authors' own: see the quotation above.

### Slide 18: Summary

Supported: "atomic accuracy" (p. 583), "physical and geometric inductive bias" (p. 588), "evolutionary, physical and geometric constraints" (p. 584). "Around one GPU minute per model for 384 residues" (p. 588). pLDDT "reliably predicts" the lDDT-Cα (p. 584).

- **How long does a prediction take?** On one V100 GPU without ensembling: 0.6 min for 256 residues, 1.1 min for 384, 2.1 h for 2,500. With the CASP14 settings: 4.8 min, 9.2 min and 18 h. Database search and relaxation need CPU time on top (Methods, "Inference regimen"). Five models are run per protein.
- **Is protein folding solved?** The CASP organizers wrote that the results "represent a solution to the classical protein folding problem, at least for single proteins" (Kryshtafovych 2021, abstract). The limits are those of slide 16.

## 3. Statements in the speaker notes that are general knowledge

`SCRIPT.md` explains some terms that the paper takes for granted. These explanations are textbook knowledge, not statements of the paper:

- A residue is one amino acid of the chain. The backbone is the part common to all residues. The side chain is the part that differs between the 20 amino acids.
- A domain is a part of a chain that folds into a compact unit.
- One ångström is 0.1 nanometre.
- Evolutionarily related proteins fold into nearly the same structure.
- A protein and its mirror image are different molecules.
- The orientation of a protein in space is arbitrary, which is why invariance is wanted on slide 10.
- The Protein Data Bank is "the single global archive for 3D macromolecular structure data" (title of reference 5 of the paper).

Two statements in the notes are my reading and not a quotation: that an outer product averaged over the sequences "measures how two columns vary together" (slide 7; compare SI 1.13.1, where the same operation on the raw features yields the pairwise frequencies), and that three entries of slide 17 "address the three limits" of slide 16.

