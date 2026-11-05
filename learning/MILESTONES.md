# Thirty milestones for discrete phase noise and photon loss

[Learning overview](README.md) · [Wilde bridge](WILDE_BRIDGE.md) · [Scientific account](../science/README.md)

This map follows the question: how much mean photon energy is needed to keep a fixed entanglement or secret-key rate when the number of possible phase rotations grows? Its targets connect the physical channel, the universal converse, and the matching communication construction. The [model and statements](../science/model.md) fix the assumptions and the [rate–energy theorem](../science/rate_energy.md#theorem-3-fixed-rate-photon-energy) gives the precise result.

The selected educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition (Cambridge University Press, 2017)**. The [reading map](WILDE_BRIDGE.md#reading-map) identifies the relevant sections. Textbook foundations, the optical derivations supplied here, and the primary research theorems used by the proofs have distinct roles.

| Phase | Milestones | Scientific role |
|---|---|---|
| [Background and preliminaries](#background-and-preliminaries) | M01–M12 | Join states, entropy and quantum operations to one optical mode, its photon budget and the assisted communication task. |
| [Narrative and innovation](#narrative-and-innovation) | M13–M30 | Build the environment-based converse and the receiver construction, combine their energy orders, and explain the endpoints, evidence and scope. |

The 12/18 allocation reflects these two bodies of work. The background phase ends with the complete communication problem. The narrative phase begins with the separate proof mechanisms and ends with their joint physical meaning. Dependencies name earlier milestones; each source link leads to the authoritative statement or argument. Technical lemmas and detailed calculations remain in those sources.

## Background and preliminaries

### M01

**States and photon-number outcomes**

- **Central question:** What does the state of one optical mode specify?
- **Understanding target:** Relate a state, its photon-number probabilities and its mean photon number. Explain why the infinitely many number states belong to one mode and do not represent infinitely many channel uses.
- **Dependencies and story role:** None. This introduces the physical object whose energy and information will be tracked.
- **Conceptual connection:** Quantum-state notation acquires an observable meaning through photon counting.
- **Sources:** [Wilde §§3.2–3.4 and §4.1](WILDE_BRIDGE.md#reading-map); [one optical mode](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet).

### M02

**References and preserved entanglement**

- **Central question:** Why must a quantum communication claim describe what happens to a reference system?
- **Understanding target:** Explain reduced states, purification and entanglement. Distinguish preserving one prepared optical state from preserving its correlations with an arbitrary retained reference.
- **Dependencies and story role:** [M01](#m01). The description expands from one mode to the joint system that communication must protect.
- **Conceptual connection:** The reference tests whether a recovery operation preserves unknown quantum information.
- **Sources:** [Wilde §§3.5–3.8 and §5.1](WILDE_BRIDGE.md#reading-map); [the reference requirement in exact recovery](../science/recovery.md#theorem-2-an-exact-success-instrument).

### M03

**Classical and quantum entropy**

- **Central question:** What uncertainty is measured by the entropies in this project?
- **Understanding target:** Distinguish Shannon entropy of a photon-number law from von Neumann entropy of a state. Explain why finite mean photon number bounds both by the thermal entropy function, without requiring a finite number variance.
- **Dependencies and story role:** [M01](#m01), [M02](#m02). This supplies the information quantities used in both proof directions.
- **Conceptual connection:** A physical mean-energy constraint limits information even in an infinite-dimensional mode.
- **Sources:** [Wilde §§10.1–10.3 and §11.1](WILDE_BRIDGE.md#reading-map); [entropy notation and the mean-energy bound](../science/model.md#entropy-notation).

### M04

**Channels and their environments**

- **Central question:** How can a noisy channel be described as part of a larger quantum evolution?
- **Understanding target:** Connect a channel's Kraus operators, an isometric extension and the discarded environment. Explain why a receiver output and its complementary environment describe different parts of the same process.
- **Dependencies and story role:** [M01](#m01), [M02](#m02). This introduces the environment that will carry the information used in the converse.
- **Conceptual connection:** Lost information can be studied through correlations with a larger system.
- **Sources:** [Wilde §§4.4–4.5 and §5.2](WILDE_BRIDGE.md#reading-map); [the channel's loss and residue Kraus representation](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet).

### M05

**Conditioning and mixtures**

- **Central question:** What changes when a classical label is known?
- **Understanding target:** Read conditional Shannon entropy as an average over posterior distributions. Explain why a mixture of pure quantum states has entropy no greater than the entropy of its mixing weights, even when those states are not orthogonal.
- **Dependencies and story role:** [M02](#m02), [M03](#m03), [M04](#m04). This connects classical uncertainty with conditional quantum entanglement.
- **Conceptual connection:** A classical probability calculation can bound a quantum state without replacing that state by a classical input.
- **Sources:** [Wilde §10.2 and §§11.1, 11.9](WILDE_BRIDGE.md#reading-map); [the posterior-mixture argument](../science/converse.md#lemma-1-an-environment-extension-valid-for-every-reference).

### M06

**Photon loss as binomial sampling**

- **Central question:** What can the loss environment learn from a number-state input?
- **Understanding target:** Explain the binomial lost-photon law for an input with a specified photon number. Relate transmissivity to the mean output energy and distinguish conditional fluctuations at a fixed input number from fluctuations of the input distribution itself.
- **Dependencies and story role:** [M01](#m01), [M04](#m04), [M05](#m05). A concrete optical channel now supplies the random variables needed by the converse.
- **Conceptual connection:** The same photon loss both damages the signal and carries information about its initial number.
- **Sources:** [the optical bridge](WILDE_BRIDGE.md#the-optical-model); [pure-loss Kraus operators](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet); [information carried away by lost photons](../science/interpretation.md#the-information-carried-away-by-lost-photons).

### M07

**Cyclic phases and surviving coherence**

- **Central question:** Which coherences survive a uniform finite phase alphabet?
- **Understanding target:** Explain why averaging equally spaced phase rotations removes coherence between different photon-number residues while retaining coherence within a residue class. Distinguish a fresh phase on every use from a phase shared across many uses.
- **Dependencies and story role:** [M01](#m01), [M04](#m04). This identifies the structure protected by phase randomization alone.
- **Conceptual connection:** A finite symmetry preserves a family of quantum subspaces, but their energy spacing depends on the alphabet size.
- **Sources:** [the optical bridge](WILDE_BRIDGE.md#the-optical-model); [cyclic twirling and residue projectors](../science/model.md#one-optical-mode-and-a-cyclic-phase-alphabet); [protection without loss](../science/interpretation.md#protection-without-loss).

### M08

**Displacements and the carrier**

- **Central question:** How does a displacement make different phase branches easier to distinguish?
- **Understanding target:** Connect displacement amplitude to translated optical states and carrier photon energy. Explain pure-loss displacement covariance and why the simple sum of data and carrier energies used here relies on the chosen data marginal having zero first field moment.
- **Dependencies and story role:** [M01](#m01), [M06](#m06), [M07](#m07). This introduces the physical operation used by the achievable construction.
- **Conceptual connection:** The carrier carries branch information in the same transmitted mode, so its photons belong in the resource account.
- **Sources:** [the recovery bridge](WILDE_BRIDGE.md#exact-recovery); [finite data and a counted carrier](../science/recovery.md#finite-data-and-a-counted-carrier); [input energy](../science/recovery.md#input-energy-of-the-encoded-data).

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
- **Sources:** [Wilde §5.3](WILDE_BRIDGE.md#reading-map); [instrument validity and exact recovery](../science/recovery.md#proof-of-instrument-validity-and-exact-recovery).

### M11

**Entanglement, key and two-way communication**

- **Central question:** What useful output is produced by a successful communication protocol?
- **Understanding target:** Explain an ebit, a secret bit and a rate per attempted channel use. Relate local operations and public classical communication to entanglement distillation, and explain why distilled entanglement provides secret key while public communication alone is not pre-shared key.
- **Dependencies and story role:** [M02](#m02), [M03](#m03), [M04](#m04), [M10](#m10). Local channel operations are connected to an asymptotic communication task.
- **Conceptual connection:** A recovery probability becomes useful only after it is converted into a reliable entanglement or key rate.
- **Sources:** [Wilde §19.2 and §24.9](WILDE_BRIDGE.md#reading-map); [two-way capacities](../science/model.md#two-way-capacities); [reverse coherent information](../science/rate_energy.md#finite-data-and-reverse-coherent-information).

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
- **Sources:** [Wilde §11.7](WILDE_BRIDGE.md#reading-map); [squashed entanglement](../science/converse.md#squashed-entanglement-and-the-imported-capacity-theorem); [CW2004](../references/REFERENCES.md#cw2004).

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

**Finite data inside the displaced optical mode**

- **Central question:** Which part of the achievable code is finite dimensional?
- **Understanding target:** Explain the finite-Fock data subspace before displacement, its preservation under pure loss, and the translated and rotated output subspaces for the phase branches. Distinguish this data cutoff from the generally infinite Fock support of the physical transmitted codeword.
- **Dependencies and story role:** [M06](#m06)–[M10](#m10), [M12](#m12). The second proof direction starts from a concrete encoded signal.
- **Conceptual connection:** Finite-dimensional data can be processed exactly inside a counted, infinite-dimensional optical mode.
- **Sources:** [exact-recovery bridge](WILDE_BRIDGE.md#exact-recovery); [finite data and a counted carrier](../science/recovery.md#finite-data-and-a-counted-carrier); [avoiding an artificial optical cutoff](../verification/README.md#avoiding-a-misleading-optical-cutoff).

### M19

**Independent displaced data subspaces**

- **Central question:** Why does a reciprocal map exist for the whole data subspace?
- **Understanding target:** Explain the Gram matrix of all displaced data basis vectors and the role of distinct displacement amplitudes. Follow how independence of exponential-polynomial functions makes this matrix positive definite for every finite alphabet and positive carrier amplitude. Recognize that positivity alone does not give a success bound uniform in alphabet size.
- **Dependencies and story role:** [M08](#m08), [M18](#m18). This establishes the algebraic possibility of exact branch recovery.
- **Conceptual connection:** Independence of complete error subspaces supports preservation of arbitrary data, beyond discrimination of one selected probe state.
- **Sources:** [exact-recovery bridge](WILDE_BRIDGE.md#exact-recovery); [Gram construction](../science/recovery.md#theorem-2-an-exact-success-instrument); [linear-independence proof](../science/recovery.md#proof-of-linear-independence).

### M20

**Reciprocal maps become a physical filter**

- **Central question:** How does an algebraic left inverse yield a valid receiver instrument?
- **Understanding target:** Explain the reciprocal-operator identities and the scaling by the smallest Gram eigenvalue that makes the total success effect at most the identity. Connect the resulting operator identity to exact recovery of the pure-loss output with any reference, and include the failure branch.
- **Dependencies and story role:** [M02](#m02), [M04](#m04), [M10](#m10), [M19](#m19). This converts algebraic recovery into an allowed local operation.
- **Conceptual connection:** A spectral bound controls both physical validity and the success probability.
- **Sources:** [Wilde §§4.4–4.5 and §5.3](WILDE_BRIDGE.md#reading-map); [instrument and reference-preservation proof](../science/recovery.md#proof-of-instrument-validity-and-exact-recovery).

### M21

**A uniform overlap bound around the phase circle**

- **Central question:** Why does the growing number of branches not introduce another alphabet-size factor?
- **Understanding target:** Explain the finite-Fock overlap envelope as a polynomial times a Gaussian. Group Gram blocks by circular separation and use the at-most-two multiplicity at each separation to obtain a summable row bound independent of the alphabet size.
- **Dependencies and story role:** [M07](#m07), [M08](#m08), [M19](#m19), [M20](#m20). Exact recovery gains a quantitative bound that survives growing alphabets.
- **Conceptual connection:** The geometry of equally spaced phase branches controls the collective overlap more sharply than multiplying one overlap by the number of branches.
- **Sources:** [displacement envelope](../science/recovery.md#an-explicit-displacement-envelope); [uniform Gram estimate](../science/recovery.md#lemma-3-uniform-success-with-amplitude-proportional-to-the-alphabet-size).

### M22

**Uniform success at quadratic carrier energy**

- **Central question:** What photon cost keeps recovery success close to one as the alphabet grows?
- **Understanding target:** For fixed data cutoff and desired success margin, explain choosing one carrier-amplitude coefficient that works for every alphabet size. Convert linear growth of carrier amplitude into quadratic physical input energy, including attenuation and the data contribution.
- **Dependencies and story role:** [M08](#m08), [M09](#m09), [M18](#m18), [M21](#m21). The recovery estimate becomes a uniform resource statement.
- **Conceptual connection:** A spectral overlap estimate has a directly charged optical energy cost.
- **Sources:** [uniform-success lemma](../science/recovery.md#lemma-3-uniform-success-with-amplitude-proportional-to-the-alphabet-size); [encoded input energy](../science/recovery.md#input-energy-of-the-encoded-data).

### M23

**Reverse hashing on finite optical data**

- **Central question:** How much entanglement can be distilled from a successful recovered pair?
- **Understanding target:** For the canonical finite-Fock purification, explain why the reference entropy is the input number entropy and the joint output entropy is the lost-count entropy. Identify their difference as reverse coherent information and connect a positive value to hashing with classical communication from receiver to sender.
- **Dependencies and story role:** [M02](#m02), [M03](#m03), [M06](#m06), [M11](#m11), [M18](#m18). The recovered quantum state is assigned an operational entanglement rate.
- **Conceptual connection:** Orthogonal loss sectors turn an entropy difference into an achievable communication resource.
- **Sources:** [Wilde §11.5 and §24.9](WILDE_BRIDGE.md#reading-map); [finite data and reverse coherent information](../science/rate_energy.md#finite-data-and-reverse-coherent-information); [DW2005](../references/REFERENCES.md#dw2005); [Reverse2009](../references/REFERENCES.md#reverse2009).

### M24

**One finite cutoff suffices for the target rate**

- **Central question:** Why can the data cutoff be fixed before alphabet size or coding length grows?
- **Understanding target:** Follow the choice of one finite-mean geometric input whose reverse rate exceeds the target, then a finite cutoff that preserves this strict margin. Explain how the explicit tail-entropy estimate controls both input and lost-count entropies, avoiding an unsupported exchange of cutoff and coding limits.
- **Dependencies and story role:** [M03](#m03), [M06](#m06), [M12](#m12), [M23](#m23). This makes the finite-dimensional recovery construction sufficient for every fixed rate below the pure-loss endpoint.
- **Conceptual connection:** A controlled entropy limit converts a bosonic capacity argument into one finite data subspace.
- **Sources:** [rates-and-limits bridge](WILDE_BRIDGE.md#rates-and-limits); [finite-cutoff lemma](../science/rate_energy.md#lemma-4-a-fixed-finite-cutoff-suffices-below-the-pure-loss-endpoint).

### M25

**Fixed-length coding after heralding**

- **Central question:** How are random successes converted into a rate per attempted use?
- **Understanding target:** Explain making a fixed number of attempts, reserving slightly fewer successful pairs than their typical number, and aborting on the vanishing-probability shortage event. Combine this with reverse hashing to approach success probability times recovered-pair rate while counting all attempted photons and uses.
- **Dependencies and story role:** [M09](#m09)–[M11](#m11), [M20](#m20), [M22](#m22)–[M24](#m24). This completes the reliable communication protocol.
- **Conceptual connection:** A conditional quantum operation becomes an unconditional, fixed-length capacity construction.
- **Sources:** [rates-and-limits bridge](WILDE_BRIDGE.md#rates-and-limits); [exact heralding followed by hashing](../science/rate_energy.md#exact-heralding-followed-by-hashing).

### M26

**The matched energy law**

- **Central question:** What has been established when the necessary and sufficient photon orders coincide?
- **Understanding target:** Combine the converse and construction under the same unconditional energy convention. Explain why both two-way entanglement and key require and admit quadratic energy for a fixed partial loss and fixed positive rate below the pure-loss endpoint. Identify which constants depend on loss and target rate, and why the theorem is not an exact finite-energy capacity formula.
- **Dependencies and story role:** [M12](#m12), [M17](#m17), [M25](#m25). The two proof directions meet in the central result.
- **Conceptual connection:** A universal lower bound and one compatible protocol determine the optimal scaling order.
- **Sources:** [fixed-rate theorem](../science/rate_energy.md#theorem-3-fixed-rate-photon-energy); [its proof](../science/rate_energy.md#proof-of-theorem-3).

### M27

**The exact lossless benchmark**

- **Central question:** Why does setting the loss exactly to zero change the energy order?
- **Understanding target:** Use the residue-zero noiseless subspace to obtain the attainable entropy, and use the residue-conditioned environment bound to obtain the matching upper bound. Explain the exact thermal-entropy formula and resulting linear photon cost. Distinguish this separate endpoint proof from taking a uniform zero-loss limit of the lossy constants.
- **Dependencies and story role:** [M03](#m03), [M07](#m07), [M13](#m13), [M24](#m24), [M26](#m26). The main law is compared with the channel's sharply different lossless endpoint.
- **Conceptual connection:** Photon loss reveals a lattice index that phase randomization alone leaves protected.
- **Sources:** [lossless theorem and proof](../science/rate_energy.md#theorem-4-exact-lossless-benchmark); [protection without loss](../science/interpretation.md#protection-without-loss).

### M28

**Positive rates and noncommuting limits**

- **Central question:** How can every finite alphabet allow a positive rate while the growing-alphabet limit has none at fixed energy?
- **Understanding target:** Explain duty cycling at any positive energy and transmissivity, the pure-loss endpoint reached as energy grows at a fixed finite alphabet, and the vanishing capacity when alphabet size grows at fixed energy. Identify the order of limits and the entanglement-breaking continuous uniform phase channel. Distinguish a fixed-rate energy law from a hard zero-capacity threshold.
- **Dependencies and story role:** [M07](#m07), [M09](#m09), [M17](#m17), [M25](#m25), [M26](#m26). The scaling theorem is placed among its operational consequences.
- **Conceptual connection:** The order of resource and noise limits changes the communication conclusion.
- **Sources:** [positive-rate construction](../science/rate_energy.md#positive-rate-for-every-finite-alphabet-and-positive-energy); [fixed-alphabet endpoint](../science/rate_energy.md#fixed-alphabet-unrestricted-capacities); [continuous-limit interpretation](../science/interpretation.md#finite-alphabets-and-the-continuous-limit).

### M29

**What the numerical example verifies**

- **Central question:** Which claims can the reproducible finite checks test, and which remain analytical?
- **Understanding target:** Trace the three-level data example from its input distribution through reverse rate, exact charged energy and recovery success. Distinguish the analytic bound uniform in alphabet size from the evaluated Gram eigenvalues, and approximate decimal evaluations from interval-certified bounds. Explain why finite tests cannot establish the heavy-tail or arbitrary-adaptive converse.
- **Dependencies and story role:** [M15](#m15), [M16](#m16), [M20](#m20)–[M26](#m26). The result is connected to concrete computation with a precise evidence boundary.
- **Conceptual connection:** Numerical reproduction tests implementation-sensitive identities while the proof supplies the universal quantifiers.
- **Sources:** [quantitative example](../verification/README.md#a-quantitative-example); [check scope](../verification/README.md#what-is-checked); [verification limits](../verification/README.md#limits-of-this-verification).

### M30

**The complete mechanism and its scope**

- **Central question:** What is the full physical explanation of the result, and what would change the problem?
- **Understanding target:** Give one connected account: loss and residue information constrain surviving entanglement; a counted carrier separates whole data subspaces; exact heralding and finite-dimensional distillation attain the same energy order. Locate the inherited theorems and the new communication argument. Explain why a shared phase across uses, extra transmitted references, continuous phase broadening or bounds on receiver implementation require additional analysis.
- **Dependencies and story role:** [M12](#m12), [M17](#m17), [M22](#m22)–[M29](#m29). This integrates the mathematical mechanism, operational claim, evidence and physical boundaries.
- **Conceptual connection:** The theorem's significance comes from matching universal necessity with an allowed protocol under one explicit resource model.
- **Sources:** [physical interpretation and boundaries](../science/interpretation.md); [related-work comparison](../references/RELATED_WORK.md); [Wilde-to-project bridge](WILDE_BRIDGE.md).

