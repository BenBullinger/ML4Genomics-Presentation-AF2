# Slide check against the paper and its Supplementary Information

Checked on 2026-10-04 against the slides in `presentation.tex` as cloned on that day.

Status: all changes of section 1 were applied to `presentation.tex` later on 2026-10-04. The column "The slide says" quotes the slides before that change. Three changes differ from the wording suggested below:

- Slide 7 now reads "Every edge ij is updated from the other two edges of all its triangles", which fits on one line.
- Slide 9: the formula now contains the clamp and the scale, min(d_clamp, ·) and 1/Z, and is set one size smaller so that it fits on one line. The line below it gives Z = d_clamp = 10 Å.
- Slide 13 keeps its sentence and cites Tunyasuvunakool et al. 2021 in a footnote. Slide 15 says "reliable confidence".

The new crop on slide 3 would show a corner of the neighbouring panel e, so a small white box covers it (commented in the source).

How sources are cited here:

- "p. 587" is a printed page of the article (`AF.pdf`). "Methods" is the unnumbered Methods section after p. 589.
- "SI 1.9.2" is a section of the Supplementary Information (`AF-SI.pdf`). "Alg. 28" is an algorithm in it.
- Slide numbers are the numbers printed on the slides. Slide 1 is the outline.
- I read the article and the Supplementary Information in full. Of all other papers I read only the passages cited.
- The paper prints no numbers for Fig. 4. The numbers given here for the ablations (Fig. 4a) are means over the three training runs per row. They and the numbers for the trajectories (Fig. 4b) are measured on the vector graphics of the figure.
- A second reader compared this file with the sources. Its corrections are included.

## 1. Statements to change

Contradicted by the paper:

| Slide | The slide says | What the paper says | Suggested wording |
|---|---|---|---|
| 12 | "A frozen structure module read out at every block" | The main network is frozen. A separate structure module is trained for each of the 48 blocks (p. 587, SI 1.14). | "With the trunk frozen, a separate structure module is trained to read out each block." |
| 12 | "ORF8 of SARS-CoV-2 needs all 48." | The axis of the figure runs to 192, which is 4 passes through the 48 blocks. ORF8 "requires nearly the full depth of the network" (Fig. 4b legend). | "ORF8 of SARS-CoV-2 needs nearly all 4 × 48 block evaluations." |

Stronger than the paper:

| Slide | The slide says | What the paper says | Suggested wording |
|---|---|---|---|
| 12 | "most targets fold in the first few" | Fig. 4b shows two targets, the videos four. The text says that for "proteins such as LmrP (T1024), the network finds the final structure within the first few layers" (p. 587). In the figure LmrP passes 90 GDT only around block 25. The legend says both domains "obtain the correct structure early in the network". | "LmrP (T1024) obtains the correct structure early in the network." |
| 7 | "The triangle inequality, built into attention." | The triangle inequality is the motivation: "On the basis of this intuition, we arrange the update operations … in terms of triangles" (p. 586). Two of the four triangle updates are not attention (SI 1.6.5). The SI calls the design "the triangle inductive bias" (SI 1.13.1). My reading of Alg. 11–14: no step enforces the inequality. | "An inductive bias motivated by the triangle inequality." |
| 11 | Title "Every piece earns its accuracy" | Removing the templates changes CASP14 accuracy by −0.3 GDT, and the interval of every run includes zero (Fig. 4a). "A surprisingly small role is played by the distogram head" (SI 1.13.3). | "Which pieces earn their accuracy" |
| 15 | "A GPU minute per structure" | "around one GPU minute per model for 384 residues" (p. 588). Five models are run per protein (Methods, "Inference regimen"). | "About one GPU minute per model for 384 residues." |
| 15 | "Open then, answered since: complexes (AlphaFold-Multimer), ligands and nucleic acids (AlphaFold 3)." | "Answered" is stronger than those papers. AlphaFold-Multimer predicts 70% of heteromeric interfaces successfully and 26% with high accuracy (its abstract). AlphaFold 3 lists its own limits (its section "Model limitations"). | "Open then, addressed since: …" |
| 9 | "the source of AlphaFold's chirality" | "the main source of chirality" (p. 587). SI 1.9.3 names two other sources. | "the main source of AlphaFold's chirality" |
| 13, 15 | "Calibrated confidence made the proteome-scale database usable." and "with calibrated confidence" | The word "calibrated" is not in the article or the SI. The article says that pLDDT "reliably predicts" the lDDT-Cα (p. 584). "Well-calibrated" and "practically useful" are from the companion paper (Tunyasuvunakool 2021, p. 591). | Cite Tunyasuvunakool et al. 2021 on slide 13, or write "reliable confidence". |

Smaller points of wording:

- Slide 2, "all-atom 3D coordinates": the network predicts "the 3D coordinates of all heavy atoms" (p. 585). Hydrogens are added in the final relaxation (SI 1.8.6).
- Slide 7, "the third edges ik, kj": the paper says each edge is updated from "the other two edges" of every triangle it belongs to (SI 1.6.5).
- Slide 8, "No chain constraint during refinement": true inside the structure module (p. 586). The final Amber step, which the paper calls relaxation, does enforce the peptide bonds. "No chain constraint inside the structure module" avoids the confusion.
- Slide 9, "in the frame of every residue": the final loss uses all backbone frames and all side-chain frames (SI 1.9.2). The formula leaves out the clamp at 10 Å and the division by 10 Å (Alg. 28). It sets vectors in bold upright; your convention is bold italic.
- Slide 11, "the triangle updates": that ablation also removes the pair bias and the gating (SI 1.13.1).

Four figure crops cut off content:

- Slide 3: the last bar and its label "G216".
- Slide 11: the first letter of "No end-to-end structure gradients" and half of the panel letter.
- Slide 12: the axis label "Domain GDT".
- Slide 13: the top of the left plot above lDDT-Cα ≈ 88 with its tick label "100", and the lower edge of the x-axis label.

Slides 10, 11 and 14 end on figures of speech ("The unlabelled sequence universe becomes training data", "No single trick; a stack of compounding ones", "The evolutionary record is still an input, not an option"). Their content is supported. I did not judge the style.

## 2. Slide by slide: what is supported, and questions to expect

### Slide 2: Sequence in, structure out

Supported: "months" of effort per structure ("months to years", p. 583). Billions of sequences (p. 583). Fifty years ("more than 50 years", p. 583). CASP is a blind test (p. 583–584).

- **What does "the protein folding problem" mean here?** The abstract restricts the claim to "the structure prediction component" of the problem: the 3D structure for a given sequence. The intermediate structures on slide 12 are described as "the belief of the network of the most likely structure at that block" (p. 587).
- **Is the sequence really the only input?** No. The inputs are the sequence, an alignment of related sequences (MSA) found by database search, and up to four template structures (Methods, "Inputs and data sources"; SI 1.2.2–1.2.3).
- **Why does an MSA contain structural information?** Marks et al. 2011 inferred couplings between pairs of positions from an MSA alone and found that their strength "is an excellent predictor of residue-residue proximity", enough to compute the fold (their abstract).

### Slide 3: CASP14

Supported: 0.96 Å against 2.8 Å (p. 584; 95% confidence intervals 0.85–1.16 Å and 2.7–4.0 Å; 87 domains). Carbon atom about 1.4 Å (p. 584).

- **What is r.m.s.d.95?** The Cα root-mean-square deviation after dropping the worst 5% of residues. Align on all Cα atoms, keep the 95% with the lowest error, repeat five times (Methods, "Metrics"). The paper states that the dropped 5% sometimes "contain genuine modelling errors".
- **And for all atoms?** 1.5 Å against 3.5 Å for the next best method (p. 584).
- **Does this hold outside CASP?** On 3,144 recent PDB chains without a close template the median is 1.46 Å (Fig. 2a).
- **What is GDT?** The score CASP uses for domains (Methods, "Metrics"). GDT-TS is the average fraction of atoms that can be superposed on the experimental structure within 1, 2, 4 and 8 Å, with the best superposition for each threshold (Mariani 2013, introduction). The CASP organizers treat values above about 90 as competitive with experiment; about two thirds of the CASP14 targets reached that (Kryshtafovych 2021).
- **Was anything done by hand?** Almost all submissions came from the automated system. Interventions on three targets changed the score, by 1.14 GDT overall at the time and by 0.01 GDT against the final automated system. Seven further interventions had no effect on the top-ranked models (Jumper et al., Proteins 2021). The numbers in the Nature paper are from the automated system re-run: mean GDT 87.65 against 87.66 for the actual submissions (SI 1.12.2).

### Slide 4: Predictions on top of experiment

Supported: the three panels are Fig. 1b–d. "Without intervention" is stated for the 2,180-residue chain T1044 only (Fig. 1 legend).

- **How can the side chains around the zinc ion be right if the ion is not modelled?** The network is trained to produce the structure "most likely to appear as part of a PDB structure". Where an ion or ligand is predictable from the sequence, the prediction tends to respect it implicitly (p. 588).
- **How does a network trained on crops of 256 and 384 residues handle 2,180?** Position along the chain enters only as a relative offset clipped at ±32, which lets the network run on much longer chains than it was trained on (SI 1.5). Long chains first collapsed; fine-tuning on crops of 384 residues "addressed the problem" (Jumper et al., Proteins 2021). Memory is handled by computing layers in chunks (SI 1.11.8).

### Slide 5: One pipeline, end to end

Supported: MSA and templates in, coordinates out (Fig. 1e). "Recycled three times" (Fig. 1e): the network runs 4 times with the same weights (Alg. 2, N_cycle = 4).

- **What is recycled?** Three outputs of the previous run: the pair representation, the first row of the MSA representation, and the predicted Cβ positions as a binned distance map (SI 1.10, Alg. 32).
- **How is that trained?** The number of runs is drawn uniformly from 1 to 4, and gradients flow only through the last run (Alg. 31). This costs 37.5% extra training time instead of 300% (SI 1.10).
- **How many models and samples at prediction time?** Five models, ranked by their mean pLDDT (SI 1.12.2). Averaging over several MSA samples ("ensembling") adds 0.1 GDT at 8 times the cost (SI 1.12.2). The CASP14 numbers in the paper use 3 samples; "we turn off ensembling for most inference" (Methods, "Inference regimen").
- **How much do the sequence databases matter?** Removing BFD costs 0.4 GDT, removing MGnify 0.7, removing both 6.1 (Methods, "Inputs and data sources").

### Slide 6: The Evoformer block

Supported: two representations that exchange information (p. 585). 48 blocks without shared weights (Fig. 3a, Alg. 6).

- **How do they exchange information?** MSA to pair: an outer product of two MSA columns, averaged over sequences, in every block (Alg. 10). Pair to MSA: the pair representation is added as a bias to the logits of the row-wise MSA attention (Alg. 7, line 3).
- **What are the two attentions on the MSA?** Row-wise attention works along one sequence, across residues. Column-wise attention works at one residue position, across sequences (SI 1.6.1–1.6.2).
- **How large are the representations?** 256 channels per MSA entry and 128 per residue pair (SI 1.5). In fine-tuning: 512 sequences, 5,120 extra sequences, crops of 384 residues (SI Table 4).
- **How is an MSA with thousands of sequences handled?** Random sequences are chosen as cluster centres, and every other sequence is summarized in the profile of its nearest centre (SI 1.2.7). Further sequences go through a small "extra MSA stack" of 4 blocks that only updates the pair representation (SI 1.7.2).
- **What does it cost?** The Evoformer cost grows with N_seq² × N_res (SI 1.2.7). The logits of the triangle attention grow with N_res³ (SI 1.11.8).

### Slide 7: Pairs updated through triangles

Supported: every edge ij is updated from the two other edges of each triangle (SI 1.6.5). See section 1 for the highlighted line.

- **What is the difference between the two kinds of update?** The multiplicative update sums, over the third node k, the product of the two other edges (Alg. 11 and 12). The triangle attention lets edge ij attend to the edges ik that start at the same node, and adds a bias from the third edge jk to the logit (Alg. 13; Alg. 14 is the mirror image).
- **Why both?** The multiplicative update was developed as a cheaper replacement for the attention. Either alone gives high accuracy; "the combination of the two updates is more accurate" (p. 586).
- **How much do triangles contribute?** The ablation replaces the triangle updates by plain axial attention and also removes the pair bias and the gating. It costs 4.6 GDT on CASP14 and 1.7 lDDT-Cα on PDB chains (Fig. 4a; SI 1.13.1).

### Slide 8: The structure module

Supported: one rotation and one translation per residue, all refined simultaneously (p. 585–586; SI 1.8). IPA is invariant, and the update is equivariant (SI 1.8.2). The chain constraint is not enforced inside the module (p. 586).

- **How does invariant point attention work?** The attention logit has three terms: the usual dot product of queries and keys, a bias from the pair representation, and minus the squared distances between "query points" of residue i and "key points" of residue j. Each residue produces these points in its own frame, and they are compared in the global frame (Alg. 22, line 7; 12 heads, 4 query points).
- **Why is it invariant?** A global rotation and translation does not change distances between points (SI 1.8.2, equations 3–4). The output points are mapped back into the frame of residue i (Alg. 22, line 10). The frame update is applied in each residue's own frame, which makes the structure update equivariant. Reflections are excluded.
- **Is the equivariance necessary?** The paper says no: "equivariance in the network is not essential as the single ablation of IPA, which removes all equivariant components, is still a very accurate structure prediction network" (SI 1.13.3). AlphaFold 3 later removed frames and equivariance (see the last section).
- **How are side chains built?** The module predicts seven torsion angles per residue as 2D vectors. Atoms are then placed with ideal bond lengths and bond angles (Alg. 20, line 14; SI 1.8.4).
- **Where do the residues start?** All at the origin with the same orientation. The SI calls this "black hole initialization" (SI 1.8). The module has 8 layers with shared weights (Alg. 20).

### Slide 9: FAPE

Supported: the formula matches Alg. 28 apart from the clamp and the scale. Invariant to rotation and translation of the prediction, not to reflection (SI 1.9.2).

- **Why not a loss on pairwise distances?** A model trained with such a loss (dRMSD) frequently produced mirror structures (SI 1.9.3, Supplementary Fig. 9). The score lDDT-Cα "cannot distinguish molecules of the opposite chirality" either (SI 1.9.3).
- **Why the clamp?** Errors are cut off at 10 Å. For the backbone this is done in 90% of the mini-batches and not in the other 10%. For side chains it is always done (Alg. 28; SI 1.11.5).
- **What is the full loss?** 0.5 FAPE + 0.5 auxiliary structure loss + 0.3 distogram + 2.0 masked MSA + 0.01 confidence. Fine-tuning adds 0.01 "experimentally resolved" + 1.0 violation (SI 1.9, equation 7).
- **Does the network use a physical energy?** Training uses no force field. Fine-tuning adds a penalty on wrong bond lengths, wrong bond angles and clashes (SI 1.9.11). The Amber force field is used only in the final relaxation, which "does not improve the accuracy" (p. 586–587). The paper notes that the network "builds hydrogen bonds effectively without a hydrogen bond score function" (p. 588).

### Slide 10: Trained beyond the PDB

Supported: around 350,000 sequences from Uniclust30, "filtered to a high-confidence subset", then training "again from scratch" (p. 587; exactly 355,993 sequences, SI 1.3). 75% predicted and 25% PDB structures (Methods, "Training regimen"). The masked-MSA loss is trained jointly "and is not pre-trained", and works "without hardcoding a particular correlation statistic into the features" (p. 587).

- **What exactly is kept as "confident"?** The SI describes the filter per residue: "At training time we mask out residues with c_i < 0.5". The confidence c_i is computed from the predicted distance distributions; pLDDT did not exist yet (SI 1.3).
- **Why does the student not just copy the teacher?** The training examples are cropped and their MSAs are subsampled, which makes it "challenging for the network to recapitulate the previously predicted structures" (p. 587; SI 1.3).
- **How much does self-distillation add?** 2.2 GDT on CASP14 and 1.9 lDDT-Cα on PDB chains (Fig. 4a).
- **How is the MSA masked?** 15% of positions. Of these, 70% become a mask token, 10% a random amino acid, 10% an amino acid drawn from the profile, 10% stay. The same masking is applied at prediction time (SI 1.2.7).
- **What data and compute?** PDB structures released up to 30 April 2018. About 10 million samples on crops of 256 residues in about one week on 128 TPU v3 cores, then about 4 days of fine-tuning on crops of 384 (Methods, "Training regimen"; SI Table 4).

### Slide 11: Ablations

The first sentence holds on the CASP14 set for all four components it names. "No single trick" is supported (p. 587; SI 1.13.3). See section 1 for the title.

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
- **How reliable are these?** The authors name two limits: the hyperparameters were not re-tuned for the ablations, and the components interact non-linearly (SI 1.13.3). Each ablation was trained with 3 or 4 seeds, without the distillation set (SI 1.13.2).
- **What does "no end-to-end structure gradients" mean?** The structure losses stay, but their gradients are stopped before the Evoformer, which is then trained by the distogram and the other auxiliary losses only (SI 1.13.1).

### Slide 12: The structure forms inside the trunk

See section 1 for all three statements.

- **What do the curves say in numbers?** ORF8 is at about 35 GDT after the first pass, 43 after the second, 62 after the third and 81 at the end. The two domains of LmrP pass 90 GDT at blocks 25 and 27 of the first pass (Fig. 4b).
- **Why is ORF8 hard?** Its first MSA had only 19 sequences and gave a low-confidence prediction (Jumper et al., Proteins 2021). It has 106 residues (caption of Supplementary Video 3 on the paper's web page).
- **Can we show it?** Supplementary Video 3 is the same trajectory as a video. It is not in the repo because of its size; `README.md` says where it is.

### Slide 13: The model knows when it is right

Supported: pLDDT is predicted per residue from the last single representation of the structure module, in 50 bins (SI 1.9.6). The figure plots chain averages: lDDT-Cα = 0.997 × pLDDT − 1.17, Pearson r = 0.76, 10,795 chains (Fig. 2c).

- **What is lDDT?** The fraction of inter-atomic distances, among atoms within 15 Å of each other in the experimental structure, that the model reproduces within 0.5, 1, 2 and 4 Å, averaged over the four thresholds. No superposition is needed (Mariani 2013).
- **How is pLDDT trained?** After each prediction, the true lDDT-Cα of every residue is computed against the experimental structure. A small head is trained to predict it with a cross-entropy loss, only on structures with resolution between 0.1 and 3.0 Å (SI 1.9.6). Its weight in the total loss is 0.01 (SI 1.9, equation 7).
- **How should the values be read?** The companion paper uses pLDDT > 90 as the cut-off for high accuracy and > 70 for a generally correct backbone (Tunyasuvunakool 2021).
- **Is there a confidence for the whole chain?** Yes, pTM, a predicted TM-score: TM-score = 0.98 × pTM + 0.07, r = 0.85 (Fig. 2d; SI 1.9.7).

### Slide 14: Where it still fails

Supported: accuracy "decreases substantially" below a median alignment depth of around 30 sequences, and gains are small above around 100 (p. 588). Weak when most contacts are with other chains (p. 588).

- **What are "effective sequences"?** The number of sequences that are not gaps at a position, with sequences above 80% identity down-weighted (Methods, "Test set of recent PDB sequences"). The plot uses the median over positions (Fig. 5a legend).
- **Does it work on folds it has never seen?** On 24 structures chosen as novel the median lDDT-Cα is 90.3. Almost all outliers have fewer than 20 sequences in the MSA (SI 1.15).
- **Can one do without the MSA?** ESMFold replaces it by a protein language model. It reaches a TM-score of 0.83 on CAMEO and 0.68 on CASP14; AlphaFold 2 with MSAs reaches 0.88 and 0.85 (Lin et al., preprint of 2022).
- **What else does a prediction not give?** Predictions "do not take into account ligands, covalent modifications or other environmental factors" (Terwilliger 2024, abstract).

### Slide 15: Summary

See section 1 for the GPU minute, "calibrated" and "answered since". Supported: "atomic accuracy" (p. 583), "physical and geometric inductive bias" (p. 588), "evolutionary, physical and geometric constraints" (p. 584).

- **How long does a prediction take?** On one V100 GPU without ensembling: 0.6 min for 256 residues, 1.1 min for 384, 2.1 h for 2,500. With the CASP14 settings: 4.8 min, 9.2 min and 18 h. Database search and relaxation need CPU time on top (Methods, "Inference regimen").
- **Is protein folding solved?** The CASP organizers wrote that the results "represent a solution to the classical protein folding problem, at least for single proteins" (Kryshtafovych 2021, abstract). The limits are those of slide 14.

### Questions on what came before and after

- **How does AlphaFold 2 differ from AlphaFold 1?** AlphaFold 1 predicted distributions of distances between residues, built a potential from them and minimized it by gradient descent (Senior 2020, abstract). AlphaFold 2 is "a completely different model" (p. 583) that outputs coordinates directly and is trained end to end.
- **What about RoseTTAFold?** First published online on 15 July 2021, the same day as the AlphaFold paper (Europe PMC record; the Science issue is dated 20 August 2021). A network with three tracks (sequence, distance map, coordinates), built after DeepMind's CASP14 talk. By its own account it "was still not as good as AlphaFold2" on the CASP14 targets (Baek 2021).
- **Why did AlphaFold 3 drop the frames and the equivariance?** It replaces the Evoformer by a simpler "pairformer" and the structure module by a diffusion module on raw atom coordinates, "without rotational frames or any equivariant processing". The authors "had observed in AF2 that removing most of the complexity of the structure module had only a modest effect". Among its limits the paper reports a chirality violation rate of 4.4% on one benchmark, and invented structure in disordered regions, which it attributes to the switch to a generative model (Abramson 2024).
- **Was this recognized?** The Nobel Prize in Chemistry 2024 went to David Baker, Demis Hassabis and John Jumper for computational protein design and protein structure prediction (`1-context/Nobel2024-scientific-background.pdf`).
