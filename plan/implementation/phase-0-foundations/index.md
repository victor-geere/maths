# Phase 0 — Foundations & Tooling

**Goal:** consolidate the general recipe and build the Python toolkit so that every subsequent phase can run its §6/§7 numerical verification programmatically.

---

## Status

| Item | File | Status |
|---|---|---|
| General recipe (damp → symmetrise → kernel) | `victor/spectral-triple.html` §3 | **Done** |
| `prime-zeros.py` — Z/P/G channels, helix, cone | `victor/prime-zeros.py` | **Partial** |
| `fibonacci_kernel`, `ou_mehler`, `eta_kernel` functions | [toolkit.md](toolkit.md) | **Open** |
| Spectral data sheet template | [../deliverables/spectral-data-sheet.md](../deliverables/spectral-data-sheet.md) | **Open** |

## Open actions

- [ ] Add `fibonacci_kernel(r, N, theta)`, `ou_mehler(t, x, y, N)`, `eta_kernel(r, sigma, theta)` to `victor/prime-zeros.py`.
- [ ] Create `deliverables/spectral-data-sheet.md` with one filled row (prime sine wave) as the template.
