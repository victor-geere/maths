# PSC2-WP07 — the normalised-gap theorem (G3), with the α/β gap-rung extensions

*Status: **open, tractable**. Census first — it is the cheap falsifier.*

## Objective

Prove: $\exists\, c > 0$ with $g_{\mathrm{sym}}(n) \ge c$ for all $n$ — the uniform
random-walk spectral gap of the bipartite divisor graph $B_n$ (measured stable at
$\approx 0.54$–$0.57$ for $n = 6\ldots9$; [N00 §3](../numerics/PSC2-N00-verification-targets.md)).

## Ordering (binding)

1. **Census extension to $n \le 14$** (sparse eigensolvers) **before** investing in the
   proof: drift down kills the conjecture early.
2. Proof attempt: the normalised one-mode operator is a doubly-smoothed divisor-correlation
   form; Perron vector explicit to first order; the fluctuation part is a bilinear form over
   $\#\{m \in I_n : pq \mid m\} - 2^n/(pq)$ — Brun–Titchmarsh + Montgomery's large sieve
   ([S02 §7](../sources/PSC2-S02-determinant-level.md), route α).

## Extensions (charter H3/H4; open after the base theorem)

- **Route α (P3.5):** weighted non-backtracking gap $\ge c/\log M_n$; through P2.4 (given C1)
  this is a de la Vallée Poussin-strength zero-free region. The expected strength must be
  *computed*, not assumed; the $1/\log$ match with the sieve's equidistribution rate is both
  a calibration sign and a ceiling (no more than dlVP without new input).
- **Route β:** Bordenave's tangle-free trace method with equidistribution replacing
  randomness — an independent engine for the same rung.

## Pricing

The base theorem is independently publishable-grade regardless of the zeta connection
(uniform expansion of sieve divisor graphs). The payoff dictionary through P2.4 activates
**only** if C1/H\* (WP12) lands; do not state zero-free-region claims before that.

## Falsifier

Census drift; or the bilinear-form estimates capping below a uniform constant (record the
best $c(n)$ profile either way).
