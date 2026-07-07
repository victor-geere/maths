# PSC2-F08 — certified enclosures (E3b): the pencil gate passes, and the radii saturate at a positive floor (a resolution caveat the E-track now carries)

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP04](../workpackages/PSC2-WP04-certified-enclosures.md). Code/run:
`numerics/wp04_certified_enclosures.py` (deterministic, no seed; pencil matrices are the
W1 closed forms of `wp02b_rewindow.py` at `mpmath` dps 35; `numpy` complex128 companion
eigensolves, certified against `mpmath.eig` and independent quadrature below). Tags per
[PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> - radii decreasing in $n$ over at least three consecutive stages on the window $[0, 50]$;
> - every certified interval cross-checked against independently computed truth **only at the
>   final-evaluation step** (I0.6).
>
> **Falsifier.** Radii stagnating while E0 passes = the compression sees the right density
> but cannot localise — a genuine, reportable obstruction profile (it would point at the
> archimedean window's band-limit dual as the bottleneck).

Operationalisation, fixed in the script header before the run (the bar itself is the WP's,
unmoved): certified interval for each positive stage eigenvalue $s_i \le 50$ = the
second-order pencil root $z$ minimising $|z - s_i|$, radius $|\mathrm{Im}\,z|$; stage
statistic $\rho_n$ = **median** radius; PASS iff $\rho_n$ strictly decreasing over $\ge 3$
consecutive computed stages; stages $n = 4, 6, 8, 10, 12$ (the E0b stages); three controls
(fixed-basis decoy and constant-radius synthetic must fail, shrinking-radius synthetic must
pass) on the identical solver/matching/median/verdict code path; validity guards
(`mpmath.eig` certification, single-coherent-state closed form, Rayleigh consistency,
independent-quadrature truth check at the final-evaluation step only); regression anchors
first. The rate fit $\rho_n \sim C(\log M_n)^{-\alpha}$ is report-only, not a gate.

## The imported theorem, and what is actually certified here

**Theorem (classical — proven; Shargorodsky 2000; Levitin–Shargorodsky 2004; refinements
Boulton–Levitin 2007, Boulton–Strauss 2011; survey Davies–Plum 2004).** For self-adjoint
$A$ and any finite-dimensional trial space $\mathcal L$: if $z$ is in the second-order
spectrum of $A$ relative to $\mathcal L$ (i.e. $\det(Q - 2zB + z^2S) = 0$ with $S, B, Q$
the matrices of $1, A, A^2$ on $\mathcal L$), then
$\mathrm{spec}(A) \cap [\mathrm{Re}\,z - |\mathrm{Im}\,z|,\ \mathrm{Re}\,z + |\mathrm{Im}\,z|]
\ne \emptyset$ — with **no** norm-resolvent hypothesis: pollution-free by theorem.

**Quasi-mode identity (proven, one line).** If $z = x + iy$, $y \ne 0$, solves the pencil
with eigenvector $u \in V_n$, then testing $P_n(D - z)^2u = 0$ against $u$ itself and
separating real and imaginary parts gives $\langle u, (D - x)u\rangle = 0$ and
$$\lVert (D - x)\,u \rVert \;=\; |y| \cdot \lVert u \rVert \qquad \text{exactly.}$$

**Honesty clause (stated in the WP script before the run, binding on the reading).** On
this ambient (S03 Lemma 1.1) $\mathrm{spec}(D) = \mathbb R$, purely absolutely continuous —
so the interval-intersection statement is **trivially true** and discovers nothing about
$\mathrm{spec}(D)$. What the run certifies is (i) the enclosure machinery itself, validated
against `mpmath.eig`, closed forms, and independent quadrature, and (ii) the radii
$|\mathrm{Im}\,z|$ as **certified resolution data**: each matched root exhibits a normalised
quasi-mode $u \in V_n$ with $\lVert(D - \mathrm{Re}\,z)u\rVert = |\mathrm{Im}\,z|$. The
radii and their stage genealogy are the deliverable (the WP05/HS7 feed). O6 binds
throughout: nothing here is evidence about zeros.

**Cross-science note (per the WP).** Second-order relative spectra were developed to kill
spectral pollution for compressed **Dirac operators** in relativistic quantum chemistry
(Levitin–Shargorodsky 2004; Boulton–Boussaid 2010 for Dirac); this run reuses that
technology unchanged on the adelic Dirac normal form $D = -i\,d/du$.

## Regression check

N00 targets reproduced: **yes** — §4 spot-values ($\gamma_1, \gamma_2, \gamma_{10}$,
$\sin(\pi\gamma_1)$, $\sin(\pi\gamma_1)/(\pi\gamma_1)$; consumed only in the regression
line, per I0.6); §2 legacy $\lVert A'\rVert_{\mathrm{op}} = 9.27, 19.5, 36.3$; §3 graph
stage $\mu_1 = 3.5419$, #detached $= 4$, #detached-real $= 2$. F07 E0b anchors reproduced
through the F07 code path: $n=4$: dev $0.118$, dim $44$, tr-ratio $0.9899$; $n=6$: dev
$0.104$, dim $164$, tr-ratio $0.9959$ — all matching verbatim. W1 closed-form self-test
(S/D/Q vs `mpmath.quad`): worst case $3.2 \times 10^{-32}$.

## Certification of the new machinery (validity guards, all passed)

- $n=4$ matched-interval centres and radii from `mpmath.eig` (dps 35) companion
  eigenvalues vs float64: max difference $7.5 \times 10^{-13}$ (guard $6.2\times10^{-7}$);
  all-roots max min-distance $9.5 \times 10^{-13}$.
- Single coherent state ($a=0.9$, $\sigma=0.31$, $\tau=17$): pencil root reproduces the
  closed form $z = \tau + i/(2\sigma)$ to $5.2 \times 10^{-15}$ relative — the certified
  radius of one Gaussian is its exact momentum uncertainty $1/(2\sigma)$.
- Rayleigh consistency $z = \beta + i\sqrt{q - \beta^2}$ ($\beta = u^*Bu$, $q = u^*Qu$),
  3 matched roots per stage $n \le 10$: worst $7.4 \times 10^{-10}$.
- **Final-evaluation truth check (I0.6):** the three sampled $n=4$ eigenvectors were
  reassembled as explicit coherent-state sums and $\lVert(D - \mathrm{Re}\,z)u\rVert$
  integrated on a dense grid, independently of the closed-form matrix elements: max
  relative deviation from $|\mathrm{Im}\,z|$ is $4.2 \times 10^{-10}$ (guard $10^{-6}$).
- Operator inequalities at every stage: $Q - B^2 \succeq 0$ and
  $\mathrm{tr}\,H^2 \le \mathrm{tr}\,P_nD^2P_n$ (ratio $0.9899 \to 0.9995$, matching F07).

## Result

```
E3b — CERTIFIED ENCLOSURES  pencil (P_n D P_n, P_n D^2 P_n)  [W1 family]
  [W1] n= 4  M_n=    31  T_n=    62.00  dim=   44 (dropped   0)  pencil roots=   88  matched(<= 50)= 17 (distinct  14)
       radii: min= 1.3387  median= 1.7411  max= 2.5816   bands [0,15|15,30|30,50] =  1.5774  1.7411  1.8261
  [W1] n= 6  M_n=   127  T_n=   158.75  dim=  164 (dropped   0)  pencil roots=  328  matched(<= 50)= 17 (distinct  14)
       radii: min= 1.3239  median= 1.7241  max= 3.1762   bands [0,15|15,30|30,50] =  1.5764  1.7241  1.7571
  [W1] n= 8  M_n=   511  T_n=   401.60  dim=  538 (dropped   0)  pencil roots= 1076  matched(<= 50)= 17 (distinct  13)
       radii: min= 1.3254  median= 1.7221  max= 3.0787   bands [0,15|15,30|30,50] =  1.5763  1.7221  1.7457
  [W1] n=10  M_n=  2047  T_n=  1012.96  dim= 1626 (dropped   0)  pencil roots= 3252  matched(<= 50)= 17 (distinct  15)
       radii: min= 1.3255  median= 1.7220  max= 3.0722   bands [0,15|15,30|30,50] =  1.5763  1.7220  1.7448
  [W1] n=12  M_n=  8191  T_n=  2553.12  dim= 4876 (dropped   0)  pencil roots= 9752  matched(<= 50)= 17 (distinct  15)
       radii: min= 1.3255  median= 1.7219  max= 3.0716   bands [0,15|15,30|30,50] =  1.5763  1.7219  1.7447

  genealogy of certified intervals on [0, 50] (rows: k-th positive stage eigenvalue; entries: radius |Im z|):
    k    n= 4      n= 6      n= 8      n=10      n=12
    1    1.5774    1.5764    1.5763    1.5763    1.5763
    2    1.4237    1.4230    1.4229    1.4229    1.4229
    3    2.2059    2.1867    2.1847    2.1845    2.1845
    4    2.4162    2.3588    2.3526    2.3521    2.3521
    5    1.7411    1.7241    1.7221    1.7220    1.7219
    6    2.5816    2.4747    2.4638    2.4630    2.4630
    7    1.3933    1.3928    1.3929    1.3929    1.3929
    8    1.3933    1.3928    1.3929    1.3929    1.3929
    9    1.8261    1.7571    1.7457    1.7448    1.7447
   10    2.0258    1.7571    1.7457    1.7448    1.7447
   11    2.0258    1.9563    1.9591    1.9593    1.9594
   12    2.2844    3.1762    3.0787    3.0722    3.0716
   13    2.2844    2.1870    2.1371    2.1328    2.1324
   14    1.5565    1.5029    1.4940    1.4933    1.4932
   15    1.3387    1.5029    1.4940    1.4933    1.4932
   16    1.3387    1.3239    1.3254    1.3255    1.3255
   17    1.3387    1.3239    1.3254    1.3255    1.3255

  certified intervals at n=12 (centre +/- radius; every one intersects spec(D) by theorem — trivially true on this ambient):
    k= 1  s=   9.341   [    8.032,    11.184]   centre=   9.608  radius= 1.5763
    k= 2  s=  11.831   [   10.355,    13.200]   centre=  11.777  radius= 1.4229
    k= 3  s=  14.760   [   12.818,    17.187]   centre=  15.002  radius= 2.1845
    k= 4  s=  18.783   [   16.782,    21.486]   centre=  19.134  radius= 2.3521
    k= 5  s=  21.889   [   20.264,    23.708]   centre=  21.986  radius= 1.7219
    k= 6  s=  24.438   [   22.180,    27.106]   centre=  24.643  radius= 2.4630
    k= 7  s=  27.926   [   27.955,    30.741]   centre=  29.348  radius= 1.3929
    k= 8  s=  29.292   [   27.955,    30.741]   centre=  29.348  radius= 1.3929
    k= 9  s=  32.087   [   30.693,    34.183]   centre=  32.438  radius= 1.7447
    k=10  s=  33.447   [   30.693,    34.183]   centre=  32.438  radius= 1.7447
    k=11  s=  35.697   [   33.377,    37.296]   centre=  35.336  radius= 1.9594
    k=12  s=  38.657   [   36.452,    42.595]   centre=  39.524  radius= 3.0716
    k=13  s=  41.613   [   39.709,    43.974]   centre=  41.841  radius= 2.1324
    k=14  s=  43.992   [   42.819,    45.805]   centre=  44.312  radius= 1.4932
    k=15  s=  45.590   [   42.819,    45.805]   centre=  44.312  radius= 1.4932
    k=16  s=  47.588   [   46.480,    49.131]   centre=  47.805  radius= 1.3255
    k=17  s=  48.567   [   46.480,    49.131]   centre=  47.805  radius= 1.3255

  rho (median radius) sequence over stages (4, 6, 8, 10, 12):  1.7411  1.7241  1.7221  1.7220  1.7219
  successive ratios rho_{k+1}/rho_k:  0.990  0.999  1.000  1.000
  report-only rate fit  rho_n ~ C (log M_n)^(-alpha):  alpha = 0.01

E3b — CONTROLS (must-fail: fixed-basis decoy, constant-radius synthetic; must-pass: shrinking-radius synthetic)
  fixed-basis decoy    rho = 1.7411  1.7411  1.7411  1.7411   -> FAILS [as required]
  constant-radius      rho = 0.8000  0.8000  0.8000  0.8000  0.8000   -> FAILS [as required]
  shrinking-radius     rho = 0.5824  0.4129  0.3207  0.2623  0.2220   -> PASSES (metric is demonstrably passable)

VERDICT (mechanical application of the pre-registered rule)
  harness valid:            True  (must-fail controls fail: True; positive control passes: True)
  E3b radii gate:           PASS (>= 3 consecutive stages with strictly decreasing median radius)
  context: last-three strictly decreasing = True
```

The numbers say: the pencil machinery works and is certified end-to-end, the gate as
pre-registered is met — the median radius decreases strictly at every one of the five
stages — and at the same time the *rate*, which the WP demanded be measured and reported,
is essentially zero: the decrease is front-loaded ($-1.0\%$ from $n=4$ to $6$), collapses
to $\approx 10^{-4}$ per stage by $n = 10$, and the fitted exponent is $\alpha = 0.01$.
The radii are converging to a **positive floor** $\rho_\infty \approx 1.72$ on $[0,50]$
(per-interval floors $1.33$–$3.07$), not to zero. The decreases are genuine, not solver
noise (radii are certified to $\sim 10^{-12}$ at $n=4$ and the companion solves are
backward-stable; the step sizes are $\gtrsim 10^{-4}$).

## The rate (the deliverable's second half): saturation, measured

- **Statistic sensitivity (two-sided disclosure).** The pre-registered median passes (5/5
  stages decreasing); the max also passes (decreasing over the last four); the **min does
  not** (1.3387, 1.3239, 1.3254, 1.3255, 1.3255 — longest decreasing run is 2). Several
  individual genealogy rows ($k = 11, 16, 17$) *increase* by $\sim 10^{-3}$ after $n=6$.
- **Structural fingerprint.** On the window $[0,50]$ the wedge geometry is
  stage-independent from the start: every site with
  $\tau_{\min}(u) \le 50$ (i.e. $u \le 1 + \log\frac{50}{2\pi} \approx 3.07$, prime powers
  $q \le 21.6$) is already present at $n = 4$ ($M_4 = 31$). Stage growth adds only far
  sites and higher-frequency ladder rungs, which couple to the window through rapidly
  decaying Gaussian tails — so the certified resolution converges to the fixed-aperture
  limit of the wedge on that window. This is precisely the obstruction profile the WP's
  falsifier text predicted ("the archimedean window's band-limit dual as the bottleneck")
  — arriving here through a formally passing gate rather than a fired falsifier.
  (Fingerprint explanation: **heuristic**; the floor values at the computed stages:
  **verified**; the $n \to \infty$ limit value: extrapolation, not proven.)
- **Scale comparison (against the family's own derived law — no $\gamma$-list).** The W1
  counting law gives mean eigenvalue spacing $1/R'(T) = 2\pi/\log\frac{T}{2\pi}$, i.e.
  $\approx 7.9$ at $T = 14$ down to $\approx 3.0$ at $T = 50$. The certified half-widths
  ($1.33$–$3.07$, median $1.72$) are *comparable to* the local spacing near the top of the
  window: four adjacent eigenvalue pairs ($k = 7/8$, $9/10$, $14/15$, $16/17$) already
  share a single certified interval at $n = 12$ — the family cannot separate them at
  certified resolution. Superposition beats the best single-Gaussian benchmark
  ($1/(2\sigma_{\max}) = 1.4427$) only at the window top (min radius $1.3255$).
- **Consequence carried forward (binding on WP05's design, informative for WP03).** The
  E4b displacement gate on $[0,50]$ will operate at certified resolution $\approx \pm 1.7$
  that does **not** improve with stage. If E4b needs finer localisation than the wedge
  aperture allows, that is a design fact about the W1 window, not a tuning problem — the
  pre-registered escalation is the genuinely quadratic prolate pencil (Connes–Moscovici
  operator), already named in F02's redesign note and WP02b's falsifier branch.

## Verdict against the pre-registered criteria

**PASS — the E3b radii gate is met** ($\rho_n$ strictly decreasing over all five stages,
$\ge 3$ consecutive as required), with the harness valid two-sidedly. The falsifier
("radii stagnating") did **not** fire by its letter. Consequences, per the charter
ordering and no further:

1. **WP04 is done.** The certified-interval genealogy above is delivered to WP05 (HS7);
   the E-track proceeds **WP03 next, then WP05**, exactly as the F07 ordering update
   scheduled.
2. **The saturation caveat travels with the deliverable.** The measured rate
   ($\alpha \approx 0.01$; floor $\approx 1.72$) and the shared-interval pairs are part of
   the HS7 feed, and WP05's E4b design must state in advance what displacement resolution
   it needs against this floor. A stricter rate-based enclosure gate (e.g. radii $\to 0$,
   or a ratio bound) would be a **new WP with its own pre-registration** — this bar does
   not move post hoc, in either direction.

## Tag

- Enclosure theorem and its pollution-freeness: **proven** (classical, cited).
- Quasi-mode identity $\lVert(D - \mathrm{Re}\,z)u\rVert = |\mathrm{Im}\,z|\,\lVert u\rVert$:
  **proven** (one-line derivation above).
- Pencil instantiation on the W1 family (closed-form $D$/$D^2$ elements, whitening,
  companion solve): **proven** closed forms, **certified** (`mpmath.eig`
  $7.5\times10^{-13}$; independent quadrature $4.2\times10^{-10}$; Rayleigh
  $7.4\times10^{-10}$; single-state $5.2\times10^{-15}$).
- Radii measurements, genealogy, controls, and the PASS verdict: **verified** against the
  pre-registered criteria (deterministic run, regression anchors reproduced first).
- Saturation floor $\rho_\infty \approx 1.72$ as a limit statement: **heuristic**
  (extrapolation from five stages; the stage values themselves are verified).
- Any statement connecting this family to the zeros: **none made** — O6; the interval
  statement about $\mathrm{spec}(D) = \mathbb R$ is trivially true and is not presented as
  spectral discovery.

**Scope (do-not list compliance).** No $\gamma$-list outside the N00 regression line, no
unfolding, no fitted parameter (the rate fit is report-only and appears nowhere in the
gate). Certified enclosures on this ambient are statements about the W1 family's
resolution, not about the zeros. Nothing here bears on the truth of RH, which remains
**open**.

## Propagation

Charter ledger updated: **yes** (T4 row → done, passed with saturation caveat; §4
ordering update appended — WP03 now first in line; §6 ledger row added). WP04 status →
done (passed; caveat recorded). WP03 status note updated (now first in line). README
numerics/findings lists updated. Source doc correction notice needed: **no** (S03 states
E3b as a gate; status lives in the charter ledger per PSC2-001 §1). N00 unchanged
(anchors for future runs live in this note's Result block, per F03–F07 precedent).
