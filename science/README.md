# Photon energy, discrete phase noise and loss

An unknown optical phase can be harmless to a suitable number-state encoding when it takes values in a finite cyclic group. Photon loss changes how much energy that protection costs. This account establishes matching energy orders for maintaining a fixed two-way entanglement or secret-key rate as the number of possible phases grows.

The main statement is

```math
E_{\min}(\eta,J,R)=\Theta_{\eta,R}(J^2)
\quad\text{for fixed }0\lt\eta\lt1,
\quad 0\lt R\lt-\log_2(1-\eta).
```

At zero loss, the exact energy-constrained capacities equal $`g(E/J)`$, where $`g`$ is the entropy of a thermal bosonic mode of mean photon number equal to its argument. The corresponding fixed-rate energy is linear in $`J`$. All energies refer to physical channel inputs; the bright carrier used by the recovery construction is included.

## Connected reading route

1. [Model and statements](model.md) defines the memoryless channel, the unconditional mean-energy constraint and the allowed communication resources. It states the claims with their quantifiers.
2. [Converse](converse.md) follows the information leaked to the environment. Its conditional-entropy estimate is uniform over all photon-number distributions of finite mean and all input reference systems. The energy-constrained squashed-entanglement theorem supplies the adaptive protocol bound.
3. [Recovery](recovery.md) builds a physical heralded map on displaced finite-Fock subspaces. Its success event preserves arbitrary entangled data exactly. The overlap estimate remains uniform as the phase alphabet grows.
4. [Rate and energy](rate_energy.md) combines the recovery with finite-support reverse hashing. It proves the quadratic energy law, the exact lossless result and the fixed-alphabet unconstrained capacity statement.
5. [Interpretation](interpretation.md) explains the mechanism, the noncommuting limits and the operational scope.

The [related-work account](../references/RELATED_WORK.md) separates the communication theorem from established lossy metrology, phase-noise coding and pure-loss capacity results. The [verification guide](../verification/README.md) describes finite checks of the entropy and recovery calculations; the universal statements rest on the written proofs and their cited dependencies.
