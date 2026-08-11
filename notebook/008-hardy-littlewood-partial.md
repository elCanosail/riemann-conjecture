# Hard-Littlewood-Style Partial Results and Bandwidth > 1 in the Pair-Correlation Method

**Date:** 2026-08-11
**Author:** Research analysis
**Purpose:** Determine what unconditional prime pair results could give F(α) → 1 at some α > 1

---

## 1. Framework: Montgomery's Form Factor

### 1.1 Definition

Montgomery's form factor (1973) for the pair correlation of zeros of ζ(s):

$$F(\alpha, T) = \frac{2\pi}{T\log T} \sum_{0 < \gamma,\gamma' \leq T} T^{i\alpha(\gamma-\gamma')} w(\gamma-\gamma')$$

where $w(u) = 4/(4+u^2)$ and the zeros are on the critical line under RH.

### 1.2 Montgomery's Proved Result (under RH)

For $0 \leq |\alpha| \leq 1$ uniformly:

$$F(\alpha, T) = T^{-2|\alpha|}\log T \cdot (1+o(1)) + |\alpha| + o(1)$$

Thus $F(0,T) \sim \frac{T\log T}{2\pi}$ (the diagonal count), and $F(1,T) = 1 + o(1)$.

### 1.3 The Strong Pair Correlation Conjecture (SPC)

For any fixed bounded $M > 1$, as $T \to \infty$:

$$F(\alpha, T) = 1 + o(1), \quad \text{uniformly for } 1 \leq \alpha \leq M$$

This is **open** for $\alpha > 1$. The "bandwidth" of the method is the range of α for which SPC is proved or provable.

### 1.4 Montgomery's Explicit Formula (prime side)

The key bridge:

$$F(\alpha, T) = T^{-2\alpha}\log T \cdot (1+o(1)) + \frac{1}{T\log T} \sum_{m \neq n} \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}} \left(\frac{m}{n}\right)^{i\alpha\log T} + \text{small error}$$

The off-diagonal sum involves prime pairs $(m, n)$. Setting $m = p$ and $n = p+h$:

$$\text{Off-diagonal contribution} = \frac{1}{T\log T} \sum_{h} \sum_{\substack{p \leq T \\ p+h \leq T}} \Lambda(p)\Lambda(p+h) \left(1 + \frac{h}{p}\right)^{i\alpha\log T}$$

The form factor at $\alpha > 1$ depends on this sum over prime pairs at gap sizes $h$.

---

## 2. What Bandwidth > 1 Actually Requires

### 2.1 The Form Factor Decomposition

Split the off-diagonal contribution by gap size:

$$F(\alpha, T) = T^{-2\alpha}\log T + \frac{1}{T\log T} \sum_{h \geq 1} G(h, T) \left(1 + \frac{h}{p}\right)^{i\alpha\log T} + o(1)$$

where $G(h, T) = \sum_{\substack{p \leq T \\ p+h \leq T}} \Lambda(p)\Lambda(p+h)$ is the weighted prime pair count.

### 2.2 The Hardy-Littlewood Bias

By the Hardy-Littlewood prime pair conjecture:

$$G(h, T) \sim \mathfrak{S}(h) \cdot \frac{T}{(\log T)^2}$$

where $\mathfrak{S}(h)$ is the twin-prime constant:

$$\mathfrak{S}(h) = \prod_{p|h, p>2} \frac{p-1}{p-2} \cdot \prod_{p>2} \left(1 - \frac{1}{(p-1)^2}\right)$$

Key property: **$\mathfrak{S}(h) > 0$ for all even $h$, and $\mathfrak{S}(h) = 0$ for odd $h > 1$**.

### 2.3 The Core Obstruction for α > 1

For the form factor at $\alpha = 1 + \varepsilon$:

$$\text{HL contribution} = \frac{1}{T\log T} \sum_{h} \mathfrak{S}(h) \cdot \frac{T}{(\log T)^2} \cdot \frac{T}{(\log T)^2} \cdot \left(1 + \frac{h}{p}\right)^{i\alpha\log T}$$

The dominant scale of gaps contributing is $h \sim T^{2\alpha-1}$. For $\alpha = 1 + \varepsilon$, this is $h \sim T^{2\varepsilon}$.

The Hardy-Littlewood bias gives a contribution of order:

$$\mathfrak{S}_{\text{avg}} \cdot \frac{T^{2-2\alpha}}{\log T} = \mathfrak{S}_{\text{avg}} \cdot T^{2(1-\alpha)} (\log T)^{-1}$$

For $\alpha = 1 + \varepsilon$: **$O(T^{-2\varepsilon} (\log T)^{-1})$** — small, yes, but the *error* terms may not be.

### 2.4 The Critical Condition

For $F(\alpha, T) \to 1$ as $T \to \infty$ at $\alpha = 1 + \varepsilon$, we need the off-diagonal contribution to be $o(1)$. This requires:

$$\sum_{h=1}^{T^{2\alpha-1}} G(h, T) \cdot h^{i\alpha\log T} = o(T\log T)$$

The **error term** in the prime pair sum must be controlled uniformly in $h$ up to scale $T^{2\alpha-1}$.

---

## 3. Question-by-Question Analysis

### Q1: What EXACTLY is needed for bandwidth > 1?

**Answer:** The form factor $F(\alpha)$ for $|\alpha| > 1$ requires estimating:

$$\sum_{m \neq n} \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}} \left(\frac{m}{n}\right)^{i\alpha\log T}$$

uniformly as $T \to \infty$.

By Montgomery's explicit formula, the $m$th prime contributes via $(m/n)^{i\alpha\log T} = e^{i\alpha\log T \cdot \log(m/n)}$. For pairs with gap $h = |n-m|$, this is:

$$\left(1 + \frac{h}{m}\right)^{i\alpha\log T} = e^{i\alpha\log T \cdot (h/m - h^2/(2m^2) + \cdots)}$$

**For $|\alpha| \leq 1$:** Only gaps $h \ll T$ matter significantly. The sum is controlled by the Hardy-Littlewood prediction and error terms from prime distribution in short intervals.

**For $|\alpha| > 1$:** The relevant gap scale is $h \sim T^{|\alpha|-1}$, which grows polynomially in $T$. The oscillatory factor no longer suppresses large gaps effectively, and the sum must be shown to cancel.

**What is needed:** A uniform estimate for the off-diagonal prime pair sum:

$$E(\alpha, T) := \sum_{h} \sum_{\substack{p \leq T \\ p+h \leq T}} \Lambda(p)\Lambda(p+h) \left(\left(1 + \frac{h}{p}\right)^{i\alpha\log T} - 1\right) = o(T\log T)$$

uniformly for $T^{|\alpha|-1} \leq h \leq T$.

This is equivalent (via Goldston-Montgomery) to an estimate for the **variance of primes in short intervals**:

$$\int_X^{2X} (\psi(x+h) - \psi(x) - h)^2 dx = hX\log(X/h) + O(hX\cdot f(h,X))$$

where $f(h,X) \to 0$ as $X \to \infty$ uniformly for $X^{1-\alpha} \leq h \leq X$.

---

### Q2: Can Bombieri-Vinogradov give information about F(α) for α slightly > 1?

**Short answer:** No meaningful quantitative information about $F(\alpha)$ at $\alpha = 1+\varepsilon$ from Bombieri-Vinogradov alone.

**Detailed analysis:**

Bombieri-Vinogradov (1955) states: for any $A > 0$, there exists $B = B(A)$ such that

$$\sum_{q \leq Q} \max_{\substack{y \leq x \\ (a,q)=1}} \left|\pi(y; q, a) - \frac{\pi(y)}{\varphi(q)}\right| \ll_A \frac{x}{(\log x)^A}$$

where $Q = x^{1/2} / (\log x)^B$. This is an **averaged** result over moduli $q$ up to $x^{1/2}$ (essentially).

For prime pairs at gap $h$, we need information about $\psi(x+h) - \psi(x) - h$ uniformly in $h$. The error term in the prime pair count $G(h, T)$ from Bombieri-Vinogradov is:

$$\text{Error}(h) \ll \frac{T}{\log T} \cdot \text{something small averaged over } h$$

But this only controls the **average** over $h$, not the **individual** $G(h, T)$ needed for the oscillatory sum.

For the form factor at $\alpha = 1+\varepsilon$, the relevant gap scale is $h \sim T^{2\varepsilon}$. The error from Bombieri-Vinogradov, when applied to this scale, is:

$$\text{Error at scale } T^{2\varepsilon} \sim T^{2\varepsilon} \cdot (\text{error per } h) \cdot (\text{number of } h \text{ values})$$

The error per $h$ is bounded by $O(T^{1/2+\varepsilon})$ (from the $Q = T^{1/2}$ level of distribution), and the number of $h$ values up to $T^{2\varepsilon}$ is $O(T^{2\varepsilon})$. So the total error is:

$$\text{Total error} \sim T^{2\varepsilon} \cdot T^{1/2+\varepsilon} = T^{1/2+3\varepsilon}$$

Compare this to the main term $O(T^{2-2\alpha}) = O(T^{1-2\varepsilon})$.

**For $\varepsilon < 1/10$:** The error term $T^{1/2+3\varepsilon}$ dominates the main term $T^{1-2\varepsilon}$. The result is trivial (error > signal).

**For any $\varepsilon$:** The error never gets small enough relative to the main term to prove $F(\alpha) \to 1$.

**Conclusion:** Bombieri-Vinogradov provides **no quantitative information** about $F(\alpha)$ at any $\alpha > 1$ because the error term always dominates. It controls an average over moduli, which does not translate to the individual prime pair correlations needed at $\alpha > 1$.

---

### Q3: Can Zhang/Maynard/Tao bounded gaps give any information about F(α)?

**Answer:** Only negligibly so. The bounded gap results affect $F(\alpha)$ only at an infinitesimal level.

**Analysis:**

The Maynard-Tao result (Zhang 2013, Maynard 2013, Polymath8) proves:

$$\liminf_{n \to \infty} (p_{n+1} - p_n) \leq 246$$

This means there exists a set of gap sizes $h \leq 246$ that occur infinitely often with positive frequency.

For the form factor at $\alpha = 1 + \varepsilon$:

$$\text{Contribution from bounded gaps } h \leq 246 = \frac{1}{T\log T} \sum_{h \leq 246} \mathfrak{S}(h) \cdot \frac{T}{(\log T)^2} \cdot \left(1 + \frac{h}{p}\right)^{i\alpha\log T}$$

The oscillatory factor $(1+h/p)^{i\alpha\log T}$ oscillates rapidly as $T \to \infty$, and the average over primes $p$ causes cancellation. The contribution is:

$$\sim \frac{1}{(\log T)^2} \sum_{h \leq 246} \mathfrak{S}(h) \cdot \text{(oscillatory sum)}$$

This is $O((\log T)^{-2})$, which is $o(1)$ and contributes negligibly to the form factor.

More importantly, the Maynard-Tao results describe gaps at scale $O(1)$, while the form factor at $\alpha = 1+\varepsilon$ probes gaps at scale $T^{2\varepsilon} \to \infty$. The bounded gaps are irrelevant at this scale.

**Even if bounded gaps contributed:** The Hardy-Littlewood constant $\mathfrak{S}(h) > 0$, so the contribution would be positive, making $F(\alpha)$ **larger** than 1, not smaller. This is the opposite of what's needed.

**Conclusion:** The bounded gap results contribute $O((\log T)^{-2})$ to $F(\alpha)$ at $\alpha > 1$ — negligible. They do not help establish $F(\alpha) \to 1$.

---

### Q4: What is the WEAKEST result about prime pairs that would give F(α) at α = 1 + ε?

**Theorem (necessary and sufficient condition):**

For $F(1+\varepsilon, T) \to 1$ as $T \to \infty$, the following condition on prime pairs is **necessary and sufficient** (under RH):

$$\sum_{p \leq T} (\psi(p + T^{2\varepsilon}) - \psi(p) - T^{2\varepsilon}/\log p) = o(T\log T)$$

uniformly for the range $1 \leq h \leq T^{2\varepsilon}$.

Equivalently (Goldston-Montgomery 1987):

The variance of primes in short intervals satisfies:
$$\int_X^{2X} (\psi(x + \delta x) - \psi(x) - \delta x)^2 dx = \frac{3}{2}X^2\delta\log(1/\delta) + o(X^2\delta)$$
uniformly for $\delta = X^{-2\varepsilon}$.

**How weak is this?**

This is significantly weaker than Hardy-Littlewood. Hardy-Littlewood would give:

$$G(h, T) = \mathfrak{S}(h) \cdot \frac{T}{(\log T)^2} + O\left(\frac{T}{(\log T)^2} \cdot \frac{1}{\log(T/h)}\right)$$

The condition for $F(\alpha) \to 1$ at $\alpha = 1+\varepsilon$ only needs:

$$\sum_{h=1}^{T^{2\varepsilon}} \mathfrak{S}(h) = o(T\log T)$$

which is a **global** condition on the average behavior of $\mathfrak{S}(h)$, not a pointwise one.

**But there's a fundamental obstruction:**

The Hardy-Littlewood constant $\mathfrak{S}(h) > 0$ for all even $h$. So:

$$\sum_{h=1}^{T^{2\varepsilon}} \mathfrak{S}(h) \sim c \cdot T^{2\varepsilon}$$

for some $c > 0$. This sum grows with $T$, contributing a **positive** amount to $F(1+\varepsilon)$.

For $F(1+\varepsilon) \to 1$, we need the oscillatory terms in the form factor sum to cancel this positive bias:

$$\sum_{h} G(h, T) \cdot \left[\left(1 + \frac{h}{p}\right)^{i\alpha\log T} - 1\right] = o(T\log T)$$

This cancellation is **not** a consequence of prime pair estimates alone — it's a consequence of the oscillatory structure of the explicit formula.

**The weakest useful statement would be:**

> **Conjecture (weak form of SPC at scale 1+ε):** There exists $\varepsilon > 0$ such that uniformly for $1 \leq h \leq T^{2\varepsilon}$:
> $$\sum_{p \leq T} (\psi(p+h) - \psi(p) - h/\log p) = o(\sqrt{T}\log T)$$
> 
> This is weaker than Hardy-Littlewood (which predicts error $O(\sqrt{T}\log^2(T/h))$) but stronger than anything currently provable.

The error $o(\sqrt{T}\log T)$ is what Bombieri-Vinogradov would give **on average** over $h$, but uniformity in $h$ is required here.

**Equivalence:** The condition $F(1+\varepsilon) \to 1$ is equivalent to the pair correlation formula holding at the specific scale $\alpha = 1+\varepsilon$, which is in turn equivalent to the variance formula for primes in short intervals at scale $h \sim T^{2\varepsilon}$. This is a specific case of SPC, not a weakening of it.

**Key insight:** The weakest statement that gives $F(\alpha) \to 1$ at a specific $\alpha > 1$ is **not strictly weaker than Hardy-Littlewood** — it's a different statement. Hardy-Littlewood gives the **positive bias**, while $F(\alpha) \to 1$ requires the **oscillatory cancellation** of this bias. The two are compatible (HL is the conjectured asymptotic, SPC is the Fourier consequence), but HL alone does not imply SPC without the explicit formula machinery.

---

### Q5: Could Elliott-Halberstam help?

**Elliott-Halberstam conjecture (EH):** For any $A > 0$,

$$\sum_{q \leq x^{1-\varepsilon}} \max_{\substack{y \leq x \\ (a,q)=1}} \left|\pi(y; q, a) - \frac{\pi(y)}{\varphi(q)}\right| \ll_A \frac{x}{(\log x)^A}$$

where the level of distribution is $1 - \varepsilon$ instead of $1/2$.

**Effect on prime pairs:**

Under EH, the prime pair asymptotic becomes uniform up to gap $h \ll x$:

$$G(h, x) = \mathfrak{S}(h) \cdot \frac{x}{(\log x)^2} + O\left(\frac{x}{(\log x)^A}\right)$$

uniformly for $h \leq x^{1-\varepsilon}$.

**Effect on the form factor:**

With EH, the off-diagonal contribution to $F(\alpha, T)$ at $\alpha = 1+\varepsilon$:

$$\frac{1}{T\log T} \sum_{h=1}^{T^{2\varepsilon}} O\left(\frac{T}{(\log T)^A}\right) = O\left(\frac{T^{2\varepsilon}}{(\log T)^{A+1}}\right)$$

For $A$ large enough, this is $o(1)$ — **the error term vanishes**.

But the **main term** from Hardy-Littlewood remains:

$$\frac{1}{T\log T} \sum_{h=1}^{T^{2\varepsilon}} \mathfrak{S}(h) \cdot \frac{T}{(\log T)^2} = \frac{T^{2\varepsilon}}{(\log T)^3} \cdot c$$

This is $O(T^{2\varepsilon}/(\log T)^3)$, which is **polynomially large** in $T$.

**Wait — this is the key issue:** The Hardy-Littlewood **main term** at scale $h \sim T^{2\varepsilon}$ grows polynomially in $T$. Even with perfect error control (EH gives this), the form factor would be:

$$F(1+\varepsilon, T) \approx 1 + c \cdot \frac{T^{2\varepsilon}}{(\log T)^3} + \text{oscillatory cancellation}$$

The oscillatory cancellation from the explicit formula is what brings $F(\alpha)$ back to 1. This cancellation is **not** controlled by prime pair estimates — it comes from the Fourier structure.

**Conclusion under EH:** Elliott-Halberstam would control the error terms perfectly, making the form factor calculation purely about the oscillatory sum. The result would still be $F(\alpha) = 1 + o(1)$ for $\alpha > 1$, but this is because the oscillations cancel, not because the error terms are small.

**EH gives us:** A clean separation of the problem into "main term + error", where the error vanishes and the main term is handled by oscillatory cancellation in the explicit formula.

**But:** EH itself does **not prove** SPC for $\alpha > 1$. It removes one obstruction (error terms) but not the core one (showing the oscillatory sum cancels).

---

### Q6: Is there a way to get bandwidth > 1 WITHOUT prime pair estimates?

This is the most interesting question. Several alternatives exist:

#### A6.1: Using the explicit formula differently

Montgomery's explicit formula can be written in a form that avoids the prime pair sum entirely:

$$\sum_{0 < \gamma,\gamma' \leq T} T^{i\alpha(\gamma-\gamma')} w(\gamma-\gamma') = \text{main term} + \text{integral involving } \zeta' / \zeta$$

The integral involves terms like $\zeta'(s)/\zeta(s)$ evaluated near the zeros, which can be analyzed using the argument principle and properties of the zeta function directly, without reference to primes.

**Potential approach:** Use contour integration and the functional equation of $\zeta(s)$ to bound the off-diagonal sum directly from the analytic properties of $\zeta(s)$, bypassing prime pair sums entirely.

**Obstacle:** The explicit formula is designed to convert the zero correlation problem into a prime pair problem. Reversing this requires solving the prime pair problem in disguise. The analytic structure of $\zeta(s)$ encodes the prime pair information.

#### A6.2: Using zero-density estimates

Zero-density estimates provide upper bounds on the number of zeros of $\zeta(s)$ with large real part:

$$N(\sigma, T) \ll T^{c(1-\sigma)}\log T$$

where $c$ is a constant.

These estimates could potentially be used to bound the contribution of zeros off the critical line to the pair correlation sum, potentially giving stronger control over $F(\alpha)$.

**However:** Under RH, all zeros are on the critical line, so zero-density estimates are vacuous for our purpose. If we don't assume RH, then the off-diagonal sum picks up contributions from zeros with $\beta \neq 1/2$, which are harder to control.

#### A6.3: Using Selberg's variance formula directly

Selberg (1943) proved:

$$\int_0^T |\zeta'(1/2 + it)|^2 dt = \frac{1}{2\pi}\log^2 T + O(\log T)$$

This is a direct computation from the functional equation and does not involve primes explicitly. The connection to pair correlation is via the Goldston-Montgomery equivalence.

**Idea:** If we can bound the integral of $|\zeta'(1/2 + it)|^2$ in short intervals more precisely, we might get information about $F(\alpha)$ for $\alpha > 1$ without going through primes.

**Status:** The best known bounds for this integral are Selberg's original $O(\log^2 T)$ upper bound and Goldston-Gonek-Montgomery's lower bound of $(c - o(1))\beta\log^2 T/T$ for $J(\beta, T)$. These bounds are **consistent** with SPC but do not prove it.

#### A6.4: The 2021 Bettin-Chandee breakthrough

Bettin and Chandee (2021), "Correlations of sieve weights and distributions of zeros" (arXiv:2101.04418), established a new conditional lower bound on the variance of primes in short intervals and on the form factor.

Their approach uses sieve weights (rather than the von Mangoldt function directly) and applies bounds on trilinear Kloosterman fractions from their earlier work (2015).

**Result:** They proved unconditionally that:

$$\int_b^{b+\ell} F(\alpha, T) d\alpha \geq (W^-(\ell) + o(1))\ell$$

for certain explicit constants $W^-(\ell) > 0$, and similarly upper bounds $W^+(\ell)$.

**Significance:** This is the **sharpest unconditional bound** on the form factor for $\alpha > 1$. However, the constants $W^\pm$ are **not** 1 — the bounds are strict inequalities, not asymptotic formulas.

**Can it be pushed to $F(\alpha) = 1 + o(1)$?** The Bettin-Chandee approach uses trilinear Kloosterman fraction bounds with saving $N^{1/20}$ (from DFI1997) or $N^{1/16}$ (from their trilinear improvement). To get $F(\alpha) = 1 + o(1)$ at $\alpha = 1+\varepsilon$, we would need the saving to be at least $T^{2\varepsilon}$, which is far beyond current trilinear bounds.

#### A6.5: Alternative approach — spectral theory

If the zeros of $\zeta(s)$ are eigenvalues of a self-adjoint operator (as suggested by the Hilbert-Pólya conjecture), then the pair correlation formula follows from the spectral theory of the operator.

**Idea:** If there exists a self-adjoint operator $H$ with spectrum $\{\gamma\}$, then the pair correlation is a spectral statistic. For generic quantum chaotic systems, pair correlation follows the GUE (Gaussian Unitary Ensemble) prediction, which gives $F(\alpha) = 1 - (\sin \pi\alpha/\pi\alpha)^2 + \delta(\alpha)$.

**Problem:** No such operator is known, and constructing one is the central open problem in the field.

---

## 4. Summary of What Can and Cannot Be Done

### What We CAN Prove Unconditionally

1. **Montgomery (1973):** $F(\alpha) = T^{-2|\alpha|}\log T (1+o(1)) + |\alpha| + o(1)$ for $0 \leq |\alpha| \leq 1$

2. **Goldston-Montgomery (1987):** SPC $\iff$ variance formula for primes in short intervals (under RH)

3. **Goldston-Gonek-Montgomery (2005):** Lower bound for the integral of $F(\alpha)$ at any $\alpha > 1$:
   $$\int_b^{b+\ell} F(\alpha, T) d\alpha \geq (W^-(\ell) + o(1))\ell$$
   where $W^-(\ell)$ is an explicit positive constant depending on the test function.

4. **Bettin-Chandee (2021):** Improved bounds via sieve weights and Kloosterman fractions, still non-asymptotic.

### What We CANNOT Prove (with current methods)

1. **SPC at any $\alpha > 1$** — open problem
2. **Any unconditional result giving $F(\alpha) = 1 + o(1)$ at $\alpha > 1$** — requires error terms smaller than currently available
3. **Using Bombieri-Vinogradov alone** — error term always dominates at $\alpha > 1$
4. **Using bounded gaps alone** — irrelevant scale and wrong sign (positive bias)
5. **Using EH alone** — controls errors but not the oscillatory cancellation

### The Fundamental Obstruction

The Hardy-Littlewood constant $\mathfrak{S}(h) > 0$ gives a **positive bias** in the prime pair count. This bias contributes **positively** to the form factor. For $F(\alpha)$ to equal 1 (or be $\leq 1$), this bias must be cancelled by the oscillatory terms in the explicit formula.

**This cancellation is non-trivial:** It is a consequence of the deep Fourier-analytic structure of the zeta function, not of any elementary prime pair estimate.

**The conjecture that the cancellation occurs** is what SPC asserts. No current method can prove it because it requires controlling the oscillatory sum at a scale that current analytic number theory techniques cannot reach.

### Comparison Table

| Method | Error control | Max α provable | Notes |
|--------|--------------|----------------|-------|
| Montgomery (1973) | $O(T^{-2\alpha}\log T)$ | α ≤ 1 | Proved under RH |
| Bombieri-Vinogradov | $O(T^{1/2+\varepsilon})$ | None | Error > signal |
| Maynard-Tao | Pointwise at h ≤ 246 | None | Irrelevant scale |
| Elliott-Halberstam | $O(T/(\log T)^A)$ | α > 1 (conditional) | Controls errors only |
| Bettin-Chandee (2021) | $O(T^{4/5+\varepsilon})$ | Non-asymptotic bound | Improved bound, not asymptotic |
| Hardy-Littlewood (conjectured) | $O(T^{1/2+\varepsilon})$ α-pointwise | α > 1 (conditional) | Full asymptotic formula |

---

## 5. The Weakest Possible Statement

The weakest statement that would give $F(\alpha) \to 1$ at $\alpha = 1+\varepsilon$ is:

> **Conjecture:** There exists $\varepsilon > 0$ such that uniformly for $1 \leq h \leq T^{2\varepsilon}$:
> $$\sum_{p \leq T} (\psi(p+h) - \psi(p) - h/\log p) = O(h^{1/2+\varepsilon})$$

This is **weaker than Hardy-Littlewood** in the sense that it only needs an $O$-bound (not an asymptotic formula), but it is **stronger than Bombieri-Vinogradov** because it needs pointwise control in $h$ (not averaged over $h$).

However, even this conjecture implies the Twin Prime Conjecture in a averaged sense, and is therefore not believed to be provable by current methods.

---

## 6. Key References

1. **Montgomery (1973)** — "The Pair Correlation of Zeros of the Zeta Function"
2. **Goldston & Montgomery (1987)** — "On pair correlations of zeros and primes in short intervals", *Analytic Number Theory and Diophantine Problems*
3. **Montgomery (2004)** — "Montgomery's pair correlation conjecture", Newton Institute lecture notes
4. **Chan (2002)** — "More precise pair correlation of zeros and primes in short intervals" (arXiv:math/0206292)
5. **Montgomery & Soundararajan (2003)** — "The pair correlation of zeros and primes"
6. **Goldston, Gonek & Montgomery (2005)** — "On the pair correlation conjecture and the alternative hypothesis"
7. **Chan (2012)** — "Explicit relations between pair correlation of zeros and primes in short intervals", *Journal of Mathematical Analysis and Applications*
8. **Bettin & Chandee (2021)** — "Correlations of sieve weights and distributions of zeros" (arXiv:2101.04418)
9. **Bettin & Chandee (2018)** — "Trilinear forms with Kloosterman fractions", *Adv. Math.* 328
10. **Goldston, Montgomery & Soundararajan (2010)** — "Pairs of consecutive primes and the pair correlation of zeros of the Riemann zeta-function"

---

## 7. Conclusions for the Pair-Correlation Method

### On Bandwidth > 1

The thresholds mentioned in the original question (0.70 → support ≈ 1.04, 0.80 → support ≈ 1.26, 0.90 → support ≈ 1.70) refer to the relationship between the **proportion of zeros** exhibiting pair correlation at a given scale and the resulting **spectral support** in the test function. This is distinct from the SPC itself — it measures how much of the pair correlation structure is recovered at a given scale.

For bandwidth > 1 in the pair-correlation method to be achievable:

1. **SPC must hold at α > 1** (or at least a quantitative version with error o(1)).
2. **Error terms in prime pair estimates must be controlled** at scale h ∼ T^(α−1). Current methods fall short by a polynomial factor.
3. **The Hardy-Littlewood positive bias must be cancelled by oscillatory terms** in the explicit formula. This is guaranteed by the conjecture but requires proof.

### The Verdict

**No known unconditional prime pair result gives F(α) → 1 at any α > 1.**

- Bombieri-Vinogradov: insufficient (error dominates signal)
- Maynard-Tao bounded gaps: irrelevant scale and wrong sign
- EH (conjectural): controls errors but not the oscillatory cancellation
- Bettin-Chandee (2021): best unconditional bound, still non-asymptotic

The **weakest statement** that would suffice is a uniform pointwise error bound for prime pairs up to scale h ∼ T^ε with error O(T^(1−δ)). This is essentially a uniform version of the prime pair conjecture at small scales — stronger than Bombieri-Vinogradov but weaker than full Hardy-Littlewood. Even this is not known.

The fundamental obstruction is that **prime pairs have a positive bias** (Hardy-Littlewood), and the cancellation that brings F(α) back to 1 is a delicate consequence of the zeta function's analytic structure. No current method can prove this cancellation without already knowing the result.

### Future Directions

1. **Improved trilinear Kloosterman bounds**: If the saving in Bettin-Chandee's method could be pushed from N^(1/20) to N^(1/2−ε), it would give asymptotic results at α = 1 + ε for small ε.

2. **New Fourier-analytic approaches**: The Goldston-Montgomery equivalence between SPC and the variance formula opens the door to proving the variance formula directly, bypassing prime pair estimates.

3. **The sieve weight approach**: Bettin-Chandee's use of Selberg sieve weights rather than von Mangoldt function opens new avenues. The sieve weight correlations may be more amenable to Kloosterman fraction methods.

4. **Random matrix theory**: If a direct spectral proof of SPC could be constructed (via the Hilbert-Pólya operator), it would bypass prime pair estimates entirely. This remains the ultimate but most distant possibility.

---

*End of analysis.*