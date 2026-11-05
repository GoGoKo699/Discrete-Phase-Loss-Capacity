# Channel and operational model

This page fixes the channel, the communication task, and the energy constraint used throughout the proofs. The main result concerns two-way entanglement generation and secret-key agreement for an independently redrawn, uniform cyclic phase alphabet followed by quantum-limited photon loss.

## One optical mode and a cyclic phase alphabet

The input and output Hilbert spaces are copies of

```math
\mathcal H=\ell^2(\mathbb N_0),
\qquad
\hat n=\sum_{n=0}^{\infty}n|n\rangle\langle n|.
```

Energy is measured in photons, so the vacuum has energy zero. All logarithms and entropies use base two. Fix an integer $`J\ge2`$ and define

```math
\theta_j=\frac{2\pi j}{J},
\qquad
U_j=e^{i\theta_j\hat n},
\qquad
P_r=\sum_{k=0}^{\infty}|Jk+r\rangle\langle Jk+r|.
```

The uniform phase channel is

```math
\mathcal D_J(X)
=\frac1J\sum_{j=0}^{J-1}U_j XU_j^\dagger
=\sum_{r=0}^{J-1}P_rXP_r.
```

The second expression follows by averaging the phase multiplying each Fock matrix element. Coherences between different number residues disappear; coherences within a residue remain.

Let $`\mathcal L_\eta`$ be the quantum-limited pure-loss channel with transmissivity $`0\le\eta\le1`$. Put $`q=1-\eta`$. For $`0\lt\eta\lt1`$, one Kraus representation is

```math
\mathcal L_\eta(X)=\sum_{\ell=0}^{\infty}A_\ell X A_\ell^\dagger,
\qquad
A_\ell|n\rangle=
\begin{cases}
\displaystyle
\sqrt{\binom n\ell q^\ell\eta^{n-\ell}}\,
|n-\ell\rangle,&n\ge\ell,\\
0,&n\lt\ell.
\end{cases}
```

Pure loss is phase covariant. Consequently the channel studied here has either ordering:

```math
\mathcal N_{\eta,J}
=\mathcal L_\eta\circ\mathcal D_J
=\mathcal D_J\circ\mathcal L_\eta.
```

A Kraus family for the first ordering is $`\{A_\ell P_r\}_{\ell,r}`$. The number of transmitted modes is the number of channel uses. Each use has a fresh independent phase draw and a fresh vacuum loss environment. A phase shared across a block of uses is a different channel.

The energy transformation is exact:

```math
\operatorname{Tr}\!\left[
\hat n\,\mathcal N_{\eta,J}(\rho)
\right]
=\eta\,\operatorname{Tr}(\hat n\rho).
```

The main theorem fixes $`0\lt\eta\lt1`$ while $`J`$ grows. The lossless endpoint $`\eta=1`$ is treated separately.

## Protocols and average input energy

Alice and Bob initially have independent local systems and no shared entanglement or secret key. They may use arbitrary local quantum operations, quantum memories, local ancillas, and adaptive authenticated two-way public classical communication. Protocols use the energy-constrained LOCC definition of [DSW2018](../references/REFERENCES.md#dsw2018). The initial product preparation satisfies its technical separability hypothesis.

An $`n`$-use protocol alternates local operations and public communication with $`n`$ uses of $`\mathcal N_{\eta,J}`$ from Alice to Bob. Let $`\rho_{A_i}^{(i)}`$ be the unconditional input marginal at use $`i`$, after averaging over every prior measurement outcome and public history. The photon constraint is

```math
\frac1n\sum_{i=1}^{n}
\operatorname{Tr}\!\left(\hat n\,\rho_{A_i}^{(i)}\right)
\le E.
\tag{1}
```

Equivalently, for the prior classical history $`H_i`$, the summand is

```math
\mathbb E_{H_i}\!\left[
\operatorname{Tr}\!\left(\hat n\,\rho_{A_i|H_i}^{(i)}\right)
\right].
```

This is an unconditional average constraint. Neither each history nor each use needs to obey a separate bound of $`E`$. Arbitrary photon-number distributions with finite mean are admitted, including distributions with infinite second moment.

All photons entering the channel count in (1). In particular, a displacement carrier counts even when it is used only to resolve the phase branch. Failed attempts and predetermined idle uses also count as channel uses. Local operations and local apparatus have no additional resource bound in this model. There is no additional transmitted reference mode outside the counted uses.

The receiver has no flag revealing the realized phase or the number of lost photons. Eve receives the complementary channel systems and the entire public transcript. The environment measurement used in the converse is a mathematical extension for an upper bound; it is not an operational resource granted to Alice or Bob.

## Two-way capacities

For entanglement generation, a protocol outputs finite-dimensional registers $`K_A,K_B`$ close in trace distance to

```math
|\Phi_D\rangle
=\frac1{\sqrt D}\sum_{k=0}^{D-1}|k\rangle_{K_A}|k\rangle_{K_B}.
```

Its rate is $`(\log_2D)/n`$ ebits per channel use. A rate is achievable at energy $`E`$ when a sequence of protocols satisfying (1) has error tending to zero and asymptotic rate at least that rate. The supremum of achievable rates is denoted

```math
Q_2(\eta,J,E)
:=Q_2(\mathcal N_{\eta,J},\hat n,E).
```

For secret-key agreement, the output registers are classical. If $`F`$ contains Eve's systems and the public transcript, the ideal target is

```math
\frac1D\sum_{k=0}^{D-1}
|kk\rangle\langle kk|_{K_AK_B}\otimes\omega_F.
```

The rate and vanishing-error definition are otherwise the same. Write

```math
K(\eta,J,E)
:=K(\mathcal N_{\eta,J},\hat n,E).
```

Trace-distance and fidelity criteria give the same vanishing-error capacities, so the average-energy theorem in [DSW2018](../references/REFERENCES.md#dsw2018) applies to these definitions. A distilled maximally entangled state yields secret key, and hence

```math
Q_2(\eta,J,E)\le K(\eta,J,E).
```

Only these two capacities are needed for the main result. The construction and converse do not assume Gaussian encoders, a prescribed bosonic code, product inputs in the converse, or a particular recovery measurement.

For $`X\in\{Q_2,K\}`$, define the energy required for a fixed target rate $`R\gt0`$ by

```math
E_{\min}^{X}(\eta,J,R)
=\inf\{E\ge0:X(\eta,J,E)\ge R\}.
\tag{2}
```

The infimum of the empty set is infinity. Achievability below is proved with a strict margin above $`R`$, so no conclusion relies on whether a boundary capacity is attained by one particular protocol.

## Entropy notation

Write $`H`$ for Shannon entropy and $`S`$ for von Neumann entropy. Define

```math
g(x)=(x+1)\log_2(x+1)-x\log_2x,
\qquad g(0)=0,
```

and

```math
f(u)=g(u)+\min\{u,1\}.
```

A nonnegative integer variable with mean at most $`x`$ has entropy at most $`g(x)`$. The maximizing law is geometric. The same bound holds for the von Neumann entropy of one optical mode with mean photon number at most $`x`$. Both statements follow from the Gibbs variational inequality with the geometric or thermal state.

In particular, for any finite-energy input, its photon-number entropy and the entropy of the output mode are finite:

```math
H(\mathsf N)\le g(E),
\qquad
S\!\left(\mathcal N_{\eta,J}(\rho)\right)\le g(\eta E).
```

The function $`f`$ is continuous, strictly increasing, and concave on the nonnegative real axis, satisfies $`f(0)=0`$, and is unbounded. Its inverse $`f^{-1}`$ is therefore well-defined.

## Structure of the argument

[The converse](converse.md) bounds the uncertainty in the input photon number after the environment records a loss count and a number residue. A rounded estimator turns that uncertainty into a bound depending on $`E/J^2`$ and only the first photon-number moment.

[The recovery construction](recovery.md) adds a counted displacement carrier and applies an exact heralded operation on a finite data subspace. A uniform Gram estimate makes its success probability close to one with carrier energy proportional to $`J^2`$.

[The rate and energy theorem](rate_energy.md) supplies a fixed finite data distribution with sufficient reverse-hashing rate, proves the cutoff limit explicitly, and combines the two bounds. The same page derives the exact lossless benchmark.

