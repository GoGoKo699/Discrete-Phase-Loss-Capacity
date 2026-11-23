# From Holevo to cyclic phase noise, photon loss and displacement

The educational anchor is Alexander S. Holevo, *Quantum Systems, Channels, Information: A Mathematical Introduction*, second revised and expanded edition (De Gruyter, 2019), [DOI 10.1515/9783110642490](https://doi.org/10.1515/9783110642490). The [detailed contents](https://api.pageplace.de/preview/DT0400.9783110642490_A39059069/preview-9783110642490_A39059069.pdf) give the section numbers below. The matching anchor in [Bosonic Noise Dimension](https://github.com/GoGoKo699/Bosonic-Noise-Dimension/blob/main/learning/HOLEVO_BRIDGE.md) follows Gaussian channels into displacement resolution. Here those tools explain why a cyclic phase alphabet changes the capacity of the same oscillator.

## Reading map

| Holevo location | Foundation | Application here |
|---|---|---|
| §§2.2–2.3 and 3.1.1–3.1.3 | States, measurements, partial trace and purification | A Fock measurement counts photons in one mode. An arbitrary-reference input is needed for [the loss converse](../science/converse.md#lemma-1-an-environment-extension-valid-for-every-reference) and [exact recovery](../science/recovery.md#theorem-2-an-exact-success-instrument). |
| §§4.1–4.2, 7.1–7.7 and 11.2 | Shannon entropy, von Neumann entropy and relative entropy | The [mean-energy budget](../science/model.md#entropy-notation) bounds the input entropy. The loss and displacement converses account for distinct kinds of environment information. |
| §§6.2–6.7 | Channel representations, measurements, complements and covariance | An attenuator couples the input to an environment. Averaging cyclic phases preserves a residue subspace, and the channel complement describes what the receiver loses. |
| §§10.3.1–10.3.3 and §10.4.4 | Coding, coherent information and degradability | A [fixed-residue code](../science/critical-crossover.md#the-finite-alphabet-bound) gives the direct rate. The flagged [displacement extension](../science/critical-displacement.md#exact-finite-channel-comparison) uses degradability to explain why a single conditional entropy is relevant. |
| §§11.2, 11.5 and 11.7 | Constrained quantum systems and entanglement-breaking channels | The constrained protocols use unconditional mean photon number. Dephasing the flagged receiver output is a measure-and-prepare channel, the comparator used in the adaptive upper bound. |
| §§12.2, 12.4.1–12.4.2 and 12.6.2–12.6.4 | Weyl displacements, one-mode Gaussian channels and their parameters | One displacement provides a counted carrier in the [fixed-loss construction](../science/recovery.md#finite-data-and-a-counted-carrier). Random Gaussian displacements instead alter the [critical capacity](../science/critical-displacement.md#channel-and-critical-capacity). |

## The optical model

For three uniformly chosen phases, the numbers zero and three acquire the same phase. The state $`a|0\rangle+b|3\rangle`$ therefore survives the phase averaging. Its mean input energy is $`3|b|^2`$ photons. If a photon is lost, the environment knows the input could only have been the three-photon component. The cyclic symmetry and the loss observation protect and reveal different parts of the same encoding.

The [channel model](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet) gives its Kraus operators and the energy convention. A transmitted carrier, a failed heralding attempt and any idle use each enter the budget. Works on squashed entanglement and energy-constrained coding supply the research theorems that turn these one-mode calculations into statements about arbitrary protocols. [Converse and imported theorem](../science/converse.md#squashed-entanglement-and-the-imported-capacity-theorem)

## The carrier and the residue

At fixed loss, a bright displacement separates phase branches. The [receiver's success instrument](../science/recovery.md#theorem-2-an-exact-success-instrument) uses an exact left inverse on the full finite data subspace, preserving its entanglement with a reference. Its uniformly bounded success probability allows a fixed-length protocol with reverse hashing. The input energy of the carrier is quadratic in alphabet size. [Matched rate and energy theorem](../science/rate_energy.md#theorem-3-fixed-rate-photon-energy)

When loss instead shrinks inversely with alphabet size, the input is scheduled in known residue classes. Bob learns the lost count modulo the alphabet size by measuring only the output residue. The entropy of the missing quotient vanishes at linear input energy. The [pure-loss crossover](../science/critical-crossover.md#exact-capacity-in-the-critical-window) then reduces to conditioning on a Poisson loss count.

With weak Gaussian displacement, attenuation followed by amplification yields both photon loss and gain. Their difference is Bob's shift, available modulo the alphabet size. In a fixed shift, the environmental state retains coherent combinations of different loss and gain counts. The [joint theorem](../science/critical-displacement.md) bounds the physical rate by giving Bob the exact shift as an aid to the converse, then controls the cost of removing that aid. The [binary example](../science/critical-displacement.md#binary-check) lets you compute the environment correction directly from a two-state Gram matrix.

[Learning overview](README.md) · [30 milestones](MILESTONES.md) · [Supplementary Wilde readings](WILDE_BRIDGE.md)
