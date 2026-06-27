# Spectral Triple / RH Framework — Phase 2b

*Full note at [project/spectral-triple.md](../../project/spectral-triple.md). Also see interactive manuscript `victor/spectral-triple.html`.*

*Status: **heuristic**. The central claim (Theorem 6.1) is equivalent to RH and is therefore as hard as RH. Treat everything here as exploratory until a complete proof or a precise conditional statement is in place.*

---

## Status

| Result | Status |
|---|---|
| Zero kernel positive definite (unconditional) | **Proved** |
| Transfer kernel $K^\varepsilon_\mathrm{RH}$ defined and trace-class | **Proved** |
| Theorem 6.1: RH ↔ positivity of $T_\varepsilon$ | **Heuristic** (proof sketch only) |
| Quaternionic positivity Theorem 7.1 | **Heuristic** |
| Numerical test (30 zeros, primes ≤ 100) | **Done** (in HTML) |
| Effective bound: verification up to $\omega = T$ → no zeros below $T$ | **Open** |
| Mollifier → closed-form kernel as $\varepsilon \to 0$ | **Open** |
| $T_\varepsilon$ spectrum as $\varepsilon \to 0$ | **Open** |

## Open actions

- [ ] Restate Theorem 6.1 as a conditional: identify exactly which step requires RH and which is unconditional. Cite Weil (1952) and Barner (1981) for the explicit formula; cite Connes (1999) for the spectral interpretation.
- [ ] Survey Bombieri–Lagarias zero-free regions via explicit formulas; add to the open-questions section.
- [ ] Port the HTML numerical test to `prime-zeros.py`; extend to 100+ zeros and vary $\varepsilon$.
