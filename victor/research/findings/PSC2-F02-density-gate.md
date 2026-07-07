# PSC2-F02 — the density gate (E0): the primary $H^G_n$ is killed; N0 builder delivered

*Finding note. Date: 2026-07-06. Work package:
[PSC2-WP02](../workpackages/PSC2-WP02-density-gate.md). Code/run:
`numerics/e0_density_gate.py` (deterministic, no seed; `mpmath` dps 35 for all matrix
elements; `numpy` float64 for the eigensolves, certified against `mpmath.svd_r` below).
Tags per [PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> - **Pass:** $N_n(T)/\big(\frac{T}{2\pi}\log\frac{T}{2\pi}\big) \to 1$ on derived windows,
>   coefficients derived, not fitted.
> - **Must-fail controls:** legacy $H_n'$ (density mismatch regression,
>   [S06](../sources/PSC2-S06-constraints-and-walls.md) §2.2); graph one-mode (F4 structural
>   spectra, [S02](../sources/PSC2-S02-determinant-level.md) §6).
> - **Shape-decoy caution (O6):** passing E0 is *not* evidence of matching zeros — any
>   two-cutoff dilation model passes; the decoy control lives in WP05.
>
> **Falsifier.** $H^G_n$ failing E0 kills the primary candidate — recorded per the phase-4
> precedent; the E-track then stops until a redesigned window is proposed, and the project's
> weight shifts to the L3 packages (WP06–WP08, WP12).

Operationalisation (fixed in the script header before any run): counting
$N^+(T) := \#\{\lambda \in \mathrm{spec},\ 0 < \lambda \le T\}$ (for the unpaired legacy
control, $\#\{|\lambda| \le T\}/2$); target $R(T) := \frac{T}{2\pi}\log\frac{T}{2\pi}$ (the
WP's own denominator, verbatim); derived window $W_n := [T_{\mathrm{lo}}, T_n]$ with
$R(T_{\mathrm{lo}}) = \sqrt{d_n}$, $R(T_n) = d_n$, $d_n = \#\{\text{positive eigenvalues}\}$
(the S03 §4 bookkeeping — a computation, never a fit); metric
$\mathrm{dev}_n := \max_{W_n} |N^+(T)/R(T) - 1|$ on a 200-point geometric grid; **PASS** iff
$\mathrm{dev}$ is strictly decreasing over the last three stages **and** final
$\mathrm{dev} \le 0.05$. Harness validity: a synthetic spectrum sampled from the smooth law
itself ($R(\lambda_k) = k - \tfrac12$; no $\gamma$-list) must pass, and the sine decoy
(I0.7) must fail, else the run is invalid.

## Regression check

N00 targets reproduced: **yes** — §4 spot-values ($\gamma_1 = 14.1347251417$,
$\gamma_2 = 21.0220396388$, $\gamma_{10} = 49.7738324777$,
$\sin(\pi\gamma_1) = 0.4107272152$, $\sin(\pi\gamma_1)/(\pi\gamma_1) = 0.009249457$; consumed
only in the regression line, per I0.6); §2 legacy $\lVert A'\rVert_{\mathrm{op}} = 9.27,
19.5, 36.3$ at $n = 8, 10, 12$ (rebuilt through `sieve_operator.py`'s own functions); §3
graph stage $\mu_1(B) = 3.5419$, #detached $= 4$, #detached-real $= 2$ at $n = 6$ (through
`prime_graph_lab.py`'s own builders). All match verbatim.

## The N0 stage builder (deliverable 1) — constructed, and F01's residual obligation discharged

Ambient: $L^2(\mathbb R, du)$ with $D = -i\,d/du$ — unitarily the dilation generator on
$L^2(\mathbb R_+, dx)$ via $u = \log x$ (S03 Lemma 1.1: the $\tfrac12$ is carried by the
normalisation), and $J$ = parity, satisfying $JDJ^{-1} = -D$ exactly. Stage subspace $V_n$,
**$J$-invariant by construction**:

- *finite places:* one even + one odd mode per prime power $q = p^k \le M_n$ (the sieve
  inventory): normalised Gaussians $g_q$ at $u = \pm\log q$, symmetrised
  $e_q = g_q + Jg_q$, $o_q = g_q - Jg_q$, width $\sigma_q = \mathrm{gap}_q/2$ (half the
  distance to the nearest other inventory point — derived from the inventory, not chosen);
- *archimedean place:* Mellin–Hermite modes $h_j$, $j < m_n = \#\{j : \sqrt{2j+1} \le L_n\}$,
  $L_n = \log M_n$ — the phase-space disk of radius $L_n$, the $O(L_n^2)$ block of the S03
  §4 bookkeeping.

Matrix elements of $D$ and $D^2$ are exact closed forms (Gaussian integrals; Hermite ladder
algebra; a three-term recursion for $\langle h_j, g_{a,\sigma}\rangle$), evaluated at dps 35
and validated against direct `mpmath.quad` quadrature to $\le 2.4\times10^{-35}$, plus an
assembled miniature stage checked entry-by-entry. In the parity grading $H^G_n = P_nDP_n$ is
exactly off-diagonal (F01 corollary C-c), so the stage spectrum is $\{\pm s_i\}$ with $s_i$
the singular values of the graded block: **the E1 pairing is exact by construction** —
symmetry defect and odd moments are identically zero, and the kernel multiplicity is
reported separately (C-b; $\dim\ker = 23$ at $n = 12$). This exhibits the $J$-invariant
basis compatible with the sieve inventory whose existence F01 assumed
($JV_n = V_n$ **constructed**, not assumed — the reportable-obstruction branch of WP01's
falsifier did *not* occur). Float64 certification: singular values agree with full
`mpmath.svd_r` at dps 35 to $5.1\times10^{-16}$ relative ($n = 4$ stage); the compression
trace inequality $\mathrm{tr}\,(H^G_n)^2 \le \mathrm{tr}\,(P_nD^2P_n)$ holds at every stage
(ratio $0.34 \to 0.25$, $n = 4 \to 12$). Non-vacuity guards all pass (full Gram rank; zero
columns dropped).

## The derived Weyl law (deliverable 2) — zero fitted parameters

Each basis state occupies one Planck cell of area $2\pi$: inventory site $q$ contributes the
cell $[\log q \pm \tfrac12\mathrm{gap}_q] \times [-\pi/\mathrm{gap}_q, \pi/\mathrm{gap}_q]$
(and its mirror), Hermite mode $j$ the shell of radius $\sqrt{2j+1}$ in the disk. The
intrinsic one-sided counting law of the stage family is therefore
$$N^{\mathrm{pred}}_n(T) \;=\; \sum_{q \le M_n} \min\!\Big(\frac{T\,\mathrm{gap}_q}{\pi},\,1\Big)
\;+\; \sum_{j < m_n} \frac{2}{\pi}\arcsin\!\Big(\min\big(1,\,T/\sqrt{2j+1}\big)\Big),$$
with every quantity read off the operator's own basis — no fitted coefficient anywhere
(derivation: semiclassical cell counting; tag **heuristic** as a law, **verified** against
the measured counts below: $\max_{W_n}|N^+ - N^{\mathrm{pred}}|/d_n = 0.10$–$0.16$ across
all five stages).

**Lemma (E0 no-go for concave counting laws) — proven.** Let $N$ be absolutely continuous
with $N(0) = 0$ and nonincreasing density $N' \ge 0$, and suppose
$|N/R - 1| \le \varepsilon$ on $[A, B]$ with $2\pi e \le A < B$. Since
$N(A) = \int_0^A N' \ge A\,N'(A)$ and $N(B) \le N(A) + (B-A)N'(A) \le N(A)\,B/A$,
$$\frac{1-\varepsilon}{1+\varepsilon} \;\le\; \frac{R(A)\,B}{A\,R(B)}
\;=\; \frac{\log(A/2\pi)}{\log(B/2\pi)}, \qquad\text{i.e.}\qquad
\varepsilon \;\ge\; \frac{\rho - 1}{\rho + 1},\quad
\rho := \frac{\log(B/2\pi)}{\log(A/2\pi)}.$$
On the derived windows ($R(T_{\mathrm{lo}}) = \sqrt{d_n}$, $R(T_n) = d_n$) one has
$\rho \to 2$, so $\varepsilon \ge \tfrac13 - o(1)$: **no stage family whose counting law is
concave above its band edge can pass E0.** $\blacksquare$

$N^{\mathrm{pred}}_n$ is concave (each summand is), and so is the phase-space law of *any*
fixed basis whose cells are frequency intervals centred on $\tau = 0$ — any bump widths, any
positions, any disk window. The pre-registered pass criterion is thus provably out of reach
for the entire design class of the N0 instantiation, not merely for this parameter choice.
At stage 12 the lemma's floor is $\varepsilon \ge 0.351$ ($\rho = 2.08$); the measured
deviation is $6.34$ — the family is far worse than the concavity floor because its dimension
budget ($\sim 2M_n/\log M_n$ states) sits at low frequencies where $R$ is still polynomially
small.

## Result

```
E0 — PRIMARY  H^G_n = P_n D P_n  (N0: sieve inventory bumps + Hermite disk)
  [N0] n= 4  M_n=    31  |Q_n|=   17  L_n= 3.434  m_n=  6  dim V_n=   40
       dim=   40 (dropped   0 redundant)  ker= 0  d_n=   20  trH^2/trPD2P=0.3419
       window=[   22.23,    56.99]  dev=     3.472   |N+ - N_pred|/d (derived law) = 0.150
  [N0] n= 6  M_n=   127  |Q_n|=   43  L_n= 4.844  m_n= 12  dim V_n=   98
       dim=   98 (dropped   0 redundant)  ker= 0  d_n=   49  trH^2/trPD2P=0.2830
       window=[   28.85,   108.18]  dev=     4.000   |N+ - N_pred|/d (derived law) = 0.101
  [N0] n= 8  M_n=   511  |Q_n|=  116  L_n= 6.236  m_n= 19  dim V_n=  251
       dim=  251 (dropped   0 redundant)  ker= 1  d_n=  125  trH^2/trPD2P=0.2572
       window=[   38.66,   220.69]  dev=     4.993   |N+ - N_pred|/d (derived law) = 0.130
  [N0] n=10  M_n=  2047  |Q_n|=  339  L_n= 7.624  m_n= 29  dim V_n=  707
       dim=  707 (dropped   0 redundant)  ker= 1  d_n=  353  trH^2/trPD2P=0.2508
       window=[   54.60,   505.50]  dev=     4.855   |N+ - N_pred|/d (derived law) = 0.157
  [N0] n=12  M_n=  8191  |Q_n|= 1077  L_n= 9.011  m_n= 41  dim V_n= 2195
       dim= 2195 (dropped   0 redundant)  ker=23  d_n= 1097  trH^2/trPD2P=0.2485
       window=[   81.29,  1293.80]  dev=     6.337   |N+ - N_pred|/d (derived law) = 0.159

  ratio profile N+(T)/R(T) at n=12 (sampled over the derived window):
    T =     81.29   N+/R =     7.337
    T =    119.99   N+/R =     5.202
    T =    177.10   N+/R =     3.666
    T =    265.08   N+/R =     2.629
    T =    391.27   N+/R =     1.940
    T =    585.63   N+/R =     1.384
    T =    864.42   N+/R =     1.070
    T =   1293.80   N+/R =     0.763

  dev sequence over stages (4, 6, 8, 10, 12):  3.472  4.000  4.993  4.855  6.337
  E0 PRIMARY: FAIL (pre-registered: last-3 strictly decreasing AND final <= 0.05)

E0 — CONTROLS
        legacy n=8       4.196   FAILS E0 [as required]
       legacy n=10       8.274   FAILS E0 [as required]
       legacy n=12      15.793   FAILS E0 [as required]
         graph n=6       3.243   FAILS E0 [as required]
         graph n=8       6.348   FAILS E0 [as required]
         graph n=9       8.849   FAILS E0 [as required]
        sine decoy       1.446   FAILS E0 [as required]
  harness positive control (smooth-law sample; no gamma-list):
    d =    68   dev = 0.0532
    d =   274   dev = 0.0270
    d =  1097   dev = 0.0129
    -> PASSES (metric is demonstrably passable)

VERDICT (mechanical application of the pre-registered rule)
  harness valid:            True  (positive control passes: True; all must-fail controls fail: True)
  E0, primary H^G_n:        FAIL
```

The numbers say: the compression's counting ratio sweeps monotonically from $7.3$ down
through $1$ to $0.76$ across the derived window — a *single crossing* of the target, exactly
the shape the no-go lemma forces on a concave law against the convex
$\frac{T}{2\pi}\log\frac{T}{2\pi}$, and never window convergence. The deviation sequence
*grows* with the stage ($3.5 \to 6.3$) where the pass criterion demanded decrease to
$\le 0.05$; the derived (parameter-free) law tracks the measured counts to $\le 0.16\,d_n$
throughout, confirming that the failure is structural, not numerical. Meanwhile the harness
proves its own two-sidedness: the smooth-law sample passes with deviation decreasing
($0.053 \to 0.013$), and every negative control fails by one to two orders of magnitude
above the threshold.

## Verdict against the pre-registered criteria

**FAIL — the primary candidate $H^G_n$, as instantiated by the N0 builder, is killed at
E0**, in precisely the WP's falsifier branch: recorded per the phase-4 precedent; the
E-track (WP03–WP05) stops until a redesigned window is proposed; the project's weight shifts
to the L3 packages (WP06–WP08, WP12). Both must-fail controls fail as required, so the kill
is informative, not a harness artifact.

**Why it fails, and what a redesign must do (exploratory; routed to any future WP02b).** The
N0 design inherits the *position* reading of the inventory — bumps at $u = \pm\log q$ with
frequency cells centred on $\tau = 0$ — which is the residue of the refuted
eigenvalue-at-$\{\log p\}$ picture (X1). The no-go lemma shows this whole class (fixed,
$\tau$-symmetric-cell bases) has concave counting and is dead at E0 *by proof*, independent
of widths or weights. In the explicit formula the primes enter as **translation lengths**
(the test function is sampled at $\log q$ — frequency data, not position data); a family
that carries the $T\log T$ law intrinsically must have wedge-shaped phase-space support —
$u$-extent growing like $\log\frac{|\tau|}{2\pi}$ at height $\tau$, the Berry–Keating
two-cutoff wedge, realised rigorously by the Connes–Moscovici prolate operator
([S00 §8](../sources/PSC2-S00-verified-foundation.md)), which is quadratic in the pencil
$(D, x)$ rather than a fixed-basis compression of $D$ — connecting naturally to WP04's
pencil $(P_nDP_n, P_nD^2P_n)$, whose $D^2$ matrix elements this builder already supplies.
Per O6, note the converse discipline: a wedge-shaped basis would pass E0 *regardless of
arithmetic content* — E0 is a filter that can only kill, never confirm, which is exactly
what it did here.

## Tag

- N0 builder, exact chiral structure, E1-pairing-by-construction, matrix elements:
  **proven** (closed forms; self-tested to $10^{-35}$; the $JV_n = V_n$ construction
  discharges F01's residual hypothesis).
- E0 no-go lemma for concave counting laws: **proven** (three-line proof above).
- E0 measurements, controls, and the FAIL verdict: **verified** against the pre-registered
  criteria (deterministic run, regression anchors reproduced).
- The redesign directions (wedge support, prolate pencil): **exploratory**.

**Scope (do-not list compliance).** No $\gamma$-list, no $N(T)$-unfolding, no fitted
parameter appears anywhere in the construction or the metric ($\gamma$-values occur only in
the N00 regression line). A *failed* density gate is a statement about this operator family,
not about the zeros; and per O6 even a passed one would not have been evidence about zeros.
Nothing here bears on the truth of RH, which remains **open**.

## Propagation

Charter ledger updated: **yes** (T2 → done/killed; live conjecture 4 → refuted; E0 row →
failed; E-track ordering note added; E1 row annotated with the delivered construction).
WP02 status → done (killed). Pause notices added to WP03, WP04, WP05 (E-track stopped per
the falsifier; WP04 note records that its $P_nD^2P_n$ inputs are nevertheless now
available). Source doc correction notice needed: **no** (S03 states E0 as a target; status
lives in the charter ledger per PSC2-001 §1).
