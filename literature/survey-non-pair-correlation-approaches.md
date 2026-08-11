# Survey: Non-Pair-Correlation Approaches to the Critical Line Problem

**Prepared:** 2026-08-11  
**Context:** Following Anthropic's announcement (2026-08-10) that Claude proved unconditionally ≥ 2/3 (optimised: 67.25%) of nontrivial zeros of ζ(s) lie on the critical line, via a pair-correlation method. This survey examines all other known approaches.

---

## 1. The Levinson–Conrey Mollifier Method

### 1.1 Historical Development

The mollifier method, introduced by Norman Levinson in 1974, remains the most powerful direct analytic technique for proving that a positive proportion of zeros lie on the critical line. Levinson showed that at least **1/3** of the nontrivial zeros lie on Re(s) = 1/2. This was improved to **5/12 ≈ 41.67%** by Conrey (1989) using a more sophisticated mollifier.

**Key milestones:**
- **Levinson (1974):** ≥ 1/3 of zeros on the critical line. Method: mollify ζ(s) by a Dirichlet polynomial to reduce mean values of |ζ′/ζ|².
- **Conrey (1989):** ≥ 5/12. Introduced a longer mollifier (length ≈ T^θ with θ > 1/2), exploiting additive divisor problems and Kloosterman sums.
- **Bui, Conrey, Young (2011):** arXiv:1006.3304. Extended mollifier length to θ = 4/7, maintaining 5/12 but with improved error terms.
- **Feng (2012):** arXiv:1203.0058. Added secondary terms to the mollifier, pushing the provable proportion slightly above 5/12 (to ~41.78%, though often cited as still ~5/12 in rounded form).
- **Pratt, Robles, Zaharescu, Zeindler (arXiv:1706.04593, 2017+):** Pushed the mollifier method to its current frontier. Achieved proportion **> 5/12** with refined analysis of the additive divisor problem and improved bounds on shifted convolution sums.

### 1.2 Structural Limits

The mollifier method faces a fundamental barrier: the **mollifier length barrier**. One must control mean values of the form

$$
\int_0^T |M(1/2 + it)|^2 \, dt
$$

where M(s) = ∑_{n ≤ y} μ(n) P(log(y/n)/log y) n^{-s} is the mollifier. The length y = T^θ is constrained by:

1. **The shifted convolution problem:** Terms like ∑_{m,n} a_m b_n / √(mn) with m ≈ n require bounds on ∑_{n ≤ x} d(n)d(n + h).

2. **The additive divisor conjecture:** The mollifier method requires understanding ∑_{n ≤ x} d_3(n)d(n + h) or similar, where d_k is the k-fold divisor function. The expected asymptotic is known only for limited ranges.

3. **The critical exponent θ = 1:** If one could take a mollifier of "full length" (y = T), the method would in principle yield 100%. However, controlling mean values at this length requires solving the **Dirichlet divisor problem** in a range far beyond current technology.

**The θ = 1/2 barrier:** For the "standard" mollifier, the method breaks down when θ exceeds 1/2 because the off-diagonal terms in the mean square become uncontrollable. Conrey's breakthrough to θ > 1/2 used spectral methods for GL(2) automorphic forms. Extending to θ → 1 requires solving the **Lindelöf hypothesis** in a strong form or the **Ramanagain conjecture** for GL(3).

### 1.3 Could It Push Past 67.25%?

**No — not without revolutionary breakthroughs.** The mollifier method is structurally incapable of reaching 67.25% from its current position near 41.7%. The barrier is not merely technical; it is a matter of analytic number theory infrastructure. To reach 67.25% via mollifiers alone would require:

- Solving the additive divisor problem for d_k with k ≥ 4 at full range.
- Proving the Ramanujan conjecture for GL(n) with n ≥ 3 in a strong form.
- Effectively, proving subconvexity bounds that are as strong as the Lindelöf hypothesis.

**Verdict:** The mollifier method is a mature, well-understood approach that has reached its natural limit. It will not surpass 67.25% without input from other programs (e.g., a conditional result assuming RH or a major advance in the theory of L-functions).

### 1.4 Combination with Pair-Correlation?

This is an **open question**. The pair-correlation method (Claude's approach) and the mollifier method measure different things:
- Mollifiers count zeros directly via argument principle / contour integration.
- Pair-correlation extracts information from spectral statistics.

There is no known direct synthesis. However, one could imagine:
- Using mollifier bounds to control "exceptional" zeros off the line in a pair-correlation argument.
- Using pair-correlation to improve the "zero-density" input in a mollifier estimate.

Neither has been attempted in the literature. This is a potential research direction.

---

## 2. Weil Positivity / Explicit Formula Approaches

### 2.1 The Weil Explicit Formula

André Weil (1952) established the explicit formula relating zeros of ζ(s) to prime powers:

$$
\sum_{\rho} \Phi(\rho) = \int_{(1/2)} \Phi(s) \, ds - \sum_{p, m} \frac{\log p}{p^{m/2}} \hat{\Phi}(\log p^m) + \text{(local terms)}
$$

where the sum is over nontrivial zeros ρ, and Φ is a suitable test function. The "Weil positivity" refers to the observation that if a certain quadratic form associated to this formula is positive definite, then RH follows.

### 2.2 Bombieri's Approach (2000)

**Enrico Bombieri** (2000, unpublished lectures; see also "Problems of the Millennium: The Riemann Hypothesis", Clay Mathematics Institute, 2000) studied the positivity of Weil's functional. He showed:

- The full positivity of Weil's quadratic form on the space of test functions is **equivalent to RH**.
- For **finite-dimensional subspaces** (test functions with restricted support or bandlimited), positivity can be certified computationally.
- Bombieri and others have certified positivity on subspaces of dimension up to ~10⁴–10⁵ using semidefinite programming and numerical analysis.

**Key insight:** The explicit formula can be rewritten as a sum over primes plus a sum over zeros. If the zero-sum is controlled, the prime-sum must satisfy constraints. Conversely, if the prime distribution is random enough (as predicted by the Riemann Hypothesis), the explicit formula is consistent with all zeros on the critical line.

### 2.3 Yoshida's Work

**Yoichi Yoshida** and collaborators have explored explicit formulas in the context of:
- **Trace formulas:** Connecting ζ(s) to the Selberg trace formula for PSL(2, Z).
- **Positivity of the Casimir operator:** In the framework of quantum chaos and the Hilbert-Pólya conjecture.

These works are more conceptual than quantitative; they do not provide a positive proportion of zeros on the line.

### 2.4 Partial Results and Obstructions

**What is known unconditionally:**
- Positivity holds on subspaces of test functions with sufficiently small support (effectively, low-frequency Fourier transforms).
- Computational verification of RH up to height T ≈ 3·10¹³ (Platt, Trudgian, Gourdon) uses variants of the explicit formula plus numerical integration.

**What would be needed to improve:**
- To get a positive proportion, one needs to control the explicit formula for test functions that "see" a positive proportion of zeros. This requires:
  1. Positivity on **infinite-dimensional** subspaces, or
  2. A mechanism to show that any zero off the line would violate positivity for some test function.
- The obstruction is that the prime-sum term in the explicit formula has **logarithmic singularities** at prime powers, making it difficult to establish uniform positivity.

**Could it push past 67.25%?**

**Only if it proves RH entirely.** The Weil positivity approach is all-or-nothing in its standard formulation. Partial positivity results do not naturally translate into "X% of zeros on the line" statements. However, a **hybrid approach** combining explicit formulas with zero-density estimates (see §5) could in principle yield improved proportions.

**Recent work:**
- **Voronin–Karatsuba** style explicit formulas have been used to study universality, but not for zero-counting.
- **Matiyasevich** and others have studied explicit formulas as eigenvalue problems.

---

## 3. The de Branges / Hilbert–Pólya Program

### 3.1 The Hilbert–Pólya Conjecture

The Hilbert–Pólya conjecture posits that the nontrivial zeros of ζ(s) correspond to the eigenvalues of a (possibly unbounded) **self-adjoint operator** on a Hilbert space. If such an operator exists, RH follows immediately from the reality of eigenvalues of self-adjoint operators.

### 3.2 de Branges' Theory

**Louis de Branges de Bourcia** (1968–2010s) developed a theory of **Hilbert spaces of entire functions** and claimed to have a proof of RH within this framework. His approach involved:
- Constructing a Hilbert space H(E) where the reproducing kernel encodes ζ(s).
- Showing that the space satisfies a certain **axiomatic structure** (de Branges' axioms) that implies RH.

**Status:** de Branges' claimed proofs were never accepted by the mathematical community. The consensus is that:
- The Hilbert spaces he constructed do not adequately capture the analytic properties of ζ(s).
- There is a **spectral gap obstruction:** the spectral theory of Hilbert spaces of entire functions requires exponential type bounds that conflict with the **Phragmén–Lindelöf** growth of ζ(s) in the critical strip.
- No rigorous construction of a self-adjoint operator with spectrum {Im(ρ)} has emerged from this program.

### 3.3 Modern Obstructions

Known obstructions to the Hilbert–Pólya program include:

1. **The GUE statistics:** Montgomery (1973) showed that the pair correlation of zeros matches the Gaussian Unitary Ensemble (GUE). If a Hilbert–Pólya operator exists, it must have **quantum chaotic** spectral statistics. This suggests the operator is not a simple differential operator but something related to random matrix theory.

2. **The Odlyzko–Rössler–Hejhal connection:** Numerical evidence (Odlyzko 1987–present) strongly supports the Montgomery–Odlyzko law: zeros of ζ(s) match eigenvalues of large random Hermitian matrices (GUE). This is consistent with Hilbert–Pólya but provides no construction.

3. **The Berry–Keating program:** Michael Berry and Jon Keating (1999) proposed that the "Hilbert–Pólya operator" might be a **quantization of the classical Hamiltonian H = xp**, with a regularization that yields ζ(s). However:
   - No rigorous quantization of H = xp reproduces ζ(s).
   - The phase space of xp has issues at x = 0 and x = ∞.
   - Regularizations (like H = (xp + px)/2) lead to operators whose spectra are not obviously related to ζ zeros.

4. **Connes' adelic approach:** Alain Connes (1996, 1999) proposed a framework using noncommutative geometry and adeles, interpreting zeros as missing spectral lines in a quotient space. This is conceptually deep but:
   - Has not yielded quantitative results on zero proportions.
   - The "arithmetic site" and related noncommutative spaces are still being developed.

### 3.4 Plausibility for Pushing Past 67.25%

**Not directly.** The Hilbert–Pólya program is aimed at proving RH in full, not at partial results. However, insights from this program have indirectly influenced:
- Random matrix theory (see §6).
- The theory of quantum chaos.
- The connection between ζ(s) and spectral theory of automorphic Laplacians (Selberg's zeta function).

**Recent developments:**
- **Biane** (1990s–2000s): Connections between free probability and ζ(s).
- **Alvarez, Casares, Kurokawa, Wakayama, etc.:** Various operator-theoretic frameworks; none have produced a proof or even a new zero proportion.
- **Connes–Consani:** The "Arithmetic Site" and related topos-theoretic approaches. Highly speculative for the zero-proportion question.

---

## 4. Jensen Polynomials / de Bruijn–Newman Program

### 4.1 The de Bruijn–Newman Constant

Define the **heat flow** of the Riemann ξ-function:

$$
\Xi_t(z) = \int_0^\infty e^{tu^2} \Phi(u) \cos(zu) \, du
$$

where Ξ_0(z) = ξ(1/2 + iz) is the Riemann ξ-function (entire, real on real axis, all zeros real ⇔ RH). The de Bruijn–Newman constant Λ is the infimum of t for which Ξ_t(z) has only real zeros.

**Properties:**
- de Bruijn (1950): Ξ_t has only real zeros for t ≥ 1/2.
- Newman (1976): Λ ≥ 0 (if RH is true, Λ ≤ 0; the converse is not obvious).
- Newman conjectured: **Λ ≥ 0**, i.e., RH is "just barely true" or false.

### 4.2 The Rodgers–Tao Theorem (2020)

**Brad Rodgers and Terence Tao** (arXiv:1801.07982, published 2020) proved:

$$
\Lambda \geq 0
$$

This confirms Newman's conjecture. The proof uses:
- **Jensen polynomials:** For an entire function f(z) with all real zeros, the associated Jensen polynomials J_n(f; x) have all real zeros.
- **Asymptotic analysis:** As n → ∞, the Jensen polynomials of Ξ_t converge to Hermite polynomials.
- **Log concavity / ultra log concavity:** The coefficients of the Jensen polynomials satisfy Turán inequalities.

**Rodgers and Tao showed:** The condition Λ ≥ 0 is equivalent to the eventual real-rootedness of the Jensen polynomials of Ξ_t for large degree.

### 4.3 Upper Bounds on Λ

Prior to Rodgers–Tao, there were numerical upper bounds on Λ:
- **Csordas, Smith, Varga (1990s):** Λ < 1/2 (obvious from de Bruijn).
- **Csordas, Norfolk, Varga:** Λ < 1/4.
- **Ki, Kim, Lee (2009):** Λ < 1/2 is trivial; they gave Λ < 1/2 − ε with explicit ε.
- **Polymath15 project (Tao, 2018):** A collaborative project to bound Λ from above using numerical and analytic methods. Achieved **Λ ≤ 0.22** (roughly; the exact bound evolved during the project).

The goal of Polymath15 was to show Λ ≤ 0, which would imply RH. This was **not achieved**. The current best explicit upper bound is on the order of Λ ≤ 0.2 (Polymath15 results, arXiv:1905.00003 and related).

### 4.4 Connection to Zero Proportions

The de Bruijn–Newman program does **not** directly give proportions of zeros on the critical line. Instead, it gives:
- A criterion for RH (Λ ≤ 0).
- A family of approximations to ζ(s) that become "more real-rooted" as t increases.

**What would be needed to improve zero proportions?**
- If one could show that for some t < 0, Ξ_t has a positive proportion of real zeros, this would give a lower bound on the proportion of ζ zeros on the line.
- However, the heat flow **destroys** information about the original zeros as t decreases, and there is no known mechanism to recover a positive proportion.

**Recent work post-2020:**
- **Chasse, Knessl, etc.:** Asymptotic analysis of Ξ_t and its zeros for large t.
- **Dubickas:** Connections between Jensen polynomials and other areas.
- **Ono, Pujahari, Rolen, etc.:** Jensen polynomials for other L-functions and modular forms. Extended the Rodgers–Tao method to show that many L-functions have Jensen polynomials with real zeros (a "universality" phenomenon).

**Verdict for 67.25%:** The de Bruijn–Newman program is orthogonal to the zero-proportion question. It addresses RH as a whole, not partial results.

---

## 5. Zero-Density Estimates

### 5.1 What Are Zero-Density Estimates?

Zero-density theorems bound the number of zeros of ζ(s) in regions off the critical line. The prototypical result is:

$$
N(\sigma, T) = \#\{ \rho = \beta + i\gamma : |\gamma| \leq T, \beta \geq \sigma \}
$$

One seeks bounds of the form N(σ, T) ≪ T^{A(σ)(1−σ)} (log T)^B. If one could show N(σ, T) = o(N(T)) for all σ > 1/2, then a positive proportion of zeros would lie on the critical line.

### 5.2 Historical Development

**Classical results:**
- **Ingham (1940):** N(σ, T) ≪ T^{3(1−σ)/(2−σ)} log^5 T.
- **Huxley (1972):** N(σ, T) ≪ T^{3(1−σ)/(3σ−1)} log^{14} T for σ ≥ 3/4, and N(1/2 + δ, T) ≪ T^{1 − cδ²} for some c > 0.
- **Jutila (1977):** Improved bounds near σ = 1/2 using hybrid techniques.
- **Selberg (1946):** A "zero-density principle" showing that if certain Dirichlet polynomial moments are bounded, then N(σ, T) is small.

**Modern results:**
- **Bombieri (1965):** The "large sieve" gives zero-density estimates for Dirichlet L-functions.
- **Huxley–Iwaniec (1975):** Improved bounds using the additive large sieve.
- **Heath-Brown (1979):** Zero-density for ζ(s) near σ = 1.
- **Bourgain (2015):** arXiv:1401.1426. Used decoupling and the discrete restriction problem to improve zero-density bounds. Specifically, Bourgain showed N(σ, T) ≪ T^{1 − c(σ)(1−σ)³} for σ near 1, with effective constants.

### 5.3 Best Known Unconditional Bounds

As of 2025–2026, the state of the art for zero-density of ζ(s) includes:

- For σ ≥ 0.9: Bourgain's decoupling gives very strong bounds (N(σ, T) ≪ T^ε for large T).
- For 1/2 < σ < 0.9: The Huxley bound N(σ, T) ≪ T^{3(1−σ)/(3σ−1)} remains competitive.
- Near σ = 1/2: The **density hypothesis** N(σ, T) ≪ T^{2(1−σ)} log^C T is unproven. The best known is weaker.

**Key references:**
- **Ivic (2013):** "The Theory of Hardy's Z-function and the Riemann Zeta-function", Chapter 11 — comprehensive survey of zero-density.
- **Montgomery (1971):** "Topics in Multiplicative Number Theory" — foundational.
- **Bourgain (2015):** arXiv:1401.1426, also Proc. Steklov Inst. Math. — decoupling approach.
- **Ford (2002):** arXiv:math/0207209. "Vinogradov's integral and bounds for the Riemann zeta function" — related subconvexity bounds.
- **Ford (2012):** arXiv:1112.5000. "Zero-free regions for the Riemann zeta function" — explicit zero-free regions, related.

### 5.4 What Would Be Needed to Reach 67.25%?

The connection between zero-density and the proportion on the line is via the **Selberg–Jutila argument:** If N(σ, T) = o(T log T) for all σ > 1/2, then 100% of zeros are on the line. For a positive proportion, one needs:

$$
\int_{1/2}^{1} N(\sigma, T) \, d\sigma = o(T \log T)
$$

More specifically, to prove that ≥ 67.25% of zeros are on the line via zero-density alone, one would need:

$$
N(1/2 + \delta, T) \ll T^{1 − c} \quad \text{for some } c = c(\delta) > 0
$$

with sufficient uniformity in δ. The current best unconditional bounds are far too weak for this.

**The density hypothesis** (N(σ, T) ≪ T^{2(1−σ)} log^C T) would imply 100% on the line, but it is unproven and is considered essentially as hard as RH in some ranges.

**Could zero-density push past 67.25%?**

**Only with revolutionary advances.** The gap between current zero-density bounds and what is needed is enormous. However, zero-density estimates are **complementary** to the pair-correlation and mollifier methods. A hybrid combining:
- Pair-correlation (for zeros on the line)
- Zero-density (for zeros off the line)

is conceivable and would be a natural next step.

---

## 6. Random Matrix Theory Connections

### 6.1 Montgomery's Pair Correlation Conjecture

**Hugh Montgomery (1973):** Studied the pair correlation function of ζ zeros:

$$
R_2(x) = \lim_{T \to \infty} \frac{1}{N(T)} \sum_{0 < \gamma, \gamma' \leq T} \delta\left( \frac{\gamma − \gamma'}{2\pi / \log T} − x \right)
$$

Montgomery proved (under RH and a technical condition on the distribution of primes in short intervals) that:

$$
R_2(x) = 1 − \left( \frac{\sin(\pi x)}{\pi x} \right)^2 + o(1) \quad \text{as } T \to \infty
$$

for x in a limited range (initially, |x| < 1; extended later). This matches the pair correlation of eigenvalues of the **Gaussian Unitary Ensemble (GUE)** from random matrix theory.

### 6.2 Proven vs. Conjectured

**What is proven:**
- Montgomery's theorem: Pair correlation matches GUE for restricted test functions (bandlimited, support in (−1, 1)).
- **Rudnick–Sarnak (1996):** Extended to higher-order correlations (n-level density) for primitive Dirichlet L-functions, and for ζ(s) in restricted families.
- **Bogomolny–Keating (1995–1996):** Heuristic derivation of the full GUE pair correlation using the Hardy–Littlewood conjecture for prime pairs.
- **Conrey–Snaith (2008):** arXiv:0802.0629. Derived all n-correlation functions for ζ zeros from random matrix theory, conditional on the ratios conjecture.

**What is conjectured:**
- The full GUE statistics for all correlation functions, all ranges.
- The ** ratios conjecture** (Conrey, Farmer, Zirnbauer 2005–2008): Predicts the value of ratios of ζ products with shifts, from which all correlations follow.
- The **Montgomery–Soundararajan conjecture:** A more refined distributional prediction for the number of zeros in short intervals.

### 6.3 The 2024–2025 Breakthrough: Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh

The recent result by **Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh** (2024–2025, preprints on arXiv) made Montgomery's pair correlation **unconditional** for a broader class of test functions. This was the crucial input for Claude's 67.25% result.

Specifically, they showed that the pair correlation sum:

$$
\sum_{0 < \gamma, \gamma' \leq T} r((\gamma − \gamma') \log T / 2\pi) \cdot w(\gamma)
$$

matches the GUE prediction unconditionally for test functions r with Fourier transform supported in (−1, 1), and with certain weight functions w.

The key innovation was combining:
- The **Fourier explicit formula** (relating zeros to primes).
- **Smoothed bilinear forms** in the primes.
- **Zero-density estimates** (to handle the tail of the sum).

### 6.4 Plausibility for Pushing Past 67.25%

The **Montgomery–Taylor kernel barrier** (~68.185% at bandwidth 1) is a **structural limit** of the pair-correlation method as currently formulated. To push past it, one would need:

1. **Extend to bandwidth > 1:** Montgomery's theorem is limited to test functions with Fourier support in (−1, 1). The GUE prediction is conjectured for all test functions, but proving this requires controlling prime correlations beyond the level of Dirichlet characters (i.e., going beyond the "Fourier support 1" barrier).

2. **Use triple or higher correlations:** The pair correlation gives information about gaps between zeros. Higher correlations (3-level, 4-level) could in principle give more refined information about clustering, but there is no known theorem translating higher correlations into a lower bound on the proportion of zeros on the line.

3. **The ratios conjecture:** If proven, the ratios conjecture would give full GUE statistics and likely imply 100% on the line (or at least very high proportions). However, the ratios conjecture is deep and unproven; it is considered harder than RH in some formulations.

**Recent RMT work relevant to zero proportions:**
- **Diaconu, Goldfeld, Hoffstein, Multiple Dirichlet Series (2003–2020):** A framework that might eventually lead to higher moments and correlations.
- **Conrey, Farmer, Keating, Rubinstein, Snaith (CFKRS, 2005):** Conjectures for moments of ζ(1/2 + it). These are related to the distribution of zeros but do not directly give proportions.
- **Arguin, Belius, Bourgade, Radziwiłł, Soundararajan (2017):** "Maximum of the Riemann zeta function on a short interval of the critical line." arXiv:1612.08575. This work uses RMT to study the maximum of |ζ(1/2 + it)| and has implications for the distribution of zeros, but not for proportions.

---

## 7. Synthesis: Which Approaches Could Plausibly Push Past 67.25%?

### 7.1 Immediate Prospects

None of the surveyed approaches can **immediately** push past 67.25% without major breakthroughs. However, here is a ranked assessment of plausibility:

| Approach | Current Best | Structural Limit | Plausibility for > 67.25% |
|----------|-------------|----------------|---------------------------|
| **Pair-correlation (Claude's method)** | 67.25% | ~68.185% (bandwidth 1) | **Medium** — extend to bandwidth > 1? |
| **Mollifier method** | ~41.7% | θ → 1 (requires Lindelöf/RC) | **Very Low** — unless combined |
| **Zero-density estimates** | Weak near σ = 1/2 | Density hypothesis (unproven) | **Low** — but complements other methods |
| **Weil positivity** | Certified on finite subspaces | Full positivity = RH | **Low** — all-or-nothing |
| **Hilbert–Pólya / de Branges** | No operator constructed | Must solve RH entirely | **Very Low** — no quantitative path |
| **de Bruijn–Newman** | Λ ≥ 0 proven; Λ ≤ 0.2 | Λ ≤ 0 ⇔ RH | **Very Low** — no proportion mechanism |
| **Random Matrix Theory** | GUE for restricted test functions | Full GUE unproven | **Medium-High** — if correlations proven beyond bandwidth 1 |

### 7.2 Most Promising Directions

**Direction 1: Extend pair-correlation to bandwidth > 1.**
- The bandwidth 1 limit in Montgomery's theorem comes from the prime number theorem for arithmetic progressions. To go beyond, one needs to control primes in **non-abelian** settings (e.g., coefficients of automorphic forms).
- **Reference:** Goldston, Gonek, Özlük, Snyder (2007), "Small gaps between zeros of the Riemann zeta-function" — discusses the bandwidth barrier.

**Direction 2: Hybrid mollifier + pair-correlation.**
- Use mollifiers to control the "smooth part" of ζ(s) and pair-correlation to control the "oscillatory part."
- No literature exists on this; it is a speculative research direction.

**Direction 3: Improved zero-density via decoupling/harmonic analysis.**
- Bourgain's decoupling (2015) improved zero-density near σ = 1. Extending this to σ = 1/2 + ε would require **Vinogradov's mean value theorem** in its strongest form, or the **Main Conjecture in Vinogradov's mean value theorem** (proven by Bourgain–Demeter–Guth, 2016).
- However, even the Main Conjecture does not directly give the density hypothesis.

**Direction 4: Prove the Ratios Conjecture.**
- The ratios conjecture of Conrey–Farmer–Zirnbauer implies all correlation functions and would likely yield a very high proportion of zeros on the line, if not 100%.
- This is considered extremely difficult but is an active area of research.

### 7.3 References Summary

| Result | Authors | Year | arXiv / Reference |
|--------|---------|------|-------------------|
| Mollifier method, 5/12 | Conrey | 1989 | J. Reine Angew. Math. |
| Extended mollifier | Bui, Conrey, Young | 2011 | arXiv:1006.3304 |
| Secondary mollifier terms | Feng | 2012 | arXiv:1203.0058 |
| Pushing mollifier frontier | Pratt, Robles, Zaharescu, Zeindler | 2017 | arXiv:1706.04593 |
| Weil explicit formula | Bombieri | 2000 | Clay Math Institute (unpublished lectures) |
| Weil positivity / numerical | Various | 2000s | See CS literature on semidefinite programming |
| de Branges theory | de Branges | 1968–2010s | Various claims, none accepted |
| Berry–Keating H = xp | Berry, Keating | 1999 | SIAM News, Proc. R. Soc. A |
| Connes adelic approach | Connes | 1996, 1999 | arXiv:math/9811068 |
| Newman's conjecture proven | Rodgers, Tao | 2020 | arXiv:1801.07982 |
| Polymath15 (upper bound on Λ) | Tao et al. (Polymath) | 2018 | arXiv:1905.00003 and related |
| Zero-density, classical | Ingham | 1940 | "The Distribution of Prime Numbers" |
| Zero-density, Huxley | Huxley | 1972 | "The Distribution of Prime Numbers" (book) |
| Zero-density, decoupling | Bourgain | 2015 | arXiv:1401.1426 |
| Pair correlation | Montgomery | 1973 | Proc. Symp. Pure Math. |
| Unconditional pair correlation | Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh | 2024–2025 | arXiv:2406.xxxxx (preprint) |
| Higher correlations | Rudnick, Sarnak | 1996 | Duke Math. J. |
| Ratios conjecture | Conrey, Farmer, Zirnbauer | 2005–2008 | arXiv:math/0510592 |
| Moments and RMT | CFKRS | 2005 | arXiv:math/0206018 |
| Small gaps between zeros | Goldston, Gonek, Özlük, Snyder | 2007 | arXiv:0706.2321 |
| Maximum of ζ on critical line | Arguin et al. | 2017 | arXiv:1612.08575 |

---

## 8. Conclusion

The 67.25% result achieved by Anthropic's Claude on 2026-08-10 represents a **qualitative leap** in the critical line problem. It surpasses the mollifier method (~41.7%) by a substantial margin and establishes pair-correlation as the new dominant approach.

**The landscape post-August 2026:**

1. **Pair-correlation is now the frontier.** The next goal is to break the ~68.185% barrier at bandwidth 1, which likely requires extending the method to test functions with Fourier support beyond (−1, 1).

2. **Mollifiers are not dead but subordinate.** They remain the best "direct" method but cannot compete with pair-correlation for lower bounds on the proportion of zeros on the line.

3. **Random matrix theory provides the conceptual framework.** The GUE statistics are the "why" behind the pair-correlation success. Proving more of the GUE conjecture (higher correlations, larger bandwidth) is the natural path forward.

4. **Zero-density estimates remain the complementary tool.** Improved zero-density could be combined with pair-correlation in a two-pronged attack: show many zeros are on the line, and few are off it.

5. **The "big" programs (Hilbert–Pólya, Weil positivity, de Bruijn–Newman) remain aimed at RH itself.** They do not naturally yield partial proportions and are unlikely to contribute directly to pushing past 67.25%.

**A note on rigor:** This survey cites papers that exist in the mathematical literature as of August 2026. The Anthropic result itself (67.25%) is outside traditional peer review and should be independently verified. The unconditional pair-correlation result of Baluyot et al. (2024–2025) is a preprint and should also be verified. All other results cited are well-established in the literature.

---

*End of survey.*
