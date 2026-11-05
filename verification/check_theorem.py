#!/usr/bin/env python3
"""Bounded numerical checks; the analytic arguments, not this script, prove the theorem."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys

import numpy as np
import scipy
from scipy.special import eval_genlaguerre
from scipy.stats import binom


SEED = 20261105
PROB_TOL = 4e-12
ENTROPY_TOL = 5e-10
MATRIX_TOL = 3e-10
CHECKS: list[dict] = []


def check(label: str, value: float, upper: float, tolerance: float = 0.0) -> None:
    passed = bool(np.isfinite(value) and value <= upper + tolerance)
    CHECKS.append(
        {"check": label, "value": float(value), "upper": float(upper),
         "tolerance": float(tolerance), "passed": passed}
    )
    if not passed:
        raise AssertionError(f"{label}: {value:.16g} > {upper:.16g} + {tolerance:.3g}")


def entropy(p: np.ndarray) -> float:
    positive = np.asarray(p, dtype=float)
    positive = positive[positive > 0]
    return float(-np.sum(positive * np.log2(positive)))


def bosonic_g(x: float) -> float:
    if x == 0:
        return 0.0
    return float((x + 1) * np.log2(x + 1) - x * np.log2(x))


def bound_f(x: float) -> float:
    return bosonic_g(x) + min(x, 1.0)


def binary_entropy(x: float) -> float:
    return entropy(np.array([x, 1 - x]))


def vn_entropy(rho: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    if eigenvalues.min() < -MATRIX_TOL:
        raise AssertionError(f"Nonpositive state: minimum eigenvalue {eigenvalues.min()}")
    return entropy(np.maximum(eigenvalues, 0))


def geometric_cutoff(mu: float, cutoff: int) -> np.ndarray:
    ratio = mu / (1 + mu)
    p = ratio ** np.arange(cutoff + 1, dtype=float)
    return p / p.sum()


def finite_joint(support: np.ndarray, p: np.ndarray, eta: float, j: int) -> dict:
    """Exact finite-support classical law, evaluated with scipy's binomial PMF."""
    n_parts, l_parts, p_parts = [], [], []
    for n, pn in zip(support, p, strict=True):
        losses = np.arange(int(n) + 1, dtype=int)
        n_parts.append(np.full(losses.size, int(n), dtype=int))
        l_parts.append(losses)
        p_parts.append(pn * binom.pmf(losses, int(n), 1 - eta))
    ns, losses, weights = map(np.concatenate, (n_parts, l_parts, p_parts))
    positive = weights > 0  # Underflowed tails are below double-precision resolution.
    ns, losses, weights = ns[positive], losses[positive], weights[positive]
    residues = ns % j
    labels = losses * j + residues
    marginal = np.bincount(labels, weights=weights)
    posterior_entropy = float(np.sum(weights * np.log2(marginal[labels] / weights)))
    return {
        "n": ns, "l": losses, "r": residues, "p": weights,
        "labels": labels, "marginal": marginal, "h_cond": posterior_entropy,
    }


def check_classical_converse() -> list[dict]:
    cases = [
        ("vacuum", 0.7, 7, np.array([0]), np.array([1.0])),
        ("truncated_geometric", 0.7, 7, np.arange(25), geometric_cutoff(2.0, 24)),
        ("two_peaks", 0.2, 3, np.array([0, 60]), np.array([0.96, 0.04])),
        ("rare_bright_tail", 0.7, 8, np.array([0, 2, 31, 503]),
         np.array([0.75, 0.2, 0.049, 0.001])),
        ("single_residue", 0.95, 5, np.array([0, 5, 10, 30, 95]),
         np.array([0.3, 0.25, 0.2, 0.2, 0.05])),
    ]
    rows = []
    for name, eta, j, support, p in cases:
        law = finite_joint(support, p, eta, j)
        ns, losses, residues, weights = (law[k] for k in ("n", "l", "r", "p"))
        mean = float(np.dot(support, p))
        q = 1 - eta
        k = (ns - residues) // j
        estimate = (losses / q - residues) / j
        z = k - np.rint(estimate).astype(int)  # Ties-to-even is an allowed convention.
        centered_second = float(np.dot(weights, (ns - losses / q) ** 2))
        expected_centered_second = eta * mean / q
        error_second = float(np.dot(weights, z.astype(float) ** 2))
        u = 4 * eta * mean / (q * j * j)
        _, z_indices = np.unique(z, return_inverse=True)
        p_z = np.bincount(z_indices, weights=weights)
        h_z = entropy(p_z)
        z_l_r = {}
        for zz, ell, rr, probability in zip(z, losses, residues, weights, strict=True):
            key = (int(zz), int(ell), int(rr))
            z_l_r[key] = z_l_r.get(key, 0.0) + float(probability)
        h_z_cond = entropy(np.array(list(z_l_r.values()))) - entropy(law["marginal"])
        n_marginal = np.bincount(ns, weights=weights, minlength=int(support.max()) + 1)
        expected_n = np.zeros_like(n_marginal)
        expected_n[support] = p
        check(f"{name}: joint normalization", abs(weights.sum() - 1), 0, PROB_TOL)
        check(f"{name}: N marginal", np.max(np.abs(n_marginal - expected_n)), 0, PROB_TOL)
        check(f"{name}: conditional centered second moment",
              abs(centered_second - expected_centered_second), 0,
              PROB_TOL * max(1, expected_centered_second))
        check(f"{name}: pointwise rounding inequality",
              float(np.max(np.abs(z) - 2 * np.abs(k - estimate))), 0, PROB_TOL)
        check(f"{name}: rounded-error second moment", error_second, u, PROB_TOL)
        check(f"{name}: conditional integer translation",
              abs(h_z_cond - law["h_cond"]), 0, ENTROPY_TOL)
        check(f"{name}: conditioning reduces entropy", law["h_cond"], h_z, ENTROPY_TOL)
        check(f"{name}: integer entropy envelope", h_z, bound_f(u), ENTROPY_TOL)
        rows.append({
            "case": name, "eta": eta, "J": j, "support": support.tolist(),
            "input_mean": mean, "input_second_moment": float(np.dot(support ** 2, p)),
            "H_N_given_L_residue": law["h_cond"], "H_Z_given_L_residue": h_z_cond,
            "H_Z": h_z, "centered_second_moment": centered_second,
            "predicted_centered_second_moment": expected_centered_second,
            "rounded_error_second_moment": error_second, "u": u, "f_u": bound_f(u),
        })
    return rows


def check_arbitrary_references(rng: np.random.Generator) -> list[dict]:
    eta, j, cutoff = 0.7, 3, 8
    p = geometric_cutoff(0.9, cutoff)
    law = finite_joint(np.arange(cutoff + 1), p, eta, j)
    raw = rng.normal(size=(3, cutoff + 1)) + 1j * rng.normal(size=(3, cutoff + 1))
    raw[0] += 3  # Deliberately overlapping, nonorthogonal reference vectors.
    nonorthogonal = raw / np.linalg.norm(raw, axis=0, keepdims=True)
    vectors = {
        "orthogonal": np.eye(cutoff + 1, dtype=complex),
        "identical": np.tile(np.array([[1.0], [0.0]]), (1, cutoff + 1)),
        "nonorthogonal": nonorthogonal,
    }
    rows = []
    for name, reference_vectors in vectors.items():
        average_entropy, maximum_branch_gap, maximum_entropy_mismatch = 0.0, 0.0, 0.0
        for label in np.flatnonzero(law["marginal"]):
            mask = law["labels"] == label
            probability = law["marginal"][label]
            posterior = law["p"][mask] / probability
            branch = np.zeros((reference_vectors.shape[0], cutoff + 1), dtype=complex)
            for n, ell, w in zip(law["n"][mask], law["l"][mask], posterior, strict=True):
                branch[:, n - ell] += np.sqrt(w) * reference_vectors[:, n]
            rho_r, rho_b = branch @ branch.conj().T, branch.conj().T @ branch
            s_r, s_b = vn_entropy(rho_r), vn_entropy(rho_b)
            average_entropy += probability * s_r
            maximum_branch_gap = max(maximum_branch_gap, s_r - entropy(posterior))
            maximum_entropy_mismatch = max(maximum_entropy_mismatch, abs(s_r - s_b))
        check(f"{name}: each posterior reference entropy inequality",
              maximum_branch_gap, 0, ENTROPY_TOL)
        check(f"{name}: conditional pure-state entropy equality",
              maximum_entropy_mismatch, 0, ENTROPY_TOL)
        check(f"{name}: averaged reference entropy inequality",
              average_entropy, law["h_cond"], ENTROPY_TOL)
        if name == "orthogonal":
            check("orthogonal reference saturates classical bound",
                  abs(average_entropy - law["h_cond"]), 0, ENTROPY_TOL)
        if name == "identical":
            check("identical reference gives zero entanglement",
                  abs(average_entropy), 0, ENTROPY_TOL)
        if name == "nonorthogonal":
            check("nonorthogonal example is a strict inequality",
                  0.001, law["h_cond"] - average_entropy)
        rows.append({
            "reference": name, "reference_dimension": reference_vectors.shape[0],
            "eta": eta, "J": j, "data_cutoff": cutoff,
            "average_branch_entanglement": average_entropy,
            "classical_posterior_entropy": law["h_cond"],
            "strictness_gap": law["h_cond"] - average_entropy,
        })
    return rows


def displacement_block(delta: complex, cutoff: int) -> np.ndarray:
    """Analytic <m|D(delta)|n>; no displaced-state Fock truncation."""
    d = cutoff + 1
    result = np.empty((d, d), dtype=complex)
    gaussian = np.exp(-abs(delta) ** 2 / 2)
    for m in range(d):
        for n in range(d):
            finite_sum = sum(
                delta ** (m - k) * (-delta.conjugate()) ** (n - k)
                / (math.factorial(m - k) * math.factorial(n - k) * math.factorial(k))
                for k in range(min(m, n) + 1)
            )
            result[m, n] = gaussian * math.sqrt(math.factorial(m) * math.factorial(n)) * finite_sum
    return result


def displacement_block_laguerre(delta: complex, cutoff: int) -> np.ndarray:
    """Independent associated-Laguerre evaluation of the same exact entries."""
    result = np.empty((cutoff + 1, cutoff + 1), dtype=complex)
    x = abs(delta) ** 2
    for m in range(cutoff + 1):
        for n in range(cutoff + 1):
            if m >= n:
                result[m, n] = (math.sqrt(math.factorial(n) / math.factorial(m))
                               * delta ** (m - n) * eval_genlaguerre(n, m - n, x))
            else:
                result[m, n] = (math.sqrt(math.factorial(m) / math.factorial(n))
                               * (-delta.conjugate()) ** (n - m)
                               * eval_genlaguerre(m, n - m, x))
    return np.exp(-x / 2) * result


def gram_matrix(j: int, cutoff: int, a: float) -> np.ndarray:
    phases = 2 * np.pi * np.arange(j) / j
    alpha = a * j * np.exp(1j * phases)
    numbers = np.arange(cutoff + 1)
    d = cutoff + 1
    gram = np.empty((j * d, j * d), dtype=complex)
    for first in range(j):
        for second in range(j):
            delta = complex(alpha[second] - alpha[first])
            weyl_phase = np.exp(1j * np.imag(alpha[first].conjugate() * alpha[second]))
            rotations = np.exp(-1j * numbers[:, None] * phases[first]
                               + 1j * numbers[None, :] * phases[second])
            gram[first * d:(first + 1) * d, second * d:(second + 1) * d] = (
                weyl_phase * rotations * displacement_block(delta, cutoff)
            )
    check(f"Gram J={j}, M={cutoff}, a={a}: Hermiticity",
          np.linalg.norm(gram - gram.conj().T, ord=2), 0, MATRIX_TOL)
    vacuum_gram = np.exp(-abs(alpha[:, None]) ** 2 / 2 - abs(alpha[None, :]) ** 2 / 2
                        + alpha[:, None].conj() * alpha[None, :])
    check(f"Gram J={j}, M={cutoff}, a={a}: coherent vacuum block",
          np.max(np.abs(gram[::d, ::d] - vacuum_gram)), 0, MATRIX_TOL)
    return (gram + gram.conj().T) / 2


def positive_polynomial(distance: float, cutoff: int) -> float:
    total = 0.0
    for m in range(cutoff + 1):
        for n in range(cutoff + 1):
            for k in range(min(m, n) + 1):
                total += (math.sqrt(math.factorial(m) * math.factorial(n))
                          * distance ** (m + n - 2 * k)
                          / (math.factorial(m - k) * math.factorial(n - k) * math.factorial(k)))
    return total


def uniform_success_lower_bound(a: float, cutoff: int) -> float:
    """Analytic summable envelope, evaluated in floating point.

    Monomial Gaussian envelopes decrease for d>=sqrt(2M). Their h-series
    successive-term ratio is <=2^(2M) exp(-24a^2), for h>=1.
    """
    if 4 * a < math.sqrt(2 * cutoff):
        raise ValueError("Monotone-envelope condition is not satisfied")
    ratio = 2 ** (2 * cutoff) * math.exp(-24 * a * a)
    if ratio >= 1:
        raise ValueError("Geometric tail ratio is not below one")
    row_bound = 2 * positive_polynomial(4 * a, cutoff) * math.exp(-8 * a * a) / (1 - ratio)
    return max(0.0, 1 - row_bound)


def pure_loss_state(rho: np.ndarray, eta: float, cutoff: int, reference_dim: int) -> np.ndarray:
    d = cutoff + 1
    result = np.zeros_like(rho)
    for ell in range(d):
        kraus = np.zeros((d, d), dtype=complex)
        for n in range(ell, d):
            kraus[n - ell, n] = np.sqrt(binom.pmf(ell, n, 1 - eta))
        expanded = np.kron(np.eye(reference_dim), kraus)
        result += expanded @ rho @ expanded.conj().T
    return result


def partial_trace_output(rho: np.ndarray, reference_dim: int, output_dim: int) -> np.ndarray:
    return np.trace(rho.reshape(reference_dim, output_dim, reference_dim, output_dim), axis1=1, axis2=3)


def check_filter(rng: np.random.Generator) -> list[dict]:
    rows = []
    for j, cutoff, a in [(3, 2, 0.65), (5, 2, 1.2)]:
        eta, reference_dim = 0.7, 2
        d = cutoff + 1
        gram = gram_matrix(j, cutoff, a)
        values, vectors = np.linalg.eigh(gram)
        success = float(values[0])
        if success <= 0:
            raise AssertionError("A tested Gram matrix is not positive definite")
        root = (vectors * np.sqrt(values)) @ vectors.conj().T
        inverse_root = (vectors * (1 / np.sqrt(values))) @ vectors.conj().T
        # Exact finite coordinates on ran(V): columns of V become G^(1/2).
        # This is not a truncation of displaced optical states.
        left_inverse_error = float(np.linalg.norm(inverse_root @ root - np.eye(j * d), ord=2))
        cp_operator = success * inverse_root.conj().T @ inverse_root
        cp_maximum = float(np.linalg.eigvalsh(cp_operator)[-1])
        check(f"filter J={j}: left inverse", left_inverse_error, 0, MATRIX_TOL)
        check(f"filter J={j}: trace-nonincreasing success instrument", cp_maximum, 1, MATRIX_TOL)
        for state_name in ("random_entangled", "two_level_bell"):
            if state_name == "random_entangled":
                psi = rng.normal(size=reference_dim * d) + 1j * rng.normal(size=reference_dim * d)
                psi /= np.linalg.norm(psi)
            else:
                psi = np.zeros(reference_dim * d, dtype=complex)
                psi[0], psi[-1] = 1 / np.sqrt(2), 1 / np.sqrt(2)
            rho = np.outer(psi, psi.conj())
            loss_target = pure_loss_state(rho, eta, cutoff, reference_dim)
            physical = np.zeros((reference_dim * j * d, reference_dim * j * d), dtype=complex)
            for phase in range(j):
                encoding = np.kron(np.eye(reference_dim), root[:, phase * d:(phase + 1) * d])
                physical += encoding @ loss_target @ encoding.conj().T / j
            recovered = np.zeros_like(loss_target)
            for outcome in range(j):
                decoding = np.kron(np.eye(reference_dim),
                                   np.sqrt(success) * inverse_root[outcome * d:(outcome + 1) * d, :])
                recovered += decoding @ physical @ decoding.conj().T
            map_error = float(np.linalg.norm(recovered - success * loss_target, ord="fro"))
            success_error = abs(float(np.trace(recovered).real) - success)
            reference_error = float(np.linalg.norm(
                partial_trace_output(recovered, reference_dim, d)
                - success * partial_trace_output(rho, reference_dim, d), ord="fro"))
            check(f"filter J={j}, {state_name}: exact reference-data map",
                  map_error, 0, MATRIX_TOL)
            check(f"filter J={j}, {state_name}: state-independent success",
                  success_error, 0, MATRIX_TOL)
            check(f"filter J={j}, {state_name}: reference marginal",
                  reference_error, 0, MATRIX_TOL)
            rows.append({
                "J": j, "M": cutoff, "a": a, "state": state_name,
                "q_min": success, "gram_condition_number": float(values[-1] / values[0]),
                "left_inverse_operator_error": left_inverse_error, "CP_operator_max_eigenvalue": cp_maximum,
                "reference_data_map_frobenius_error": map_error,
                "success_probability_error": success_error, "reference_marginal_error": reference_error,
            })
    return rows


def lost_distribution(p: np.ndarray, eta: float) -> np.ndarray:
    result = np.zeros(p.size)
    for n, pn in enumerate(p):
        result[:n + 1] += pn * binom.pmf(np.arange(n + 1), n, 1 - eta)
    return result


def check_rates_and_scaling() -> dict:
    eta, cutoff, mu, a, target_rate = 0.7, 2, 1.0, 1.2, 0.5
    p = geometric_cutoff(mu, cutoff)
    mean = float(np.dot(np.arange(cutoff + 1), p))
    loss_p = lost_distribution(p, eta)
    r0 = entropy(p) - entropy(loss_p)
    uniform_lower = uniform_success_lower_bound(a, cutoff)
    check("example: analytic uniform success lower bound is positive", 0, uniform_lower)
    check("example: analytic guaranteed rate exceeds target", target_rate, uniform_lower * r0)
    rows = []
    for j in (2, 3, 4, 8, 16, 32, 64):
        gram = gram_matrix(j, cutoff, a)
        values = np.linalg.eigvalsh(gram)
        s = float(values[0])
        check(f"scaling J={j}: Gram eigenvalue above uniform envelope",
              uniform_lower, s, MATRIX_TOL)
        rows.append({
            "J": j, "Gram_dimension": int(gram.shape[0]), "carrier_output_amplitude": a * j,
            "q_min": s, "gram_distance_from_identity": float(np.max(np.abs(values - 1))),
            "rate_s_R0": s * r0, "charged_input_energy": mean + (a * j) ** 2 / eta,
        })
    cutoff_rows = []
    limit_mu = 3.0
    ratio = limit_mu / (1 + limit_mu)
    target_h_l = bosonic_g((1 - eta) * limit_mu)
    for m in (4, 12, 32, 64):
        truncated = geometric_cutoff(limit_mu, m)
        loss_truncated = lost_distribution(truncated, eta)
        eps = ratio ** (m + 1)
        predicted_h_n = bosonic_g(limit_mu) - binary_entropy(eps) / (1 - eps)
        h_n, h_l = entropy(truncated), entropy(loss_truncated)
        tail_bound = (eps * (target_h_l + bosonic_g((1 - eta) * (m + 1 + limit_mu)))
                      + binary_entropy(eps)) / (1 - eps)
        check(f"cutoff M={m}: geometric conditional entropy identity",
              abs(h_n - predicted_h_n), 0, ENTROPY_TOL)
        check(f"cutoff M={m}: explicit lost-count entropy convergence bound",
              abs(h_l - target_h_l), tail_bound, ENTROPY_TOL)
        cutoff_rows.append({
            "M": m, "tail_probability": eps, "H_input": h_n, "H_loss": h_l,
            "reverse_coherent_information": h_n - h_l,
            "loss_entropy_limit": target_h_l, "loss_entropy_error": abs(h_l - target_h_l),
            "analytic_loss_entropy_error_bound": tail_bound,
        })
    return {
        "eta": eta, "M": cutoff, "untruncated_geometric_mean": mu,
        "p": p.tolist(), "lost_count_probabilities": loss_p.tolist(),
        "data_mean_energy": mean, "reverse_coherent_information_R0": r0,
        "carrier_a": a, "carrier_energy_coefficient_a_squared_over_eta": a * a / eta,
        "target_rate": target_rate, "analytic_uniform_q_lower": uniform_lower,
        "analytic_uniform_rate_lower": uniform_lower * r0,
        "minimum_q_over_tested_J": min(row["q_min"] for row in rows),
        "tested_J_values": rows,
        "fixed_mu_cutoff_limit": {
            "eta": eta, "mu": limit_mu,
            "thermal_reverse_coherent_information": bosonic_g(limit_mu) - target_h_l,
            "cases": cutoff_rows,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    for cutoff in (2, 4):
        for delta in (0.7 + 0.2j, -1.1 + 0.4j, 2.7 - 0.3j):
            discrepancy = np.max(np.abs(displacement_block(delta, cutoff)
                                        - displacement_block_laguerre(delta, cutoff)))
            check(f"independent displacement formulas M={cutoff}, delta={delta}",
                  discrepancy, 0, 2e-12)
    result = {
        "status": "passed",
        "scope": "Finite numerical checks, not a proof or a capacity computation.",
        "environment": {
            "python": sys.version.split()[0], "numpy": np.__version__,
            "scipy": scipy.__version__, "random_seed": SEED,
        },
        "tolerances": {
            "probability_and_moment": PROB_TOL, "entropy": ENTROPY_TOL,
            "matrix_operator_or_frobenius": MATRIX_TOL,
        },
        "classical_converse": check_classical_converse(),
        "arbitrary_reference_inputs": check_arbitrary_references(rng),
        "exact_filter": check_filter(rng),
        "rate_energy_example": check_rates_and_scaling(),
        "checks": CHECKS,
    }
    result["number_of_checks"] = len(CHECKS)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    example = result["rate_energy_example"]
    print(json.dumps({
        "status": result["status"], "number_of_checks": len(CHECKS),
        "output": str(args.output),
        "example_R0": example["reverse_coherent_information_R0"],
        "example_uniform_q_lower": example["analytic_uniform_q_lower"],
        "example_uniform_rate_lower": example["analytic_uniform_rate_lower"],
        "example_minimum_q_tested": example["minimum_q_over_tested_J"],
    }, indent=2))


if __name__ == "__main__":
    main()
