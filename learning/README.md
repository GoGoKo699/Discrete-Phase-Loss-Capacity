# Learning the phase-loss energy law

How much light is needed to keep a quantum communication rate fixed as the number of possible phase shifts grows? The answer depends on how photon loss scales. At fixed loss, a counted carrier makes exact heralded recovery possible. When loss falls as the alphabet grows, a photon-number residue in the receiver's output gives a different route to reliable communication.

The educational anchor is **Alexander S. Holevo, *Quantum Systems, Channels, Information: A Mathematical Introduction*, second revised and expanded edition (2019)**. The [Holevo bridge](HOLEVO_BRIDGE.md) links the relevant sections on quantum channels, energy constraints and Gaussian systems to the proofs.

## Reading routes

| Starting question | Route |
|---|---|
| How does familiar quantum information lead to this optical problem? | Begin with the [Holevo bridge](HOLEVO_BRIDGE.md#reading-map), including the [three-phase example](HOLEVO_BRIDGE.md#the-optical-model). |
| What are the conceptual dependencies of the whole result? | Follow the [30-milestone map](MILESTONES.md) in order. |
| What happens between zero loss and fixed loss? | Start with the [critical crossover](../science/critical-crossover.md#exact-capacity-in-the-critical-window) and its [two-level example](../science/critical-crossover.md#a-two-level-example). |
| What changes if the mode also undergoes Gaussian displacement? | Use the [critical displacement theorem](../science/critical-displacement.md) and its [binary calculation](../science/critical-displacement.md#binary-check). |
| Where are the precise assumptions and complete proofs? | Use the [scientific overview](../science/README.md) and its topic-based route. |
| Which calculations can I reproduce? | Read the [verification guide](../verification/README.md), then compare its finite checks with the analytic claims they support. |

## Two phases, one scientific story

The map has exactly **30 project-defined milestones**. Each records its central question, understanding target, dependencies, conceptual connection and sources.

**M01–M12: background and preliminaries.** The [first phase](MILESTONES.md#background-and-preliminaries) builds from individual states and photon outcomes to references, entropy, channels, optical loss, phase residues and displacements. It then combines these ingredients with the mean-energy budget and the communication task. These twelve targets establish the common model used by both sides of the theorem.

**M13–M30: narrative and innovation.** The [second phase](MILESTONES.md#narrative-and-innovation) develops the environment-based converse, exact recovery and its uniform energy estimate, then finite-cutoff hashing and fixed-length heralding. It then joins the fixed-loss bounds and compares their energy cost with exact lossless transmission. [M28–M30](MILESTONES.md#m28) derive the receiver's modular loss information and the pure-loss capacity limit, then establish the coherent environment correction in the Gaussian displacement crossover.

The [Holevo bridge](HOLEVO_BRIDGE.md) explains how the textbook tools enter the proof. The [Wilde reading notes](WILDE_BRIDGE.md) provide supplementary quantum Shannon theory.

## Keep the scaling question fixed

The [main theorem](../science/rate_energy.md#theorem-3-fixed-rate-photon-energy) fixes a partial transmissivity and a positive target rate below the pure-loss endpoint while the phase alphabet grows. The required energy is the unconditional mean number of photons entering the channel per use. It includes the carrier and unsuccessful attempts.

The data cutoff, alphabet size and coding length play different roles. A finite data cutoff is chosen to support the target rate; the alphabet size controls the carrier cost; the coding length makes the final error vanish. Keeping these roles separate connects the local recovery calculation to the universal communication statement.

In the [critical crossover](../science/critical-crossover.md), mean input energy divided by alphabet size stays fixed while the loss probability is of order the inverse alphabet size or smaller. At each alphabet size, capacity is defined by taking coding length to infinity first. The final joint limit gives a common curve for unassisted quantum transmission, two-way quantum communication and two-way secret key. The [scope discussion](../science/interpretation.md#boundaries-of-the-result) states the phase and receiver assumptions.

[Repository overview](../README.md) · [Holevo bridge](HOLEVO_BRIDGE.md) · [30 milestones](MILESTONES.md) · [Science](../science/README.md)
