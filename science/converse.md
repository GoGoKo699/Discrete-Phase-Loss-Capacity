# Universal converse from the lost-photon count

The channel and protocol conventions are those in [model.md](model.md). Fix $`J\ge2`$, $`0\lt\eta\lt1`$, $`q=1-\eta`$, and $`E\ge0`$.

## Theorem 1: capacity bound

Under the unconditional average photon constraint,

```math
Q_2(\eta,J,E)
\le K(\eta,J,E)
\le
\min\left\{
-\log_2(1-\eta),
\ f\!\left(\frac{4\eta E}{(1-\eta)J^2}\right)
\right\}.
\qquad\text{(1)}
```

Here $`f(u)=g(u)+\min\{u,1\}`$. The bound applies to arbitrary reference-entangled inputs and to adaptive protocols. Its energy dependence requires only a finite first moment of the photon number.

The pure-loss endpoint in (1) is inherited from [PLOB2017](../references/REFERENCES.md#plob2017). The conversion of the one-use entanglement estimate below into a capacity bound uses the average-energy weak-converse theorem of [DSW2018](../references/REFERENCES.md#dsw2018). The new estimate is the explicit conditional-entropy bound in Lemmas 1 and 2.

## Squashed entanglement and the imported capacity theorem

For a bipartite state $`\sigma_{RB}`$, squashed entanglement is

```math
E_{\rm sq}(R:B)_\sigma
=\frac12\inf_{\omega_{RBC}:\mathrm{Tr}_C\omega=\sigma}
I(R:B|C)_\omega.
```

An equivalent minimization applies a channel to a purifying environment. The energy-constrained channel quantity is

```math
E_{\rm sq}(\mathcal N,\hat n,E)
=
\sup_{\psi_{RA}:\mathrm{Tr}(\hat n\psi_A)\le E}
E_{\rm sq}(R:B)_{(\mathrm{id}_R\otimes\mathcal N)(\psi)},
```

where the inputs in the supremum are pure and the reference is arbitrary.

[DSW2018, Theorem 4](../references/REFERENCES.md#dsw2018) upper-bounds the adaptive average-energy secret-key capacity by this quantity, assuming a Gibbs input observable and finite output entropy at each finite input-energy bound. The number observable satisfies

```math
\mathrm{Tr}(e^{-\beta\hat n})
=\frac1{1-e^{-\beta}}\lt\infty
\qquad(\beta\gt0).
```

The channel satisfies the other hypothesis because its output mean is $`\eta E`$ and its output entropy is at most $`g(\eta E)`$. Thus

```math
Q_2(\eta,J,E)
\le K(\eta,J,E)
\le E_{\rm sq}(\mathcal N_{\eta,J},\hat n,E).
\qquad\text{(2)}
```

The source's Eq. (101) uses the average over channel inputs, not a separate energy cap on each use. The result is a weak-converse capacity bound. No strong-converse assertion is needed here.

## Lemma 1: an environment extension valid for every reference

For any pure input $`|\psi\rangle_{RA}`$, expand in the input Fock basis:

```math
|\psi\rangle_{RA}
=\sum_{n=0}^{\infty}|\xi_n\rangle_R|n\rangle_A,
\qquad
p_n=\langle\xi_n|\xi_n\rangle.
```

The vectors $`|\xi_n\rangle`$ are unnormalized and need not be orthogonal. Suppose $`\sum_nnp_n\le E`$. Introduce classical random variables with law

```math
\mathsf N\sim p,
\qquad
\mathsf S=\mathsf N\bmod J,
\qquad
\mathsf L\mid\mathsf N=n\sim\mathrm{Bin}(n,q).
```

Then

```math
E_{\rm sq}(R:B)_{(\mathrm{id}\otimes\mathcal N_{\eta,J})(\psi)}
\le H(\mathsf N\mid\mathsf L,\mathsf S).
\qquad\text{(3)}
```

**Proof.** Use the channel's Kraus operators $`A_\ell P_r`$ in a Stinespring dilation and measure their orthogonal environment label $`(\ell,r)`$. This is a legitimate squashing channel. Its conditional, unnormalized reference-output vector is

```math
|\widetilde\psi_{\ell,r}\rangle
=
\sum_{\substack{n\ge\ell\\n\equiv r\ ({\rm mod}\ J)}}
\sqrt{\binom n\ell q^\ell\eta^{n-\ell}}\,
|\xi_n\rangle_R|n-\ell\rangle_B.
```

For fixed $`\ell`$, the receiver number states corresponding to distinct $`n`$ are orthogonal. Therefore the branch probability is

```math
p_{\ell,r}
=
\sum_{\substack{n\ge\ell\\n\equiv r\ ({\rm mod}\ J)}}
p_n\binom n\ell q^\ell\eta^{n-\ell},
```

and the reference marginal of the normalized branch is a mixture of the pure states $`|\xi_n\rangle/\sqrt{p_n}`$, with the classical posterior weights of $`\mathsf N`$ given $`(\mathsf L,\mathsf S)=(\ell,r)`$. Terms with zero weight can be omitted. The entropy of a pure-state mixture is at most the entropy of its mixing weights, so

```math
S(R)_{\psi_{\ell,r}}
\le
H(\mathsf N\mid\mathsf L=\ell,\mathsf S=r).
```

Each conditional $`RB`$ state is pure. If $`C`$ denotes the classical environment outcome, then

```math
\begin{aligned}
\frac12 I(R:B|C)
&=\sum_{\ell,r}p_{\ell,r}S(R)_{\psi_{\ell,r}}\\
&\le H(\mathsf N\mid\mathsf L,\mathsf S).
\end{aligned}
```

Taking this particular extension in the definition of squashed entanglement proves (3).

All entropies used here are finite: $`H(\mathsf N)\le g(E)`$, $`H(\mathsf L)\le g(qE)`$, and $`H(\mathsf S)\le\log_2J`$. The reference entropy is also finite because it equals the input entropy. The countable classical extension consequently has the stated conditional-entropy interpretation. The proof does not replace a general input by a Fock-diagonal input. It only uses its Fock probabilities to upper-bound the entropy of the actual conditional reference states. ∎

## Lemma 2: a prior-uniform integer-estimation bound

For every distribution of $`\mathsf N`$ with mean at most $`E`$,

```math
H(\mathsf N\mid\mathsf L,\mathsf S)
\le
f\!\left(\frac{4\eta E}{qJ^2}\right).
\qquad\text{(4)}
```

**Proof.** Define the integer quotient and an estimator by

```math
\mathsf K=\frac{\mathsf N-\mathsf S}{J},
\qquad
\widehat{\mathsf K}
=\frac{\mathsf L/q-\mathsf S}{J}.
```

Fix any nearest-integer convention at ties, and set

```math
\mathsf Z
=\mathsf K-\mathrm{round}(\widehat{\mathsf K}).
```

For every integer $`k`$ and real $`x`$,

```math
|k-\mathrm{round}(x)|\le2|k-x|.
\qquad\text{(5)}
```

If the rounded value equals $`k`$, the inequality is immediate. Otherwise $`|k-x|\ge1/2`$, and the triangle inequality gives
$`|k-\mathrm{round}(x)|\le|k-x|+1/2\le2|k-x|`$.

Apply (5), then condition on the photon number before evaluating the second moment:

```math
\begin{aligned}
\mathbb E[\mathsf Z^2]
&\le \frac4{J^2}
\mathbb E\!\left[
\left(\mathsf N-\frac{\mathsf L}{q}\right)^2
\right]\\
&=\frac4{J^2}
\mathbb E\!\left[
\mathbb E\!\left[
\left(\mathsf N-\frac{\mathsf L}{q}\right)^2
\middle|\mathsf N
\right]\right]\\
&=\frac{4\eta\,\mathbb E[\mathsf N]}{qJ^2}
\le u,
\qquad
u:=\frac{4\eta E}{qJ^2}.
\end{aligned}
\qquad\text{(6)}
```

The conditional identity uses

```math
\mathbb E[\mathsf L\mid\mathsf N]=q\mathsf N,
\qquad
\mathrm{Var}(\mathsf L\mid\mathsf N)=q\eta\mathsf N.
```

Equation (6) never subtracts potentially divergent unconditional second moments. Its integrand is nonnegative, and its conditional expectation is linear in $`\mathsf N`$. A finite photon-number variance is therefore unnecessary.

For each fixed observed pair $`(\mathsf L,\mathsf S)`$, the maps from $`\mathsf N`$ to $`\mathsf K`$ and then to $`\mathsf Z`$ are one-to-one on their conditional supports. Hence

```math
H(\mathsf N\mid\mathsf L,\mathsf S)
=
H(\mathsf Z\mid\mathsf L,\mathsf S)
\le H(\mathsf Z).
\qquad\text{(7)}
```

Since $`\mathsf Z`$ is integer-valued,

```math
\mathbb E|\mathsf Z|\le\mathbb E[\mathsf Z^2]\le u,
\qquad
\Pr(\mathsf Z\ne0)\le\min\{u,1\}.
```

Its nonnegative integer magnitude has entropy at most $`g(u)`$. Conditional on a nonzero magnitude, its sign has at most one bit of entropy; at zero, there is no sign choice. Therefore

```math
\begin{aligned}
H(\mathsf Z)
&=H(|\mathsf Z|)
+H(\mathsf Z\mid|\mathsf Z|)\\
&\le g(u)+\Pr(\mathsf Z\ne0)\\
&\le g(u)+\min\{u,1\}.
\end{aligned}
```

Combining this with (7) proves (4). ∎

## Proof of Theorem 1

Lemmas 1 and 2 hold for every input purification satisfying the energy constraint. Taking the supremum in the channel squashed entanglement and using (2) gives

```math
K(\eta,J,E)
\le f\!\left(\frac{4\eta E}{qJ^2}\right).
```

This step invokes the adaptive average-energy theorem directly; it does not assume that the input to each adaptive use has mean at most $`E`$. The same fixed environment measurement works for all inputs. Also, $`f`$ is concave and increasing, so an average of the resulting bounds over finite conditional input-energy budgets is at most the bound evaluated at their average.

For the other term, $`\mathcal N_{\eta,J}=\mathcal D_J\circ\mathcal L_\eta`$ is pure loss followed by receiver noise. Its two-way key capacity cannot exceed that of pure loss with unrestricted input energy. [PLOB2017](../references/REFERENCES.md#plob2017) gives that endpoint as $`-\log_2q`$. Together with $`Q_2\le K`$, this proves (1). ∎

## Corollary: necessary energy for a fixed positive rate

For either $`X=Q_2`$ or $`X=K`$, if $`X(\eta,J,E)\ge R\gt0`$, then

```math
E\ge
\frac{1-\eta}{4\eta}\,f^{-1}(R)\,J^2.
\qquad\text{(8)}
```

In particular, at fixed $`0\lt\eta\lt1`$, any sequence $`E_J=o(J^2)`$ obeys

```math
\lim_{J\to\infty}Q_2(\eta,J,E_J)
=
\lim_{J\to\infty}K(\eta,J,E_J)
=0.
```

This is an asymptotic rate statement. It does not assert zero capacity at a positive finite energy for a finite alphabet; a positive-rate construction for that case appears in [rate_energy.md](rate_energy.md).

