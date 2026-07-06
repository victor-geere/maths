# PSC2-WP02 — the density gate (E0): first kill

*Status: **open** (design law stated; computation pending). Priority: immediately after WP01.*

## Objective

Build the stage family $H^G_n = P_nDP_n$ (N0 builder: $J$-invariant basis = sieve prime-power
inventory $\{p^k \le M_n\}$ + prolate-type archimedean window; matrix elements of $D$ and
$D^2$, `mpmath` dps 35) and derive its **intrinsic Weyl law with zero fitted parameters**;
verify numerically on derived windows $T \le T_n$.

## Pre-registered criteria (fixed before any run)

- **Pass:** $N_n(T)/\big(\frac{T}{2\pi}\log\frac{T}{2\pi}\big) \to 1$ on derived windows,
  coefficients derived, not fitted.
- **Must-fail controls:** legacy $H_n'$ (density mismatch regression,
  [S06](../sources/PSC2-S06-constraints-and-walls.md) §2.2); graph one-mode (F4 structural
  spectra, [S02](../sources/PSC2-S02-determinant-level.md) §6).
- **Shape-decoy caution (O6):** passing E0 is *not* evidence of matching zeros — any
  two-cutoff dilation model passes; the decoy control lives in WP05.

## Inputs

[S03](../sources/PSC2-S03-eigenvalue-level.md) §3(c)–§4 (design law, bookkeeping
$\dim V_n$, window derivation); Connes–Moscovici precedent
([S00](../sources/PSC2-S00-verified-foundation.md) §8).

## Deliverable

N0 stage-builder code under `numerics/`; finding note with the derived Weyl law and the
pass/fail verdict published verbatim against the criteria above. Tag target: **proven** (a
computation about an explicit finite family).

## Falsifier

$H^G_n$ failing E0 kills the primary candidate — recorded per the phase-4 precedent; the
E-track then stops until a redesigned window is proposed, and the project's weight shifts to
the L3 packages (WP06–WP08, WP12).
