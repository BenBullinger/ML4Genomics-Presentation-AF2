# Grader's review of the AlphaFold 2 deck (pages p-02 to p-41, 15 October 2026)

Role: lecturer or head TA grading paper presentations in 263-5351-00L. Read-only. Slide 27 (exam question placeholder) is not reported.

## Criteria applied, quoted from the guidelines

- "The presentation should be 25 min long (part 1) ... will be cut if you supersede the 25 min mark."
- "present your attempted answer at the end of the presentation, after your conclusion" and "prepare at least two questions for the audience and moderate a small discussion section".
- Introduction: "put the study into context, using class material when relevant. Please, provide necessary CS or biological background."
- Methods: "familiar with the methods in detail (including anything hidden in supplementary!) ... present it so that it is accessible ... a couple hidden slides at the end".
- Results: "highlight the main results of the article and their relevance."
- Discussion: "Be critical about the article! ... put the contributions into context, understand the relevance and importance of the paper, and its limitations."
- "capacity to communicate clearly a message to the audience ... making the presentation somewhat entertaining and keeping your audience concentrated throughout."

I checked every number on the slides against _AF2.pdf, _AF2-SI.pdf and AF3.pdf (and the AF3 supplement for ablations). All numbers hold, including 0.96 Å on 87 domains, 350,000 distillation structures and 75 %, the 30-sequence threshold, c_m = 256 and c_z = 128, N_seq = 128 and crops of 256 (SI Table 4), 10 million and 1.5 million samples on 128 TPU v3 cores, the 50 pLDDT bins and the 0.1 to 3 Å filter, 3 or 4 seeds per ablation, the 4.4 % chirality rate, 5 seeds times 5 samples, the 20-step mini rollout, and "about one GPU minute per model" (1.1 min for 384 residues without ensembling, Methods). The AF3 paper and its supplement report no ablation. The deck's content is correct.

## 1. Grade

5.0 as the deck stands. With weaknesses 1 to 3 fixed it is a 5.5, and with 4 and 5 fixed it is a 6.

Justification. The content is correct at the level of the supplement, the thread (four properties, four design choices, their ablation cost, AlphaFold 3's verdict) is the best organising idea I have seen in a student deck, and the backups answer the questions a TA asks. It loses marks because the headline result slide is unfinished (a working note stands on slide 3 and its chart is commented out), because 26 slides for 25 minutes will be cut before the summary, and because the critical discussion repeats the paper's own two limitations and adds no criticism of its own.

## Structure, timing and split

Structure follows the recommendation: problem and benchmark (2 to 4), methods (5 to 16), training (17), results and interpretation (18 to 21), discussion and conclusion (22 to 26), exam question after the conclusion (27), audience questions (28). The main accuracy result sits in the introduction (slides 3 and 4), which is fine, but then the results section carries no accuracy number beyond CASP14.

Timing. Part 1 is slides 1 to 26. That is 58 seconds per slide. Eight of them (9 to 16) are architecture slides with formulas or paper figures; the previous script budgeted 1.5 to 2.5 minutes for each and was already "very tight" at 26.5 minutes of reading for 18 slides in a 30-minute plan. The current deck will run 32 to 35 minutes. The chair cuts at 25:00, which removes the summary and the AlphaFold 3 verdict, the two slides that earn the grade. The deck has to lose five or six slides, see weakness 2.

Split. Evita has 16 slides, including the three geometry slides (14 to 16) and both formulas, in 12.5 minutes: 47 seconds a slide. Ben has 10 slides in 12.5 minutes: 75 seconds a slide. Move the handover to after slide 13 (triangles). The structure module, IPA and FAPE then go to Ben, who wrote SYMMETRY.tex and backups 3 and 4 and will take the questions on them anyway. That gives 13 and 13, and matches the paper's sections: Evita presents the problem, CASP14 and the Evoformer, Ben presents end-to-end structure prediction, training, interpretation and discussion. WORK-SPLIT.md already lists slide 16 as open.

## 2. The five costliest weaknesses, ranked

1. Slide 3 is unfinished. The redrawn Fig. 1a bar chart is commented out in the source, a bold working note "Show the average prediction hist from the paper" stands on the slide, the hyphen in "Blind test - experimental structures" is the dash the deck forbids, and the key statement "below one atom width" has no figure and no 1.4 Å reference. A grader sees a draft. Fix: restore the commented tikz chart (AlphaFold 0.96 Å against the next 14 groups, the dashed 1.4 Å carbon line is already drawn), delete the note, and move the Å and RMSD definitions into the footnote. Keep three lines: what CASP is, blind, when.

2. The deck is too long for 25 minutes (see above). Fix, in this order: drop slide 4 (its left panel repeats slide 2, Evita already proposed deleting it); fold slides 11 and 12 into slide 10 by using their two key lines as the two statements of slide 10 (the SI screenshots stay in the backup, where slide 11 already is as backup 11); move slide 24 (AF3 architecture) to the backup; merge slides 23 and 25 into one AF3 table. That is 22 slides in part 1, about 68 seconds each. Rehearse with a stopwatch at the dry run and stop at 24:00.

3. The split is uneven in time, not in slide count (see above). Fix: handover after slide 13.

4. The critical discussion is the paper's own. Slide 21 shows the two limitations the paper reports, slides 23 and 25 are a fair and well-sourced critique of AlphaFold 3, but nothing on the deck questions Jumper et al. themselves, and nothing ties the paper to class material. What a grader expects to hear, spoken, not written: the redrawn ablation chart drops the paper's 95 % intervals, with 3 or 4 seeds the rows at minus 0.3 and minus 0.4 are within noise (slide 18, draw the intervals as thin lines); the paper's own supplement concludes "equivariance in the network is not essential" (SI 1.13.3), which is the deck's own property 3 and the thing AlphaFold 3 dropped, so say it on slide 6 or 23 as the test of your thread; one static structure per sequence, a point mutation changes the prediction little, which is the question a genomics audience will ask; and where the course's material appears in the method (attention over an alignment, BERT-style masking as in DNA language models, coevolution). Fix: say these on slides 6, 18 and 21, and add the intervals to the chart on slide 18.

5. The results section carries no accuracy beyond CASP14. The paper's second result, generalisation to 3,144 recent PDB chains after the training cutoff with a median of 1.46 Å (Fig. 2a), and the side-chain accuracy given an accurate backbone (Fig. 2b), are not on the deck. Slide 4 claims "also in the side chains" from one picture. Fix: if slide 4 stays, replace its three pictures by Fig. 2a's histogram and one side-chain picture, so the slide shows the result on new structures instead of repeating slide 2.

## 3. Per-slide findings

Severity: high, medium, low. Slide numbers are the printed ones (p-NN is slide NN-2).

- Slide 1, low. The outline names "The benchmark" as a section of two slides and hides the critical part under "Conclusion". Fix: rename section 6 "Limitations and AlphaFold 3" so the grader sees the discussion in the outline.
- Slide 2, low. The structure panel is the same panel as the left third of slide 4. Fix: drop slide 4, or show Fig. 1c (the zinc site) here.
- Slide 3, high. Unfinished, see weakness 1. Fix: restore the chart, delete the note and the dash.
- Slide 4, medium. Repeats slide 2's figure and costs a minute; the side-chain claim rests on one picture. Fix: delete, or replace the three panels by Fig. 2a and 2b, see weakness 5.
- Slide 6, low. "Removing any one of the four costs accuracy" is true but the costs differ by a factor of seven (property 3: 2.3 GDT on CASP14, 0.3 lDDT on PDB chains) and the supplement calls equivariance "not essential". Fix: say the sizes differ and that slides 18 and 23 will test the claim; no text change.
- Slide 7, low. "query" here, "target" on slide 8, for the same row. Fix: one word on both slides. A TA may ask where the single representation and the frames are if "everything is written into these two tables"; answer: the single representation is a linear map of the first MSA row.
- Slide 11, medium. A screenshot of Supplementary Fig. 2 whose labels are illegible from the back row, carrying one line of message, and identical to backup 11. Fix: fold the key line into slide 10, keep the figure as the backup.
- Slide 12, medium. The figure is Supplementary Fig. 3 only, shown at 60 % width and illegible even at full size, while the subtitle names Figs. 3 to 5 and the slide's point, the outer product mean, has no picture. Fix: show Supplementary Fig. 5 at full width, or drop the figure and fold the two lines into slide 10.
- Slide 14, low. Content correct (the paper enforces the peptide bond only through the violation loss in fine-tuning and the relaxation afterwards). The key statement invites the question "then how are the bonds right?"; the backups do not cover it. Fix: have the answer ready; no slide change.
- Slide 17, low. The 25 % and 75 % are sampling probabilities per training example, not shares of a dataset; "adds 350,000 structures" is the 355,993 predicted sequences before the confidence filter. Fix: say so when asked.
- Slide 18, medium. The redrawn chart drops the paper's 95 % bootstrap intervals, so one-decimal bars read as exact. Fix: draw the intervals as thin lines, as the commented chart on slide 3 does.
- Slide 19, low. The blue and orange curves are the two domains of LmrP (T1024 D1 and D2, Fig. 4b legend); the slide labels "LmrP" once and a TA will ask what the second curve is. Fix: label "LmrP, two domains".
- Slide 20, low. The plot is Fig. 2c of Jumper et al. (10,795 chains), but the footnote names only Tunyasuvunakool, the source of the key sentence. Fix: footnote "Fig. 2c. The key sentence is from Tunyasuvunakool et al. 2021".
- Slide 21, medium. Two limitations, both the paper's. See weakness 4. Fix: spoken points on noise, static structures and point mutations; replace the second statement by the one that matters most to this audience if you want it on the slide.
- Slide 22, low. "With one exception" must be named when speaking: AIchemy_RNA2 with human input on the CASP15 RNA targets.
- Slide 23, low. "The bitter lesson, with two footnotes" is a figure of speech that needs the footnote's quote read aloud. Fix: say Sutton's sentence first, then the key line.
- Slide 24, low. Correct, but the first candidate for the backup when time is cut. Fix: move to the backup.
- Slide 25, low. "loops for disorder" is unclear to a listener; "wins everywhere but one RNA entry" needs the entry named. Fix: say "AlphaFold 2 draws disordered regions as loose loops, AlphaFold 3 invents structure there". The claim "no ablation of the removed parts is reported" is correct for the paper and its supplement.
- Slide 28, low. Three good questions. Question 1 is the most abstract; question 2 is the one every student can answer. Fix: ask 2 first, then 1 with AlphaFold 3's numbers as the reveal, 3 if time remains, as the source comment already plans.
- Backup 1, low. Pulling T_global out of the weighted sum needs the weights to sum to one (an affine map commutes with a convex combination). A TA may ask. Fix: say it.
- Backup 2, low. "the output's global frame is arbitrary" is imprecise: with all frames at the identity the output frame is fixed by the weights and unrelated to the experiment's frame, which is why the loss must be invariant. Fix: replace "arbitrary" by "unrelated to the experiment's frame".
- Backup 4, low. The bound in SI eqs. 18 to 22 is a mean point error after the best proper alignment, which the SI calls "RMSD-like", not the RMSD. Fix: "at least the mean point error after the best rigid alignment".
- Backup 6, low. "s_u = m_1u" is a linear map of m_1u (Algorithm 2 line 10). "Recycling, 4 cycles" against slide 5's "recycled three times" needs one spoken sentence: four passes, three recycles. Fix: write "s_u = Linear(m_1u)".
- Backup 11, low. Identical to slide 11. Fix: keep one copy, in the backup.

Skipped, nothing to report: slides 5, 8, 9, 10, 13, 15, 16, 26, 27 (placeholder), backups 3, 5, 7, 8, 9, 10. All were checked against the papers.

## 4. Three things the deck does better than typical student presentations

1. It has a thread. Four properties of proteins, four design choices, the cost of each in the ablations, and AlphaFold 3's verdict on each. The four discs at the top right tell the audience where they are. Most student decks walk through the figures in the paper's order.
2. It works at the level of the supplement and says so. Every method slide cites the algorithm and section, the two formulas (IPA, FAPE) are reduced to the terms that carry the idea with the scaling constants named in a footnote, the figures are redrawn with legible axes, and the backups answer the questions a TA actually asks: why invariant, where the handedness comes from, what each ablation removed, how pLDDT is trained.
3. The critique is evidence, not opinion. The AlphaFold 3 slides use the follow-up paper's own numbers (4.4 % chirality violations, patches by ranking and seeds, no ablation reported), and the audience questions grow out of the deck's thread rather than being generic.
