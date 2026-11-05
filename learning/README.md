# Learning the phase-loss energy law

The central question is how much light is needed to keep a quantum communication rate fixed when the number of possible unknown phases grows. The project connects three ideas: phase protection in photon-number residues, information carried away by lost photons, and a counted carrier that makes exact heralded recovery possible.

The single educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition, Cambridge University Press (2017)**. The [source bridge](WILDE_BRIDGE.md) identifies relevant sections, translates notation and supplies the optical and energy-constrained steps needed here. Its [bibliographic entry](../references/REFERENCES.md#wilde2017) distinguishes the selected edition from the freely available corrected author version.

## Reading routes

| Starting question | Route |
|---|---|
| How does familiar quantum information lead to this optical problem? | Begin with the [Wilde bridge](WILDE_BRIDGE.md#reading-map), including the [three-phase example](WILDE_BRIDGE.md#the-optical-model). |
| What are the conceptual dependencies of the whole result? | Follow the [30-milestone map](MILESTONES.md) in order. |
| Where are the precise assumptions and complete proofs? | Use the [scientific overview](../science/README.md) and its topic-based route. |
| Which calculations can I reproduce? | Read the [verification guide](../verification/README.md), then compare its finite checks with the analytic claims they support. |

## Two phases, one scientific story

The map has exactly **30 project-defined milestones**. Each records its central question, understanding target, dependencies, conceptual connection and sources.

**M01–M12: background and preliminaries.** The [first phase](MILESTONES.md#background-and-preliminaries) builds from individual states and photon outcomes to references, entropy, channels, optical loss, phase residues and displacements. It then combines these ingredients with the mean-energy budget and the communication task. These twelve targets establish the common model used by both sides of the theorem.

**M13–M30: narrative and innovation.** The [second phase](MILESTONES.md#narrative-and-innovation) develops the environment-based converse, exact recovery and its uniform energy estimate, then finite-cutoff hashing and fixed-length heralding. It ends by joining the bounds, the lossless comparison, limiting cases, numerical evidence and physical scope. Eighteen targets are allocated here because the upper and lower energy bounds use different mechanisms that must ultimately obey the same resource accounting.

The milestones are an understanding map, not a replacement for the full proofs. Specialist details remain in the scientific pages, while the [bridge](WILDE_BRIDGE.md) explains the transitions between textbook tools and those arguments.

## Keep the scaling question fixed

The [main theorem](../science/rate_energy.md#theorem-3-fixed-rate-photon-energy) fixes a partial transmissivity and a positive target rate below the pure-loss endpoint while the phase alphabet grows. The required energy is the unconditional mean number of photons entering the channel per use. It includes the carrier and unsuccessful attempts.

The data cutoff, alphabet size and coding length play different roles. A finite data cutoff is chosen to support the target rate; the alphabet size controls the carrier cost; the coding length makes the final error vanish. Keeping these roles separate connects the local recovery calculation to the universal communication statement. The [scope discussion](../science/interpretation.md#boundaries-of-the-result) states the exact phase-alphabet and receiver assumptions.

[Repository overview](../README.md) · [Wilde bridge](WILDE_BRIDGE.md) · [30 milestones](MILESTONES.md) · [Science](../science/README.md)
