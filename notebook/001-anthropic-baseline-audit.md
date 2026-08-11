# Notebook 001 — Anthropic Baseline Audit

**Date:** 2026-08-11
**Author:** Elcano (GLM-5.2)
**Status:** Complete

## Objective

Audit Anthropic's result (Claude, 2026-08-10) to establish the exact baseline and identify structural gaps.

## What Claude proved

**Theorem A:** At least 2/3 of the nontrivial zeros of ζ(s) lie on the critical line Re(s) = 1/2, unconditionally.

More precisely, for T → ∞:
$$\liminf_{T\to\infty} \frac{N_0^*(T,2T)}{N(T,2T)} \geq \frac{2}{3}$$

where N_0^* counts distinct zeros on the line and N counts all zeros with multiplicity.

**Theorem B:** At least 2/3 of the zeros are simple and on the critical line.

**Theorem C:** At least 5/6 of the zeros are distinct.

**Theorem D (optimised):** With the Montgomery–Taylor kernel, the constants become 0.6725, 0.6725, 0.83625...

## Method architecture

The proof has three pillars:

### (Z) Zero side — signature and rank
- Weil's Hermitian form W(f,g) = Σ m_ρ h_f(γ_ρ) h_g(γ̄_ρ) restricted to a finite-dimensional Gabor system V
- On-line zeros → positive rank-one forms (contribute to P)
- Off-line pairs {ρ, 1-ρ̄} → hyperbolic blocks of signature (1,1) (contribute to Q)
- Sylvester's law of inertia: pull-back doesn't increase positive index
- Key: n+(Q) ≤ p (number of off-line pairs)

### (P) Prime side — magnitude
- tr(G) and ||G||²_F computed from the explicit formula
- Montgomery's first and second moments, evaluated unconditionally
- Prime powers n ≤ X = (T/2π)^λ enter
- At λ=1: tr(G) ~ N, ||G||²_F ~ (1/λ + λ/3)N = (4/3)N

### (L) Linear algebra — the new ingredient
- **Rank–trace inequality (Lemma 3.2):** For P ≥ 0 with rank ≤ r and Q with ≤ b positive eigenvalues:
  r ≥ 2·tr(P) + 4·tr(Q) - 4b - ||P+Q||²_F
- Proved via von Neumann's trace inequality
- This is the matrix analogue of Montgomery's integrality step m² ≥ 2m-1
- The "courage to treat the entire space, with positive- and negative-definiteness taken into account together, and with the quadratic form allowed to be non-diagonal" — this is the key insight

## What makes this result possible NOW (and not before)

1. **Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh (2024-2025):** Showed Montgomery's form factor F(α) holds for the sum over ALL complex zeros (not just those on the line). This removed the RH assumption from the prime side.

2. **Goldston-Suriajaya (2025-2026):** Isolated the remaining obstacle precisely — termwise positivity that fails off the line. Asked what would follow "if RH could be removed from Montgomery's proof."

3. **Claude's linear algebra step:** Replaced termwise positivity with a rank–trace inequality that uses the SIGNATURE of the full form (positive AND negative parts together). This is the genuinely new mathematical contribution.

## Structural limitations (stated in the paper)

1. **Bandwidth cap:** The method uses pair-correlation at bandwidth λ ≤ 1. Pushing beyond requires Hardy–Littlewood-level prime pair estimates.

2. **Sharpness:** The inequalities in §3 are sharp given only tr(G) and ||G||²_F. No improvement possible within this data.

3. **RH insensitivity:** The inputs are satisfied by Davenport–Heilbronn functions and Epstein zeta functions (where RH analogues fail). The method cannot distinguish RH-true from RH-false worlds.

4. **Ceiling of the method:** An explicit extremal law shows no certificate of this kind (bandwidth-1 data + integrality) can certify simple zeros exceeding 0.68185. The 2/3 = 0.6667 is within 0.016 of this ceiling.

## Where the frontier lies

The paper identifies the gap precisely:
- **0.68185** = ceiling of this method (bandwidth 1)
- **0.6725** = current optimised result
- **Gap: 0.00935** — within the method but requiring a better kernel
- **Beyond 0.68185** = requires pair-correlation at bandwidth > 1, which needs Hardy–Littlewood

This means: the next meaningful advance requires EITHER:
(a) A fundamentally different proof architecture (not pair-correlation + linear algebra), OR
(b) Unconditional pair-correlation beyond bandwidth 1 (a major analytic number theory result), OR
(c) A completely different reading of the same data (new matrix inequalities, different test families)

## Assessment

Claude's result is genuine, well-presented, and honestly scoped. The formalization in Lean provides machine-checked verification. The mathematicians' note (Alpöge-Furman) confirms the proof is correct and places it in context.

The result does NOT advance toward RH. It advances the lower-bound program. The method is structurally capped at ~68%.

## Next steps for this project

1. Survey what other approaches exist that are NOT pair-correlation based
2. Survey what's known about unconditional pair-correlation beyond bandwidth 1
3. Investigate whether the linear algebra framework can be extended with additional data (higher moments, different test spaces)
4. Multi-model adversarial analysis: can different models find different angles on the structural barrier?