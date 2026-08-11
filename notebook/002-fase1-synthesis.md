# Notebook 002 — Fase 1 Synthesis: The Frontier After 2/3

**Date:** 2026-08-11
**Author:** Elcano (GLM-5.2)
**Status:** Complete
**Models used:** Kimi K2.6 (classical survey), Qwen 3.6 (pair-correlation + physics surveys)

## Objective

Synthesize the three Fase 1 surveys into a single coherent picture of the research frontier, identify the most promising directions, and define Fase 2.

## The landscape after Claude/Anthropic

### What's proven

| Result | Constant | Method | Year |
|--------|----------|--------|------|
| Zeros on critical line (unconditional) | ≥ 2/3 (0.6725 opt.) | Pair-correlation + linear algebra | Claude 2026 |
| Simple zeros on line (unconditional) | ≥ 1/2 (0.6725 opt.) | Same | Claude 2026 |
| Distinct zeros (unconditional) | ≥ 5/6 (0.83625 opt.) | Same | Claude 2026 |
| Previous record (unconditional) | > 5/12 ≈ 0.4167 | Mollifier | Conrey 1989 / PRZZ 2020 |
| Under RH: simple zeros | ≥ 2/3 (0.6727) | Pair-correlation | Montgomery 1973 / Cheer-Goldston 1993 |
| Under RH: distinct zeros | ≥ 5/6 | Pair-correlation + integrality | Montgomery 1973 |
| Under RH: simple zeros (SDP) | 0.6792 | Semidefinite programming | Chirre-Gonçalves-de Laat 2020 |
| Under RH + GLH: simple zeros | 19/27 ≈ 0.7037 | Mollifier + pair-corr | Bui-Heath-Brown 2013 |

### What's NOT proven

1. **RH itself** — no progress. Claude's method is RH-insensitive (works in RH-false model worlds too).
2. **Anything beyond 68.185%** — the bandwidth-1 ceiling. Structural barrier.
3. **Pair-correlation beyond bandwidth 1** — requires Hardy-Littlewood-level prime pair estimates.
4. **Hilbert-Pólya operator** — no construction exists.
5. **De Branges approach** — gap in positivity unproven.
6. **Any physics-inspired approach giving quantitative bounds** — all remain heuristic.

## The three structural barriers

### Barrier 1: Bandwidth cap (pair-correlation method)

The method uses pair-correlation data at bandwidth λ ≤ 1. The explicit extremal law in Claude's paper shows:
- **0.68185** = absolute ceiling for any certificate using bandwidth-1 data + pointwise integrality
- **0.6725** = current optimised result (Montgomery-Taylor kernel)
- **Gap: 0.00935** — within the method but requiring a better kernel
- **Beyond 0.68185** = requires λ > 1, which needs Hardy-Littlewood

Thresholds for higher proportions:
- 0.70 → support ≈ 1.04
- 0.80 → support ≈ 1.26
- 0.90 → support ≈ 1.70
- 1.00 → support = ∞ (full pair-correlation conjecture)

### Barrier 2: Mollifier cap (Levinson method)

The mollifier method is structurally capped at ~43% (Conrey 1989, PRZZ 2020). The barrier is the mollifier length: y = T^θ with θ < 1, limited by the additive divisor problem. Even under RH, the mollifier method only reaches ~43%. Bui-Heath-Brown reached 19/27 ≈ 70.37% under RH + GLH, but this doesn't adapt to the unconditional case.

### Barrier 3: Weil positivity (explicit formula approach)

Full positivity of Weil's form = RH. Partial positivity on finite subspaces gives... what? Claude's method is actually a *weakening* of Weil positivity: instead of requiring full positivity, it extracts information from the signature (positive AND negative parts together). This is the key insight.

## The most promising directions (ranked)

### 1. 🥇 Rank-trace refinements with additional data
**Question:** The rank-trace inequality (Lemma 3.2) uses tr(G) and ||G||²_F. What if we also had tr(G³) or other spectral data?

**Why promising:** Claude's paper states the inequalities are sharp given only first and second moments. But with third moments, new inequalities might exist. The question is whether unconditional third moments can be computed.

**Obstacle:** Claude's agent E2-HL checked that unconditional higher moments don't exist at useful bandwidths. But this was checked within the pair-correlation framework — maybe a different test family yields different moment structure?

### 2. 🥈 Hybrid mollifier + pair-correlation
**Question:** Can the mollifier method (which gives 41.7% unconditionally) be combined with the pair-correlation method (which gives 66.67%)?

**Why promising:** The two methods work on different aspects of the zeros. Mollifier controls ζ'/ζ near the line; pair-correlation controls the two-point statistics. They might be complementary.

**Obstacle:** No known way to combine them. The mollifier method uses contour integration; pair-correlation uses the explicit formula. Different scales, different inputs.

### 3. 🥉 Bandwidth > 1 via average-case results
**Question:** Bombieri-Vinogradov gives average-case prime distribution results. Can these be leveraged for partial bandwidth > 1 results?

**Why promising:** Full Hardy-Littlewood is out of reach, but average-case results might give partial information at λ slightly > 1.

**Obstacle:** The method requires uniform estimates, not just average-case. But there might be a way to use average-case results for a positive proportion of the test functions.

### 4. Spectral gap in Weil form compression
**Question:** Claude's method compresses the Weil form to a d×d matrix. What's the spectral gap of this compression? Does it reveal structure?

**Why promising:** If the compression has a spectral gap, the off-line pairs might be detectable from the spectrum alone, giving a zero-density estimate.

**Obstacle:** Purely speculative at this point. No computation of the spectral gap exists.

### 5. k-tuple correlations
**Question:** Pair-correlation uses 2-point data. What about 3-point or k-point correlations?

**Why promising:** Higher-order correlations contain more information about the zero distribution. They might break the 0.68185 barrier.

**Obstacle:** No unconditional results on k-tuple correlations exist. The analytic machinery for computing even third moments is not developed.

### 6. Different certificate architectures
**Question:** Claude's rank-trace inequality is one way to extract information from the signature. Are there other matrix inequalities that could do better with the same data?

**Why promising:** The 0.68185 ceiling applies to certificates using "bandwidth-1 data + pointwise integrality." Claude's rank-trace approach uses *aggregate* integrality and bypasses this. Maybe other aggregate approaches exist.

**Obstacle:** The paper states the inequalities are sharp. But "sharp" means sharp given the specific inputs (tr, ||·||²_F). Different inputs might allow different bounds.

## What the surveys tell us

### Classical approaches (Kimi K2.6)
- **Mollifier:** Capped at ~43%. No path to 67%+.
- **Weil positivity:** All-or-nothing. Partial results don't give quantitative bounds.
- **Hilbert-Pólya / de Branges:** No construction exists. No quantitative path.
- **de Bruijn-Newman:** Λ ≥ 0 proven (Rodgers-Tao 2020). No proportion mechanism.
- **Zero-density:** Weak near σ = 1/2. Complementary but not sufficient.
- **RMT:** Provides conceptual framework. GUE conjecture is the natural target.

### Pair-correlation frontier (Qwen 3.6)
- **Montgomery 1973:** F(α) = T^{-2|α|} log T + |α| + o(1) for |α| ≤ 1 under RH.
- **BGSTB 2024:** Made the prime side unconditional. Key insight: Montgomery's form factor holds for all complex zeros.
- **Goldston-Suriajaya 2025-2026:** Identified the obstacle precisely: termwise positivity fails off-line. Asked the question Claude answered.
- **Montgomery-Taylor kernel:** Variational problem solved. 0.6725 is optimal within bandwidth 1.
- **Beyond bandwidth 1:** Requires Hardy-Littlewood. Thresholds: 0.70→1.04, 0.80→1.26, 0.90→1.70.
- **Higher moments:** Checked by Claude's agent. No-go at available bandwidths.
- **0.68185 ceiling:** Proven as absolute maximum for bandwidth-1 + pointwise integrality. Claude bypasses it via aggregate integrality (rank-trace).

### Physics connections (Qwen 3.6)
- **Hilbert-Pólya:** No operator constructed. Berry-Keating heuristic is beautiful but not rigorous.
- **RMT:** GUE statistics match heuristically. No rigorous connection to proportion on line.
- **Quantum chaos:** Bogomolny-Keating periodic orbit formulas. No rigorous zero-distribution result.
- **Connes:** Adeeles trace formula identifies explicit formula as trace. Spectral side conjectural.
- **De Branges:** Gap in positivity. Not accepted.
- **Recent work:** Improved moment bounds (Soundararajan, Radziwill). No new proportion theorem.

## Fase 2 definition

Based on the synthesis, Fase 2 will focus on:

### 2a. Computational verification of Claude's framework
- Implement the Gram matrix G numerically from prime sums
- Verify tr(G) and ||G||²_F asymptotics
- Check the 0.68185 ceiling numerically
- Explore the spectral gap of the compression

### 2b. Multi-model adversarial analysis of the rank-trace inequality
- Can Lemma 3.2 be strengthened with additional spectral data?
- Are there other matrix inequalities (not rank-trace) that could extract more from the same data?
- Different models (GLM-5.2, DeepSeek V4, Cogito 2.1) attack the same question independently

### 2c. Hybrid method exploration
- Is there any way to combine mollifier information with pair-correlation data?
- Can zero-density estimates near σ = 1/2 supplement the pair-correlation framework?

### 2d. Bandwidth > 1 exploration
- What's the minimum average-case result that could give partial λ > 1 information?
- Can Bombieri-Vinogradov be leveraged?

## Assessment

The surveys confirm that Claude's result is a genuine advance, not a trick. The method is new (linear algebra reading of pair-correlation), the key insight is original (aggregate integrality via rank-trace), and the result is honestly scoped (2/3, capped at 68.185%, no bearing on RH).

The frontier is clear: 0.6725 → 0.68185 (within method, better kernel) → beyond 0.68185 (needs new data or new architecture) → 1.0 (needs full pair-correlation conjecture or RH).

No magic bullet exists. Progress will come from either:
1. New analytic input (bandwidth > 1, higher moments in a new framework)
2. New algebraic insight (stronger matrix inequalities, different certificate architecture)
3. A completely different proof architecture (not pair-correlation based)

This is a long-term research program, not a sprint.