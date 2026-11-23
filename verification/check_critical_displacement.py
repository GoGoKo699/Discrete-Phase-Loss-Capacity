"""Check the two-level coherent information for weak loss and displacement."""

from collections import defaultdict
from dataclasses import dataclass
from math import exp, fsum, log1p, log2, sqrt


@dataclass
class CountPairs:
    probabilities: dict[tuple[int, int], float]
    tail_bound: float


def poisson(mean, cutoff):
    values = [exp(-mean)]
    for k in range(1, cutoff + 1):
        values.append(values[-1] * mean / k)
    return values


def binomial(n, loss, cutoff):
    values = [exp(n * log1p(-loss))]
    odds = loss / (1 - loss)
    for l in range(1, cutoff + 1):
        values.append(values[-1] * max(0, n - l + 1) * odds / l)
    return values


def gain_counts(n, variance, cutoff):
    values = [exp(-(n + 1) * log1p(variance))]
    odds = variance / (1 + variance)
    for k in range(1, cutoff + 1):
        values.append(values[-1] * (n + k) * odds / k)
    return values


def tail_from_ratios(values, cutoff):
    first = values[cutoff + 1]
    if first == 0:
        return 0.0
    ratio = values[cutoff + 2] / first
    if ratio >= 1:
        raise ValueError("Increase cutoff until successive tail terms decrease.")
    # The Poisson, binomial, and gain-count ratios are nonincreasing.
    return first / (1 - ratio)


def finite_pairs(n, j, loss_scale, displacement_scale, cutoff):
    variance = displacement_scale / j
    loss = (loss_scale / j + variance) / (1 + variance)
    losses = binomial(n, loss, cutoff + 2)
    probabilities = {}
    for lost, prob in enumerate(losses[: cutoff + 1]):
        if prob == 0:
            continue
        for gained, conditional in enumerate(gain_counts(n - lost, variance, cutoff)):
            probabilities[lost, gained] = prob * conditional
    # Gains after attenuation are bounded in distribution by gains with no loss.
    gains_without_loss = gain_counts(n, variance, cutoff + 2)
    return CountPairs(
        probabilities,
        tail_from_ratios(losses, cutoff) + tail_from_ratios(gains_without_loss, cutoff),
    )


def limiting_pairs(x, loss_scale, displacement_scale, cutoff):
    losses = poisson((loss_scale + displacement_scale) * x, cutoff + 2)
    gains = poisson(displacement_scale * x, cutoff + 2)
    probabilities = {
        (lost, gained): p_loss * p_gain
        for lost, p_loss in enumerate(losses[: cutoff + 1])
        for gained, p_gain in enumerate(gains[: cutoff + 1])
    }
    return CountPairs(
        probabilities,
        tail_from_ratios(losses, cutoff) + tail_from_ratios(gains, cutoff),
    )


def weighted_binary_entropy(left, right):
    total = left + right
    return fsum(-p * log2(p / total) for p in (left, right) if p > 0)


def entropy(probabilities):
    return fsum(-p * log2(p) for p in probabilities if p > 0)


def diagnostic(low, high, j=None):
    """Return classical residual uncertainty, environment entropy and physical rate."""
    shift_diagonals = defaultdict(lambda: [0.0, 0.0])
    received_diagonals = defaultdict(lambda: [0.0, 0.0])
    overlaps = defaultdict(float)
    for index, branch in enumerate((low, high)):
        assert 1 - fsum(branch.probabilities.values()) <= branch.tail_bound + 2e-14
        for (lost, gained), prob in branch.probabilities.items():
            shift = gained - lost
            shift_diagonals[shift][index] += prob / 2
            if j is not None:
                received_diagonals[index * j + shift][index] += prob / 2
            if index == 1:
                overlaps[shift] += sqrt(prob * low.probabilities.get((lost, gained), 0)) / 2

    classical_terms = []
    quantum_terms = []
    for shift, (left, right) in shift_diagonals.items():
        classical_terms.append(weighted_binary_entropy(left, right))
        larger = (left + right + sqrt((left - right) ** 2 + 4 * overlaps[shift] ** 2)) / 2
        determinant = max(0.0, left * right - overlaps[shift] ** 2)
        smaller = determinant / larger if larger else 0.0
        quantum_terms.append(weighted_binary_entropy(larger, smaller))

    classical = fsum(classical_terms)
    quantum = fsum(quantum_terms)
    ambiguity = fsum(weighted_binary_entropy(*pair) for pair in received_diagonals.values())
    rate = classical - quantum - ambiguity
    if j is not None:
        direct_rate = (
            entropy(sum(pair) for pair in received_diagonals.values())
            - entropy(sum(pair) for pair in shift_diagonals.values())
            - quantum
        )
        # On the retained subspace the identity is exact up to omitted mass.
        assert abs(direct_rate - rate) <= low.tail_bound + high.tail_bound + 2e-14
    return classical, quantum, ambiguity, rate


def main():
    cutoff = 48
    cases = [(0.0, 0.5), (1.0, 1.0), (1.0, 0.0)]
    print("Rates for equal weights on the vacuum and one lattice step, at E=J/2.")
    print("case           J     H(U|S)   Holevo loss   alias cost    rate      omitted mass ≤")
    for loss_scale, displacement_scale in cases:
        limit = tuple(
            limiting_pairs(x, loss_scale, displacement_scale, cutoff) for x in (0, 1)
        )
        expected = diagnostic(*limit)
        for j in (8, 32, 128, 512, 2048, 4096, 65536, None):
            branches = (
                tuple(finite_pairs(n, j, loss_scale, displacement_scale, cutoff) for n in (0, j))
                if j is not None
                else limit
            )
            classical, quantum, ambiguity, rate = diagnostic(*branches, j)
            tail = fsum(branch.tail_bound for branch in branches) / 2
            assert tail < 1e-22
            assert 0 <= quantum <= classical + 1e-13
            if j == 65536:
                assert abs(rate - expected[-1]) < 6e-5
            if j is None and displacement_scale > 0:
                assert 0 < rate < classical
            if displacement_scale == 0:
                assert quantum < 1e-13
            print(
                f"({loss_scale:g},{displacement_scale:g}) {str(j or '∞'):>11}"
                f"   {classical:10.7f}   {quantum:10.7f}   {ambiguity:10.3g}"
                f"  {rate:10.7f}    {tail:.3g}"
            )


if __name__ == "__main__":
    main()
