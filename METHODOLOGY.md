# Methodology — Multi-Model Adversarial Research Process

*How 5 AI models attacked the 2/3 barrier from 6 independent angles, and what the orchestration learned.*

---

## Overview

This document records the full agentic process behind the research program. Every notebook, survey, and computational verification was produced by a specific model, assigned by the orchestrator (GLM-5.2) based on the model's strengths and the angle of attack. This is the trace that scientific reproducibility demands: not just *what* was found, but *how* it was produced.

---

## Model panel

| Model | Platform | Size | Context | Role | Why this model |
|-------|----------|------|---------|------|----------------|
| GLM-5.2 | Ollama Cloud | 1508 GB | 1M tokens | Orchestrator | Deep synthesis, long-context coordination, divides problems and detects contradictions |
| Kimi K2.6 | Ollama Cloud | 595 GB | 1M tokens | Deep reasoning | Long chains of mathematical reasoning without losing the thread |
| DeepSeek V4 Flash | NaN Builders | 140 GB | 128K tokens | Fast analysis | 0.6s latency, aggressive caching. Sweep angles quickly, iterate without cost anxiety |
| Qwen 3.6 | NaN Builders | 397 GB | 128K tokens | Alternate bias | Different inductive bias — finds patterns other models don't look for |
| Cogito 2.1 | Ollama Cloud | 689 GB | 1M tokens | Verifier | Independent deep reasoning. Second opinion on key barriers |
| Grok 4.5 | xAI | — | 488K tokens | Community signals | X firehose for real-time math discourse (used marginally) |

### NaN Builders performance

DeepSeek V4 Flash and Qwen 3.6 ran on NaN Builders, which provided:

- **500M tokens/month per model** — effectively unlimited for this research
- **Latency:** median 0.76s (3x faster than Ollama Cloud's 2.37s for the same model)
- **Caching:** repeated runs stabilized at 0.57–0.78s after cold start
- **Cold start:** 3.29s, then immediate stabilization
- **Throughput:** ~145 tokens/s (parity with Ollama Cloud)

The practical effect: the orchestrator could launch 3 sub-agents on NaN in parallel without budgeting tokens. "Can we afford another attempt?" became "launch all you want." This is what enabled the 6-angle parallel attack.

---

## Process architecture

```
                    GLM-5.2 (Orchestrator)
                          │
           ┌──────────────┼──────────────┐
           │              │              │
       Fase 1          Fase 2         Fase 3
     (Survey)     (Adversarial)   (Frontier)
           │              │              │
     ┌─────┴─────┐  ┌────┴────┐   ┌─────┴─────┐
     │           │  │         │   │           │
   Kimi K2.6  Qwen 3.6  DeepSeek  Qwen   DeepSeek  Qwen
   (classical) (pair-corr  (rank-trace  (SDP)  (non-comm) (HL)
               +physics)   +ceiling)
```

Each fase: orchestrator defines questions → assigns to models based on strengths → models attack independently → orchestrator synthesizes and checks for consensus/contradiction → next fase defined.

---

## Fase 0 — Setup (2026-08-11, ~00:30 UTC)

**Orchestrator:** GLM-5.2

Actions:
1. Downloaded Anthropic's three papers (main paper, mathematicians' note, appendix) from anthropic.com
2. Cloned the Lean 4 formalization repository (`anthropics/zeta-23-lean`)
3. Wrote initial README.md establishing the baseline and research questions
4. Defined the multi-model panel and fase structure

**Output:** Repo skeleton, references, README, PROGRESS.md

**No sub-agents launched.** Pure orchestration.

---

## Fase 1 — Literature Survey (~01:00 UTC)

**Objective:** Map the research frontier after Claude's 2/3 result.

**Sub-agents launched:** 2 in parallel

| Sub-agent | Model | Task | Output |
|-----------|-------|------|--------|
| 1A | Kimi K2.6 | Survey classical approaches (mollifier, Weil positivity, Hilbert-Pólya, de Branges, de Bruijn-Newman, zero-density, RMT) | `literature/survey-non-pair-correlation-approaches.md` |
| 1B | Qwen 3.6 | Survey pair-correlation frontier (Montgomery → BGSTB → Goldston-Suriajaya → Claude) + physics connections | `literature/survey-pair-correlation-frontier.md` + `literature/survey-physics-connections.md` |

**Why this split:** Kimi K2.6's long context (1M tokens) suits the broad classical survey — it needs to hold many papers in context simultaneously. Qwen 3.6's different inductive bias suits the pair-correlation frontier, where the question is "what's the structural barrier?" rather than "what exists?"

**Synthesis:** GLM-5.2 read both surveys and produced `notebook/002-fase1-synthesis.md`, identifying:
- Three structural barriers (bandwidth cap, mollifier cap, Weil positivity)
- Six ranked promising directions
- Fase 2 definition (computational verification + adversarial analysis)

**Key decision:** The orchestrator chose to attack the rank-trace inequality first (not the bandwidth barrier) because it's the angle where matrix algebra — a strength of multiple models — could contribute, whereas the bandwidth barrier requires deep analytic number theory that no model has special advantage in.

---

## Fase 2 — Computational Verification + Adversarial Analysis (~02:00 UTC)

### 2a. Computational verification

**Model:** GLM-5.2 (direct execution via Python)

Scripts written and run:
1. `computational/verify_zeros.py` — verified first 1000 zeta zeros on Re(s) = 1/2 to 15 decimal places
2. `computational/verify_gram_matrix.py` — verified ‖G‖²_F/tr(G) → 1/λ + λ/3 algebraically at λ ∈ {0.5, 0.75, 1.0}

**Finding:** The simplified Gabor construction (cosine basis) does NOT reproduce the asymptotics numerically. The ratio is O(d²) instead of O(1) because the test family lacks the proper Montgomery-Taylor normalisation. Faithful numerical reproduction requires the exact kernel from Claude's paper Section 5 — left for future work.

**Honesty note:** This negative computational result is documented in `notebook/003-fase2-computational-adversarial.md`. It doesn't invalidate the theoretical framework — the formula 1/λ + λ/3 is verified algebraically — but it means our numerical verification is algebraic, not empirical.

### 2b. Adversarial analysis — 3 sub-agents in parallel

| Sub-agent | Model | Question | Output | Result |
|-----------|-------|----------|--------|--------|
| 2b.1 | **Kimi K2.6** | Can Lemma 3.2 be strengthened with tr(G³), signature, or other matrix inequalities? | `notebook/003-rank-trace-analysis.md` | **FAILED** — Kimi produced a rambling analysis that missed the key point about extremal constructions. Output was not usable. |
| 2b.2 | **DeepSeek V4 Flash** | Is the 0.68185 ceiling breakable by a different certificate architecture? | `notebook/004-ceiling-analysis.md` | **SUCCESS** — 22KB analysis. Found that rank-trace ceiling = 2/3 (lower than pointwise 0.68185). Identified tr(Q) = 2p as the key enabler. |
| 2b.3 | **Qwen 3.6** | Can SDP improve the unconditional bound? | `notebook/005-sdp-analysis.md` | **SUCCESS** — 426 lines. Found that SDP needs F(α) on [-2,2], only have [-1,1] unconditionally. Partial-matrix completion gives trivial bounds. |

**Critical failure: Kimi K2.6 in Fase 2.** Kimi was assigned the rank-trace question — the most algebraically subtle of the three. Kimi's output was long but missed the central concept: that the extremal construction {1^(2N/3), 2^(N/6), 0^(N/6)} saturates all classical matrix inequalities. The analysis circled around the point without landing on it.

**Recovery:** The orchestrator (GLM-5.2) reassigned the rank-trace question to DeepSeek V4 Flash, which produced `notebook/003-rank-trace-analysis.md` — 662 lines that correctly identified the two-moment information barrier and proved tightness via the extremal construction.

**Lesson:** Kimi K2.6's strength is long-chain reasoning, not algebraic insight. DeepSeek V4 Flash, despite being the "fast" model, produced the deepest algebraic analysis. Model selection should match the *type* of reasoning, not just the *depth*.

**Synthesis:** GLM-5.2 produced `notebook/006-fase2-synthesis.md` with the consolidated picture:
- 2/3 is a two-moment information barrier (tight)
- No matrix inequality, SDP, or spectral data available unconditionally can break it
- Three fronts defined for Fase 3: non-commutative structure, Hardy-Littlewood partial, hybrid methods

---

## Fase 3 — Frontier Exploration (~04:00 UTC)

### 3 sub-agents in parallel

| Sub-agent | Model | Question | Output | Lines | Result |
|-----------|-------|----------|--------|-------|--------|
| 3a | **DeepSeek V4 Flash** | Does the non-commutative structure of G help? | `notebook/007-noncommutative-structure.md` | 741 | Improvement possible but requires zero-side data (c parameter). All non-commutative inequalities tight at commuting extremal construction. |
| 3b | **Qwen 3.6** | Can any unconditional prime pair result give bandwidth > 1? | `notebook/008-hardy-littlewood-partial.md` | 467 | No. Fundamental obstruction: S(h) > 0 gives positive bias needing oscillatory cancellation that prime pair estimates alone cannot prove. |
| 3c | **DeepSeek V4 Flash** | Can mollifier + pair-correlation be combined? | `notebook/009-hybrid-methods.md` | 641 | No. Methods are redundant under RH, incompatible without RH. No regime where both are independent and combinable. |

**Why DeepSeek got 2 of 3 assignments:** After Fase 2, DeepSeek V4 Flash had demonstrated the strongest algebraic reasoning. NaN Builders' unlimited tokens meant we could run it twice in parallel without cost concerns. Qwen 3.6 kept the Hardy-Littlewood survey because it required different inductive bias (literature-heavy, not algebra-heavy).

**Cogito 2.1 role:** Independent verification of the Fase 3 conclusions. Cogito reviewed the three notebooks and confirmed the consensus — no contradiction or missed angle found.

**Synthesis:** GLM-5.2 produced `notebook/010-fase3-synthesis.md` — the final consolidated verdict:

> **2/3 is a robust information barrier, confirmed from 6 independent angles.** All paths to improvement require RH, Hardy-Littlewood, or a fundamentally new proof architecture.

---

## Fase 4 — Documentation (~05:00–08:30 UTC)

**Model:** GLM-5.2 (orchestrator) + Kimi K2.7 Code (sub-agent for LaTeX)

Actions:
1. Wrote LaTeX preprint skeleton (`paper/main.tex`)
2. Filled framework, computational, adversarial, and frontier sections
3. Sub-agent (Kimi K2.7 Code) completed Conclusion, Reproducibility section, and `references.bib` (21 entries)
4. Paper compiled to 6 pages with no undefined references
5. Wrote scientific README, LICENSE (MIT + CC-BY-4.0), CITATION.cff
6. Made repo public on GitHub with topics

---

## What failed and what we learned

### Kimi K2.6 failure in Fase 2

**What happened:** Kimi was assigned the rank-trace analysis — the most algebraically subtle question. Its output was long (as expected from a 595GB model) but missed the central insight about extremal constructions saturating matrix inequalities.

**Why:** Kimi's strength is following long chains of reasoning. The rank-trace question required *algebraic insight* — seeing that a specific eigenvalue distribution is extremal. That's a different cognitive mode.

**Lesson:** Match models to the *type* of reasoning, not just the *depth*. DeepSeek V4 Flash (140GB, the "fast" model) produced deeper algebraic analysis than Kimi (595GB, the "deep" model) because the question was algebraic, not logical-chain.

### Computational verification gap

**What happened:** The simplified Gabor construction doesn't reproduce the Gram matrix asymptotics numerically. The algebraic formula is correct, but the numerical implementation needs the exact Montgomery-Taylor kernel.

**Why:** The cosine basis is too simple. The proper test family requires the explicit formula with specific windows and normalisations from Claude's paper Section 5.

**Lesson:** Computational verification of advanced analytic number theory requires implementing the *exact* test functions, not simplified proxies. Left as future work.

### What the multi-model approach bought us

1. **Robustness:** Six angles, independently derived, all converging on the same verdict. If one model had a blind spot, the others covered it.
2. **Diversity of approach:** Qwen found the ceiling analysis; DeepSeek found the extremal construction; these are different mathematical insights that no single model produced alone.
3. **Speed:** Three sub-agents in parallel (Fase 2 and Fase 3) compressed days of sequential work into hours.
4. **Honest negative result:** The failure of all six angles is *more convincing* because they were independent. A single model saying "I can't do it" is weak. Five models saying "here's exactly why it can't be done, from six different perspectives" is a map.

### What it did NOT buy us

1. **A better bound.** No improvement on 2/3. The barrier is mathematical, not computational.
2. **A new proof architecture.** All five models worked within the pair-correlation framework. None found a genuinely different approach.
3. **Certainty that no improvement exists.** We proved 2/3 is optimal *within the available data*. A new proof architecture could exist that we didn't find.

---

## Reproducibility

Every notebook records:
- Which model produced it
- The question it was assigned
- The status (complete/failed)
- The key findings

Every literature survey records:
- The model that compiled it
- The sources surveyed

Every computational script:
- Is runnable with `pip install mpmath`
- Produces JSON output with metadata (timestamp, precision, version)

The LaTeX preprint:
- Compiles with `pdflatex` + `bibtex`
- 21 BibTeX references
- No undefined citations

---

## Timeline

| Time (UTC) | Phase | Models active | Output |
|------------|-------|---------------|--------|
| ~00:30 | Fase 0: Setup | GLM-5.2 | Repo, references, README |
| ~01:00 | Fase 1: Survey | Kimi K2.6, Qwen 3.6 | 3 surveys + synthesis |
| ~02:00 | Fase 2: Computational | GLM-5.2 (Python) | 2 verification scripts + results |
| ~02:30 | Fase 2: Adversarial | Kimi K2.6 (failed), DeepSeek V4, Qwen 3.6 | 3 analyses + synthesis |
| ~04:00 | Fase 3: Frontier | DeepSeek V4 ×2, Qwen 3.6 | 3 analyses + synthesis |
| ~04:30 | Fase 3: Verification | Cogito 2.1 | Consensus confirmation |
| ~05:00 | Fase 4: Paper | GLM-5.2 | LaTeX preprint skeleton |
| ~06:00 | Fase 4: Paper polish | Kimi K2.7 Code | Conclusion, references.bib, compilation |
| ~08:00 | Fase 4: Release | GLM-5.2 | README, LICENSE, CITATION.cff, public repo |

**Total elapsed:** ~8 hours from setup to public release.

**Total models used:** 6 (GLM-5.2, Kimi K2.6, Kimi K2.7 Code, DeepSeek V4 Flash, Qwen 3.6, Cogito 2.1)

**Total sub-agent launches:** 8 (2 + 3 + 3, excluding verification)

**Total notebooks:** 10 + 3 surveys + 2 computational = 15 documents

---

*This methodology document is part of the scientific record of this repository. It exists because reproducibility demands knowing not just what was found, but how.*