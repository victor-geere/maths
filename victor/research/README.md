# PSC2 — Prime Sieve Continued, plan 2 (standalone research project)

A self-contained research project extracted from `victor/prime-sieve-continued/` on
6 Jul 2026. Everything the plan builds on is inside this folder: the source documents are
distillations (with proofs where load-bearing) of that snapshot's `adele/`, `berry-keating/`,
`prime-sieve/`, `flawed/gate-1.md`, and the two harmonic-sine manuscripts; the numeric anchors
ship as runnable scripts. Nothing here requires a file outside `victor/research/`.

**Read first:** [PSC2-000-charter.md](PSC2-000-charter.md) (the plan) and
[PSC2-001-conventions.md](PSC2-001-conventions.md) (rigour tags, evidence hygiene, naming,
the declaration bar). **RH is open**; the charter's status ledger is the single source of
truth for what is proven, open, dead, or a wall.

## Layout and numbering

`PSC2-<series><nn>-<slug>.md` — series `0` governance, `S` sources, `WP` work packages,
`N` numerics, `F` findings (see PSC2-001 §1).

```
research/
  README.md                          this file
  PSC2-000-charter.md                THE PLAN — unified picture, inventory, triage, ordering
  PSC2-001-conventions.md            rigour tags · evidence hygiene I0 · naming · declaration bar
  sources/
    PSC2-S00-verified-foundation.md  proven compendium: sieve, trace identity, adelic Weil
                                     trace (10^-36), truncation rate, Meyer, Connes–Moscovici,
                                     F4/F8 calibrations, I0 origin  [adapted references.md]
    PSC2-S01-character-level.md      L2: flow character χ_W; circularity theorem; what the
                                     zero side needs (walls)
    PSC2-S02-determinant-level.md    L3: stage objects, Hurwitz dictionary, H*, findings
                                     F1–F10, gate state G1–G6
    PSC2-S03-eigenvalue-level.md     L4: Lemma 0, triage K1/K2, H^G_n design, density law,
                                     obstructions O1–O6, E-gates
    PSC2-S04-model-pair.md           harmonic sine ↔ Xi: greedy Egyptian stages (proven),
                                     moment identities, pairing law, HS-gate statements,
                                     misuse fences (X8/X9)
    PSC2-S05-salvaged-G1.md          the weighted Ihara–Bass resolvent identity, salvaged
                                     from flawed/gate-1.md, with audit obligations
    PSC2-S06-constraints-and-walls.md  N1–N4 · D1/D2 · M1–M5 · density mismatch ·
                                     X-ledger (dead ends) · W-ledger (walls) · rule I0
  workpackages/
    PSC2-WP01 … PSC2-WP14            one open problem each: objective, inputs, method,
                                     falsifier, pre-registered criteria, status
  numerics/
    PSC2-N00-verification-targets.md regression numbers every run must reproduce
    adele_trace.py                   L1 anchor: adelic place-by-place Weil trace (10^-36)
    sieve_operator.py                sieve, vacuity demo, repaired trace
    prime_graph_lab.py               bipartite divisor graph lab (F2–F9 reproduction)
  findings/
    PSC2-F00-template.md             finding-note template (pre-registered criteria verbatim)
```

## Running the numerics

```bash
cd victor && python -m venv .venv && source .venv/bin/activate
pip install numpy mpmath
python research/numerics/adele_trace.py      # must reproduce N00 §1 (balance ~1e-36)
python research/numerics/sieve_operator.py   # must reproduce N00 §2 tables
python research/numerics/prime_graph_lab.py  # must reproduce N00 §3 (F2/F3/F4 rows)
```

Numerical verification is manual: compare output against
[numerics/PSC2-N00-verification-targets.md](numerics/PSC2-N00-verification-targets.md).
A mismatch is a finding (file it under `findings/`), not a formatting nit.

## Provenance

Parent snapshot: `victor/prime-sieve-continued/` (which is itself a standalone fork of the
wider `maths` repo). Edits do not propagate in either direction. Archival pointers of the form
`adele/…`, `prime-sieve/…` inside S00 refer to that snapshot and are retained for audit only —
the extracted content is complete without them. Results that land **proven** here should be
reflected back in the parent snapshot's status tables per repo convention.
