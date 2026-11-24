# Thirty milestones for discrete phase noise and photon loss

[Learning overview](README.md) · [Holevo bridge](HOLEVO_BRIDGE.md) · [Scientific account](../science/README.md)

How much mean photon energy is needed to keep a fixed communication rate as the number of possible phase rotations grows? The route connects one optical mode, the adaptive converse and a counted carrier construction at fixed loss. It then asks which photon-number coherences survive residual angular jitter and how that jitter enters the limiting capacity at weak loss and displacement. The [model](../science/model.md), [fixed-rate theorem](../science/rate_energy.md#theorem-3-fixed-rate-photon-energy) and [phase-jitter theorem](../science/phase-jitter.md) give the precise statements.

The educational anchor is **Alexander S. Holevo, *Quantum Systems, Channels, Information: A Mathematical Introduction*, second revised and expanded edition (2019)**. The [reading map](HOLEVO_BRIDGE.md#reading-map) identifies the textbook sections used below.

| Phase | Milestones | Scientific role |
|---|---|---|
| [Background and preliminaries](#background-and-preliminaries) | M01–M12 | Join states, entropy and quantum operations to one optical mode, its photon budget and the assisted communication task. |
| [Narrative and innovation](#narrative-and-innovation) | M13–M30 | Build the environment converse and carrier recovery, compare fixed loss with zero loss, and derive the harmonic criterion and critical capacity. |

The 12/18 allocation reflects these two bodies of work. The background phase ends with the complete communication problem. The narrative phase begins with the fixed-loss proof mechanisms and ends with the phase-sensitive capacity in the joint limit. Dependencies name earlier milestones; each source link leads to the authoritative statement or argument. Technical lemmas and detailed calculations remain in those sources.

## Background and preliminaries

### M01

**States and photon-number outcomes**

- **Central question:** What does the state of one optical mode specify?
- **Understanding target:** Relate a state, its photon-number probabilities and its mean photon number. Explain why the infinitely many number states belong to one mode and do not represent infinitely many channel uses.
- **Dependencies and story role:** None. This introduces the physical object whose energy and information will be tracked.
- **Conceptual connection:** Quantum-state notation acquires an observable meaning through photon counting.
- **Sources:** [Holevo §§2.2–2.3](HOLEVO_BRIDGE.md#reading-map); [one optical mode](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet).

### M02

**References and preserved entanglement**

- **Central question:** Why must a quantum communication claim describe what happens to a reference system?
- **Understanding target:** Explain reduced states, purification and entanglement. Distinguish preserving one prepared optical state from preserving its correlations with an arbitrary retained reference.
- **Dependencies and story role:** [M01](#m01). The description expands from one mode to the joint system that communication must protect.
- **Conceptual connection:** The reference tests whether a recovery operation preserves unknown quantum information.
- **Sources:** [Holevo §§3.1.1–3.1.3](HOLEVO_BRIDGE.md#reading-map); [the reference requirement in exact recovery](../science/recovery.md#theorem-2-an-exact-success-instrument).

### M03

**Classical and quantum entropy**

- **Central question:** What uncertainty is measured by the entropies in this project?
- **Understanding target:** Distinguish Shannon entropy of a photon-number law from von Neumann entropy of a state. Explain why finite mean photon number bounds both by the thermal entropy function, without requiring a finite number variance.
- **Dependencies and story role:** [M01](#m01), [M02](#m02). This supplies the information quantities used in both proof directions.
- **Conceptual connection:** A physical mean-energy constraint limits information even in an infinite-dimensional mode.
- **Sources:** [Holevo §§4.1–4.2 and 11.2](HOLEVO_BRIDGE.md#reading-map); [entropy notation and the mean-energy bound](../science/model.md#entropy-notation).

### M04

**Channels and their environments**

- **Central question:** How can a noisy channel be described as part of a larger quantum evolution?
- **Understanding target:** Connect a channel's Kraus operators, an isometric extension and the discarded environment. Explain why a receiver output and its complementary environment describe different parts of the same process.
- **Dependencies and story role:** [M01](#m01), [M02](#m02). This introduces the environment that will carry the information used in the converse.
- **Conceptual connection:** Lost information can be studied through correlations with a larger system.
- **Sources:** [Holevo §§6.4–6.7](HOLEVO_BRIDGE.md#reading-map); [the channel's loss and residue Kraus representation](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet).

### M05

**Conditioning and mixtures**

- **Central question:** What changes when a classical label is known?
- **Understanding target:** Read conditional Shannon entropy as an average over posterior distributions. Explain why a mixture of pure quantum states has entropy no greater than the entropy of its mixing weights, even when those states are not orthogonal.
- **Dependencies and story role:** [M02](#m02), [M03](#m03), [M04](#m04). This connects classical uncertainty with conditional quantum entanglement.
- **Conceptual connection:** A classical probability calculation can bound a quantum state without replacing that state by a classical input.
- **Sources:** [Holevo §§4.2 and 7.1–7.3](HOLEVO_BRIDGE.md#reading-map); [the posterior-mixture argument](../science/converse.md#lemma-1-an-environment-extension-valid-for-every-reference).

### M06

**Photon loss as binomial sampling**

- **Central question:** What can the loss environment learn from a number-state input?
- **Understanding target:** Explain the binomial lost-photon law for an input with a specified photon number. Relate transmissivity to the mean output energy and distinguish conditional fluctuations at a fixed input number from fluctuations of the input distribution itself.
- **Dependencies and story role:** [M01](#m01), [M04](#m04), [M05](#m05). A concrete optical channel now supplies the random variables needed by the converse.
- **Conceptual connection:** The same photon loss both damages the signal and carries information about its initial number.
- **Sources:** [the optical bridge](HOLEVO_BRIDGE.md#the-optical-model); [pure-loss Kraus operators](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet); [information carried away by lost photons](../science/interpretation.md#the-information-carried-away-by-lost-photons).

### M07

**Cyclic phases and surviving coherence**

- **Central question:** Which coherences survive a uniform finite phase alphabet?
- **Understanding target:** Explain why averaging equally spaced phase rotations removes coherence between different photon-number residues while retaining coherence within a residue class. Distinguish a fresh phase on every use from a phase shared across many uses.
- **Dependencies and story role:** [M01](#m01), [M04](#m04). This identifies the structure protected by phase randomization alone.
- **Conceptual connection:** A finite symmetry preserves a family of quantum subspaces, but their energy spacing depends on the alphabet size.
- **Sources:** [the optical bridge](HOLEVO_BRIDGE.md#the-optical-model); [cyclic twirling and residue projectors](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet); [protection without loss](../science/interpretation.md#protection-without-loss).

### M08

**Displacements and the carrier**

- **Central question:** How does a displacement make different phase branches easier to distinguish?
- **Understanding target:** Connect displacement amplitude to translated optical states and carrier photon energy. Explain pure-loss displacement covariance and why the simple sum of data and carrier energies used here relies on the chosen data marginal having zero first field moment.
- **Dependencies and story role:** [M01](#m01), [M06](#m06), [M07](#m07). This introduces the physical operation used by the achievable construction.
- **Conceptual connection:** The carrier carries branch information in the same transmitted mode, so its photons belong in the resource account.
- **Sources:** [the recovery bridge](HOLEVO_BRIDGE.md#the-carrier-and-the-residue); [finite data and a counted carrier](../science/recovery.md#finite-data-and-a-counted-carrier); [input energy](../science/recovery.md#input-energy-of-the-encoded-data).

### M09

**Unconditional mean energy**

- **Central question:** Which uses and measurement histories count toward the photon budget?
- **Understanding target:** Explain averaging across all uses and prior histories. Recognize that rare bright signals, idle uses and distributions with infinite photon-number variance are allowed when the unconditional mean is finite; failures and carrier photons still count.
- **Dependencies and story role:** [M03](#m03), [M06](#m06), [M08](#m08). The physical operations are placed under one common resource convention.
- **Conceptual connection:** A protocol-wide mean constraint is weaker than a peak or per-history cap, so the converse must cover a larger set of strategies.
- **Sources:** [notation and resources](WILDE_BRIDGE.md#notation-and-resources); [protocols and average input energy](../science/model.md#protocols-and-average-input-energy).

### M10

**Heralded quantum instruments**

- **Central question:** How can a recovery operation succeed exactly on some attempts and remain physically valid?
- **Understanding target:** Distinguish a success map from a complete instrument. Explain the trace bound on its success operators, the necessary failure outcome, and why conditioning on success does not remove failed attempts from the rate or energy denominator.
- **Dependencies and story role:** [M02](#m02), [M04](#m04), [M09](#m09). This supplies the operational language for the receiver construction.
- **Conceptual connection:** Exact conditional recovery is compatible with nonorthogonal signals when inconclusive outcomes are included.
- **Sources:** [Holevo §§2.4 and 6.5](HOLEVO_BRIDGE.md#reading-map); [instrument validity and exact recovery](../science/recovery.md#proof-of-instrument-validity-and-exact-recovery).

### M11

**Entanglement, key and two-way communication**

- **Central question:** What useful output is produced by a successful communication protocol?
- **Understanding target:** Explain an ebit, a secret bit and a rate per attempted channel use. Relate local operations and public classical communication to entanglement distillation, and explain why distilled entanglement provides secret key while public communication alone is not pre-shared key.
- **Dependencies and story role:** [M02](#m02), [M03](#m03), [M04](#m04), [M10](#m10). Local channel operations are connected to an asymptotic communication task.
- **Conceptual connection:** A recovery probability becomes useful only after it is converted into a reliable entanglement or key rate.
- **Sources:** [Holevo §§10.3.1–10.3.2](HOLEVO_BRIDGE.md#reading-map); [two-way capacities](../science/model.md#two-way-capacities); [reverse coherent information](../science/rate_energy.md#finite-data-and-reverse-coherent-information).

### M12

**The complete fixed-rate problem**

- **Central question:** What is held fixed, what grows, and what must a matching energy theorem prove?
- **Understanding target:** Assemble the known independent phase alphabet, fixed partial loss, permitted two-way operations and unconditional photon budget into one model. Distinguish alphabet size, coding block length and data cutoff. Explain why necessity and sufficiency must use the same rate and resource definitions, with the target strictly below the pure-loss endpoint.
- **Dependencies and story role:** [M06](#m06)–[M11](#m11). This integrates the background into the precise scientific question.
- **Conceptual connection:** Operational definitions determine which energy comparison is meaningful.
- **Sources:** [notation and resources](WILDE_BRIDGE.md#notation-and-resources); [model](../science/model.md); [fixed-rate theorem](../science/rate_energy.md#theorem-3-fixed-rate-photon-energy).

## Narrative and innovation

### M13

**An environment extension for the converse**

- **Central question:** How can a mathematical operation on the environment bound communication?
- **Understanding target:** Explain squashed entanglement as a minimization over extensions and why one chosen extension gives an upper bound. Identify the loss-count and residue labels in this extension without granting either label to the communicating parties.
- **Dependencies and story role:** [M03](#m03)–[M07](#m07), [M11](#m11), [M12](#m12). The first proof direction starts with a local environment construction.
- **Conceptual connection:** Conditional quantum information turns the channel's hidden records into a communication constraint.
- **Sources:** [Holevo §§7.2–7.3](HOLEVO_BRIDGE.md#reading-map); [squashed entanglement](../science/converse.md#squashed-entanglement-and-the-imported-capacity-theorem); [CW2004](../references/REFERENCES.md#cw2004).

### M14

**A posterior bound for every reference**

- **Central question:** Why does the classical photon posterior control entanglement for a fully quantum input?
- **Understanding target:** Follow the pure conditional reference–receiver states after the environment labels are measured. Explain how orthogonal receiver number states produce posterior mixing weights while the reference vectors may remain nonorthogonal. Recognize that no Fock-diagonal restriction is imposed on the converse inputs.
- **Dependencies and story role:** [M02](#m02), [M05](#m05), [M06](#m06), [M13](#m13). The environment construction becomes a bound valid for arbitrary reference-entangled inputs.
- **Conceptual connection:** A classical posterior bounds the entropy of the actual quantum branch, rather than substituting a different input.
- **Sources:** [the converse bridge](WILDE_BRIDGE.md#the-converse); [Lemma 1](../science/converse.md#lemma-1-an-environment-extension-valid-for-every-reference).

### M15

**The residue lattice and its estimator**

- **Central question:** How accurately does the lost-photon count locate the input on its residue lattice?
- **Understanding target:** Explain rescaling the lost count, subtracting the known residue and rounding the resulting lattice-index estimate. Show why the centered squared error is evaluated conditional on input photon number and therefore needs only its first moment, even for an infinite-variance input law.
- **Dependencies and story role:** [M06](#m06), [M07](#m07), [M09](#m09), [M14](#m14). The posterior problem is reduced to a prior-uniform integer error.
- **Conceptual connection:** Lattice spacing grows with the phase alphabet while conditional loss fluctuations grow with photon number.
- **Sources:** [the converse bridge](WILDE_BRIDGE.md#the-converse); [Lemma 2 and its conditional-moment calculation](../science/converse.md#lemma-2-a-prior-uniform-integer-estimation-bound).

### M16

**Small integer error means small entropy**

- **Central question:** How does a mean-squared estimation error bound the remaining information?
- **Understanding target:** Explain the one-to-one translation from the input lattice index to its integer error at fixed observations. Bound the entropy through the error's magnitude and sign, and identify the ratio of mean photons to squared alphabet size as the controlling scale.
- **Dependencies and story role:** [M03](#m03), [M05](#m05), [M15](#m15). The estimator yields an entropy bound that vanishes at subquadratic energy.
- **Conceptual connection:** An estimation statement supplies the specific entropy bound needed by the quantum converse.
- **Sources:** [the converse bridge](WILDE_BRIDGE.md#the-converse); [integer-error entropy in Lemma 2](../science/converse.md#lemma-2-a-prior-uniform-integer-estimation-bound); [entropy functions](../science/model.md#entropy-notation).

### M17

**From one use to every adaptive protocol**

- **Central question:** Why does the one-use entropy estimate constrain adaptive two-way communication?
- **Understanding target:** Identify the Gibbs-observable and finite-output-entropy hypotheses of the imported average-energy squashed-entanglement theorem. Explain its application to the unconditional protocol budget, the separate pure-loss ceiling, and the resulting quadratic necessary energy at fixed positive rate. Distinguish this weak converse from a strong-converse claim.
- **Dependencies and story role:** [M09](#m09), [M11](#m11)–[M16](#m16). This completes the universal necessity argument.
- **Conceptual connection:** A local information leak becomes a protocol-level limit through a theorem that permits adaptivity and energy averaging.
- **Sources:** [capacity-bound proof](../science/converse.md#proof-of-theorem-1); [necessary-energy corollary](../science/converse.md#corollary-necessary-energy-for-a-fixed-positive-rate); [DSW2018](../references/REFERENCES.md#dsw2018); [PLOB2017](../references/REFERENCES.md#plob2017).

### M18

**Displaced data and their Gram matrix**

- **Central question:** How does a fixed finite data subspace fit inside a displaced optical mode?
- **Understanding target:** Distinguish the finite-Fock data space from the full Fock support of the transmitted signal. Explain how the Gram matrix of the displaced and rotated output basis tests independence of all phase branches. Follow why distinct exponential-polynomial functions give a positive smallest eigenvalue at every fixed alphabet size.
- **Dependencies and story role:** [M06](#m06)–[M10](#m10), [M12](#m12). The constructive proof moves from the channel to a concrete encoding.
- **Conceptual connection:** The receiver must preserve an entire data subspace and its reference, so discrimination of a single probe is insufficient.
- **Sources:** [Finite data and the counted carrier](../science/recovery.md#finite-data-and-a-counted-carrier), [Gram construction](../science/recovery.md#theorem-2-an-exact-success-instrument) and [linear-independence proof](../science/recovery.md#proof-of-linear-independence).

### M19

**Reciprocal maps become a physical filter**

- **Central question:** How does an algebraic left inverse yield a valid receiver instrument?
- **Understanding target:** Use the reciprocal-operator identities and the smallest Gram eigenvalue to scale the total success effect below the identity. Explain how the resulting success operation recovers the pure-loss output with its arbitrary reference. Include the failure outcome.
- **Dependencies and story role:** [M02](#m02), [M04](#m04), [M10](#m10), [M18](#m18). The algebraic recovery becomes a local operation.
- **Conceptual connection:** The Gram eigenvalue controls both physical validity and success probability.
- **Sources:** [Holevo §§2.4 and 6.5–6.6](HOLEVO_BRIDGE.md#reading-map) and [instrument validity and exact recovery](../science/recovery.md#proof-of-instrument-validity-and-exact-recovery).

### M20

**Uniform success at quadratic carrier energy**

- **Central question:** Why does linear carrier amplitude suffice for a growing phase alphabet?
- **Understanding target:** Explain the polynomial-times-Gaussian overlap envelope for displaced finite-Fock data. Group Gram blocks by circular separation to find a summable row bound and a carrier coefficient independent of the alphabet size. Convert the amplitude to unconditional mean input photons.
- **Dependencies and story role:** [M07](#m07)–[M09](#m09), [M18](#m18), [M19](#m19). The receiver construction gains a quantitative resource bound.
- **Conceptual connection:** Circular separation controls the overlap sum and fixes the energy cost of making success uniformly close to one.
- **Sources:** [Displacement envelope](../science/recovery.md#an-explicit-displacement-envelope), [uniform Gram estimate](../science/recovery.md#lemma-3-uniform-success-with-amplitude-proportional-to-the-alphabet-size) and [encoded input energy](../science/recovery.md#input-energy-of-the-encoded-data).

### M21

**Reverse hashing on finite optical data**

- **Central question:** How much entanglement can be distilled from a successfully recovered pair?
- **Understanding target:** For the canonical finite-Fock purification, identify the reference entropy as the input number entropy and the joint output entropy as the lost-count entropy. Explain how their difference gives a reverse hashing rate with messages from receiver to sender.
- **Dependencies and story role:** [M02](#m02), [M03](#m03), [M06](#m06), [M11](#m11), [M18](#m18). A recovered quantum state receives an operational rate.
- **Conceptual connection:** Orthogonal loss sectors turn an entropy difference into a distillable resource.
- **Sources:** [Holevo §§10.3.1–10.3.2](HOLEVO_BRIDGE.md#reading-map), [finite data and reverse coherent information](../science/rate_energy.md#finite-data-and-reverse-coherent-information), [DW2005](../references/REFERENCES.md#dw2005) and [Reverse2009](../references/REFERENCES.md#reverse2009).

### M22

**One finite cutoff for a target rate**

- **Central question:** Why can the data cutoff be fixed before the alphabet size or coding length grows?
- **Understanding target:** Choose one finite-mean geometric distribution whose reverse rate exceeds the target. Use a tail-entropy estimate on the input number and lost count to retain that strict margin after taking a finite cutoff.
- **Dependencies and story role:** [M03](#m03), [M06](#m06), [M12](#m12), [M21](#m21). This makes finite-dimensional recovery sufficient below the pure-loss endpoint.
- **Conceptual connection:** Controlling two entropy tails converts an optical capacity benchmark into a finite data-space choice.
- **Sources:** [Limits in the Wilde reading notes](WILDE_BRIDGE.md#rates-and-limits) and [fixed finite-cutoff lemma](../science/rate_energy.md#lemma-4-a-fixed-finite-cutoff-suffices-below-the-pure-loss-endpoint).

### M23

**Fixed-length coding after heralding**

- **Central question:** How do random successes become a rate per attempted use?
- **Understanding target:** Plan a fixed number of attempts, reserve slightly fewer successes than the typical number, and abort the coding block upon a shortage. Multiply the recovered-pair rate by the success probability and include the energy from every attempt.
- **Dependencies and story role:** [M09](#m09)–[M11](#m11), [M19](#m19)–[M22](#m22). The local construction becomes a reliable communication protocol.
- **Conceptual connection:** Heralding reveals which pairs to use while the protocol averages over all attempted uses.
- **Sources:** [Limits in the Wilde reading notes](WILDE_BRIDGE.md#rates-and-limits) and [exact heralding followed by hashing](../science/rate_energy.md#exact-heralding-followed-by-hashing).

### M24

**Quadratic energy with loss, linear energy without it**

- **Central question:** Why does removing loss change the energy order?
- **Understanding target:** Combine the fixed-loss converse and carrier construction for a fixed target rate below the pure-loss endpoint. At zero loss, use the noiseless residue-zero subspace and the residue-conditioned entropy bound to derive the exact thermal-entropy benchmark. Explain why this gives a separate linear photon cost.
- **Dependencies and story role:** [M03](#m03), [M07](#m07), [M12](#m12), [M17](#m17), [M23](#m23). The two proof directions meet and their lossless endpoint becomes a comparison.
- **Conceptual connection:** Photon loss reveals information about the lattice index that cyclic phase averaging alone preserves.
- **Sources:** [Fixed-rate energy theorem](../science/rate_energy.md#theorem-3-fixed-rate-photon-energy) and [lossless benchmark](../science/rate_energy.md#theorem-4-exact-lossless-benchmark).

### M25

**Residual angular jitter and its harmonics**

- **Central question:** Which within-residue coherences survive after the cyclic phase peaks broaden?
- **Understanding target:** Fold the residual angle by multiplying by the alphabet size and reducing modulo a full turn. Show that coherences whose Fock numbers differ by $`kJ`$ are multiplied by the $`k`$th Fourier coefficient of that folded law. For a folded law with equal masses at zero and half a turn, find the first nonzero positive harmonic.
- **Dependencies and story role:** [M04](#m04), [M07](#m07), [M24](#m24). The phase alphabet now has independent angular jitter within each phase branch.
- **Conceptual connection:** The number spacing in the input determines which Fourier coefficient controls its surviving coherence.
- **Sources:** [Phase-jitter bridge](HOLEVO_BRIDGE.md#phase-jitter-and-folded-harmonics) and [folded phase law](../science/phase-jitter.md#folded-phase-law).

### M26

**Why a moving harmonic can disappear at fixed loss**

- **Central question:** Why can quadratic energy fail even if the phase-only capacity stays positive?
- **Understanding target:** Recenter the photon-number quotient using the flagged count, then use its bounded second moment to restrict attention to a fixed window. Explain why finite-window phase tags become orthogonal when the folded law tends to uniform, and why the omitted tail costs vanishing entropy. Apply the result to a fixed-amplitude cosine whose harmonic index tends to infinity and grows more slowly than $`J`$.
- **Dependencies and story role:** [M05](#m05), [M14](#m14)–[M17](#m17), [M24](#m24), [M25](#m25). The posterior estimate shows which harmonics a fixed-loss photon budget can keep useful.
- **Conceptual connection:** The phase-only relative entropy to uniform can stay constant while the separation in Fock number required to carry coherence grows.
- **Sources:** [Rate bound for arbitrary inputs](../science/phase-jitter.md#a-rate-bound-for-arbitrary-inputs) and [moving-harmonic example](../science/phase-jitter.md#a-moving-harmonic-raises-the-energy-scale).

### M27

**Heralding a Fock doublet at fixed loss**

- **Central question:** How does one surviving harmonic give a positive assisted rate at quadratic energy?
- **Understanding target:** Use two Fock levels separated by $`kJ`$ with an entangled reference. Describe the receiver's disjoint two-level projections and one typical-loss acceptance window. Relate nonzero surviving coherence and the two leakage populations to Bell fidelity above one half. Track the acceptance probability and the mean photons of all attempts through recurrence and hashing.
- **Dependencies and story role:** [M06](#m06), [M09](#m09)–[M11](#m11), [M23](#m23), [M25](#m25), [M26](#m26). A physical receiver supplies the achievable half of the harmonic criterion.
- **Conceptual connection:** Modular number coherence can support assisted communication even when the original branch-separation receiver is unavailable.
- **Sources:** [Fixed-loss rate threshold](../science/phase-jitter.md#fixed-loss-rate-threshold) and [receiver and its loss window](../science/phase-jitter.md#a-receiver-that-accepts-typical-loss).

### M28

**What Bob can infer from the output residue**

- **Central question:** Which information about the lost photons can Bob infer while preserving the encoded number superposition?
- **Understanding target:** Use the known input residue to infer $`L\bmod J`$ from the receiver's output residue. Explain why measuring the residue preserves coherence within a residue class. Derive the forward coherent information of a fixed-residue input and bound its deficit from the converse by the entropy of the unresolved loss quotient. Explain how a predetermined schedule handles multiple input residues within the budget.
- **Dependencies and story role:** [M03](#m03), [M06](#m06), [M07](#m07), [M09](#m09), [M14](#m14), [M21](#m21), [M24](#m24). The achievable proof returns to the residue subspaces used in the lossless benchmark.
- **Conceptual connection:** The converse uses the full lost count. Bob learns its residue, and mean lost photons control the ambiguity cost.
- **Sources:** [Holevo bridge](HOLEVO_BRIDGE.md#the-carrier-and-the-residue) and [finite-alphabet bound](../science/critical-crossover.md#the-finite-alphabet-bound).

### M29

**From a binomial loss count to an exact capacity**

- **Central question:** Why do all three capacities converge to the same curve when loss falls inversely with the alphabet size?
- **Understanding target:** At energy $`E=eJ`$ and with $`Jq_J\to\lambda`$, split the normalized input number into a fractional residue and an integer index. Explain how a uniform entropy-tail bound allows Poisson convergence on a bounded set of indices and how rounding the residue down respects the budget. Take the coding limit at each fixed alphabet size before taking the joint limit.
- **Dependencies and story role:** [M03](#m03), [M06](#m06), [M09](#m09), [M15](#m15), [M24](#m24), [M28](#m28). The lossless entropy formula becomes one endpoint of a curve.
- **Conceptual connection:** The lost count becomes a Poisson observation of the rescaled input number. In the absence of displacement and jitter, the resulting posterior uncertainty gives the limiting rate.
- **Sources:** [Pure-loss critical window](../science/critical-crossover.md#exact-capacity-in-the-critical-window) and [Holevo bridge](HOLEVO_BRIDGE.md#the-carrier-and-the-residue).

### M30

**Two environment records at linear energy**

- **Central question:** Why can identical photon-number transitions coexist with different communication capacities?
- **Understanding target:** Identify the coherent loss and gain histories within one net shift. Tensor their environment vectors with the phase tags whose overlaps are the folded harmonics. Explain why the receiver can infer the shift modulo $`J`$, how the ambiguity vanishes, and why a nonzero harmonic still gives a positive limiting rate with weak loss and displacement. Recover the no-jitter and uniform folded-law limits.
- **Dependencies and story role:** [M04](#m04), [M05](#m05), [M21](#m21), [M25](#m25), [M27](#m27)–[M29](#m29). The model reaches a common limit for unassisted quantum transmission, two-way quantum communication and secret key.
- **Conceptual connection:** A count shift and the environment's information within that shift are different resources. Residual phase changes the latter while leaving the receiver's photon-number transitions fixed.
- **Sources:** [Critical displacement](../science/critical-displacement.md), [phase-jitter bridge](HOLEVO_BRIDGE.md#phase-jitter-and-folded-harmonics) and [phase-tagged critical capacity](../science/phase-jitter.md#exact-capacity-at-weak-loss-and-displacement).
