# Zeros ↔ Primes Explicit Formula — Phase 3a

*Status: **conditional on RH** for the positivity claim; the explicit formula itself is unconditional.*

Current heuristic treatment is in `project/spectral-triple.md` (Theorem 6.1 proof sketch). This note will provide the rigorous conditional version.

---

## Goal

State the Weil–Guinand–Barner explicit formula with complete hypotheses and identify, step by step, which parts of the Theorem 6.1 proof sketch are unconditional and which require RH.

## The explicit formula (to be stated precisely)

For a suitable test function $f$ (Barner 1981 conditions: $f$ even, $\hat f$ compactly supported, $f \in L^1 \cap \mathrm{BV}$):

$$\sum_\rho f(\gamma_\rho) = \hat f(0) \cdot (\text{archimedean term}) - \sum_{n=1}^\infty \frac{\Lambda(n)}{\sqrt{n}} \hat f(\log n) + (\text{correction terms})$$

where $\rho = \tfrac{1}{2} + i\gamma_\rho$ are the nontrivial zeros (assuming RH for this form).

## Proof-sketch decomposition (from `project/spectral-triple.md` Thm 6.1)

| Step | Unconditional? | Notes |
|---|---|---|
| Zero kernel $K^\gamma$ positive definite | **Yes** | $\gamma_n > 0$, Bochner |
| Transfer kernel $K^\varepsilon_\mathrm{RH}$ trace-class | **Yes** | mollifier bound |
| $\mathrm{tr}(T_\varepsilon) = $ explicit formula sum | **Conditional** | requires zeros on critical line |
| Positivity of $T_\varepsilon$ ↔ all $\mathrm{tr}(T_\varepsilon f * \tilde f) \ge 0$ | **Conditional on RH** | this is the core claim |

## Open actions

- [ ] Transcribe the Barner (1981) hypothesis list; confirm the mollifier $e^{-\varepsilon|\gamma|}$ satisfies them.
- [ ] Write the unconditional portion of the argument as a standalone lemma.
- [ ] Clearly state Theorem 6.1 as: "**conditional on RH**, $T_\varepsilon \ge 0$; conversely, if $T_\varepsilon \ge 0$ for all $\varepsilon > 0$ then RH holds."
- [ ] Survey Bombieri–Lagarias for effective bounds (zero-free regions from explicit-formula positivity tests).
