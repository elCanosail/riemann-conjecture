# Notebook 003 — Fase 2: Computational Verification + Adversarial Analysis

**Date:** 2026-08-11
**Author:** Elcano (GLM-5.2)
**Status:** In progress
**Models used:** GLM-5.2 (orchestrator), Kimi K2.6, DeepSeek V4 Flash, Qwen 3.6 (adversarial)

## Objective

Verify Claude's framework computationally and attack the rank-trace inequality from multiple angles using different models as adversarial reviewers.

## 2a. Computational verification

### Zeta zeros on the critical line

| Range | On line | Off line | Max |Re - 1/2| | Status |
|-------|---------|----------|-------------|--------|
| 1-50 | 50 | 0 | 0.00e+00 | ✅ |
| 1-1000 | pending | pending | pending | running |

### Gram matrix framework

Theoretical predictions verified:

| Bandwidth λ | ||G||²_F/tr(G) | Bound 2 - ratio | Matches Claude? |
|-------------|----------------|-----------------|-----------------|
| 1.0 | 4/3 = 1.3333 | 2/3 = 0.6667 | ✅ |
| 0.75 | 1.5833 | 0.4167 | ✅ |
| 0.5 | 2.1667 | -0.1667 | ✅ |

**Key finding:** The simplified Gabor construction (cosine basis) does NOT reproduce the asymptotics numerically. The ratio ||G||²_F/tr(G) is O(d²) instead of O(1) because the test family lacks the proper normalisation and Montgomery-Taylor window. A faithful implementation requires the exact kernel from Claude's paper Section 5 — this is left for future work with a proper explicit formula implementation.

**What this means:** The theoretical framework is sound (the formula 1/λ + λ/3 is verified algebraically), but the numerical construction needs the exact test functions, not a simplified proxy.

### Montgomery-Taylor kernel

The optimised kernel gives 0.6725 (vs 0.6667 for the flat window). This is a variational optimisation within the bandwidth-1 constraint. The improvement is small (0.0058) and confirms that the method is near its ceiling within bandwidth 1.

## 2b. Adversarial analysis (in progress)

Three sub-agents launched in parallel, each attacking a different question:

### 2b.1 — Rank-trace strengthening (Kimi K2.6)
**Question:** Can Lemma 3.2 be strengthened using additional spectral data (tr(G³), tr(G^k), signature)?

Key considerations:
- The rank-trace inequality uses only first and second moments of eigenvalues
- The eigenvalues have specific block structure: PSD (on-line) + hyperbolic ±c (off-line)
- Third moments might distinguish these blocks better than second moments
- Claude's agent E2-HL checked higher moments and found no improvement — but within the pair-correlation framework

### 2b.2 — Ceiling analysis (DeepSeek V4 Flash)
**Question:** Is the 0.68185 ceiling breakable by a different certificate architecture?

Key considerations:
- 0.68185 is the ceiling for POINTWISE integrality certificates
- Claude's AGGREGATE integrality (rank-trace) bypasses this
- Does the rank-trace approach have its OWN ceiling? Is it also 0.68185?
- If the rank-trace ceiling is HIGHER, there's room within bandwidth 1
- Lemma R is stated as TIGHT — but tight for which class of matrices?

### 2b.3 — SDP approach (Qwen 3.6)
**Question:** Can semidefinite programming improve the unconditional bound?

Key considerations:
- Chirre-Gonçalves-de Laat (2020) used SDP to get 0.6792 UNDER RH
- They exploited positivity of F(α) outside [-1,1] — CONJECTURAL without RH
- BGSTB gives unconditional F(α) only for |α| ≤ 1
- Can partial positivity (at finitely many points) be used as SDP constraints?
- What's the minimum unconditional positivity we need?

## Assessment so far

The computational verification confirms the theoretical framework but highlights that faithful numerical reproduction requires the exact Montgomery-Taylor kernel. The adversarial analysis is exploring three angles of attack on the 0.68185 ceiling. Results pending.