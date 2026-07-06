# PSC2-WP12 — the AFE-symmetric family V2 (G2): the corrected H\* attack

*Status: **open** — high-risk / high-value. Depends on WP01 (HS5 fixes the family's form:
paired spectra, even stage products).*

## Objective

Replace the eliminated family V1 (X4) by V2 obeying design law C-2, now in the spectral form
mandated by HS5: stage determinants that are **even in $t$ by construction** (equivalently,
exactly $s \leftrightarrow 1-s$ symmetric), built from symmetrised AFE/Riemann–Siegel-type
kernels
$$C^{V2}_{pq}(s) = \sum_{m \in I_n,\ pq \mid m} a_p a_q
\big[m^{-s}\varphi(s) + m^{s-1}\varphi(1-s)\big]\cdot(pq)^{\mathrm{calibration}},$$
with $\varphi$ a smooth AFE cutoff. Re-run the F5 stability sweep and F6 asymmetry sweep
against the baselines in [N00 §3](../numerics/PSC2-N00-verification-targets.md).

## Pre-registered gate criterion

Median FE asymmetry **decreasing in $n$** at some fixed $\theta \ne 0$, with the
$\sigma > 1$ control column intact (consistency with C1 on the half-plane,
[S02 §2](../sources/PSC2-S02-determinant-level.md)). That outcome is the first genuine
evidence for H\*; the tag stays **heuristic** until a convergence proof (obligations
H\*-a…d, S02 §3).

## Falsifier (pre-registered; binding)

If no V2 member beats the $\theta = 0$ baseline (asymmetry $1.17$), **H\* in determinant form
is demoted**: record, close WP12, and let the project's L3 weight rest on WP06–WP08 (which do
not need H\*).

## Pricing

H\* itself is below the wall (it is a convergence statement, not a zero-location statement);
its payoff dictionary (P2.4: gaps ⇔ zero-free regions) activates only on success, and C2 at
full strength remains the wall (W2) regardless.
