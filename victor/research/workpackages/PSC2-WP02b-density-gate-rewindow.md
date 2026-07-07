# PSC2-WP02b — the density gate rewindowed (E0b): the wedge-windowed compression $H^{G,\mathrm{w}}_n$

*Status: **done — passed** (7 Jul 2026, [PSC2-F07](../findings/PSC2-F07-density-rewindow.md)).
Verdict: **PASS** against the pre-registered criteria below (dev
$0.118 \to 0.104 \to 0.064 \to 0.022 \to 0.020$ over stages $n = 4\ldots12$; harness valid
two-sidedly). Per the pre-registration: the E-track **reopens** (WP03–WP05 unpaused, WP04
first), and — O6, binding — the pass is **not evidence about zeros**; the arithmetic test
of the W1 family is E4b/WP05. This was the redesigned window whose absence kept the E-track
paused since [F02](../findings/PSC2-F02-density-gate.md). Everything below — the builder,
its constants, the gate, the falsifier — was fixed **before the gate run**; the design-stage
derivation checks (ladder-vs-$R$ tracking, convexity) are part of the derivation, not the
gate.*

## Objective

Salvage the primary candidate $H^G_n = P_nDP_n$ by redesigning the **phase-space window**
that defines $V_n$ — not the measurement window, not the metric, not the pass bar, all of
which are inherited from [WP02](PSC2-WP02-density-gate.md) verbatim. F02's proven no-go
lemma killed the entire N0 design class (fixed bases whose cells are frequency intervals
centred on $\tau = 0$: concave counting laws cannot pass E0 on the derived windows). F02's
redesign note prescribes the escape: a family that carries $\frac{T}{2\pi}\log\frac{T}{2\pi}$
intrinsically must have **wedge-shaped phase-space support** — $u$-extent growing like
$\log\frac{|\tau|}{2\pi}$ at height $\tau$ (the Berry–Keating two-cutoff wedge; the
Connes–Moscovici precedent, [S00 §8](../sources/PSC2-S00-verified-foundation.md)) — and the
sieve inventory must enter as **translation lengths** (frequency data), the way $\log q$
actually enters the explicit formula, not as bump positions (the residue of the refuted X1
picture).

## The W1 builder (fixed before any run)

Ambient unchanged (S03 Lemma 1.1): $L^2(\mathbb R, du)$, $D = -i\,d/du$, $J$ = parity,
$JDJ^{-1} = -D$. Stage basis $V_n$, $J$-invariant by construction:

- **Sites.** $u_0 = 0$ (archimedean site) and $u_q = \log q$ for every prime power
  $q = p^k \le M_n = 2^{n+1}-1$ (the sieve inventory).
- **Tiling widths.** $w_i = (u_{i+1} - u_{i-1})/2$ (midpoint tiling of the site axis);
  0-site: mirror neighbour at $-\log 2$, so $w_0 = \log 2$; last site: $w = $ left gap.
  Gaussian width $\sigma_i = w_i/2$. All derived from the inventory, nothing chosen.
- **Wedge ladders (the rewindow).** Site $i$ carries modulated coherent states
  $$\psi_{i,j}(u) = (2\pi\sigma_i^2)^{-1/4}\exp\Big(-\frac{(u-u_i)^2}{4\sigma_i^2}\Big)
  e^{i\tau_j u},\qquad
  \tau_j = \tau_{\min}(u_i) + \big(j+\tfrac12\big)\Delta\tau_i \le T_n,$$
  with $\tau_{\min}(u) = 2\pi e^{u-1}$ (the wedge boundary $|u| = 1 + \log\frac{\tau}{2\pi}$),
  $\Delta\tau_i = 2\pi/w_i$, **except** the self-mirrored 0-site, whose cosine/sine pair
  occupies a single physical cell: $\Delta\tau_0 = 4\pi/w_0$ (Planck-cell counting,
  one-sided).
- **Cap.** $T_n := 2\pi M_n^{2/3}$ — a derived power of the sieve cutoff, fixed here in
  advance; it keeps $\dim V_n$ inside the S03 §4 budget (a few $\times 10^3$ at $n \le 12$)
  and puts the derived window's bottom count $\sqrt{d_n}$ high enough that midpoint-rounding
  noise is not the dominant term. Sites with $\tau_{\min}(u_i) > T_n$ carry no modes
  (the wedge has not reached them).
- **Symmetrisation.** $e_{i,j} = \psi_{i,j} + J\psi_{i,j}$, $o_{i,j} = \psi_{i,j} - J\psi_{i,j}$
  ($J\psi_{a,\sigma,\tau} = \psi_{-a,\sigma,-\tau}$). $JV_n = V_n$ exactly; by F01
  corollary C-c the compression is exactly off-diagonal in the parity grading, so the
  spectrum is $\{\pm s_i\}$ with $s_i$ the singular values of the whitened graded block —
  E1 pairing exact by construction, as in F02's N0 builder.

**Why this is the derived law and not a fit.** One Planck cell of area $2\pi$ per state,
tiled over the wedge $\{(u,\tau): 0 \le u \le 1 + \log\frac{\tau}{2\pi},\ \tau \le T\}$
(one-sided), gives
$$N^{\mathrm{pred}}(T) = \#\{(i,j): \tau_j \le T\} \approx \frac1{2\pi}\int_{2\pi/e}^{T}
\Big(1 + \log\frac{\tau}{2\pi}\Big)d\tau = \frac{T}{2\pi}\log\frac{T}{2\pi} + O(1),$$
which is the WP02 target $R(T)$ **exactly, including the $-T/2\pi$ term** (the $+1$ in the
wedge extent, i.e. the $e^{-1}$ in $\tau_{\min}$, is what cancels it — an analytic
derivation performed once, above, before any run; no coefficient is fitted). The predicted
density $N^{\mathrm{pred}\prime}(T) \approx \frac1{2\pi}\log\frac{T}{2\pi}$ is
**increasing**: the law is convex, structurally outside the class killed by F02's no-go
lemma. The gate run must include a mechanical convexity check of the enumerated ladder.

**Matrix elements.** $\langle\psi_1,\psi_2\rangle$, $\langle\psi_1,D\psi_2\rangle$,
$\langle\psi_1,D^2\psi_2\rangle$ are exact closed forms (complex Gaussian integrals),
evaluated with `mpmath` at dps 35 (float prefilter on the Gaussian exponent as in F02) and
validated against direct `mpmath.quad` quadrature; float64 pipeline certified against
`mpmath.svd_c` on the $n=4$ stage. $D^2$ blocks feed the compression trace inequality and
are the WP04 pencil input, as in F02.

## Pre-registered criteria (inherited from WP02 verbatim; the bar does not move)

- Counting $N^+(T) := \#\{\lambda \in \mathrm{spec}: 0 < \lambda \le T\}$; target
  $R(T) := \frac{T}{2\pi}\log\frac{T}{2\pi}$; derived window $W_n = [T_{\mathrm{lo}}, T_n^{\mathrm{win}}]$
  with $R(T_{\mathrm{lo}}) = \sqrt{d_n}$, $R(T_n^{\mathrm{win}}) = d_n$,
  $d_n = \#\{\text{positive eigenvalues}\}$; $\mathrm{dev}_n = \max_{W_n}|N^+/R - 1|$ on a
  200-point geometric grid.
- **PASS** iff $\mathrm{dev}$ strictly decreasing over the last three stages **and** final
  $\mathrm{dev} \le 0.05$. Stages: $n = 4, 6, 8, 10, 12$.
- **Must-fail controls** (identical code path to F02): legacy $H_n'$; graph one-mode;
  sine decoy. **Positive control** (smooth-law sample) must pass, else the run is invalid.
- Non-vacuity guards; full Gram-rank reporting; compression trace inequality
  $\mathrm{tr}(H^{G,\mathrm{w}}_n)^2 \le \mathrm{tr}(P_nD^2P_n)$ at every stage; N00
  regression anchors reproduced first (I0.5). No $\gamma$-list, no unfolding, no fitted
  parameter (I0.1/I0.6).

**O6 discipline (binding, stated in advance).** A wedge-shaped basis passes E0 *regardless
of arithmetic content* — this gate can certify only that the redesign repaired the killed
component. **A PASS is not evidence about zeros**; it reopens the E-track (WP03–WP05
unpause, WP04 first per the F02 ordering note) and nothing more. The arithmetic content of
the E-track lives entirely in E4b and the WP05 decoy battery.

## Falsifier (pre-registered; binding)

- **FAIL, spectrum tracks ladder** (measured $\max_{W_n}|N^+ - N^{\mathrm{pred}}|/d_n \le 0.05$
  but the gate bar is missed): the obstruction is prime-gap discreteness of the inventory at
  the window bottom, not phase-space shape. Record as its own branch; the E-track stays
  paused; **the bar does not move post hoc** — any revised gate is a new WP with its own
  pre-registration.
- **FAIL, spectrum does not track ladder**: the fixed-coherent-state realisation of the
  wedge is dead too (broadening/Gram effects destroy the law); the redesign must go to the
  genuinely quadratic prolate pencil (Connes–Moscovici operator; WP04's $(D, D^2)$
  machinery). Record and stop.
- Any must-fail control passing, or the positive control failing, invalidates the run
  (harness artifact, not a finding about the family).

## Deliverable

W1 builder code under `numerics/` (`wp02b_rewindow.py`); finding note
(`PSC2-F07-density-rewindow.md`) with the enumerated parameter-free law, the convexity
check, and the pass/fail verdict published verbatim against the criteria above. Tag target:
**proven** (a computation about an explicit finite family) + **verified** (gate verdict).

## Inputs

[F02](../findings/PSC2-F02-density-gate.md) (kill + no-go lemma + redesign note);
[S03](../sources/PSC2-S03-eigenvalue-level.md) §3(c)–§4; [S00 §8](../sources/PSC2-S00-verified-foundation.md)
(Connes–Moscovici precedent); `e0_density_gate.py` (gate harness, reused verbatim).
