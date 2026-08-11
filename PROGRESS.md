# PROGRESS.md — Research State

## Current baseline

**Claude/Anthropic (2026-08-10):** ≥ 2/3 of zeta zeros on the critical line (unconditional).
- Optimised constant: 0.6725 (Montgomery–Taylor kernel)
- Simple zeros on line: ≥ 1/2
- Distinct zeros: ≥ 5/6
- Method: Pair-correlation + linear algebra (rank–trace inequality, von Neumann trace inequality)
- No mollifier, no zero-density estimate, no zero-free region used
- Formalized in Lean 4 (passes comparator)

## What Anthropic's method CANNOT do (stated in their paper)

1. **Cannot reach 100%** — the method is structurally capped. Pair-correlation at bandwidth ≤ 1 gives at most ~0.68185 for simple zeros. Reaching 0.70, 0.80, 0.90 would require pair-correlation beyond bandwidth 1 (Hardy–Littlewood strength).
2. **No bearing on RH** — the result is a lower bound only. The remaining 1/3 are not shown to be off the line.
3. **Insensitive to off-line zeros** — the inputs are satisfied by functions where RH is false (Davenport–Heilbronn, Epstein zeta).
4. **λ ≤ 1 is essential** — for X ≫ T, off-diagonal prime sums need Hardy–Littlewood-level information.

## Open questions after Anthropic

1. **Can the 67.25% be pushed with a different kernel?** — Anthropic used Montgomery–Taylor. Are there other test families?
2. **Can pair-correlation beyond bandwidth 1 be made unconditional?** — This is the structural barrier. Any progress here would be significant.
3. **Can the linear algebra be strengthened?** — The rank–trace inequality is sharp. But are there other matrix inequalities?
4. **Can higher moments help?** — Anthropic's agent checked: unconditional higher moments exist only at bandwidths where the method's own cap kills everything.
5. **What about completely different approaches?** — Weil positivity, de Branges, Jensen polynomials, heat flow, etc. All hit walls per Anthropic's campaign. But different models might find different walls.
6. **Dirichlet L-functions** — Anthropic extended to fixed primitive Dirichlet L-functions. What about other L-functions?

## Research log

### 2026-08-11 — Fase 0: Setup
- Repo created
- Anthropic papers downloaded (paper, mathematicians' note, appendix)
- Lean 4 formalization cloned (anthropics/zeta-23-lean)
- README.md written
- Sub-agents launched for Fase 1 survey

## Status

✅ **Fase 0: Setup** — complete (repo, references, baseline audit)
🟡 **Fase 1: Survey** — 3 sub-agents running (classical, pair-correlation, physics)
🟡 **Fase 2: Computational verification** — first 50 zeros verified (100% on line)
⬜ **Fase 3: Multi-model research rounds** — pending
⬜ **Fase 4: Documentation** — pending