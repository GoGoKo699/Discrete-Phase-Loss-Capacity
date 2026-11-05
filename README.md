# Discrete Phase Noise and Photon Loss

**How much light is needed to maintain a fixed quantum communication rate when the phase takes one of many unknown discrete values?** For an optical mode with independently redrawn cyclic phase noise, fixed partial photon loss changes the required mean input energy from linear to quadratic in the number of possible phases.

Let $`J`$ equally spaced phase shifts be equally likely on each channel use, and let $`\eta`$ be the photon transmissivity. The energy $`E`$ is the unconditional mean number of input photons per use, including the carrier and failed attempts. Arbitrary local operations and public two-way classical communication are allowed.

| Channel | Energy needed for a fixed positive rate |
|---|---|
| Cyclic phase noise without photon loss | $`\Theta_R(J)`$ |
| Cyclic phase noise with fixed $`0\lt\eta\lt1`$ | $`\Theta_{\eta,R}(J^2)`$ |

The lossy statement holds for both two-way entanglement generation and secret-key agreement, at every fixed rate

```math
0\lt R\lt C_\eta,
\qquad C_\eta=-\log_2(1-\eta).
```

The endpoint $`C_\eta`$ is the established unconstrained two-way capacity of pure loss. The contribution here is the matching energy requirement in the presence of a growing cyclic phase alphabet. [Exact model and claims](science/model.md) · [Rate–energy theorem](science/rate_energy.md)

## Why the energy is quadratic

Photon loss leaves the environment with a noisy estimate of the input photon number. Together with its residue modulo $`J`$, that estimate sharply limits the entanglement that can remain. A conditional-entropy argument gives an upper bound for every encoding, including adaptive protocols and photon distributions with finite mean but infinite variance.

For achievability, a bright displacement separates the finitely many rotated data subspaces. A heralded recovery identifies a phase branch while preserving the unknown quantum data. A carrier amplitude proportional to $`J`$ keeps the success probability bounded uniformly in $`J`$, and its photon energy is proportional to $`J^2`$. Reverse hashing of the accepted states attains any fixed rate below $`C_\eta`$.

The two sides use the same unconditional energy budget. Every failed recovery and every idle use enters the accounting.

## Read the science

Start with the [scientific overview](science/README.md), then follow the route matching your question.

| Question | Authoritative account |
|---|---|
| What channel, resources and capacity notion are fixed? | [Model and statements](science/model.md) |
| Why can arbitrary encodings and rare bright pulses not improve the energy order? | [Converse](science/converse.md) |
| How can recovery distinguish phase branches without measuring the data? | [Exact recovery construction](science/recovery.md) |
| How do the bounds give matching rates, the lossless benchmark and the infinite-energy limit? | [Rate and energy](science/rate_energy.md) |
| What is the physical meaning, and which limits do not commute? | [Interpretation](science/interpretation.md) |
| Which results and techniques are inherited? | [Related work](references/RELATED_WORK.md) and [references](references/REFERENCES.md) |
| What can be reproduced numerically? | [Verification guide](verification/README.md) |

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_theorem.py
```

The deterministic suite checks the conditional-entropy calculations, arbitrary-reference branches, displacement matrix elements, the recovery map and a concrete rate–energy construction. [Saved results](verification/results.json) record the inputs, tolerances and outputs. These finite checks support the implementation; the all-input and asymptotic statements follow from the proofs.

## Scope

The phase alphabet is known and exactly discrete, while the realized phase is hidden and independently redrawn on every use. There is no additional transmitted reference mode or initial shared entanglement. The receiver may implement arbitrary quantum operations. The recovery proof does not establish efficient hardware implementation or robustness to continuously broadened phase errors.

The energy law concerns fixed rates and fixed transmissivity. It is not uniform in a simultaneous lossless limit, and it does not determine the exact finite-energy capacity curve. For every finite cyclic alphabet, positive transmissivity and positive energy budget, the two-way rate remains positive; the theorem determines the energy needed to keep that rate fixed as the alphabet grows.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
