# PSC2-WP15 — the prolate pencil: E-track candidate 2 (the pre-registered escalation)

*Status: **open — chartered by the WP05 escalation** (7 Jul 2026). Created when WP05
executed and the W1 family closed as counting-law-only
([PSC2-F10](../findings/PSC2-F10-e4a-trace-consistency.md)–[F14](../findings/PSC2-F14-hs7-genealogy.md));
this WP is the escalation named in advance by F02's redesign note, WP02b's falsifier
branch, F08 and F09. Depends on: the WP05 harness (candidate-independent, delivered —
reused verbatim). All rules of I0 ([S06 §5](../sources/PSC2-S06-constraints-and-walls.md))
binding.*

## Objective

Replace the fixed-aperture wedge *basis* by finite stages of the genuinely quadratic
**prolate wave operator** (Connes–Moscovici 2022, [S00 §8](../sources/PSC2-S00-verified-foundation.md)):
the archimedean/time-band-limiting fiber whose semiclassical counting law is **proven**
to match $N(T)$ and whose window grows with the stage rather than sitting at fixed
aperture — the structural defect that closed W1 (F08 radii floor $\approx 1.72$; F09
quasi-mode floor $\ge 0.73$; F10–F14: stage-stable spectrum, counting law only).

## Inputs

- The prolate operator $W_\Lambda$ of Connes–Moscovici (PNAS 119 (2022)): self-adjoint
  extension of the band-limiting difference on $[0, \Lambda]$; negative spectrum
  numerically near $\{-\gamma_k^2\}$; counting theorem proven.
- The delivered E-track machinery: exact Gaussian/Hermite closed forms
  (`e0_density_gate.py`, `wp02b_rewindow.py`), the pencil/enclosure code path
  (`wp04_certified_enclosures.py`), the stage-resolution functional (`wp03_inclusion.py`),
  and the full evaluation harness (`wp05_evaluation_harness.py`) — all candidate-independent.
- The sieve inventory enters only through the arithmetic places, as in the semi-local
  trace ([S00 §6](../sources/PSC2-S00-verified-foundation.md)); no fitted parameter.

## Method (stages, each with its own bar)

1. **Matrix elements.** Exact (or certified-quadrature) matrix elements of the prolate
   quadratic form on an explicit finite basis; self-test at dps 35 against independent
   quadrature (the F07 pattern). The stage scale $\Lambda_n$ must be **derived** from the
   sieve cutoff $M_n$, not tuned.
2. **E0b re-run** (harness of F02/F07, unchanged): the derived counting law must be convex
   and the deviation sequence must pass the E0b rule. Connes–Moscovici's theorem is the
   proven precedent that this is attainable; it is *not* a substitute for the run (O6).
3. **E3b/E2 re-run** (F08/F09 machinery): certified radii and quasi-mode floors on
   $[0, 50]$. **The binding design requirement fixed now:** the certified floors must
   *decrease with stage* on the fixed window (the prolate window grows with $\Lambda_n$) —
   this is precisely what W1 provably could not do; if the prolate stages also floor out,
   the obstruction is not the window geometry and the E-track closes at L4 for
   fixed-basis-type programs generally.
4. **E4/HS re-run** (WP05 harness verbatim, including the decoy battery and the same
   budget discipline): the E4b resolution budget must be stated in advance against the
   *measured* stage-3 floors before any final evaluation.

## Falsifier / risk

- Stage-3 floors do not decrease $\Rightarrow$ the fixed-window resolution obstruction is
  not aperture-specific: report, close the candidate, and record the strengthened no-go
  profile (a genuine sharpening of O6/K2).
- E0b fails $\Rightarrow$ the implementation does not realise the proven counting theorem —
  an implementation finding, not a theorem finding; fix or close.
- Any control misbehaving in the reused harness invalidates the run (E4c/HS6 lines
  unchanged).

## Pre-registered criteria (fixed at chartering; sharpened before each run)

The bars of E0b, E3b, E2 and E4 are the existing WPs' bars, unmoved. New candidate-specific
bar (stage 3): certified quasi-mode floor on $[0, 50]$ strictly decreasing over $\ge 3$
consecutive stages. Per-run operationalisations are fixed in the script headers before
running, per the F-series convention.

## Deliverable

Builder + finding note per stage, criteria quoted verbatim; the harness comparison table
W1 vs prolate on identical gates (the first two-candidate line of the E-track).

## Pricing (binding)

Passing every stage here still decides nothing about zeros (O6; E5 completeness is the
wall, W1/W6). The value below the wall: a second, structurally different family measured
by the same certified gates — either a candidate that genuinely localises, or a proof-grade
demonstration that the obstruction is not the window.
