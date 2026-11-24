"""Exercise the lossy Fock pair and weak-limit environment tags."""

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.special import i0
from scipy.stats import binom, norm

from check_critical_displacement import (
    entropy,
    finite_pairs,
    limiting_pairs,
    weighted_binary_entropy,
)


def cosine_coefficient(index, harmonic, modulation, phase):
    """Evaluate the Fourier coefficient of 1 + a cos(k phi - phase)."""
    angles = 2 * np.pi * np.arange(8 * harmonic + 1) / (8 * harmonic + 1)
    density = 1 + modulation * np.cos(harmonic * angles - phase)
    return np.mean(density * np.exp(1j * index * angles))


def fixed_loss_pair(j, harmonic, coefficient):
    loss = 0.42
    energy_scale = 0.4
    low = math.floor(energy_scale * j**2)
    gap = harmonic * j
    high = low + gap
    half_width = 0.1
    center = loss * harmonic / 2
    lower = math.ceil(loss * low + (center - half_width) * j)
    upper = math.floor(loss * low + (center + half_width) * j)
    lost = np.arange(lower, upper + 1)
    assert lost.size and upper - lower < gap
    assert (low + high) / 2 <= 0.45 * j**2

    # Construct the projected joint reference–receiver matrix for every flag.
    # Reference x and reported receiver basis y require loss ell + (x-y)gap.
    diagonals = []
    for x, photon_number in enumerate((low, high)):
        for y in (0, 1):
            diagonals.append(0.5 * binom.pmf(lost + (x - y) * gap, photon_number, loss))
    d00, d01, d10, d11 = diagonals
    coherence = coefficient * np.sqrt(d00 * d11)
    block = np.diag([column.sum() for column in diagonals]).astype(complex)
    block[0, 3] = coherence.sum()
    block[3, 0] = block[0, 3].conjugate()
    assert np.min(np.linalg.eigvalsh(block)) >= -1e-15
    acceptance = float(block.trace().real)
    bell_overlap = (block[0, 0].real + block[3, 3].real) / 2 + abs(block[0, 3])
    corrected_fidelity = float(bell_overlap) / acceptance

    # The NPT block tests the two leakage populations, not the accepted trace.
    log_ratio = np.log(np.abs(coherence) ** 2 / (d01 * d10))
    clt_log_ratio = math.log(abs(coefficient) ** 2) + harmonic**2 / (loss * energy_scale)
    assert np.min(log_ratio) > 0
    assert acceptance > 0.08 and corrected_fidelity > 0.6

    # Independently integrate the four limiting Gaussian densities and the
    # geometric mean of the matching pairs over the acceptance window.
    sigma = math.sqrt(loss * (1 - loss) * energy_scale)

    def gaussian_window(mean):
        return norm.cdf((center + half_width - mean) / sigma) - norm.cdf(
            (center - half_width - mean) / sigma
        )

    means = (0, harmonic, -(1 - loss) * harmonic, loss * harmonic)
    limiting_diagonals = [gaussian_window(mean) / 2 for mean in means]
    limiting_acceptance = math.fsum(limiting_diagonals)
    limiting_coherence = (
        0.5 * abs(coefficient) * math.exp(-means[3] ** 2 / (8 * sigma**2))
        * gaussian_window(means[3] / 2)
    )
    limiting_fidelity = (
        (limiting_diagonals[0] + limiting_diagonals[3]) / 2 + limiting_coherence
    ) / limiting_acceptance
    return {
        "J": j,
        "harmonic": harmonic,
        "coherent_amplitude": abs(coefficient),
        "accepted_mass": acceptance,
        "bell_fidelity": corrected_fidelity,
        "limit_accepted_mass": limiting_acceptance,
        "limit_bell_fidelity": limiting_fidelity,
        "limit_log_ppt_ratio": clt_log_ratio,
        "max_log_ppt_ratio_error": float(np.max(np.abs(log_ratio - clt_log_ratio))),
    }


def weak_binary(low, high, coefficient, j=None):
    """Compute the flagged and physical rates from the binary Gram matrices."""
    by_shift = defaultdict(lambda: np.zeros((2, 2), dtype=complex))
    by_output = defaultdict(lambda: [0.0, 0.0])
    for counts in low.probabilities.keys() | high.probabilities.keys():
        lost, gained = counts
        shift = gained - lost
        p0 = low.probabilities.get(counts, 0.0) / 2
        p1 = high.probabilities.get(counts, 0.0) / 2
        overlap = coefficient * math.sqrt(p0 * p1)
        by_shift[shift] += np.array([[p0, overlap], [overlap.conjugate(), p1]])
        if j is not None:
            by_output[shift][0] += p0
            by_output[j + shift][1] += p1

    bound = (low.tail_bound + high.tail_bound) / 2
    retained_probability = math.fsum(float(m.trace().real) for m in by_shift.values())
    assert abs(1 - retained_probability) <= bound + 2e-14
    eigenvalues = [np.linalg.eigvalsh(m) for m in by_shift.values()]
    assert min(eigs[0] for eigs in eigenvalues) >= -2e-15
    environment_entropy = entropy(value for eigs in eigenvalues for value in eigs)
    flagged_output_entropy = entropy(
        float(value.real) for m in by_shift.values() for value in m.diagonal()
    )
    flagged_rate = flagged_output_entropy - environment_entropy
    alias_cost = math.fsum(weighted_binary_entropy(*pair) for pair in by_output.values())

    if j is not None:
        physical_rate = entropy(sum(pair) for pair in by_output.values()) - environment_entropy
        assert abs(physical_rate - (flagged_rate - alias_cost)) < 2e-13
    else:
        physical_rate = flagged_rate
    return {
        "flagged_rate": flagged_rate,
        "physical_rate": physical_rate,
        "alias_cost": alias_cost,
        "omitted_probability_bound": bound,
    }


def weak_binary_closed_form(loss_scale, displacement_scale, coefficient):
    # Vacuum fixes the common shift to zero. Within that shift only the
    # zero-loss, zero-gain outcome overlaps the vacuum environment state.
    bessel = i0(2 * math.sqrt((loss_scale + displacement_scale) * displacement_scale))
    zero_shift = math.exp(-loss_scale - 2 * displacement_scale) * bessel
    posterior = zero_shift / (1 + zero_shift)
    overlap_sq = abs(coefficient) ** 2 / bessel
    smaller_eigenvalue = (
        1 - math.sqrt(1 - 4 * posterior * (1 - posterior) * (1 - overlap_sq))
    ) / 2
    classical = weighted_binary_entropy(posterior, 1 - posterior)
    quantum = weighted_binary_entropy(smaller_eigenvalue, 1 - smaller_eigenvalue)
    return (1 + zero_shift) * (classical - quantum) / 2


def weak_displacement_checks():
    cutoff = 48
    cases = {}
    for loss, displacement in ((1.0, 0.0), (0.0, 0.5), (1.0, 1.0)):
        finite = []
        limiting = []
        branches = [limiting_pairs(n, loss, displacement, cutoff) for n in (0, 1)]
        for delta in (0.0, 1.0, 2.0, 3.0):
            coefficient = math.exp(-delta**2 / 2)
            diagnostics = weak_binary(*branches, coefficient)
            predicted = weak_binary_closed_form(loss, displacement, coefficient)
            assert abs(diagnostics["flagged_rate"] - predicted) < 2e-13
            assert diagnostics["omitted_probability_bound"] < 1e-22
            limiting.append({"scaled_gaussian_jitter": delta, "rate": predicted})

        rates = [row["rate"] for row in limiting]
        assert all(a > b > 0 for a, b in zip(rates, rates[1:]))
        assert abs(weak_binary(*branches, 0)["flagged_rate"]) < 2e-13
        rate_real_tag = weak_binary(*branches, 0.3)["flagged_rate"]
        rate_imaginary_tag = weak_binary(*branches, 0.3j)["flagged_rate"]
        assert abs(rate_real_tag - rate_imaginary_tag) < 2e-13
        for j in (8, 32, 128, 512, 2048, 65536):
            coefficient = math.exp(-0.5)
            finite_branches = [finite_pairs(n, j, loss, displacement, cutoff) for n in (0, j)]
            diagnostic = weak_binary(*finite_branches, coefficient, j)
            assert diagnostic["omitted_probability_bound"] < 1e-22
            assert diagnostic["physical_rate"] > 0
            finite.append({"J": j, **diagnostic})
        assert abs(finite[-1]["physical_rate"] - rates[1]) < 6e-5
        cases[f"lambda={loss:g}, beta={displacement:g}"] = {
            "limiting_rates": limiting,
            "finite_at_scaled_gaussian_jitter_1": finite,
        }
    return cases


def recentered_moving_harmonic():
    radius = 3
    harmonic = 2 * radius + 1
    modulation = 0.8
    first = cosine_coefficient(1, harmonic, modulation, 0.7)
    visible = cosine_coefficient(harmonic, harmonic, modulation, 0.7)
    assert abs(first) < 2e-14
    assert abs(visible - (modulation / 2) * np.exp(0.7j)) < 2e-14
    offsets = np.arange(-radius, radius + 1)
    differences = offsets[:, None] - offsets[None, :]
    coefficients = np.vectorize(lambda index: cosine_coefficient(index, harmonic, modulation, 0.7))
    centered = coefficients(differences)
    translated = offsets + 1_000_000
    far_from_origin = coefficients(translated[:, None] - translated[None, :])
    assert np.max(np.abs(centered - np.eye(2 * radius + 1))) < 2e-14
    assert np.array_equal(centered, far_from_origin)

    # A phase-only two-level prior can still access the moving coefficient.
    # This is a check of a fixed window, not of the loss-based tail theorem.
    eigs = np.linalg.eigvalsh(np.array([[1, visible], [visible.conjugate(), 1]]) / 2)
    phase_only_binary_rate = 1 - entropy(eigs)
    assert phase_only_binary_rate > 0
    return {
        "window_radius": radius,
        "harmonic_outside_window": harmonic,
        "translated_window_center": 1_000_000,
        "max_gram_error": float(np.max(np.abs(centered - np.eye(2 * radius + 1)))),
        "phase_only_binary_rate": phase_only_binary_rate,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    gaussian = math.exp(-1.2**2 / 2)
    harmonic_two = cosine_coefficient(2, 2, 0.8, 0.7)
    assert abs(cosine_coefficient(1, 2, 0.8, 0.7)) < 2e-14
    assert abs(harmonic_two - 0.4 * np.exp(0.7j)) < 2e-14
    fixed = {}
    for name, harmonic, coefficient in (
        ("gaussian", 1, gaussian),
        ("cosine_with_first_nonzero_harmonic_two", 2, harmonic_two),
    ):
        rows = [fixed_loss_pair(j, harmonic, coefficient) for j in (128, 512, 2048, 8192)]
        assert rows[-1]["max_log_ppt_ratio_error"] < 0.012
        assert abs(rows[-1]["accepted_mass"] - rows[-1]["limit_accepted_mass"]) < 0.001
        assert abs(rows[-1]["bell_fidelity"] - rows[-1]["limit_bell_fidelity"]) < 0.001
        fixed[name] = rows
    report = {
        "fixed_loss_pair": fixed,
        "weak_displacement_binary": weak_displacement_checks(),
        "recentered_moving_harmonic": recentered_moving_harmonic(),
    }
    rendered = json.dumps(report, indent=2)
    if args.output is None:
        print(rendered)
    else:
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
