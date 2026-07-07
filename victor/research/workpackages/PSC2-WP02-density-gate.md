# PSC2-WP02 — the density gate (E0): first kill

*Status: **done — primary killed** (6 Jul 2026,
[PSC2-F02](../findings/PSC2-F02-density-gate.md)). Verdict: **FAIL** against the
pre-registered criteria below, with both must-fail controls failing as required and the
positive harness control passing — the kill is informative, not an artifact. The falsifier
branch executed: the E-track (WP03–WP05) is stopped pending a redesigned window; weight
shifts to WP06–WP08, WP12. Deliverables landed: N0 builder
(`numerics/e0_density_gate.py`, matrix elements of $D$ and $D^2$ at dps 35), the derived
parameter-free Weyl law, and a proven no-go lemma (concave counting laws cannot pass E0)
covering the whole fixed-basis design class. WP01's residual obligation is discharged: the
$J$-invariant basis compatible with the sieve inventory is **constructed** ($JV_n = V_n$
exact; E1 pairing exact by construction).*

> **Notice (7 Jul 2026).** The redesigned window this falsifier demanded has landed:
> [WP02b](PSC2-WP02b-density-gate-rewindow.md) (W1 wedge builder, instantiating this WP's
> F02 redesign note) **passed E0b** ([PSC2-F07](../findings/PSC2-F07-density-rewindow.md))
> and the E-track is reopened. Nothing in this WP's verdict changes: the N0 instantiation
> stays killed and the no-go lemma stands — W1 sits outside its hypothesis class (convex
> counting law, checked mechanically).

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
