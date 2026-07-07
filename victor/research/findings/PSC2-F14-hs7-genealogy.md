# PSC2-F14 — HS7, the enclosure genealogy: 15 of 17 certified chains persist across all five stages with median drift 0.026 — the pollution is structural, not transient

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP05](../workpackages/PSC2-WP05-evaluation-harness.md). Code/run: the same
deterministic run as [PSC2-F10](PSC2-F10-e4a-trace-consistency.md) (harness validity,
regression record, disclosures there); intervals from the F08 pencil code path
(`wp04_certified_enclosures.py`), recomputed at every stage. Tags per
[PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP and S04 §7 before the run)

> - **HS7 — enclosure genealogy.** Persistence chains of WP04's certified intervals across
>   stages; chain breaks localize pollution ([S04 §7](../sources/PSC2-S04-model-pair.md)).

> Do the certified E3b enclosure intervals form persistent chains across stages, with
> chain displacements decreasing at a measured rate? An intrinsic, parameter-free
> "sweep"; chain breaks localize pollution events. […] **exploratory**, falsifier built
> in.

Operationalisation (header, fixed before the run): link rule between consecutive stages
at aligned index $k$ — intervals overlap **and** $|\text{centre shift}| \le
(r_{k,n} + r_{k,n+1})/2$; report unbroken chains, breaks, per-chain total centre drift,
shared-interval multiplicities. Report-only (the WP sets no pass bar); guard: F08 $n=4$
anchors (min radius $1.3387$, median $1.7411$, tol $5\times10^{-4}$) and the
$r$/radius coherence check reproduced first (they were — F10's regression block).

## Regression check

Via [F10](PSC2-F10-e4a-trace-consistency.md) (same run): all anchors reproduced,
including the F08 pencil anchors and quasi-mode coherence; harness valid.

## Result

```
HS7 — ENCLOSURE GENEALOGY  persistence chains of certified intervals  [W1]
  aligned interval count across stages: 17  (per stage: [17, 17, 17, 17, 17])
  unbroken chains across all computed stages: 15 / 17
    BREAK at interval k=10 between n=4 and n=6 (localised pollution event)
    BREAK at interval k=15 between n=4 and n=6 (localised pollution event)
  per-chain total centre drift: min = 0.0016  median = 0.0258  max = 3.4916
  shared-interval multiplicities at n=12: [2, 2] (2 shared intervals; F08 fingerprint)
```

The numbers say: the genealogy is **fully persistent from $n = 6$ onward** — every one
of the 17 certified intervals on $[0, 50]$ chains through $n = 6, 8, 10, 12$ unbroken.
The only two breaks sit at the $n = 4 \to 6$ transition, at exactly the two genealogy
rows ($k = 10, 15$) where F08's published radii table already showed root re-assignment
(the $k=10$ radius drops $2.026 \to 1.757$ and $k=15$ jumps $1.339 \to 1.503$ as
matched roots re-pair) — the link rule localises the early re-arrangement events and
nothing else. Median total centre drift over four stage transitions is $0.026$ —
**seventy times smaller than the certified radius floor** $1.72$ (F08): the intrinsic,
parameter-free "sweep" shows the certified picture frozen, consistent with F09's
$9.2\times10^{-4}$ mobility and with the E4b letter-drift of
[F11](PSC2-F11-e4b-matched-displacement.md). (The max drift $3.49$ belongs to chain
$k = 12$, the widest interval, whose root wanders within its own radius — flagged by
size, not by a break.) Multiplicity note: at $n = 12$, 2 intervals are shared by
matched-root *index* (F08's "distinct 15/17"); by interval geometry — conjugate pencil
roots give identical centre/radius — 4 adjacent eigenvalue pairs share intervals, F08's
published fingerprint; the two counts are the same fact at two granularities.

**The design purpose, answered.** HS7 was built so that *chain breaks* would localise
pollution events. The run's answer is sharper: the pollution here is **not transient** —
no chain ever breaks after $n = 6$; in particular the two sub-$\gamma_1$ chains
($k = 1$ at $s \approx 9.34$, $k = 2$ at $s \approx 11.83$ — the carriers of the E4a
excess, [F10](PSC2-F10-e4a-trace-consistency.md)) persist with total drift $< 0.02$
across all stages. The surplus mass is a permanent, certified structural feature of the
wedge window, not a stage artifact that genealogy tracking could age out.

## Verdict against the pre-registered criteria

**HS7: delivered (report-only), genealogy persistent.** The component behaves as
designed (breaks localise the only re-arrangement events; drift quantifies the frozen
certified picture); its substantive content — structural, permanent pollution below
$\gamma_1$ — feeds the family closure of
[F11](PSC2-F11-e4b-matched-displacement.md). With this, S04 §7's "displacements
decreasing at a measured rate" question is answered negatively for W1: the measured
rate is zero (frozen), which in this family's situation is the *pollution-persistence*
branch, not the convergence branch.

## Tag

- HS7 measurements (chains, breaks, drifts, multiplicities): **verified**
  (deterministic run; F08 anchors and coherence reproduced first; harness valid per
  F10).
- The identification of the two breaks with F08's published root re-assignments:
  **verified** (row-level comparison).
- HS7 as a general gate (S04 §7): stays **exploratory** apparatus; this run is its
  first full execution and calibration.
- Any statement connecting this to zeros: **none made** (O6). RH is **open**.

**Scope (do-not list compliance).** Entirely $\gamma$-free; no unfolding; no fitted
parameter; the enclosure-interval statement about $\mathrm{spec}(D) = \mathbb R$ remains
trivially true on this ambient (F08's honesty clause) and is not presented as spectral
discovery.

## Propagation

Charter §3 conjecture list row (HS7 delivered, first execution) and §6 ledger row
updated. Everything else via
[F10](PSC2-F10-e4a-trace-consistency.md)/[F11](PSC2-F11-e4b-matched-displacement.md).
