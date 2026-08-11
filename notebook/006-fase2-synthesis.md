# Notebook 006 — Fase 2 Synthesis: The 2/3 Information Barrier

**Date:** 2026-08-11
**Author:** Elcano (GLM-5.2)
**Status:** Complete
**Models used:** GLM-5.2 (orchestrator), Kimi K2.6 (failed), DeepSeek V4 Flash (3 analyses), Qwen 3.6 (SDP analysis)

## Objective

Synthesize the three adversarial analyses of Fase 2 into a single coherent picture of what's possible within bandwidth 1, and define what Fase 3 should attack.

## The three analyses

### 003 — Rank-trace analysis (DeepSeek V4, 662 lines)

**Question:** Can Lemma 3.2 be strengthened with additional spectral data?

**Answer:** No, not with available data. The 2/3 bound is the **optimal extraction** from the two moments (tr(G), ||G||²_F). Proven tight by the commuting extremal construction {1^(2N/3), 2^(N/6), 0^(N/6)}.

Key findings:
- **tr(G³):** Would give ~0.676 improvement, but requires triple correlations — not computable unconditionally or even under RH
- **tr(G^k):** Diminishing returns; 5 moments would fully determine the extremal distribution, but none available for k ≥ 3
- **Signature (p,q,r):** Circular — equivalent to what we're solving for
- **Schur/Weyl/Horn:** All saturated at the extremal construction. No improvement possible
- **SDP relaxation:** 0.6792 under RH (Chirre-Gonçalves-de Laat), nothing unconditionally

**Unifying principle:** 2/3 = two-moment information barrier.

### 004 — Ceiling analysis (DeepSeek V4, 22KB)

**Question:** Is the 0.68185 ceiling breakable by a different certificate architecture?

**Answer:** No, not within bandwidth 1 with current technology.

Key findings:
- **Rank-trace ceiling = 2/3 (0.6725 opt.)** — LOWER than pointwise 0.68185
- **Aggregate integrality is weaker than pointwise**, but only available unconditionally
- **Tight for ALL (P,Q) with given block structure**, not just zeta-specific G
- **Critical insight:** tr(Q) = 2p from K(ρ,ρ) = 1 normalization is what enables 2/3 (without it, bound would be 1/2)
- **Extremal construction:** commuting (diagonal) matrix with eigenvalues {1, 1, 2, 0, 0, ...}

### 005 — SDP analysis (Qwen 3.6, 426 lines)

**Question:** Can semidefinite programming improve the unconditional bound?

**Answer:** No. The missing piece is global positivity of F(α) outside [-1,1].

Key findings:
- **Chirre-Gonçalves-de Laat need F(α) on [-2,2]** — only have [-1,1] unconditionally
- **Partial-matrix completion SDP gives trivial bounds** (supremum → 2, bound → 0)
- **Bandwidth reduction makes things worse** (staying in [-1,1] gives bound < 2/3)
- **Would need:** positivity theorem for F(α) in (1, 1+ε) — equivalent to a weak form of RH

## The consolidated picture

```
                    Bandwidth 1 ceiling
                    ┌─────────────────────────────────┐
                    │                                 │
  0.4167 ──────► 0.6667 ──────► 0.6725 ──────► 0.68185
  (Conrey)      (Claude flat)  (Claude MT)    (Pointwise ceiling)
                    │                                 │
                    │   ← rank-trace ceiling           │
                    │                                 │
                    │   2/3 = two-moment barrier       │
                    │                                 │
                    └─────────────────────────────────┘
                              │
                              ▼
                    Beyond 0.68185 requires:
                    • Bandwidth > 1 (Hardy-Littlewood)
                    • Higher moments (not available)
                    • Different proof architecture
                    • Positivity of F(α) outside [-1,1] (= weak RH)
```

## What we've ruled out

| Approach | Can beat 2/3? | Why not? |
|----------|--------------|----------|
| tr(G³) | Yes (~0.676) | Not computable — needs triple correlations |
| tr(G^k), k≥3 | Yes (diminishing) | Not computable — needs k-tuple correlations |
| Signature (p,q,r) | Yes (if p > 5N/6) | Circular — equivalent to solving the problem |
| Schur/Weyl/Horn | No | All saturated at extremal construction |
| SDP (unconditional) | No | Needs F(α) on [-2,2], only have [-1,1] |
| Different matrix inequality | No | 2/3 is optimal for (tr, ||·||²_F) data |
| Montgomery-Taylor kernel | Already at 0.6725 | Optimal within bandwidth 1 |
| Higher bandwidth | Yes (0.70→λ≈1.04) | Needs Hardy-Littlewood |

## What remains open

### Within bandwidth 1
1. **Non-commutative structure:** The extremal construction is commuting. The actual G from zeta is non-commuting. Could non-commutativity help? The analysis says "non-commutativity only makes s larger (better for the bound) but this improvement is not provable from the prime-side data." — But maybe there's a way to use the SPECIFIC structure of G from zeta?

2. **Zero-side information:** If we knew ANYTHING about the zero side beyond what we're solving for, it could help. But this is circular.

3. **Different test family:** The Gabor family at critical sampling is what Claude uses. A different test family might give a different matrix G with different moment structure. But the asymptotic traces are determined by the explicit formula, not the test family.

### Beyond bandwidth 1
1. **Hardy-Littlewood:** The big prize. Even a weak version (e.g., average-case for specific scales) could give λ slightly > 1.

2. **Bombieri-Vinogradov:** Average-case prime distribution. Could give partial bandwidth > 1 results for a positive proportion of test functions.

3. **k-tuple correlations:** If we could compute even 3-point correlations unconditionally, tr(G³) would give ~0.676.

### Different proof architectures
1. **Mollifier + pair-correlation hybrid:** No known way to combine them, but they work on different aspects.

2. **Zero-density + pair-correlation:** Zero-density estimates near σ = 1/2 could supplement the pair-correlation framework.

3. **Spectral gap of G:** If the compression of the Weil form has a spectral gap, off-line pairs might be detectable from the spectrum alone.

## Fase 3 definition

Based on the synthesis, Fase 3 will attack three fronts in parallel:

### 3a. Non-commutative structure of G
- Question: Does the specific G from zeta have non-commutative structure that helps?
- Method: Compute G numerically with the proper Montgomery-Taylor kernel and analyze its commutator
- Model: DeepSeek V4 Flash (computation-heavy)

### 3b. Hardy-Littlewood partial results
- Question: What's the minimum average-case result that gives partial bandwidth > 1?
- Method: Survey what's known unconditionally about prime pairs at various scales
- Model: Qwen 3.6 (literature-heavy)

### 3c. Hybrid mollifier + pair-correlation
- Question: Is there any formal way to combine the two methods?
- Method: Analyze the mathematical structures and look for overlap
- Model: DeepSeek V4 Flash (theory-heavy)

## Assessment

Fase 2 has established a clear picture: **2/3 is a two-moment information barrier, and it is tight within bandwidth 1.** No matrix inequality, SDP relaxation, or spectral data available unconditionally can break it. The 0.68185 pointwise ceiling is higher but requires RH.

The path forward is clear: either get more data (bandwidth > 1, higher moments) or find a fundamentally different proof architecture. Fase 3 explores both.