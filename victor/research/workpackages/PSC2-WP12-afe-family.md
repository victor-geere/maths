# PSC2-WP12 — the AFE-symmetric family V2 (G2): the corrected H\* attack

*Status: **open** — high-risk / high-value. WP01 landed (6 Jul 2026): HS5 is **proven**
([PSC2-F01](../findings/PSC2-F01-pairing-lemma.md)), fixing the family's form — paired
spectra, even stage products. This WP is unblocked.*

## Objective

Replace the eliminated family V1 (X4) by V2 obeying design law C-2, in the spectral form
mandated by HS5 (**proven**, [F01](../findings/PSC2-F01-pairing-lemma.md)).

**Binding family definition (spectral; supersedes the kernel schematic below).** A V2 member
is a stage family whose stage spectra are $\pm$-paired by construction — equivalently
(F01, Thm HS5) whose stage determinants are even in $t$ / exactly
$s \leftrightarrow 1-s$ symmetric. By F01 this single requirement delivers H\*-d (the Vitali
identification set) automatically, the stage products are exponential-factor free (the
target's even-Hadamard normal form at every stage), and all odd spectral moments vanish
exactly (free integrity check, F01 C-a). The route to pairing is E1: exhibit a $J$-invariant
stage construction (or an exact chiral/bipartite grading, F01 C-c).

*Kernel schematic (heuristic starting point only, no longer the definition):* symmetrised
AFE/Riemann–Siegel-type kernels
$$C^{V2}_{pq}(s) = \sum_{m \in I_n,\ pq \mid m} a_p a_q
\big[m^{-s}\varphi(s) + m^{s-1}\varphi(1-s)\big]\cdot(pq)^{\mathrm{calibration}},$$
with $\varphi$ a smooth AFE cutoff — admissible only if the resulting stage spectra are
verified $\pm$-paired (the F01 controls give the test: symmetry defect and FE defect at
machine precision). Re-run the F5 stability sweep and F6 asymmetry sweep against the
baselines in [N00 §3](../numerics/PSC2-N00-verification-targets.md).

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
