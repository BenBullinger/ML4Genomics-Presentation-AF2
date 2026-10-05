# Speaker notes for the AlphaFold 2 talk

The talk has 30 minutes, the title slide and 18 numbered slides. Each section below gives what to say on one slide. The sources for the statements are in `background/SLIDE-CHECK.md`. Lines in italics are directions, not speech.

`SCREENPLAY.txt` is the same text as plain text, written the way it is spoken, for rehearsing by reading or with a text-to-speech app. `python3 make_screenplay.py` writes it from this file, so edit this file only.

**Handover after slide 9.** The first speaker takes the title and slides 1 to 9 (14.5 minutes): the problem, the input and the network up to the structure module. The second speaker takes slides 10 to 18 (15.5 minutes): the two slides on frames, the training, the analysis and what followed.

**Length.** The text has about 3,120 words. Read aloud at 130 words per minute it takes about 24 minutes. The remaining 6 minutes are for pointing at the figures and for pauses. This is tight. It grew because a listener who had not read the paper needed a sentence of explanation for many terms. The section "What could be cut" at the end lists what to drop first.

**Words.** The notes use one word for one thing: "experimental structure" for a structure determined in the laboratory, "MSA" for the alignment, "network" for AlphaFold's neural network, "block" for one of the 48 Evoformer blocks or 8 structure-module blocks, "layer" for a part of a block.

| Slide | Title | Minutes | Ends at |
|---|---|---|---|
| title, 1 | Title and outline | 0.5 | 0:30 |
| 2 | Sequence in, structure out | 1.5 | 2:00 |
| 3 | CASP14: atomic accuracy, alone | 2 | 4:00 |
| 4 | Predictions on top of experiment | 1 | 5:00 |
| 5 | The input: a multiple sequence alignment (MSA) | 2 | 7:00 |
| 6 | One pipeline, end to end | 2 | 9:00 |
| 7 | The Evoformer block | 1.5 | 10:30 |
| 8 | Pairs updated through triangles | 2 | 12:30 |
| 9 | The structure module: residues as rigid bodies | 2 | 14:30 |
| 10 | Invariant point attention | 2.5 | 17:00 |
| 11 | FAPE: a loss over local frames | 2 | 19:00 |
| 12 | Trained beyond the PDB | 1.5 | 20:30 |
| 13 | Which pieces earn their accuracy | 2.5 | 23:00 |
| 14 | The structure forms inside the trunk | 1.5 | 24:30 |
| 15 | The model knows when it is right | 1.5 | 26:00 |
| 16 | Where it still fails | 1.5 | 27:30 |
| 17 | What followed | 1.5 | 29:00 |
| 18 | Summary | 1 | 30:00 |

## Title

We present the paper "Highly accurate protein structure prediction with AlphaFold" by John Jumper and co-authors, most of them at DeepMind. It was published in Nature in 2021. It describes the second version of AlphaFold, usually called AlphaFold 2. When we say AlphaFold, we mean this version.

## Slide 1: Outline

The talk has five parts: the problem, the network, the training, what makes it work, and the conclusion, which includes what came after the paper.

## Slide 2: Sequence in, structure out

*Point at the row of letters.*

A protein is a chain of amino acids. The letters on the slide are such a chain: each letter stands for one of 20 amino acids. One amino acid in the chain is called a residue. All residues have a common part, and these parts form the backbone of the chain. The part that differs between the 20 amino acids is called the side chain.

In the cell the chain folds into a 3D structure, and knowing the structure helps to understand what the protein does. The task is to compute the 3D coordinates of all atoms except hydrogen from the sequence. The slide calls them heavy atoms.

Determining one structure by experiment takes months to years. The structures of about 100,000 different proteins have been determined, but billions of sequences are known. The problem has been open for more than 50 years.

Progress is measured in CASP, the Critical Assessment of protein Structure Prediction, held every two years. The participants predict structures that have been determined but not yet published. So CASP is a blind test.

## Slide 3: CASP14: atomic accuracy, alone

*Point at the dark bar at the left.*

This is the result of CASP14, held in 2020. Each bar is one participating group. The figure shows the best 15 of 146. AlphaFold is the dark bar.

The height of a bar is the median error of that group over 87 domains. A domain is a part of a chain that folds into a compact unit. CASP scores domains separately. The error is given in ångström. One ångström is a tenth of a nanometre, about the size of an atom.

The error is computed like this. Take one backbone atom per residue, the Cα atom. Place the prediction on the experimental structure so that these atoms fit as well as possible. Leave out the 5 percent of the residues that fit worst. The root-mean-square distance of the rest is the error. Lower is better.

AlphaFold has a median error of 0.96 ångström. The next best group has 2.8. A carbon atom is about 1.4 ångström wide. So the typical error of AlphaFold is smaller than the width of a carbon atom.

## Slide 4: Predictions on top of experiment

Three predictions, each in blue, on top of the experimental structure in green.

On the left one domain. The backbone error is 0.8 ångström.

In the middle the side chains around a zinc ion, the grey sphere. The ion is not part of the network's output, and still the side chains that hold it are placed correctly.

On the right a single chain of 2,180 residues with several domains. AlphaFold placed the domains correctly relative to each other. The paper stresses that this prediction was made without manual intervention.

## Slide 5: The input: a multiple sequence alignment (MSA)

Now the network, starting with its input. The input is not only the sequence of the target protein. A database search finds evolutionarily related proteins. They descend from a common ancestor: their sequences differ, but they fold into nearly the same structure. One of the databases, BFD, contains over 2 billion sequences.

The related sequences are written below the target and lined up, so that positions that correspond to each other stand in the same column. A dash marks a position that one sequence lacks. This table is called a multiple sequence alignment, MSA. The drawing is a made-up example with six rows. A real MSA can have thousands of rows.

*Point at the two shaded columns and at the arc above them.*

Why does it help? Residues that touch in the structure may change together during evolution, because their interaction has to stay favourable. In the drawing, columns 3 and 9 always hold one positively and one negatively charged amino acid. In the first three rows the positive one is in column 3, in the last three rows in column 9. Marks and colleagues showed in 2011 that such pairs of columns can suffice to compute the fold of a protein.

Many earlier methods gave their network only statistics of the MSA. AlphaFold also gives it the aligned sequences themselves.

## Slide 6: One pipeline, end to end

*Point at the inputs on the left.*

This is the whole system. On the left are the inputs: the target sequence, the MSA, and templates. Templates are known structures of related proteins, at most four.

The network keeps two arrays. The MSA representation has one vector for every sequence and every residue. The pair representation has one vector for every pair of residues. It holds what the network knows about the relation between the two residues, for example their distance. The letters in brackets are the array shapes: s sequences, r residues, c channels.

*Point at the Evoformer box, then at the structure module box.*

The Evoformer, a stack of 48 blocks, updates both arrays. The paper calls this part the trunk. Then the structure module computes 3D coordinates. It uses the pair representation and the first row of the MSA representation, which belongs to the target. The figure calls this row the single representation.

*Point at the recycling arrow at the bottom.*

After that, three outputs are fed back as additional inputs: the pair representation, the first MSA row and the predicted structure. The network runs again with the same weights. This is called recycling. It is done three times, so the network runs four times in total.

The database searches happen before. Everything after them is one network, trained end to end.

## Slide 7: The Evoformer block

This is one of the 48 blocks. The upper row updates the MSA representation, the lower row the pair representation.

The upper row has two attention layers. The first attends along one sequence, across its residues. The second attends along one column, across the sequences. The boxes labelled "transition" are small feed-forward layers.

*Point at the arrow from the pair representation up into the first box, then at the box "outer product mean".*

The two representations exchange information in both directions. From pair to MSA: when residue i attends to residue j in the first layer, the pair vector of i and j is added as a bias. From MSA to pair: for each sequence, the block takes its vectors at columns i and j and forms their outer product. The average over all sequences is added to the pair vector of i and j. Such an average measures how two columns vary together.

The lower row has four triangle layers, which the next slide explains. Each of the 48 blocks has its own weights.

## Slide 8: Pairs updated through triangles

Think of the residues as nodes of a graph. The pair vector of i and j is an edge from i to j. The edges are directed: the vector for i j differs from the one for j i.

If the pair vectors are to describe one real 3D structure, they must be consistent. For example, the distances between three residues must satisfy the triangle inequality. So each of the four triangle layers updates edge i j from the two other edges of every triangle i, j, k. In each drawing, i j is the edge that is updated.

*Point at the first two drawings.*

The first two layers multiply the two other edges and sum over all k. The first uses the edges that leave i and j towards k, the second the edges that arrive at i and j from k. That is the difference between "outgoing" and "incoming".

*Point at the last two drawings.*

The last two layers use attention. In the third, edge i j attends to all edges that start at node i, and the third edge of the triangle, j k, adds a bias to the attention weight. The fourth does the same for the edges that end at node j.

The network does not enforce the triangle inequality. The paper's supplementary text calls the design an inductive bias.

## Slide 9: The structure module: residues as rigid bodies

The structure module computes the coordinates. It represents the backbone of every residue as a rigid body, given by one rotation and one translation. Together they are called the frame of the residue. The frame fixes the positions of the backbone atoms N, Cα and C. The paper calls this set of independent frames a residue gas.

*Point at the frames at the bottom, then at the box labelled IPA.*

At the start all frames sit at the origin. The module has 8 blocks with shared weights. Each block first updates the single representation by an attention layer, the box labelled IPA, which the next slide explains. Then it predicts a change of every frame. The side chains are added from torsion angles, which are rotations around the bonds of the side chain. The figure calls them chi angles.

All residues move at the same time, and nothing in the module forces neighbouring residues to stay connected. The authors chose this so that all parts of the chain can be refined at once. Correct bonds between neighbours are enforced only at the very end, by an energy minimization with a physical force field, outside the network.

*Handover to the second speaker.*

## Slide 10: Invariant point attention

The attention layer inside the structure module is called invariant point attention. The formula gives the weight with which residue i attends to residue j. We left out the scaling constants.

*Point at the first two terms.*

The first term is the usual one: q i and k j are a query and a key vector, computed from the single representation. The second term, b i j, is a bias computed from the pair vector of i and j.

*Point at the sum.*

The third term is new. Every residue also produces four query points and four key points in 3D. These are the letters with an arrow. The residue produces them in the coordinates of its own frame. T i with the small circle means: apply the frame of residue i. This moves the points into the common, global coordinate system. The term sums, over the four points p, the squared distance between a point of i and a point of j. It enters with a minus sign: the further apart the points, the lower the weight.

Why this construction? The orientation of a protein in space is arbitrary, so the result should not depend on it. If we rotate or shift all frames together, the points move with them, the distances stay the same, and so do the weights. This is the invariance in the name.

The change of each frame is then predicted in that residue's own coordinates. If all frames are rotated together before a block, the updated frames come out rotated in the same way. This is called equivariance.

## Slide 11: FAPE: a loss over local frames

How is a predicted structure compared with the experimental one? The loss is called frame aligned point error, FAPE. In the formula, "true" marks the experimental structure, k counts frames and i counts atoms.

*Point at the two halves of the difference in the formula.*

Take one frame and one atom. Write the position of the atom in the coordinates of that frame, once in the prediction and once in the experimental structure. Take the distance between the two positions. FAPE is the mean of this distance over all frames and all atoms. The frames are the backbone frame of every residue and frames for the parts of its side chain. Distances are cut off at 10 ångström, the d clamp on the slide. Z, also 10 ångström, makes the loss unitless.

Only positions relative to frames enter. So the loss does not change if the predicted structure is rotated or shifted as a whole.

It does change if the structure is mirrored, because a frame is a right-handed coordinate system and the mirrored atoms lie at mirrored positions inside it. This matters: a protein and its mirror image are different molecules. The slide calls this property chirality. The authors tested it. A network trained with a loss on distances between atoms, which are the same in a mirror image, frequently produced mirror images.

## Slide 12: Trained beyond the PDB

Now the training. The training data are structures from the Protein Data Bank, PDB, the public archive of experimental structures, released up to April 2018. Two techniques add information from sequences without an experimental structure.

The first is self-distillation. A trained network predicts structures for about 350,000 sequences from the database Uniclust. A new network is then trained from scratch on three quarters predicted and one quarter experimental structures. It sees each of these sequences with a reduced MSA and only a part of the chain, but it must reproduce the structure that the first network predicted from the full input. Residues where the first network was not confident are left out of the loss.

The second is a masked-MSA loss as in BERT. Some entries of the MSA are hidden, and the network must predict them. The authors write that this encourages the network to learn which columns vary together. This loss is trained together with FAPE. There is no pre-training.

## Slide 13: Which pieces earn their accuracy

Which components matter? The authors removed one component at a time and trained the network again. Each row is one such experiment. The points are three training runs with their 95 percent intervals. The baseline at zero is the network without self-distillation, and the top row adds it.

Both panels show the change of an accuracy score between 0 and 100. Left of the grey line means worse. The left panel uses GDT on the CASP14 domains. GDT is the score of CASP: roughly the percentage of Cα atoms that lie close to their experimental position. The right panel uses the score lDDT-Cα on about 2,300 recent PDB chains. That score compares distances between nearby residues, and slide 15 comes back to it.

*Point at each row as you name it.*

Some rows. Giving the network only statistics of the MSA, the row "No raw MSA", costs about 2 points on CASP14. Removing recycling costs about 4.5. Replacing the triangle layers by ordinary attention, which also removes the pair bias and the gating, costs about 4.5. Stopping the gradient of FAPE before the Evoformer costs about 6.

*Point at the row "No IPA", then at the bottom row.*

Now the row "No IPA". Without invariant point attention the network has no equivariant part left. This costs about 2 points on CASP14 and almost nothing on the PDB chains. The authors conclude that equivariance is not essential. But removing IPA and recycling together costs 16 points, far more than the sum. The authors explain this by components whose roles overlap.

Their overall conclusion: many components contribute.

## Slide 14: The structure forms inside the trunk

Where in the network does the structure appear? The authors froze the trained network. Then they trained a separate structure module on the output of each of the 48 Evoformer blocks. The network runs four times, which gives 192 intermediate structures for one protein. On the axis, 48, 96 and 144 mark the ends of the first three runs.

*Point at the blue and the orange curve, then at the green curve.*

The plot shows the GDT of these structures for two CASP14 targets. T1024 is the protein LmrP. It has two domains, hence two curves, blue and orange. Both are nearly correct within the first run. T1064 is ORF8 of the coronavirus SARS-CoV-2, the green curve. After the first run it is at about 35, and it keeps rising until the end of the fourth.

So the structure appears inside the Evoformer stack, early for some proteins and late for others. ORF8 was hard: during CASP14 its MSA at first had only 19 sequences. Slide 16 shows why that matters.

## Slide 15: The model knows when it is right

The network also predicts how accurate it is. For every residue it outputs a number between 0 and 100 called pLDDT, the predicted lDDT. lDDT stands for local distance difference test. For one residue it is, roughly, the percentage of its distances to nearby atoms that agree with the experimental structure.

*Point at the left plot, then at the label of its horizontal axis.*

The plot compares the predicted score with the true score for about 10,800 recent PDB chains, each averaged over the chain. The x-axis says "resolved region". That is the part of a chain that is visible in the experiment. The fitted line has a slope of almost exactly one, so on average the predicted score matches the true one. The correlation is 0.76.

The highlighted sentence comes from a companion paper. There the same group predicted structures for nearly all human proteins, the human proteome. They write that such predictions are only practically useful with a well-calibrated confidence.

## Slide 16: Where it still fails

The paper names two limits.

*Point at the blue curve where it falls, at the left.*

The first is the MSA. The plot shows the accuracy against the number of effective sequences in the MSA, written N eff. In this count, very similar sequences are weighted down. The axis is logarithmic. The two curves separate the proteins by how much of the chain is covered by templates. The blue curve is for proteins with little template coverage. The accuracy falls once the MSA has fewer than about 30 effective sequences, and above about 100 more sequences add little.

The second limit concerns chains inside a complex of several chains. If the shape of a chain is determined mainly by its contacts with other chains, AlphaFold is much weaker. It was trained on single chains. The authors expect that a system that predicts whole complexes will remove this difficulty.

Later work adds a third limit. A prediction does not account for ligands, which are small molecules bound to the protein, or for other effects of the environment.

## Slide 17: What followed

What came after? On the day the paper appeared online, David Baker's group published RoseTTAFold, a network with three tracks: for the sequence, for residue pairs and for 3D coordinates. One week later the AlphaFold team published predictions for 98.5 percent of human proteins.

The next three entries address the three limits of the previous slide. AlphaFold-Multimer, first posted in October 2021, is trained on complexes of several chains. ESMFold, from 2022, replaces the MSA by a protein language model. It is faster and less accurate than AlphaFold 2. AlphaFold 3, from 2024, also predicts complexes with small molecules, DNA and RNA. These are the ligands and nucleic acids on the slide.

AlphaFold 3 generates the coordinates by diffusion. It predicts the structure without frames and without equivariance. This fits the row "No IPA" on slide 13.

In 2024 Demis Hassabis and John Jumper received the Nobel Prize in Chemistry, together with David Baker.

## Slide 18: Summary

To summarize. In CASP14 the typical backbone error of AlphaFold 2 was below one ångström.

The network combines the evolutionary information in the MSA with components built for 3D geometry: the triangle layers, the frames of the structure module, and the FAPE loss. It is trained end to end and applied four times in a row.

One run takes about one GPU minute for 384 residues, and five trained networks are run per protein. Every prediction comes with a confidence for each residue.

The limits: it needs enough related sequences, and it was trained on single chains. Later work showed that not all of its geometric components are necessary.

Thank you. We are happy to take questions.

## What could be cut

If the talk runs long in rehearsal, drop these first. Each is a whole point, so nothing else depends on it. Together they save about 2 minutes.

1. Slide 4: skip "The paper stresses that this prediction was made without manual intervention."
2. Slide 11: skip the sentence on the side-chain frames and the sentence on Z.
3. Slide 12: skip the sentence that begins "It sees each of these sequences".
4. Slide 13: skip the row "No raw MSA".
5. Slide 14: skip the sentence on the axis marks 48, 96 and 144.
6. Slide 15: skip the two sentences on the "resolved region".
7. Slide 16: skip the third limit. Then say "two limits" on slide 17 and name only AlphaFold-Multimer and ESMFold in that sentence.
8. Slide 8: replace the two paragraphs on the four layers by "Two layers do this by multiplying the two other edges, two layers by attention."
