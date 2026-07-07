# PSC2-WP04 — certified enclosures (E3b): the tractable core of pollution control

*Status: **done — passed, with a saturation caveat** (7 Jul 2026,
[PSC2-F08](../findings/PSC2-F08-certified-enclosures.md)). Verdict: **PASS** against the
pre-registered criteria (median radius strictly decreasing over all five stages
$1.7411 \to 1.7241 \to 1.7221 \to 1.7220 \to 1.7219$; harness valid two-sidedly;
machinery certified to $7.5\times10^{-13}$ against `mpmath.eig` and $4.2\times10^{-10}$
against independent quadrature). The measured **rate**, however, is $\alpha \approx 0.01$:
the radii saturate at a positive floor $\approx 1.72$ on $[0,50]$ — the fixed-aperture
limit of the wedge on the window, exactly the band-limit-dual fingerprint the falsifier
text named, arriving through a passing gate. The caveat travels with the HS7 genealogy
feed to WP05; E-track proceeds WP03 next, then WP05. Was: **open — reopened, first in
line** (7 Jul 2026, E0b passed, [PSC2-F07](../findings/PSC2-F07-density-rewindow.md));
before that **paused** (6 Jul 2026, WP02 falsifier —
[PSC2-F02](../findings/PSC2-F02-density-gate.md)); before that **open**. Depends on:
WP02b (matrix elements — delivered by `numerics/wp02b_rewindow.py`).*

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
