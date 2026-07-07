# PSC2-WP08 — block-purity of the detached spectrum (G4): the anti-Siegel theorem

*Status: **open**. Depends on WP06 Part B (a locus against which "detached" is defined).*

*Gating update (7 Jul 2026, [F03](../findings/PSC2-F03-weighted-locus.md)): WP06 landed in
its pre-registered weak branch — the proven annulus has $r_1 \ll 1/\rho$ at every stage
(locus-detached count $0$), so it defines "graph-Siegel" in principle (F03 Def. B6) but cannot
isolate the structural pair. Per WP06's falsifier this WP's **theorem target is re-scoped to
the measured census** ($|\mu| > 1.02\sqrt{\mu_1}$, exactly 4 detached, 2 real, stable
$n = 5\ldots9$); the β-sweep ordering below is unchanged. F03's recorded margins for any
future sharpening: at $n=7$ the Perron pair sits at $|u| = 0.1894$ vs nearest non-real pair
$0.2054$ — the separation exists empirically; the unconsumed balance identity ($\dagger$) is
the lever.*

## Objective

Upgrade F4 from measurement to theorem: relative to WP06's locus, the detached spectrum of
$B_w$ consists exactly of the structural part (Perron + bipartite mirror + one conjugate
pair) — **no arithmetic exceptionals**. Measured: exactly 4 detached at every stage
$n = 6\ldots9$, $\beta = \tfrac12$ ([N00 §3](../numerics/PSC2-N00-verification-targets.md)).

## Ordering (binding)

1. **$\beta$-sweep first** ($\beta \in [0.3, 0.7]$, numerically): check the finding is not a
   $\beta = \tfrac12$ accident.
2. Proof: community-detection technology (Krzakala et al.; Bordenave–Lelarge–Massoulié) —
   detached non-backtracking eigenvalues count structural blocks; our graph has an explicit
   2-block (prime/composite) + degree-profile structure, so the expected detached set is
   computable. Proof input: divisor-count concentration (shared with WP07).

## Significance if proven

The finite stages provably exhibit **no Landau–Siegel avatar** — a clean structural statement
about the sieve, meaningful independent of RH; the honest finite-stage half of what the
discarded proof-sketch hand-waved as "avoiding exceptional zeros."

## Falsifier (two-sided, pre-registered)

A $\beta$ at which a fifth eigenvalue detaches **persistently** across stages — a genuine
discovery either way; document per the two-sided rule (I0.4), do not suppress.

## Pricing

Below the wall. The graph-Siegel *dictionary* (exceptional real poles ↔ Landau–Siegel
phenomena) stays tagged **heuristic** even if the theorem lands; only the block-purity
statement itself gets **proven**.
