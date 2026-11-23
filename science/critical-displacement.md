# Critical bosonic capacity under weak Gaussian displacement

## Channel and critical capacity

Consider one oscillator per independent channel use. The input undergoes the uniform cyclic phase twirl of order $`J`$, quantum-limited pure loss of transmissivity $`\eta_J`$, and centered isotropic Gaussian displacement of variance $`b_J=\mathbb E|Z_J|^2`$ in complex amplitude. A displacement of amplitude $`z`$ acts by $`D(z)=\exp(z a^\dagger-\bar z a)`$. The circular Gaussian law has centered real and imaginary quadratures of variance $`b_J/2`$ and adds $`b_J`$ photons to vacuum. The sender and receiver know the channel law. The noise record stays in the environment. There is one transmitted mode per use and no preshared entanglement. The constraint is the unconditional average input photon number, including all uses and adaptive histories. Take the coding limit at each $`J`$ before sending $`J`$ to infinity.

Suppose $`J(1-\eta_J)\to\lambda`$, $`Jb_J\to\beta`$ and the input budget is $`eJ`$, with $`e,\lambda,\beta`$ finite and nonnegative. The unassisted quantum capacity, two-way entanglement-generation capacity and two-way secret-key capacity have the same limit:

```math
F_{\lambda,\beta}(e)=
\sup_{\mathbb E[A+U]\le e} H(U\mid A,S,\mathsf E).
```

Here $`A\in[0,1)`$ is the normalized photon-number residue, $`U\in\mathbb N_0`$ is the quotient, and $`x=A+U`$. Draw $`L\sim\operatorname{Pois}((\lambda+\beta)x)`$ and $`G\sim\operatorname{Pois}(\beta x)`$ independently given $`x`$. For net shift $`s=G-L`$, the environment $`\mathsf E`$ has the subnormalized vector

```math
v_s(x)=\sum_{g-l=s}
\sqrt{\Pr(L=l\mid x)\Pr(G=g\mid x)}\,|l,g\rangle.
```

Its squared norm is $`\Pr(S=s\mid x)`$. The conditional environment state is $`|v_s(x)\rangle\langle v_s(x)|/\Pr(S=s\mid x)`$ whenever the shift has positive probability. In particular the objective is $`H(U\mid A,S)-I(U{:}\mathsf E\mid A,S)`$. Capacities are in qubits, ebits or secret bits per use. All entropies use base two.

Setting $`\lambda=0`$ isolates the effect of weak displacement following the cyclic phase twirl. The case $`\beta=0`$ gives the existing pure-loss Poisson limit $`F_{\lambda,0}(e)=\sup H(U\mid A,L)`$. If both noise scales are zero, the result is $`g(e)`$, where $`g(y)=(y+1)\log_2(y+1)-y\log_2 y`$. At $`e=0`$ the capacities vanish. For $`e\gt 0`$ and $`\beta\gt 0`$, the optimized shift-only expression is strictly higher than $`F_{\lambda,\beta}(e)`$.

## Exact finite-channel comparison

**Dilation.** Write $`b=b_J`$ and $`\tau=\eta_J/(1+b)`$. The composed Gaussian part equals a quantum-limited attenuator of transmissivity $`\tau`$ followed by a quantum-limited amplifier of gain $`1+b`$. This follows by comparing the signal gain and vacuum characteristic functions, using the decomposition of [Ivan, Sabapathy and Simon](../references/REFERENCES.md#iss2011). Conditional on input Fock number $`n`$, the lost count $`l`$ is binomial with loss probability $`1-\tau`$. Conditional on $`l`$, the gain count $`g`$ is the sum of $`n-l+1`$ geometric variables of mean $`b`$ on $`\mathbb N_0`$. The Kraus coefficient for $`(l,g)`$ is the nonnegative square root of this joint probability, up to a fixed convention on the environment basis. The output number is $`m=n+g-l`$. Twirling attaches the input residue $`r=n\bmod J`$ to the environment and eliminates coherences between residues. Define $`v_{n,s}^{(J)}`$ by grouping the joint square-root amplitudes with $`g-l=s`$. In the Stinespring isometry the input $`|n\rangle`$ maps to $`\sum_s |n+s\rangle_B |r\rangle_R |v_{n,s}^{(J)}\rangle_{\mathsf E}`$. The environment subspaces spanned by the loss and gain pairs for different shifts are orthogonal.

**Exact-shift extension.** Give Bob classical flags $`(r,s)`$ while retaining the environment's coherent vector $`v_{n,s}^{(J)}`$ in that branch. The flags can be copied from orthogonal environment subspaces in a Stinespring dilation. Dropping them recovers the physical channel. The complement is simulated from Bob's flagged output by measuring $`m`$, recovering $`n=m-s`$, and preparing its conditional environment state. Thus the extension is degradable. Its diagonal input coherent information is
$`G_J(p)=H(N\mid r,S,\mathsf E)`$ for input Fock prior $`p`$. Conditional on $`(r,s)`$ the output number uniquely indexes $`n`$, so this expression follows directly from the two output entropies. The score is concave in $`p`$ by concavity of conditional entropy. Write $`M_J(E)=\sup_{p:\mathbb E N\le E}G_J(p)`$.

**Adaptive upper bound.** Let $`\Phi`$ denote the extension with arbitrary retained Alice and Bob registers, and let $`\Delta`$ pinch Bob's new Fock number within each flag. The channel $`\Delta\Phi`$ can be implemented by measuring $`n`$ at Alice, classically sampling and sending $`(m,r,s)`$, and preparing the corresponding Fock state at Bob. For any pre-use state $`\rho`$ and separable trial state $`\sigma`$ across the pre-use cut, $`\Delta\Phi(\sigma)`$ is therefore separable across the post-use cut. The pinching identity and data processing give

```math
\begin{aligned}
D(\Phi\rho\Vert\Delta\Phi\sigma)
&= D(\Phi\rho\Vert\Delta\Phi\rho)
+ D(\Delta\Phi\rho\Vert\Delta\Phi\sigma) \\
&\le D(\Phi\rho\Vert\Delta\Phi\rho)+D(\rho\Vert\sigma).
\end{aligned}
```

The identity applies to countable Fock blocks. Keep the first $`k`$ receiver-number blocks coherent and pinch all higher numbers individually, removing coherences between the two parts. The resulting state tends to $`\Phi\rho`$ in trace norm and its complete pinch is still $`\Delta\Phi\rho`$. On this intermediate state only a finite pinching of the first $`k`$ blocks remains. Apply the finite pinching identity there. Both references $`\Delta\Phi\rho`$ and $`\Delta\Phi\sigma`$ are fixed by the intermediate channel, so data processing and lower semicontinuity give convergence of the two relative entropies with that intermediate first argument.

To bound the first term, purify $`\rho`$ and include the purifying register only for this calculation. Tracing it out commutes with $`\Delta`$ and can only decrease relative entropy. At each $`(r,s)`$ the full branch before tracing the environment is pure. This comparison generalizes the [number-preserving pinching argument](../references/REFERENCES.md#arqandsmith2026) to a channel with number shifts. After pinching, its joint retained-register and receiver entropy is $`H(N\mid r,s)`$ because each conditional retained-register vector is pure. Before pinching, the entropy is the conditional environment entropy. Their difference averaged over flags is $`G_J(p)`$ for the actual photon marginal. These entropies are finite because the number and absolute shift have finite means. Minimize over separable $`\sigma`$ and drop the flags locally at Bob for the actual adaptive protocol. Telescope the relative entropy of entanglement over all uses and apply concavity at the unconditional mean budget. The [Kaur–Wilde privacy test](../references/REFERENCES.md#kw2018) on the final private state gives $`(1-\epsilon)\log_2 d-h_2(\epsilon)\le E_R`$ for test failure at most $`\epsilon\le1/2`$ and key size $`d`$. This yields $`K_J(E)\le M_J(E)`$, and also bounds two-way entanglement.

**Physical lower bound.** Use a fixed, known input residue $`r`$ and a Fock-diagonal prior, with its canonical purification for calculating coherent information. Different shifts occupy orthogonal reference–Bob subspaces, indexed by $`m-n=s`$. Therefore the coherent information without the flags is exactly $`G_J(p)-H(S\mid M,r)`$, with $`M`$ the receiver photon number in the diagonal output; retaining the shift flag changes only Bob's marginal entropy difference. A modular number measurement reveals $`S\bmod J`$ from the known residue and preserves coherence within that class. For a centered representative modulo $`J`$, let $`T`$ be the signed integer quotient. Then $`|T|\le 2|S|/J`$ and $`H(S\mid M,r)\le H(T)`$. A nonnegative integer with mean $`t`$ has entropy at most $`g(t)`$, and the sign costs at most $`\min(t,1)`$ bits. From the exact dilation
$`\mathbb E|S|\le [1-\tau+b\tau]E+b`$. Thus we obtain the finite comparison

```math
\begin{aligned}
M_J(E)-g(w)-\min(w,1)&\le Q_J(E),\\
Q_J(E)\le Q_{2,J}(E)\le K_J(E)&\le M_J(E),\\
w&=2([1-\tau+b\tau]E+b)/J.
\end{aligned}
```

Use a predetermined schedule over residues. The schedule is part of the code, and each channel use still transmits only one oscillator. Apply [energy-constrained coherent-information coding](../references/REFERENCES.md#wildeqi2018) to each finite-support prior and concatenate the scheduled codes. The unconditional energy and the concave bound on the penalty average over the schedule. Finite supports approximate the supremum by the conditional-entropy tail argument below. Lower energies or a strict rate margin allow rounding scheduling fractions in a sequence of long block codes. At $`E=eJ`$ the penalty tends to zero.

## First-moment limit and strictly positive correction

Write $`N=J U+r`$ and $`A=r/J`$. On a fixed cutoff $`U\le M_0`$, the binomial loss law converges uniformly to its Poisson limit by the law of small numbers. Conditional gain can be compared in total variation to a Poisson with mean $`b(n-l+1)`$ by replacing each geometric variable with a Poisson of mean $`b`$ at cost $`O(b^2)`$ per summand. Comparing that Poisson mean to $`\beta x`$ costs at most $`(M_0+1)|Jb-\beta|+b(l+1)`$. The average loss is uniformly bounded on the cutoff. This gives uniform joint total variation convergence on bounded $`x`$. Square-root amplitudes give trace-norm convergence of the environment, keeping coherence inside each shift block. [Conditional entropy continuity](../references/REFERENCES.md#winter2016) on the finite register $`U`$ then applies uniformly over priors, even though the environment register is unbounded.

For the complement of the cutoff, let $`T_0=1_{\{U\gt M_0\}}`$, with probability $`p_0\le e/(M_0+1)`$. The chain rule bounds the objective lost by retaining only the good contribution by $`h_2(p_0)+p_0 g(e/p_0)`$, which tends uniformly to zero. Replacing the tail by vacuum preserves the energy budget and gives at least the weighted good contribution after conditioning on the tail label. This controls rare bright inputs without a variance assumption. To approximate a limiting prior by an allowed finite-$`J`$ prior, round $`A`$ down to the residue grid. The energy decreases, changing $`x`$ by at most $`1/J`$ affects the bounded-input kernels uniformly, and dropping the original finer $`A`$ can only increase conditional entropy. Together these steps justify taking the supremum in the limit.

For strictness after optimization, allow probability measures over pairs $`(a,p)`$, where $`p`$ is a law of $`U`$ and $`0\le a\le1`$. At a fixed residue, averaging the priors can only improve the conditional entropy by concavity, so this time-sharing relaxation has the same value as the original problem. The endpoint $`a=1`$ can be re-expressed as $`a=0`$ and $`U`$ increased by one. The mean-cost bound gives tightness of these measures since sublevel sets of $`a+\mathbb E_p U`$ are compact, and lower semicontinuity of cost makes the feasible set closed. The score truncated to $`U\le M_0`$ and weighted by its retained probability is bounded and continuous. Averaging the tail estimate and using Jensen's inequality gives uniform convergence of these truncated scores on the feasible set. Therefore the quantum objective attains its supremum in the time-sharing representation.

At $`s=0`$ the ratio of the $`(1,1)`$ and $`(0,0)`$ amplitudes of $`v_0(x)`$ is $`x\sqrt{(\lambda+\beta)\beta}`$. For $`\beta\gt 0`$, distinct number quotients at any residue give distinct pure states with positive zero-shift probability. Every nontrivial prior has a strictly positive conditional Holevo penalty. The vacuum and a single excited quotient give a positive quantum rate at any $`e\gt 0`$, because their zero-shift states have nonzero overlap. Thus a maximizing quantum schedule has nontrivial priors with positive measure. Evaluating the shift-only objective on that schedule proves a strictly larger optimized shift-only value. One operational comparator is the mathematical channel with one Kraus operator per $`(r,s)`$, amplitude $`\sqrt{\Pr(S=s\mid n)}`$ and translation $`|n\rangle\mapsto|n+s\rangle`$ within residue $`r`$. It has the same Fock transition law, and the same comparison proof gives its shift-only capacity limit.

The noise scale is also sharp. The environment can be measured for its lost count $`L`$, so the objective is at most $`H(U\mid A,L)`$. For $`c=\lambda+\beta\gt 0`$, estimate $`U`$ by rounding $`L/c-A`$ to the nearest nonnegative integer. A nonzero rounded error is bounded in magnitude by four times the squared estimation error before rounding. Thus the mean absolute rounded error is at most $`4e/c`$, and $`F_{\lambda,\beta}(e)\le g(4e/c)+\min(4e/c,1)`$. If $`Jb_J\to\infty`$ and $`J(1-\eta_J)\to\lambda\lt \infty`$, postprocessing each channel of variance $`\beta_0/J`$ by additional independent Gaussian displacement gives the original channel for all sufficiently large $`J`$. Take $`J\to\infty`$ and then $`\beta_0\to\infty`$ to see that all three capacities vanish at energy $`eJ`$. This places the positive-rate crossover at displacement variance of order $`1/J`$, or root-mean-square amplitude of order $`1/\sqrt J`$.

## Binary check

For an equal mixture of $`U=0,1`$ at $`A=0`$ and $`e=1/2`$, only the zero shift leaves uncertainty about $`U`$. Define $`z=(\lambda+\beta)\beta`$, $`I=I_0(2\sqrt z)`$, $`p=e^{-(\lambda+2\beta)}I`$, and $`\alpha=p/(1+p)`$. Here $`I_0`$ is the modified Bessel function. The two conditional zero-shift environment states have squared overlap $`1/I`$. Their mixture's smaller eigenvalue is
$`[1-\sqrt{1-4\alpha(1-\alpha)(1-1/I)}]/2`$.
Multiplying its binary entropy by $`(1+p)/2`$ gives the Holevo penalty. These checks use a prescribed prior.

| Loss scale $`\lambda`$ | Displacement scale $`\beta`$ | Shift-only bits/use | With environmental coherence |
|---:|---:|---:|---:|
| 0 | 0.5 | 0.661005 | 0.457863 |
| 1 | 1 | 0.404950 | 0.073567 |
| 1 | 0 | 0.574469 | 0.574469 |

For the first case the finite-channel calculation at $`J=2048`$ gives $`0.458951`$ qubits per use, compared with $`0.662251`$ bits per use from the shift statistic alone. Running the loss and gain cutoffs at 48 reproduces the approach to the limits and checks the coherent-information identity against the direct entropy difference, including the nonzero receiver alias cost at small $`J`$.

## What photon counting misses

The [displacement-only resolution law](https://github.com/GoGoKo699/Bosonic-Noise-Dimension/blob/4491f1b73dca4487d1356151e169bdf88486e707/science/05-broadening.md) gives $`\log_2 J+O(1)`$ qubits per use at $`E=eJ`$ for $`e\gt 0`$ and $`Jb_J\to\beta\lt\infty`$ when the displacement acts alone. Here the growing cyclic twirl leaves only the number-lattice degrees of freedom, giving the finite limiting capacity above. [Bosonic Noise Dimension's companion analysis](https://github.com/GoGoKo699/Bosonic-Noise-Dimension/blob/main/science/07-cyclic-phase.md) explains how to compare two channels with the same Fock transition law and different off-diagonal amplitudes. The [pure-loss crossover](critical-crossover.md) is the endpoint where the environment vector within a fixed shift has a single component.

[Scientific overview](README.md) · [Related work](../references/RELATED_WORK.md#weak-gaussian-displacement-and-number-preserving-dephasing) · [Reproduce the binary calculation](../verification/README.md#weak-displacement-check)
