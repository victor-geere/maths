# PSC2-WP04 — certified enclosures (E3b): the tractable core of pollution control

*Status: **open — reopened, first in line** (7 Jul 2026) — WP02b's rewindowed primary
$H^{G,\mathrm{w}}_n$ (W1 wedge builder) passed E0b
([PSC2-F07](../findings/PSC2-F07-density-rewindow.md)); per the pre-registration the E-track
pause is lifted and this WP runs first, exactly as F02's ordering note anticipated. Its
pencil input $(P_nDP_n, P_nD^2P_n)$ is **delivered** for the W1 family by
`numerics/wp02b_rewindow.py` (complex closed forms at dps 35, `svd_c`-certified; the older
N0 elements in `e0_density_gate.py` remain available as a comparison family). O6 caveat
carried over: the E0b pass is not evidence about zeros — enclosures here are statements
about the family, pending E4b. Was: **paused** (6 Jul 2026, WP02 falsifier —
[PSC2-F02](../findings/PSC2-F02-density-gate.md)); before that **open** (the enclosure
theorem is classical — proven; our instantiation pending). Depends on: WP02b (matrix
elements).*

## Objective

From the pencil built of $P_nDP_n$ and $P_nD^2P_n$, compute **second-order relative spectra**:
every pencil root $z$ certifies
$\mathrm{spec}(D) \cap [\mathrm{Re}\,z - |\mathrm{Im}\,z|,\ \mathrm{Re}\,z + |\mathrm{Im}\,z|]
\ne \emptyset$ — pollution-free **by theorem**, no norm-resolvent convergence needed
(Shargorodsky; Levitin–Shargorodsky 2004; Boulton–Levitin; Davies–Plum).

## Deliverable

Certified intervals around stage eigenvalues at small $n$, with radii $|\mathrm{Im}\,z|$ and
their decrease rate across $n$ **measured and reported** (feeds WP05's HS7 genealogy).
Tag target: **proven** (the theorem is classical; our part is computing $D^2$ elements
correctly — geometric sums at finite places, Gaussian/Mellin integrals at $\infty$).

## Cross-science note

This technology was built to kill spectral pollution for compressed **Dirac operators** in
relativistic quantum chemistry; we reuse it on the adelic Dirac. Cite the transfer precisely
in the finding note.

## Pre-registered criteria

- radii decreasing in $n$ over at least three consecutive stages on the window $[0, 50]$;
- every certified interval cross-checked against independently computed truth **only at the
  final-evaluation step** (I0.6).

## Falsifier

Radii stagnating while E0 passes = the compression sees the right density but cannot localise
— a genuine, reportable obstruction profile (it would point at the archimedean window's
band-limit dual as the bottleneck).

## Explicitly out of scope

E3a (norm-resolvent windows) — wall-adjacent at full strength; no work here until WP03/WP04
have spoken. E3c (positivity) is gate E5, a wall, not a work item.
