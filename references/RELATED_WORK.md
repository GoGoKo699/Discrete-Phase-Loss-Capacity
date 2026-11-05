# Related work and contribution boundary

This comparison concerns the model and theorem in [model.md](../science/model.md), [converse.md](../science/converse.md), [recovery.md](../science/recovery.md), and [rate_energy.md](../science/rate_energy.md). Primary metadata and the relevant statements were checked on 2026-11-05. The bibliography is in [REFERENCES.md](REFERENCES.md) and [references.bib](references.bib). This is a bounded comparison of the closest identified results, not an exhaustive priority claim.

## The precise result being compared

Each use of a single optical mode undergoes a uniformly chosen phase rotation from the known cyclic alphabet of size $`J`$, independently of every other use, together with quantum-limited pure loss of fixed transmissivity $`0\lt \eta\lt 1`$. The resource is the unconditional mean number of photons sent through the channel, averaged over uses and adaptive histories. Bright displacement carriers count toward that resource. There is no additional transmitted reference mode, realized-phase side information, or initial shared entanglement.

For any fixed target rate $`0\lt R\lt  -\log_2(1-\eta)`$, the project proves that the minimum mean input energy for two-way entanglement generation or secret-key generation is $`\Theta_{\eta,R}(J^2)`$. Its explicit weak converse is


```math
Q_2(\eta,J,E)\le K(\eta,J,E)
\le\min\left\{-\log_2(1-\eta),\,
g(u)+\min\{u,1\}\right\},\qquad
u=\frac{4\eta E}{(1-\eta)J^2},
```


where $`g(x)=(x+1)\log_2(x+1)-x\log_2x`$. A matching construction reaches every fixed rate below the pure-loss endpoint using energy $`O(J^2)`$. At $`\eta=1`$, the same resource convention gives the exact benchmark $`Q_2=K=g(E/J)`$, hence linear fixed-rate energy. The lossy result does not determine the exact finite-energy capacity or a joint limit in which $`\eta`$ approaches one with $`J`$.

## Results and methods inherited by the proof

| Source | What is inherited | What is established here |
|---|---|---|
| [Christandl–Winter 2004](REFERENCES.md#cw2004), [Takeoka–Guha–Wilde 2014](REFERENCES.md#tgw2014), [Davis–Shirokov–Wilde 2018](REFERENCES.md#dsw2018) | Squashed entanglement and its use to bound adaptive quantum and secret-key communication; the infinite-dimensional, average-energy theorem used here is DSW Theorem 4. | A channel-specific environment measurement and a modular/binomial estimate valid for every finite-mean photon distribution yield the displayed $`E/J^2`$ bound. |
| [Pirandola–Laurenza–Ottaviani–Banchi 2017](REFERENCES.md#plob2017) | The unconstrained pure-loss endpoint $`Q_2=K=-\log_2(1-\eta)`$; data processing supplies the same ceiling after phase randomization. | The energy needed to maintain a fixed rate below this inherited endpoint as the phase alphabet grows. |
| [Devetak–Winter 2005](REFERENCES.md#dw2005), [García-Patrón et al. 2009](REFERENCES.md#reverse2009) | One-way hashing and its reverse-reconciliation form, with achievable rate $`S(A)-S(AB)`$. | A finite-support input with a strict rate margin, an exact heralded reduction to pure loss, and a uniform success bound with all attempts and carrier photons charged. |

The use of a measured environment is mathematical: it bounds the channel's squashed entanglement and does not grant the receiver access to lost photons or to the phase label. DSW's Gibbs-observable and output-entropy hypotheses are checked in the [converse](../science/converse.md). The new entropy estimate uses the conditional variance of the binomial loss count and requires only the first moment of input photon number. It does not impose a photon-number variance bound or a physical input cutoff.

## Closest external comparisons

### Bosonic loss and continuous phase diffusion

[Leviant et al. 2022](REFERENCES.md#leviant2022) study quantum-capacity bounds and numerically optimized codes for combined bosonic loss and dephasing. [Mele et al. 2024](REFERENCES.md#mele2024) give stronger structural results for the loss-dephasing channel, including an antidegradable region and positive two-way rates at positive transmissivity and finite Gaussian phase-diffusion strength. Their Theorem 3 uses a heralded multirail construction.

These works directly establish the importance of studying loss and dephasing together. Their principal dephasing model suppresses a number-basis coherence by a Gaussian function of its number difference. Here, the exact cyclic twirl instead removes coherences between distinct residues modulo $`J`$ while preserving coherences within each residue. The question is the mean energy needed at a fixed assisted communication rate as $`J`$ grows. An antidegradability statement about unassisted quantum capacity must not be substituted for a statement about $`Q_2`$ or $`K`$.

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

Finite phase atoms, a continuous phase density, and a phase shared across a block are distinct noise models. A phase alphabet becoming dense does not justify exchanging the alphabet-size, energy, and coding limits. Robustness of this construction to continuous broadening of the atoms remains outside the proved result.

## Internal antecedents at pinned revisions

Two existing project sources supply particularly close comparisons. These are repository records, not journal publications.

**[Bosonic-Phase-Noise-Capacity](REFERENCES.md#internalphase)**, main commit `2080352d5c356b3a87d8cc8780b787bc3ca0fc5f`, treats independent phase randomization under a mean-energy constraint and explicitly excludes photon loss. The inspected model and capacity pages give the relevant lossless phase-law antecedent. They do not establish the fixed-loss quadratic threshold.

**[Quantum-Group-Memory-Laws](REFERENCES.md#internalgroup)**, main commit `0d585db681ebc66fe0f2c7acb75f0c636869beef`, already uses an environment measurement, a hidden-label conditional-entropy bound, and adaptive squashed-entanglement reasoning. Those proof ideas are shared and are credited as such. Its finite-deformation spin-chain projection and local-erasure model yields a different capacity ceiling. The bosonic binomial loss estimate, modular uncertainty bound, charged-energy scaling, and matching optical recovery are the specific additions here.

## Supported contribution statement

For the stated memoryless single-mode channel, the project supplies matching necessary and sufficient orders of mean energy at every fixed assisted quantum or secret-key rate below the pure-loss endpoint. The technically specific advance is a first-moment-only modular/binomial converse paired with an entanglement-preserving recovery whose success remains uniform as the cyclic phase alphabet grows. The exact finite-energy capacity, optimal constants, efficient implementation, broadened phase atoms, and a uniform lossless crossover are not claimed. The source comparisons above support this scoped contribution; they do not establish exhaustive priority.
