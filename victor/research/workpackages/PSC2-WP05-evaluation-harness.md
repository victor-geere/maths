# PSC2-WP05 — the evaluation harness (E4 + HS gates)

*Status: **open — reopened** (7 Jul 2026) — WP02b's rewindowed primary
$H^{G,\mathrm{w}}_n$ (W1 wedge builder) passed E0b
([PSC2-F07](../findings/PSC2-F07-density-rewindow.md)); per the pre-registration the E-track
pause is lifted (WP04 first). **This WP is where the W1 family's arithmetic content is
actually decided** (O6): the bare-wedge/prolate decoy of E4c — wedge phase-space support
with no sieve inventory — must pass E0's shape and must fail E4b, or the harness is
invalid; W1 itself must beat that decoy at E4b or the family closes as "counting law only".
The harness design below is candidate-independent and stays; F02's E0 evaluator (window
rule, dev metric, positive/decoy controls) is a first delivered component, reused verbatim
by F07. Was: **paused** (6 Jul 2026, WP02 falsifier —
[PSC2-F02](../findings/PSC2-F02-density-gate.md)); before that **open** (targets are
in-repo verified values). Depends on: WP02b (spectra), WP04 (enclosures for HS7). All rules
of I0 ([S06 §5](../sources/PSC2-S06-constraints-and-walls.md)) binding.*

## Components

- **E4a — trace consistency (strongest test).** $\sum_{\lambda} g_t(\lambda)$ over
  $\mathrm{spec}(H^G_n)$ must converge, within the proven $O(M_n^{-1/2})$ envelope
  ([S00](../sources/PSC2-S00-verified-foundation.md) §5–6), to the place-by-place values of
  [N00 §1](../numerics/PSC2-N00-verification-targets.md). Persistent excess = quantified
  pollution mass; deficit = quantified spectral loss. Consumes no new target data.
- **E4b — matched displacement (final evaluation only).** Median $|\lambda_k - \gamma_k|$
  under optimal matching on $[0, 50]$; success = decreasing over ≥ 3 stages. $\gamma$-list
  used **only here** (I0.6).
- **HS1 — paired-product gate.** $\Xi_n(t) = \Xi(0)\prod(1 - t^2/\lambda_k^2)$ vs $\Xi(t)$
  computed from $\xi(\tfrac12+it)$ via `mpmath` on derived windows — the L4→L3 bridge, no
  zero list ([S04 §6](../sources/PSC2-S04-model-pair.md)).
- **HS2 — moment gate.** $\sigma_n(2m) = \sum_k \lambda_k^{-2m}$ vs $\sigma(2m)$ from Taylor
  coefficients of $\xi$ at $s = \tfrac12$ — low-window, $\gamma$-free pollution detector
  ([S04 §3](../sources/PSC2-S04-model-pair.md)); Li-adjacent, strictly below the Li wall.
- **HS7 — enclosure genealogy.** Persistence chains of WP04's certified intervals across
  stages; chain breaks localize pollution ([S04 §7](../sources/PSC2-S04-model-pair.md)).
- **E4c/HS6 — controls.** *Positive:* harmonic oscillator compression. *Decoys:* bare
  prolate/xp compression (must pass E0's shape, must fail E4b) **and the sine model with
  spectrum $\mathbb Z_{>0}$** (must pass every internal-consistency step, must fail every
  arithmetic test by the density-class gap — [S04 §5](../sources/PSC2-S04-model-pair.md)).
  *Negatives:* legacy $H_n'$, graph one-mode. A harness on which any decoy scores
  "arithmetic" is invalid.
- **Backlog: HS3.** Sylvester-denominator resolution schedule for the archimedean window —
  basis engineering only; falsifier: no conditioning gain over uniform Mellin–Hermite at
  $n \le 10$; schedule fixed before any target comparison.

## Pre-registered criteria (fixed now)

E4a residual within $C\,M_n^{-1/2}$, $C$ derived from S00 §5 Prop 6.1; E4b and HS2 monotone
over ≥ 3 stages; HS1 divergence-while-E4a-passes is the quantified-pollution branch, reported
as such; every control behaves per its must-pass/must-fail line above.

## Deliverable

Harness code under `numerics/`; one finding note per component, criteria quoted verbatim.
