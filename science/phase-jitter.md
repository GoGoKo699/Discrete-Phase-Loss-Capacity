# Phase broadening and the photon budget

A cyclic phase alphabet preserves coherence between photon numbers separated by integer multiples of its size $`J`$. Broadening the phases acts on those surviving coherences. At fixed photon loss, a positive rate at quadratic input energy depends on whether the broadened phase law retains a Fourier harmonic at a fixed index after rescaling. At weak loss and displacement, the same rescaled law enters the exact linear-energy capacity through an additional environment register.

## Folded phase law

On each independent use, apply the uniform cyclic twirl of order $`J`$ and an independent residual rotation of angle $`\Theta_J`$. The rotation and its realized value are hidden. The channel law is known. Then apply quantum-limited pure loss of transmissivity $`\eta_J`$ and, where specified, independent isotropic Gaussian displacement of variance $`b_J=\mathbb E|Z_J|^2`$ in complex amplitude. There is one transmitted oscillator per use, no transmitted reference mode and no preshared entanglement. The constraint bounds the unconditional mean input photon number, including every attempted use and adaptive history. Take the coding limit at each $`J`$ before increasing $`J`$.

Write $`N=r+JU`$ for input photon number $`N`$, residue $`0\le r\lt J`$ and quotient $`U\ge0`$. Let $`\nu_J`$ be the law of $`J\Theta_J`$ modulo $`2\pi`$, and let $`\widehat\nu_J(k)=\int e^{ik\varphi}\,\nu_J(d\varphi)`$. Within a fixed residue class the phase channel multiplies $`|r+Ju\rangle\langle r+Ju'|`$ by $`\widehat\nu_J(u-u')`$. Attach the unit vector $`\chi_u^{(J)}(\varphi)=e^{iu\varphi}`$ in $`L^2(\nu_J)`$ to the environment to realize this map after the cyclic twirl. The residue is already an environment label. This representation works for any probability law on the circle, including a discrete law.

## Fixed-loss rate threshold

**Theorem.** Suppose $`0\lt \eta\lt 1`$ is fixed, $`b_J=0`$, $`e\gt 0`$ and $`\nu_J`$ converges weakly to $`\nu`$. At mean input energy $`eJ^2`$:

- If $`\nu`$ is uniform, the two-way secret-key capacity tends to zero.
- If $`\nu`$ is nonuniform, the two-way entanglement-generation capacity has strictly positive limit inferior.

The second conclusion gives a positive two-way secret-key rate as well. The [existing loss-based converse](converse.md) applies by data processing and rules out a positive limiting rate at $`E=o(J^2)`$ for every residual law. Consequently quadratic energy is the minimum order for maintaining some positive rate when the limiting folded law is nonuniform. This threshold does not determine the exact fixed-loss capacity or the unassisted capacity in that regime.

### A rate bound for arbitrary inputs

Put $`q=1-\eta`$. The loss count $`L`$ satisfies $`L\mid N\sim\mathrm{Bin}(N,q)`$. Apply the exact-shift extension and relative-entropy argument given [below](#exact-capacity-at-weak-loss-and-displacement), with no displacement and shift $`S=-L`$. For every input energy $`E`$ it gives the adaptive upper bound

```math
K_J(E)\le\sup_{\mathbb E N\le E} H(U\mid r,L,\mathsf E_\phi),
```

where $`\mathsf E_\phi`$ holds the conditional vector $`\chi_U^{(J)}`$. The bound supplies neither the loss count nor the phase environment to the parties in the physical channel.

For a given pair $`(r,L)`$, estimate $`U`$ by rounding $`(L/q-r)/J`$ to the nearest integer, with any fixed tie convention. Write $`\widehat U`$ for this estimate and $`Y=U-\widehat U`$. Translating by a function of the conditioning registers gives $`H(U\mid r,L,\mathsf E_\phi)=H(Y\mid r,L,\mathsf E_\phi)`$. The conditional binomial variance and the at most half-unit rounding error give

```math
\mathbb E Y^2\le \frac{2\eta\,\mathbb E N}{qJ^2}+\frac12
\le C,\qquad C=\frac{2\eta e}{q}+\frac12.
```

Only the first input moment enters this bound. Fix a positive integer $`M_0`$. In the window $`|Y|\le M_0`$, the Gram matrix of the phase tags for $`y=-M_0,\ldots,M_0`$ has entries $`\widehat\nu_J(y'-y)`$. The common translation $`\widehat U`$ cancels from all overlaps, so this Gram matrix applies to every conditional prior and every recentering. With $`\nu`$ uniform, the matrix converges to the identity at fixed $`M_0`$. Represent the vectors by the columns of its positive square root, and measure in the coordinate basis. The worst-case misidentification probability on this finite set tends to zero. By data processing and Fano's inequality, the good-window contribution to $`H(Y\mid r,L,\mathsf E_\phi)`$ tends to zero uniformly over the input prior.

The tail flag costs at most $`h_2(p)`$ for $`p=\Pr(|Y|\gt M_0)\le C/M_0^2`$. Dropping the phase register and conditioning only on the tail, the signed integer has entropy at most $`1+g(\sqrt C/p)`$, where $`g(x)=(x+1)\log_2(x+1)-x\log_2 x`$. This uses $`\mathbb E|Y|\le\sqrt C`$ and the geometric maximum-entropy bound for the magnitude. Thus the tail contribution, including its flag, is at most $`h_2(p)+p[1+g(\sqrt C/p)]`$, with right-hand side zero at $`p=0`$. First take $`J\to\infty`$ at fixed $`M_0`$, then increase $`M_0`$. This proves the converse, including for input photon distributions with infinite variance.

### A receiver that accepts typical loss

If $`\nu`$ is nonuniform, some fixed positive integer $`k`$ has $`\gamma=|\widehat\nu(k)|\gt 0`$. Let $`d=kJ`$ and $`n=\lfloor cJ^2\rfloor`$, with $`0\lt c\lt e`$ chosen to satisfy $`\gamma^2\exp[k^2/(qc)]\gt 1`$. Prepare

```math
\frac{|0\rangle_R|n\rangle+|1\rangle_R|n+d\rangle}{\sqrt 2}.
```

Its unconditional mean input is $`n+d/2\le eJ^2`$ for all sufficiently large $`J`$. For each integer $`\ell`$ with $`t=(\ell-qn)/J`$ in a small interval centered at $`qk/2`$, the receiver projects onto the span of $`|n-\ell\rangle,|n-\ell+d\rangle`$. Choose the interval to have width less than $`k`$. For large $`J`$ the accepted number pairs are mutually disjoint and have nonnegative occupations. Include a failure outcome for their orthogonal complement. Accepting the pair does not reveal which number it contains. Map it to a common two-level register, correct the known phase of $`\widehat\nu_J(k)`$, and pool the results.

Write $`p_m(j)=\Pr(\mathrm{Bin}(m,q)=j)`$, with zero probability outside the binomial support. For a particular accepted pair the four diagonal entries, before the common factor $`1/2`$, are

```math
A=p_n(\ell),\qquad B=p_n(\ell-d),\qquad
C'=p_{n+d}(\ell+d),\qquad D=p_{n+d}(\ell).
```

Only the $`00,11`$ off-diagonal pair survives. Its corrected positive entry, before the same factor, is $`Z=|\widehat\nu_J(k)|\sqrt{AD}`$. The reason is that the coherent paths lose the same number $`\ell`$ of photons. The two other diagonal entries arise from different loss counts and enter as incoherent errors.

Uniformly for $`t`$ in the chosen interval, the binomial local limit gives for $`J(A,B,C',D)`$ the limiting vector

```math
\left(\phi_a(t),\phi_a(t-k),\phi_a(t+\eta k),\phi_a(t-qk)\right),
\qquad a=q\eta c,
```

where $`\phi_a`$ is the centered Gaussian density of variance $`a`$. The estimate follows from Stirling's formula for deviations of order $`J`$ from a binomial mean of order $`J^2`$. The limiting ratio $`Z^2/(BC')`$ is $`\gamma^2\exp[k^2/(qc)]`$. At the midpoint of the interval the limiting values of $`B`$ and $`C'`$ agree, so the limiting corrected off-diagonal density exceeds the average of the two error densities there. By continuity choose an interval of positive width on which this inequality persists. Riemann sums give a positive limiting acceptance probability, and the accepted state's limiting fidelity with $`(|00\rangle+|11\rangle)/\sqrt2`$ exceeds $`1/2`$. Indeed, the fidelity exceeds $`1/2`$ exactly when $`2\sum Z\gt \sum(B+C')`$.

An LOCC twirl preserving this Bell fidelity followed by [recurrence](../references/REFERENCES.md#bbpssw1996) and [hashing](../references/REFERENCES.md#dw2005) distills entanglement at a positive rate bounded below for all sufficiently large $`J`$. A fixed fidelity margin permits a fixed number of recurrence steps, after which hashing has positive rate. Counting failed outcomes gives the rate per physical channel use. This protocol accepts a window of typical loss counts. The [rail construction of Mele and coauthors](../references/REFERENCES.md#mele2024) proves positivity for fixed ordinary loss and dephasing by heralding vacuum in the loss port. Within a fixed-total-number code with exact cyclic coherence, a nontrivial number difference requires at least $`J`$ photons, so that route's no-loss probability is at most $`\eta^J`$.

### A moving harmonic raises the energy scale

For a wrapped Gaussian residual angle of rms width $`\sigma_J`$ before wrapping, $`\widehat\nu_J(k)=\exp[-(J\sigma_J)^2 k^2/2]`$. If $`J\sigma_J\to\delta\lt \infty`$, a positive rate survives at $`eJ^2`$. If $`J\sigma_J\to\infty`$, the folded law tends to uniform and the rate at that energy vanishes. For this Gaussian case the vanishing also holds at unlimited energy by data processing and the [pure-dephasing capacity theorem](../references/REFERENCES.md#phase2023), since the phase density becomes uniformly close to the uniform density.

The finite-energy converse also detects phase laws for which the pure-dephasing capacity stays constant. Let the folded law have density $`[1+a_0\cos(k_J\varphi)]/(2\pi)`$, where $`0\lt a_0\lt 1`$ and $`k_J\to\infty`$ through integers. The law converges weakly to uniform even though its relative entropy to uniform is independent of $`k_J`$ and positive. For fixed loss the capacity tends to zero at $`eJ^2`$. The net phase density is $`[1+a_0\cos(Jk_J\theta)]/(2\pi)`$. Equivalently, the channel has cyclic alphabet size $`J'=Jk_J`$ with a fixed nonuniform folded law. Applying the threshold and the inherited loss converse at this new alphabet size shows that the energy scale for a positive two-way rate is $`(Jk_J)^2`$. The loss count limits which quotient differences can carry useful coherence, so moving all phase contrast to higher harmonics changes the energy scale even at constant phase-only capacity.

If $`k_J=o(J)`$, the phase-only channel already gives a positive rate at the same budget $`eJ^2`$. Encoding into $`|0\rangle,|Jk_J\rangle`$ with equal weights costs $`Jk_J/2=o(J^2)`$ photons and realizes a qubit dephasing channel of coherence $`a_0/2`$. Its coherent information is $`1-h_2((1+a_0/2)/2)\gt0`$. In particular, $`k_J=\lfloor\sqrt J\rfloor`$ leaves a positive phase-only rate within the quadratic budget, while fixed loss requires cubic energy for a positive two-way rate.

## Exact capacity at weak loss and displacement

**Theorem.** Suppose $`J(1-\eta_J)\to\lambda`$, $`Jb_J\to\beta`$, and $`\nu_J\Rightarrow\nu`$, with $`\lambda,\beta\ge0`$ finite. At mean input energy $`eJ`$ for finite $`e\ge0`$, the unassisted quantum, two-way entanglement-generation and two-way secret-key capacities have the same limit

```math
F_{\lambda,\beta,\nu}(e)=
\sup_{\mathbb E[A+U]\le e} H(U\mid A,S,\mathsf E_D,\mathsf E_\phi).
```

Here $`A\in[0,1)`$, $`U\in\mathbb N_0`$ and $`x=A+U`$. Draw $`L\sim\mathrm{Pois}((\lambda+\beta)x)`$ and $`G\sim\mathrm{Pois}(\beta x)`$ independently given $`x`$, with $`S=G-L`$. The unnormalized displacement-environment vector at shift $`s`$ is

```math
v_s(x)=\sum_{g-l=s}\sqrt{\Pr(L=l\mid x)\Pr(G=g\mid x)}\,|l,g\rangle.
```

The square of its norm gives the shift probability. At a shift of positive probability use the normalized vector in $`\mathsf E_D`$ and the phase vector $`\chi_U(\varphi)=e^{iU\varphi}`$ in $`\mathsf E_\phi=L^2(\nu)`$. This is a conditional entropy of a classical register given the two quantum registers. Point mass phase jitter leaves the capacity in the [existing critical displacement theorem](critical-displacement.md).

### Finite-channel bounds

Use the [attenuator–amplifier dilation](critical-displacement.md#exact-finite-channel-comparison) of the Gaussian part, with transmissivity $`\tau_J=\eta_J/(1+b_J)`$ in the attenuator and amplifier gain $`1+b_J`$. For an input number $`n=r+Ju`$, replace the unnormalized vector $`v^{(J)}_{n,s}`$ in the displacement register by $`v^{(J)}_{n,s}\otimes\chi_u^{(J)}`$. The residue $`r`$ and shift $`s`$ label orthogonal environmental subspaces, so they can be copied to classical flags at Bob as an upper bound. Dropping the flags gives the physical channel. Conditioned on both flags the output number is $`n+s`$, which still identifies the input number. For Fock prior $`p`$, put

```math
G_J(p)=H(U\mid r,S,\mathsf E_D,\mathsf E_\phi),\qquad
M_J(E)=\sup_{p:\mathbb E_p N\le E}G_J(p).
```

To see why this bounds arbitrary adaptive key agreement, pinch the new output number inside each flag. The pinched channel is implemented by measuring input number and preparing the corresponding sampled output and flag, which preserves separability across the parties' cut. For the actual input, include a purifying register just for this estimate. Conditioned on the flags, the retained registers, received system and environments together are pure. The entropy after pinching the received number is the Shannon entropy of the conditional input-number probabilities because the residual retained-register vector is pure given that number. The entropy before pinching is the conditional environment entropy. Their difference is $`G_J(p)`$, where $`p`$ is the true photon-number marginal of the arbitrary input. Tracing out the auxiliary purification can only reduce the relative entropy to the pinched state. The countable pinching limit and amortization are those in the [critical displacement converse](critical-displacement.md#exact-finite-channel-comparison). Adding the phase tags leaves all entropies finite at finite mean energy because conditional environment entropy within a flag is bounded by the corresponding photon-number entropy. Telescoping the relative entropy of entanglement over channel uses and applying concavity at the unconditional energy budget gives $`K_J(E)\le M_J(E)`$.

For the lower bound, use a Fock-diagonal input with a fixed residue known to Bob. With its canonical purification, the different exact shifts still occupy orthogonal reference–output subspaces. Without giving Bob those flags, the coherent information is $`G_J(p)-H(S\mid M,r)`$, where $`M`$ is the output number. The number modulo $`J`$ supplies $`S\bmod J`$ from the known residue. As in the [critical displacement lower bound](critical-displacement.md#exact-finite-channel-comparison), let $`w=2([1-\tau_J+b_J\tau_J]E+b_J)/J`$. The integer quotient of the shift relative to a centered representative modulo $`J`$ has mean magnitude at most $`w`$, so the entropy cost is at most $`g(w)+\min(w,1)`$. Phase jitter does not change the shift distribution. Average over a predetermined residue schedule and apply energy-constrained coherent-information coding to obtain

```math
M_J(E)-g(w)-\min(w,1)
\le Q_J(E)\le Q_{2,J}(E)\le K_J(E)\le M_J(E).
```

All channel uses contribute to the mean constraint. The schedule carries no message and provides no extra mode. At $`E=eJ`$ in this regime, $`w\to0`$.

### Convergence and attainment

For a fixed quotient cutoff $`U\le M_0`$, the binomial and geometric counts of the exact dilation converge uniformly to the stated Poisson counts, as in the [first-moment argument](critical-displacement.md#first-moment-limit-and-strictly-positive-correction). Taking square roots of their joint probabilities preserves the coherent shift blocks in the trace-norm limit. The phase Gram matrix on the cutoff also converges, because its entries are finitely many Fourier coefficients of $`\nu_J`$. Its positive square root represents all phase vectors in a common finite space; continuity of the square root also covers degenerate limiting Gram matrices. The combined registers therefore converge uniformly for $`U\le M_0`$, including uniformly over the normalized residue $`A=r/J`$. Conditional-entropy continuity with the finite classical register $`U`$ makes the convergence uniform over priors on the cutoff.

For an unrestricted prior, a tail of probability $`p=\Pr(U\gt M_0)\le e/(M_0+1)`$ contributes at most $`h_2(p)+p g(e/p)`$, using the conditional entropy chain rule and the mean bound. Replacing the tail by vacuum does not increase energy and preserves at least the weighted good contribution by strong subadditivity. For a limiting prior on a fixed cutoff, round $`A`$ down to the finite residue grid. This reduces energy and changes $`x`$ by at most $`1/J`$. The uniform convergence of the bounded-input kernels applies, and dropping the original finer residue from the conditioning cannot lower the score. These two comparisons justify convergence of the optimized scores with only a first-moment bound.

The limiting score attains its supremum. Allow schedules given by probability measures on pairs $`(a,p)`$, where $`a\in[0,1]`$ and $`p`$ is a quotient prior. The cost $`a+\mathbb E_p U`$ is lower semicontinuous and its sublevel sets are compact in the weak topology. An average cost bound makes schedules tight, so the feasible set is weakly compact. The finite-cutoff score, weighted by the retained probability, is bounded and continuous in $`(a,p)`$. The tail estimate makes these averaged scores uniformly converge to the objective over feasible schedules. Concavity in the quotient prior lets us merge schedules with the same residue. At $`a=1`$, move the prior to $`a=0`$ and increase every quotient by one. This preserves the cost and shift vectors, and multiplying all phase tags by the same function is unitary. Thus allowing the endpoint and mixing schedules gives the same value as the stated supremum.

### What broadening changes

For $`e\gt 0`$ and finite $`\lambda,\beta`$, the exact limit is positive if and only if $`\nu`$ is nonuniform. Uniform $`\nu`$ gives orthogonal phase tags for distinct quotients. For nonuniform $`\nu`$, pick $`k\ge1`$ with $`\widehat\nu(k)\ne0`$ and take a binary prior on $`U=0,k`$ at $`A=0`$, with both weights positive and small enough excited weight to meet the energy bound. The zero shift has positive probability for both inputs. The conditional displacement vectors have positive overlap from their $`|0,0\rangle`$ components, and the phase vectors overlap by assumption. The conditional entropy on that flag is therefore positive.

For wrapped Gaussian broadening the optimized limit is strictly decreasing in the finite scaled width $`\delta=\lim J\sigma_J`$ whenever $`e\gt 0`$. To prove strictness, fix a nontrivial quotient prior at some residue, and condition on zero shift. The weighted Gram matrix of the joint pure environment ensemble has at least one nonzero off-diagonal entry at any finite $`\delta`$. Increasing $`\delta`$ Schur-multiplies that matrix by the Gram matrix of an independent Gaussian phase of positive variance, an average of diagonal unitary conjugations. The entropy of the weighted Gram matrix equals the entropy of the average environment state. Strict entropy concavity increases it because the conjugations change the nonzero off-diagonal entry. Entropies are finite since they are bounded by the quotient prior's Shannon entropy. For other shifts the environment entropy is nondecreasing by the same averaging. Thus the score strictly falls at any nontrivial prior. A maximizing schedule at the larger finite width has positive score and hence uses a nontrivial prior on a positive-measure set of residues. Evaluating the smaller-width score on that schedule proves strictness of the optimized limits.

[Scientific overview](README.md) · [Critical displacement](critical-displacement.md) · [Related work](../references/RELATED_WORK.md)
