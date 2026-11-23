# Capacity at the loss and phase-alphabet crossover

At fixed loss, a sender needs order $`J^2`$ photons per use to maintain a positive assisted rate as the cyclic phase alphabet grows. At zero loss the requirement is order $`J`$. The crossover occurs when the loss probability is of order $`1/J`$. In that regime the unassisted quantum, two-way quantum and secret-key capacities share an exact limit. A photon-number measurement modulo $`J`$ explains why the receiver can approach the same bound as a protocol with arbitrary assistance.

We use the [one-mode memoryless channel](model.md) with $`J\ge2`$ equally spaced, equally likely phases and pure photon loss of probability $`q=1-\eta`$. The channel uses a fresh phase draw and a fresh loss environment on each use. The phase alphabet and transmissivity are known. Every physical input photon counts toward the unconditional mean budget $`E`$ per use. Let $`Q`$, $`Q_2`$ and $`K`$ be the unassisted quantum, two-way quantum and two-way secret-key capacities with this budget. Rates use base-two entropies and are measured per physical channel use.

## The finite-alphabet bound

Let $`\mathsf N`$ denote input photon number, $`\mathsf L`$ the number lost, and $`\mathsf S=\mathsf N\bmod J`$ the input residue. For a classical prior on $`\mathsf N`$, draw $`\mathsf L\mid\mathsf N=n\sim\mathrm{Bin}(n,q)`$. Define

```math
C_J(q,E)=\sup_{\mathbb E\mathsf N\le E}
 H(\mathsf N\mid\mathsf L,\mathsf S).
```

Here $`g(x)=(1+x)\log_2(1+x)-x\log_2 x`$ is the entropy of a geometric law with mean $`x`$, with $`g(0)=0`$. For all finite $`E\ge0`$,

```math
\boxed{
\max\{0,C_J(q,E)-g(qE/J)\}
\ \le\ Q\ \le\ Q_2\ \le\ K\ \le\ C_J(q,E).
}
```

The [environment extension in the converse](converse.md#lemma-1-an-environment-extension-valid-for-every-reference) gives $`E_{\mathrm{sq}}(R:B)\le H(\mathsf N\mid\mathsf L,\mathsf S)`$ for any input purification, with $`\mathsf N`$ distributed according to its Fock probabilities. The source's energy-constrained squashed-entanglement bound therefore gives $`K\le C_J(q,E)`$ for adaptive protocols. This proof allows arbitrary quantum inputs and does not require a finite photon-number variance. The zero-loss channel has the [exact capacity](rate_energy.md) $`g(E/J)`$, which also equals $`C_J(0,E)`$. At complete loss the receiver gets vacuum and all four quantities are zero.

### What the receiver learns

For the lower bound, fix one input residue $`r`$. Use a Fock-diagonal input with prior $`p_n`$ supported on $`n\equiv r\bmod J`$, and purify it canonically as $`\sum_n\sqrt{p_n}\,|n\rangle_R|n\rangle_A`$. All cyclic phase rotations act by a common phase on this subspace. In the loss branch $`\ell`$ the joint reference and receiver state has unnormalized vector

```math
  \sum_{n\ge \ell}
     \sqrt{p_n\Pr[\mathsf L=\ell\mid\mathsf N=n]}\,
     |n\rangle_R|n-\ell\rangle_B.
```

Different loss branches have orthogonal joint support, since the reference and receiver number labels differ by $`\ell`$. The receiver marginal is diagonal with number distribution $`\mathsf B=\mathsf N-\mathsf L`$. Thus this input has forward coherent information

```math
\begin{aligned}
I_c &= H(\mathsf B)-H(\mathsf L)\\
    &= H(\mathsf N\mid\mathsf L)-H(\mathsf L\mid\mathsf B).
\end{aligned}
```

The second line uses the bijection between $`(\mathsf B,\mathsf L)`$ and $`(\mathsf N,\mathsf L)`$. The receiver can measure $`\mathsf B\bmod J`$ without resolving the encoded levels. Since $`r`$ is known, this gives $`\mathsf L\bmod J=(r-\mathsf B)\bmod J`$. The receiver can use the least nonnegative representative of the loss residue as its syndrome. It equals the full loss count when $`0\le\ell\lt J`$. Within such a branch the receiver can relabel $`|r+Ju-\ell\rangle`$ as $`|u\rangle`$ without measuring the encoded label $`u`$. The proof of the rate uses the full loss distribution and charges all events, including losses of $`J`$ photons or more. In particular, if $`E_r=\mathbb E[\mathsf N\mid\mathsf S=r]`$,

```math
H(\mathsf L\mid\mathsf B)
 = H\!\left(\left\lfloor\mathsf L/J\right\rfloor\middle|\mathsf B\right)
 \le g(qE_r/J).
```

This follows because $`\mathsf B`$ fixes the residue of $`\mathsf L`$ and $`\mathbb E\lfloor\mathsf L/J\rfloor\le qE_r/J`$. The geometric entropy bound makes all the entropies above finite at finite mean energy.

For an arbitrary prior, use each conditional prior $`p_{n\mid r}`$ in the corresponding predetermined fraction $`\Pr[\mathsf S=r]`$ of physical channel uses. The schedule is agreed before coding. It carries no message and consumes no transmitted reference mode or feedback. Coherent information adds over this product input, and concavity of $`g`$ gives

```math
 \sum_r \Pr[\mathsf S=r] I_{c,r}
 \ \ge\ H(\mathsf N\mid\mathsf L,\mathsf S)-g(qE/J).
```

To implement the fractions in a finite period, first reserve an arbitrarily small vacuum fraction for energy slack, then approximate the remaining fractions by rational numbers. This gives a deterministic product input on the finite block, with average energy at most $`E`$. The vacuum fraction and any rounding cost vanish in the rate limit. The summed photon-number observable has a finite Gibbs partition function at every positive inverse temperature. The output entropy of a block of $`m`$ uses at mean per-use input energy $`E`$ is bounded by $`m\,g(\eta E)`$, by subadditivity and concavity. The [energy-constrained coherent-information coding theorem](../references/REFERENCES.md#wildeqi2018) therefore supplies the product coherent information per physical use as an achievable unassisted rate. The vacuum-only case is immediate. Taking the supremum over priors completes the lower bound.

## Exact capacity in the critical window

Let $`J\to\infty`$ through integers, let $`E=eJ`$ for fixed $`e\ge0`$, and suppose $`Jq_J\to\lambda`$ with $`0\le\lambda\lt\infty`$. For each $`J`$ take the capacity coding limit at that channel and energy before taking the limit in $`J`$. Then

```math
\begin{aligned}
 \lim_{J\to\infty}Q
  &=\lim_{J\to\infty}Q_2
   =\lim_{J\to\infty}K
   =F_\lambda(e),\\
 F_\lambda(e)
  &=\sup_{\substack{0\le A\le1,\ \mathsf U\in\mathbb Z_{\ge0}\\
                   \mathbb E[A+\mathsf U]\le e}}
       H(\mathsf U\mid\mathsf L,A),
 \qquad
 \mathsf L\mid (A=a,\mathsf U=u)
     \sim\mathrm{Poisson}\!\left(\lambda(a+u)\right).
\end{aligned}
```

The supremum is over joint laws of the normalized residue $`A`$ and the number-lattice index $`\mathsf U`$. The cost $`A+\mathsf U`$ is the input photon number divided by $`J`$. The residue specifies which number lattice is in use and which loss residue the receiver should infer. The Poisson observation represents information lost to the environment. The code has access to the received oscillator.

For $`\lambda=0`$ the count is deterministic and $`F_0(e)=g(e)`$, attained using $`A=0`$ and a geometric index of mean $`e`$. At $`e=0`$ the capacity is zero. For each positive $`e`$ and finite $`\lambda`$, an index supported on two adjacent nonnegative integers with $`A=0`$ and both probabilities positive can be chosen within the budget. The observation $`\mathsf L=0`$ leaves both indices possible, so $`F_\lambda(e)\gt0`$. When $`Jq_J\to\infty`$ and $`E=eJ`$ instead, the [lost-count estimate](converse.md#lemma-2-a-prior-uniform-integer-estimation-bound) bounds the capacity of the lossy channel by $`f(4\eta e/(Jq_J))`$ with $`f(x)=g(x)+\min\{x,1\}`$ and forces all three rates to zero. Complete loss gives zero directly.

### Proof of the variational limit

The finite-alphabet bound leaves a gap of at most $`g(q_Je)`$, which tends to zero. It remains to take the limit of $`C_J(q_J,eJ)`$. Set $`A=\mathsf S/J`$ and $`\mathsf U=\lfloor\mathsf N/J\rfloor`$. The optimized entropy becomes $`H(\mathsf U\mid\mathsf L,A)`$, with the same mean constraint as the limiting formula and the binomial count of $`J(A+\mathsf U)`$ trials. Two estimates make the limit uniform over admissible priors.

**Truncating the index.** Let $`T=\mathbf 1_{\{\mathsf U\gt M\}}`$ and $`p=\Pr[T=1]\le e/(M+1)`$. The chain rule gives

```math
H(\mathsf U\mid\mathsf L,A)
 \le (1-p) H(\mathsf U\mid\mathsf L,A,T=0)
       +h_2(p)+p\,g(e/p),
```

where $`h_2`$ is the binary entropy and the last term is zero at $`p=0`$. The conditional mean on the tail is at most $`e/p`$, so the geometric entropy bound gives its contribution. Replace the tail by $`A=\mathsf U=\mathsf L=0`$. The replacement obeys both the mean constraint and the channel law, in either the binomial or Poisson model. Its conditional entropy is at least the first term on the right, by further conditioning on the old tag $`T`$. The error is uniformly small for large $`M`$ since $`h_2(p)+p\,g(e/p)\to0`$ as $`p\to0`$. This step requires only a first-moment constraint.

**Comparing the counts.** At fixed $`M`$, uniformly for $`\mathsf U\le M`$ and residues in the $`1/J`$ grid, the binomial count differs from $`\mathrm{Poisson}(\lambda(A+\mathsf U))`$ in total variation by at most

```math
\delta_{J,M}=(M+1)\bigl(Jq_J^2+|Jq_J-\lambda|\bigr).
```

Coupling each Bernoulli trial with a Poisson of the same mean costs at most $`q_J^2`$ per trial in total variation. Coupling two Poisson laws by adding an independent increment costs at most the difference in their means. These two couplings give the bound and $`\delta_{J,M}\to0`$. For two joint laws at total variation distance $`\delta`$ with $`\mathsf U\in\{0,\ldots,M\}`$ the conditional entropies differ by at most $`\delta\log_2(M+1)+h_2(\delta)`$. To see this, write each law as a mixture of their common mass of weight $`1-\delta`$ and its residual mass. Conditional entropy of the mixture differs from the mixture of conditional entropies by the information carried by the binary mixture tag, at most $`h_2(\delta)`$. This bound depends on the index alphabet, even if the conditioning variables have infinitely many possible values.

Apply the comparison to each truncated grid prior to bound its rate by the continuum Poisson supremum plus a vanishing error. Conversely, start with any admissible Poisson prior with $`\mathsf U\le M`$ and round $`A`$ down to $`A_J=\min\{\lfloor JA\rfloor,J-1\}/J`$. This produces a legal residue and cannot increase the mean cost. In the original Poisson law, conditioning on the coarser $`A_J`$ gives

```math
H(\mathsf U\mid\mathsf L,A_J)\ge H(\mathsf U\mid\mathsf L,A).
```

Now compare the original Poisson count and the physical binomial count associated with $`A_J`$. The extra mean change costs at most $`\lambda/J`$ in total variation. The conditional entropy of the rounded binomial law therefore approaches at least the original Poisson term. Its photon number $`J(A_J+\mathsf U)`$ is integral, so the law is a candidate for $`C_J(q_J,eJ)`$. Taking $`J\to\infty`$ first and then sending the cutoff $`M`$ to infinity proves convergence of the optimized conditional entropy and hence of all three capacities.

## A two-level example

Take one residue with equal input probabilities on $`|0\rangle`$ and $`|J\rangle`$. At $`q=1/J`$ it spends $`J/2`$ photons per use on average. In the loss count, only $`\mathsf L=0`$ is compatible with both logical inputs. In the received count, only $`\mathsf B=0`$ is compatible with both, because the high-number input can lose all its photons. Write

```math
b(x)=\tfrac12\bigl((1+x)\log_2(1+x)-x\log_2 x\bigr).
```

The exact coherent information of this input is

```math
I_c=b\!\left((1-1/J)^J\right)-b\!\left(J^{-J}\right).
```

At $`J=128`$ the achievable rate is about $`0.573102`$ qubits per physical use. It approaches $`b(\exp(-1))\simeq0.574469`$ qubits per use. This is one feasible prior in $`F_1(1/2)`$. The limiting capacity optimizes over all paid number levels and residues.

The result assumes exactly cyclic phase noise and arbitrary ideal local operations. The finite-alphabet theorem bounds the capacity gap even away from the critical limit. The exact shared variational formula concerns the limiting capacities. Hardware cost, robustness to continuous phase broadening and any exact capacity at a fixed nonzero loss and finite alphabet are separate questions.

## With Gaussian displacement

The [critical displacement theorem](critical-displacement.md) recovers this curve when the displacement scale vanishes. When the variance is of order the inverse alphabet size, the environment can retain coherent information about distinct loss and gain histories with the same net shift. The receiver's unresolved shift remains a vanishing entropy cost.
