# Photon energy, discrete phase noise and loss

An unknown optical phase can be harmless to a suitable number-state encoding when it takes values in a finite cyclic group. Photon loss changes how much energy that protection costs. The fixed-loss theorem gives the energy order for maintaining a two-way quantum or key rate. The critical-loss theorem gives an exact common limit for unassisted quantum, two-way quantum and two-way key communication.

The main statement is

```math
E_{\min}(\eta,J,R)=\Theta_{\eta,R}(J^2)
\quad\text{for fixed }0\lt\eta\lt1,
\quad 0\lt R\lt-\log_2(1-\eta).
```

At zero loss, the exact energy-constrained capacities equal $`g(E/J)`$, where $`g`$ is the entropy of a thermal bosonic mode of mean photon number equal to its argument. The corresponding fixed-rate energy is linear in $`J`$. All energies refer to physical channel inputs; the bright carrier used by the recovery construction is included.

At linear energy and loss probability of order the inverse alphabet size, a number-residue encoding reaches the same limiting capacity as the adaptive key converse. The limiting rate is a conditional entropy for the Poisson loss count. [Critical photon-loss crossover](critical-crossover.md)

At the same energy scale, Gaussian displacement of variance of order the inverse alphabet size gives another common limiting capacity. The receiver can nearly resolve the net number shift. The environment retains coherent information inside each shift class, producing a strictly lower rate than a channel with the same number transitions and only a shift record. [Critical displacement](critical-displacement.md) · [Displacement-only comparison](https://github.com/GoGoKo699/Bosonic-Noise-Dimension/blob/main/science/07-cyclic-phase.md)

Independent phase jitter changes which Fock-level separations retain coherence. At fixed loss and quadratic energy, the limiting phase law after rescaling by the alphabet size determines whether a two-way rate survives. At linear energy with weak loss and displacement, the same law contributes a coherent environment tag to the capacity formula. [Phase jitter](phase-jitter.md)

## Connected reading route

1. [Model and statements](model.md) defines the memoryless channel, the unconditional mean-energy constraint and the allowed communication resources. It states the claims with their quantifiers.
2. [Converse](converse.md) follows the information leaked to the environment. Its conditional-entropy estimate is uniform over all photon-number distributions of finite mean and all input reference systems. The energy-constrained squashed-entanglement theorem supplies the adaptive protocol bound.
3. [Recovery](recovery.md) builds a physical heralded map on displaced finite-Fock subspaces. Its success event preserves arbitrary entangled data exactly. The overlap estimate remains uniform as the phase alphabet grows.
4. [Rate and energy](rate_energy.md) combines the recovery with finite-support reverse hashing. It proves the quadratic energy law, the exact lossless result and the fixed-alphabet unconstrained capacity statement.
5. [Critical photon-loss crossover](critical-crossover.md) bounds the value of two-way assistance at finite alphabet size and evaluates the common limit when the loss probability shrinks.
6. [Critical displacement](critical-displacement.md) proves the finite-alphabet gap bound and the energy-constrained limit with weak Gaussian displacement.
7. [Phase jitter](phase-jitter.md) proves the fixed-loss harmonic criterion, gives a two-level protocol at typical loss, and incorporates the angular environment tag into the exact weak-noise limit.
8. [Interpretation](interpretation.md) explains the mechanisms, the noncommuting limits and the operational scope.

The [related-work account](../references/RELATED_WORK.md) separates the communication theorem from established lossy metrology, phase-noise coding and pure-loss capacity results. The [verification guide](../verification/README.md) describes finite checks of the entropy and recovery calculations; the universal statements rest on the written proofs and their cited dependencies.
