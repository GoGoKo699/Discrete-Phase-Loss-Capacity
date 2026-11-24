# References

The fixed-loss sources were checked on 2026-11-05 and the crossover references on 2026-11-18. The keys below match [references.bib](references.bib); headings supply ordinary Markdown anchors, for example `REFERENCES.md#dsw2018`. [RELATED_WORK.md](RELATED_WORK.md) explains the contribution boundary. The educational textbook, research articles and pinned project repositories have distinct roles.

## Holevo2019

Alexander S. Holevo, **Quantum Systems, Channels, Information: A Mathematical Introduction**, second revised and expanded edition, De Gruyter (2019).

- [Publisher and DOI 10.1515/9783110642490](https://doi.org/10.1515/9783110642490) · [Detailed contents](https://api.pageplace.de/preview/DT0400.9783110642490_A39059069/preview-9783110642490_A39059069.pdf)
- Role: the educational anchor, with section-by-section links in the [Holevo bridge](../learning/HOLEVO_BRIDGE.md).

## ISS2011

J. Solomon Ivan, Krishna Kumar Sabapathy and R. Simon, **Operator-sum representation for bosonic Gaussian channels**, *Physical Review A* **84**, 042311 (2011).

- [DOI 10.1103/PhysRevA.84.042311](https://doi.org/10.1103/PhysRevA.84.042311) · [arXiv:1012.4266](https://arxiv.org/abs/1012.4266)
- Role: Gaussian channel composition and the Fock coefficients of quantum-limited attenuation and amplification in the [shift-resolved dilation](../science/critical-displacement.md#exact-finite-channel-comparison).

## ArqandSmith2026

Amir Arqand and Graeme Smith, **No advantage from classical assistance for energy-constrained bosonic dephasing channels** (2026).

- [arXiv:2610.13854](https://arxiv.org/abs/2610.13854)
- Role: pinching-based relative-entropy comparison for number-preserving dephasing, extended here using the net-shift flag.

## KW2018

Eneet Kaur and Mark M. Wilde, **Amortized entanglement of a quantum channel and approximately teleportation-simulable channels**, *Journal of Physics A: Mathematical and Theoretical* **51**, 035303 (2018).

- [DOI 10.1088/1751-8121/aa9da7](https://doi.org/10.1088/1751-8121/aa9da7) · [arXiv:1707.07721](https://arxiv.org/abs/1707.07721)
- Role: amortization and the privacy-test bound for adaptive secret-key protocols.

## Winter2016

Andreas Winter, **Tight uniform continuity bounds for quantum entropies: conditional entropy, relative entropy distance and energy constraints**, *Communications in Mathematical Physics* **347**, 291–313 (2016).

- [DOI 10.1007/s00220-016-2609-8](https://doi.org/10.1007/s00220-016-2609-8) · [arXiv:1507.07775](https://arxiv.org/abs/1507.07775)
- Role: conditional entropy continuity used for finite quotient support and an unbounded environment.

## Wilde2017

Mark M. Wilde, **Quantum Information Theory**, second edition, Cambridge University Press (2017).

- DOI and publisher: [10.1017/9781316809976](https://doi.org/10.1017/9781316809976)
- Free author version: [arXiv:1106.1445v8, *From Classical to Quantum Shannon Theory*](https://arxiv.org/abs/1106.1445v8), revised 14 July 2019 with corrections. This access version is distinct from the published 2017 edition.
- Role: supplementary quantum Shannon theory for the [learning route](../learning/README.md). The [reading notes](../learning/WILDE_BRIDGE.md) identifies the relevant chapters and connects states, channels, entropy and communication protocols to this optical model.
- Scope: textbook foundations support the learning map. The channel-specific estimates and constructions are proved in the scientific pages, and research-level capacity and distillation ingredients are credited to the primary papers below.

## CW2004

Matthias Christandl and Andreas Winter, **“Squashed entanglement”: An additive entanglement measure**, *Journal of Mathematical Physics* **45**(3), 829–840 (2004).

- DOI: [10.1063/1.1643788](https://doi.org/10.1063/1.1643788)
- Author manuscript: [arXiv:quant-ph/0308088](https://arxiv.org/abs/quant-ph/0308088)
- Role: foundational definition and properties of squashed entanglement; inherited background for the [converse](../science/converse.md).

## TGW2014

Masahiro Takeoka, Saikat Guha, and Mark M. Wilde, **The squashed entanglement of a quantum channel**, *IEEE Transactions on Information Theory* **60**(8), 4987–4998 (2014).

- DOI: [10.1109/TIT.2014.2330313](https://doi.org/10.1109/TIT.2014.2330313)
- Author manuscript: [arXiv:1310.0129](https://arxiv.org/abs/1310.0129)
- Role: channel squashed-entanglement bounds on assisted quantum and private communication. The infinite-dimensional average-energy statement invoked here is cited separately as DSW2018.

## DSW2018

Noah Davis, Maksim E. Shirokov, and Mark M. Wilde, **Energy-constrained two-way assisted private and quantum capacities of quantum channels**, *Physical Review A* **97**(6), 062310 (2018).

- DOI: [10.1103/PhysRevA.97.062310](https://doi.org/10.1103/PhysRevA.97.062310)
- Author manuscript: [arXiv:1801.08102](https://arxiv.org/abs/1801.08102); [checked version 3](https://arxiv.org/html/1801.08102v3)
- Pinpoint: Sec. IV, Eq. (101), and Theorem 4, Eqs. (139)–(141); Proposition 1 gives the finite-block weak converse for approximate private-state generation.
- Role: the imported adaptive weak-converse theorem. The [converse](../science/converse.md) checks its Gibbs-observable and finite-output-entropy conditions and supplies the channel-specific entropy bound. The average-energy framework itself is inherited.

## WildeQi2018

Mark M. Wilde and Haoyu Qi, **Energy-constrained private and quantum capacities of quantum channels**, *IEEE Transactions on Information Theory* **64**(12), 7802–7827 (2018).

- [DOI 10.1109/TIT.2018.2854766](https://doi.org/10.1109/TIT.2018.2854766) · [arXiv:1609.01997](https://arxiv.org/abs/1609.01997)
- Theorems 1, 2 and 5 and Eq. (164) justify the regularized coherent-information lower bound for unassisted communication under mean input energy. The [crossover proof](../science/critical-crossover.md) applies it to a fixed schedule of residue subspaces.

## Michael2016

Marios H. Michael, Matti Silveri, R. T. Brierley, Victor V. Albert, Juha Salmilehto, Liang Jiang and S. M. Girvin, **New class of quantum error-correcting codes for a bosonic mode**, *Physical Review X* **6**, 031006 (2016).

- [DOI 10.1103/PhysRevX.6.031006](https://doi.org/10.1103/PhysRevX.6.031006)
- Generalized number parity identifies photon-loss and photon-gain syndromes in binomial codes.

## Grimsmo2020

Arne L. Grimsmo, Joshua Combes and Ben Q. Baragiola, **Quantum computing with rotation-symmetric bosonic codes**, *Physical Review X* **10**, 011058 (2020).

- [DOI 10.1103/PhysRevX.10.011058](https://doi.org/10.1103/PhysRevX.10.011058)
- Rotation-symmetric encodings establish the role of fixed number residues as code subspaces.

## Jacoby2026

Shoham Jacoby, Rotem Arnon-Friedman and Serge Rosenblum, **Hardware-efficient entanglement distillation using bosonic systems**.

- [arXiv:2503.09700v3](https://arxiv.org/abs/2503.09700v3)
- Section 2 uses modular measurements on a chosen two-cavity entangled state for loss and dephasing distillation with classical communication.

## Falco2026

Alessandro Falco, Francesco Anna Mele, Ludovico Lami and Vittorio Giovannetti, **Energy-constrained two-way capacities of the pure-loss channel**.

- [arXiv:2610.12365](https://arxiv.org/abs/2610.12365)
- The exact energy-constrained two-way capacity reported in this preprint concerns pure loss with no cyclic phase channel.

## DW2005

Igor Devetak and Andreas Winter, **Distillation of secret key and entanglement from quantum states**, *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences* **461**(2053), 207–235 (2005).

- DOI: [10.1098/rspa.2004.1372](https://doi.org/10.1098/rspa.2004.1372)
- Author manuscript: [arXiv:quant-ph/0306078](https://arxiv.org/abs/quant-ph/0306078)
- Role: the one-way hashing inequality. Exchanging the parties gives the reverse coherent-information distillation rate used after successful recovery in [rate_energy.md](../science/rate_energy.md).

## Reverse2009

Raúl García-Patrón, Stefano Pirandola, Seth Lloyd, and Jeffrey H. Shapiro, **Reverse Coherent Information**, *Physical Review Letters* **102**, 210501 (2009).

- DOI: [10.1103/PhysRevLett.102.210501](https://doi.org/10.1103/PhysRevLett.102.210501)
- Author manuscript: [arXiv:0808.0210](https://arxiv.org/abs/0808.0210)
- Pinpoint: Eq. (6) defines the reverse rate $`I_R(\rho_{AB})=S(A)-S(AB)`$, with the operational feedback construction immediately around it.
- Role: reverse-reconciliation entanglement distribution. The present proof computes the rate for a finite Fock-diagonal pure-loss input and proves the required truncation limit explicitly; reverse hashing is not a new protocol here.

## PLOB2017

Stefano Pirandola, Riccardo Laurenza, Carlo Ottaviani, and Leonardo Banchi, **Fundamental limits of repeaterless quantum communications**, *Nature Communications* **8**, 15043 (2017).

- DOI: [10.1038/ncomms15043](https://doi.org/10.1038/ncomms15043)
- Publisher: [article and supplementary material](https://www.nature.com/articles/ncomms15043)
- Author manuscript: [arXiv:1510.08863](https://arxiv.org/abs/1510.08863)
- Pinpoint: main Eq. (19) gives the pure-loss two-way endpoint; the energy-constrained discussion and reverse-coherent-information lower bound appear in Supplementary Note 7, including Eqs. (S246)–(S247).
- Role: inherited ceiling $`-\log_2(1-\eta)`$ and the endpoint approached by the achievability construction. This is not an exact finite-energy pure-loss capacity formula.

## Leviant2022

Peter Leviant, Qian Xu, Liang Jiang, and Serge Rosenblum, **Quantum capacity and codes for the bosonic loss-dephasing channel**, *Quantum* **6**, 821 (2022).

- DOI: [10.22331/q-2022-09-29-821](https://doi.org/10.22331/q-2022-09-29-821)
- Publisher: [article](https://quantum-journal.org/papers/q-2022-09-29-821/)
- Author manuscript: [arXiv:2205.00341](https://arxiv.org/abs/2205.00341)
- Role: closely related bosonic loss-dephasing capacity bounds and code optimization. It is a comparison source, not an imported proof of the growing cyclic-alphabet energy threshold.

## Mele2024

Francesco Anna Mele, Farzin Salek, Vittorio Giovannetti, and Ludovico Lami, **Quantum communication on the bosonic loss-dephasing channel**, *Physical Review A* **110**, 012460 (2024).

- DOI: [10.1103/PhysRevA.110.012460](https://doi.org/10.1103/PhysRevA.110.012460)
- Author manuscript: [arXiv:2401.15634](https://arxiv.org/abs/2401.15634); [checked version 3](https://arxiv.org/html/2401.15634v3)
- Pinpoint: channel definition, antidegradability results, and Theorem 3 with Eq. (8) for a positive two-way rate.
- Role: comparison with Gaussian phase diffusion combined with loss. Its unassisted-capacity conclusions and assisted-rate conclusions have distinct operational meanings. Neither is identified here with the exact cyclic-twirl model.

## NP2025

Dong-Long Hu, Weizhou Cai, Chang-Ling Zou, and Ze-Liang Xiang, **Generalized number-phase lattice encoding of a bosonic mode for quantum error correction**, *Nature Communications* **16**, 7647 (2025).

- DOI: [10.1038/s41467-025-62898-1](https://doi.org/10.1038/s41467-025-62898-1)
- Publisher: [article and supplementary information](https://www.nature.com/articles/s41467-025-62898-1)
- Author manuscript: [arXiv:2508.12354](https://arxiv.org/abs/2508.12354); [checked version 1](https://arxiv.org/html/2508.12354v1)
- Pinpoint: main Eqs. (16), (19)–(21), the phase-error discrimination discussion, and Supplementary Notes 4–6.
- Role: close number–phase coding and error-subspace recovery antecedent. Credit belongs here for these coding ideas; the present claim is the all-encoder converse and matching energy order for an exact finite phase alphabet.

## Cai2024

Weizhou Cai, Jing-Ning Zhang, Ziyue Hua, Weiting Wang, Xiaoxuan Pan, Xinyu Liu, Yuwei Ma, Ling Hu, Xianghao Mu, Haiyan Wang, Yipu Song, Chang-Ling Zou, and Luyan Sun, **Unambiguous discrimination of general quantum operations**, *Science Advances* **10**(46), eadq2529 (2024).

- DOI: [10.1126/sciadv.adq2529](https://doi.org/10.1126/sciadv.adq2529)
- Author manuscript: [arXiv:2404.13317](https://arxiv.org/abs/2404.13317); [checked version 1](https://arxiv.org/html/2404.13317v1)
- Pinpoint: the operational discrimination condition and reciprocal-state measurement construction.
- Role: unambiguous operation discrimination and reciprocal-frame methodology. The [recovery](../science/recovery.md) proves its full-data-subspace identity and growing-alphabet uniformity rather than claiming reciprocal inversion as a new technique.

## Escher2011

B. M. Escher, R. L. de Matos Filho, and L. Davidovich, **General framework for estimating the ultimate precision limit in noisy quantum-enhanced metrology**, *Nature Physics* **7**, 406–411 (2011).

- DOI: [10.1038/nphys1958](https://doi.org/10.1038/nphys1958)
- Publisher: [article](https://www.nature.com/articles/nphys1958)
- Author manuscript: [arXiv:1201.1693](https://arxiv.org/abs/1201.1693), posted in 2012 after the journal publication.
- Pinpoint: Eqs. (11)–(12), including the lossy phase-estimation QFI bound.
- Role: the physical precedent for the loss-induced phase-resolution scaling. A metrology bound alone does not upper-bound an arbitrary assisted communication protocol.

## Zhuang2021

Quntao Zhuang, **Quantum-Enabled Communication without a Phase Reference**, *Physical Review Letters* **126**, 060502 (2021).

- DOI: [10.1103/PhysRevLett.126.060502](https://doi.org/10.1103/PhysRevLett.126.060502)
- Publisher full text: [PDF](https://link.aps.org/pdf/10.1103/PhysRevLett.126.060502)
- Role: communication when a random phase is common to several modes, including lossless results and assisted or thermal-loss settings. Its shared-phase channel must be distinguished from independent phase noise on each single-mode use here.

## Phase2023

Ludovico Lami and Mark M. Wilde, **Exact solution for the quantum and private capacities of bosonic dephasing channels**, *Nature Photonics* **17**, 525–530 (2023).

- DOI: [10.1038/s41566-023-01190-4](https://doi.org/10.1038/s41566-023-01190-4)
- Publisher: [article](https://www.nature.com/articles/s41566-023-01190-4)
- Author manuscript: [arXiv:2205.05736](https://arxiv.org/abs/2205.05736); [checked version 2](https://arxiv.org/html/2205.05736v2)
- Pinpoint: main Eqs. (4)–(7); Theorem S7 states the phase-density regularity assumption and the coincidence of the capacities with relative entropy from the uniform phase density.
- Role: exact pure-dephasing capacities without loss. This theorem is not cited as a finite-energy capacity formula for an atomic cyclic phase law.

## Cao2015

Zhu Cao, Zhen Zhang, Hoi-Kwong Lo, and Xiongfeng Ma, **Discrete-phase-randomized coherent state source and its application in quantum key distribution**, *New Journal of Physics* **17**, 053014 (2015).

- DOI: [10.1088/1367-2630/17/5/053014](https://doi.org/10.1088/1367-2630/17/5/053014)
- Author manuscript: [arXiv:1410.3217](https://arxiv.org/abs/1410.3217)
- Role: discrete phase randomization as a source-preparation procedure in a specified QKD security analysis. This differs from optimizing the capacity over all encoders for the single-mode channel studied here.

## InternalPhase

GoGoKo699, **Bosonic-Phase-Noise-Capacity**, research repository, main commit `2080352d5c356b3a87d8cc8780b787bc3ca0fc5f`, inspected 2026-11-05. This is an internal project source, not a journal publication.

- Inspected [model](https://github.com/GoGoKo699/Bosonic-Phase-Noise-Capacity/blob/2080352d5c356b3a87d8cc8780b787bc3ca0fc5f/science/01-model.md) and [capacity](https://github.com/GoGoKo699/Bosonic-Phase-Noise-Capacity/blob/2080352d5c356b3a87d8cc8780b787bc3ca0fc5f/science/03-capacity.md) pages.
- Role: mean-energy capacity theory for independent phase noise without photon loss; the closest internal lossless antecedent.

## InternalGroup

GoGoKo699, **Quantum-Group-Memory-Laws**, research repository, main commit `0d585db681ebc66fe0f2c7acb75f0c636869beef`, inspected 2026-11-05. This is an internal project source, not a journal publication.

- Inspected [model](https://github.com/GoGoKo699/Quantum-Group-Memory-Laws/blob/0d585db681ebc66fe0f2c7acb75f0c636869beef/science/model.md) and [capacity](https://github.com/GoGoKo699/Quantum-Group-Memory-Laws/blob/0d585db681ebc66fe0f2c7acb75f0c636869beef/science/capacity.md) pages.
- Role: inherited environment-measurement, hidden-label entropy, and adaptive squashed-entanglement proof structure in a different spin-chain projection/erasure model. It does not supply the bosonic modular/binomial estimate or the matching energy theorem.

## BBPSSW1996

Charles H. Bennett, Gilles Brassard, Sandu Popescu, Benjamin Schumacher, John A. Smolin, and William K. Wootters, **Purification of Noisy Entanglement and Faithful Teleportation via Noisy Channels**, *Physical Review Letters* **76**, 722–725 (1996).

- DOI: [10.1103/PhysRevLett.76.722](https://doi.org/10.1103/PhysRevLett.76.722)
- Author manuscript: [arXiv:quant-ph/9511027](https://arxiv.org/abs/quant-ph/9511027)
- Role: recurrence distillation above Bell fidelity one half. A fixed number of rounds reaches the positive one-way hashing regime, with [one-way coding](#dw2005) providing the final rate.
