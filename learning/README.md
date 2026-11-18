# Learning the phase-loss energy law

How much light is needed to keep a quantum communication rate fixed as the number of possible phase shifts grows? The answer depends on how photon loss scales. At fixed loss, a counted carrier makes exact heralded recovery possible. When loss falls as the alphabet grows, a photon-number residue in the receiver's output gives a different route to reliable communication.

The single educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition, Cambridge University Press (2017)**. The [source bridge](WILDE_BRIDGE.md) identifies relevant sections, translates notation and supplies the optical and energy-constrained steps needed here. Its [bibliographic entry](../references/REFERENCES.md#wilde2017) distinguishes the selected edition from the freely available corrected author version.

## Reading routes

| Starting question | Route |
|---|---|
| How does familiar quantum information lead to this optical problem? | Begin with the [Wilde bridge](WILDE_BRIDGE.md#reading-map), including the [three-phase example](WILDE_BRIDGE.md#the-optical-model). |
| What are the conceptual dependencies of the whole result? | Follow the [30-milestone map](MILESTONES.md) in order. |
| What happens between zero loss and fixed loss? | Start with the [critical crossover](../science/critical-crossover.md#exact-capacity-in-the-critical-window) and its [two-level example](../science/critical-crossover.md#a-two-level-example). |
| Where are the precise assumptions and complete proofs? | Use the [scientific overview](../science/README.md) and its topic-based route. |
| Which calculations can I reproduce? | Read the [verification guide](../verification/README.md), then compare its finite checks with the analytic claims they support. |

## Two phases, one scientific story

The map has exactly **30 project-defined milestones**. Each records its central question, understanding target, dependencies, conceptual connection and sources.

**M01–M12: background and preliminaries.** The [first phase](MILESTONES.md#background-and-preliminaries) builds from individual states and photon outcomes to references, entropy, channels, optical loss, phase residues and displacements. It then combines these ingredients with the mean-energy budget and the communication task. These twelve targets establish the common model used by both sides of the theorem.

**M13–M30: narrative and innovation.** The [second phase](MILESTONES.md#narrative-and-innovation) develops the environment-based converse, exact recovery and its uniform energy estimate, then finite-cutoff hashing and fixed-length heralding. It then joins the fixed-loss bounds and compares their energy cost with exact lossless transmission. [M28–M30](MILESTONES.md#m28) complete the story by deriving the receiver's modular loss information, taking the joint loss and alphabet limit, and working through a two-level example.

The milestones are an understanding map, not a replacement for the full proofs. Specialist details remain in the scientific pages, while the [bridge](WILDE_BRIDGE.md) explains the transitions between textbook tools and those arguments.

## Keep the scaling question fixed

The [main theorem](../science/rate_energy.md#theorem-3-fixed-rate-photon-energy) fixes a partial transmissivity and a positive target rate below the pure-loss endpoint while the phase alphabet grows. The required energy is the unconditional mean number of photons entering the channel per use. It includes the carrier and unsuccessful attempts.

The data cutoff, alphabet size and coding length play different roles. A finite data cutoff is chosen to support the target rate; the alphabet size controls the carrier cost; the coding length makes the final error vanish. Keeping these roles separate connects the local recovery calculation to the universal communication statement.

In the [critical crossover](../science/critical-crossover.md), the mean photon budget per phase stays fixed while the loss probability falls inversely with the alphabet size. At each alphabet size, capacity is defined by taking coding length to infinity first. The final joint limit gives a common curve for unassisted quantum transmission, two-way quantum communication and two-way secret key. The [scope discussion](../science/interpretation.md#boundaries-of-the-result) states the phase and receiver assumptions.

[Repository overview](../README.md) · [Wilde bridge](WILDE_BRIDGE.md) · [30 milestones](MILESTONES.md) · [Science](../science/README.md)
