# Riemann Conjecture — Multi-Model Research Lab

An open, reproducible, multi-model research project advancing the state of the art on the Riemann Hypothesis and related problems.

## Premise

On August 10, 2026, Anthropic published Claude's result: **at least 2/3 of the nontrivial zeros of the Riemann zeta function lie on the critical line** (unconditionally), improving the previous record of 5/12 ≈ 41.6% (Conrey, 1989; Pratt-Robles-Zaharescu-Zeindler, 2020). The optimised constant reaches **67.25%** using the Montgomery–Taylor kernel.

This project takes that result as the **new baseline** and explores what lies beyond.

## Starting point

| Milestone | Constant | Year | Method |
|-----------|----------|------|--------|
| Hardy | ∞ zeros on line | 1914 | — |
| Selberg | κ > 0 | 1942 | Mollifier |
| Levinson | 1/3 | 1974 | Mollifier |
| Conrey | 5/12 ≈ 0.4167 | 1989 | Refined mollifier |
| PRZZ | > 5/12 | 2020 | Further refinement |
| **Claude/Anthropic** | **2/3 ≈ 0.6667** | **2026** | **Pair-correlation + linear algebra** |
| Claude (optimised) | **0.6725** | 2026 | Montgomery–Taylor kernel |

## Architecture

Multi-model adversarial research panel, inspired by Anthropic's sub-agent methodology but with a key difference: **cross-model diversity**. Each model brings a different inductive bias.

| Role | Model | Platform | Why |
|------|-------|----------|-----|
| Orchestrator | GLM-5.2 | Ollama Cloud | Coordination, synthesis |
| Deep reasoning | Kimi K2.6 | Ollama Cloud | 1M ctx, long chains |
| Fast/parallel | DeepSeek V4 Flash | NaN Builders | Unlimited tokens, 0.6s |
| Alternate analysis | Qwen 3.6 | NaN Builders | Unlimited tokens, different bias |
| Verification | Cogito 2.1 | Ollama Cloud | Deep reasoning, second opinion |
| Community signals | Grok 4.5 | xAI | X firehose, real-time math discourse |
| Computation | Python/C++ | local | Numerical verification |

## Repository structure

```
riemann-conjecture/
├── README.md              ← This file
├── PROGRESS.md            ← Current state, what's been tried
├── references/            ← Key papers (PDFs, cloned repos)
│   ├── anthropic-claude-paper.pdf
│   ├── anthropic-mathematicians-note.pdf
│   ├── anthropic-claude-appendix.pdf
│   └── zeta-23-lean/      ← Lean 4 formalization (Anthropic)
├── literature/            ← Survey of the state of the art
├── theoretical/           ← Analytical approaches documented
├── computational/         ← Numerical verification code
├── negative-results/      ← Paths explored that did not work
├── notebook/             ← Research notebooks with full traceability
└── papers/               ← Preprints produced
```

## Scientific principles

1. **Reproducibility** — every step must be repeatable and give the same result
2. **Negative results are results** — document what doesn't work
3. **Traceability** — every claim has a commit, model, prompt, and output
4. **Radical honesty** — if we don't advance, we say so. Zero hype.
5. **Scientific standard** — paper format, citations, simulated peer review

## What this project is NOT

- Not an attempt to "solve RH" in a session
- Not a showcase — it's a laboratory
- Not independent of prior work — it builds on it explicitly

## License

MIT (code), CC-BY-4.0 (papers and documentation)

## Authorship

Elcano (AI navigator) with multi-model sub-agents. Human oversight: Chema Hontoria.