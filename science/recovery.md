# Exact recovery on a displaced finite data subspace

The construction in this page is a receiver operation that sometimes declares failure. On success it restores the ordinary pure-loss output exactly, including its correlations with any reference. The displacement energy is charged at the input. The channel is defined in [model.md](model.md).

Unambiguous discrimination and reciprocal-state constructions are established methods; see [Cai2024](../references/REFERENCES.md#cai2024) and the bosonic error-space discussion in [NP2025](../references/REFERENCES.md#np2025). The property needed here is an operator identity on an entire data subspace, together with a recovery bound uniform in the alphabet size.

## Finite data and a counted carrier

Fix $`M\in\mathbb N_0`$ and let

```math
\mathcal H_M=\operatorname{span}\{|0\rangle,\ldots,|M\rangle\},
\qquad
\Pi_M=\sum_{m=0}^{M}|m\rangle\langle m|.
```

Pure loss maps operators supported on $`\mathcal H_M`$ to operators supported on the same subspace.

For $`\alpha\in\mathbb C`$, the displacement operator is

```math
D(\alpha)=e^{\alpha a^\dagger-\overline\alpha a}.
```

Fix a real output carrier amplitude $`A\gt0`$, and displace the channel input by

```math
\beta=\frac{A}{\sqrt\eta}.
```

The displacement covariance of pure loss gives

```math
\mathcal L_\eta\!\left(D(\beta)XD(\beta)^\dagger\right)
=
D(A)\mathcal L_\eta(X)D(A)^\dagger.
```

For the cyclic phase angles $`\theta_j=2\pi j/J`$, define isometries from $`\mathcal H_M`$ into the physical output mode:

```math
W_j
=
D(Ae^{i\theta_j})e^{i\theta_j\hat n}\big|_{\mathcal H_M}.
```

Consequently, for every $`X`$ supported on $`\mathcal H_M`$,

```math
\mathcal N_{\eta,J}\!\left(D(\beta)XD(\beta)^\dagger\right)
=
\frac1J\sum_{j=0}^{J-1}
W_j\mathcal L_\eta(X)W_j^\dagger.
\tag{1}
```

The data cutoff is imposed before displacement. The actual channel input generally has infinite Fock support, with finite and explicitly counted mean energy.

## Theorem 2: an exact success instrument

Define

```math
V:\mathbb C^J\otimes\mathcal H_M\longrightarrow\mathcal H,
\qquad
V(|j\rangle\otimes|\varphi\rangle)=W_j|\varphi\rangle,
\qquad
G=V^\dagger V.
```

For every $`A\gt0`$, the finite matrix $`G`$ is positive definite. Put

```math
s=\lambda_{\min}(G),
\qquad
R_j=(\langle j|\otimes I_{\mathcal H_M})G^{-1}V^\dagger.
\tag{2}
```

There is a receiver instrument with success branches

```math
\mathcal F_j(Y)=sR_jYR_j^\dagger
```

and a failure branch. It satisfies

```math
\mathcal F_j\!\left[
\mathcal N_{\eta,J}\!\left(D(\beta)XD(\beta)^\dagger\right)
\right]
=
\frac{s}{J}\mathcal L_\eta(X)
\tag{3}
```

for every operator $`X`$ supported on $`\mathcal H_M`$. Thus the total success map is exactly $`s\mathcal L_\eta`$. Its success probability is $`s`$, independent of the data state. Equations (1)–(3) remain valid after tensoring every map with the identity on an arbitrary reference.

### Proof of linear independence

In the Bargmann representation, the vector $`D(\alpha)|m\rangle`$ is, up to a nonzero scalar,

```math
e^{\alpha z}(z-\overline\alpha)^m.
```

The phase factor in $`W_j|m\rangle`$ only multiplies this vector by a nonzero scalar. For each fixed $`j`$, its $`M+1`$ polynomial factors form a basis of the polynomials of degree at most $`M`$.

The amplitudes $`\alpha_j=Ae^{i\theta_j}`$ are distinct. Suppose that

```math
\sum_{j=0}^{J-1}e^{\alpha_jz}P_j(z)=0,
\qquad
\deg P_j\le M.
```

Fix $`j`$ and apply

```math
\prod_{\ell\ne j}(\partial_z-\alpha_\ell)^{M+1}.
```

Every term except the $`j`$th vanishes. The remaining polynomial is obtained from $`P_j`$ by

```math
\prod_{\ell\ne j}
(\partial_z+\alpha_j-\alpha_\ell)^{M+1}.
```

Each factor is invertible on the finite-dimensional polynomial space: its matrix is triangular with nonzero diagonal because $`\alpha_j-\alpha_\ell\ne0`$. Thus $`P_j=0`$. This holds for every $`j`$, proving independence of all columns of $`V`$ and hence $`G\gt0`$.

### Proof of instrument validity and exact recovery

From (2),

```math
R_jW_\ell=\delta_{j\ell}I_{\mathcal H_M}.
\tag{4}
```

Also,

```math
\sum_jR_j^\dagger R_j=VG^{-2}V^\dagger.
```

Write the polar decomposition $`V=WG^{1/2}`$, where $`W`$ is an isometry on the finite domain. The last operator is $`WG^{-1}W^\dagger`$, whose nonzero eigenvalues are $`1/\lambda_k(G)`$. Therefore

```math
s\sum_jR_j^\dagger R_j\le I_{\mathcal H}.
\tag{5}
```

The success maps are trace nonincreasing and can be completed by a failure map with effect $`I-s\sum_jR_j^\dagger R_j`$. For example, the failure map can place its trace weight in a separate failure flag. Since each diagonal Gram block is the identity, a Rayleigh quotient supported on one block equals one; therefore $`0\lt s\le1`$.

Substitution of (4) into (1) gives (3). The proof is an operator identity, so reference correlations are preserved without any additional hypothesis. ∎

The outcome label $`j`$ is produced by the receiver's filter; no phase or loss label is supplied by the channel. Inconclusive events are essential to the validity of the instrument.

## An explicit displacement envelope

For $`d\ge0`$, define a polynomial with nonnegative coefficients:

```math
B_M(d)
=
\sum_{m,n=0}^{M}\sqrt{m!\,n!}
\sum_{k=0}^{\min(m,n)}
\frac{d^{m+n-2k}}
{(m-k)!(n-k)!k!}.
\tag{6}
```

Its degree is $`2M`$. Normal ordering gives

```math
D(\alpha)
=e^{-|\alpha|^2/2}
e^{\alpha a^\dagger}e^{-\overline\alpha a},
```

and hence

```math
\langle m|D(\alpha)|n\rangle
=
e^{-|\alpha|^2/2}\sqrt{m!\,n!}
\sum_{k=0}^{\min(m,n)}
\frac{\alpha^{m-k}(-\overline\alpha)^{n-k}}
{(m-k)!(n-k)!k!}.
```

Taking entrywise absolute values and bounding the operator norm by the sum of absolute matrix entries yields

```math
\|\Pi_M D(\alpha)\Pi_M\|
\le B_M(|\alpha|)e^{-|\alpha|^2/2}.
\tag{7}
```

This estimate is deliberately uniform rather than optimized.

## Lemma 3: uniform success with amplitude proportional to the alphabet size

For every fixed $`M`$ and $`0\lt\delta\lt1`$, there is a finite $`a=a(M,\delta)\gt0`$ such that choosing

```math
A=aJ
```

in Theorem 2 gives

```math
s\ge1-\delta
```

for every $`J\ge2`$.

**Proof.** The off-diagonal Gram block $`G_{j\ell}=W_j^\dagger W_\ell`$ differs from a cutoff displacement matrix only by phase rotations and a scalar phase. Its norm is bounded by (7) at

```math
d_{j\ell}
=
|Ae^{i\theta_j}-Ae^{i\theta_\ell}|.
```

Let $`h=\min\{|j-\ell|,J-|j-\ell|\}`$. For $`1\le h\le J/2`$ and $`A=aJ`$,

```math
d_{j\ell}=2aJ\sin(\pi h/J)\ge4ah.
\tag{8}
```

The last inequality uses $`\sin x\ge2x/\pi`$ for $`0\le x\le\pi/2`$.

There are at most two entries at each positive circular separation in a block row. The Hermitian block Schur bound therefore gives

```math
\|G-I\|
\le
2\sum_{h=1}^{\infty}
\sup_{d\ge4ah}B_M(d)e^{-d^2/2}.
\tag{9}
```

For completeness, the block Schur bound follows by applying
$`|\langle x_j,G_{j\ell}x_\ell\rangle|
\le\|G_{j\ell}\|\,\|x_j\|\,\|x_\ell\|`$
and then the ordinary scalar row-sum bound. The at-most-two multiplicity in (9) is independent of $`J`$.

Choose $`a`$ so that $`4a\ge\sqrt{2M}`$. Each monomial $`d^r e^{-d^2/2}`$ with $`0\le r\le2M`$ is then nonincreasing throughout the relevant range. Thus the supremum in (9) is bounded by its value at $`4ah`$. Define

```math
c_h=B_M(4ah)e^{-8a^2h^2},
\qquad
\rho_M(a)=2^{2M}e^{-24a^2}.
```

Because the polynomial coefficients are nonnegative and its degree is at most $`2M`$,

```math
\frac{B_M(4a(h+1))}{B_M(4ah)}
\le\left(\frac{h+1}{h}\right)^{2M}
\le2^{2M}.
```

It follows that $`c_{h+1}\le\rho_M(a)c_h`$. Whenever $`\rho_M(a)\lt1`$, (9) yields the explicit uniform bound

```math
\|G-I\|
\le
\Omega_M(a)
:=
\frac{2B_M(4a)e^{-8a^2}}
{1-\rho_M(a)}.
\tag{10}
```

For fixed $`M`$, this expression tends to zero as $`a\to\infty`$. Choose a finite $`a`$ meeting the stated conditions and $`\Omega_M(a)\le\delta`$. Then

```math
s=\lambda_{\min}(G)\ge1-\|G-I\|\ge1-\delta,
```

uniformly for every alphabet size. ∎

There is no factor of $`J`$ in the row sum after grouping by circular separation. The sufficient input carrier energy is exactly

```math
|\beta|^2=\frac{a^2J^2}{\eta}.
```

## Input energy of the encoded data

For any data state with finite first and second field moments,

```math
D(\beta)^\dagger\hat nD(\beta)
=
\hat n+\beta a^\dagger+\overline\beta a+|\beta|^2.
```

The data marginals used in [rate_energy.md](rate_energy.md) are Fock diagonal, so their first field moments vanish. If their mean photon number is $`E_0`$, the actual transmitted mean is

```math
E_{\rm active}=E_0+\frac{a^2J^2}{\eta}.
\tag{11}
```

Equation (11) is the energy of every attempted active use, including attempts for which the receiver declares failure. The recovery theorem permits arbitrary local non-Gaussian operations; it does not supply a bound on circuit size or control precision.

