# CLAUDE.md — research/

**Not the same folder as `victor/research/`.** This is the track-1 circle-kernel catalogue's
structured research notes (phase-by-phase). `victor/research/` is PSC2, an unrelated standalone
offshoot of the track-2 Hilbert–Pólya/adèle work — see [victor/CLAUDE.md](../victor/CLAUDE.md).

## Repository structure

```
research/                 # structured research notes, one folder per phase
  index.md                # phase index with gate conditions and status
  todo.md                 # actionable task list (derived from plan/project.md)
  deliverables/
    spectral-data-sheet.md  # one row per catalogue object
  phase-0-foundations/
    toolkit.md            # Python functions to add to prime-zeros.py
  phase-1-rigorous-cases/
    prime-sine-wave.md    # Phase 1a research notes
    fibonacci-kernel.md   # Phase 1b research notes
    ou-process.md         # Phase 1c research notes
  phase-2-dirichlet-family/
    eta-zeta-transfer.md  # Phase 2a research notes
    spectral-triple.md    # Phase 2b research notes
    dirichlet-lf.md       # Phase 2c — not started
  phase-3-dynamical/
    explicit-formula.md   # Phase 3a — Weil/Barner explicit formula
    collatz.md             # Phase 3b — feasibility memo
  phase-4-generalisation/
    generalised-algorithm.md  # blocked until Phase 1 numerics done
  phase-5-helix-quaternion/
    helix-lift.md          # H1–H3 proved; H4 conjectural
    quaternionic-module.md # module definition open
```

These notes mirror the `project/` catalogue (see [project/CLAUDE.md](../project/CLAUDE.md)) and
implement the recipe in [victor/CLAUDE.md](../victor/CLAUDE.md) §Architecture. `research/index.md`
is the authoritative gate-condition/status table; `plan/project.md` (see
[plan/CLAUDE.md](../plan/CLAUDE.md)) is the master task list these phases map to.

Rigour tags, the RH declaration bar, and math-rendering convention are defined once in root
[CLAUDE.md](../CLAUDE.md) and bind every note in this folder unchanged.
