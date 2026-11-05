# Fixed-rate energy theorem and lossless benchmark

This page combines the converse and exact recovery construction under the [average-energy communication model](model.md). Put

```math
C_\eta=-\log_2(1-\eta)
\qquad (0\lt\eta\lt1).
```

The endpoint $`C_\eta`$ is the unrestricted pure-loss two-way capacity from [PLOB2017](../references/REFERENCES.md#plob2017). Only that unrestricted endpoint is used; an exact finite-energy pure-loss capacity formula is unnecessary.

## Theorem 3: fixed-rate photon energy

Fix $`0\lt\eta\lt1`$ and $`0\lt R\lt C_\eta`$. For each $`X\in\{Q_2,K\}`$, there are constants

```math
0\lt c_{\eta,R}\le C_{\eta,R}\lt\infty
```

independent of $`J`$ such that, for all $`J\ge2`$,

```math
c_{\eta,R}J^2
\le E_{\min}^{X}(\eta,J,R)
\le C_{\eta,R}J^2.
\tag{1}
```

One valid lower constant is

```math
c_{\eta,R}
=
\frac{1-\eta}{4\eta}f^{-1}(R).
\tag{2}
```

The upper construction uses a fixed finite data cutoff and a carrier amplitude proportional to $`J`$. Its constants depend on $`\eta`$ and the target rate but not on coding block length. The result is for fixed transmissivity; it makes no claim uniform in a simultaneous limit $`\eta\to1`$.

The proof proceeds through a finite-dimensional reverse-hashing construction, proved next.

## Finite data and reverse coherent information

Let $`p`$ be a distribution on $`\{0,\ldots,M\}`$. Alice prepares its canonical purification

```math
|\psi_p\rangle_{RA}
=
\sum_{n=0}^{M}\sqrt{p_n}\,|n\rangle_R|n\rangle_A.
```

Let $`\sigma_{RB}=(\operatorname{id}_R\otimes\mathcal L_\eta)(\psi_p)`$. The loss Kraus decomposition is

```math
\sigma_{RB}
=
\sum_{\ell=0}^{M}|\phi_\ell\rangle\langle\phi_\ell|,
```

where

```math
|\phi_\ell\rangle
=
\sum_{n=\ell}^{M}
\sqrt{p_n\binom n\ell(1-\eta)^\ell\eta^{n-\ell}}\,
|n\rangle_R|n-\ell\rangle_B.
```

The branch vectors are mutually orthogonal: they have distinct values of the difference between the reference label and receiver photon number. If
$`\mathsf N\sim p`$ and
$`\mathsf L\mid\mathsf N\sim\operatorname{Bin}(\mathsf N,1-\eta)`$,
their squared norms are the probabilities of $`\mathsf L`$. Therefore

```math
S(R)_\sigma=H(p),
\qquad
S(RB)_\sigma=H(\mathsf L).
```

The reverse coherent information is exactly

```math
I_{\rm rev}(p,\eta)
=
S(R)_\sigma-S(RB)_\sigma
=
H(p)-H(\mathsf L).
\tag{3}
```

The finite-dimensional hashing inequality with communication from Bob to Alice achieves any rate below the positive part of (3); see [DW2005](../references/REFERENCES.md#dw2005) and its reverse-reconciliation application in [Reverse2009](../references/REFERENCES.md#reverse2009). Both retained systems have dimension at most $`M+1`$, so no infinite-dimensional distillation limit is being imported in this step.

## Lemma 4: a fixed finite cutoff suffices below the pure-loss endpoint

For every $`0\lt R\lt C_\eta`$, there is a finite $`M`$ and a distribution $`p`$ supported on $`\{0,\ldots,M\}`$ such that

```math
R_0:=H(p)-H(\mathsf L)\gt R.
\tag{4}
```

The choice can be fixed before varying either $`J`$ or the coding block length.

**Proof.** Write $`q=1-\eta`$. Start with a geometric input law of mean $`\mu\gt0`$:

```math
p_n^{(\mu)}=(1-z)z^n,
\qquad
z=\frac{\mu}{1+\mu}.
```

Binomial thinning makes the lost-photon law geometric with mean $`q\mu`$. For example, its probability generating function is

```math
\mathbb E[t^{\mathsf L}]
=
\mathbb E[(\eta+qt)^{\mathsf N}]
=
\frac1{1+q\mu(1-t)}.
```

The formal reverse coherent information of this finite-mean distribution is

```math
g(\mu)-g(q\mu)
\longrightarrow-\log_2q=C_\eta
\qquad(\mu\to\infty).
\tag{5}
```

The limit follows from $`g(x)=\log_2(ex)+o(1)`$ as $`x\to\infty`$. Choose one finite $`\mu`$ for which the expression in (5) exceeds $`R`$.

It remains to replace this fixed geometric law by one with finite support without losing the strict margin. Let $`p^{(\mu,M)}`$ be the law conditioned on $`\mathsf N\le M`$. Set

```math
T=\mathbf 1_{\{\mathsf N\gt M\}},
\qquad
\epsilon_M=\Pr(T=1)=z^{M+1}.
```

Geometric memorylessness implies

```math
\mathsf N\mid(T=1)
\ \stackrel{\rm law}{=}\ M+1+\mathsf N,
```

where the variable on the right has the original geometric law. Thus its tail entropy is $`g(\mu)`$, and its tail mean is $`M+1+\mu`$. The entropy chain rule gives the exact formula

```math
H\!\left(p^{(\mu,M)}\right)
=
g(\mu)-\frac{h_2(\epsilon_M)}{1-\epsilon_M},
\tag{6}
```

where $`h_2`$ is binary entropy.

Let $`\mathsf L_M`$ denote the lost-photon count for the truncated input. In the same joint experiment it has the conditional law of $`\mathsf L`$ given $`T=0`$. The chain rule now gives

```math
g(q\mu)
=
(1-\epsilon_M)H(\mathsf L_M)
+\epsilon_M H(\mathsf L\mid T=1)
+I(\mathsf L:T).
```

The tail mean of $`\mathsf L`$ is $`q(M+1+\mu)`$. The maximum-entropy bound and
$`0\le I(\mathsf L:T)\le h_2(\epsilon_M)`$
therefore imply

```math
\left|H(\mathsf L_M)-g(q\mu)\right|
\le
\frac{
\epsilon_M\!\left[g(q\mu)+g(q(M+1+\mu))\right]
+h_2(\epsilon_M)
}{1-\epsilon_M}.
\tag{7}
```

The right side tends to zero: $`\epsilon_M`$ decreases exponentially and the entropy of the tail mean grows only logarithmically. Equations (6) and (7) establish

```math
I_{\rm rev}\!\left(p^{(\mu,M)},\eta\right)
\longrightarrow g(\mu)-g(q\mu).
```

Choose a finite $`M`$ preserving the strict margin above $`R`$, and set $`p=p^{(\mu,M)}`$. Its mean $`E_0`$ is finite and at most $`\mu`$. This proves the lemma. ∎

This explicit tail argument avoids an exchange between a photon cutoff and the asymptotic coding limit.

## Exact heralding followed by hashing

Fix the distribution from Lemma 4, with cutoff $`M`$, mean $`E_0`$, and reverse rate $`R_0`$. Choose $`0\lt\delta\lt1`$ so that

```math
(1-\delta)R_0\gt R.
\tag{8}
```

By [Lemma 3 in recovery.md](recovery.md#lemma-3-uniform-success-with-amplitude-proportional-to-the-alphabet-size), choose a finite $`a=a(M,\delta)`$ giving success probability $`s_J\ge1-\delta`$ for every $`J`$, with output carrier amplitude $`A=aJ`$.

For each attempted use Alice prepares $`|\psi_p\rangle`$, displaces its transmitted half by $`D(aJ/\sqrt\eta)`$, and sends that mode. Bob applies the exact filter. On success, their normalized state is precisely $`\sigma_{RB}`$ from (3); on failure they discard the pair. The success probability is independent of the input and the reference.

For independent prepared pairs and independent channel uses, the success flags are independent Bernoulli variables with parameter $`s_J`$, and the retained pairs are copies of $`\sigma_{RB}`$. A fixed-length protocol can be made explicit. For fixed $`J`$ and $`0\lt t\lt s_J`$, make $`n`$ attempts and reserve

```math
m_n=\lfloor(s_J-t)n\rfloor
```

successful pairs. If fewer are available, declare abort and output a fixed state on the prescribed final registers. The probability of this event tends to zero. Otherwise, select the first $`m_n`$ successful pairs and apply a reverse-hashing protocol at any rate below $`R_0`$. Its error also tends to zero. Letting the hashing margin and then $`t`$ tend to zero proves

```math
Q_2\!\left(
\eta,J,E_0+\frac{a^2J^2}{\eta}
\right)
\ge s_JR_0
\ge(1-\delta)R_0
\gt R.
\tag{9}
```

Every attempted use has the same input marginal. Because the data marginal is Fock diagonal, the displacement cross terms vanish and its mean is exactly
$`E_0+a^2J^2/\eta`$.
Thus all attempts, including the failures, satisfy the stated average-energy accounting. The public success announcements are permitted two-way communication; distillation to ebits makes the resulting key secure against the full environment and transcript.

The cutoff $`M`$, data law $`p`$, and carrier coefficient $`a`$ were fixed using only $`\eta`$ and $`R`$. None grows with $`n`$ or $`J`$. The receiver instrument itself depends on $`J`$, as required to resolve its known alphabet.

## Proof of Theorem 3

The necessary energy (2) follows from the converse in [converse.md](converse.md).

For sufficiency, (9) achieves a rate strictly above $`R`$. For $`J\ge2`$,

```math
E_0+\frac{a^2J^2}{\eta}
\le
\left(E_0+\frac{a^2}{\eta}\right)J^2.
```

Take $`C_{\eta,R}=E_0+a^2/\eta`$. The same construction yields secret key by measuring the distilled ebits, so it proves the upper energy bound for both capacities. Together with the common lower bound, this proves (1). ∎

## Positive rate for every finite alphabet and positive energy

For each fixed $`J\ge2`$, $`0\lt\eta\lt1`$, and $`E\gt0`$,

```math
Q_2(\eta,J,E)\gt0,
\qquad
K(\eta,J,E)\gt0.
\tag{10}
```

To see this, use $`M=1`$ and $`p_0=p_1=1/2`$. Equation (3) gives

```math
R_0=1-h_2\!\left(\frac{1-\eta}{2}\right)\gt0.
```

Choose any fixed $`A\gt0`$. Theorem 2 gives a strictly positive exact success probability $`s`$. The active-use mean energy is

```math
E_{\rm active}=\frac12+\frac{A^2}{\eta}.
```

Use active signals in a predetermined fraction
$`\lambda=\min\{1,E/E_{\rm active}\}`$
of the channel uses, sending vacuum in all other slots. A schedule with
$`\lfloor\lambda n\rfloor`$
active uses obeys the average constraint for every $`n`$. Hashing the accepted active pairs achieves rates approaching

```math
\lambda sR_0\gt0.
```

Thus the quadratic law is the energy required to maintain a fixed positive rate as the alphabet grows. It is not a hard zero-capacity boundary at a finite positive energy.

## Fixed-alphabet unrestricted capacities

For each fixed $`J\ge2`$ and $`0\lt\eta\lt1`$,

```math
\sup_{E\lt\infty}Q_2(\eta,J,E)
=
\sup_{E\lt\infty}K(\eta,J,E)
=
C_\eta.
\tag{11}
```

Indeed, Theorem 3 supplies a finite energy for every target below $`C_\eta`$, while Theorem 1 supplies the endpoint upper bound. Monotonicity in $`E`$ also makes (11) the corresponding limit as $`E\to\infty`$. This statement concerns the two capacities defined here and a fixed finite alphabet.

## Theorem 4: exact lossless benchmark

For every $`J\ge2`$ and $`E\ge0`$,

```math
Q_2(1,J,E)=K(1,J,E)=g(E/J).
\tag{12}
```

Consequently, for either capacity and every finite $`R\gt0`$,

```math
E_{\min}^{X}(1,J,R)=J\,g^{-1}(R).
\tag{13}
```

**Converse.** At $`\eta=1`$, the channel is $`\mathcal D_J`$. Measuring its residue environment gives the same pure-branch extension as Lemma 1, without a loss count. For an arbitrary input purification with photon law $`\mathsf N`$, set
$`\mathsf S=\mathsf N\bmod J`$
and
$`\mathsf K=(\mathsf N-\mathsf S)/J`$.
Then

```math
\begin{aligned}
E_{\rm sq}(R:B)
&\le H(\mathsf N\mid\mathsf S)\\
&=H(\mathsf K\mid\mathsf S)\\
&\le H(\mathsf K)\\
&\le g(E/J).
\end{aligned}
```

The last step uses
$`\mathbb E[\mathsf K]\le\mathbb E[\mathsf N]/J\le E/J`$.
The Gibbs and finite output-entropy conditions still hold, so [DSW2018](../references/REFERENCES.md#dsw2018) converts this to the adaptive key upper bound in (12).

**Achievability.** The residue-zero subspace

```math
\operatorname{span}\{|Jk\rangle:k\ge0\}
```

is noiseless under $`\mathcal D_J`$. For $`E\gt0`$, take a geometric law of mean $`\nu=E/J`$ on $`k`$ and condition it on $`k\le M`$. Alice sends the second half of

```math
\sum_{k=0}^{M}\sqrt{p_k^{(\nu,M)}}\,|k\rangle_R|Jk\rangle_A.
```

Its transmitted energy is at most $`J\nu=E`$, and its output is the same pure entangled state. Finite-dimensional hashing, or entanglement concentration, yields its entropy
$`H(p^{(\nu,M)})`$.
By (6), that entropy tends to $`g(\nu)`$ as $`M\to\infty`$. Taking the supremum over finite $`M`$ proves achievability at energy $`E`$. At $`E=0`$, only the vacuum input is available and both sides of (12) vanish. Equation (13) follows by strict monotonicity of $`g`$. ∎

For each fixed nonzero loss, (1) gives a quadratic fixed-rate energy requirement. At exactly zero loss, (13) gives a linear requirement. The constants in the lossy theorem need not remain bounded as the transmissivity approaches one.

