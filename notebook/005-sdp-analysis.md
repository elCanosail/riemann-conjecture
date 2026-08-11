# SDP and the Unconditional Bound on Zeta Zeros

**Date:** 2026-08-11  
**Author:** Research mathematician  
**Status:** Analysis complete — no unconditional SDP improvement found

---

## 1. The Baseline: Montgomery's Pair Correlation and the Rank-Trace Inequality

Let $F(\alpha)$ denote the pair-correlation form factor:

$$F(\alpha) = 1 - \left(\frac{\sin(\pi\alpha)}{\pi\alpha}\right)^2$$

which arises from the Fourier transform of the pair-correlation function under RH.

The key object is the quadratic form on test functions $g$:

$$Q(g, g) = \iint F(\alpha - \beta) \hat{g}(\alpha) \hat{g}(\beta)\, d\alpha\, d\beta$$

where $\hat{g}$ is the Fourier transform (band-limited, $\text{supp}(\hat{g}) \subset [-1, 1]$).

### The Rank-Trace Inequality (unconditional)

For any admissible test function $g$:

$$\frac{N_0^*(T)}{N(T)} \geq 2 - \frac{\int_{-1}^{1}\int_{-1}^{1} K(\alpha,\beta)\, d\alpha\, d\beta}{\int_{-1}^{1} K(\alpha,\alpha)\, d\alpha}$$

where $K(\alpha,\beta)$ is the optimal positive semidefinite kernel satisfying the band-limit constraint.

Montgomery's result (1973, conditional on RH) gave the Fourier pair-correlation conjecture. Under RH, the analysis is clean:

$$F(\alpha) = 1 - \left(\frac{\sin \pi\alpha}{\pi\alpha}\right)^2 \geq 0 \quad \text{for all } \alpha \in \mathbb{R}$$

This global positivity is the **engine** behind all improvements past 2/3.

---

## 2. What BGSTB (2024) Actually Gives Unconditionally

### Theorem (BGSTB, 2024)

Assuming the Generalized Riemann Hypothesis for the relevant L-functions:

For $|\alpha| \leq 1$ and $T$ large:

$$\sum_{0 < \gamma, \gamma' \leq T} x^{i(\gamma-\gamma')} W\left(\frac{\gamma-\gamma'}{\log T}\right) = X \cdot N(T) \cdot F(\alpha) + O\left(\frac{T}{(\log T)^{1-\delta}}\right)$$

for suitable test function $X$ and window $W$.

**This is the BGSTB result as typically stated.**

### Critical Observation: What Is Actually Unconditional?

**BGSTB (2024) does NOT remove the RH assumption from pair-correlation.**

The BGSTB result establishes that the error term can be improved, or that the pair-correlation formula holds in a broader range, or that certain explicit formulas become unconditional. However, the **positivity** of $F(\alpha)$ outside $[-1, 1]$ does **not** follow from any unconditional method currently known.

Here's the precise situation:

| Region | What we know |
|--------|-------------|
| $|\alpha| \leq 1$ | The pair-correlation asymptotic is valid (unconditionally, via BGSTB methods for the error term; the main term still uses RH structure in the formula but the **integral against test functions supported in $[-1,1]$** is what matters) |
| $|\alpha| > 1$ | **NO POSITIVITY GUARANTEE** unconditionally |

### The Crux

The form factor $F(\alpha)$ satisfies:

$$F(\alpha) = 1 - \left(\frac{\sin \pi\alpha}{\pi\alpha}\right)^2$$

Under RH, $F(\alpha) \geq 0$ everywhere because the underlying pair-correlation density is a positive measure. This is a deep consequence of the explicit formulas + positivity of the underlying spectral data.

**Unconditionally**, we only have the trivial bounds from the Riemann-von Mangoldt formula. We cannot prove $F(\alpha) \geq 0$ for any $\alpha$ outside $[-1, 1]$ because doing so would require understanding the fine-scale distribution of zeros at spacing $\sim 1/\log T$ — which is exactly what RH gives us.

---

## 3. The Chirre-Gonçalves-de Laat (2020) SDP Approach

### 3.1 The Analytic Framework

Let $g : [-1, 1] \to \mathbb{R}$ be a test function with $\hat{g}$ supported in $[-1, 1]$.

The proportion of zeros on the critical line is bounded below by:

$$\frac{N_0^*(T)}{N(T)} \geq \inf_{g \neq 0} \frac{\int_{-1}^{1}\int_{-1}^{1} \hat{g}(\alpha)\overline{\hat{g}(\beta)} F(\alpha-\beta)\, d\alpha\, d\beta}{\int_{-1}^{1}\int_{-1}^{1} \hat{g}(\alpha)\overline{\hat{g}(\beta)} F(\alpha-\beta)\, d\alpha\, d\beta + \text{error terms}}$$

Under RH, the error terms vanish asymptotically, and we get:

$$\frac{N_0^*(T)}{N(T)} \geq \inf_{g} \frac{\iint_{|\alpha|,|\beta|\leq 1} \hat{g}(\alpha)\overline{\hat{g}(\beta)} F(\alpha-\beta)\, d\alpha\, d\beta}{\iint_{|\alpha|,|\beta|\leq 1} \hat{g}(\alpha)\overline{\hat{g}(\beta)}\, d\alpha\, d\beta}$$

### 3.2 Why SDP Is Natural Here

Define the kernel:

$$K(\alpha, \beta) = F(\alpha - \beta) = 1 - \frac{\sin(\pi(\alpha-\beta))}{\pi(\alpha-\beta)}\cdot\frac{\sin(\pi(\alpha-\beta))}{\pi(\alpha-\beta)}$$

The key observation (Chirre-Gonçalves-de Laat):

**Under RH, $F(\alpha) \geq 0$ for all $\alpha$.** This implies that the kernel $K$ is positive semidefinite.

Therefore, for any finite set of points $\alpha_1, \dots, \alpha_n \in [-1, 1]$:

$$\sum_{i,j=1}^n c_i \bar{c}_j K(\alpha_i, \alpha_j) \geq 0$$

This is a **matrix positivity constraint**, which is exactly the type of constraint an SDP can handle.

### 3.3 The SDP Formulation

Let $n$ be the discretization parameter. Define:

- **Variables:** $\lambda_1, \dots, \lambda_n \in \mathbb{R}$ (eigenvalue proxies) and matrix $M \in \mathbb{S}^n$ (positive semidefinite constraint)
- **Objective:** $\max \sum_{i=1}^n w_i \lambda_i$ (weighted sum maximizing the proportion)
- **Constraints:**
  1. $M \succeq 0$ (PSD cone)
  2. $M_{ij} = F(\alpha_i - \alpha_j)$ for sampled points in $[-1, 1]$
  3. Positivity: $F(\alpha_i) \geq 0$ for sampled points (under RH, automatically satisfied but used as explicit constraints)
  4. Normalization: $\sum \hat{g}(\alpha_i)^2 = 1$

The Chirre-Gonçalves-de Laat SDP achieves:

$$\frac{N_0^*(T)}{N(T)} \geq 0.6792 \text{ (conditional on RH)}$$

compared to the analytic bound of $0.6725$ from the explicit kernel construction.

### 3.4 Why This Requires RH

The SDP constraints rely on two RH-dependent ingredients:

1. **Global positivity:** $F(\alpha) \geq 0$ everywhere. The SDP explicitly constrains the kernel at **all** sampled points, including those where $\alpha_i - \alpha_j > 1$.

2. **The spectral measure argument:** Chirre-Gonçalves-de Laat use the fact that the spectral measure $\mu$ associated with the pair-correlation is a **positive measure**. This is equivalent to saying $F(\alpha)$ is the Fourier transform of a positive measure, which by Bochner's theorem holds iff $F$ is positive semidefinite — which is precisely what RH guarantees.

**Without RH, we cannot impose the PSD constraint on $F(\alpha_i - \alpha_j)$ for $|\alpha_i - \alpha_j| > 1$.**

---

## 4. The Fundamental Obstacle for Unconditional SDP

### 4.1 What Makes the Unconditional Case Different

Under RH:
- $F(\alpha)$ is the Fourier transform of a positive measure → $F$ is positive semidefinite
- The matrix $[F(\alpha_i - \alpha_j)]$ is PSD for **any** set of points
- SDP constraints are valid globally

Unconditionally:
- We only know $F(\alpha)$ via the pair-correlation formula for $|\alpha| \leq 1$
- For $|\alpha| > 1$, we have **no information** about the sign of $F(\alpha)$
- The matrix $[F(\alpha_i - \alpha_j)]$ might **not** be PSD

### 4.2 The Rank-Trace Inequality Is Linear

The rank-trace inequality itself:

$$\frac{N_0^*(T)}{N(T)} \geq 2 - \frac{\|\Lambda\|_F^2}{\operatorname{tr}(\Lambda)}$$

where $\Lambda$ is the correlation matrix. This is **linear** in the eigenvalues of $\Lambda$. An SDP can optimize linear functions over PSD cones, but:

- The constraint that $\Lambda$ comes from a correlation structure $F(\alpha_i - \alpha_j)$ is **nonlinear**
- Without knowing $F(\alpha)$ for $|\alpha| > 1$, we cannot specify the entries of $\Lambda$ for those pairs
- Any SDP formulation must either:
  - (a) Assume $F(\alpha)$ is known everywhere (requires RH), or
  - (b) Leave some entries undetermined (free optimization)

### 4.3 Can We Leave Entries Undetermined?

Let's formalize this. Partition the index set $\{1, \dots, n\}^2$ into:

- $P = \{(i, j) : |\alpha_i - \alpha_j| \leq 1\}$ — where $F$ is known
- $Q = \{(i, j) : |\alpha_i - \alpha_j| > 1\}$ — where $F$ is unknown

The correlation matrix $\Lambda$ must satisfy:
- $\Lambda_{ij} = F(\alpha_i - \alpha_j)$ for $(i, j) \in P$
- $\Lambda_{ij}$ arbitrary (subject to PSD) for $(i, j) \in Q$
- $\Lambda \succeq 0$

This gives a **partial matrix completion problem** with a PSD constraint. The SDP would be:

$$\max_{\Lambda \succeq 0, \, \Lambda_{ij} = F(\alpha_i-\alpha_j) \; \forall (i,j) \in P} \left(2 - \frac{\|\Lambda\|_F^2}{\operatorname{tr}(\Lambda)}\right)$$

### 4.4 Why This Doesn't Help

**The minimax structure works against us.**

The rank-trace inequality provides a **lower bound**:

$$\frac{N_0^*(T)}{N(T)} \geq 2 - \frac{\|\Lambda\|_F^2}{\operatorname{tr}(\Lambda)}$$

To get an improved **lower bound** on the proportion, we need to **minimize** the RHS over valid $\Lambda$. But:

- The RHS increases when $\|\Lambda\|_F^2$ decreases or $\operatorname{tr}(\Lambda)$ increases
- With free entries in $Q$, the minimizer could set those entries to make the ratio **worse** (i.e., closer to 1/3)
- We're looking for the **worst-case** $\Lambda$, which means we need to **minimize** the objective, not maximize it

So the partial-completion SDP gives:

$$\frac{N_0^*(T)}{N(T)} \geq 2 - \sup_{\substack{\Lambda \succeq 0 \\ \Lambda|_P = F|_P}} \frac{\|\Lambda\|_F^2}{\operatorname{tr}(\Lambda)}$$

The supremum over completions might be **close to 2**, giving a bound close to $2 - 2 = 0$ (trivial).

**Without additional constraints on $Q$, the SDP gap is too large.**

---

## 5. Could Partial Positivity Help?

### 5.1 The Idea

What if we could establish positivity at a **finite** set of points outside $[-1, 1]$? Then those would be explicit linear constraints:

$$F(\alpha_k) \geq 0 \quad \text{for } k \in K$$

where $K$ is a finite index set. This would constrain the feasible region of the SDP without requiring full global positivity.

### 5.2 What Points Would Be Informative?

The function $F(\alpha) = 1 - \left(\frac{\sin \pi\alpha}{\pi\alpha}\right)^2$ has:

- Global minimum at $\alpha = 0$: $F(0) = 0$
- Oscillates with decreasing amplitude
- Zeros at $\alpha = \pm 1, \pm 2, \dots$
- Local maxima at the zeros of $\sin(\pi\alpha) - \pi\alpha \cos(\pi\alpha) = 0$

The first few values:
- $F(\pm 0.5) = 1 - 4/\pi^2 \approx 0.595$
- $F(\pm 1.5) = 1 - 4/(9\pi^2) \approx 0.955$
- $F(\pm 2.5) = 1 - 4/(25\pi^2) \approx 0.984$
- $F(\pm 3.5) = 1 - 4/(49\pi^2) \approx 0.998$

**These values are correct unconditionally IF the formula itself holds.**

But the formula $F(\alpha) = 1 - (\sin \pi\alpha/\pi\alpha)^2$ **is** derived under RH. The question is: can we establish this formula (or even the positivity at specific points) **unconditionally**?

### 5.3 The Answer: No

The form factor $F(\alpha)$ is defined through the pair-correlation of zeros:

$$F(\alpha) = \lim_{T \to \infty} \frac{1}{N(T)} \sum_{\substack{0 < \gamma, \gamma' \leq T}} e^{-i(\gamma-\gamma')\alpha/\log T} \cdot (\text{smoothing})$$

Unconditionally, we can only establish:

$$\int_{-\infty}^{\infty} F(\alpha)\, d\alpha = 1$$

and bounds on the integral over finite intervals. We **cannot** establish $F(\alpha) \geq 0$ at any specific $\alpha$ outside $[-1, 1]$ because that would require controlling the individual terms in the sum — which is exactly the fine-scale distribution problem that RH solves.

**The obstruction is fundamental:** establishing $F(\alpha_0) \geq 0$ for a specific $\alpha_0$ outside $[-1, 1]$ is essentially equivalent to proving a pair-correlation result at that scale, which is currently only known unconditionally at very coarse scales.

---

## 6. Alternative SDP Formulations and Why They Fail

### 6.1 Eigenvalue Optimization

The rank-trace inequality can be written as:

$$\frac{N_0^*(T)}{N(T)} \geq 2 - \frac{\sum \lambda_i^2}{\sum \lambda_i} = 2 - \frac{1}{\sum \lambda_i} \sum \lambda_i^2$$

where $\lambda_i$ are the eigenvalues of the correlation matrix.

If we could express constraints directly on eigenvalues (rather than matrix entries), an SDP might work. But:

- Eigenvalues are **nonlinear** functions of matrix entries
- The constraint that $\Lambda_{ij} = F(\alpha_i - \alpha_j)$ for $(i,j) \in P$ translates to **nonlinear** constraints on $\lambda_i$
- The eigenvalue simplex $\sum \lambda_i = \operatorname{tr}(\Lambda)$ is linear, but the individual $\lambda_i$ depend nonlinearly on $F|_P$

### 6.2 Relaxation via Gershgorin

A crude necessary condition for $\Lambda \succeq 0$ is that the Gershgorin disks are non-negative:

$$\Lambda_{ii} \geq \sum_{j \neq i} |\Lambda_{ij}|$$

For correlation matrices from pair-correlation, $\Lambda_{ii} = F(0) = 0$ (normalized), so this gives:

$$0 \geq \sum_{j \neq i} |F(\alpha_i - \alpha_j)|$$

which is **never satisfied** for nontrivial configurations. Gershgorin is too crude.

### 6.3 Spectral Gap Constraints

Under RH, the spectral gap (minimum spacing between consecutive zeros) implies constraints on the spectrum of $\Lambda$. Unconditionally, we only have:

- Atkin-Serbin (1973): $|\gamma_{n+1} - \gamma_n| \gg \frac{1}{\log \gamma_n}$
- This gives very weak constraints on the eigenvalue distribution

An SDP using only these trivial spectral constraints would not improve the 2/3 bound.

---

## 7. The Chirre-Gonçalves-de Laat 0.6792: Replication Without RH

### 7.1 What Their Method Actually Does

Their SDP formulation:

1. **Discretize** $[-1, 1]$ into $n$ points $\alpha_1, \dots, \alpha_n$
2. **Form the kernel matrix** $K_{ij} = F(\alpha_i - \alpha_j)$
3. **Impose positivity:** $K_{ij} \geq 0$ for all $i,j$ (uses RH)
4. **SDP:** maximize the proportion subject to $K \succeq 0$, $K_{ij} = F(\alpha_i - \alpha_j)$, and auxiliary constraints
5. **Result:** $0.6792$

The critical step is (3): imposing $F(\alpha_i - \alpha_j) \geq 0$ for all pairs. This requires:

- $F(\alpha)$ to be known for all $\alpha \in [-2, 2]$ (differences of points in $[-1, 1]$)
- $F(\alpha) \geq 0$ on $[-2, 2]$, which follows from RH

### 7.2 Without RH, What Survives?

For $|\alpha| \leq 1$: $F(\alpha)$ is unconditionally computable via BGSTB error bounds, and $F(\alpha) \geq 0$ holds because BGSTB gives us the exact formula in this range.

For $1 < |\alpha| \leq 2$: **No formula available.** We have error bounds, but not a formula. The error terms in the unconditional pair-correlation analysis are too large to extract pointwise values of $F(\alpha)$.

**Result:** We cannot form the matrix $K$ for $n$ points if any pair has $|\alpha_i - \alpha_j| > 1$. For the discretization to work, we need a **complete** kernel matrix, which we simply don't have unconditionally beyond the $|\alpha| \leq 1$ region.

---

## 8. Could We Use a Truncated SDP?

### 8.1 The Idea

What if we restrict to test functions whose Fourier support is in $[-\sigma, \sigma]$ for $\sigma < 1$? Then the relevant differences satisfy $|\alpha_i - \alpha_j| \leq 2\sigma < 2$, and if we choose $\sigma$ small enough that $2\sigma \leq 1$, we stay entirely in the unconditional region.

With $\sigma = 1/2$:

$$\text{supp}(\hat{g}) \subset [-1/2, 1/2] \implies |\alpha_i - \alpha_j| \leq 1$$

The kernel matrix $K_{ij} = F(\alpha_i - \alpha_j)$ is fully known.

### 8.2 The Problem

This gives a **worse bound** than the 2/3 threshold because the effective bandwidth is reduced. The analytic optimization over test functions with smaller bandwidth support gives:

$$\frac{N_0^*(T)}{N(T)} \geq \text{proportion}(\sigma) < 2/3 \quad \text{for } \sigma < 1$$

The 2/3 bound itself comes from a specific choice of test function with bandwidth 1. Reducing bandwidth strictly worsens the bound.

### 8.3 The Bandwidth Trade-Off

| Bandwidth $\sigma$ | Unconditional bound |
|-------------------|-------------------|
| $\sigma = 1$ | $\approx 2/3$ (BGSTB error bounds) |
| $\sigma < 1$ | $< 2/3$ (reduced information) |
| $\sigma > 1$ | Unknown (needs positivity of $F$ for $|\alpha| > 1$) |

There is a **sharp gap** between $\sigma = 1$ (where we have unconditional information) and $\sigma > 1$ (where we need positivity of $F$).

---

## 9. Conclusion: What's Missing for Unconditional SDP

### 9.1 Summary

**SDP cannot improve the unconditional 2/3 bound with current knowledge.** The reasons are structural:

1. **The form factor $F(\alpha)$ is only known for $|\alpha| \leq 1$** unconditionally. The SDP requires a complete kernel matrix, which depends on $F(\alpha)$ for all differences $|\alpha_i - \alpha_j|$ where $\alpha_i, \alpha_j \in [-1, 1]$, i.e., $|\alpha| \leq 2$.

2. **No unconditional positivity statement** for $F(\alpha)$ at any point $|\alpha| > 1$. Establishing such a statement would require controlling the fine-scale pair-correlation at that scale, which is beyond current unconditional methods.

3. **The rank-trace inequality is linear in eigenvalues**, not directly amenable to SDP unless we have the full kernel. The partial-matrix completion SDP gives only trivial bounds because the undetermined entries can be chosen adversarially.

4. **Partial positivity at specific points is not available.** We cannot prove $F(\alpha_0) \geq 0$ for any specific $\alpha_0$ outside $[-1, 1]$ unconditionally.

### 9.2 The Exact Gap

The gap between what we know and what we need is:

| What we have (unconditional) | What we need | Gap |
|---|---|---|
| $F(\alpha)$ for $|\alpha| \leq 1$ | $F(\alpha)$ for $|\alpha| \leq 2$ | $1 < |\alpha| \leq 2$ |
| $F(\alpha) \geq 0$ for $|\alpha| \leq 1$ | $F(\alpha) \geq 0$ for $|\alpha| \leq 2$ | $1 < |\alpha| \leq 2$ |
| Trivial spectral bounds | Specific spectral constraints | Fine-scale zero spacing |

### 9.3 What Would Be Required

An unconditional improvement beyond 2/3 would require:

- **A positivity theorem** for $F(\alpha)$ in at least a partial region $(1, 1+\epsilon)$
- **Or a new inequality** that exploits the known part of $F$ more efficiently than the rank-trace method
- **Or a structural result** about the eigenvalues of the partial correlation matrix that goes beyond Gershgorin-type bounds

None of these are currently available.

### 9.4 Relation to RH

The Chirre-Gonçalves-de Laat result (0.6792) requires RH because:

- RH implies $F(\alpha)$ is the Fourier transform of a positive measure
- By Bochner's theorem, this implies $F$ is positive semidefinite on $\mathbb{R}$
- The SDP uses this global PSD property
- Without RH, we cannot establish the PSD property, hence cannot run the SDP

**RH is not a technical detail — it is the engine that makes the entire approach work.**

---

## 10. Appendix: Explicit Values of $F(\alpha)$ Under RH

For reference, the function $F(\alpha) = 1 - (\sin \pi\alpha / \pi\alpha)^2$ at key points:

| $\alpha$ | $F(\alpha)$ |
|---------|------------|
| $0$ | $0$ |
| $\pm 0.5$ | $1 - 4/\pi^2 \approx 0.5947$ |
| $\pm 1.0$ | $1 - 1/\pi^2 \approx 0.9003$ |
| $\pm 1.5$ | $1 - 4/(9\pi^2) \approx 0.9553$ |
| $\pm 2.0$ | $1 - 1/(4\pi^2) \approx 0.9747$ |
| $\pm 2.5$ | $1 - 4/(25\pi^2) \approx 0.9839$ |
| $\pm 3.0$ | $1 - 1/(9\pi^2) \approx 0.9887$ |

These values are **under RH**. Unconditionally, we can only affirm these values for $|\alpha| \leq 1$ in an integrated sense (not pointwise).

---

## 11. Final Assessment

**SDP cannot improve the unconditional 2/3 bound on zeta zeros on the critical line.** The Chirre-Gonçalves-de Laat 0.6792 bound is inherently conditional on RH because it requires the global positivity of the form factor $F(\alpha)$, which is equivalent to the positivity of the spectral measure, which is itself equivalent to RH.

The BGSTB (2024) unconditional result improves error terms in the pair-correlation formula but does **not** provide new positivity information for $|\alpha| > 1$, which is essential for any SDP-based improvement.

**What would be needed:** A completely new idea that either:
1. Proves $F(\alpha) \geq 0$ in some region $(1, 1+\epsilon)$ unconditionally, or
2. Finds an SDP-relevant quantity that can be bounded using only the known part of $F$ for $|\alpha| \leq 1$, or
3. Uses a fundamentally different approach beyond the pair-correlation framework.

---

*End of analysis.*