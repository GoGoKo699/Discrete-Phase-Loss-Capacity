# Numerical verification

These checks exercise concrete implementation risks in the analytical theorem.
They are **finite numerical checks, not a proof, a capacity computation, or a
search over all inputs**. The scientific arguments establish the statements for
all alphabet sizes and all finite-mean states.

## Reproduce

The committed output was generated with Python **3.12.14**, NumPy **2.3.5**, and
SciPy **1.17.0**. The numerical packages are pinned in `requirements.txt`. From the
repository root, run:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_theorem.py
```

The script uses the fixed seed `20261105`, takes about one second in the recorded
environment, and writes `verification/results.json`. An alternative output path
can be supplied with `--output`. No network or external data are needed after
installing the dependencies. The script exits unsuccessfully at the first failed
check; a successful run currently records **109 checks**.

## What is checked

| Part | Concrete checks |
|---|---|
| Classical converse | Construct the joint law of photon number, lost count, and residue directly for finite-support distributions. Check normalization, marginals, the centered-binomial second moment, the pointwise rounding inequality, the conditional integer-translation entropy identity, and the integer-error entropy bound. Cases include vacuum, a truncated geometric law, separated peaks, a rare bright tail, and one residue class. |
| Arbitrary references | Construct conditional pure reference–receiver states using orthogonal, identical, and deliberately nonorthogonal reference vectors. Check equality of the two marginal entropies and the reference entropy upper bound by the classical posterior entropy. Orthogonal vectors saturate the bound; identical vectors give zero entanglement; the nonorthogonal example has a strict gap. |
| Displacement matrix elements | Compare the finite normal-ordered sum against an independent associated-Laguerre evaluation for complex displacements. Check Gram Hermiticity and the coherent-state vacuum overlap, including its Weyl phase. |
| Exact recovery instrument | Check the left inverse and trace-nonincreasing success operator. Simulate the encoded mixed phase branches and recovery on random entangled and Bell-like reference–data states. Check the full successful output against the predicted scalar multiple of the pure-loss output, the success probability, and the reference marginal. |
| Energy and rate | Compute the finite-support input and lost-count entropies, reverse coherent information, charged carrier energy, and rate after heralding. Evaluate an explicit analytic uniform Gram bound and compare it with eigenvalues for seven alphabet sizes. Check finite-cutoff entropy convergence against an explicit geometric-tail bound. |

### Avoiding a misleading optical cutoff

The data cutoff $`M`$ is part of the proposed code. Displaced codewords themselves
have infinite Fock support. The script does **not** approximate their inner
products by projecting displaced states onto a second, artificial photon cutoff.
Instead it evaluates the exact entries

```math
\langle m|D(\delta)|n\rangle
=e^{-|\delta|^2/2}\sqrt{m!n!}
\sum_{k=0}^{\min(m,n)}
\frac{\delta^{m-k}(-\delta^*)^{n-k}}
     {(m-k)!(n-k)!k!}.
```

For recovery, it uses finite orthonormal coordinates on the exact span of the
codewords: the synthesis map is represented by $`G^{1/2}`$, and the stacked left
inverse by $`G^{-1/2}`$. This preserves the physical Gram matrix without
truncating displaced optical states. The operation can be extended by zero
outside this span and completed by a failure outcome.

The probability tolerance is $`4\times10^{-12}`$, with relative scaling for the
centered second moment. Entropy checks use $`5\times10^{-10}`$ bits, and matrix
identities use $`3\times10^{-10}`$ in the specified operator or Frobenius norm.
Each check and its actual value, bound, and tolerance are retained in the JSON.
Underflowed binomial tails are omitted only below floating-point resolution;
normalization and input marginals are checked afterward.

## A quantitative example

Take

```math
\eta=0.7,\qquad M=2,\qquad
p=(4,2,1)/7,\qquad A=1.2J.
```

The input data mean is $`4/7`$, and its reverse coherent information is

```math
R_0=H(p)-H(L)\approx0.6835261561.
```

The **charged physical input energy** per attempted channel use is

```math
E=\frac47+\frac{72}{35}J^2
  \approx\frac47+2.0571428571J^2.
```

The first field moment of the Fock-diagonal data marginal is zero, so there is no
displacement cross term. Both failed and successful attempts count.

For this example, the positive polynomial in the analytic envelope is

```math
B_2(d)=\tfrac12d^4+\sqrt2\,d^3+(3+\sqrt2)d^2+(2+2\sqrt2)d+3.
```

Define the exact analytic lower bound

```math
b_*=1-\frac{2B_2(24/5)e^{-288/25}}{1-16e^{-864/25}}.
```

The bound gives $`s\ge b_*`$ and $`sR_0\ge b_*R_0`$ for every $`J\ge2`$.
Floating-point evaluation gives $`b_*\approx0.9890834744`$ and
$`b_*R_0\approx0.6760644254`$. These decimals are approximate evaluations of
the exact expression, not interval-certified numerical bounds. The construction
has a substantial margin above the illustrative target of $`0.5`$ ebits per
attempted use.

| $`J`$ | Numerically evaluated $`\lambda_{\min}(G)`$ | Charged photons per attempt |
|---:|---:|---:|
| 2 | 0.9975715971 | 8.8000 |
| 3 | 0.9999950332 | 19.0857 |
| 4 | 0.9999998246 | 33.4857 |
| 8 | 0.9999999949 | 132.2286 |
| 16 | 0.9999999981 | 527.2000 |
| 32 | 0.9999999985 | 2107.0857 |
| 64 | 0.9999999986 | 8426.6286 |

The smallest evaluated eigenvalue is $`0.9975715971`$, at $`J=2`$. The finite table
does not establish a bound for untested alphabet sizes. Uniformity comes from the
analytic estimate: if $`B_M(d)`$ is the sum of absolute monomials in the cutoff
displacement matrix and $`4a\ge\sqrt{2M}`$, then, with
$`r=2^{2M}e^{-24a^2}<1`$,

```math
\|G-I\|
\le 2\sum_{h\ge1}B_M(4ah)e^{-8a^2h^2}
\le \frac{2B_M(4a)e^{-8a^2}}{1-r}.
```

The second inequality follows by bounding the ratio of successive positive
terms by $`r`$. The polynomial is defined explicitly in the script.

## Limits of this verification

The finite-support checks cannot establish the converse for states with infinite
photon-number variance. That conclusion follows from the analytic conditional
second-moment identity, which requires only finite mean. The adaptive capacity
bound and reverse hashing likewise rely on their stated information-theoretic
theorems, not on these simulations.

No efficient implementation of the non-Gaussian recovery instrument is claimed.
Continuous phase perturbations, a correlated phase process, joint limits in
loss and alphabet size, and optimal energy constants are outside these checks.

## Hosted mathematical display

The [browser collector](hosted/capture_hosted_math.cjs) compares the mathematical expressions in a pinned Git revision with their actual rendering on GitHub. It inspects every tracked Markdown page at widths of 1440 and 760 pixels, including formulas in tables. The [text contract](hosted/math-contract.json) adds explicit expected text for the overview and repaired model displays.

The source and hosted sides have different roles. MathJax compiles the source into an expected MathML structure; Chromium reads the MathML actually supplied by GitHub. The collector compares symbols, scripts, fractions, labels, expression counts and bounded display geometry, then saves the HTML, screenshots, inventories and report. Inspect the screenshots as well: a structural pass does not establish visual legibility or scientific correctness.

To reproduce from an exact checked-out commit, install the browser dependencies outside the repository and use a new evidence directory:

```bash
npm install --prefix /tmp/phase-loss-hosted-deps playwright@1.56.1 mathjax-full@3.2.1
/tmp/phase-loss-hosted-deps/node_modules/.bin/playwright install chromium
checked_revision="$(git rev-parse HEAD)"
NODE_PATH=/tmp/phase-loss-hosted-deps/node_modules node verification/hosted/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Discrete-Phase-Loss-Capacity \
  --revision "$checked_revision" \
  --contract verification/hosted/math-contract.json \
  --output /tmp/phase-loss-hosted-evidence
```

This requires Node.js 18 or later, Python 3.10 or later, Git and a compatible Chromium environment. The pinned commit must already exist on the public repository: local working changes are not the hosted source. A report passes only for its recorded revision and page scope. The read-only pull-request workflow runs the same full-page comparison and retains its diagnostic captures for seven days. A failed request or rendering check remains failed until a fresh, successful capture is inspected.
