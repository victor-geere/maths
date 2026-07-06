# CLAUDE.md

This file guides Claude Code when working inside `victor/prime-sieve-continued/`.

## What this folder is

A **standalone, self-contained snapshot** of the Hilbert–Pólya / adèle "eigenvalue" track,
forked from the wider `maths` repo so it can be worked on without any file outside this folder.
The charter document is [research-plan.md](research-plan.md): it builds sieve-computable finite
self-adjoint matrices $H_n$ whose eigenvalues are tested against $\mathrm{Im}\,\rho=\pm\gamma$ of
the nontrivial zeros, gated E0–E5 as laid out there. Everything else in this folder is a copy of
the notes and scripts `research-plan.md`'s argument depends on, imported once and then rewired to
resolve locally.

**Do not assume this folder tracks the original files it was copied from.** Edits here (or to
`victor/adele/`, `victor/prime-sieve/`, `victor/berry-keating/`, `victor/flawed/` back in the main
tree) do not propagate either direction automatically.

## Running the code

```bash
# from repo root, same venv as the rest of the project
cd victor
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python prime-sieve-continued/adele/sieve_operator.py   # sieve, H_n, the vacuity flaw, repaired trace
python prime-sieve-continued/adele/adele_trace.py      # adelic place-by-place Weil trace + zero/prime balance

python prime-sieve-continued/prime-sieve/ihara-riemann-spectrums.py
python prime-sieve-continued/prime-sieve/ihara-zeta-convergence.py
python prime-sieve-continued/prime-sieve/numeric-verification.py
python prime-sieve-continued/prime-sieve/prime_graph_lab.py
```

```bash
# Interactive manuscripts — open in a browser (KaTeX + Plotly via CDN)
open victor/prime-sieve-continued/adele/prime-sieve-adele.html
open victor/prime-sieve-continued/berry-keating/prime-sieve.html
open victor/prime-sieve-continued/prime-sieve/ihara-connes.html
```

No build step, no test runner. Numerical verification is manual: compare script output against
the values quoted verbatim in each note's tables (`adele/phase6.md` and `adele/adele_trace.py`
are the anchor: the adelic trace is verified there to $10^{-36}$).

## Repository structure

```
prime-sieve-continued/
  research-plan.md        # THE CHARTER — read this first; §5 gates (E0–E5) drive all work here
  CLAUDE.md                # this file

  adele/                   # Phases 1–7 of the sieve-on-the-adèle-class-space construction
    index.md               # phase index / status table
    phase1.md … phase7.md  # phase1 sieve completeness; phase3/4 the corrected H_n' + refutation;
                            # phase6 the verified adelic trace ($10^{-36}$); phase7 the zero-side gap
    prime-side.md          # copy of the berry-keating unconditional prime-side package
    adele_trace.py          # Phase 6 numerics
    sieve_operator.py       # Phases 1,3,4 numerics
    adeles.py               # integer -> idèle representative helper
    prime-kernel.html, prime-sieve-adele.html, prime-sieve-adele-plan.html  # manuscripts

  prime-sieve/             # the Ihara/graph-determinant lab (framework #3 in the triage; toolkit only)
    closed-form.md          # the five closed-form frameworks, triaged in research-plan.md §1
    findings.md, path.md, implementation.md, notes.md, proof-sketch.md, new-research-plan.md
    ihara-connes.html
    ihara-riemann-spectrums.py, ihara-zeta-convergence.py, numeric-verification.py, prime_graph_lab.py

  berry-keating/           # the unconditional Hilbert–Pólya "prime side" package
    prime-side.md           # RKHS + von Mangoldt weights + operator-trace explicit formula
    research-findings.md    # the verified foundation — proven/conditional/RH-equivalent tagged
    worksheet.md            # audit trail: review, refutations, salvage log
    prime-kernel.html, prime-sieve.html, berry-keating-addendum-errata.html

  flawed/                  # graveyard: the discarded "arithmetic Berry–Keating" proof series,
                            # kept as an audit trail — every new candidate in this folder must
                            # face gates E0/E4 as regression tests against these refutations
    barry-keating-hp-1.html … hp-7.html
    barry-keating-hamiltonian-sieve.html, barry-keating-completing.html
    gate-1.md
```

Three links in this folder intentionally point back out to the main repo, because the content
they cite belongs to a different, unrelated track and was deliberately not copied in:
`adele/phase2.md` → `../../../plan/project.md`, `adele/phase5.md` →
`../../../research/phase-2-dirichlet-family/dirichlet-lf.md`, `prime-sieve/path.md` →
`../../../sympy/mcp_server.py`.

## The working object

`research-plan.md` §3.2 fixes the triage: framework #5 (finite self-adjoint matrices, here
redesigned as the sieve-Galerkin compression $H^G_n = P_n D P_n$) is the working expression;
framework #2 (the adèle class space operator $D$) is the target; the legacy $H_n'$ and the
graph/divisor operators in `prime-sieve/` are toolkit and negative controls, not the map itself.
Obstruction ledger and gates are §4–§5 of `research-plan.md`; do not re-derive them here — extend
that document.

## Rigour convention

Inherited unchanged from the main repo and binding on every note in this folder:

- **proven** — complete proof present in the note, or a classical result with citation
- **conditional** — depends on RH or another named hypothesis; state it explicitly
- **RH-equivalent** — proven *equivalent* to RH (e.g. Weil positivity, Connes' global trace
  formula). These mark the **frontier**; an RH-equivalent restatement is not itself a step toward
  a proof, and may never be presented as one.
- **heuristic/exploratory** — conjecture or numerical evidence only

Do not assert that a construction implies RH unless the chain is tied to the zeros themselves,
not merely to a density/trace match or an RH-equivalent restatement standing in for the
conclusion — see `flawed/` for the discarded series that made exactly that mistake, refuted at
three independent, provable points (`berry-keating/worksheet.md` is the audit trail).

### Declaring RH proven

An unconditional proof of RH is a permitted outcome of work in this folder — the door is open,
per `research-plan.md` §0's honest framing. But it may be claimed only at the full bar:

- every link in the chain is itself tagged **proven** — nothing **conditional**, nothing
  **heuristic**, and no **RH-equivalent** restatement substituting for the conclusion;
- the chain terminates in a statement about the nontrivial zeros $\rho=\tfrac12+i\gamma$
  themselves, reached explicitly — not merely in positivity of a kernel, spectral density
  matching, or trace-level agreement (gate E5 in `research-plan.md` is priced, not attacked);
- the argument survives independent verification — symbolic and numerical — and an adversarial
  read-through looking specifically for the gap;
- until all of the above hold, RH stays tagged **open**.

This opens the door to a proof; it does not lower the threshold for claiming one. Do not present
gate progress (E0–E4) as "approaching RH" — see the do-not list in `research-plan.md` §8.

## Math rendering

Notes use standard LaTeX math (rendered by GitHub's KaTeX). Avoid `\operatorname{}` — use
`\mathrm{}` instead (GitHub's renderer disallows `\operatorname`).
