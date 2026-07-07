# PSC2-WP09 — the truncation-rate proposition, standalone with constants

*Status: **open** (content essentially banked; packaging + constants pending). Independent —
start any time.*

## Objective

State and prove, as a single tagged proposition with explicit constants, the stage-$n$
truncation bound already implicit in [S00](../sources/PSC2-S00-verified-foundation.md) §5
(Prop 6.1) and realised adelically in §6.3(c):

$$\Big|\mathrm{Tr}\big(W^{1/2}g(A)W^{1/2}\big) -
\mathrm{Tr}\big(W_n^{1/2}g(A_n)W_n^{1/2}\big)\Big| \le C_g\,M_n^{-\varepsilon},$$

with $C_g$ made explicit for the Gaussian test family of `adele_trace.py` (the measured
constant is $\approx 2.0$ at $\varepsilon = \tfrac12$; [N00 §1](../numerics/PSC2-N00-verification-targets.md)),
and the $\varepsilon$-dependence $C\,c\,\frac{1+\varepsilon}{\varepsilon}$ traced through the
Chebyshev bound.

## Deliverable

A one-theorem finding note (tag target **proven**) plus a regression test comparing the
derived $C_g$ against the measured $|error| \cdot M_n^{1/2} \to 2.0$ column — the derived
constant must upper-bound the measured one, with the gap reported.

## Why it earns a work package

It is the quantitative envelope every harness component (WP05 E4a) prices against; making
the constant explicit converts "within the proven envelope" from a phrase into a number.

## Falsifier

Derived constant below the measured one = an error in the derivation or the code; either is
a finding.
