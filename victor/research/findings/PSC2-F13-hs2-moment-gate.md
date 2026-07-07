# PSC2-F13 — HS2, the moment gate: the $\gamma$-free pollution detector fires — stage moments sit at $2.2\times$ the secondary-zeta targets and drift further away with stage

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP05](../workpackages/PSC2-WP05-evaluation-harness.md). Code/run: the same
deterministic run as [PSC2-F10](PSC2-F10-e4a-trace-consistency.md) (harness validity,
regression record, disclosures there). Tags per [PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> - **HS2 — moment gate.** $\sigma_n(2m) = \sum_k \lambda_k^{-2m}$ vs $\sigma(2m)$ from Taylor
>   coefficients of $\xi$ at $s = \tfrac12$ — low-window, $\gamma$-free pollution detector
>   ([S04 §3](../sources/PSC2-S04-model-pair.md)); Li-adjacent, strictly below the Li wall.
> - E4b and HS2 monotone over ≥ 3 stages […]

Operationalisation (header, fixed before the run): $m \in \{1, 2, 3\}$; targets
$\sigma(2m) = -m\,[t^{2m}]\log(\Xi(t)/\Xi(0))$ from the `mpmath` Taylor expansion of
$\xi$ at $s = \tfrac12$ (S04 §3's own prescription; no zero list; evenness asserted;
identity re-check at $t = 0.5$ agreed to $6\times10^{-16}$ at design time); stage side
$\sigma_n(2m) = \sum_{s_i > 0} s_i^{-2m}$ over the full positive spectrum; **PASS** iff
$|\sigma_n(2m) - \sigma(2m)|$ strictly decreasing over $\ge 3$ consecutive stages for
**every** $m$. The model-side identity grounding the gate
($\log\tfrac{\sin\pi z}{\pi z} = -\sum_m \tfrac{\zeta(2m)}{m}z^{2m}$, S04 §3) was
cross-checked symbolically via the sympy-verifier (coefficients $-\pi^2/6$,
$-\pi^4/180$, $-\pi^6/2835$ $=$ $-\zeta(2), -\zeta(4)/2, -\zeta(6)/3$ exactly).

## Regression check

Via [F10](PSC2-F10-e4a-trace-consistency.md) (same run): all anchors reproduced; harness
valid. The sine control's *internal* moment line ($|\sum_{k\le d}k^{-2} - \zeta(2)|$
decreasing with $|err \cdot d - 1| = 2.05\times10^{-4}$) doubles as the gate's own
positive calibration: the metric detects a spectrum converging to *its own* moment
targets.

## Result

```
HS2 — MOMENT GATE  sigma_n(2m) vs sigma(2m) from xi Taylor  [W1]
  sigma(2) target = 0.0231049931154
  sigma(4) target = 3.71725992853e-5
  sigma(6) target = 1.44173931401e-7
      n     sigma_n(2)       |err|     sigma_n(4)       |err|     sigma_n(6)       |err|
      4   3.925285e-02  1.6148e-02   2.248617e-04  1.8769e-04   2.001164e-06  1.8570e-06
      6   4.549938e-02  2.2394e-02   2.268727e-04  1.8970e-04   2.009542e-06  1.8654e-06
      8   4.844939e-02  2.5344e-02   2.270867e-04  1.8991e-04   2.010342e-06  1.8662e-06
     10   4.978121e-02  2.6676e-02   2.271028e-04  1.8993e-04   2.010390e-06  1.8662e-06
     12   5.041086e-02  2.7306e-02   2.271042e-04  1.8993e-04   2.010394e-06  1.8662e-06
  HS2 [W1]: FAIL (per-m decreasing runs >= 3: m=1: False, m=2: False, m=3: False)
```

The numbers say: at every $m$ the error is **increasing or flat**, never decreasing —
the gate fails in the strongest possible way for a monotonicity criterion. The profile
separates the two pollution mechanisms cleanly. At $m = 2, 3$ the moments are dominated
by the lowest eigenvalues and are stage-frozen at $\approx 6.1\times$ and
$\approx 13.9\times$ their targets: this is the **sub-$\gamma_1$ surplus** ($s = 9.341$
and $11.831$ contribute $\approx 1.7\times10^{-4}$ of the $2.27\times10^{-4}$ at
$m = 2$ by themselves, against a total target of $3.7\times10^{-5}$). At $m = 1$ the
error *grows* with stage ($1.61 \to 2.73 \times10^{-2}$): the in-window spectrum is
frozen, so the growth is the accumulating tail $\sum_{s_i > 50} s_i^{-2}$ as
$T_n \to 2553$ — the wedge density exceeds the zero density by the same $T/2\pi$-term
at *every* scale, so the total moment drifts monotonically away from the arithmetic
value as the family grows. The decoy's HS2 table (F10's run, report-only) fails
identically ($\sigma_{12}(2) = 4.70\times10^{-2}$) — density-class behaviour, not
inventory behaviour. Both readings are the measured counterpart of the E4a excess
([F10](PSC2-F10-e4a-trace-consistency.md)), obtained **without any zero data** — the
low-window $\gamma$-free pollution detector did exactly the job S04 §3 assigned it.

## Verdict against the pre-registered criteria

**HS2: FAIL** (no decreasing run at any $m$). Jointly with E4a's persistent excess and
HS1's divergence: one consistent, quantified pollution profile across the trace,
determinant, and moment diagnostics, all attributable to the wedge counting surplus.
Feeds the family-level closure of [F11](PSC2-F11-e4b-matched-displacement.md).

## Tag

- $\sigma(2m)$ targets (Taylor of $\xi$ at $\tfrac12$; Voros secondary-zeta category per
  S04 §3, kept separate from the M3 spectral-zeta error): **proven** identity, **verified**
  values (design-time identity re-check $6\times10^{-16}$; model-side coefficients
  symbolically exact).
- HS2 measurements and the FAIL verdict: **verified** (deterministic run; harness valid
  per F10).
- The two-mechanism reading (frozen sub-$\gamma_1$ mass at $m \ge 2$; growing tail at
  $m = 1$): **verified** at the computed stages (component sums); as an $n \to \infty$
  statement: extrapolation, not proven.
- Any statement connecting this to zeros: **none made** (O6). RH is **open**.

**Scope (do-not list compliance).** No zero list (targets from $\xi$'s Taylor
coefficients); strictly below the Li wall (finite $m \le 3$, no positivity claim in
either direction); no unfolding; no fitted parameter.

## Propagation

Charter §3 conjecture list row (HS2 gate delivered, fired) and §6 ledger row updated.
Everything else via [F10](PSC2-F10-e4a-trace-consistency.md)/[F11](PSC2-F11-e4b-matched-displacement.md).
