# CLAUDE.md — plan/

`plan/project.md` is the master task list for the circle-kernel track (track 1 — see root
[CLAUDE.md](../CLAUDE.md) §Two tracks), derived from `project/` and root-level `research/` notes.

## Open work (GitHub project board → plan/project.md)

All 16 items on [the project board](https://github.com/users/victor-geere/projects/1) are in **Todo**. They map directly to tasks in `plan/project.md`:

| Phase | Item | Key action |
|---|---|---|
| 0 | Extend `prime-zeros.py` | Add `fibonacci_kernel`, `ou_mehler`, `eta_kernel` functions |
| 0 | Create `project/spectral-data-sheet.md` | Template row; fill as objects are verified |
| 1b | Fibonacci §6 numerics | Verify $K_r(0)$, PD grid, eigenvalues, Parseval |
| 1b | Lucas transfer multiplier | Prove $L_n = F_{n-1} + F_{n+1}$ as bounded multiplier + trace identity |
| 1c | OU §7 numerics | Mehler, trace, heat kernel, Mellin $\Gamma\zeta$ (use `mpmath`) |
| 1c | $L^2(\gamma) \to L^2(\mathbb{T})$ functor | Formalise as bounded intertwining map |
| 2a | $\eta$↔$\zeta$ §5 numerics | Verify rotation identity, extra zeros, transfer correction |
| 2a | Measure-level equality | Prove extra mass at $\{k \log 2\}$ with coefficients $1/k$ |
| 2b | Thm 6.1 proof | Upgrade sketch to full proof or precise Weil/Barner citation |
| 2b | Effective-bound survey | Bombieri–Lagarias zero-free regions via explicit formulas |
| 2c | `project/dirichlet-series.md` | Kernel ↔ functional-equation dictionary for $L(s,\chi)$ |
| 3a | Weil explicit formula | Barner 1981 version; flag conditional vs. unconditional steps |
| 3b | Collatz feasibility memo | Before committing a full note |
| 5 | Quaternionic Hilbert module | Precise definition; consult Colombo–Sabadini–Struppa |
| 5 | H4 proof attempt | $D_t = -j\partial_t$ self-adjoint in S-spectrum sense |
| 5 | H4 numerical test | Cone indicator on $\eta$ kernel after helix lift |

**Do not start Phase 4** (generalised algorithm) until Phase 1 numerics (1b, 1c) are done and the $L^2(\gamma) \to L^2(\mathbb{T})$ functor is formalised.

The Hilbert–Pólya/adèle track (`victor/berry-keating/`, `victor/adele/`) is not on this board — see
its own status table in [victor/CLAUDE.md](../victor/CLAUDE.md).

Rigour tags, the RH declaration bar, and math-rendering convention are defined once in root
[CLAUDE.md](../CLAUDE.md) and bind here unchanged.
