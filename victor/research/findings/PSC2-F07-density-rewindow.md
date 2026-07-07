# PSC2-F07 — the rewindowed density gate (E0b): the wedge-windowed $H^{G,\mathrm{w}}_n$ passes; the E-track reopens (and, per O6, this is not evidence about zeros)

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP02b](../workpackages/PSC2-WP02b-density-gate-rewindow.md). Code/run:
`numerics/wp02b_rewindow.py` (deterministic, no seed; `mpmath` dps 35 for all matrix
elements via exact closed forms with a float prefilter; `numpy` complex128 for the
eigensolves, certified against `mpmath.svd_c` below). Gate harness, metric, windows,
controls: `e0_density_gate.py`, reused verbatim. Tags per
[PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> - Counting $N^+(T) := \#\{\lambda \in \mathrm{spec}: 0 < \lambda \le T\}$; target
>   $R(T) := \frac{T}{2\pi}\log\frac{T}{2\pi}$; derived window $W_n = [T_{\mathrm{lo}}, T_n^{\mathrm{win}}]$
>   with $R(T_{\mathrm{lo}}) = \sqrt{d_n}$, $R(T_n^{\mathrm{win}}) = d_n$,
>   $d_n = \#\{\text{positive eigenvalues}\}$; $\mathrm{dev}_n = \max_{W_n}|N^+/R - 1|$ on a
>   200-point geometric grid.
> - **PASS** iff $\mathrm{dev}$ strictly decreasing over the last three stages **and** final
>   $\mathrm{dev} \le 0.05$. Stages: $n = 4, 6, 8, 10, 12$.
> - **Must-fail controls** (identical code path to F02): legacy $H_n'$; graph one-mode;
>   sine decoy. **Positive control** (smooth-law sample) must pass, else the run is invalid.
> - **O6 discipline (binding, stated in advance).** A wedge-shaped basis passes E0
>   *regardless of arithmetic content* — this gate can certify only that the redesign
>   repaired the killed component. **A PASS is not evidence about zeros**; it reopens the
>   E-track (WP03–WP05 unpause, WP04 first per the F02 ordering note) and nothing more.
>
> **Falsifier.** FAIL with spectrum tracking the ladder → obstruction is inventory
> discreteness, bar does not move post hoc; FAIL without tracking → the coherent-state
> wedge realisation is dead too, redesign goes to the prolate pencil; any control
> misbehaving → run invalid.

The builder and all its constants (sites, tiling widths $w_i$, $\sigma_i = w_i/2$, wedge
boundary $\tau_{\min}(u) = 2\pi e^{u-1}$, ladder spacings $2\pi/w_i$ with $4\pi/w_0$ at the
self-mirrored 0-site, offset $j + \tfrac12$, cap $T_n = 2\pi M_n^{2/3}$) were fixed in
WP02b before the gate ran; the ladder-vs-$R$ tracking and convexity checks performed at
design time are recorded there as part of the derivation, not the gate.

## Regression check

N00 targets reproduced: **yes** — §4 spot-values ($\gamma_1 = 14.1347251417$,
$\gamma_2 = 21.0220396388$, $\gamma_{10} = 49.7738324777$, $\sin(\pi\gamma_1) = 0.4107272152$,
$\sin(\pi\gamma_1)/(\pi\gamma_1) = 0.009249457$; consumed only in the regression line, per
I0.6); §2 legacy $\lVert A'\rVert_{\mathrm{op}} = 9.27, 19.5, 36.3$ at $n = 8, 10, 12$; §3
graph stage $\mu_1(B) = 3.5419$, #detached $= 4$, #detached-real $= 2$ at $n = 6$ — all
rebuilt through the source scripts' own functions and matching verbatim.

## The W1 stage builder (deliverable 1)

The rewindow changes **only** the phase-space window defining $V_n$; ambient, symmetry,
gate, and bar are F02's, unchanged. Modulated coherent states
$\psi_{i,j}(u) = (2\pi\sigma_i^2)^{-1/4}e^{-(u-u_i)^2/(4\sigma_i^2)}e^{i\tau_j u}$ sit on
the sieve sites ($u_0 = 0$ and $u_q = \log q$, $q = p^k \le M_n$); each site's frequency
ladder switches on at the Berry–Keating wedge boundary $\tau_{\min}(u_i) = 2\pi e^{u_i-1}$
— i.e. the inventory enters as **translation lengths** (frequency data), the way $\log q$
enters the explicit formula, discharging F02's redesign prescription. $V_n$ is
$J$-invariant by construction ($e = \psi + J\psi$, $o = \psi - J\psi$); by F01 C-c the
compression is exactly off-diagonal in the parity grading, so the spectrum is $\{\pm s_i\}$
with $s_i$ the singular values of the whitened graded block — **E1 pairing exact by
construction**, kernel reported separately ($\dim\ker = 0$ at every stage this run).

Matrix elements of $D$ and $D^2$ are exact closed forms (complex Gaussian integrals),
evaluated at dps 35 and validated against direct `mpmath.quad` quadrature to
$\le 3.2\times10^{-32}$ (with a Hermiticity cross-check at $4.9\times10^{-34}$), plus an
assembled miniature stage checked entry-by-entry ($\le 9.2\times10^{-16}$ vs quadrature).
Float64 certification: singular values agree with full `mpmath.svd_c` at dps 35 to
$3.5\times10^{-16}$ relative ($n = 4$ stage). Non-vacuity guards pass (full Gram rank at
every stage; zero columns dropped: none). The compression trace inequality
$\mathrm{tr}(H^{G,\mathrm{w}}_n)^2 \le \mathrm{tr}(P_nD^2P_n)$ holds at every stage, with
ratio $0.99 \to 0.9995$ ($n = 4 \to 12$) — near-saturation, i.e. the basis states are
nearly $D$-coherent, in sharp contrast to N0's $0.34 \to 0.25$. The $D^2$ blocks are the
WP04 pencil input, delivered.

## The derived Weyl law (deliverable 2) — zero fitted parameters, and convex

The parameter-free law is the enumerated ladder itself,
$N^{\mathrm{pred}}_n(T) = \#\{(i,j): \tau_j \le T\}$: one Planck cell per state tiling the
wedge $\{(u,\tau): 0 \le u \le 1 + \log\frac{\tau}{2\pi},\ \tau \le T_n\}$, whose one-sided
cell count is $\frac{T}{2\pi}\log\frac{T}{2\pi} + O(1)$ — the target $R(T)$ exactly,
including the $-T/2\pi$ cancellation carried by the $+1$ in the wedge extent (one integral,
derived in the WP before the run). The mechanical convexity check (wedge density
$\sum_{\tau_{\min} < T} w_i/2\pi$ nondecreasing in $T$) **passes at every stage**: the
family is structurally outside the class killed by F02's no-go lemma. Measured tracking:
$\max_{W_n}|N^+ - N^{\mathrm{pred}}|/d_n = 0.091 \to 0.007$, decreasing across all five
stages — the operator's spectrum follows the derived law, and increasingly well.

## Result

```
E0b — PRIMARY  H^{G,w}_n = P_n D P_n  (W1: wedge ladders on the sieve sites)
  [W1] n= 4  M_n=    31  T_n=    62.00  #sites(active)=   11  modes N=   22  dim V_n=   44
       dim=   44 (dropped   0 redundant)  ker=  0  d_n=   22  trH^2/trPD2P=0.9899  convex=True
       window=[   22.84,    60.87]  dev=     0.118   |N+ - N_pred|/d (derived law) = 0.091
  [W1] n= 6  M_n=   127  T_n=   158.75  #sites(active)=   24  modes N=   82  dim V_n=  164
       dim=  164 (dropped   0 redundant)  ker=  0  d_n=   82  trH^2/trPD2P=0.9959  convex=True
       window=[   33.81,   159.35]  dev=     0.104   |N+ - N_pred|/d (derived law) = 0.037
  [W1] n= 8  M_n=   511  T_n=   401.60  #sites(active)=   44  modes N=  269  dim V_n=  538
       dim=  538 (dropped   0 redundant)  ker=  0  d_n=  269  trH^2/trPD2P=0.9983  convex=True
       window=[   49.79,   405.57]  dev=     0.064   |N+ - N_pred|/d (derived law) = 0.026
  [W1] n=10  M_n=  2047  T_n=  1012.96  #sites(active)=   85  modes N=  813  dim V_n= 1626
       dim= 1626 (dropped   0 redundant)  ker=  0  d_n=  813  trH^2/trPD2P=0.9991  convex=True
       window=[   73.03,  1006.32]  dev=     0.022   |N+ - N_pred|/d (derived law) = 0.011
  [W1] n=12  M_n=  8191  T_n=  2553.12  #sites(active)=  176  modes N= 2438  dim V_n= 4876
       dim= 4876 (dropped   0 redundant)  ker=  0  d_n= 2438  trH^2/trPD2P=0.9995  convex=True
       window=[  108.80,  2550.45]  dev=     0.020   |N+ - N_pred|/d (derived law) = 0.007

  ratio profile N+(T)/R(T) at n=12 (sampled over the derived window):
    T =    108.80   N+/R =     1.013
    T =    169.58   N+/R =     1.012
    T =    264.33   N+/R =     1.004
    T =    418.59   N+/R =     1.001
    T =    652.46   N+/R =     1.002
    T =   1033.24   N+/R =     1.001
    T =   1610.53   N+/R =     0.999
    T =   2550.45   N+/R =     0.993

  dev sequence over stages (4, 6, 8, 10, 12):  0.118  0.104  0.064  0.022  0.020
  E0b PRIMARY: PASS (pre-registered: last-3 strictly decreasing AND final <= 0.05)

E0 — CONTROLS
        legacy n=8       4.196   FAILS E0 [as required]
       legacy n=10       8.274   FAILS E0 [as required]
       legacy n=12      15.793   FAILS E0 [as required]
         graph n=6       3.243   FAILS E0 [as required]
         graph n=8       6.348   FAILS E0 [as required]
         graph n=9       8.849   FAILS E0 [as required]
        sine decoy       1.187   FAILS E0 [as required]
  harness positive control (smooth-law sample; no gamma-list):
    d =   152   dev = 0.0397
    d =   609   dev = 0.0186
    d =  2438   dev = 0.0091
    -> PASSES (metric is demonstrably passable)

VERDICT (mechanical application of the pre-registered rule)
  harness valid:            True  (positive control passes: True; all must-fail controls fail: True)
  E0b, primary H^{G,w}_n:   PASS
```

The numbers say: where F02's concave family swept through the target once
($7.3 \to 0.76$, single crossing, deviation growing with stage), the wedge family's ratio
profile hugs $1$ across the entire derived window at $n = 12$ ($1.013 \to 0.993$), the
deviation sequence decreases as required ($0.118 \to 0.020$ against the bar $\le 0.05$),
and the spectrum tracks the parameter-free ladder law to $0.007\,d_n$. The same harness
that killed N0 validates itself again two-sidedly: every negative control fails by one to
three orders of magnitude, and the smooth-law positive control passes with deviation
decreasing.

## Verdict against the pre-registered criteria

**PASS — the rewindowed primary $H^{G,\mathrm{w}}_n$ clears E0b**, with the harness valid.
Consequences, exactly as pre-registered and no further:

1. **The E-track reopens.** WP03–WP05 pause notices are lifted; WP04 (certified enclosures)
   is first in line, its pencil input $(H^{G,\mathrm{w}}_n, P_nD^2P_n)$ delivered by this
   builder. The working primary of L4 is now the W1 family.
2. **O6, restated at the moment of passing (binding).** The wedge law was *designed into*
   the basis; any wedge-shaped family passes E0 regardless of arithmetic content
   (Connes–Moscovici is the proven precedent, [S00 §8](../sources/PSC2-S00-verified-foundation.md)).
   E0 is a filter that can only kill — it killed N0, and it cannot confirm W1. Whether the
   sieve inventory's placement of the ladders carries any arithmetic beyond the counting
   law is exactly what gates E4b and the WP05 decoy battery (bare-wedge decoy: must pass
   E0's shape, must fail E4b) exist to decide.

## Tag

- W1 builder, exact chiral structure, E1-pairing-by-construction, matrix elements of $D$
  and $D^2$: **proven** (closed forms; self-tested to $10^{-32}$; `svd_c` certification).
- Derived wedge Weyl law $= R(T) + O(1)$ (cell-count integral) and its convexity:
  **proven** (one-integral derivation in the WP; mechanical check in-run).
- E0b measurements, controls, and the PASS verdict: **verified** against the
  pre-registered criteria (deterministic run, regression anchors reproduced).
- Any statement connecting this family to the zeros: **none made** — deferred to
  E4b/WP05 by construction (O6).

**Scope (do-not list compliance).** No $\gamma$-list, no $N(T)$-unfolding, no fitted
parameter appears anywhere in the construction or the metric ($\gamma$-values occur only
in the N00 regression line). A passed density gate is a statement about this operator
family's counting law, not about the zeros. Nothing here bears on the truth of RH, which
remains **open**.

## Propagation

Charter ledger updated: **yes** (E0 row → W1 rewindow passed, E-track reopened; live-
conjecture list annotated; ordering update appended). WP02b status → done (passed).
Pause notices lifted on WP03, WP04, WP05 (with the O6 caveat repeated at each site).
F02 unaffected (its kill and no-go lemma stand — W1 is outside the killed class by the
convexity that this run checks mechanically). Source doc correction notice needed: **no**
(S03 states E0 as a target; status lives in the charter ledger per PSC2-001 §1).
