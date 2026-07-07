# PSC2-F12 — HS1, the paired-product gate: $\Xi_n$ diverges from $\Xi$ on $[0, 30]$ — the conjectured implication (E0 ∧ E3b ⇒ convergence) is refuted for the W1 instantiation

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP05](../workpackages/PSC2-WP05-evaluation-harness.md). Code/run: the same
deterministic run as [PSC2-F10](PSC2-F10-e4a-trace-consistency.md) (harness validity,
regression record, disclosures there). Tags per [PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP and S04 §6 before the run)

> - **HS1 — paired-product gate.** $\Xi_n(t) = \Xi(0)\prod(1 - t^2/\lambda_k^2)$ vs $\Xi(t)$
>   computed from $\xi(\tfrac12+it)$ via `mpmath` on derived windows — the L4→L3 bridge, no
>   zero list ([S04 §6](../sources/PSC2-S04-model-pair.md)).
> - HS1 divergence-while-E4a-passes is the quantified-pollution branch, reported as such.

> **Conjecture HS1. — open.** If E0 and E3b pass, $\Xi_n \to \Xi$ uniformly on derived
> windows $|t| \le T'_n$, $T'_n \to \infty$. The eigenvalue-level avatar of C1 — the
> L4→L3 bridge. *Hygiene:* $\Xi$ computed independently from $\xi(\tfrac12 + it)$
> (`mpmath`); no zero list; $\lambda_k$ from the stage construction with zero fitted
> parameters. […] *Falsifier:* pointwise divergence on $[0,30]$ while E4a passes —
> reportable either way (quantified determinant-level pollution).

Operationalisation (header, fixed before the run): $\Xi_n$ over the **full** positive
stage spectrum; $\Xi(t) = \xi(\tfrac12+it)$ via `mpmath` at dps 35,
$\xi(s) = \tfrac{s(s-1)}{2}\pi^{-s/2}\Gamma(\tfrac s2)\zeta(s)$ (no zero list); grid
$t = 0\,(0.25)\,30$; metric $M1_n := \mathrm{median}\,|\log(|\Xi_n(t)|/|\Xi(t)|)|$ with
per-band medians $[0,10\,|\,10,20\,|\,20,30]$; **CONVERGENT** iff $M1_n$ strictly
decreasing over $\ge 3$ consecutive stages and final $\le \log 1.5 = 0.4055$; else
**DIVERGENT**, classified jointly with E4a.

## Regression check

Via [F10](PSC2-F10-e4a-trace-consistency.md) (same run): all anchors reproduced; harness
valid.

## Result

```
HS1 — PAIRED-PRODUCT GATE  Xi_n(t) vs Xi(t) on [0, 30]  [W1]
    n= 4  M1 = median|log(|Xi_n|/|Xi|)| =   1.4576   bands [0,10|10,20|20,30] =   0.4476   0.9872   3.2084   excluded pts = 0
    n= 6  M1 = median|log(|Xi_n|/|Xi|)| =   1.4495   bands [0,10|10,20|20,30] =   0.5968   2.1849   0.9075   excluded pts = 0
    n= 8  M1 = median|log(|Xi_n|/|Xi|)| =   2.4744   bands [0,10|10,20|20,30] =   0.6670   2.9997   2.5039   excluded pts = 0
    n=10  M1 = median|log(|Xi_n|/|Xi|)| =   2.9264   bands [0,10|10,20|20,30] =   0.6987   3.2714   3.2955   excluded pts = 0
    n=12  M1 = median|log(|Xi_n|/|Xi|)| =   3.1430   bands [0,10|10,20|20,30] =   0.7137   3.4752   3.6567   excluded pts = 0
  HS1 [W1]: DIVERGENT (decreasing run >= 3: False; final M1 = 3.1430 vs bar 0.4055)
```

The numbers say: the stage products move **away** from $\Xi$ monotonically in $n$
($M1: 1.458 \to 3.143$), in every band. The structural cause is visible without any zero
data: on $(0, 30]$ the stage product has 8 zeros ($9.34, 11.83, 14.76, \ldots, 29.29$)
where $\Xi$ has 3 ($14.13, 21.02, 25.01$) — the wedge counting surplus again
([F10](PSC2-F10-e4a-trace-consistency.md)) — so the two functions cannot share a
log-modulus profile at any stage; and the growing high tail of the stage spectrum
(eigenvalues in $(50, T_n]$, $T_n \to 2553$) multiplies in an ever-larger Gaussian-type
damping $\exp(-t^2\sum_{\lambda > 50}\lambda^{-2})$ that $\Xi$'s zero set does not have
at the same weight — which is why $M1_n$ *increases* with stage even though the
in-window spectrum is frozen ([F13](PSC2-F13-hs2-moment-gate.md) measures the same tail
at $m = 1$).

## Verdict against the pre-registered criteria

**HS1: DIVERGENT.** Joint classification with E4a (the pre-registered branch table): E4a
**failed by persistent excess** ([F10](PSC2-F10-e4a-trace-consistency.md)), so this is
**not** the "divergence-while-E4a-passes" branch — it is the *consistent* branch: L3
(determinant) and L4 (trace/eigenvalue) diagnostics fail together, from the same
quantified pollution mass. Consequence for the conjecture ledger: **Conjecture HS1, as
stated in S04 §6, is refuted for the W1 instantiation** — its hypotheses held (E0b
passed, F07; E3b passed, F08) and its conclusion fails. What survives as open is the
implication for families that pass E4a/E4b — i.e. HS1 restated with the harness's
arithmetic gates in the hypothesis, not just the shape gates. The gate itself (metric,
hygiene, falsifier) is delivered and validated as WP05 apparatus.

## Tag

- HS1 measurements and the DIVERGENT verdict: **verified** (deterministic run; harness
  valid per F10; $\Xi$ computed independently of any zero list).
- Conjecture HS1 (E0 ∧ E3b ⇒ $\Xi_n \to \Xi$): **refuted for W1** (hypotheses verified
  held; conclusion verified false at five stages with monotone divergence). The
  restated conjecture (arithmetic-gate hypotheses) is **open**.
- The tail-damping explanation of the monotone increase: **heuristic** (consistent with
  the measured band profile and the F13 moment tail; not proven as a limit statement).
- Any statement connecting this to zeros: **none made** (O6). RH is **open**.

**Scope (do-not list compliance).** No zero list anywhere in this component ($\Xi$ from
$\xi$ directly); no unfolding; no fitted parameter. Nothing here bears on the truth of
RH.

## Propagation

Charter §3 conjecture list row (HS1) updated; §6 ledger row added. Everything else via
[F10](PSC2-F10-e4a-trace-consistency.md)/[F11](PSC2-F11-e4b-matched-displacement.md).
