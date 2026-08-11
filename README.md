# Advancing the Proportion of Riemann Zeta Zeros on the Critical Line

**A multi-model adversarial research program on the information barriers beyond the 2/3 bound.**

> **Preprint:** [`paper/main.tex`](paper/main.tex) — compiled PDF available in releases.
> **Live baseline:** Claude/Anthropic (2026-08-10) — ≥ 2/3 of non-trivial zeros on the critical line, unconditionally.

---

## Abstract

On 2026-08-10, Anthropic announced that Claude proved unconditionally that at least **2/3** of the non-trivial zeros of the Riemann zeta function ζ(s) lie on the critical line Re(s) = 1/2, with an optimised constant of **0.6725** via the Montgomery–Taylor kernel. This result was formalised in Lean 4 against Mathlib.

This repository takes that result as the **new baseline** and asks: *what would it take to push beyond 2/3?*

We conducted a systematic multi-model adversarial analysis across 10 research notebooks, 3 literature surveys, and 2 computational verifications. Six independent attack angles were explored: rank-trace inequality sharpening, SDP relaxation, non-commutative matrix structure, Hardy–Littlewood partial results, hybrid mollifier + pair-correlation methods, and higher-moment computation.

**Result:** The 2/3 bound is a **robust information barrier**. It is the optimal extraction from the two moments (tr(G), ‖G‖²_F) available unconditionally at bandwidth λ ≤ 1. No manipulation of this data—matrix inequalities, semidefinite programming, non-commutative structure, or hybrid methods—can improve it. Breaking the barrier requires **new data** (higher moments, bandwidth > 1, or zero-side information) or a **fundamentally different proof architecture**.

This is a negative result, but a precise one. It maps the frontier exactly and identifies the specific advances needed to push past 2/3.

---

## Historical context

| Result | Constant | Year | Method |
|--------|----------|------|--------|
| Hardy | ∞ zeros on line | 1914 | Moment method |
| Selberg | κ > 0 | 1942 | Mollifier |
| Levinson | ≥ 1/3 | 1974 | Mollifier |
| Conrey | ≥ 5/12 ≈ 0.4167 | 1989 | Refined mollifier |
| Pratt–Robles–Zaharescu–Zeindler | > 5/12 | 2020 | Further refinement |
| **Claude (Anthropic)** | **≥ 2/3 ≈ 0.6667** | **2026** | **Pair-correlation + linear algebra** |
| Claude (optimised) | **0.6725** | 2026 | Montgomery–Taylor kernel |
| Method ceiling | 0.68185 | — | Bandwidth-1 certificates |

---

## Key findings

### The 2/3 information barrier

The bound 2/3 is **tight** for the data available unconditionally. It was confirmed from six independent angles:

| # | Approach | Verdict | Why |
|---|----------|---------|-----|
| 1 | Rank-trace inequality | Tight | Extremal construction with eigenvalues {1^(2N/3), 2^(N/6), 0^(N/6)} saturates all classical inequalities |
| 2 | Ceiling analysis | Blocked | 0.68185 requires RH (pointwise integrality); 2/3 uses only aggregate integrality |
| 3 | SDP relaxation | Blocked | Chirre–Gonçalves–de Laat SDP needs F(α) on (1, 1+ε), equivalent to weak RH |
| 4 | Non-commutative structure | Blocked | Commutator [P,Q] is d²-dimensional; test functions cannot distinguish on-line from off-line zeros |
| 5 | Hardy–Littlewood partial | Blocked | No unconditional prime pair result gives bandwidth > 1; fundamental oscillation obstruction |
| 6 | Hybrid mollifier + pair-corr. | Blocked | Methods are redundant under RH, incompatible without RH |

### What would break the barrier

1. **Prove RH** → 0.68185 via pointwise integrality; full RH → 100%
2. **Prove Hardy–Littlewood** → bandwidth > 1, pushing toward 0.70+
3. **Compute tr(G³) unconditionally** → ~0.676 (needs triple correlations)
4. **Trilinear Kloosterman breakthrough** → from N^{1/20} to N^{1/2−ε} would give partial bandwidth > 1
5. **A fundamentally different proof architecture** — neither pair-correlation nor mollifier

---

## Repository structure

```
riemann-conjecture/
├── README.md                    ← This file
├── PROGRESS.md                  ← Research state and phase log
├── LICENSE                      ← MIT (code) + CC-BY-4.0 (docs)
├── CITATION.cff                 ← Citation metadata
│
├── paper/                       ← LaTeX preprint
│   ├── main.tex                 ← Full preprint
│   └── references.bib           ← Bibliography
│
├── notebook/                    ← Research notebooks (full traceability)
│   ├── 001-anthropic-baseline-audit.md
│   ├── 002-fase1-synthesis.md
│   ├── 003-fase2-computational-adversarial.md
│   ├── 003-rank-trace-analysis.md
│   ├── 004-ceiling-analysis.md
│   ├── 005-sdp-analysis.md
│   ├── 006-fase2-synthesis.md
│   ├── 007-noncommutative-structure.md
│   ├── 008-hardy-littlewood-partial.md
│   ├── 009-hybrid-methods.md
│   └── 010-fase3-synthesis.md
│
├── literature/                  ← State-of-the-art surveys
│   ├── survey-pair-correlation-frontier.md
│   ├── survey-non-pair-correlation-approaches.md
│   └── survey-physics-connections.md
│
├── computational/               ← Numerical verification
│   ├── verify_zeros.py          ← Zeta zero verification (mpmath)
│   ├── verify_gram_matrix.py    ← Gram matrix framework verification
│   ├── first-50-zeros.json      ← First 50 zeros data
│   ├── first-1000-zeros.json    ← First 1000 zeros data
│   └── gram-matrix-results.json ← Gram matrix verification results
│
└── references/                  ← Key reference materials
    ├── anthropic-claude-paper.pdf
    ├── anthropic-mathematicians-note.pdf
    ├── anthropic-claude-appendix.pdf
    └── zeta-23-lean/            ← Lean 4 formalization (Anthropic)
```

---

## Computational verification

Two scripts verify the framework numerically:

### Zeta zeros on the critical line

```bash
pip install mpmath
python computational/verify_zeros.py --T 100 --2T 200
```

All of the first 1000 non-trivial zeros of ζ(s) lie on Re(s) = 1/2 to 15 decimal places. Maximum deviation: |Re(s) − 1/2| = 0.

### Gram matrix framework

```bash
python computational/verify_gram_matrix.py
```

Verifies algebraically that ‖G‖²_F / tr(G) → 1/λ + λ/3 at λ ∈ {0.5, 0.75, 1.0}, yielding bounds −0.167, 0.417, and 0.667 respectively.

> ⚠️ **Numerical verification is not a proof.** These scripts serve as sanity checks and foundations for future experiments.

---

## Multi-model methodology

This project used a multi-model adversarial panel—inspired by Anthropic's sub-agent methodology but with **cross-model diversity**. Each model brings a different inductive bias, reducing the risk of shared blind spots.

| Role | Model | Platform | Contribution |
|------|-------|----------|--------------|
| Orchestrator | GLM-5.2 | Ollama Cloud | Coordination, synthesis, baseline audit |
| Deep reasoning | Kimi K2.6 | Ollama Cloud | Long-chain analysis, non-commutative structure |
| Fast analysis | DeepSeek V4 Flash | NaN Builders | Hardy–Littlewood partial, hybrid methods |
| Alternate bias | Qwen 3.6 | NaN Builders | Independent verification, ceiling analysis |
| Verification | Cogito 2.1 | Ollama Cloud | Second opinion on key barriers |
| Community signals | Grok 4.5 | xAI | Real-time math discourse on X |

**Adversarial design:** Each model attacked the 2/3 barrier from a different angle independently. Results were cross-checked for consensus. The six-angle agreement on the barrier's robustness is the core finding.

---

## Scientific principles

1. **Reproducibility** — every step is documented with model, prompt, and output
2. **Negative results are results** — we document what doesn't work and why
3. **Traceability** — every claim traces to a commit, a notebook, and a model run
4. **Radical honesty** — this project did NOT improve the 2/3 bound. We say so clearly.
5. **No hype** — the barrier is real. The mapping is precise. That's the contribution.

---

## What this project is — and is not

**Is:**
- A systematic mapping of the information-theoretic frontier beyond Claude's 2/3 result
- A negative result with precise identification of what's needed to push further
- A reproducible, traceable research process using multi-model adversarial analysis
- A survey of all known approaches, coded by whether they can help unconditionally

**Is not:**
- An attempt to "solve RH"
- An improvement on the 2/3 bound (there is none)
- A claim of mathematical theoremhood (the computational verifications are sanity checks, not proofs)
- Independent of prior work — it builds explicitly on Claude/Anthropic, Montgomery, Levinson, Conrey, and others

---

## Lean 4 formalization

The `references/zeta-23-lean/` directory contains Anthropic's Lean 4 formalization of the 2/3 result, verified against Mathlib's definition of ζ(s). This provides machine-checked assurance of the theorem.

See `references/zeta-23-lean/README.md` for build instructions.

---

## License

- **Code** (computational scripts, Python): **MIT**
- **Documentation** (notebooks, surveys, preprint, README): **CC-BY-4.0**

See [`LICENSE`](LICENSE) for full text.

---

## Citation

If you reference this work, please use the citation in [`CITATION.cff`](CITATION.cff) or:

```bibtex
@software{elcano_riemann_2026,
  author = {{Elcano Research Program}},
  title  = {Advancing the Proportion of Riemann Zeta Zeros on the Critical Line:
            A Multi-Model Research Program},
  year   = {2026},
  url    = {https://github.com/elCanosail/riemann-conjecture},
}
```

---

## Acknowledgements

- **Anthropic / Claude** — the 2/3 result and Lean 4 formalization that established the baseline
- **Montgomery, Levinson, Conrey, Selberg, Hardy** — the foundational results this builds upon
- **Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh** — the unconditional Montgomery framework
- **Chirre, Gonçalves, de Laat** — the SDP approach analysis
- **Alpöge, Furman** — the mathematicians' note on Claude's result

---

*Research conducted 2026-08-10 to 2026-08-11. Repo made public 2026-08-11.*