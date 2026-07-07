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
  manuscript.md                      the program manuscript: abstract, all four levels,
                                     findings F01-F07, relation to RH, adjacent concepts,
                                     further research, alternative routes, PSC3 sketch
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
    PSC2-WP01 … PSC2-WP15            one open problem each: objective, inputs, method,
                                     falsifier, pre-registered criteria, status
    PSC2-WP02b-density-gate-rewindow.md  the E0 rewindow: W1 wedge builder (F02's redesign
                                     note, pre-registered) — done, passed (F07)
    PSC2-WP15-prolate-pencil.md      E-track candidate 2 (Connes–Moscovici prolate
                                     pencil) — chartered by the WP05 escalation after
                                     the W1 counting-law-only closure (F10–F14)
  numerics/
    PSC2-N00-verification-targets.md regression numbers every run must reproduce
    adele_trace.py                   L1 anchor: adelic place-by-place Weil trace (10^-36)
    sieve_operator.py                sieve, vacuity demo, repaired trace
    prime_graph_lab.py               bipartite divisor graph lab (F2–F9 reproduction)
    pairing_lemma_check.py           E1/HS5 numerical controls (F01)
    e0_density_gate.py               N0 stage builder + gate E0 harness and controls (F02)
    wp02b_rewindow.py                W1 wedge builder + gate E0b (rewindowed density gate,
                                     harness reused from e0_density_gate) (F07)
    wp04_certified_enclosures.py     E3b certified enclosures: second-order relative
                                     spectra of the (D, D^2) pencil on the W1 family,
                                     radii genealogy + controls + certification (F08)
    wp03_inclusion.py                E2 inclusion criterion on the W1 family: stage
                                     resolution r_n(lambda), spectral gaps/holes,
                                     prototype + exhausting-Gabor controls (F09)
    wp03_inclusion_supplement.py     F09's labelled post-hoc supplement: the n=12
                                     fine-grid certified floor (~90 min)
    wp06_bass_certify.py             exact Q-certification of the weighted Ihara–Bass
                                     identity on stage graphs n<=6 (F03 Part A)
    wp06_locus_check.py              2-core radii, annulus containment, census (F03 Part B)
    wp07_gap_census.py               normalised-gap census n<=15 + uniform-gap theorem
                                     ingredient checks (F04)
    wp08_beta_sweep.py               detached-census beta-sweep (n<=12) + edge-purity
                                     theorem ingredient checks (F05)
    wp13_asano_gluing.py             sieve-step gluing law (exact Q certification n<=6),
                                     Asano/GWS chain, locus coverage, controls (F06)
    wp05_evaluation_harness.py       the E4 + HS evaluation harness: E4a trace gate,
                                     E4b matched displacement (final evaluation), HS1
                                     product gate, HS2 moment gate, HS7 genealogy, and
                                     the E4c/HS6 control battery (h.o. positive control,
                                     nested bare-wedge decoy, sine decoy, negatives);
                                     candidate-independent — reused by WP15 (F10–F14)
  findings/
    PSC2-F00-template.md             finding-note template (pre-registered criteria verbatim)
    PSC2-F01-pairing-lemma.md        E1 + HS5 proven; controls at machine precision
    PSC2-F02-density-gate.md         E0 run: primary H^G_n killed; no-go lemma; N0 delivered
    PSC2-F03-weighted-locus.md       G1 audit closed: Ihara–Bass identity proven; honest
                                     weighted locus (weak annulus); WP08 re-scoped
    PSC2-F04-normalised-gap.md       G3 base theorem proven (uniform gap, explicit c);
                                     census flat ~0.566 to n=15; sharp constant open
    PSC2-F05-anti-siegel.md          G4: edge-purity theorem proven (all n, all beta);
                                     beta-sweep fired the falsifier — "exactly 4 detached"
                                     is a window artifact; real census clean everywhere
    PSC2-F06-asano-gluing.md         G6/Q-γ2: sieve-step gluing law proven (Green-quadratic
                                     multiplier); no zero locus survives — falsifier fired,
                                     route γ closed (X13)
    PSC2-F07-density-rewindow.md     E0b run: wedge-windowed H^{G,w}_n passes; E-track
                                     reopened; per O6 not evidence about zeros
    PSC2-F08-certified-enclosures.md E3b run: pencil gate passes (radii decreasing, harness
                                     valid, machinery certified); radii saturate at floor
                                     ~1.72 on [0,50] — resolution caveat for WP03/WP05
    PSC2-F09-inclusion-theorem.md    E2: ambient record (E2a) + inclusion criterion,
                                     prototype and coarse-inclusion theorems proven (E2b);
                                     W1 window fails graph-density on fixed windows —
                                     falsifier branch, quantified (certified r_n floors)
    PSC2-F10-e4a-trace-consistency.md  WP05 harness note: control battery valid; E4a
                                     fails by persistent excess = the sub-gamma_1
                                     counting surplus, quantified
    PSC2-F11-e4b-matched-displacement.md  E4b: letter rule passes on sub-resolution
                                     drift, certified rule and decoy comparison do not —
                                     W1 family closes as counting law only; WP15 chartered
    PSC2-F12-hs1-product-gate.md     HS1: Xi_n diverges from Xi on [0,30] — conjectured
                                     implication refuted for W1
    PSC2-F13-hs2-moment-gate.md      HS2: gamma-free moment gate fires (2.2x targets,
                                     errors increasing with stage)
    PSC2-F14-hs7-genealogy.md        HS7: 15/17 certified chains persist, drift 0.026 —
                                     the pollution is structural, not transient
```

## Running the numerics

```bash
cd victor && python -m venv .venv && source .venv/bin/activate
pip install numpy mpmath
python research/numerics/adele_trace.py      # must reproduce N00 §1 (balance ~1e-36)
python research/numerics/sieve_operator.py   # must reproduce N00 §2 tables
python research/numerics/prime_graph_lab.py  # must reproduce N00 §3 (F2/F3/F4 rows)
python research/numerics/pairing_lemma_check.py         # must reproduce F01's control block
cd research/numerics && python e0_density_gate.py       # must reproduce F02 (self-test,
                                             # N00 regression, E0 tables, verdict)
pip install sympy                            # needed by wp06_bass_certify.py only
python research/numerics/wp06_bass_certify.py  # must reproduce F03 Part A (exact, ~2 min)
python research/numerics/wp06_locus_check.py   # must reproduce F03 Part B (census, radii)
python research/numerics/wp07_gap_census.py    # must reproduce F04 (census + ingredients)
pip install scipy                            # optional: wp08's n=12 anchor point only
python research/numerics/wp08_beta_sweep.py    # must reproduce F05 (sweep, incl. the six
                                             # DEVIATION rows — they are data, not defects)
python research/numerics/wp13_asano_gluing.py  # must reproduce F06 (lemmas, exact chain
                                             # certification, injection census, controls)
cd research/numerics && python wp02b_rewindow.py  # must reproduce F07 (self-test, N00
                                             # regression, E0b tables, controls, verdict)
cd research/numerics && python wp04_certified_enclosures.py  # must reproduce F08 (regressions,
                                             # enclosure tables, genealogy, controls, verdict;
                                             # ~15 min — the n=12 companion eigensolve; 'fast'
                                             # drops n=12)
cd research/numerics && python wp03_inclusion.py  # must reproduce F09 (regressions, r_n
                                             # profiles + certified floors, gap/hole table,
                                             # controls, verdict; 'fast' drops n=12)
cd research/numerics && python wp05_evaluation_harness.py  # must reproduce F10–F14
                                             # (regressions incl. N00 §1 adelic anchors,
                                             # stage data, E4a/HS2/HS1/HS7 tables, control
                                             # battery, final evaluation, verdict; ~20 min
                                             # — the n=12 builds; 'fast' drops n=12)
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
