# Communication review: AlphaFold 2 deck (2026-10-15)

Reviewer role: senior researcher, NeurIPS, ICML and the geometric deep learning community, judging against the tutorial standard of Petar Velickovic. Read-only. Pages p-02 to p-41 were viewed at full size, the dense ones also at back-row size. Facts were checked in _AF2.pdf, _AF2-SI.pdf, AF3.pdf and _DEV/background.

## 1. Verdict

The spine is a real research argument: four facts about proteins become four design choices, the ablation prices each one, and AlphaFold 3 tells which survived; the four discs make that thread visible on every slide, and the own drawings on slides 6, 15, 16 and 18 are at the bar. What separates the deck from that bar is finish, not design: slide 3 is an unfinished draft without its chart, slides 11 and 12 paste supplementary figures that nobody past the third row can read, seven pasted figures carry no figure number on their slide and one (slide 20) reads as another paper's figure, and the climax lines on slides 23 and 25 are slogans a listener could not repeat. At 26 content slides for 25 minutes, with the first speaker holding 16 of them, the talk will run over unless about six slides are merged or cut.

## 2. The five costliest weaknesses, ranked

1. Slide 3 is a draft (high). The headline number of the paper, 0.96 A against 2.8 A, has no chart; the slide is five definitions and a bold placeholder, while the footnote already says "Redrawn from Fig. 1a". Fix: restore the bar chart that is commented out in main.tex (lines 337 to 358), keep two lines ("CASP14 is a blind test, May to July 2020" and the metric line), move the angstrom and RMSD definitions to the speaker or to one grey line, replace the hyphen used as a dash.

2. Pasted figures are not attributed where they are used (high). Slides 4, 5, 10, 13, 14, 19 and 21 show Jumper et al. figures with no figure number or author on the slide; slides 2 and 9 give the figure number but not the paper; slide 20 cites only Tunyasuvunakool, so its Fig. 2c of Jumper reads as hers. Fix: one grey line under every pasted figure in a fixed form, "Jumper et al., Nature 2021, Fig. 4b", and on the summary slide one licence line: "Figures reproduced from Jumper et al. 2021 and Abramson et al. 2024, both CC BY 4.0" (both PDFs print the Creative Commons Attribution licence).

3. Slides 11 and 12 show figures nobody can read (high). Supplementary Figs. 2 and 3 are box diagrams with 6 pt labels; at back-row size slide 12 is a smear and slide 11 a shape. Each slide carries one sentence of content. Fix: one own drawing replacing both slides, built from the arrays of slide 7: on the left one MSA row with q, k and a z_ij block entering the softmax (row attention with pair bias), on the right two columns i and j combined into cell z_ij (outer product mean). This also removes the paper's own red boxes on slide 11, which read as the deck's marks.

4. Key lines that are slogans (medium to high). Slide 23 "The bitter lesson, with two footnotes. The graph survived. The hand came back." and slide 25 "It wins everywhere but one RNA entry. The costs were paid in patches." are the climax of the talk and cannot be paraphrased without the speaker. Slides 7, 9, 12, 19, 21 and 24 have milder cases. Literal replacements are in section 4.

5. Rhythm (medium). 26 content slides in 25 minutes; the script of 5 October had 3,440 words for 18 slides and ran 26.5 minutes, and the deck has grown by eight slides since. The first speaker has 16 slides in 12.5 minutes, 47 seconds each, including the dense architecture slides. Cut or merge: the outline (the discs do its job), slide 4 into slide 3 (chart left, side-chain panel right), slide 9 into slide 7, slide 12 into slide 11, slide 25 into slide 23, slide 19 to the backups. At 22 slides: 1 problem, 2 CASP14 with the chart and the side chains, 3 pipeline, 4 four facts, 5 the two arrays with the pair's content, 6 MSA, 7 Evoformer block, 8 row attention and outer product mean (own drawing), 9 triangles, 10 structure module, 11 IPA, 12 FAPE, 13 training, 14 ablations, 15 confidence, 16 limitations, 17 timeline, 18 AlphaFold 3 architecture, 19 AlphaFold 3 verdict and cost in one table, 20 summary, 21 exam question, 22 audience questions. Handover after 12: the first speaker has 12 slides at about 60 seconds, the second 8 content slides at about 95 seconds, which fits since the second half is tables.

Also missing, lower cost:

- The DOI and the repository link on the title slide, and the deck's own licence on the last slide (the README says "To be set"). The deck will be read without the README.
- One sentence that states the thesis. It exists nowhere. Proposal for slide 26: "Four facts became four design choices. Each costs accuracy when removed. AlphaFold 3 kept one."
- A running biological example. T1049 appears on slides 2 and 4 and never again; LmrP and ORF8 on slide 19 are not named as proteins. The paper gives a thread for free: ORF8 of SARS-CoV-2 (T1064) is slow in the trunk (slide 19), had a 19-sequence MSA at first (Jumper et al., Proteins 2021, in the background folder), and is the natural case for audience question 2 on slide 28. Name it on 19, use it on 21, point to it on 28.
- A consistent grey subtitle. Three uses now: the fact of slide 6 (slides 10, 13 to 16), the source (11, 12, 23 to 25, backups), a description (7, 9). Rule: the subtitle is the fact wherever a disc is filled, the source always goes to the footnote.
- Fonts: sentences set inside tikz come out sans on text slides (the seven rows of slide 22). Sans is for labels on figures by the deck's own rule; a list of sentences is text.
- Slide 11 and backup 11 are the same figure, slide 24 and backup 10 the same key line, slide 23 and 25 the same 4.4 % row, slide 3 and 26 the same key line. The last is a deliberate bookend and can stay; the others break "nothing twice".

## 3. Slide 22: how to attribute the six works

The right form is a citation column: a right-aligned grey column on the same line as each row, first author et al., venue, year. Reasons: a footnote separates the six claims from their sources and the listener must match them by order, which the back row cannot do; an inline citation at the end of each sentence would zigzag because the rows differ in length; a column keeps claim and source on one line and stays scannable. Volume and pages belong in a reference, not on a slide. The rows, with the citation column:

2021  RoseTTAFold appears online the same day  |  Baek et al., Science 2021
2021  98.5% of human proteins are predicted  |  Tunyasuvunakool et al., Nature 2021
2021  AlphaFold-Multimer predicts complexes  |  Evans et al., bioRxiv 2021
2022  ESMFold uses a language model and no MSA  |  Lin et al., bioRxiv 2022, Science 2023
2024  AlphaFold 3 is one model for proteins, DNA, RNA and ligands  |  Abramson et al., Nature 2024
2024  Baker, Hassabis and Jumper receive the Nobel Prize in Chemistry  |  Royal Swedish Academy of Sciences, 2024
2025  AlphaGenome predicts regulatory activity from a million bases of DNA  |  Avsec et al., bioRxiv 2025

Verified in the repository:
- Baek: Science 373 (6557), 871 to 876, 20 August 2021, CC BY, from the Europe PMC manuscript header. Not verified: its online date of 15 July 2021, which "the same day" rests on; the manuscript prints only the issue date. Jumper's own online date, 15 July 2021, is printed on page 583 and is verified.
- Tunyasuvunakool: Nature 596, 590 to 596, online 22 July 2021, open access; "98.5% of human proteins" is in the abstract. Verified.
- Evans: not in the repository (the README leaves the preprint out for its licence). Nothing verified; AlphaFold-Multimer has, to my knowledge, no journal version, so bioRxiv 2021 is the citation.
- Lin: bioRxiv 10.1101/2022.07.20.500902, version of 21 December 2022, "eliminating the need for a multiple sequence alignment". Verified. The Science 2023 version is not in the repository; the README gives its DOI, so cite both or the journal version alone.
- Abramson: Nature 630, 493 to 500, online 8 May 2024; "In all but one category" on page 493; the exception is CASP15 RNA, where the human-aided AIchemy_RNA2 was better, page 497; 4.4 % chirality violations page 497; 5 seeds times 5 samples, 25 in total, in the Methods. All verified.
- Nobel: the Academy's scientific background of 9 October 2024 names Baker, Hassabis and Jumper. Verified.
- Avsec: not in the repository; the slide-check note rests on a DeepMind web page that also says the work appeared in Nature in January 2026. Nothing verified. If the Nature version exists by the talk, cite "Avsec et al., Nature 2026" and keep the row at 2025 for the preprint, or drop the row: AlphaGenome is not on the spine of this talk.

With the column in place the footnote is free, and the key line can speak for the slide as a whole, for example "Three of the six address the limits of slide 21", or keep the AlphaFold 3 line as the bridge to slide 23.

## 4. Per-slide findings

Skipped: slide 27 (placeholder). No finding: slide 15, backups 4, 7, 8 and 9.

Title (p-02). Low. The paper line is informal and the public deck has no DOI or repository link. Fix: "Jumper et al., Nature 596, 583 to 589 (2021), doi:10.1038/s41586-021-03819-2" and a grey line with the GitHub address.

Slide 1, outline. Low. Seven generic words show nothing of the argument, and the sub-items "The data, The network, in detail" are awkward. Fix: cut the slide; the discs and slide 6 are the map.

Slide 2. Medium. The key line is the least important of the three statements, and the grey caption begins lowercase as a fragment; the panel reappears on slide 4. Fix: key line "Predict the 3D coordinates of every heavy atom from the sequence alone"; caption "A sequence of amino acids. Each has the same backbone and its own side chain."; footnote "Jumper et al. 2021, Fig. 1b".

Slide 3. High. Draft state, see weakness 1. Fix: restore the chart; two text lines; "May to July 2020"; no hyphen as dash.

Slide 4. Medium. Three panels of Fig. 1 without attribution; the left panel is slide 2's figure again. Fix: grey "Jumper et al. 2021, Fig. 1b to d"; drop the repeated panel or merge the slide into slide 3.

Slide 5. Medium. Fig. 1e without attribution; "come out of the network itself" is colloquial. Fix: grey "Jumper et al. 2021, Fig. 1e"; key line "The network outputs the 3D coordinates directly".

Slide 6. Low. The title says "properties", the column says "Fact", and fact 1 is about the input, not the protein. Fix: title "Four facts, four design choices". The key line's forward reference to the ablation is right for a map slide.

Slide 7. Medium. "Everything the network learns is written into these two tables" is imprecise: the network learns weights, the arrays hold the computation, and the single representation and the frames are state too; the subtitle is a description. Fix: key line "Each of the 48 Evoformer blocks reads and writes only these two arrays"; subtitle to the fact or none.

Slide 8. Low. Good slide, and the alignment returns on slide 17, which is the only running example in the deck. Fix, optional: key line "The network reads the raw alignment, not its statistics", which sets up ablation row 1.

Slide 9. Medium. Two fragments ("Started from...", and the key line), a small Fig. 3b named without the paper, a descriptive subtitle, "Pair" capitalised unlike "MSA representation" on slide 8. Fix: merge into slide 7 with one line "128 numbers per ordered pair, started from the two amino acids and their chain distance, clipped at 32"; key line "The pair array stores distances before any coordinates exist".

Slide 10. Medium. Fig. 3a without attribution; "The edges are residues in proximity" is garbled (an edge joins residues). Fix: grey "Jumper et al. 2021, Fig. 3a"; key line "The paper calls this graph inference. An edge joins two residues that are close in space."

Slide 11. High. See weakness 3; also "steer" is a figure of speech and the figure's red boxes are the paper's, not marks. Fix: own drawing; key line "The pairs decide which residues a sequence attends to".

Slide 12. High. See weakness 3; "writes into" is a figure of speech. Fix: own drawing; key line "The outer product mean adds alignment statistics to the pairs in each of the 48 blocks".

Slide 13. Medium. The Fig. 3c row is unattributed while the text cites Fig. 3b; the key line claims an inductive bias that no step enforces (the slide check says so). Fix: grey "Jumper et al. 2021, Fig. 3c"; key line "Each edge is updated from the two edges that close a triangle with it. Nothing enforces the inequality."

Slide 14. Medium. Fig. 3d and 3e without attribution; the Fig. 3d labels are unreadable from the back, the red marks carry it. Fix: grey "Jumper et al. 2021, Fig. 3d, e". The key line is a model: literal and surprising.

Slide 15. None. The best slide of the deck.

Slide 16. Low. "A rotation changes nothing" has no subject, and a flat drawing cannot show the mirror. Fix: "A rotation of the prediction changes nothing."; footnote "the mirror case is on backup 3".

Slide 17. Low. Footnote citations lack venues. Fix: "Xie et al., CVPR 2020. Devlin et al., NAACL 2019."

Slide 18. Low. Red has two meanings: the numbered choices and the two IPA rows, and "No IPA and no recycling" is red without being one of the four. Fix: red only on the numbered rows, or on none; keep the numbers.

Slide 19. Medium. Fig. 4b without attribution; "solved" is vague; LmrP and ORF8 are not named as proteins. Fix: grey "Jumper et al. 2021, Fig. 4b"; labels "LmrP, a bacterial multidrug transporter" and "ORF8 of SARS-CoV-2"; key line "LmrP is correct after about 25 blocks, ORF8 only after about 150". First candidate for the backups if time is short.

Slide 20. High. The only citation names Tunyasuvunakool, so Fig. 2c of Jumper is misattributed; the key line is a norm, not the result shown. Fix: footnote "Jumper et al. 2021, Fig. 2c, n = 10,795 chains. The sentence follows Tunyasuvunakool et al., Nature 2021."; key line "pLDDT predicts the measured lDDT with slope 1.0 and r = 0.76".

Slide 21. Medium. Fig. 5a without attribution; the title and one line promise complexes but no figure shows them; "enough" is vague. Fix: grey "Jumper et al. 2021, Fig. 5a"; key line "Without a template, accuracy falls below about 30 effective sequences"; add Fig. 5b (the 6SK0 trimer) as a small panel or drop "complexes" from the title; name ORF8's 19 sequences as the example.

Slide 22. Medium. Attribution by a first-author footnote, rows in sans on a text slide, AlphaGenome off the spine, key line about one row. Fix: section 3; rows in the serif; key line for the whole slide.

Slide 23. High. The key line is the deck's largest slogan. Fix: "Two of the four choices were dropped. The triangles stayed. 4.4 % of the outputs have the wrong hand."; show slide 24 before this one; merge slide 25 into it as a fourth column.

Slide 24. Medium. "Less structure in the network" is ambiguous in a talk about protein structure; the line is also backup 10's. Fix: "Fewer constraints in the network, more in the data and the sampling."

Slide 25. Medium to high. "paid in patches", "the hand in the loss", "It wins", "The patch" are figures of speech; row 1 repeats slide 23's row 4. Fix: merge into slide 23; key line "AlphaFold 3 is best in every category but CASP15 RNA. Each dropped constraint needed a fix at inference."; column header "The fix".

Slide 26. Low. The key line repeats slide 3's verbatim (a bookend, fine once slide 3 has its chart); the thesis sentence is missing; the licence line belongs here. Fix: key line "Four facts became four design choices. Each costs accuracy when removed. AlphaFold 3 kept one."; footnote adds "Figures reproduced from Jumper et al. 2021 and Abramson et al. 2024, both CC BY 4.0".

Slide 28. Low. "the hand" in question 1 is deck jargon for biologists. Fix: "chirality". Question 1 is the right question for this audience.

Backup 1. Low. The second derivation line runs to the margin. Fix: break after the first equality.

Backup 2. Low. "In group language: SE(3)" is a colon for effect. Fix: "The group is SE(3)."

Backup 3. Low. "FAPE(X, X_mirror) = 2 sum |...|" omits the clamp, the mean and 1/Z, so the equality is loose. Fix: "before clamping and normalisation" or a proportionality sign.

Backup 5. Medium. The key line "Geometry enters only through distances" contradicts the table's own IPA row, where values are moved by T_u^-1 T_v. Fix: "Geometry enters the weights through distances and the values through relative frames." A geometric deep learning reader will read this slide closely.

Backup 6. Low. The only slide without a key line; the table is unreadable from the back, acceptable for a backup.

Backup 10. Low. Same key line as slide 24. Fix: "Tokens, pairformer, diffusion, ranking: the four changes, with the page for each."

Backup 11. Low to medium. The same figure as slide 11, and the key line is a comma splice. Fix: delete once slide 11 has its own drawing.

## 5. The three strongest slides

Slide 15, Invariant point attention. One formula with its three terms named in words, one drawing that shows the invariance by rotating everything, one literal claim, and a footnote that states what the formula omits. A listener can repeat the claim and a reader can check it. This is the Velickovic standard.

Slide 18, Ablations. The paper's Fig. 4a redrawn so that the back row reads the numbers, both target sets kept, the four choices numbered in the deck's own thread, the baseline and the metrics defined in the footnote, and the chirality case placed honestly as a separate line because it comes from a different experiment. The whole argument of the talk is priced on one slide.

Slide 6, Four facts, four design choices. A table that turns the architecture into four testable claims, each with a drawing a biologist can read, and a key line that tells the audience what evidence is coming. Everything after it is a return to this slide, which is what a spine is.
