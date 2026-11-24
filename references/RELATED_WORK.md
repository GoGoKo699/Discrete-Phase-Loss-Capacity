# Related work and contribution boundary

This comparison concerns the model and theorem in [model.md](../science/model.md), [converse.md](../science/converse.md), [recovery.md](../science/recovery.md), and [rate_energy.md](../science/rate_energy.md). The [critical crossover](../science/critical-crossover.md) extends the channel model to shrinking loss at linear energy. The bibliography is in [REFERENCES.md](REFERENCES.md) and [references.bib](references.bib). This is a bounded comparison of the closest identified results, not an exhaustive priority claim.

## The precise result being compared

Each use of a single optical mode undergoes a uniformly chosen phase rotation from the known cyclic alphabet of size $`J`$, independently of every other use, together with quantum-limited pure loss of fixed transmissivity $`0\lt \eta\lt 1`$. The resource is the unconditional mean number of photons sent through the channel, averaged over uses and adaptive histories. Bright displacement carriers count toward that resource. There is no additional transmitted reference mode, realized-phase side information, or initial shared entanglement.

For any fixed target rate $`0\lt R\lt  -\log_2(1-\eta)`$, the project proves that the minimum mean input energy for two-way entanglement generation or secret-key generation is $`\Theta_{\eta,R}(J^2)`$. Its explicit weak converse is


```math
Q_2(\eta,J,E)\le K(\eta,J,E)
\le\min\left\{-\log_2(1-\eta),\,
g(u)+\min\{u,1\}\right\},\qquad
u=\frac{4\eta E}{(1-\eta)J^2},
```


where $`g(x)=(x+1)\log_2(x+1)-x\log_2x`$. A matching construction reaches every fixed rate below the pure-loss endpoint using energy $`O(J^2)`$. At $`\eta=1`$, the same resource convention gives the exact benchmark $`Q_2=K=g(E/J)`$, hence linear fixed-rate energy. At linear energy and inverse-alphabet loss probability, the crossover theorem identifies a common capacity limit from a Poisson loss count and bounds the advantage of two-way assistance at finite alphabet size.

## Results and methods inherited by the proof

| Source | What is inherited | What is established here |
|---|---|---|
| [Christandl–Winter 2004](REFERENCES.md#cw2004), [Takeoka–Guha–Wilde 2014](REFERENCES.md#tgw2014), [Davis–Shirokov–Wilde 2018](REFERENCES.md#dsw2018) | Squashed entanglement and its use to bound adaptive quantum and secret-key communication; the infinite-dimensional, average-energy theorem used here is DSW Theorem 4. | A channel-specific environment measurement and a modular/binomial estimate valid for every finite-mean photon distribution yield the displayed $`E/J^2`$ bound. |
| [Pirandola–Laurenza–Ottaviani–Banchi 2017](REFERENCES.md#plob2017) | The unconstrained pure-loss endpoint $`Q_2=K=-\log_2(1-\eta)`$; data processing supplies the same ceiling after phase randomization. | The energy needed to maintain a fixed rate below this inherited endpoint as the phase alphabet grows. |
| [Devetak–Winter 2005](REFERENCES.md#dw2005), [García-Patrón et al. 2009](REFERENCES.md#reverse2009) | One-way hashing and its reverse-reconciliation form, with achievable rate $`S(A)-S(AB)`$. | A finite-support input with a strict rate margin, an exact heralded reduction to pure loss, and a uniform success bound with all attempts and carrier photons charged. |

The use of a measured environment is mathematical: it bounds the channel's squashed entanglement and does not grant the receiver access to lost photons or to the phase label. DSW's Gibbs-observable and output-entropy hypotheses are checked in the [converse](../science/converse.md). The new entropy estimate uses the conditional variance of the binomial loss count and requires only the first moment of input photon number. It does not impose a photon-number variance bound or a physical input cutoff.

## Closest external comparisons

### Weak Gaussian displacement and number-preserving dephasing

[Arqand and Smith](REFERENCES.md#arqandsmith2026) derive the finite-energy equality of assisted and unassisted capacities for number-preserving bosonic dephasing through an amortized relative-entropy comparison to complete dephasing. Gaussian displacement mixes received numbers. The [critical displacement theorem](../science/critical-displacement.md) applies the comparison after providing the receiver with a net-shift flag, then controls the cost of removing that flag using a number-residue code. [Ivan, Sabapathy and Simon](REFERENCES.md#iss2011) give the attenuation–amplification decomposition used to build the dilation. At the critical scale the loss and gain counts become conditionally independent Poisson variables, but their amplitudes within a shift block remain coherent. Those coherences cause a strict capacity separation from a shift-only channel with the same number transitions.

[Bosonic Noise Dimension](https://github.com/GoGoKo699/Bosonic-Noise-Dimension/blob/main/science/07-cyclic-phase.md) treats the operational comparison and connects it to the displacement-only resolution law. The project-level proof of optimality here uses the additional cyclic phase twirl and charges all input energy.

### Modular photon number and the crossover

[Michael et al.](REFERENCES.md#michael2016) and [Grimsmo, Combes and Baragiola](REFERENCES.md#grimsmo2020) establish the use of photon-number residues and generalized parity in bosonic codes. [Jacoby, Arnon-Friedman and Rosenblum](REFERENCES.md#jacoby2026) use modular number measurements to distill selected entangled two-cavity states. The crossover proof uses a known input residue and bounds the information in loss counts that agree modulo the alphabet size. Optimized coherent information approaches the adaptive converse, producing an exact limit across three communication tasks. [Wilde and Qi](REFERENCES.md#wildeqi2018) supply the constrained unassisted coding theorem. [Crossover proof](../science/critical-crossover.md)

[Falco et al.](REFERENCES.md#falco2026) derive the finite-energy assisted capacity for the pure-loss channel. A cyclic twirl adds a residue label in the environment and changes which photon-number coherences survive. The Poisson posterior in the crossover depends on this extra channel structure.

### Bosonic loss and continuous phase diffusion

[Leviant et al. 2022](REFERENCES.md#leviant2022) study quantum-capacity bounds and numerically optimized codes for combined bosonic loss and dephasing. [Mele et al. 2024](REFERENCES.md#mele2024) give stronger structural results for the loss-dephasing channel, including an antidegradable region and positive two-way rates at positive transmissivity and finite Gaussian phase-diffusion strength. Their Theorem 3 uses a heralded multirail construction.

These works establish the importance of studying loss and dephasing together. Their Gaussian dephasing model suppresses a coherence according to the number difference. The exact cyclic twirl here removes coherences across residues modulo $`J`$. Independent phase jitter then suppresses the coherences within each residue according to its folded Fourier coefficients. The [broadened-alphabet theorem](../science/phase-jitter.md#fixed-loss-rate-threshold) asks for a rate bounded away from zero as $`J`$ grows at fixed loss. Its receiver accepts a band of typical binomial loss counts. The fixed-parameter no-loss construction in Mele et al. yields no such bound for the growing alphabet. [Bennett et al.](REFERENCES.md#bbpssw1996) supply the distillation step for the accepted Bell states.

### Number–phase codes and unambiguous recovery

[Hu et al. 2025](REFERENCES.md#np2025) develop generalized number–phase lattice codes and analyze correction of loss and dephasing, code performance, and repeater communication. Their main Eqs. (16) and (19)–(21) and supplementary analysis provide a close coding comparison. In particular, phase-error subspaces and their discrimination are established coding ideas; this project does not claim to introduce them.

[Cai et al. 2024](REFERENCES.md#cai2024) study unambiguous discrimination of quantum operations using designed probes and measurements, including reciprocal-state constructions. The algebra of reciprocal vectors and Gram inversion is an inherited method. The [recovery proof](../science/recovery.md) applies it to a full finite Fock data subspace: the reciprocal operators satisfy $`R_jW_\ell=\delta_{j\ell}I`$, so the success branch preserves data entangled with an arbitrary reference. A summable bound on all off-diagonal Gram blocks makes success uniformly close to one for growing $`J`$ when the displacement amplitude is proportional to $`J`$.

The contribution is the combination of that uniform recovery estimate with a converse covering all encoders and adaptive key protocols. It is not the general idea of quantum data correction, unambiguous discrimination, or number–phase encoding. The achievability model allows arbitrary local operations and does not establish an efficient or Gaussian-only receiver.

### Lossy phase metrology

[Escher, de Matos Filho, and Davidovich 2011](REFERENCES.md#escher2011), Eqs. (11)–(12), bound the quantum Fisher information for lossy phase estimation. Their bound implies $`F_Q\le4\eta E/(1-\eta)`$, displaying the familiar loss-induced shot-noise scaling. This is a close physical antecedent: distinguishing angular spacings of order $`1/J`$ suggests an energy cost of order $`J^2`$.

That suggestion is not itself the communication converse. An arbitrary channel code need not estimate a phase, and a phase estimator need not preserve entanglement. The present theorem connects the familiar optical scaling to an all-protocol assisted communication bound and a matching data-preserving construction. It does not claim discovery of shot-noise physics.

### Phase memory, pure dephasing, and source randomization

| Comparison | Contract in the source | Distinction needed here |
|---|---|---|
| [Zhuang 2021](REFERENCES.md#zhuang2021) | Communication without a phase reference when a random phase is shared across a block of modes; exact lossless results and results involving entanglement assistance and thermal loss. | Here the phase is redrawn independently on every single-mode use. Shared phase across several modes supplies a different channel with memory. Pre-shared entanglement is also not supplied here. |
| [Lami–Wilde 2023](REFERENCES.md#phase2023) | Exact unconstrained quantum and private capacities, including assisted versions, for bosonic dephasing described by a phase density; Theorem S7 states the regularity hypothesis. | This is a pure-dephasing result without photon loss. A finite atomic phase law is not a probability density, and the present claim concerns energy-constrained fixed-rate behavior with loss. |
| [Cao et al. 2015](REFERENCES.md#cao2015) | Discrete phase randomization of a coherent-state source and security of an associated quantum-key-distribution protocol. | A source-randomization security result has a specified preparation and encoding contract. It does not evaluate the optimized secret-key capacity of the single-mode phase-and-loss channel defined here. |

The [moving-harmonic example](../science/phase-jitter.md#a-moving-harmonic-raises-the-energy-scale) keeps Lami–Wilde's phase-only capacity constant while raising the minimum energy scale for positive rate under fixed loss. The lost-photon count limits the range of quotient differences that can carry information at a given energy. The [weak-loss jitter limit](../science/phase-jitter.md#exact-capacity-at-weak-loss-and-displacement) uses the pinching method of [Arqand and Smith](REFERENCES.md#arqandsmith2026) together with the shift-resolving code already used for weak displacement. Phase tags preserve the information about the transmitted quotient that is carried by the residual rotation.

## Internal antecedents at pinned revisions

Two existing project sources supply particularly close comparisons. These are repository records, not journal publications.

**[Bosonic-Phase-Noise-Capacity](REFERENCES.md#internalphase)**, main commit `2080352d5c356b3a87d8cc8780b787bc3ca0fc5f`, treats independent phase randomization under a mean-energy constraint and explicitly excludes photon loss. The inspected model and capacity pages give the relevant lossless phase-law antecedent. They do not establish the fixed-loss quadratic threshold.

**[Quantum-Group-Memory-Laws](REFERENCES.md#internalgroup)**, main commit `0d585db681ebc66fe0f2c7acb75f0c636869beef`, already uses an environment measurement, a hidden-label conditional-entropy bound, and adaptive squashed-entanglement reasoning. Those proof ideas are shared and are credited as such. Its finite-deformation spin-chain projection and local-erasure model yields a different capacity ceiling. The bosonic binomial loss estimate, modular uncertainty bound, charged-energy scaling, and matching optical recovery are the specific additions here.

## Supported contribution statement

For the exact cyclic alphabet, the project supplies matching mean-energy orders at every fixed assisted rate below the pure-loss endpoint. With independent phase jitter, it gives the necessary and sufficient folded-law criterion for positive assisted rate at quadratic energy. Uniform performance comes from a receiver using typical losses and a converse valid for all finite-mean encoders. The exact linear-energy limit covers the regime of inverse-alphabet loss and displacement and includes the residual phase law. Exact capacity at general fixed positive loss and the hardware cost of the receivers remain open.
