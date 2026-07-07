# PSC2-WP13 — Asano gluing on the per-edge product (Q-γ2 / G6)

*Status: **open**, machine-checkable. Depends on WP06 (the identity and an honest locus).
The quarantined "Asano Compatibility" proof (X10) is void — this WP is the honest version of
the question it pretended to answer.*

*Gating update (7 Jul 2026): WP06 landed ([F03](../findings/PSC2-F03-weighted-locus.md)) —
the identity is **proven** (multigraph form, exact certification) and the locus exists (weak
annulus, radii fitted-constant-free). This WP is unblocked. Useful F03 inputs: the leaf
reduction (Prop. B1) shows a degree-1 vertex addition acts trivially on
$\det(I - uB)$ — the gluing question lives entirely on the 2-core; the exact rationalisation
lemmas (L1–L3 in `numerics/wp06_bass_certify.py`) make the $n \le 6$ symbolic checks cheap.*

## Objective

Using the per-edge product form $\prod_e(1 - u^2w_e^2)\det M(u)$
([S05](../sources/PSC2-S05-salvaged-G1.md) §4): test, symbolically at $n \le 6$, whether the
sieve step $n \to n+1$ (adjoining the composites of $I_{n+1}$, i.e. Schur-complement rank-one
vertex additions) acts on the stage polynomials as an **Asano-type contraction /
Schur–Szegő composition preserving a zero locus** (Lee–Yang 1952; Asano 1970;
Borcea–Brändén 2009).

## Method

Each instance is a finite polynomial identity — sympy-verifier territory. The Schur-complement
block form of a single vertex addition (correctly derived, unlike X10's version) is the object
to compare against the Asano contraction template; the question is whether the linear
fractional structure it induces belongs to the stability-preserving class, **proved**, not
asserted.

## Deliverable

Either: an identified gluing structure (a lemma, tag **proven**, with the preserved locus
stated) — which would make route γ2 the first cross-scale structure to survive; or a
documented failure at small $n$.

## Falsifier (pre-registered; binding)

No identifiable gluing structure at $n \le 6$ ⇒ **close route γ entirely** (γ1 already closed
by X5); the gap program (WP07/WP08) does not depend on it.

## Pricing

Route γ at *full* Ramanujan strength, with C1, is the wall (W3) — reality-of-roots technology
is Hermite–Biehler in polynomial coordinates. Any partial gluing result is stated as the
locus-preservation lemma it is.
