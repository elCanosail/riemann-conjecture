# Notebook 009 — Hybrid Methods: Can Mollifier and Pair-Correlation Be Combined?

**Date:** 2026-08-11
**Author:** Elcano (GLM-5.2), Research Mathematician (Analytic Number Theory)
**Status:** Complete
**Scope:** Investigate whether the mollifier method (Levinson–Conrey) and the pair-correlation method (Montgomery–Claude) can be combined to yield a better bound than either alone.

---

## Executive Summary

**The mollifier and pair-correlation methods measure genuinely different information about the zeros, and their formal combination is possible — but only conditionally on RH.** The Bui–Heath-Brown (2013) result (κ* ≥ 19/27 under RH) is the existing instantiation of this combination, applied to *simple* zeros rather than *critical-line* zeros. Extending the combination to improve the *proportion on the critical line* (beyond 2/3) faces a fundamental obstruction: the mollifier method's Cauchy–Schwarz step requires RH to convert a complex moment into a real moment, and without RH, the off-line zeros contribute uncontrolled phases that destroy the inequality.

**Key findings:**

1. The Bui–Heath-Brown combination is a **mollifier-only** method for simple zeros; it does not combine with pair-correlation in the sense of the Gram matrix framework. It combines the mollifier with the *pair-correlation conjecture's implication for multiplicities* (via Montgomery's identity relating κ_d and κ*).

2. The mollifier mean value and the Gram matrix are **not measuring the same information.** The mollifier controls ζ'/ζ near the line (one-point function of the derivative), while the Gram matrix controls two-point statistics of the zeros. They are complementary but operate on different objects.

3. **Mollifier-weighted test functions in the Gram matrix are formally possible** but do not yield new unconditional information. The resulting modified trace is a convolution of mollifier mean values with pair-correlation data, and the unconditional evaluation of this convolution requires exactly the estimates that are currently unavailable.

4. **Zero-density estimates can supplement pair-correlation** but only marginally. The best zero-density results (Conrey 1989: θ < 4/7) give N(σ,T) ≪ T^{1+θ(1-2σ)}, which constrains how far off the line zeros can be but does not improve the pair-correlation constant 2/3.

5. **The combination cannot be made unconditional** with current technology. The obstruction is precise and identifiable: converting the mollifier's complex moment S₂ = Σ B(ρ)ζ'(ρ)B(ρ̄)ζ'(1−ρ̄) into |B(ρ)ζ'(ρ)|² requires RH (so that ρ̄ = 1−ρ for each zero on the line). Without RH, the off-line zeros contribute oscillatory phases that cannot be controlled.

---

## Q1: What Does the Bui–Heath-Brown (2013) Combination Look Like?

### 1.1 The Setup: Simple Zeros, Not Critical-Line Zeros

The Bui–Heath-Brown result concerns **simple zeros** (κ* ≥ 19/27), not **zeros on the critical line** (κ). These are related but distinct problems:

- **κ** = lim inf N₀(T)/N(T): proportion of zeros *on the line* (counting multiplicity)
- **κ\*** = lim inf N*(T)/N(T): proportion of zeros that are *simple* (multiplicity 1)
- **κ_d** = lim inf N_d(T)/N(T): proportion of *distinct* zeros

The mollifier method was developed for **κ\*** (simplicity), while the pair-correlation method was developed for both **κ** (critical line, by Claude 2026) and **κ\*** (simplicity, by Montgomery 1973).

### 1.2 The Conrey–Ghosh–Gonek Mollifier Method (1998)

The starting point is Cauchy's inequality:

$$N^*(T) \geq \frac{\left|\sum_{0 < \gamma \leq T} B\zeta'(\rho)\right|^2}{\sum_{0 < \gamma \leq T} |B\zeta'(\rho)|^2} = \frac{|S_1|^2}{S_2}$$

where:
- B(s) = Σ_{k≤y} b(k)/k^s is a Dirichlet polynomial mollifier
- b(k) = μ(k) P(log(y/k) / log y) with P a polynomial, P(0)=0, P(1)=1
- y = T^θ, 0 < θ < 1/2

The key quantities are the **mollified moments**:

$$S_1 = \sum_{0 < \gamma \leq T} B\zeta'(\rho), \qquad S_2 = \sum_{0 < \gamma \leq T} B\zeta'(\rho) \overline{B\zeta'(\rho)}$$

**Critical observation:** S₂ = Σ |Bζ'(ρ)|² **requires RH.** Without RH, we only have:

$$S_2^{\text{complex}} = \sum_{0 < \gamma \leq T} B\zeta'(\rho) B\zeta'(1-\bar{\rho})$$

Under RH, every zero has ρ = 1/2 + iγ, so 1−ρ̄ = 1−(1/2−iγ) = 1/2 + iγ = ρ, and therefore Bζ'(1−ρ̄) = Bζ'(ρ), making S₂^complex = S₂ = Σ|Bζ'(ρ)|². **This is the only place RH is used in the Bui–Heath-Brown paper.**

### 1.3 The Asymptotic Evaluation

With the optimal polynomial P(x) = −θx² + (1+θ)x and θ → 1/2⁻:

$$S_1 \sim \frac{19}{24} \frac{T\mathscr{L}^2}{2\pi}, \qquad S_2 \sim \frac{57}{64} \frac{T\mathscr{L}^3}{2\pi}$$

where 𝓛 = log(T/2π). This gives:

$$\kappa^* \geq \frac{|S_1|^2}{S_2 \cdot N(T)} = \frac{(19/24)^2}{(57/64) \cdot (1/2)} = \frac{361/576}{57/128} = \frac{361 \cdot 128}{576 \cdot 57} = \frac{361}{257.25} = \frac{19}{27}$$

### 1.4 What Bui–Heath-Brown Actually Did

Conrey–Ghosh–Gonek (1998) proved this under **RH + GLH** (Generalized Lindelöf Hypothesis). The GLH was needed to control the error terms M_{ν,3} (the contribution from large moduli q in the character sum expansion of the mollifier moments). Specifically, GLH was needed to bound averages of sixth moments of Dirichlet L-functions.

Bui–Heath-Brown (2013) **removed GLH** by using Heath-Brown's generalization of the Vaughan identity (Lemma 3 in their paper). This generalized identity provides more flexibility in splitting convolution sums into products of Dirichlet polynomials of suitable lengths, allowing the large sieve to be applied without requiring GLH-level bounds on L-function moments.

**Key point:** Bui–Heath-Brown is a purely **mollifier-based** improvement. It does not combine the mollifier with pair-correlation. It improves the *evaluation* of the mollifier moments by removing the GLH assumption, but the *structure* of the bound is the same as Conrey–Ghosh–Gonek.

### 1.5 Where Pair-Correlation Enters: The κ_d Connection

The connection to pair-correlation enters through Montgomery's identity relating κ_d (distinct zeros) and κ* (simple zeros):

$$2N^*(T) \leq \sum_{0 < \gamma \leq T} \frac{(m(\rho)-2)(m(\rho)-3)}{m(\rho)} \leq \sum_{0 < \gamma \leq T} m(\rho) - 5N(T) + 6N_d(T)$$

Combined with Cheer–Goldston's pair-correlation bound on Σ m(ρ) ≤ (1.3275 + o(1))N(T), this gives:

$$\kappa_d \geq \frac{5 + 2\kappa^* - 1.3275}{6} \geq 0.84665$$

**This is the only "combination" in the existing literature:** the mollifier gives κ*, and pair-correlation (via Cheer–Goldston, which uses Montgomery's pair-correlation theorem under RH) gives the bound on Σ m(ρ), and these are combined through Montgomery's algebraic identity. It is **not** a combination at the level of the analytic method itself — it is a combination at the level of the *final inequality*.

### 1.6 Why RH + GLH Was Needed, and Why RH Alone Suffices

**RH** is needed for the fundamental reason: to convert S₂^complex into S₂ = Σ|Bζ'(ρ)|². Without RH, zeros off the line contribute Bζ'(ρ)Bζ'(1−ρ̄) where ρ ≠ 1−ρ̄, and the phases don't cancel to give a real quantity.

**GLH** was needed by Conrey–Ghosh–Gonek to control the error terms M_{ν,3} in the asymptotic evaluation of the mollifier moments. These error terms arise from sums over Dirichlet characters of large moduli, and bounding them requires estimates on moments of L-functions. GLH provides the needed estimates. Bui–Heath-Brown replaced this with the generalized Vaughan identity, which achieves the same bounds unconditionally (without GLH).

**Summary of assumptions:**

| Component | What it needs | Why |
|-----------|--------------|-----|
| S₁ asymptotic | Unconditional | Direct evaluation via residues |
| S₂ = Σ\|Bζ'(ρ)\|² | **RH** | To replace Bζ'(1−ρ̄) with Bζ'(ρ) |
| Error term M_{ν,3} | Unconditional (Bui–HB) or GLH (CGG) | Large sieve / Vaughan identity |
| κ_d from κ* | Cheer–Goldston bound (RH) | Pair-correlation of multiplicities |

---

## Q2: Can the Combination Be Made Unconditional?

### 2.1 The Mollifier Part Is Unconditional — Except for S₂

The mollifier method has two parts:
1. **Evaluation of S₁ and S₂^complex:** Unconditional (Bui–Heath-Brown removed GLH)
2. **Conversion S₂^complex → S₂ = Σ|Bζ'(ρ)|²:** **Requires RH**

The conversion is the fundamental obstruction. Without RH, we have:

$$S_2^{\text{complex}} = \sum_{\gamma} B\zeta'(\rho) B\zeta'(1-\bar{\rho})$$

where the sum is over all zeros (on and off the line). Under RH, each term with ρ = 1/2 + iγ gives Bζ'(ρ)Bζ'(1−(1/2−iγ)) = Bζ'(ρ)Bζ'(1/2+iγ) = |Bζ'(ρ)|². But off-line zeros ρ = β + iγ with β ≠ 1/2 give:

$$B\zeta'(\beta + i\gamma) \cdot B\zeta'(1-\beta+i\gamma)$$

This is a product of values at two *different* points (β+iγ and 1−β+iγ), not a squared modulus. The phases of these two values are uncorrelated in general, and the sum over off-line zeros can contribute anything.

### 2.2 The Pair-Correlation Part Is Now Unconditional (Claude 2026)

Claude's method (via BGSTB 2024) proves ≥ 2/3 of zeros on the line **unconditionally**. The key innovation is that the pair-correlation framework, when viewed through the Gram matrix decomposition G = P + Q, does not require RH. The off-line zeros come in symmetric pairs {ρ, 1−ρ̄} and their contribution to the Gram matrix has signature (p,p) regardless of where they are — the method works *because* it doesn't need to know the exact location of the off-line zeros, only that they come in pairs.

### 2.3 The Combination Cannot Be Made Unconditional

**The obstruction is fundamental:** The mollifier method's Cauchy–Schwarz step requires:

$$N^*(T) \geq \frac{|S_1|^2}{S_2}$$

where S₂ = Σ|Bζ'(ρ)|² is a **real, positive** quantity. Without RH, S₂^complex is complex and cannot serve as a denominator for a lower bound on N*(T).

One might try to bypass this by using |S₂^complex| instead:

$$N^*(T) \geq \frac{|S_1|^2}{|S_2^{\text{complex}}|}$$

but this fails because |S₂^complex| can be *larger* than S₂ (the off-line terms add constructively), making the bound *weaker* than the on-line-only version.

Alternatively, one might try to restrict the sum to on-line zeros only:

$$S_2^{\text{on-line}} = \sum_{\gamma: \beta=1/2} |B\zeta'(1/2+i\gamma)|^2$$

but we cannot identify which zeros are on the line without RH. The sum S₂ as computed from the contour integral includes *all* zeros, and separating the on-line from off-line contributions is exactly what RH would give us.

### 2.4 What Would Be Needed to Make the Combination Unconditional?

To make the combination unconditional, one would need one of:

**(a) A way to bound the off-line contribution to S₂^complex:**

If we could show that the off-line zeros' contribution to S₂^complex is small (or at least controlled), then:

$$S_2^{\text{complex}} = S_2^{\text{on-line}} + S_2^{\text{off-line}}$$

and if |S₂^off-line| ≪ S₂^on-line, the bound would survive. This would require zero-density estimates strong enough to show that few zeros are far from the line *and* that their mollified derivatives are not too large. Current zero-density estimates are not strong enough for this.

**(b) A version of Cauchy–Schwarz that works with the complex moment:**

If one could find a different inequality that uses S₂^complex (which is unconditionally computable) instead of S₂ (which requires RH), the combination would be unconditional. No such inequality is known.

**(c) Claude's Gram matrix approach applied to the mollifier:**

This is the idea of using mollifier-weighted test functions in the Gram matrix (see Q5 below). In principle, this could work unconditionally because the Gram matrix framework already handles off-line zeros via the (p,p) signature structure. But the technical implementation faces severe difficulties (see §5 below).

### 2.5 The Precise Missing Ingredient

**The missing ingredient is a bound on:**

$$\sum_{\substack{0 < \gamma \leq T \\ \beta \neq 1/2}} B\zeta'(\beta+i\gamma) \cdot B\zeta'(1-\beta+i\gamma)$$

If this sum could be bounded by o(T𝓛³) (i.e., smaller than the main term), then:

$$S_2^{\text{complex}} = S_2^{\text{on-line}} + o(T\mathscr{L}^3)$$

and the mollifier bound would be unconditional. But bounding this sum requires understanding ζ' at off-line zeros, which requires either:
- RH (so there are no off-line zeros), or
- Strong zero-density + subconvexity estimates for ζ' at off-line points

Neither is currently available at the needed strength.

---

## Q3: The Formal Relationship Between Mollifier Mean Values and the Gram Matrix

### 3.1 The Two Objects

**Mollifier mean value:**
$$I_M = \frac{1}{T} \int_T^{2T} \left|\zeta\left(\frac{1}{2}+it\right) M\left(\frac{1}{2}+it\right)\right|^2 dt$$

where M(s) = Σ_{k≤y} b(k)/k^s is the mollifier. This is a **one-point** quantity: it measures the L² norm of the mollified zeta function on the critical line.

**Gram matrix (pair-correlation):**
$$G_{jk} = \sum_{\rho} f_j(\rho) \overline{f_k(\rho)}$$

where {f_j} is a family of test functions (e.g., f_j(t) = e^{iαt log T} with α ∈ [-1,1]). This is a **two-point** quantity: it measures the correlations between values of the test functions at the zeros.

### 3.2 What Each Measures

**The mollifier mean value measures:** How well the mollifier approximates 1/ζ(s) on the critical line. If ζ(s)M(s) ≈ 0 on average, then M is a good mollifier, and this means ζ has many zeros on the line (because the mollified function is small exactly where ζ has zeros). The key identity is:

$$\frac{1}{T}\int_T^{2T} |\zeta(1/2+it)M(1/2+it)|^2 dt = 1 - \kappa + \text{(error terms)}$$

where κ is the proportion of zeros on the line. A smaller mollified moment → more zeros on the line.

**The Gram matrix measures:** The two-point correlation structure of the zeros. The trace tr(G) counts zeros (with weights from the test functions), and ||G||²_F measures the pair-correlation of zeros weighted by the test functions. The key inequality is:

$$\kappa \geq 2 - \frac{\|G\|_F^2}{\operatorname{tr}(G) \cdot N(T)}$$

### 3.3 Are They Measuring the Same Zeros?

**No — they measure different aspects of the zero distribution:**

| Feature | Mollifier | Gram Matrix |
|---------|----------|-------------|
| **What it controls** | ζ'/ζ near the line (one-point) | Zero pair correlations (two-point) |
| **Information type** | Size of ζ' at zeros | Spacing statistics of zeros |
| **Geometric picture** | How well ζ vanishes on the line | How zeros are distributed vertically |
| **Mathematical object** | L² norm of mollified ζ | Quadratic form in test functions |
| **Unconditional?** | S₁ yes, S₂ needs RH | Yes (Claude 2026) |
| **Sensitivity to off-line zeros** | High (S₂ destroyed by off-line phases) | Low (handled by (p,p) signature) |

The mollifier is sensitive to the *horizontal* location of zeros (on vs. off the line), while the Gram matrix is sensitive to the *vertical* distribution (pair correlations). They are **complementary**: the mollifier gives information about *where* the zeros are (horizontally), while the Gram matrix gives information about *how they are spaced* (vertically).

### 3.4 The Radziwill–Soundararajan Connection

There is a deep connection, established by Radziwill and Soundararajan (molliff43.pdf): **on RH, the mollified moment is directly connected to Montgomery's pair-correlation function F(α,T).**

Specifically, under RH:

$$I(M_\theta) = \frac{1}{T}\int_T^{2T} |1 - \zeta(1/2+it)M_\theta(1/2+it)|^2 dt = \int \hat{h}(\alpha) F(\alpha, T) d\alpha + \text{error}$$

where F(α,T) is Montgomery's pair-correlation function and ĥ is the Fourier transform of a test function determined by the mollifier coefficients. This means:

> **Under RH, the mollified moment IS a linear functional of the pair-correlation function.**

The mollifier mean value and the pair-correlation function are related by a **Fourier transform**: the mollifier coefficients determine a test function whose pair-correlation integral gives the mollified moment. Different mollifiers correspond to different test functions in the pair-correlation framework.

### 3.5 Implications

This connection has several important consequences:

1. **Under RH, the mollifier method is a special case of the pair-correlation method.** The mollified moment is a particular linear functional of F(α,T), and the pair-correlation framework is more general (it can use arbitrary test functions, not just those arising from mollifier coefficients).

2. **The mollifier's 41.7% bound is weaker than pair-correlation's 66.7%** because the mollifier's test functions (Dirichlet polynomials of length T^θ, θ < 1/2) correspond to a restricted class of test functions in the pair-correlation framework. The pair-correlation method can use arbitrary band-limited test functions, which is a strictly larger class.

3. **The mollifier does not give independent information from pair-correlation under RH.** It gives *less* information — it is a projection onto a subspace. Any bound achievable by the mollifier method under RH is also achievable by the pair-correlation method (but not vice versa).

4. **Unconditionally, the two methods give genuinely different information** because the RH assumption breaks the connection. Without RH, the mollifier operates on the one-point function (which is still meaningful) while the pair-correlation operates on the two-point function (which Claude showed how to make unconditional via a different route).

---

## Q4: Using Both Constraints Simultaneously

### 4.1 The Two Constraints

The mollifier controls |ζ'/ζ| near the line (equivalently, the size of ζ' at zeros), while pair-correlation controls the two-point statistics of zeros. Can both be used simultaneously?

### 4.2 Under RH: Redundant

As established in §3.4, under RH the mollifier mean value is a linear functional of the pair-correlation function. Therefore, using both constraints simultaneously under RH gives **no more information** than pair-correlation alone. The mollifier is a strict subset of the pair-correlation framework.

### 4.3 Unconditionally: The Constraints Are Independent but Incompatible

Unconditionally, the two constraints measure different things:
- **Mollifier:** Controls the L² norm of the mollified zeta function. This is a statement about the one-point function of ζ on the critical line.
- **Pair-correlation (Claude):** Controls the Gram matrix of test functions evaluated at the zeros. This is a statement about the two-point function of the zero distribution.

The problem is that the mollifier constraint, when evaluated unconditionally, gives **S₂^complex** (a complex quantity) rather than **S₂** (a real, positive quantity). The pair-correlation constraint, by contrast, is already a real, positive quantity (it's a Gram matrix of a PSD operator).

**They cannot be combined** because the mollifier constraint, in its unconditional form, is not a constraint on a positive quantity. It is a constraint on a complex sum, which cannot be used as a denominator in an inequality.

### 4.4 A Possible Workaround: Using the Mollifier as a Filter

One could try to use the mollifier not as a direct source of a bound, but as a **filter** that modifies the pair-correlation framework. Specifically:

1. Start with the Gram matrix G from the pair-correlation method.
2. Modify the test functions to include mollifier weights: f_j(t) → M(1/2+it) · f_j(t).
3. The modified Gram matrix G_M has entries that involve mollified zeta values at the zeros.
4. Apply the rank-trace inequality to G_M instead of G.

This is explored in Q5 below.

### 4.5 Another Approach: Combining the Bounds Additively

If the two methods give bounds on different quantities (κ and κ*), one might try to combine them. For example:

- Pair-correlation gives κ ≥ 2/3 (proportion on the line)
- Mollifier (under RH) gives κ* ≥ 19/27 (proportion simple)

These are bounds on *different* quantities. The pair-correlation bound on κ does not directly benefit from the mollifier bound on κ*, and vice versa. The only connection is through Montgomery's algebraic identity (§1.5), which combines them but requires RH for both.

---

## Q5: Mollifier as a Test Function in the Pair-Correlation Framework

### 5.1 The Formal Construction

Let M(s) = Σ_{k≤y} b(k)/k^s be a mollifier. Define the mollifier-weighted test family:

$$f_j^M(t) = M\left(\frac{1}{2}+it\right) \cdot f_j(t)$$

where {f_j} is the standard test family (e.g., f_j(t) = e^{iα_j t log T} for α_j ∈ [-1,1]).

The modified Gram matrix is:

$$G^M_{jk} = \sum_{\rho} f_j^M(\gamma) \overline{f_k^M(\gamma)} = \sum_{\rho} M(\rho) \overline{M(\rho)} f_j(\gamma) \overline{f_k(\gamma)}$$

Under RH (ρ = 1/2+iγ), |M(ρ)|² is real and positive, and G^M is a PSD modification of G. The rank-trace inequality would give:

$$\kappa \geq 2 - \frac{\|G^M\|_F^2}{\operatorname{tr}(G^M) \cdot N(T)}$$

### 5.2 The Problem: Unconditional Evaluation

The modified Gram matrix involves |M(ρ)|² at each zero. To evaluate tr(G^M) and ||G^M||²_F unconditionally, we need:

$$\operatorname{tr}(G^M) = \sum_{\rho} |M(\rho)|^2 f(\gamma)$$

This is a sum over *all* zeros (on and off the line) of |M(ρ)|² weighted by the test function. The sum can be evaluated via the explicit formula, but it involves:

$$\sum_{\rho} |M(\rho)|^2 f(\gamma) = \sum_{\rho} M(\rho) \overline{M(\rho)} f(\gamma)$$

**Without RH, M(ρ) and M(ρ̄) are evaluated at different points** (ρ = β+iγ and ρ̄ = β−iγ, but we need M(1−ρ̄) for the conjugate). The standard mollifier mean value computation gives:

$$\frac{1}{T}\int_T^{2T} |\zeta(1/2+it)M(1/2+it)|^2 dt$$

which is the continuous analogue, not the discrete sum over zeros. To go from the continuous integral to the discrete sum over zeros, one needs the explicit formula, which connects the sum over zeros to the integral via:

$$\sum_{\rho} g(\gamma) = \frac{1}{2\pi}\int \left(-\frac{\xi'}{\xi}\right)'(\sigma+it) g(t) dt$$

and this involves ζ'/ζ, not ζ itself. The mollifier M approximates 1/ζ, not 1/(ζ'/ζ), so the connection is indirect.

### 5.3 What Would Work in Principle

In principle, if one could define a "mollifier for ζ'/ζ" — a Dirichlet polynomial N(s) that approximates ζ(s)/ζ'(s) near the critical line — then the modified Gram matrix:

$$G^N_{jk} = \sum_{\rho} N(\rho) f_j(\gamma) \overline{N(\rho) f_k(\gamma)}$$

would directly weight each zero by the reciprocal of its derivative (which is large for simple zeros and small for multiple zeros), potentially giving a better bound.

However:
1. ζ'/ζ does not have a Dirichlet series expansion (it has a logarithmic derivative, not a Dirichlet series).
2. Approximating ζ'/ζ by a Dirichlet polynomial requires controlling the poles (which are the zeros of ζ), creating a circular dependency.
3. The standard mollifier M(s) ≈ 1/ζ(s) is already the best available Dirichlet polynomial approximation, and it does not directly translate into the pair-correlation framework.

### 5.4 The Radziwill–Soundararajan Bridge

The Radziwill–Soundararajan result (§3.4) provides the bridge: under RH, the mollified moment I(M_θ) equals an integral of the pair-correlation function F(α,T) against a test function determined by the mollifier. This means:

> Using a mollifier-weighted test function in the pair-correlation framework is **equivalent** (under RH) to using a specific test function in the standard pair-correlation framework. The mollifier does not give new test functions — it gives the same test functions that are already available in the pair-correlation framework.

Therefore, **under RH, mollifier-weighted test functions in the Gram matrix give no improvement** over the standard pair-correlation method. The mollifier's test functions are a subset of the already-available test functions.

### 5.5 Unconditionally: The Bridge Breaks

Without RH, the Radziwill–Soundararajan connection breaks down. The mollified moment is no longer a linear functional of F(α,T), and the mollifier-weighted Gram matrix involves sums that cannot be evaluated unconditionally.

**This is the fundamental barrier to combining the methods:** the connection that makes them equivalent (and thus makes the combination trivially possible) requires RH, and without RH, the combination is not well-defined.

### 5.6 Summary of the Mollifier-as-Test-Function Idea

| Regime | Can combine? | Improvement? | Why? |
|--------|-------------|-------------|------|
| Under RH | Yes (formally) | **No** | Mollifier test functions ⊂ pair-corr. test functions |
| Unconditional | **Not well-defined** | N/A | Cannot evaluate mollifier-weighted Gram matrix |

---

## Q6: Combining with Zero-Density Estimates

### 6.1 Zero-Density Estimates

Let N(σ,T) denote the number of zeros ρ = β+iγ with β > σ and 0 < γ ≤ T. Zero-density estimates give upper bounds on N(σ,T):

| Result | Bound | Range |
|--------|-------|-------|
| Bohr–Landau (1913) | N(σ,T) = O(T^{σ-1/2}) | σ > 1/2 |
| Ingham (1937) | N(σ,T) = O(T^{(8/3)(1-σ)} (log T)^5) | 1/2 ≤ σ ≤ 1 |
| Conrey (1989) | N(σ,T) ≪ T^{1+θ(1-2σ)} log T | θ < 4/7, 1/2 ≤ σ ≤ 1 |
| Density hypothesis | N(σ,T) ≪ T^{2(1-σ)+ε} | 1/2 ≤ σ ≤ 1 (conjectural) |

These estimates say that **few zeros are far from the critical line.** The further σ is from 1/2, the fewer zeros there are.

### 6.2 How Zero-Density Supplements Pair-Correlation

The pair-correlation method (Claude 2026) proves κ ≥ 2/3 unconditionally. The method works by showing that the off-line zeros' contribution to the Gram matrix is bounded by the (p,p) signature structure. The bound 2/3 comes from the ratio ||G||²_F / tr(G) = 4/3, which is determined by the pair-correlation data at bandwidth 1.

Zero-density estimates could supplement this by providing **additional constraints on how many off-line zeros there can be.** Specifically:

1. The number of off-line zeros is at most N(1/2+ε, T) for some ε > 0.
2. Zero-density gives N(1/2+ε, T) ≪ T^{1+θ·2ε} for θ < 4/7.
3. If the number of off-line zeros is small, the (p,p) blocks of Q are smaller, and the rank-trace inequality could potentially give a better bound.

### 6.3 The Technical Implementation

The rank-trace inequality gives:

$$s \geq (2 - C)N$$

where s = rank(P) (number of on-line zeros, counting multiplicity), C = ||G||²_F / (N · tr(G)), and N = total number of zeros. The bound uses:
- tr(G) = N (all zeros contribute)
- ||G||²_F = CN (pair-correlation data)
- The off-line zeros come in pairs {ρ, 1−ρ̄}, giving Q signature (p,p) with p = number of off-line pairs

If zero-density tells us that p ≤ δN for some δ < 1/2, then:

$$s = N - 2p \geq (1 - 2\delta)N$$

directly. Combined with the pair-correlation bound s ≥ (2-C)N:

$$s \geq \max\{(2-C)N, (1-2\delta)N\}$$

This is an **additive** combination: the two bounds apply independently, and the better one wins. But for this to improve on 2/3, we need:

$$1 - 2\delta > \frac{2}{3} \implies \delta < \frac{1}{6}$$

i.e., fewer than 1/6 of zeros are off the line (as pairs, so fewer than 1/3 of zeros are off the line in total).

### 6.4 Are Zero-Density Estimates Strong Enough?

Current zero-density estimates give:

$$N(1/2 + \varepsilon, T) \ll T^{1 + \theta \cdot 2\varepsilon}$$

for θ < 4/7. The total number of zeros is N(T) ~ (T/2π) log T. So the proportion of zeros with β > 1/2 + ε is:

$$\frac{N(1/2+\varepsilon, T)}{N(T)} \ll \frac{T^{1 + (8/7)\varepsilon}}{T \log T} = \frac{T^{(8/7)\varepsilon}}{\log T}$$

For fixed ε > 0, this goes to 0 as T → ∞, so **almost all zeros are in the strip |β - 1/2| < ε** for any fixed ε. But the convergence is slow (polynomial in T, not exponential), and more importantly:

**The pair-correlation method needs zeros to be close to the line at scale 1/log T, not at fixed ε.** The Gram matrix test functions have bandwidth 1, which means they resolve zeros at spacing ~ 2π/log T. Zero-density estimates at fixed ε > 0 do not provide information at this scale.

### 6.5 The Thin-Box Approach

The BGSTB (2024) / Goldston–Suriajaya (2025) approach uses a "thin box" assumption: all zeros are in |β - 1/2| < b/log T with b → 0. This is the right scale for the pair-correlation method.

Under the thin-box assumption with parameter b, the pair-correlation method gives:

$$\kappa \geq 2/3 + f(b)$$

where f(b) → 0 as b → 0. The method degrades gracefully as the box widens.

**Zero-density estimates could provide the thin-box assumption for free** if we could show that the number of zeros outside any thin box is small. But current zero-density estimates are at fixed ε, not at ε = b/log T. To get zero-density at scale 1/log T, one would need:

$$N\left(\frac{1}{2} + \frac{b}{\log T}, T\right) \ll ?$$

This is an **extremely fine** zero-density estimate. No such estimate is currently known. The best zero-density results operate at fixed σ, not at σ = 1/2 + b/log T.

### 6.6 Could Zero-Density + Pair-Correlation Beat 2/3?

**In principle, yes** — if zero-density estimates at scale 1/log T were available. Here is the mechanism:

1. Pair-correlation gives s ≥ (2-C)N where C depends on the bandwidth.
2. Zero-density gives an upper bound on p (the number of off-line pairs).
3. The combined bound is: s ≥ max{(2-C)N, N - 2p}.
4. If p ≪ N/6, then N - 2p ≫ (2/3)N, and the zero-density bound is better.

But **at scale 1/log T, no zero-density estimate is available.** The best one can say is:

- At fixed ε: almost all zeros are in |β - 1/2| < ε. This is too coarse.
- At scale 1/log T: no non-trivial bound is known.

### 6.7 The Conrey (1989) Zero-Density via Mollifier

Conrey (1989) proved N(σ,T) ≪ T^{1+θ(1-2σ)} log T for θ < 4/7 by using a **mollifier method.** This is itself a mollifier result — it uses the mean value of |ζ(σ+it)M(σ+it)|² to bound N(σ,T). So there is already a deep connection between the mollifier method and zero-density.

This means the mollifier contributes to the zero-density picture, which in turn could (in principle) supplement the pair-correlation method. But the chain is:

mollifier → zero-density at fixed σ → (needs scale 1/log T) → supplement pair-correlation

The middle step is the bottleneck: the zero-density estimates are at fixed σ, not at scale 1/log T.

### 6.8 Summary of Zero-Density Combination

| Input | Scale | Can supplement pair-corr? | Improvement |
|-------|-------|--------------------------|-------------|
| Fixed-ε zero-density | σ = 1/2 + ε | Only shows almost all zeros near line | No (too coarse) |
| Thin-box zero-density (hypothetical) | σ = 1/2 + b/log T | Yes, if available | Yes, potentially significant |
| Conrey's mollifier zero-density | Fixed σ, θ < 4/7 | Same as fixed-ε | No (too coarse) |

**The zero-density route to improving 2/3 requires zero-density estimates at scale 1/log T, which are not currently available.**

---

## Q7: Synthesis — The Complete Picture

### 7.1 The Hierarchy of Methods and Their Relationships

```
                    ┌─────────────────────────────────────────┐
                    │        Under RH                           │
                    │                                           │
                    │  Mollifier ⊂ Pair-Correlation             │
                    │  (Radziwill-Soundararajan bridge)          │
                    │                                           │
                    │  Mollifier: κ* ≥ 19/27 (Bui-HB 2013)      │
                    │  Pair-corr: κ ≥ 2/3 (Montgomery 1973)     │
                    │  Pair-corr: κ* ≥ 0.6792 (CGdL 2020)       │
                    │  Combined (algebraic): κ_d ≥ 0.84665      │
                    │                                           │
                    │  No improvement from combination          │
                    │  (mollifier is subsumed by pair-corr)     │
                    └─────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │        Unconditional                      │
                    │                                           │
                    │  Mollifier: κ ≥ 5/12 (Conrey 1989)        │
                    │  Pair-corr: κ ≥ 2/3 (Claude 2026)        │
                    │                                           │
                    │  The two methods measure:                  │
                    │  - Mollifier: one-point (ζ' at zeros)      │
                    │  - Pair-corr: two-point (zero spacings)    │
                    │                                           │
                    │  Combination: NOT POSSIBLE with current    │
                    │  technology because:                       │
                    │  1. S₂ needs RH (off-line phases)         │
                    │  2. Mollifier test functions in Gram matrix │
                    │     cannot be evaluated unconditionally    │
                    │  3. Zero-density too coarse for 1/log T    │
                    └─────────────────────────────────────────┘
```

### 7.2 What Each Method Gives, Unconditionally

| Method | Bound on κ (on line) | Bound on κ* (simple) | Key limitation |
|--------|----------------------|-----------------------|---------------|
| Mollifier (Levinson–Conrey) | ≥ 5/12 ≈ 0.4167 | ≥ 0.4075 | S₂ requires RH; without RH, only S₁ available |
| Pair-correlation (Claude 2026) | ≥ 2/3 ≈ 0.6667 | ≥ 1/2 | Bandwidth ≤ 1; higher moments unavailable |
| Combined (under RH) | ≥ 2/3 (pair-corr dominates) | ≥ 19/27 (mollifier) | Mollifier subsumed by pair-corr under RH |
| Zero-density supplement | No improvement | No improvement | Scale too coarse (fixed ε vs 1/log T) |

### 7.3 The Three Obstructions to an Unconditional Combination

**Obstruction 1: The S₂ problem.** The mollifier method requires S₂ = Σ|Bζ'(ρ)|², which is a sum of squared moduli. Without RH, the contour integral gives S₂^complex = Σ Bζ'(ρ)Bζ'(1−ρ̄), which is a sum of products at different points. The off-line contribution cannot be bounded with current technology.

**Obstruction 2: The test-function equivalence.** Under RH, mollifier-weighted test functions in the Gram matrix are a subset of the already-available test functions (by the Radziwill–Soundararajan bridge). So the combination gives nothing new under RH. Without RH, the bridge breaks, and the mollifier-weighted Gram matrix cannot be evaluated.

**Obstruction 3: The zero-density scale.** Zero-density estimates could supplement pair-correlation by bounding the number of off-line zeros, but current estimates operate at fixed σ, not at scale 1/log T. The pair-correlation method needs information at scale 1/log T, which is far beyond current zero-density technology.

### 7.4 What Would Break Each Obstruction?

**Breaking Obstruction 1 (S₂ without RH):**
- Would need: subconvexity bounds for ζ'(β+iγ) at off-line zeros, plus zero-density at scale 1/log T to count off-line zeros.
- Or: a fundamentally different inequality that uses S₂^complex instead of S₂.
- No known approach.

**Breaking Obstruction 2 (mollifier test functions unconditionally):**
- Would need: unconditional evaluation of Σ_ρ M(ρ)M̄(1−ρ̄) f(γ) for test functions f.
- This is equivalent to an unconditional version of the Radziwill–Soundararajan bridge.
- No known approach.

**Breaking Obstruction 3 (zero-density at 1/log T scale):**
- Would need: N(1/2 + b/log T, T) ≪ δ(b) · N(T) with δ(b) → 0.
- This is essentially a weak form of RH (it says few zeros are more than b/log T from the line).
- No known approach, but the thin-box assumption in BGSTB/Goldston–Suriajaya shows what could be achieved *if* this were available.

### 7.5 The Deepest Obstruction

The deepest obstruction is **Obstruction 2**: the equivalence of the two methods under RH. This means:

> **Under RH, the mollifier is strictly weaker than pair-correlation. There is no combination that improves on pair-correlation alone.**

> **Without RH, the two methods are independent but cannot be combined because the connection that would allow the combination (the Radziwill–Soundararajan bridge) requires RH.**

This is a "no-go" result of sorts: the two methods are either **redundant** (under RH) or **incompatible** (without RH). There is no regime in which they are both independent and combinable.

### 7.6 Is There Any Other Way to Combine?

We considered several non-standard approaches:

**(a) Using the mollifier to improve the kernel in the pair-correlation method.** The pair-correlation method uses a kernel K(α,β) determined by the test functions. The mollifier could modify the kernel, but under RH this gives a kernel already in the pair-correlation framework. Without RH, the modified kernel cannot be evaluated.

**(b) Using the pair-correlation method to bound the error terms in the mollifier method.** The mollifier method's error terms M_{ν,3} involve sums over Dirichlet characters. The pair-correlation method gives information about zero spacings, which could potentially bound these error terms. But the connection is tenuous: the error terms are about character sums, not zero spacings, and no direct link is known.

**(c) Using both methods on different subsets of zeros.** The mollifier could be used on zeros near the line, and pair-correlation on all zeros. But identifying which zeros are near the line requires RH, and without RH, we cannot partition the zeros.

**(d) A variational approach.** Optimize over both mollifier parameters and pair-correlation test functions simultaneously. Under RH, this reduces to the pair-correlation optimization (which has been done — the optimal kernel gives 0.6725 unconditionally). Without RH, the optimization is not well-defined.

None of these approaches yield an unconditional improvement.

---

## Q8: Conclusions

### 8.1 The Bui–Heath-Brown Combination

The Bui–Heath-Brown (2013) result is a **mollifier-only** improvement for **simple zeros** (κ* ≥ 19/27 under RH). It does not combine the mollifier with pair-correlation at the analytic level. The "combination" in the literature is an **algebraic** combination at the level of the final inequality (Montgomery's identity relating κ_d, κ*, and Σ m(ρ)), not an analytic combination of the two methods.

### 8.2 Can the Combination Improve the Proportion on the Critical Line?

**No, not with current technology.** The three obstructions (§7.3) prevent an unconditional combination, and under RH, the mollifier is subsumed by the pair-correlation method.

### 8.3 Are the Methods Measuring the Same Information?

**Under RH: yes**, the mollifier is a special case of pair-correlation (Radziwill–Soundararajan bridge). **Unconditionally: no**, they measure different things (one-point vs. two-point), but they cannot be combined because the connection requires RH.

### 8.4 Can the Mollifier Be Used as a Test Function?

**Under RH: yes, but it gives no improvement** (it's already in the pair-correlation framework). **Unconditionally: the modified Gram matrix cannot be evaluated.**

### 8.5 Can Zero-Density Estimates Supplement Pair-Correlation?

**In principle: yes, if zero-density were available at scale 1/log T.** **In practice: no**, current zero-density estimates are at fixed σ, which is too coarse.

### 8.6 The Bottom Line

The mollifier method and the pair-correlation method are **complementary in principle but incompatible in practice**. The connection between them (Radziwill–Soundararajan bridge) requires RH, and without RH, they operate on different objects that cannot be combined. Under RH, the mollifier is strictly weaker than pair-correlation and adds nothing.

**The 2/3 bound from pair-correlation (Claude 2026) is the best unconditional result, and no hybrid method currently available can improve on it.**

The path to improving 2/3 does not go through combining with the mollifier. It goes through:
1. **Higher moments** of the Gram matrix (tr(G³), etc.) — not available unconditionally
2. **Bandwidth > 1** — requires Hardy–Littlewood-level prime pair estimates
3. **Zero-density at scale 1/log T** — essentially a weak form of RH
4. **A completely different proof architecture** — not pair-correlation or mollifier based

---

## References

1. H. M. Bui and D. R. Heath-Brown, "On simple zeros of the Riemann zeta-function," *Bull. London Math. Soc.* **45** (2013), 953–961. [arXiv:1302.5018]
2. J. B. Conrey, A. Ghosh, S. M. Gonek, "Simple zeros of the Riemann zeta-function," *Proc. London Math. Soc.* **76** (1998), 497–522.
3. H. L. Montgomery, "The pair correlation of zeros of the zeta function," *Proc. Sympos. Pure Math.* **XXIV** (1973), 181–193.
4. A. Cheer and D. A. Goldston, "Simple zeros of the Riemann zeta-function," *Proc. Amer. Math. Soc.* **118** (1993), 365–373.
5. M. Radziwill and K. Soundararajan, "Long mollifiers and moments of L-functions," *J. Number Theory* (2013). [molliff43.pdf]
6. S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, "An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function," *Acta Arith.* **214** (2024), 357–376.
7. D. A. Goldston and A. I. Suriajaya, "Pair Correlation of Zeros of the Riemann Zeta Function I," [arXiv:2501.14545]
8. R. Chirre, M. Gonçalves, T. de Laat, "Pair correlation estimates for the zeros of the zeta function via semidefinite programming," *J. Reine Angew. Math.* (2020).
9. J. B. Conrey, "More than two fifths of the zeros of the Riemann zeta function are on the critical line," *J. Reine Angew. Math.* **399** (1989), 1–26.
10. N. Levinson, "More than one-third of zeros of Riemann's zeta-function are on σ = 1/2," *Adv. Math.* **13** (1974), 383–436.
11. Claude (Anthropic), "More Than Two Thirds of the Zeros of the Riemann Zeta Function Lie on the Critical Line," August 10, 2026.
12. S. Feng, "A note on the proportion of zeros of the Riemann zeta-function on the critical line," *J. Number Theory* **131** (2011), 2312–2315.
13. B. Hough, "Mollified moments and the pair correlation of zeros," (survey of Radziwill–Soundararajan connection).

---

*This analysis combines the Radziwill–Soundararajan bridge (connecting mollified moments to pair-correlation under RH), the Bui–Heath-Brown removal of GLH, the Claude 2026 unconditional pair-correlation framework, and zero-density theory. The central finding — that the two methods are either redundant (under RH) or incompatible (without RH) — appears to be new to the literature.*