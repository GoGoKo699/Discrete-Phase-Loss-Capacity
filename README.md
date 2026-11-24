# Discrete Phase Noise and Photon Loss

**How much light is needed to communicate quantum information through an unknown optical phase?** For an optical mode with independently redrawn cyclic phase noise, fixed partial photon loss changes the required mean input energy from linear to quadratic in the number of possible phases. When the loss probability shrinks inversely with the alphabet size, an exact limiting capacity describes the crossover.

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

## Capacity when photon loss shrinks

Let $`q_J=1-\eta_J`$ be the loss probability. When $`Jq_J\to\lambda`$ and $`E=eJ`$, the unassisted quantum, two-way quantum and two-way secret-key capacities share a limit. Write the input photon number as a multiple of the alphabet size plus a residue. In the limit, $`U`$ is the integer quotient, $`A`$ is the residue divided by $`J`$, and the environment's loss count $`L`$ is Poisson:

```math
F_\lambda(e)=\sup_{\mathbb E[A+U]\le e} H(U\mid L,A),
\qquad L\mid (A,U)\sim\mathrm{Pois}\!\left(\lambda(A+U)\right).
```

The receiver can infer the loss count modulo the alphabet size from the received number residue. This leaves an ambiguity with entropy at most $`g(q_J E/J)`$, which vanishes in this regime. The achievability code schedules its input residues in advance and uses the transmitted mode itself. [Proof and two-level example](science/critical-crossover.md)

## What changes under weak Gaussian displacement

Independent displacement of variance of order $`1/J`$ preserves a positive rate at linear energy and changes the limiting capacity. Bob can infer the net photon-number shift up to a vanishing ambiguity. Within the environment, different loss and gain histories that give the same shift can still carry information about the input. Accounting for these coherent histories yields one limiting capacity for unassisted quantum communication, two-way entanglement generation and two-way secret key. The optimized rate is strictly below the prediction obtained from the shift alone.

[Critical displacement theorem](science/critical-displacement.md) · [Companion analysis in Bosonic Noise Dimension](https://github.com/GoGoKo699/Bosonic-Noise-Dimension/blob/main/science/07-cyclic-phase.md)

## When the phase angles have jitter

Add an independent residual rotation to each nominal cyclic phase. The relevant angular law is the distribution of the residual angle multiplied by $`J`$ and reduced modulo $`2\pi`$. At fixed photon loss and an unconditional budget of $`eJ^2`$ photons per use, a nonuniform limiting law preserves a positive two-way quantum and secret-key rate. A uniform limiting law drives both rates to zero. The receiver uses a surviving Fourier harmonic to choose a pair of Fock levels and accepts a band of typical photon losses.

A harmonic that moves to higher order can preserve the phase-only capacity while pushing the required energy in the lossy channel above the quadratic scale. With loss and Gaussian displacement at the inverse-alphabet scale, a phase tag in the environment gives an exact common capacity limit at linear energy. [Phase-jitter theorems](science/phase-jitter.md)

## Read the science

Start with the [scientific overview](science/README.md), then follow the route matching your question.

| Question | Authoritative account |
|---|---|
| What channel, resources and capacity notion are fixed? | [Model and statements](science/model.md) |
| Why can arbitrary encodings and rare bright pulses not improve the energy order? | [Converse](science/converse.md) |
| How can recovery distinguish phase branches without measuring the data? | [Exact recovery construction](science/recovery.md) |
| How do the bounds give matching rates, the lossless benchmark and the infinite-energy limit? | [Rate and energy](science/rate_energy.md) |
| When does unassisted quantum communication reach the two-way limit? | [Critical photon-loss crossover](science/critical-crossover.md) |
| Why can channels with the same photon-number transitions have different capacities? | [Critical displacement](science/critical-displacement.md) |
| Which residual phase laws support communication after loss? | [Phase jitter and surviving harmonics](science/phase-jitter.md) |
| What is the physical meaning, and which limits do not commute? | [Interpretation](science/interpretation.md) |
| Which results and techniques are inherited? | [Related work](references/RELATED_WORK.md) and [references](references/REFERENCES.md) |
| What can be reproduced numerically? | [Verification guide](verification/README.md) |

## Learn the project

The [learning route](learning/README.md) follows Alexander S. Holevo's *Quantum Systems, Channels, Information*, second revised and expanded edition (2019). The [Holevo bridge](learning/HOLEVO_BRIDGE.md) connects the textbook to the photon budget, the optical channels and the capacity proof. The [30-milestone map](learning/MILESTONES.md) develops the communication-energy theorem, the critical limits and the role of phase harmonics.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_theorem.py
python3 verification/check_critical_displacement.py
python3 verification/check_phase_jitter.py
```

The deterministic suite checks the conditional-entropy calculations, arbitrary-reference branches, displacement matrix elements, the heralded recovery and the finite-alphabet loss-count calculation. The displacement check reproduces the binary coherent-information calculation and its finite-alphabet alias cost. The jitter check evaluates binomial loss windows and phase-tag overlaps. The all-input and asymptotic statements follow from the proofs. [Verification guide](verification/README.md)

## Scope

The nominal phase alphabet and any residual phase law are known. The realized phases are hidden and independently redrawn on every use. There is no additional transmitted reference mode or initial shared entanglement. The constructions allow arbitrary local quantum operations, including number-selective measurements. Hardware costs for these operations are outside the channel-use and photon budgets.

The quadratic energy law for target rates below the pure-loss capacity applies to the exact cyclic alphabet at fixed positive loss. The jitter criterion decides whether a positive rate survives at quadratic energy. The exact critical limits take the ordinary coding limit first for each channel, then grow the alphabet with linear mean input energy.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
