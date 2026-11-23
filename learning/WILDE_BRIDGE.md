# From Wilde to discrete phase noise and photon loss

A supplementary source is Mark M. Wilde, *Quantum Information Theory*, second edition, Cambridge University Press (2017), [DOI 10.1017/9781316809976](https://doi.org/10.1017/9781316809976). The [publisher's contents](https://assets.cambridge.org/97811071/76164/frontmatter/9781107176164_frontmatter.pdf) fix the section numbers below. A freely accessible [author version, arXiv:1106.1445v8](https://arxiv.org/abs/1106.1445v8), was revised in July 2019 and includes corrections; it is an access version of the 2017 book. See [Wilde2017](../references/REFERENCES.md#wilde2017) for the bibliographic record.

The [Holevo bridge](HOLEVO_BRIDGE.md) is the main reading route and covers the displacement extension. Wilde supplies the language of states, channels, entropy and communication. This bridge develops the additional optical model and explains where each part enters the energy theorem. The [30-milestone map](MILESTONES.md) gives the complete conceptual route; the linked scientific pages contain the precise statements and proofs.

## Reading map

Consult these sections as the corresponding ideas arise. The project does not require reading the entire book first.

| Wilde location | Foundation to use | Where it enters this project |
|---|---|---|
| Sections 3.2–3.8 and 5.1 | States, measurements, composite systems, entanglement and purification | An input may be entangled with a retained reference; [the converse](../science/converse.md#lemma-1-an-environment-extension-valid-for-every-reference) must cover that full state. |
| Sections 4.1–4.5 and 5.2 | Mixed states, measurements, channels and isometric extensions | [Photon loss and phase averaging](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet) have inaccessible environment systems. |
| Sections 4.2 and 5.3 | Measurements with recorded outcomes and quantum instruments | [The recovery](../science/recovery.md#theorem-2-an-exact-success-instrument) has successful outcomes and an explicit failure outcome. |
| Sections 10.1–10.3 | Classical entropy and conditioning | The [lost-photon estimate](../science/converse.md#lemma-2-a-prior-uniform-integer-estimation-bound) bounds the uncertainty left about an input number. |
| Sections 11.1–11.2, 11.4–11.7 and 11.9 | Quantum entropy, coherent information, conditional mutual information and their inequalities | These connect [environment information to an upper bound](../science/converse.md#squashed-entanglement-and-the-imported-capacity-theorem) and [retained correlations to an attainable rate](../science/rate_energy.md#finite-data-and-reverse-coherent-information). |
| Sections 9.1–9.3 | Trace distance and fidelity | The [capacity definitions](../science/model.md#two-way-capacities) require error to vanish with coding length. |
| Sections 24.3–24.4 | Quantum capacity and direct coherent-information coding | The [critical crossover](../science/critical-crossover.md) uses forward coherent information. The mean-photon constraint is handled by the energy-constrained extension cited there. |
| Sections 19.2, 24.1 and 24.9 | Local operations with classical communication, coding tasks and distillation | [Hashing after heralding](../science/rate_energy.md#exact-heralding-followed-by-hashing) produces reliable entanglement from noisy shared pairs. |

## Notation and resources

The same mathematical symbol can play different roles in different accounts. Use these translations when moving between the anchor and the project.

| Notation here | Meaning |
|---|---|
| $`S(A)_\rho`$ | Quantum entropy of a reduced state; Wilde generally writes $`H(A)_\rho`$. |
| $`H(\mathsf N)`$ | Shannon entropy of a classical random variable. It need not equal the entropy of a quantum state with that photon-number distribution. |
| Systems $`R,A,B`$ | Retained reference, transmitted input and received output. The scalar target rate $`R`$ is distinguished by context. |
| $`\hat n`$ and $`E`$ | Photon-number observable and unconditional mean input photons per channel use. The scalar $`E`$ is a resource budget. |
| $`J`$ and $`\eta`$ | Number of equally spaced phase possibilities and photon transmissivity. The phase is redrawn independently each use. |
| $`Q`$, $`Q_2`$ and $`K`$ | Unassisted quantum, two-way quantum and two-way secret-key capacities under the same energy constraint. |

The [operational model](../science/model.md#protocols-and-average-input-energy) permits local quantum processing and public two-way classical messages. It starts without shared entanglement or secret key. Every transmitted optical mode is a counted channel use, and every input photon counts, including the displacement carrier. The energy average includes adaptive histories, failed recovery attempts and idle uses. This permits rare bright signals and photon distributions with infinite variance; it requires only a finite mean.

## The optical model

A Fock state $`|n\rangle`$ contains exactly $`n`$ photons in one mode. A phase rotation multiplies it by a number-dependent phase. For the cyclic alphabet,

```math
U_j|n\rangle=e^{2\pi ijn/J}|n\rangle.
```

Two photon numbers acquire the same factor whenever their difference is a multiple of $`J`$. Averaging the unknown phase therefore removes coherences between different residues modulo $`J`$, while retaining coherences within a residue. The full [channel definition](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet) writes this as a sum over residue projectors.

For a small example, take $`J=3`$ and an input $`a|0\rangle+b|3\rangle`$, with $`|a|^2+|b|^2=1`$. Each of the three phase rotations leaves this state unchanged. Its mean photon number is $`3|b|^2`$. If photon loss is then present, a nonzero lost-photon count can only have come from the three-photon component. The environment can thus learn something about the encoded state even though cyclic phase noise alone preserves it. This illustrates why residue protection does not eliminate the effect of loss.

Pure loss sends each of the input photons to the environment with probability $`q=1-\eta`$. Conditional on an input number $`\mathsf N=n`$, the number lost obeys $`\mathsf L\sim\mathrm{Bin}(n,q)`$. This conditional classical law is useful in the proof, while the actual input may remain a quantum superposition entangled with a reference.

## The converse

Start from purification and conditional mutual information. A channel environment can be processed mathematically to construct an extension of the reference-output state. Squashed entanglement is one half of the infimum of conditional mutual information over such extensions. For this channel, one particular extension records the lost-photon count and the input residue. It gives

```math
E_{\rm sq}(R:B)
\le H(\mathsf N\mid\mathsf L,\mathsf N\bmod J).
```

The right side measures the uncertainty about the original photon number after those two observations. Its appearance does not assume that the reference states for different photon numbers are orthogonal. The [branch argument](../science/converse.md#lemma-1-an-environment-extension-valid-for-every-reference) explicitly handles arbitrary reference vectors. The recorded environment labels are part of the upper-bound construction; the communicating parties receive no such flags.

The loss count estimates $`q\mathsf N`$. After the residue is known, the remaining candidate photon numbers are separated by $`J`$. The [rounded estimator](../science/converse.md#lemma-2-a-prior-uniform-integer-estimation-bound) exploits this separation. Its error bound depends on $`E/J^2`$: the conditional binomial variance is linear in the input number. Taking that conditional variance before averaging is what allows a finite-mean distribution with infinite variance.

The passage from this one-use estimate to arbitrary adaptive communication is a separate research ingredient. [DSW2018](../references/REFERENCES.md#dsw2018), published after Wilde's 2017 edition, supplies the required average-energy capacity theorem. The [converse page](../science/converse.md#squashed-entanglement-and-the-imported-capacity-theorem) checks its entropy and energy hypotheses. This use preserves the unconditional average constraint; it does not silently impose an energy cap on every use or history.

## Exact recovery

The receiver needs to preserve unknown quantum data while resolving which phase branch occurred. Distinguishing a list of known signal states alone would not establish this property.

Choose a finite data space spanned by $`|0\rangle,\ldots,|M\rangle`$ and add a displacement carrier. After loss, the different phases place rotated copies of this data space around a circle of output amplitude $`A`$. Let $`W_j`$ embed the data in branch $`j`$. The [reciprocal construction](../science/recovery.md#theorem-2-an-exact-success-instrument) produces operators $`R_j`$ satisfying

```math
R_jW_\ell=\delta_{j\ell}I.
```

This is an identity on the entire data space. It therefore preserves superpositions and correlations with any reference. A normalization determined by the smallest Gram eigenvalue makes these operators valid success branches of a quantum instrument. The remaining probability belongs to an inconclusive failure branch. Conditional on success, the output is exactly the ordinary pure-loss output of the data.

Adjacent carrier locations are separated by $`2A\sin(\pi/J)`$. A carrier proportional to $`J`$ keeps this separation bounded away from zero as the alphabet grows. The [uniform Gram estimate](../science/recovery.md#lemma-3-uniform-success-with-amplitude-proportional-to-the-alphabet-size) controls all branch overlaps together and proves a success bound independent of $`J`$. For the Fock-diagonal data marginal used in the rate construction,

```math
A=aJ,
\qquad
E_{\rm active}=E_0+\frac{a^2J^2}{\eta}.
```

Here $`E_0`$ is the data's mean photon number; the second term is the input carrier energy. The data cutoff is imposed before displacement. The transmitted state generally has infinite Fock support, so a finite data dimension is not a photon-number ceiling on the physical signal. The construction permits arbitrary local receiver operations and does not bound their implementation complexity.

## Rates and limits

Wilde's Section 24.9 provides the finite-dimensional distillation setting. Here Bob sends classical messages to Alice, giving the reverse coherent information of the accepted pair,

```math
I_{\rm rev}=S(R)-S(RB)=H(p)-H(\mathsf L),
```

where $`p`$ is the data's photon-number distribution. The optical channel still carries the signal from Alice to Bob; only the distillation messages are reversed. The [rate derivation](../science/rate_energy.md#finite-data-and-reverse-coherent-information) establishes the entropy identity and cites [DW2005](../references/REFERENCES.md#dw2005) and [Reverse2009](../references/REFERENCES.md#reverse2009).

For any fixed target below the pure-loss endpoint, an explicit tail estimate first chooses a finite data cutoff with a strictly larger reverse rate. That cutoff is fixed before either the phase alphabet or coding length grows. The [finite-cutoff lemma](../science/rate_energy.md#lemma-4-a-fixed-finite-cutoff-suffices-below-the-pure-loss-endpoint) is what permits use of finite-dimensional hashing without an uncontrolled interchange of limits.

If the recovery succeeds with probability $`s_J`$, the attainable rate per attempted use approaches $`s_J I_{\rm rev}`$. The [fixed-length construction](../science/rate_energy.md#exact-heralding-followed-by-hashing) reserves a predetermined number of accepted pairs and lets the probability of insufficient successes vanish. Failed attempts remain in both the rate denominator and the energy accounting.

Combining this construction with the converse gives the [matching quadratic law](../science/rate_energy.md#theorem-3-fixed-rate-photon-energy). The pure-loss endpoint is supplied by [PLOB2017](../references/REFERENCES.md#plob2017); the project determines the additional energy order required by the growing discrete phase alphabet. At exactly zero loss, the protected residue subspace gives the [linear benchmark](../science/rate_energy.md#theorem-4-exact-lossless-benchmark). The final [interpretation](../science/interpretation.md) connects these statements to positive rates at every finite alphabet, the order of the continuous-phase and high-energy limits, and the physical scope of the receiver model.

## The critical crossover

The fixed-loss proof uses a carrier to recover the phase branch. In the crossover, use an input supported on one photon-number residue chosen as part of a fixed schedule. The cyclic phase has the same action on all number states in that residue. If $`N`$ photons enter, $`L`$ are lost and $`B=N-L`$ arrive, Bob's output determines $`L\bmod J`$ through the known input residue. A local measurement can reveal this label while preserving coherence within the corresponding output subspace.

For a Fock-diagonal input in one residue, the joint output with its canonical reference has orthogonal loss branches. Wilde's coherent information and the classical chain rule give

```math
I_{\mathrm c}=H(B)-H(L)=H(N\mid L)-H(L\mid B).
```

Once Bob's photon number is given, any uncertainty about $`L`$ lies in the integer quotient $`\lfloor L/J\rfloor`$. Its mean is at most the mean lost count divided by $`J`$. The thermal entropy bound and a fixed schedule over input residues then give a gap of at most $`g(qE/J)`$ between unassisted quantum and two-way secret-key capacity. The [finite-alphabet proof](../science/critical-crossover.md#the-finite-alphabet-bound) uses the unrestricted adaptive converse and [Wilde and Qi's energy-constrained coding theorem](https://arxiv.org/abs/1609.01997). The coding theorem turns the coherent information of the fixed schedule into a rate without classical assistance.

Let $`E=eJ`$ and let the loss probability $`q_J`$ satisfy $`Jq_J\to\lambda`$. Split the rescaled input number into a fractional residue $`A=(N\bmod J)/J`$ and the integer index $`U=\lfloor N/J\rfloor`$. Then $`N/J=A+U`$ and the lost count tends to a Poisson law of mean $`\lambda(A+U)`$. The exact limiting capacity is the supremum of $`H(U\mid L,A)`$ at mean cost $`\mathbb E[A+U]\le e`$. At fixed $`J`$ the code first makes its error vanish with block length. The [limit proof](../science/critical-crossover.md#exact-capacity-in-the-critical-window) then controls the Poisson approximation uniformly over input laws using only the mean energy. It also explains how continuum residue offsets are realized by physical residues in the limit.

In the [two-level example](../science/critical-crossover.md#a-two-level-example), the input is equally likely to have zero or $`J`$ photons and the loss probability is $`1/J`$. A nonzero lost count reveals the occupied level, so the residual uncertainty comes from the runs in which zero photons were lost. The resulting rate approaches about $`0.57447`$ qubits per channel use at a mean of $`J/2`$ input photons. This is the rate of the specified input distribution. The full curve also optimizes the fractional residue and the distribution over indices.

[Learning overview](README.md) · [30 milestones](MILESTONES.md) · [Scientific route](../science/README.md)
