# PSC2-F11 — E4b, matched displacement: the letter rule passes on a sub-resolution drift, the certified rule and the decoy comparison do not — the W1 family closes as counting law only

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP05](../workpackages/PSC2-WP05-evaluation-harness.md). Code/run: the same
deterministic run as [PSC2-F10](PSC2-F10-e4a-trace-consistency.md)
(`numerics/wp05_evaluation_harness.py`; harness validity, control battery, regression
record, and the run-1 control-artifact disclosure live there). **This is the note where
the W1 family's arithmetic content is decided** (the WP's own framing, and the
manuscript §12 Phase B pre-registered decision point). Tags per
[PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> - **E4b — matched displacement (final evaluation only).** Median $|\lambda_k - \gamma_k|$
>   under optimal matching on $[0, 50]$; success = decreasing over ≥ 3 stages. $\gamma$-list
>   used **only here** (I0.6).
> - E4b and HS2 monotone over ≥ 3 stages […]
> - **This WP is where the W1 family's arithmetic content is actually decided** (O6): the
>   bare-wedge/prolate decoy of E4c — wedge phase-space support with no sieve inventory —
>   must pass E0's shape and must fail E4b, or the harness is invalid; W1 itself must beat
>   that decoy at E4b or the family closes as "counting law only".

And the binding resolution budget carried by the WP status note (from F08 + F09), which
the E4b design was required to price **in advance**:

> (a) certified-enclosure radii on $[0,50]$ floor at $\approx 1.72$ and do not improve
> with stage (F08); (b) the certified quasi-mode floor $r_n(\lambda) \ge 0.73$ on $[0,50]$
> (grid minima $\approx 0.98$) at every computed stage (F09) — no trial vector in $V_n$
> localises better; (c) the W1 spectra have a permanent low-energy hole $(-9.34, 9.34)$ …
> The E4b design must state in advance the displacement resolution it needs against
> (a)–(b) and its handling of (c); if the budget is unmeetable, the pre-registered
> escalation is the prolate pencil.

Operationalisation, fixed in the script header before the run: targets = the 10 zero
ordinates $\le 50$ (`mpmath.zetazero`, consumed in this component only — I0.6);
candidates = stage eigenvalues in $(0, 50]$; matching = monotone min-total-$|\cdot|$
assignment (L1-optimal for sorted sequences; validated in-run against brute force on 60
seeded instances); statistic = median matched displacement $\mathrm{med}_n$. Rules:
**LETTER** (the WP's line) — $\mathrm{med}_n$ strictly decreasing over $\ge 3$
consecutive stages; **CERTIFIED** (the budget, priced in advance) — LETTER **and**
cumulative decrease $\ge$ RES_FLOOR $= 0.73$ (floor (b): smaller improvements are not
resolvable against the family's own certified energy fuzziness) **and** final median
$\le$ half the mean target spacing ($1.98$, target-derived — a localisation claim must at
least reach sub-spacing scale); **BEATS-DECOY** — $\mathrm{med}(\text{decoy}) -
\mathrm{med}(\mathrm{W1}) \ge 0.73$ at each of the last 3 stages (the density-matched
comparison); **COUNTING-LAW-ONLY** branch iff neither CERTIFIED nor BEATS-DECOY.

**The budget statement made in advance (header, verbatim in substance):** predicted from
F08's *published* $n = 12$ table, the E4b statistic starts at median $\approx 0.68$ —
*below* floor (b). The entire dynamic range of the statistic on $[0, 50]$ is therefore
sub-resolution, and the budget is **unmeetable as a certified-localisation claim** unless
the run measures cumulative improvement $\ge 0.73$, which would falsify the
frozen-spectrum picture (F09: stage mobility $9.2\times10^{-4}$). Handling of hole (c):
$\gamma_1 = 14.13\ldots > 9.34$, so the hole blocks no match on this window; stage
eigenvalues in $[9.34, 14.13)$ are surplus, reported in the pollution inventory. Density
hygiene (from the design dry run, disclosed): absolute displacement levels are not
comparable across density classes — the rules are improvement-based, and the only
cross-family level comparison is against the density-matched decoy.

## Regression check

Via [F10](PSC2-F10-e4a-trace-consistency.md) (same run): N00 §1–§4, F07, F08 anchors all
reproduced; harness valid (every control behaved).

## Result

```
E4b — MATCHED DISPLACEMENT ON [0, 50]  (FINAL EVALUATION, I0.6: the
      gamma-list is consumed HERE ONLY, as pre-registered)
  targets: 10 ordinates <= 50 (gamma_1 = 14.134725 ... gamma_10 = 49.773832)
  hole handling (budget item c): gamma_1 > 9.34 hole edge: True — the hole blocks no match on this window
      n  W1 N+(50)    W1 med  decoy N+(50)  decoy med  decoy-W1
      4         17    0.8076            17     0.7774   -0.0302
      6         17    0.7456            17     0.6916   -0.0540
      8         17    0.6850            17     0.6948    0.0098
     10         17    0.6801            17     0.6948    0.0147
     12         17    0.6797            17     0.6948    0.0151
  pollution inventory at n=12: 2 eigenvalues below gamma_1 (9.341, 11.831);
    their share of the E4a t=0.05 excess: 2.7315e-02 of 2.7261e-02 (100.2%)
  certified-interval coverage of the 10 ordinates at n=12: 9/10  (report-only: intervals cover ~56 of the 50-window — coverage is not evidence)
  localisation scale (half mean target spacing, target-derived): 1.9800
  E4b LETTER rule (median strictly decreasing over >= 3 stages): True (cumulative decrease over best run = 0.1279)
  E4b CERTIFIED rule (LETTER and decrease >= RES_FLOOR = 0.73 and final <= 1.98): False
  BEATS-DECOY (decoy - W1 >= 0.73 at each of last 3 stages): False
  -> W1 E4b: NOT CERTIFIED;  counting-law-only branch fires: True
  decoy E4b: letter = False (drop 0.0000), certified = False  -> FAILS E4b [as required]
  sine decoy meds (stage-matched d_n) = 17.7606  0.1080  0.1080  0.1080  0.1080  in-window candidates = 50 (density witness)  certified = False -> FAILS [as required]
    (absolute sine level may sit below W1 by density alone — S04 §5:
     levels are not comparable across density classes; rules are
     improvement-based and the decoy comparison is density-matched)
  legacy meds =   33.5134    32.2317    30.8108   certified = False -> FAILS [as required]
  graph meds =   34.5133    30.8504    30.0211   certified = False -> FAILS [as required]
```

The numbers say three things, each two-sided:

1. **The WP's letter rule fires — and the budget correctly rejects it.** The W1 median
   *is* strictly decreasing at all five stages ($0.8076 \to 0.6797$), so "success =
   decreasing over ≥ 3 stages" holds by the letter. But the entire decrease is $0.1279$,
   almost all of it front-loaded at $n = 4 \to 8$ and dwindling to $4\times10^{-4}$ per
   stage — the F09 frozen-spectrum mobility — against a certified quasi-mode floor of
   $0.73$: the family's own certified resolution cannot distinguish this drift from
   fixed-aperture jitter. Had WP05 run without the F08/F09 budget, the raw rule would
   have scored a sub-resolution drift as an arithmetic success. This is precisely the
   failure mode the budget requirement existed to price, and it is the run's sharpest
   methodological product.
2. **W1 does not beat the density-matched decoy.** The nested bare wedge with *no*
   arithmetic in its site placement matches the zeros at median $0.6948$; W1 at $0.6797$.
   The difference, $0.015$, is fifty times smaller than the certified resolution floor.
   Both families sit exactly where a wedge-law spectrum with 17 eigenvalues on a
   10-ordinate window must sit: at the half-local-spacing noise level. The sieve
   inventory moved the ladders' *frequencies*, and it bought nothing measurable at E4b.
3. **The pollution inventory closes the loop with E4a.** The two sub-$\gamma_1$
   eigenvalues ($9.341$, $11.831$) — the wedge counting law's surplus below the first
   ordinate — carry 100.2% of the E4a excess. The same structural term
   ($R(T) - N(T) \approx T/2\pi$, $= 7.08$ at $T = 50$; observed surplus $17 - 10$)
   accounts for the trace failure, the moment failure
   ([F13](PSC2-F13-hs2-moment-gate.md)), and the product divergence
   ([F12](PSC2-F12-hs1-product-gate.md)). The interval-coverage line (9/10) is reported
   with its own disclaimer: intervals covering $\sim56$ of the 50-unit window certify
   nothing.

## Verdict against the pre-registered criteria

**E4b: NOT CERTIFIED — and the counting-law-only branch fires** (neither CERTIFIED nor
BEATS-DECOY). Per the WP's own closure line and the manuscript §12 Phase B pre-registered
decision point: **the W1 family closes as "counting law only"** — wedge phase-space
support plus sieve inventory carries, on the evaluation window, no measurable arithmetic
content beyond its (derived, convex, E0b-passing) counting law. What the family retains
is everything already banked: the proven builder and closed forms (F07), the certified
enclosure machinery (F08), the inclusion criterion and coarse-inclusion constants (F09),
and its role as the harness's calibrated example. Per the pre-registered escalation
(F02 redesign note → WP02b falsifier branch → F08 → F09 → this run), the E-track
candidate moves to the genuinely quadratic **prolate pencil**:
[PSC2-WP15](../workpackages/PSC2-WP15-prolate-pencil.md), chartered with this finding.
The harness itself is candidate-independent and is the WP05 deliverable that survives.

## Tag

- E4b measurements, matching optimality (DP $=$ brute force), rule applications, and the
  NOT-CERTIFIED / counting-law-only verdict: **verified** against the pre-registered
  criteria (deterministic run; harness valid per F10).
- The L1-optimality of monotone matching on sorted sequences: **proven** (classical
  exchange argument; machine-checked on 60 instances in-run).
- The family-closure statement ("counting law only") as a *stage-limit* claim: the
  computed-stage facts are **verified**; the $n \to \infty$ persistence rests on the F09
  frozen-spectrum extrapolation, tagged there **verified (extrapolation)** — the closure
  is a design decision taken at the pre-registered branch, not a theorem about all $n$.
- Any statement connecting any of this to zeros: **none made**. Per O6 (binding, quoted
  at every E-track site): a family-level kill is a statement about this window design;
  it is not evidence about zeros, and neither its failure nor any future candidate's
  success at these gates decides anything about RH, which remains **open**.

**Scope (do-not list compliance).** The $\gamma$-list was consumed exactly once, in this
component's final evaluation, as pre-registered (I0.6); no unfolding, no fitted
parameter, no statistical claim as Hilbert–Pólya progress. The sine decoy's absolute
median ($0.108$, by density alone) is quoted as the standing demonstration of why
absolute displacement levels are never evidence (S04 §5).

## Propagation

Charter ledger updated: **yes** (T5 row → done with family closure; §3 conjecture list
annotated; §4 ordering update appended — E-track weight moves to WP15; §6 ledger rows).
WP05 status → done. [WP15](../workpackages/PSC2-WP15-prolate-pencil.md) chartered as the
pre-registered escalation. README and manuscript updated (Phase B decision point
recorded). Source doc correction notice needed: **no**. N00 unchanged.
