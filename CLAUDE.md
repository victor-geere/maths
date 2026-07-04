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
# Hilbert–Pólya / adèle track (needs mpmath; same .venv)
python adele/sieve_operator.py   # Phases 1,3,4: sieve, H_n, the vacuity flaw, repaired trace
python adele/adele_trace.py      # Phase 6: adelic place-by-place Weil trace + zero/prime balance
```

```bash
# Interactive manuscripts — open in a browser (KaTeX + Plotly via CDN)
open victor/spectral-triple.html
open victor/adele/prime-sieve-adele.html
```

No build step, no test runner. `requirements.txt` pins `numpy`, `matplotlib`, `mpmath`,
`streamlit`. Numerical verification is done manually by comparing script output against the values
recorded in the §6/§7 tables of each project note (the adèle track quotes `adele_trace.py` /
`sieve_operator.py` output verbatim in its phase notes).

## Repository structure

```
victor/
  prime-zeros.py          # main numerical script: Z/P/G channels, helix lift, cone indicator
  spectral-triple.html    # interactive heuristic manuscript (KaTeX + Plotly, self-contained)
  series-spectrum-circle.html  # additional interactive visualisation
  requirements.txt        # numpy, matplotlib
  notes/                  # (empty — scratch space)
  barry-keating/          # Hilbert–Pólya "prime side" track (see §Two tracks)
    research-findings.md  # the verified foundation — only what is proven, tagged proven/conditional/RH-equivalent
    prime-side.md         # unconditional spectral package (RKHS + von Mangoldt weights + operator-trace explicit formula)
    worksheet.md          # audit trail: review, refutations, salvage log
    prime-kernel.html / prime-sieve.html / hermite-biehler.html / research-findings.html / *-errata.html
  adele/                  # Prime sieve on the adèle class space (Connes trace formula)
    index.md              # implementation index — 6 phases, per-phase status
    phase1.md … phase6.md # staged notes; phase6 is the working construction (trace verified to 1e-36)
    prime-side.md         # (copy of the barry-keating prime-side package, measured against)
    sieve_operator.py     # Phases 1,3,4: sieve, H_n, the vacuity flaw, repaired trace
    adele_trace.py        # Phase 6: adelic place-by-place Weil trace + zero/prime balance
    adeles.py / adeles2.py  # supporting numerics
    prime-kernel.html / prime-sieve-adele*.html # source program + visualisations
  flawed/                 # graveyard: discarded RH-proof attempts, kept as an audit trail
    barry-keating-hp-1.html … hp-7.html  # the refuted "arithmetic Berry–Keating" proof series
    barry-keating-hamiltonian-sieve.html / barry-keating-completing.html

leo/                      # (empty — scratch space, .gitkeep only)

project/                  # one Markdown note per catalogue object
  prime-sine-wave.md      # Phase 1a — COMPLETE (T1–T4 proved, §6 numerics done)
  fibonacci-kernel.md     # Phase 1b — proofs done (F1–F4), §6 numerics open
  ou-process.md           # Phase 1c — proofs done (O1–O5), §7 numerics open
  eta-zeta-transfer.md    # Phase 2a — proofs done (E1–E4), §5 numerics open
  spectral-triple.md      # Phase 2b — heuristic (Thm 6.1 is a proof sketch only)
  helix-quaternion-proposal.md  # Phase 5 — exploratory/conjectural

plan/
  project.md              # master task list with per-phase status tables

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
    collatz.md            # Phase 3b — feasibility memo
  phase-4-generalisation/
    generalised-algorithm.md  # blocked until Phase 1 numerics done
  phase-5-helix-quaternion/
    helix-lift.md         # H1–H3 proved; H4 conjectural
    quaternionic-module.md  # module definition open

library/                  # reference library, one folder per subject area
  content/
    01-foundations-logic/
    02-algebra/
    03-number-theory/
    ...                   # 30 subject folders total
  index.md

sympy/                    # SymPy MCP verification server
  mcp_server.py           # MCP server exposing simplify / verify tools
  requirements.txt
  environment.yml
  CLAUDE.md               # sympy-specific guidance
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

## Two tracks

The repository now runs **two complementary attacks** on the same object, and new work
should be filed under whichever it belongs to:

1. **The circle-kernel recipe** (above) — the `project/` and `research/` notes, catalogue of
   sequences → self-adjoint convolution operators → transfer operators. Goal: the generalised
   algorithm.
2. **The Hilbert–Pólya "prime side"** — `victor/barry-keating/` and `victor/adele/`. Instead of
   damping a sequence onto the circle, it builds the arithmetic side of the Guinand–Weil explicit
   formula as a genuine operator trace, and (Phase 6) realises it place-by-place on the adèle class
   space $X=\mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times$ à la Connes. `barry-keating/prime-side.md` is
   the unconditional package; `adele/adele_trace.py` reproduces the trace to $10^{-36}$. This track
   *reproduces* the explicit formula; it does **not** decide RH (see the rigour convention).

Both tracks obey the same rigour convention. The `victor/flawed/` folder is deliberately kept: it
holds a discarded `barry-keating-hp-*` series that *claimed* a proof of RH and was refuted at three
independent, provable points — the standing reminder of why the guardrails below exist.

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

### Hilbert–Pólya / adèle track (`victor/barry-keating/`, `victor/adele/`)

Not on the original 16-item board; added in the current branch. Status per note:

| Object | Where | Status |
|---|---|---|
| Composite-generator sieve; equidistribution of normalised primes | `barry-keating/research-findings.md`, `adele/phase1.md` | **proven** (numerics confirm) |
| Unconditional prime-side package (RKHS + von Mangoldt weights + operator-trace explicit formula) | `barry-keating/prime-side.md` | **proven**, but boundary/positivity claims are **RH-equivalent**, not a proof |
| Finite "Sieving Laplacian" $H_n=D_n+\varepsilon_n A$ | `adele/phase3.md` | **flaw found** — $A\equiv0$, vacuous; repair has wrong spectral density |
| Eigenvalues $\to$ zeros (Conjecture 5.1) | `adele/phase4.md` | **refuted** — contradicted by a theorem *and* numerics |
| Adèle place-by-place Weil trace (Connes) | `adele/phase6.md`, `adele/adele_trace.py` | **proven** trace identity (imported), verified to $10^{-36}$ |

Open items on this track: define the quaternionic/adelic operator rigorously; state and test the
truncation-rate bound $O(M_n^{-1/2})$; keep the salvaged results separate from the refuted ones.

## Rigour convention

Every result must be tagged — maintain these distinctions strictly:

- **proven** — complete proof present in the note, or a classical result with citation
- **conditional** — depends on RH or another named hypothesis; state it explicitly
- **RH-equivalent** — proven *equivalent* to RH (e.g. Weil positivity, Hermite–Biehler positivity, Connes' global trace formula). These mark the **frontier**; an RH-equivalent restatement is not itself a step toward a proof, and may never be presented as one.
- **heuristic/exploratory** — conjecture or numerical evidence only

`prime-sine-wave.md` is the canonical template for a *proven* note (four theorems, honest §7 scope disclaimer, 10-digit numerical match). `victor/barry-keating/prime-side.md` is the template for an unconditional *package* built toward Hilbert–Pólya. New notes should follow one of those structures.

Do not assert that a framework implies RH unless it is provably tied to the zeros, not merely to the prime zeta singularity (see `prime-sine-wave.md` §7) or to an RH-*equivalent* restatement standing in for the conclusion (see `victor/flawed/`: the discarded `barry-keating-hp-*` series claimed a proof and was refuted at three independent, provable points).

### Declaring RH proven

An unconditional proof of RH **is a permitted outcome of this project** — the door is open. But it may be claimed only at the full bar, and the bar does not move:

- every link in the chain is itself tagged **proven** — nothing **conditional**, nothing **heuristic**, and no **RH-equivalent** restatement substituting for the conclusion;
- the chain terminates in a statement about the nontrivial zeros $\rho=\tfrac12+i\gamma$ themselves (their location), reached explicitly — not merely in positivity of a kernel, a singularity of the prime zeta, or the density/trace matching;
- the argument survives independent verification — symbolic (via the `sympy-verifier` MCP server) and numerical — and an adversarial read-through looking specifically for the gap (that is how the `flawed/` series was caught);
- until all of the above hold, RH stays tagged **open**, exactly as every current note states it is.

This convention *opens the door to a proof; it does not lower the threshold for claiming one.* If a genuine proof is assembled, say so plainly and unhedged (see the harness rule on reporting outcomes faithfully); short of that, do not hint that the project is "close."

## Math rendering

Project notes use standard LaTeX math (rendered by GitHub's KaTeX). Avoid `\operatorname{}`— use `\mathrm{}` instead (GitHub's renderer disallows `\operatorname`).
