# Research Index — Spectral Number Theory

Pipeline: `sequence → damped kernel → self-adjoint operator → spectrum → transfer operator → explicit formula`

See [README.md](../README.md) for the full mathematical setting and [plan/project.md](../plan/project.md) for the task-level status.

---

## Phases

| Phase | Folder | Gate condition | Status |
|---|---|---|---|
| 0 — Foundations & tooling | [phase-0-foundations/](phase-0-foundations/) | — | Partial |
| 1 — Rigorous cases | [phase-1-rigorous-cases/](phase-1-rigorous-cases/) | — | Proofs done; numerics open |
| 2 — Dirichlet family | [phase-2-dirichlet-family/](phase-2-dirichlet-family/) | — | Partial |
| 3 — Dynamical / hard | [phase-3-dynamical/](phase-3-dynamical/) | Independent of 4/5 | Not started |
| 4 — Generalisation | [phase-4-generalisation/](phase-4-generalisation/) | Phase 1 numerics + L²(γ)→L²(𝕋) functor | Sketch drafted; gate partly discharged (only Fibonacci §6 open) |
| 5 — Helix / quaternion | [phase-5-helix-quaternion/](phase-5-helix-quaternion/) | Quaternionic module defined | Exploratory |

## Deliverables

| Deliverable | File | Status |
|---|---|---|
| Spectral data sheet (one row per object) | [deliverables/spectral-data-sheet.md](deliverables/spectral-data-sheet.md) | Partial |
| Computational toolkit | [phase-0-foundations/toolkit.md](phase-0-foundations/toolkit.md) | Partial |
| Generalised algorithm write-up | [phase-4-generalisation/generalised-algorithm.md](phase-4-generalisation/generalised-algorithm.md) | Sketch drafted (Tier A/B ready; Tier C deferred) |

## Rigour key

Every result in every note must be tagged:

- **proven** — complete proof present
- **conditional on [hypothesis]** — state the hypothesis explicitly
- **heuristic** — conjecture or numerical evidence only
