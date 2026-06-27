# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the code

```bash
# Python experiments (from repo root)
cd victor
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python prime-zeros.py          # prints R-range / peak; shows 3-D helix if matplotlib present
```

```bash
# Interactive manuscript — open in a browser (uses KaTeX + Plotly via CDN)
open victor/spectral-triple.html
```

No build step, no test runner. Numerical verification is done manually by comparing
script output against values recorded in the §6/§7 tables of each project note.

## Repository structure

```
victor/
  prime-zeros.py          # main numerical script: Z/P/G channels, helix lift, cone indicator
  spectral-triple.html    # interactive heuristic manuscript (KaTeX + Plotly, self-contained)
  requirements.txt        # numpy, matplotlib

project/                  # one Markdown note per catalogue object
  prime-sine-wave.md      # Phase 1a — COMPLETE (T1–T4 proved, §6 numerics done)
  fibonacci-kernel.md     # Phase 1b — proofs done (F1–F4), §6 numerics open
  ou-process.md           # Phase 1c — proofs done (O1–O5), §7 numerics open
  eta-zeta-transfer.md    # Phase 2a — proofs done (E1–E4), §5 numerics open
  spectral-triple.md      # Phase 2b — heuristic (Thm 6.1 is a proof sketch only)
  helix-quaternion-proposal.md  # Phase 5 — exploratory/conjectural

plan/project.md           # master task list with per-phase status tables
```

## Architecture: the one construction

Every note follows the same recipe applied to a different arithmetic sequence:

1. **Damp** the sequence with weights $w_n$ (geometric $r^n$, or Gaussian) to force convergence.
2. **Symmetrise**: $\lambda_n = \lambda_{-n} = a_n w_n$.
3. **Form the kernel**: $K(\theta) = \sum_{n \in \mathbb{Z}} \lambda_n e^{in\theta}$ — a real, even function on $\mathbb{T}$.

The convolution operator $T_K$ is self-adjoint on $L^2(\mathbb{T})$ with eigenvalues $\lambda_n$ (the damped sequence). Positive definiteness ↔ all $\lambda_n \ge 0$ (Bochner). The **transfer operator** between two objects is convolution with the *difference* of their kernels; the **explicit formula** is the trace identity that makes the zero-side and prime-side comparable.

`prime-zeros.py` implements this for the zeros↔primes case. Its three functions are the canonical numerical pattern to replicate for each new object:
- `channels(omega)` → the Z, P, G spectral channels
- `sign_aware_helix(omega, R)` → helix lift encoding sign as winding (Phase 5)
- `quaternion_cone(Z, P, G)` → positivity indicator $Z^2 - (P^2 + G^2)$

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

## Rigour convention

Every result must be tagged in one of three ways — maintain this distinction strictly:

- **proven** — complete proof present in the note
- **conditional** — depends on RH or another named hypothesis; state it explicitly
- **heuristic/exploratory** — conjecture or numerical evidence only

`prime-sine-wave.md` is the canonical template for a *proven* note (four theorems, honest §7 scope disclaimer, 10-digit numerical match). New notes should follow that structure.

Never assert that a framework implies RH unless it is provably tied to the zeros, not merely to the prime zeta singularity (see `prime-sine-wave.md` §7).

## Math rendering

Project notes use standard LaTeX math (rendered by GitHub's KaTeX). Avoid `\operatorname{}`— use `\mathrm{}` instead (GitHub's renderer disallows `\operatorname`).
