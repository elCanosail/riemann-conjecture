# The Pair-Correlation Line of Research: From Montgomery (1973) to Claude (2026) and Beyond

**A survey of the pair-correlation method for bounding the proportion of Riemann zeta zeros on the critical line, with an analysis of the frontier.**

*Compiled: 2026-08-11*

---

## Table of Contents

1. [Montgomery (1973): The Original Pair-Correlation Theorem](#1-montgomery-1973-the-original-pair-correlation-theorem)
2. [Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh (2024): Unconditional Montgomery](#2-baluyotgoldstonsuriajayaturnage-butterbaugh-2024-unconditional-montgomery)
3. [Goldston–Suriajaya (2025–2026): Removing RH from Montgomery's Proof](#3-goldstonsuriajaya-20252026-removing-rh-from-montgomerys-proof)
4. [The Montgomery–Taylor Optimised Kernel](#4-the-montgomerytaylor-optimised-kernel)
5. [Beyond Bandwidth 1: The Hardy–Littlewood Barrier](#5-beyond-bandwidth-1-the-hardy-littlewood-barrier)
6. [Higher Moments and Alternative Approaches](#6-higher-moments-and-alternative-approaches)
7. [The 0.68185 Ceiling: Method Optimality](#7-the-068185-ceiling-method-optimality)
8. [Claude (Anthropic, 2026-08-10): The Breakthrough](#8-claude-anthropic-2026-08-10-the-breakthrough)
9. [What Lies Beyond](#9-what-lies-beyond)
10. [References](#10-references)

---

## 1. Montgomery (1973): The Original Pair-Correlation Theorem

### The Paper

H. L. Montgomery, *"The pair correlation of zeros of the zeta function,"* Proc. Sympos. Pure Math. **XXIV** (1973), 181–193. AMS, Providence, RI. MR 0337821.

### What Montgomery Proved

Montgomery studied the Fourier transform of the pair correlation distribution:

$$F(\alpha, T) = \left(\frac{T}{2\pi}\log T\right)^{-1} \sum_{0<\gamma,\gamma'\leq T} T^{i\alpha(\gamma-\gamma')} w(\gamma-\gamma')$$

where $w(u) = 4/(4+u^2)$ and the sum runs over ordinates of nontrivial zeros $\rho = 1/2 + i\gamma$ (assuming RH).

**Theorem (Montgomery, 1973, assuming RH):** For real $\alpha$ and $T \geq 2$, uniformly for $0 \leq |\alpha| \leq 1$:

$$F(\alpha, T) = T^{-2|\alpha|}\log T\,(1+o(1)) + |\alpha| + o(1)$$

as $T \to \infty$.

The first term $T^{-2|\alpha|}\log T$ is the **diagonal contribution** ($\gamma = \gamma'$); the second term $|\alpha|$ is the **off-diagonal contribution** arising from the prime sum via the explicit formula.

### What Required RH

Montgomery's evaluation of the off-diagonal sum uses the **explicit formula** (Riemann–von Mangoldt form):

$$\sum_{\gamma,\gamma'} f(\gamma-\gamma') = \text{main term} + \sum_{\rho} \widehat{f}(\rho-1/2) + \cdots$$

When RH holds, $\rho = 1/2 + i\gamma$ is purely imaginary shift, so $\widehat{f}(\rho-1/2) = \widehat{f}(i(\gamma-\gamma'))$ is purely a function of the real ordinate differences $\gamma-\gamma'$. This allows the sum to be evaluated as a sum over primes via the von Mangoldt function $\Lambda(n)$:

$$\sum_{\rho,\rho'} T^{i\alpha(\gamma-\gamma')} = \sum_{n \leq T} \frac{\Lambda(n)}{\sqrt{n}} T^{i\alpha \cdot 0} + \sum_{m,n \leq T} \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}} T^{i\alpha(\log m - \log n)} + \cdots$$

The key step is that **without RH**, the zeros $\rho = \beta + i\gamma$ have $\beta \neq 1/2$, and the terms $T^{i\alpha(\rho-\rho')} = T^{i\alpha((\beta-\beta') + i(\gamma-\gamma'))}$ acquire real-exponential factors $T^{-\alpha(\beta-\beta')}$ that destroy the clean prime-side evaluation. The diagonal terms $T^{i\alpha(\rho-\rho)}$ are still $1$, but the off-diagonal terms mix real and imaginary parts in a way that cannot be isolated by sign.

### What Was Unconditional

Montgomery's **conjecture** (now called the **pair-correlation conjecture**) states that for fixed $\alpha \leq \beta$:

$$\lim_{T\to\infty} \frac{\#\{(\gamma,\gamma'): 0<\gamma,\gamma'\leq T,\; 2\pi\alpha/\log T \leq \gamma-\gamma' \leq 2\pi\beta/\log T\}}{\frac{T}{2\pi}\log T} = \int_\alpha^\beta \left(1 - \left(\frac{\sin\pi u}{\pi u}\right)^2\right) du + \delta(\alpha,\beta)$$

where $\delta(\alpha,\beta) = 1$ if $0 \in [\alpha,\beta]$ and $0$ otherwise. This conjecture was **not proved**; it was derived from the theorem by assuming $F(\alpha) = 1 + o(1)$ for $|\alpha| > 1$ (Montgomery's "strong pair-correlation conjecture"), which was not established.

Montgomery also conjectured that $F(\alpha) = 1 + o(1)$ uniformly for $|\alpha| > 1$ in bounded intervals — this remains open.

### The Simple-Zero Corollary

From the theorem, Montgomery derived **Corollary 2**: assuming RH, at least $2/3$ of the zeros are simple.

**Proof sketch:** Using the Fejér kernel $r(u) = \max(1-|u|, 0)$, one has $\widehat{r}(\alpha) = (\sin \pi\alpha / \pi\alpha)^2 \geq 0$. Then:

$$\sum_{\gamma,\gamma' \leq T} r\left(\frac{\gamma-\gamma'}{\frac{1}{2}\log T}\right) w(\gamma-\gamma') = \left(\frac{T}{2\pi}\log T\right) \int_{-\infty}^{\infty} \widehat{r}(\alpha) F(\alpha,T)\,d\alpha$$

By the theorem, the right side is $(1+o(1)) \frac{T}{2\pi}\log T \cdot (1 + 2\int_0^1 \alpha \widehat{r}(\alpha)\,d\alpha) = (4/3 + o(1)) \frac{T}{2\pi}\log T$.

On the other hand, the diagonal terms ($\gamma = \gamma'$) contribute $\sum_\rho m_\rho^2$ where $m_\rho$ is the multiplicity. Thus $\sum_\rho m_\rho^2 \leq (4/3 + o(1)) N(T)$. Since $m_\rho^2 \geq 2m_\rho - 1$ for integers $m_\rho \geq 1$, we get:

$$\sum_\rho (2m_\rho - 1) \leq \sum_\rho m_\rho^2 \leq \frac{4}{3} N(T) \implies 2N_{\text{simple}} + 2N_{\text{multiple}} - N(T) \leq \frac{4}{3} N(T)$$

which gives $N_{\text{simple}} \geq (2 - 4/3)N(T) = (2/3)N(T)$.

The constant $2/3 = 2 - \lambda^{-1} - \lambda^3$ evaluated at $\lambda = 1$ (the bandwidth limit).

### Significance

Montgomery's paper was revolutionary: it was the first result showing that **infinitely many** zeros are simple (previously, even this was unknown). The connection to Freeman Dyson's observation that the pair-correlation function $1 - (\sin \pi u / \pi u)^2$ matches the GUE (Gaussian Unitary Ensemble) eigenvalue correlation function launched the entire random-matrix approach to zeta zeros.

---

## 2. Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh (2024): Unconditional Montgomery

### The Paper

S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, *"An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function,"* Acta Arith. **214** (2024), 357–376. arXiv:2306.04799. DOI: 10.4064/aa230612-20-3.

### The Key Innovation

The central achievement of BGSTB24 is making Montgomery's pair-correlation theorem **unconditional**. They define the unconditional form of Montgomery's function:

$$F(x, T) = \sum_{T<\gamma,\gamma'\leq 2T} x^{\rho-\rho'} W(\rho-\rho')$$

where $W(u) = 4/(4-u^2)$ and the sum runs over **all** zeros (not just those on the critical line).

**Theorem 1 (BGSTB24):** The function $F(\alpha)$ is real, even, and nonnegative. Moreover, as $T \to \infty$:

$$F(\alpha) = T^{-2\alpha}(\log T + O(1)) + \alpha + O\left(\frac{1}{\sqrt{\log T}}\right)$$

uniformly for $0 \leq \alpha \leq 1$.

This is **nearly identical** to Montgomery's theorem but does **not assume RH**.

### How They Removed RH

The key insight is that Montgomery's **prime-side evaluation** is already unconditional. The sum over prime powers:

$$\sum_{n \leq X} \frac{\Lambda(n)}{\sqrt{n}} + \sum_{m,n \leq X} \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}} X^{i\alpha(\log m - \log n)}$$

depends only on the distribution of primes, not on the location of zeros. The unconditional evaluation uses:

1. **Chebyshev–Mertens estimates** for $\sum_{n \leq X} \Lambda(n)^2$, $\sum_{n \leq X} \Lambda(n)^2/n$, and $\sum_{n \leq X} \Lambda(n)n^{-1/2}$.
2. The **Montgomery–Vaughan generalised Hilbert inequality** for the frequencies $\log n$, $n \leq X$.

The difficulty was on the **zero side**: without RH, zeros $\rho = \beta + i\gamma$ have $\beta \neq 1/2$, and the terms $x^{\rho-\rho'} = x^{(\beta-\beta') + i(\gamma-\gamma')}$ have real-exponential factors. BGSTB24 handle this by working with the absolute value $x^{|\beta-\beta'|}$ and showing the error is controlled.

### What Remains Conditional

BGSTB24's simple-zero result requires a **thin-box assumption**:

**Theorem 2 (BGSTB24):** Suppose all zeros $\rho = \beta + i\gamma$ with $T^{3/8} < \gamma \leq T$ satisfy $|\beta - 1/2| < 1/(2\log T)$. Then at least **61.7%** of these zeros are simple.

The method "neither requires nor provides any information on whether any of these zeros are on the critical line." The thin-box assumption is weaker than RH but stronger than nothing — it allows zeros to be slightly off the line but constrains them to a narrow horizontal strip.

The same result holds under the weaker assumption of a **strong zero-density hypothesis**.

---

## 3. Goldston–Suriajaya (2025–2026): Removing RH from Montgomery's Proof

### The Papers

- D. A. Goldston and A. I. Suriajaya, *"Zeta Zeros on the Critical Line,"* arXiv:2511.20059 (2025). [Exposé]
- D. A. Goldston, J. Lee, J. Schettler, A. I. Suriajaya, *"Pair Correlation Conjecture for the zeros of the Riemann zeta-function I: simple and critical zeros,"* arXiv:2503.15449 (2025). [GLSS25]
- D. A. Goldston, A. I. Suriajaya, *"Zeta zeros in a narrow vertical box,"* arXiv:2603.28104 (2026). [GS26]
- S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, *"Pair correlation of zeros of Dirichlet L-functions: a possible path towards the conjectures of Chowla, Elliott-Halberstam and Montgomery,"* Math. Ann. (2026). [BGSTB25]

### The Central Question

Goldston and Suriajaya explicitly asked: **"What would follow if RH could be removed from Montgomery's proof?"**

Their analysis revealed that Montgomery's proof has **two distinct components**:

1. **The prime-side evaluation** (Montgomery's sum over prime powers) — this is unconditional, as BGSTB24 showed.
2. **The zero-side reading** — classically requires RH because without it, the diagonal terms $T^{i\alpha(\gamma-\gamma')}$ are not sufficient: zeros off the line come in symmetric pairs $\{\rho, 1-\bar{\rho}\}$, and each such pair contributes to the "diagonal" when $\gamma = \gamma'$ even though $\rho \neq \rho'$.

### The Symmetric-Diagonal Problem

Without RH, the sum over zeros with $\gamma = \gamma'$ includes:
- **True diagonal terms**: $\rho = \rho'$, contributing $m_\rho$ (the multiplicity)
- **Symmetric-diagonal terms**: $\rho \neq \rho'$ but $\gamma = \gamma'$, i.e., pairs $\{\beta+i\gamma, 1-\beta+i\gamma\}$ with $\beta \neq 1/2$, contributing $2$ each

BGSTB24 showed that the sum of **both types** of diagonal terms is bounded by $(4/3 + o(1))N(T)$, the same bound as in the RH case. Since the true diagonal terms have the number of zeros as a lower bound, the symmetric-diagonal terms can account for at most $1/3$ of $N(T)$. Hence at least $2/3$ of the zeros must be on the critical line — **provided** all zeros are in a thin enough box.

### The Key Result

**Theorem (Goldston–Suriajaya, 2025):** Suppose all zeros $\rho = \beta + i\gamma$ with $T < \gamma \leq 2T$ lie in the vertical box:

$$B_b = \left\{s = \sigma + it : \left|\sigma - \frac{1}{2}\right| < \frac{b}{2\log T},\; T < t \leq 2T\right\}$$

where $b = b(T) \to 0$ as $T \to \infty$. Then asymptotically at least **2/3** of the zeros are simple **and** on the critical line.

With $b = 0.3185$: at least $0.66666908 + o(1)$ of zeros are simple, $0.66666908 + o(1)$ are on the critical line, and $0.33333816 + o(1)$ are both simple and on the critical line.

With $b = 0.001$: at least $0.67250064 + o(1)$ of zeros are simple, $0.67250064 + o(1)$ are on the critical line, and $0.34500129 + o(1)$ are both.

### What Was Identified as the Remaining Obstacle

Goldston and Suriajaya identified that the **termwise positivity** that fails off the line is the precise obstacle. On the line, each zero contributes a positive rank-one form. Off the line, a symmetric pair $\{\rho, 1-\bar{\rho}\}$ contributes a form of **indefinite signature (1, 1)** — one positive and one negative eigenvalue. This indefiniteness prevents the clean separation of diagonal and off-diagonal terms.

The question then becomes: can one **replace** the termwise positivity argument with something that works for indefinite forms? This is precisely what Claude (2026) did.

---

## 4. The Montgomery–Taylor Optimised Kernel

### The Optimisation Problem

Montgomery's original kernel $r(u) = \max(1-|u|, 0)$ (the Fejér kernel) gives the constant $2/3$. Montgomery and Taylor (1975, lecture notes) found a better kernel that improves this to **0.6725**.

Cheer and Goldston (1993) improved it to **0.6727** under RH.

Chirre, Gonçalves, and de Laat (2020) used **semidefinite programming** to obtain **0.6792** by exploiting the positivity of $F$ outside $[-1, 1]$.

### The Variational Problem

The optimisation problem is: maximise the proportion of simple zeros subject to the constraints imposed by the pair-correlation data at bandwidth $\lambda \leq 1$.

Concretely, one considers test functions $f$ with $\operatorname{supp}(\widehat{f}) \subseteq [-1, 1]$ and forms the functional:

$$\mathcal{J}(f) = \frac{\int_{-\infty}^{\infty} \widehat{f}(\alpha) F(\alpha)\,d\alpha - f(0)}{\int_{-\infty}^{\infty} f(u)\,du - f(0)}$$

where the numerator is the off-diagonal contribution and the denominator is related to the diagonal. The optimal $f$ is found by solving a variational problem.

### Montgomery–Taylor Kernel

The Montgomery–Taylor kernel is a specific choice of $f$ (or equivalently, $r$) that optimises the simple-zero bound within bandwidth 1. It is a piecewise polynomial function with support in $[-1, 1]$ and satisfies $\widehat{f} \geq 0$.

The constant $0.6725$ arises as the optimal value of $2 - C$ where $C$ is the optimal bound on $\sum m_\rho^2 / N(T)$ achievable with bandwidth-1 test functions.

### Can It Be Improved Further Within Bandwidth 1?

**No, not significantly.** The 0.6792 result of Chirre, Gonçalves, and de Laat (2020) already pushes close to the limit by using SDP and exploiting the positivity of $F$ outside $[-1, 1]$. However, this exploitation of $F$ for $|\alpha| > 1$ is **conjectural** — it relies on the strong pair-correlation conjecture $F(\alpha) = 1 + o(1)$ for $|\alpha| > 1$, which is not proved.

Within the **proven** regime (bandwidth 1, unconditional), the Montgomery–Taylor kernel at 0.6725 (or 2/3 in the simple Fejér case) represents the practical limit.

### The Optimisation Framework (Cohn–Elkies Connection)

Chirre, Gonçalves, and de Laat (2020) and later Carneiro, Chandee, Chirre, and Milinovich (2022) connected the pair-correlation optimisation to the **Cohn–Elkies framework** for sphere-packing bounds. This uses functions in the Schwartz class (not just bandlimited) with $\widehat{f}(\alpha) \leq 0$ for $|\alpha| \geq 1$, matching the conditions for linear-programming bounds in the Delsarte/Cohn–Elkies theory.

This framework has been further developed in "Fourier optimization and Montgomery's pair correlation conjecture" (2023), which gives bounds for the average value of $F(\alpha)$ over long intervals.

---

## 5. Beyond Bandwidth 1: The Hardy–Littlewood Barrier

### What Bandwidth 1 Means

The bandwidth of a test function $f$ is the support of its Fourier transform $\widehat{f}$. Bandwidth 1 means $\operatorname{supp}(\widehat{f}) \subseteq [-1, 1]$, which corresponds to probing zero spacings up to $2\pi/\log T$ (the average spacing).

Montgomery's theorem proves the pair-correlation asymptotic for $|\alpha| \leq 1$ unconditionally. For $|\alpha| > 1$, the formula involves:

$$F(\alpha, T) = T^{-2\alpha}(\log T + O(1)) + \alpha + O\left(\frac{1}{\sqrt{\log T}}\right)$$

which is **not valid** for $\alpha > 1$ without additional input.

### What Unconditional Pair-Correlation at $\lambda > 1$ Would Require

To extend the pair-correlation analysis to $\lambda > 1$, one needs to evaluate the prime-side sum:

$$\sum_{m,n \leq X} \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}} X^{i\alpha(\log m - \log n)}$$

for $X = T^\lambda$ with $\lambda > 1$. This requires controlling the **correlation of prime powers** at scales $\log m - \log n$ that are larger than what the Montgomery–Vaughan Hilbert inequality handles.

The Hardy–Littlewood prime pair conjecture gives the asymptotic:

$$\sum_{n \leq X} \Lambda(n)\Lambda(n+h) \sim \mathfrak{S}(h) X$$

where $\mathfrak{S}(h)$ is the twin-prime constant. For the pair-correlation problem, one needs this uniformly for $h$ up to $X^\delta$ for some $\delta > 0$, which is **far beyond** current technology.

### The Connection

The relationship is:

1. **Bandwidth 1** ($\lambda \leq 1$): The Montgomery–Vaughan generalised Hilbert inequality gives the needed bound unconditionally. This is what BGSTB24 used.

2. **Bandwidth $\lambda > 1$**: Requires bounds on prime correlations at larger scales. The Hardy–Littlewood conjecture would give these, but it is **not proved** for any $\delta > 0$ beyond the trivial range.

3. **The precise threshold**: To reach simple-zero proportion $p$, one needs pair-correlation information on Fourier support out to roughly:
   - $p = 0.70$: Fourier support to $\approx 1.04$
   - $p = 0.80$: Fourier support to $\approx 1.26$
   - $p = 0.90$: Fourier support to $\approx 1.70$

These thresholds come from the variational analysis of the optimisation problem: the optimal test function's Fourier transform must be known on $[-\lambda, \lambda]$ to certify a given proportion.

### How Far Are We?

**Very far.** The Hardy–Littlewood prime pair conjecture in the range needed (uniformly for $h$ up to $X^\delta$) is one of the deepest open problems in analytic number theory. Current best results (e.g., the Bombieri–Vinogradov theorem) give average-case bounds but not the pointwise correlations needed.

The **Elliott–Halberstam conjecture** would help, but it is itself unproved. Even assuming GRH, one only gets $O(X^{1/2+\epsilon})$ error terms, which is insufficient for the pair-correlation at $\lambda > 1$.

---

## 6. Higher Moments and Alternative Approaches

### Unconditional Higher Moments at Available Bandwidths

Claude's paper (2026) explicitly checked whether higher moments of the pair-correlation sum could help. The analysis shows that at bandwidth $\lambda \leq 1$, the **unconditional** higher moments do not provide additional leverage beyond the second moment.

The reason is structural: the pair-correlation data at bandwidth 1 encodes only the first two trace moments of the Weil form compression. Higher moments would require either:
- Higher-order correlations (k-tuple correlations), which are not available unconditionally at any bandwidth $> 0$
- Higher trace moments of the compression, which are not accessible from the prime-side data at bandwidth 1

### Is This Definitive?

The result is definitive **for certificates that read only bandwidth-1 pair-correlation data and hold configuration by configuration** (i.e., that bound the proportion of simple zeros from the inequality $m_\rho^2 \geq 2m_\rho - 1$ applied pointwise to multiplicities).

The 0.68185 ceiling (see §7 below) confirms that **no certificate of this form** can exceed 0.68185, regardless of which test function is used.

### Other Ways to Use Higher-Order Data

1. **k-tuple correlations**: Montgomery (1973) conjectured that the k-tuple correlation function of zeros matches that of GUE. Proving this unconditionally would give access to higher-order moment data, but this is far beyond current methods.

2. **Mollifier methods**: The Conrey–Ghosh–Gonek (1998) / Bui–Heath-Brown (2013) approach uses mollified moments of $\zeta'(\rho)$:
   $$M_\nu = \sum_\rho \left|\frac{\zeta'}{\zeta}(\rho) B(\rho)\right|^{2\nu}$$
   where $B(s)$ is a mollifier. This gives $19/27 \approx 0.7037$ under RH (Bui–Heath-Brown, 2013), which is **better** than the pair-correlation bound at bandwidth 1. However, mollifier methods are **not easily adaptable** to the off-critical-line case, and they require RH (or GRH) for the error term analysis.

3. **Levinson's method**: The current unconditional record is Pratt, Robles, Zaharescu, Zeindler (2020): at least **41.7%** of zeros are on the critical line and at least **40.7%** are simple and on the critical line. This is a different technique from pair correlation, using a carefully chosen mollifier and the explicit formula.

4. **Selberg's variance method**: Selberg (1946) proved that a **positive density** of zeros are simple and on the critical line (unconditionally). This is the weakest but most robust result.

5. **Higher-order Weil forms**: Bombieri (2000) studied Weil's quadratic functional from a variational perspective. The functional is positive semidefinite if and only if RH is true. Finite truncations of the associated quadratic form have a number of negative eigenvalues equal to half the number of zeros off the critical line (if finitely many). This suggests a **spectral** approach to counting off-line zeros, but no effective quantitative bound has emerged.

---

## 7. The 0.68185 Ceiling: Method Optimality

### How It Is Computed

Claude's paper (2026) establishes that the pair-correlation method with bandwidth $\lambda \leq 1$ and configuration-by-configuration certificates (i.e., certificates that bound the proportion of simple zeros from the inequality $m_\rho^2 \geq 2m_\rho - 1$ applied to each multiplicity) has an **absolute ceiling** of **0.68185**.

This is computed by constructing an **explicit extremal configuration** of multiplicities that saturates the pair-correlation constraints at bandwidth 1 while minimising the proportion of simple zeros.

The extremal configuration is a probability distribution on the multiplicity values $\{1, 2, 3, \ldots\}$ that:
1. Satisfies the first moment constraint: $\sum m_\rho = N(T)$
2. Satisfies the second moment constraint: $\sum m_\rho^2 \leq C(\lambda) \cdot N(T)$ where $C(\lambda)$ is the optimal bound from the pair-correlation at bandwidth $\lambda$
3. Minimises the proportion of multiplicity-1 elements

For $\lambda = 1$, the optimal $C(1)$ from Montgomery's theorem is $4/3$, and the minimisation gives:

$$\text{min proportion of simple zeros} = 1 - \frac{1}{2}\left(\frac{4}{3} - 1\right) = \frac{2}{3}$$

But the **true** optimisation over all test functions (not just the Fejér kernel) with the constraint that the certificate is of the form $m_\rho^2 \geq 2m_\rho - 1$ gives **0.68185** as the absolute ceiling.

### Is It Tight?

The 0.68185 value is the **theoretical maximum** for any certificate of the specified form. It is tight in the sense that there exists a configuration of multiplicities that achieves exactly this bound (in the limit).

The Claude result of 0.6725 (with the Montgomery–Taylor kernel) is therefore within **0.00935** of the ceiling of its own method — remarkably close.

### Could a Different Certificate Architecture Do Better?

**Yes, potentially.** The 0.68185 ceiling applies only to certificates that:
1. Read only bandwidth-1 pair-correlation data
2. Hold configuration by configuration (i.e., bound the proportion from inequalities applied to each multiplicity)
3. Use the integrality of multiplicities ($m_\rho^2 \geq 2m_\rho - 1$) applied **pointwise** to each individual multiplicity $m_\rho$

Claude's breakthrough was to **abandon the pointwise integrality argument** and instead treat the Weil form as a whole Hermitian matrix, applying a **rank–trace inequality** (Lemma 3.2, proved via von Neumann's trace inequality). This is the matrix analogue of $m_\rho^2 \geq 2m_\rho - 1$ applied to the **aggregate** rather than termwise.

By Sylvester's law of inertia, the off-line pairs contribute blocks of signature $(1, 1)$ — one positive and one negative eigenvalue each. The on-line zeros contribute rank-one positive semidefinite forms. The rank–trace inequality bounds the number of on-line zeros from below using only the rank and trace of the full form, without needing to control individual multiplicities.

This architecture **bypasses the 0.68185 ceiling** because it does not hold configuration by configuration — it extracts global spectral information from the aggregate data.

However, the **0.68185 ceiling is still valid** as a statement about the original certificate architecture. It tells us that pushing further within *that* architecture would require fundamentally different data — specifically, pair-correlation information at bandwidth $> 1$.

### The Claude Architecture Summary

| Component | Role |
|-----------|------|
| $P$ (on-line contribution) | Positive semidefinite, rank $\leq s$ (number of distinct on-line zeros) |
| $Q$ (off-line contribution) | Signature $(p, p)$ where $p$ = number of distinct off-line pairs |
| Rank–trace inequality (von Neumann) | Binds $s$ from below using $\operatorname{tr} P$, $\operatorname{tr} Q$, $\|P+Q\|_F$ |
| Montgomery's moment at $\lambda = 1$ | Evaluates $\operatorname{tr} G$ and $\operatorname{tr} G^2$ unconditionally |
| Sylvester's law of inertia | Ensures signature of $Q$ is $(p, p)$ |

The result: at $\lambda = 1$, $H(1) = 2 - 1 - 1/3 = 2/3$. With the Montgomery–Taylor kernel, the constant becomes $0.6725$.

---

## 8. Claude (Anthropic, 2026-08-10): The Breakthrough

### The Paper

Claude, *"More Than Two Thirds of the Zeros of the Riemann Zeta Function Lie on the Critical Line,"* August 10, 2026. [PDF](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf)

A Lean 4 formalization is available at [anthropics/zeta-23-lean](https://github.com/anthropics/zeta-23-lean), verified with the standard `comparator` tool.

### The Three Main Theorems

**Theorem A.** For $0 < \lambda \leq 1$:
$$N_0^*(T, 2T) \geq H(\lambda) N(T, 2T)$$
where $H(\lambda) = 2 - \lambda^{-1} - \lambda^3/3$. At $\lambda = 1$, $H(1) = 2/3$.

**Theorem B.** Same bound for simple zeros on the line:
$$N_0^s(T, 2T) \geq H(\lambda) N(T, 2T)$$

**Theorem C.** For distinct zeros:
$$N_d(T, 2T) \geq \max(H_d(\lambda), F(\lambda)) N(T, 2T)$$
where $H_d(\lambda) = (1 + H(\lambda))/2$ and $F(\lambda) = \lambda(1+\lambda^{2/3})^{-1}$. At $\lambda = 1$, $H_d(1) = 5/6$.

With the Montgomery–Taylor optimised test family, the constants become:
- Simple zeros on the critical line: **0.6725**
- Distinct zeros on the critical line: **0.6725**
- Distinct zeros (anywhere): **0.83625**

### The Core Innovation

Claude's key insight was to treat the **full indefinite Weil form** (positive AND negative parts together) rather than requiring termwise positivity. The decomposition:

$$G = P + Q$$

where:
- $P$ is the contribution from on-line zeros (positive semidefinite, rank $\leq s$)
- $Q$ is the contribution from off-line pairs (signature $(p, p)$)

And then applying a **rank–trace inequality** (Lemma 3.2) proved via **von Neumann's trace inequality**:

For Hermitian $P \succeq 0$ of rank $\leq r$ and Hermitian $Q$ with $\leq b$ positive eigenvalues:
$$r \geq \frac{(\operatorname{tr}(P+Q))^2}{\|P+Q\|_F^2} - b$$

This is the **matrix analogue** of $m_\rho^2 \geq 2m_\rho - 1$ but applied to the **aggregate** structure rather than termwise.

Combining with Sylvester's law of inertia (off-line pairs contribute signature $(1,1)$ blocks) and Montgomery's unconditional moment evaluation:

$$s \geq 4N - 2N - (1 + \lambda^3)N - o(N) = H(\lambda)N - o(N)$$

At $\lambda = 1$: $s \geq (2/3 - o(1))N$.

### What the Method Uses

1. **Functional equation** of $\zeta(s)$
2. **Weil's explicit formula** for $\zeta(s)$
3. **Chebyshev–Mertens estimates** for prime-power sums
4. **Montgomery–Vaughan generalised Hilbert inequality**
5. **Riemann–von Mangoldt zero-counting formula**
6. **Sylvester's law of inertia**
7. **Von Neumann's trace inequality** (the new ingredient)

No mollifier, no Levinson's method, no zero-density estimate, no zero-free region.

### What the Method Does NOT Say

- It has **no bearing** on RH in either direction.
- It certifies that **at least 2/3 of the zeros are on the line** — it says nothing about the remaining third, which are not shown to be off the line but simply not reached by the certificate.
- The inputs are insensitive to $o(N)$ off-line zeros.

---

## 9. What Lies Beyond

### The Immediate Frontier: Bandwidth > 1

Claude's paper explicitly states that reaching higher proportions by the same route would require pair-correlation information on Fourier supports out to:
- $0.70$: Fourier support to $\approx 1.04$
- $0.80$: Fourier support to $\approx 1.26$
- $0.90$: Fourier support to $\approx 1.70$

This requires **unconditional pair-correlation estimates at $\lambda > 1$**, which requires:
1. Hardy–Littlewood-level prime-pair correlation estimates
2. Uniformity for prime correlations at scales $\gg X$ (where $X = T^\lambda$)

Currently, the best unconditional results are at the Bombieri–Vinogradov level (average over moduli), which is insufficient for the pointwise correlations needed.

### The Alternative Hypothesis

Goldston, Lee, Suriajaya, and Schettler (GLSS25) showed that the **Alternative Hypothesis** (AH) — which posits a different pair-correlation density from the GUE — also implies asymptotically 100% of zeros are simple and on the critical line. AH is a counter-hypothesis to Montgomery's PCC that could arise from Landau–Siegel zeros. Both PCC and AH lead to the same conclusion about simple zeros, but they describe **different** distributions of zero spacings.

### Higher Moments via k-Tuple Correlations

Montgomery conjectured that the $k$-tuple correlation function matches GUE. Proving this unconditionally (even for $k=3$) would give access to third and higher moments, which could potentially improve the bounds further. However, the current technology for even the pair-correlation at bandwidth 1 is the result of 50+ years of work by many mathematicians.

### The Rank–Trace Idea

Claude's rank–trace approach is novel and opens a new direction: **linear-algebraic reading of the Weil form**. This could potentially be:
- Applied to $L$-functions beyond $\zeta(s)$
- Combined with other matrix-analytic inequalities (e.g., Horn's inequalities, free probability)
- Extended to higher-order Weil forms (Bombieri's quadratic functional has natural higher-order analogues)

### The 0.68185 Ceiling: What It Teaches

The 0.68185 ceiling teaches a structural lesson: **any approach that reads only bandwidth-1 pair-correlation data and uses pointwise integrality of multiplicities cannot exceed 0.68185**. This means:
- Better test functions within bandwidth 1 will not help.
- Better bounds on the second moment within bandwidth 1 will not help.
- To exceed 0.68185 by this route, one needs pair-correlation data at $\lambda > 1$.
- Claude's approach already bypassed the ceiling by **not** using pointwise integrality, so this bound is a statement about a **different** method than Claude's.

### The Deepest Open Questions

1. **Unconditional pair-correlation at $\lambda > 1$**: Requires breakthroughs in prime correlations, essentially equivalent to progress on the Hardy–Littlewood conjecture.

2. **Unconditional k-tuple correlations for $k \geq 3$**: Even at bandwidth 1, this is wide open.

3. **Can the rank–trace idea be refined?** The von Neumann inequality gives a specific bound. Could sharper matrix inequalities (e.g., from free probability or non-commutative geometry) extract more information from the same data?

4. **Does the Weil form compression have a spectral gap?** Bombieri's (2000) work suggests that negative eigenvalues of finite truncations correspond to off-line zeros. Can this be made quantitative?

5. **Is 2/3 the right target?** Assuming RH, Conrey–Ghosh–Gonek (with GLH) and Bui–Heath-Brown (unconditionally under RH) get $19/27 \approx 0.7037$ via mollifiers. The pair-correlation approach is currently behind the mollifier approach *under RH*. The gap between them is a major open question.

6. **What does Claude's Lean proof teach us?** The fact that Claude produced a complete, $\texttt{sorry}$-free Lean formalisation in a matter of days suggests that **formal verification** may become a practical tool for checking complex analytic number theory proofs. This could help resolve disagreements about the correctness of novel arguments.

---

## 10. References

### Foundational

- [Mon73] H. L. Montgomery, "The pair correlation of zeros of the zeta function," *Proc. Sympos. Pure Math.* **XXIV** (1973), 181–193. MR 0337821.
- [Mon75] H. L. Montgomery, "Gaps between primes," 1975. Lecture notes for Hanover Talk, Summer 1975.
- [GM78] P. X. Gallagher and J. H. Mueller, "Primes and zeros in short intervals," *J. Reine Angew. Math.* **303/304** (1978), 205–220.
- [CG93] A. Y. Cheer and D. A. Goldston, "Simple zeros of the Riemann zeta-function," *Proc. Amer. Math. Soc.* **118** (1993), 365–373.
- [CGdL20] R. Chirre, M. Gonçalves, and T. de Laat, "Pair correlation estimates for the zeros of the zeta function via semidefinite programming," arXiv:1810.08843, *J. Reine Angew. Math.* (2020).

### Mollifier Methods (Under RH)

- [CGG98] J. B. Conrey, A. Ghosh, and S. M. Gonek, "Simple zeros of the Riemann zeta-function," *Proc. London Math. Soc.* **76** (1998), 497–522. [RH + GLH $\Rightarrow 19/27$]
- [BHB13] H. M. Bui and D. R. Heath-Brown, "On simple zeros of the Riemann zeta-function," arXiv:1302.5018 (2013). [RH alone $\Rightarrow 19/27$]

### Unconditional Work on Simple Zeros

- [PRZZ20] K. Pratt, N. Robles, A. Zaharescu, and D. Zeindler, "More than five-twelfths of the zeros of $\zeta$ are on the critical line," *Res. Math. Sci.* **7** (2020), Paper No. 2. [Unconditional: $>41.7\%$ on line, $>40.7\%$ simple and on line]
- [Sel46] A. Selberg, "Contributions to the theory of the Riemann zeta-function," *Arch. Math. Naturv.* **48** (1946), 89–155.

### Unconditional Montgomery (BGSTB24)

- [BGSTB24] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, "An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function," *Acta Arith.* **214** (2024), 357–376. arXiv:2306.04799. DOI: 10.4064/aa230612-20-3.

### Removing RH from Montgomery (GS25–GS26)

- [GLSS25] D. A. Goldston, J. Lee, J. Schettler, A. I. Suriajaya, "Pair Correlation Conjecture for the zeros of the Riemann zeta-function I: simple and critical zeros," arXiv:2503.15449 (2025).
- [GLSS25b] D. A. Goldston, J. Lee, J. Schettler, A. I. Suriajaya, "Pair Correlation Conjecture for the zeros of the Riemann zeta-function II: The alternative hypothesis," arXiv:2507.06823 (2025).
- [GS25] D. A. Goldston and A. I. Suriajaya, "Zeta zeros on the critical line," arXiv:2511.20059 (2025). [Exposé]
- [GS26] D. A. Goldston and A. I. Suriajaya, "Zeta zeros in a narrow vertical box," arXiv:2603.28104 (2026).
- [BGSTB25] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, "Pair correlation of zeros of Dirichlet L-functions," *Math. Ann.* (2026).

### Weil's Quadratic Functional

- [Bom00] E. Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I," *Rend. Lincei Mat. Appl.* **11** (2000), 183–233. eudml.org/doc/252338.

### Fourier Optimization

- [CCCM22] E. Carneiro, D. Chandee, R. Chirre, and Y. Milinovich, arXiv:2104.xxxx — bounds for integrals of $F(\alpha,T)$ at $|\alpha|>1$.
- [CCdL23] R. Chirre, M. Gonçalves, T. de Laat, "Fourier optimization and Montgomery's pair correlation conjecture," *arXiv:2310.01913* (2023).

### Claude's Result (2026)

- Claude, "More Than Two Thirds of the Zeros of the Riemann Zeta Function Lie on the Critical Line," Anthropic, August 10, 2026. [PDF](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf)
- [anthropics/zeta-23-lean](https://github.com/anthropics/zeta-23-lean) — Lean 4 formalisation.
- [anthropics/zeta-23-note](https://www-cdn.anthropic.com/23455459f8832d06bb175cc0f88d019aed962ef8.pdf) — informal expert note by Alpöge and Furman.
- [Anthropic research page](https://www.anthropic.com/research/riemann-zeta)

---

*This survey was compiled from publicly available papers, arXiv preprints, and the Anthropic Claude paper (2026). All claims are attributed to the original sources. References marked "arXiv" may have since appeared in peer-reviewed journals.*
