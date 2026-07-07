# PSC2-WP06 — audit the salvaged identity; derive the honest weighted locus (G1)

*Status: **done** (7 Jul 2026) — [PSC2-F03](../findings/PSC2-F03-weighted-locus.md).
Part A: audit closed, Theorem 1.1 **proven** (explicit factorisation; exact
$\mathbb{Q}$-certification at $n \le 6$; Watanabe–Fukumizu cross-check). Part B: leaf
reduction, balance identities, annulus and Perron inner bound **proven** and verified against
the census — in the pre-registered **weak-locus branch**: the annulus cannot separate
structural detachment, so WP08's theorem target is re-scoped to the measured census, per the
falsifier below.*

*Original header — Status: **open**. The previous written attempt failed audit and is
quarantined (X10, [S06 §3](../sources/PSC2-S06-constraints-and-walls.md)); its salvageable
half is [S05](../sources/PSC2-S05-salvaged-G1.md). Gating: F4's "no graph-Siegel zeros" and
any Ramanujan-type statement are **undefined** until this locus exists.*

## Part A — close the audit of Theorem 1.1 (the resolvent identity)

Work the four obligations of [S05 §3](../sources/PSC2-S05-salvaged-G1.md): explicit
block-triangular factorisation with dimension bookkeeping; degenerate cases (degree-1
vertices — present in the sieve graph; singular $u$ with $u^2w_e^2 = 1$); independent
symbolic certification at $n \le 6$ (sympy-verifier, coefficient-by-coefficient, in this
project's tree); cross-check against Mizuno–Sato 2004 / Watanabe–Fukumizu 2009. On success,
upgrade S05's tag to **proven** (dated correction notice, per convention).

## Part B — the honest confinement locus

From $\det M(u) = 0$ derive where non-real stage zeros can live as a function of the weight
distribution, and what "detached/exceptional" means intrinsically. Structure to exploit: each
diagonal term $u^2w^2/(1 - u^2w^2)$ is a Möbius function of $u^2$ (Herglotz-type positivity).
Do **not** reuse the quarantined Gershgorin bounds without repair; if Gershgorin is the tool,
state the leaf/degree-1 treatment honestly (Schur reduction of degree-1 composites, proved,
not waved).

## Pre-registered expectations

- a weak locus (fat annulus) still unblocks WP08 — record it even if unimpressive;
- the measured pole census (parent snapshot: 208 real poles at $n = 7$, $|u| \in [0.19, 4.18]$)
  is the reality check: the derived locus must contain the measured poles with no fitted
  constants.

## Deliverable

A `W-theorem` finding note: identity **proven** (Part A) + locus proposition with explicit
radii/regions (Part B), symbolically verified at small $n$.

## Falsifier

None needed for Part A (the $10^{-15}$ agreement makes identity failure implausible); Part B's
risk is weakness, not falsity. If the locus cannot separate structural from arithmetic
detachment even in principle, WP08's theorem target is re-scoped to the measured census.
