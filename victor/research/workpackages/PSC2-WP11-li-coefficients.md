# PSC2-WP11 — Li coefficients: unconditional finite-range computation and asymptotics

*Status: **open**. Independent; pairs naturally with WP05's HS2 moment gate.*

## Objective

1. Compute $\lambda_n^{\mathrm{Li}} = \sum_\rho\big[1 - (1 - 1/\rho)^n\big]$ unconditionally
   for finite ranges via the Bombieri–Lagarias representation (derivatives of
   $\log\xi$ at $s = 1$ — no zero list), at `mpmath` dps 35, with error control.
2. Asymptotic analysis of the computed range against the known conditional shape;
   positivity verified for the computed range is **cumulative and unconditional** — and is
   never presented as evidence for W6 (Li positivity for *all* $n$ ⇔ RH).
3. Bridge to HS2: relate the even ordinate power sums $\sigma(2m)$
   ([S04 §3](../sources/PSC2-S04-model-pair.md)) to the $\lambda_n^{\mathrm{Li}}$ family
   (both are zero-power-sum families under different maps); a small dictionary note so the
   two harness metrics cross-check each other.

## Deliverable

Code under `numerics/` + finding note with the computed table, its error budget, and the
HS2 dictionary. Tag targets: computation **verified**; dictionary **proven** (it is
bookkeeping on convergent series).

## Falsifier

A negative $\lambda_n^{\mathrm{Li}}$ in range would be a disproof of RH and is subject to the
full declaration bar of [PSC2-001 §4](../PSC2-001-conventions.md) — independent symbolic +
numerical verification and adversarial review before any claim. (Expected outcome: all
positive in range; the value is the unconditional record and the cross-check machinery.)
