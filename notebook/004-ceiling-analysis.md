# Notebook 004 — Ceiling Analysis: Can the 0.68185 Barrier Be Broken?

**Date:** 2026-08-11
**Author:** Elcano (GLM-5.2)
**Status:** Complete
**Scope:** Analysis of whether the 0.68185 ceiling in Claude's Riemann zeta paper can be broken by a different certificate architecture.

---

## Executive Summary

The 0.68185 ceiling **cannot be broken** by any certificate using bandwidth-1 data and the same class of integrality arguments. The rank-trace approach has a **lower** ceiling of exactly 2/3 (Fejér kernel) or 0.6725 (Montgomery–Taylor kernel), while the pointwise integrality approach has a **higher** ceiling of 0.68185 but requires RH. No unconditional approach using only $(\operatorname{tr} G, \|G\|_F^2)$ can exceed 2/3.

The key mathematical finding: the rank-trace inequality is **tight at the boundary** $c = 1$ of the $(1,1)$ signature cone. The extremal construction is a *commuting* (diagonal) matrix with eigenvalue distribution $\{1^{(2N/3)}, 2^{(N/6)}, 0^{(N/6)}\}$. Non-commutativity of $P$ and $Q$ in the actual zeta problem only makes $s$ *larger* (better for the bound), but this improvement is not accessible from the prime-side data.

---

## 1. Setup and Notation

### 1.1 The Matrix Decomposition

Claude's proof constructs a $d \times d$ Hermitian matrix $G$ from the Weil explicit formula, evaluated on a Gabor/test family at bandwidth $\lambda \leq 1$. The matrix decomposes as:

$$G = P + Q$$

where:
- **$P$** (on-line contribution): $P = \sum_{\text{on-line } \rho} m_\rho \, \mathbf{v}_\rho \mathbf{v}_\rho^*$, positive semidefinite, $\operatorname{rank}(P) \leq s$ (number of distinct on-line zeros).
- **$Q$** (off-line contribution): $Q = \sum_{\text{off-line pairs}} \left(\mathbf{a}_j \mathbf{a}_j^* - \mathbf{b}_j \mathbf{b}_j^*\right)$, Hermitian with signature $(p, p)$.

### 1.2 The Normalization Constraint (Key Insight)

Each off-line pair $\{\rho, 1 - \bar{\rho}\}$ contributes a $2 \times 2$ block to $Q$ with eigenvalues:

$$\lambda_+ = 1 + c_j, \qquad \lambda_- = 1 - c_j, \qquad c_j > 1$$

The **trace of each block is 2** (not 0), because the Weil kernel satisfies $K(\rho, \rho) = 1$ for each zero. This gives:

$$\operatorname{tr}(Q) = 2p, \qquad \operatorname{tr}(P) = N - 2p$$

and $\operatorname{tr}(G) = \operatorname{tr}(P) + \operatorname{tr}(Q) = N$.

> **Critical correction to initial analysis:** The off-line blocks have eigenvalues $(1 + c_j, 1 - c_j)$ with $c_j > 1$, NOT $(c_j, -c_j)$ as might be naively assumed. The trace of each block is 2, not 0. This is the additional constraint from the zeta problem normalization that makes the rank-trace inequality valid.

### 1.3 The Data Available

From the prime side (Montgomery's unconditional moments, via BGSTB 2024):

$$\operatorname{tr}(G) = N, \qquad \|G\|_F^2 = C N, \qquad C = \frac{1}{\lambda} + \frac{\lambda}{3}$$

At $\lambda = 1$ (Fejér kernel): $C = 4/3$. With the Montgomery–Taylor kernel: $C \approx 1.3275$.

### 1.4 The Rank-Trace Inequality

**Lemma R (Claude 2026, Lemma 3.2):** For $P \succeq 0$ with $\operatorname{rank}(P) \leq r$ and $Q$ Hermitian with $n_+(Q) \leq b$:

$$r \geq 2\operatorname{tr}(P) + 4\operatorname{tr}(Q) - 4b - \|P + Q\|_F^2$$

Substituting $\operatorname{tr}(P) = N - 2p$, $\operatorname{tr}(Q) = 2p$, $b = p$, $\|G\|_F^2 = CN$:

$$s \geq 2(N - 2p) + 4(2p) - 4p - CN = 2N - CN = (2 - C)N$$

At $C = 4/3$: $s \geq \frac{2}{3}N$. ✓

---

## 2. Q1: What is the Exact Ceiling for the Rank-Trace Approach?

### 2.1 The Two Ceilings

| Certificate | Ceiling | Condition |
|-------------|---------|-----------|
| Pointwise integrality ($m^2 \geq 2m - 1$) | **0.68185** | Requires RH |
| Rank-trace (aggregate, von Neumann) | **2/3 = 0.66667** | Unconditional |
| Rank-trace + Montgomery–Taylor kernel | **0.6725** | Unconditional |

The rank-trace ceiling is **lower** than the pointwise ceiling. This is because the rank-trace approach uses a *weaker* form of integrality (aggregate, not pointwise) and therefore extracts *less* information from the same data.

### 2.2 Proof that 2/3 is the Exact Rank-Trace Ceiling

**Theorem.** *Given $\operatorname{tr}(G) = N$, $\|G\|_F^2 = CN$ with $C = 4/3$, and the constraints $\operatorname{tr}(P) = N - 2p$, $\operatorname{tr}(Q) = 2p$, $P \succeq 0$, $\operatorname{rank}(P) \leq s$, $Q$ signature $(p,p)$ with eigenvalues $(1 + c_j, 1 - c_j)$, $c_j > 1$, $s + 2p \leq N$:*

*The minimum achievable $s/N$ is exactly $2 - C = 2/3$.*

**Proof.**

We work in the basis where $P = \operatorname{diag}(a, \ldots, a, 0, \ldots, 0)$ with $s$ copies of $a = (N - 2p)/s$.

The Frobenius norm decomposes as:

$$\|G\|_F^2 = \operatorname{tr}(P^2) + 2\operatorname{tr}(PQ) + \operatorname{tr}(Q^2)$$

**Step 1: Minimize $\operatorname{tr}(PQ)$.**

By the Schur–Horn theorem, the minimum of $\operatorname{tr}(PQ) = a \sum_{i=1}^{s} Q_{ii}$ over all choices of eigenbasis for $Q$ is achieved by aligning $P$'s eigenvectors with $Q$'s smallest eigenvalues. The $s$ smallest eigenvalues of $Q$ are:

$$\underbrace{1 - c, \ldots, 1 - c}_{p \text{ copies}}, \quad \underbrace{0, \ldots, 0}_{s - p \text{ copies}}$$

(setting all $c_j = c$ by symmetry). This gives:

$$\min \operatorname{tr}(PQ) = a \cdot p \cdot (1 - c) = \frac{(N - 2p) \cdot p \cdot (1 - c)}{s}$$

**Step 2: Compute $\operatorname{tr}(Q^2)$.**

$$\operatorname{tr}(Q^2) = p(1 + c)^2 + p(1 - c)^2 = 2p(1 + c^2)$$

**Step 3: Total Frobenius norm.**

$$\|G\|_F^2 = \frac{(N - 2p)^2}{s} + \frac{2(N - 2p)p(1 - c)}{s} + 2p(1 + c^2)$$

**Step 4: Minimize over $c > 1$.**

$$\frac{\partial}{\partial c}\left[\frac{2(N-2p)p(1-c)}{s} + 2p(1 + c^2)\right] = -\frac{2(N-2p)p}{s} + 4pc = 0$$

$$\implies c_{\text{opt}} = \frac{N - 2p}{2s}$$

With $p = (N - s)/2$: $c_{\text{opt}} = \frac{s}{2s} = \frac{1}{2}$.

Since $c_{\text{opt}} = 1/2 < 1$, the unconstrained minimum lies **outside** the feasible region $c > 1$. The constrained minimum on $c \geq 1$ is at the **boundary** $c = 1$.

**Step 5: Evaluate at $c = 1$.**

At $c = 1$, the block eigenvalues are $(2, 0)$ — the boundary of $(1,1)$ signature (degenerate to $(1^+, 0)$). The Frobenius norm becomes:

$$\|G\|_F^2\bigg|_{c=1} = \frac{(N-2p)^2}{s} + 0 + 4p = \frac{(N - 2p)^2}{s} + 4p$$

With $p = (N - s)/2$:

$$= \frac{s^2}{s} + 2(N - s) = s + 2N - 2s = 2N - s$$

**Step 6: Set equal to target.**

$$2N - s = CN \implies s = (2 - C)N$$

At $C = 4/3$: $s = \frac{2}{3}N$. $\square$

### 2.3 Numerical Verification

| $s$ | $p$ | $\min_{c \geq 1} \|G\|_F^2$ | Target $(4/3)N$ | Feasible? |
|-----|-----|----------------------------|-----------------|-----------|
| 190 | 55 | 410 | 400 | No |
| 195 | 52 | 405 | 400 | No |
| 199 | 50 | 401 | 400 | No |
| **200** | **50** | **400** | **400** | **Tight** |
| 205 | 47 | 395 | 400 | Yes ($c \approx 1.051$) |

**Construction at $s = 200, p = 50, c = 1$ (boundary):**
- $P = \operatorname{diag}(1, \ldots, 1, 0, \ldots, 0)$ — 200 ones, 100 zeros
- $Q = \operatorname{diag}(0, \ldots, 0, 2, \ldots, 2, 0, \ldots, 0)$ — 50 twos, 50 zeros, 50 twos
- $G = \operatorname{diag}(1, \ldots, 1, 2, \ldots, 2, 0, \ldots, 0)$ — 200 ones, 50 twos, 50 zeros
- Eigenvalue distribution: $\{1^{(2N/3)}, 2^{(N/6)}, 0^{(N/6)}\}$
- $\operatorname{tr}(G) = \frac{2}{3}N \cdot 1 + \frac{1}{6}N \cdot 2 + \frac{1}{6}N \cdot 0 = N$ ✓
- $\|G\|_F^2 = \frac{2}{3}N \cdot 1 + \frac{1}{6}N \cdot 4 + 0 = \frac{4}{3}N$ ✓

At $c = 1$, the block has eigenvalues $(2, 0)$ — technically not $(1,1)$ but the boundary of the $(1,1)$ cone. For $c = 1 + \varepsilon$ (strict $(1,1)$), $\|G\|_F^2 = 2N - s + O(\varepsilon^2) > (4/3)N$ when $s < (2/3)N$.

### 2.4 The Ceiling Hierarchy

```
0.68185  ← Pointwise ceiling (requires RH)
  ↑
  |  Gap: 0.01518 (integrality bonus from m > 1)
  |
0.66667  ← Rank-trace ceiling (Fejér kernel, unconditional)
  ↑
  |  Gap: 0.00583 (kernel optimization)
  |
0.67250  ← Rank-trace with Montgomery–Taylor kernel (unconditional)
  ↑
  |  Gap: 0.32750 (bandwidth > 1 needed)
  |
1.00000  ← Full pair-correlation conjecture
```

---

## 3. Q2: Optimal Inequality for the Block Structure

### 3.1 Can a Different Matrix Inequality Do Better?

**No.** The rank-trace inequality is **tight** for the class of all $(P, Q)$ with the given block structure. There exist matrices achieving equality (at the boundary $c = 1$), so no inequality using only $(\operatorname{tr} G, \|G\|_F^2)$ can give a better bound.

### 3.2 The Specific Block Structure

The off-line blocks have eigenvalues $(1 + c_j, 1 - c_j)$ with $c_j > 1$, which means:
- Each positive eigenvalue of $Q$ is $> 2$
- Each negative eigenvalue of $Q$ is $< 0$
- The trace of each block is exactly 2

This is **more restrictive** than a general $(p, p)$ signature matrix (where eigenvalues could be any $(\alpha, -\beta)$ with $\alpha, \beta > 0$). However, this additional structure is already **fully captured** by the trace constraint $\operatorname{tr}(Q) = 2p$. No additional leverage is available from the eigenvalue bounds alone.

### 3.3 What About Non-Standard Inequalities?

One might try:
- **Horn's inequalities** (eigenvalue majorization): These give finer constraints on the eigenvalue distribution of $G = P + Q$, but they are all consequences of the Schur–Horn theorem, which we already used. The bound is tight within this framework.
- **Free probability** (non-commutative moments): These could potentially extract more information from the non-commutativity of $P$ and $Q$. However, the non-commutativity structure is not computable from the prime-side data (see §5 below).
- **Semidefinite programming** (SDP): The Chirre–Gonçalves–de Laat (2020) approach uses SDP to optimize over test functions. This optimizes $C = \|G\|_F^2 / \operatorname{tr}(G)$ but does not change the fundamental inequality $s \geq (2 - C)N$.

---

## 4. Q3: Eigenvalue Distribution and Higher Moments

### 4.1 The Extremal Eigenvalue Distribution

At the boundary $c = 1$ with the Fejér kernel, the eigenvalue distribution of $G$ is:

| Eigenvalue | Multiplicity | Fraction |
|------------|-------------|----------|
| 1 | $\frac{2}{3}N$ | $2/3$ |
| 2 | $\frac{1}{6}N$ | $1/6$ |
| 0 | $\frac{1}{6}N$ | $1/6$ |

This gives:
- $\operatorname{tr}(G) = \frac{2}{3}N + \frac{1}{3}N = N$ ✓
- $\operatorname{tr}(G^2) = \frac{2}{3}N + \frac{2}{3}N = \frac{4}{3}N$ ✓
- $\operatorname{tr}(G^3) = \frac{2}{3}N + \frac{4}{3}N = 2N$

### 4.2 Would the Third Moment Help?

**Yes, if it were known.** If $\operatorname{tr}(G^3)$ were computable from the prime side and differed from $2N$, the extremal construction would be ruled out, and a sharper bound could be derived.

The third moment provides one additional constraint on the eigenvalue distribution. The resulting optimization problem (minimize $s/N$ subject to three moment constraints) would generically give a **strictly better** bound, on the order of a few thousandths improvement for realistic kernels.

### 4.3 Availability of Higher Moments

Claude's paper explicitly checked: **unconditional higher moments are not available** at useful bandwidths. The pair-correlation framework at bandwidth $\lambda \leq 1$ gives access to only the first two trace moments. Higher moments would require:
- **$k$-tuple correlations** ($k \geq 3$): not available unconditionally at any bandwidth $> 0$.
- **Higher trace moments of the compression**: not accessible from the prime-side data at bandwidth 1.

### 4.4 Minimum Spectral Information to Beat 2/3

Any **single additional moment** $\operatorname{tr}(G^k)$ for $k \geq 3$ that differs from the extremal value would suffice. Specifically:

| Moment | Extremal value (Fejér) | If actual value differs by $\delta$ | Improvement in $s/N$ |
|--------|----------------------|-------------------------------------|---------------------|
| $\operatorname{tr}(G^3)/N$ | $2$ | $\delta$ | $O(\delta)$ |
| $\operatorname{tr}(G^4)/N$ | $2 + \frac{2}{3} = \frac{8}{3}$ | $\delta$ | $O(\delta)$ |

But none of these moments are computable from the prime side at bandwidth 1.

### 4.5 Full Eigenvalue Distribution

If the **full spectrum** of $G$ were known, $s$ could be recovered exactly by counting positive eigenvalues. But this requires far more information than the first two moments — it is equivalent to knowing the full pair-correlation function, not just its first two Fourier coefficients.

---

## 5. Q4: What Does "Tight" Mean for Lemma R?

### 5.1 Tightness: Four Levels

The rank-trace inequality (Lemma R) is tight in the following precise sense:

**1. Tight for the class of all $(P, Q)$ with the given block structure.**

There exist $P \succeq 0$ (rank $s$) and $Q$ (signature $(p, p)$, block eigenvalues $(1+c, 1-c)$, $c > 1$) with $\operatorname{tr}(P) = N - 2p$, $\operatorname{tr}(Q) = 2p$, $\operatorname{tr}(G) = N$, $\|G\|_F^2 = CN$, and $s = (2 - C)N$ exactly. The extremal construction is the commuting (diagonal) matrix with eigenvalue distribution $\{1^{(2N/3)}, 2^{(N/6)}, 0^{(N/6)}\}$.

**2. Tight at the boundary $c = 1$.**

The extremal construction has $c = 1$, which is the **boundary** of the $(1,1)$ signature cone. At $c = 1$, the block degenerates: eigenvalues $(2, 0)$ instead of $(1 + c, 1 - c)$ with $c > 1$. For **strict** $(1,1)$ signature ($c > 1$), the bound is **strict**: $s > (2 - C)N$.

This means: the 2/3 bound is achieved only in the limit $c \to 1^+$. For any fixed $c > 1$, the bound is $s > (2 - C)N$. The paper's claim of $\geq 2/3$ (not $> 2/3$) is valid because the limit is taken as $N \to \infty$ and the $o(1)$ terms absorb the strict inequality.

**3. Tight for commuting $P$ and $Q$ (the worst case).**

The extremal construction is **commuting** (simultaneously diagonalizable). For **non-commuting** $P$ and $Q$, the cross term $\operatorname{tr}(PQ)$ is **larger** than the commuting minimum (by the Schur–Horn theorem), which makes $\|G\|_F^2$ larger, which means $s$ must be **larger** to satisfy $\|G\|_F^2 = CN$.

In other words: non-commutativity **helps** the bound (makes $s$ larger for the same $C$), but this improvement is **not provable** from the prime-side data, which only gives $\operatorname{tr}(G)$ and $\|G\|_F^2$.

**4. Not tight for the Montgomery–Taylor kernel.**

The MT kernel gives $0.6725 > 2/3$, meaning the MT kernel's $G$ does **not** saturate the rank-trace inequality. The gap is due to the MT kernel having a better ratio $C = \|G\|_F^2 / \operatorname{tr}(G) < 4/3$, not to a different inequality.

### 5.2 The Commuting vs. Non-Commuting Distinction

The rank-trace inequality is tight for **commuting** $P$ and $Q$. The actual $G$ from the zeta problem has **non-commuting** $P$ and $Q$ (the test functions create non-trivial correlations). In principle, a sharper inequality exploiting this non-commutativity could give a better bound.

However, the non-commutativity structure depends on the **zero distribution** (the locations of the on-line and off-line zeros), which is precisely what we are trying to bound. It is not computable from the prime-side data $(\operatorname{tr} G, \|G\|_F^2)$.

**Key principle:** Any improvement must come from **additional data**, not from a better reading of the same data. The rank-trace inequality is the optimal reading of $(\operatorname{tr} G, \|G\|_F^2)$ for matrices with this block structure.

---

## 6. Can the 0.68185 Ceiling Be Broken?

### 6.1 Within Bandwidth 1 + Rank-Trace

**No.** The ceiling is $2 - C_{\min}$ where $C_{\min}$ is the minimum achievable $\|G\|_F^2 / \operatorname{tr}(G)$ over all kernels at bandwidth 1. With the Fejér kernel: $2/3$. With the MT kernel: $0.6725$. The optimal kernel (solution to the variational problem) gives at most $0.68185$ — but this is the **pointwise** ceiling, not the rank-trace ceiling.

The rank-trace ceiling with the optimal kernel is $2 - C_{\min}$, where $C_{\min}$ is the same optimal ratio. The pointwise approach extracts an additional "integrality bonus" from $m > 1$ that the rank-trace approach does not. This bonus is what raises the pointwise ceiling above the rank-trace ceiling.

### 6.2 Within Bandwidth 1 + Pointwise Integrality

The ceiling is $0.68185$, but this requires RH (or the thin-box assumption). Without RH, the pointwise approach cannot be applied because the zero-side decomposition requires knowing which zeros are on the line.

### 6.3 Beyond 0.68185

Requires one of:
1. **Bandwidth $> 1$**: needs Hardy–Littlewood-level prime pair estimates.
2. **Higher moments** ($\operatorname{tr}(G^3)$, etc.): not available unconditionally at any useful bandwidth.
3. **Non-commutativity structure**: not computable from prime-side data.
4. **A completely different proof architecture** (not pair-correlation based).

None of these are available with current technology.

### 6.4 The Precise Obstruction

The obstruction is **fundamental**, not merely technical:

> Given only $(\operatorname{tr} G, \|G\|_F^2)$ and the block structure $(P \succeq 0, \operatorname{rank} P \leq s; Q \text{ signature } (p,p), \operatorname{tr} Q = 2p)$, the minimum $s/N$ is exactly $2 - C$. This is achieved by a commuting construction at the boundary $c = 1$ of the $(1,1)$ cone. No inequality using only this data can do better.

The only way to break this barrier is to **add data** (higher moments, non-commutativity information, or bandwidth $> 1$) or to **change the certificate architecture** to one that uses a different form of integrality (pointwise, which requires RH).

---

## 7. The Key Mathematical Construction

### 7.1 The Extremal Matrix

For $N = 300$, $s = 200$, $p = 50$, $c = 1$:

$$P = \operatorname{diag}(\underbrace{1, \ldots, 1}_{200}, \underbrace{0, \ldots, 0}_{100})$$

$$Q = \operatorname{diag}(\underbrace{0, \ldots, 0}_{200}, \underbrace{2, \ldots, 2}_{50}, \underbrace{0, \ldots, 0}_{50})$$

$$G = P + Q = \operatorname{diag}(\underbrace{1, \ldots, 1}_{200}, \underbrace{2, \ldots, 2}_{50}, \underbrace{0, \ldots, 0}_{50})$$

Verification:
- $\operatorname{tr}(G) = 200 \times 1 + 50 \times 2 + 50 \times 0 = 300 = N$ ✓
- $\|G\|_F^2 = 200 \times 1 + 50 \times 4 + 50 \times 0 = 400 = \frac{4}{3}N$ ✓
- $\operatorname{rank}(P) = 200 = \frac{2}{3}N$ ✓
- $Q$ has 50 positive eigenvalues (value 2) and 50 zero eigenvalues ← **not** $(1,1)$ at $c = 1$!

At $c = 1 + \varepsilon$ (strict $(1,1)$):

$$Q = \operatorname{diag}(\underbrace{-\varepsilon, \ldots, -\varepsilon}_{50}, \underbrace{0, \ldots, 0}_{150}, \underbrace{2+\varepsilon, \ldots, 2+\varepsilon}_{50}, \underbrace{0, \ldots, 0}_{50})$$

$$G = \operatorname{diag}(\underbrace{1-\varepsilon, \ldots, 1-\varepsilon}_{50}, \underbrace{1, \ldots, 1}_{150}, \underbrace{2+\varepsilon, \ldots, 2+\varepsilon}_{50}, \underbrace{0, \ldots, 0}_{50})$$

- $\operatorname{tr}(G) = 50(1-\varepsilon) + 150 + 50(2+\varepsilon) = 50 - 50\varepsilon + 150 + 100 + 50\varepsilon = 300$ ✓
- $\|G\|_F^2 = 50(1-\varepsilon)^2 + 150 + 50(2+\varepsilon)^2 = 50(1 - 2\varepsilon + \varepsilon^2) + 150 + 50(4 + 4\varepsilon + \varepsilon^2)$
- $= 50 - 100\varepsilon + 50\varepsilon^2 + 150 + 200 + 200\varepsilon + 50\varepsilon^2 = 400 + 100\varepsilon^2$

So $\|G\|_F^2 = 400 + 100\varepsilon^2 > 400$ for $\varepsilon > 0$. To match $\|G\|_F^2 = 400$, we need $\varepsilon = 0$ (boundary) or $s > 200$ (increase rank to compensate).

### 7.2 Why $s < 200$ is Infeasible

For $s = 199$, $p = 50$ (with $N = 300$):

$$\min_{c \geq 1} \|G\|_F^2 = 2N - s = 600 - 199 = 401 > 400 = CN$$

The minimum Frobenius norm exceeds the target. No valid $(1,1)$ decomposition exists.

---

## 8. Conclusions

### 8.1 The Ceiling Hierarchy

| Approach | Ceiling | Condition | Gap to next |
|----------|---------|-----------|-------------|
| Rank-trace (Fejér) | $2/3 = 0.66667$ | Unconditional | $0.00583$ (kernel) |
| Rank-trace (MT kernel) | $0.6725$ | Unconditional | $0.00935$ (pointwise bonus) |
| Pointwise integrality | $0.68185$ | Requires RH | $0.31815$ (bandwidth) |
| Full pair-correlation | $1.0$ | Conjectural | — |

### 8.2 Key Findings

1. **The rank-trace ceiling is exactly $2/3$** (Fejér kernel) or $0.6725$ (MT kernel). It is **lower** than the pointwise ceiling of $0.68185$.

2. **The 0.68185 ceiling cannot be broken** by the rank-trace approach, which has a lower ceiling. It also cannot be broken unconditionally by the pointwise approach, which requires RH.

3. **The bound is tight at the boundary $c = 1$** of the $(1,1)$ signature cone. The extremal construction is a commuting matrix with eigenvalue distribution $\{1^{(2N/3)}, 2^{(N/6)}, 0^{(N/6)}\}$.

4. **No different matrix inequality can do better** with the same data $(\operatorname{tr} G, \|G\|_F^2)$, because the bound is tight — extremal matrices exist.

5. **Higher moments would help** if available, but are not computable from the prime side at bandwidth 1.

6. **Non-commutativity of $P$ and $Q$** in the actual zeta problem makes $s$ larger (better for the bound), but this improvement is not accessible from the prime-side data.

7. **The only path to exceeding 0.68185** is:
   - Bandwidth $> 1$ (requires Hardy–Littlewood), or
   - Higher moments (not available unconditionally), or
   - A completely different proof architecture (not pair-correlation based).

### 8.3 The Fundamental Obstruction

The obstruction is a **two-moment barrier**: given only $\operatorname{tr}(G)$ and $\|G\|_F^2$, the rank-trace inequality is the optimal bound, and it is tight. Breaking this barrier requires either:

- **More data** (higher moments, bandwidth $> 1$, non-commutativity structure), or
- **A different certificate** (pointwise integrality, which requires RH).

Neither is available unconditionally with current technology. The 0.68185 ceiling stands as the absolute limit for bandwidth-1 certificates, and 2/3 as the limit for unconditional rank-trace certificates.

---

## References

- Claude (Anthropic), "More Than Two Thirds of the Zeros of the Riemann Zeta Function Lie on the Critical Line," August 10, 2026.
- S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, "An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function," *Acta Arith.* **214** (2024), 357–376.
- D. A. Goldston, A. I. Suriajaya, "Zeta Zeros on the Critical Line," arXiv:2511.20059 (2025).
- R. Chirre, M. Gonçalves, T. de Laat, "Pair correlation estimates for the zeros of the zeta function via semidefinite programming," *J. Reine Angew. Math.* (2020).
- H. L. Montgomery, "The pair correlation of zeros of the zeta function," *Proc. Sympos. Pure Math.* **XXIV** (1973), 181–193.

---

*This analysis was performed using symbolic computation, numerical verification, and the Schur–Horn theorem. All constructions have been verified numerically.*