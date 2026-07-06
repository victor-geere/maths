# Phase 5 — Hecke / Langlands enrichment on $\mathrm{GL}_1$

*Implements §7 of [prime-sieve-adele-plan.html](prime-sieve-adele-plan.html).*
*Status: **exploratory / conjectural**. The Phase 3–4 gate is now cleared — they are **corrected**
([phase3.md](phase3.md), [phase4.md](phase4.md)); the speculative parts below remain gated on their
own merits.*

Back: [phase4.md](phase4.md) · Index: [index.md](index.md).

## 5.1 The proposal

The Hecke algebra $\mathcal H$ of $\mathrm{GL}_1(\mathbb A_\mathbb{Q})$ acts on the adèle class
space by correspondences. Local Hecke operators $T_p$ act at the place $p$; the plan observes
that the sieve's factorisation data — "which primes divide $m$, with what exponents" — *is*
precisely the record of local Hecke correspondences. Enriching the finite operators $H_n$ with
the $T_p$ should give a joint spectral decomposition recovering the automorphic characters of
$\mathrm{GL}_1$, i.e. the Hecke (Größencharakter) $L$-functions.

## 5.2 What is actually solid here

The one rigorous grain: for $\mathrm{GL}_1$, "automorphic forms" are Hecke characters, and their
$L$-functions are Dirichlet $L$-functions $L(s,\chi)$. The sieve/kernel construction of
[prime-side.md](prime-side.md) generalises verbatim from $\zeta=L(s,\chi_0)$ to $L(s,\chi)$ by
twisting the von Mangoldt weights: $\Lambda(q)\mapsto\chi(q)\Lambda(q)$, giving the kernel
$-\frac{L'}{L}(1-i(\lambda-\bar\mu),\chi)$. That much is a genuine, provable extension and is the
sensible first concrete step — it is also already on the master board as Phase 2c
([../../../research/phase-2-dirichlet-family/dirichlet-lf.md](../../../research/phase-2-dirichlet-family/dirichlet-lf.md)).

## 5.3 What is speculative

- "$H_n$ enriched by $T_p$ recovers the Langlands correspondence for $\mathrm{GL}_1$" —
  $\mathrm{GL}_1$ Langlands is class field theory, already fully known; casting it as a spectral
  decomposition of sieve operators is at best a re-encoding. Phase 3/4 now *do* produce a
  meaningful object — the corrected, non-vacuous $H_n'$ and its accepted trace target
  ([phase3.md](phase3.md), [phase4.md](phase4.md)) — but even so, that trace target is not an
  eigenbasis, so a "joint spectral decomposition recovering Hecke characters" remains speculative.
- Any suggestion that this reaches beyond $\mathrm{GL}_1$ (toward $\mathrm{GL}_n$ automorphy) is
  unsupported and should not be written down as a claim.

## 5.4 Honest gate — now cleared

Both gating conditions are met:
1. Phase 3 has a non-vacuous, correctly-normalised operator — Def 3.2 with
   $\varepsilon_n=c/\lVert A'\rVert$ ([phase3.md](phase3.md) §3.3); and
2. Phase 4's trace reformulation ([phase4.md](phase4.md) §4.4) is the accepted target.

So Hecke enrichment now decorates a well-defined object. What remains gated is *internal* to this
phase, not to Phases 3–4: the solid, provable step is the twist to $L(s,\chi)$ (§5.2); the
"$T_p$-enriched $H_n$ recovers Langlands $\mathrm{GL}_1$" picture stays speculative on its own
merits (§5.3), since the corrected operator's role is a trace, not an eigenbasis of Hecke
characters.

## 5.5 Task status

| Task | Status |
|---|---|
| Twist to $L(s,\chi)$: kernel $-\frac{L'}{L}(\dots,\chi)$ | **tractable next step** (§5.2); provable |
| Sieve $\times$ Dirichlet character numerics | **open**, low-risk |
| "$T_p$-enriched $H_n$ = Langlands $\mathrm{GL}_1$" | **speculative** (3–4 gate cleared; §5.4) |
| Beyond $\mathrm{GL}_1$ | out of scope; no claim |

**Recommendation.** Fold the solid part (§5.2) into the existing Phase-2c Dirichlet-family task
rather than treating it as a separate adèle-sieve deliverable; leave the Hecke-operator picture
as a remark until Phases 3–4 are on firm ground.
