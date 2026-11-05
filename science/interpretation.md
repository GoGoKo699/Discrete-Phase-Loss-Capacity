# What photon loss changes

The [model](model.md) has one noisy optical mode per channel use. Its phase is chosen uniformly from $`J`$ equally spaced angles, independently on each use, and a fraction $`1-\eta`$ of its photons is lost. The alphabet is known in the agreed phase convention; the realized phase is unavailable. All physical input photons count, including any carrier used to make the phase branches distinguishable.

The [rate–energy theorem](rate_energy.md) fixes the desired number of ebits or secret bits per physical use. Its conclusion is a minimum-energy order, with constants depending on the fixed transmissivity and target rate. It gives no common constant for all losses or for rates approaching the pure-loss endpoint.

## Protection without loss

A cyclic phase twirl keeps coherence between number states whose photon numbers differ by a multiple of $`J`$. In particular, the states

```math
|0\rangle,\ |J\rangle,\ |2J\rangle,\ldots
```

form a noiseless subspace. A geometric distribution on these levels encodes entropy $`g(E/J)`$ at mean photon number $`E`$. The environment sees only the number residue, so the [lossless converse](rate_energy.md) gives the same upper bound. Increasing the alphabet size stretches the energy separation between logical levels linearly.

This protection uses a property of the exact cyclic alphabet. Additional phase errors outside that alphabet change the action on the protected coherence.

## The information carried away by lost photons

Suppose the input contains $`n`$ photons. The loss environment's photon count has the binomial law

```math
L\mid N=n\sim\mathrm{Bin}(n,1-\eta).
```

The rescaled count $`L/(1-\eta)`$ is an unbiased estimate of $`n`$, with conditional mean-squared error

```math
\mathbb E\!\left[
\left(N-\frac{L}{1-\eta}\right)^2\middle|N=n
\right]
=\frac{\eta n}{1-\eta}.
```

The twirl environment also carries the residue $`N\bmod J`$. Given both labels, possible input numbers lie on a lattice of spacing $`J`$. When the count uncertainty is small compared with that spacing, little uncertainty remains about the lattice index. The [converse](converse.md) turns this observation into an entanglement bound by measuring those environment labels in a squashing extension.

This measurement is a mathematical construction in an upper-bound proof. Neither communicating party receives the lost-photon count or the hidden phase. For every input purification, including those with nonorthogonal reference vectors, the remaining conditional entanglement is bounded by the classical posterior entropy

```math
H(N\mid L,N\bmod J).
```

A rounded estimator of the lattice index has mean-squared error at most $`4\eta E/((1-\eta)J^2)`$. Its entropy consequently vanishes when $`E/J^2`$ vanishes. The argument conditions on $`N`$ before taking expectations, so it never subtracts infinite photon-number second moments. Rare bright pulses and an infinite number variance are covered whenever the mean energy is finite.

The established energy-constrained squashed-entanglement theorem extends the bound to arbitrary adaptive two-way protocols. Its application is a weak converse for asymptotically reliable communication. [Davis–Shirokov–Wilde](../references/REFERENCES.md#dsw2018)

## A carrier that attains the energy order

For the lower bound, choose a fixed finite-Fock data subspace large enough to support the desired pure-loss reverse-hashing rate. The transmitter displaces the data before sending it. In each phase branch, displacement covariance of pure loss produces a translated and rotated copy of the same finite-cutoff loss output.

The [recovery construction](recovery.md) uses reciprocal maps for these finitely many subspaces. A successful outcome identifies its branch and restores the pure-loss data state exactly, including any entanglement with a reference. There is also an inconclusive outcome. Its probability is included in the achieved rate.

For output carrier amplitude $`A=aJ`$, branches with circular index separation $`h`$ have displacement separation

```math
d_h=2aJ\sin\frac{\pi h}{J}\ge4ah,
\qquad 1\le h\le J/2.
```

Finite-Fock overlaps are bounded by a fixed polynomial times a Gaussian in this separation. There are at most two branches at each circular separation. Summing these overlaps gives a bound independent of $`J`$, so one fixed choice of $`a`$ makes the success probability as close to one as the chosen rate requires.

The input carrier energy is $`a^2J^2/\eta`$. The data energy and cutoff can both remain fixed as $`J`$ grows. Reverse hashing of accepted pairs then attains every fixed rate below the pure-loss endpoint. This gives a matching sufficiency statement under the same energy convention as the converse.

A [quantitative example](../verification/README.md#a-quantitative-example) uses $`\eta=0.7`$, the three-level data law $`p=(4,2,1)/7`$, and $`a=1.2`$. Its exact energy is

```math
E=\frac47+\frac{72}{35}J^2.
```

The analytic uniform recovery bound evaluates to about $`0.98908`$ success, yielding a rate bound of about $`0.67606`$ ebits per attempted use. The verification page gives the exact bounding expression, its numerical evaluation and the finite Gram-matrix checks separately. These constants illustrate a feasible code; they are not optimized energy constants.

## Relation to phase-estimation limits

Lossy optical metrology already gives a phase quantum Fisher information ceiling proportional to mean photon number. Escher, de Matos Filho and Davidovich derive $`F_Q\le4\eta E/(1-\eta)`$, explaining why fixed loss removes Heisenberg scaling at high energy. [Escher2011](../references/REFERENCES.md#escher2011)

The communication theorem establishes a corresponding optimal energy requirement for maintaining entanglement or secret key. Its converse allows encodings that never estimate the phase, and its lower bound preserves unknown quantum data during successful branch recovery. This operational statement requires both the conditional-entropy proof and a compatible communication construction. The metrological scaling, the squashed-entanglement framework and reciprocal-state discrimination remain established ingredients.

## Finite alphabets and the continuous limit

For every fixed finite alphabet size, the [achievability theorem](rate_energy.md) reaches any rate below the pure-loss two-way endpoint as the input energy is increased. The pure-loss upper bound therefore gives

```math
\sup_{E\lt\infty}Q_2(\eta,J,E)
=\sup_{E\lt\infty}K(\eta,J,E)
=C_\eta,
\qquad C_\eta=-\log_2(1-\eta).
```

At every fixed finite energy, the converse instead implies that both capacities tend to zero as $`J`$ grows. For either capacity $`\mathcal C\in\{Q_2,K\}`$, the two iterated limits satisfy

```math
\lim_{J\to\infty}\lim_{E\to\infty}
\mathcal C(\eta,J,E)=C_\eta,
\qquad
\lim_{E\to\infty}\lim_{J\to\infty}
\mathcal C(\eta,J,E)=0.
```

Uniform continuous phase randomization measures photon number and prepares the corresponding diagonal state. Composing it with loss remains entanglement breaking, so its two-way entanglement and secret-key capacities vanish. The quadratic energy law quantifies the growing cost that is suppressed by taking an unconstrained-energy limit at each finite alphabet size.

The convergence here concerns the stated energy-constrained capacities. No unconstrained diamond-norm convergence or interchange of the two limits is assumed.

## What the threshold means operationally

For finite $`J`$, positive transmissivity and every positive mean-energy budget, a strictly positive two-way rate is possible. A finite-energy successful construction can be used on a fixed fraction of channel uses and vacuum sent on the others. The fraction counts in both rate and energy. The [positive-rate corollary](rate_energy.md) makes this precise.

Thus quadratic energy is necessary to keep a specified positive rate as the alphabet grows. A smaller energy budget permits a rate that vanishes with $`J`$. The theorem permits such duty cycling in its converse and does not impose a photon-number cutoff or a per-history energy cap on general protocols.

## Boundaries of the result

The exact phase atoms, their independence across uses and the known alphabet are part of the channel. A phase common to many uses creates a memory channel with different protected subspaces and different capacities. A separately transmitted noiseless reference or additional optical degree of freedom also changes the resource model.

Local operations are unrestricted. The carrier energy is fully counted, while the implementation time, local laboratory energy, control precision and gate complexity of the non-Gaussian recovery are not optimized. The code is an existence construction for the stated capacity model. Its robustness to continuous perturbations of the phase alphabet remains a separate question.

The analysis fixes $`\eta`$ strictly between zero and one. It does not establish a joint crossover law when the loss tends to zero as $`J`$ grows, an optimal low-transmissivity rate exponent at fixed energy, or the exact finite-energy capacity curve. These limitations leave the matched fixed-loss, fixed-rate energy law intact.
