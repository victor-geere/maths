# PSC2-F10 — the evaluation harness delivered and valid (E4c/HS6), and E4a: the trace gate fails by persistent excess — the pollution mass is exactly the sub-$\gamma_1$ counting surplus

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP05](../workpackages/PSC2-WP05-evaluation-harness.md). Code/run:
`numerics/wp05_evaluation_harness.py` (deterministic; the matching validator is seeded
20260707; `mpmath` dps 35; stages $n = 4, 6, 8, 10, 12$; stage matrices are the W1 closed
forms of `wp02b_rewindow.py` through the F08 pencil code path of
`wp04_certified_enclosures.py`; E4a targets through `adele_trace.py`). This is the
**harness note** for the WP05 run: the E4c/HS6 control battery, the run-validity record,
and component E4a live here; components E4b, HS1, HS2, HS7 have their own notes
([F11](PSC2-F11-e4b-matched-displacement.md), [F12](PSC2-F12-hs1-product-gate.md),
[F13](PSC2-F13-hs2-moment-gate.md), [F14](PSC2-F14-hs7-genealogy.md)) quoting the same
run. Tags per [PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> - **E4a — trace consistency (strongest test).** $\sum_{\lambda} g_t(\lambda)$ over
>   $\mathrm{spec}(H^G_n)$ must converge, within the proven $O(M_n^{-1/2})$ envelope
>   ([S00](../sources/PSC2-S00-verified-foundation.md) §5–6), to the place-by-place values of
>   [N00 §1](../numerics/PSC2-N00-verification-targets.md). Persistent excess = quantified
>   pollution mass; deficit = quantified spectral loss. Consumes no new target data.
> - **E4c/HS6 — controls.** *Positive:* harmonic oscillator compression. *Decoys:* bare
>   prolate/xp compression (must pass E0's shape, must fail E4b) **and the sine model with
>   spectrum $\mathbb Z_{>0}$** (must pass every internal-consistency step, must fail every
>   arithmetic test by the density-class gap — [S04 §5](../sources/PSC2-S04-model-pair.md)).
>   *Negatives:* legacy $H_n'$, graph one-mode. A harness on which any decoy scores
>   "arithmetic" is invalid.
> - E4a residual within $C\,M_n^{-1/2}$, $C$ derived from S00 §5 Prop 6.1; […] every
>   control behaves per its must-pass/must-fail line above.

Operationalisation, fixed in the script header before the run (the bar itself is the
WP's, unmoved): Gaussian test pair $h_t(r) = e^{-tr^2}$,
$g_t(x) = e^{-x^2/4t}/(2\sqrt{\pi t})$ at $t \in \{0.05, 0.2\}$ (the two N00 §1 balance
instances); stage trace $= \sum_{\pm s_i} h_t(\pm s_i) + \ker\cdot h_t(0)$ over the full
spectrum; target $Z(t) := W_\infty(g_t) - \sum_p W_p(g_t)$ computed place-by-place
($\gamma$-free) and asserted against the N00 §1 literals in regression; envelope constant
derived from S00 §5 Prop 6.1 at $\varepsilon = \tfrac12$:
$$|g_t(x)| \le 2g_t(\log 2)\,e^{-x}\ (x \ge \log 2)
\;\Rightarrow\;
\Big|\sum_{q > M_n}\tfrac{\Lambda(q)}{\sqrt q}\big(g_t(\log q)+g_t(-\log q)\big)\Big|
\le \underbrace{12\,c_{\mathrm{RS}}\,g_t(\log 2)}_{C(t)}\,M_n^{-1/2},$$
$c_{\mathrm{RS}} = 1.03883$ (Rosser–Schoenfeld, $\psi(x) < 1.03883\,x$ for $x > 0$), so
$C(0.05) = 1.4235$, $C(0.2) = 4.3131$. PASS iff $|T_n(t) - Z(t)| \le C(t)M_n^{-1/2}$ at
every computed stage for both $t$. The three calculus/algebra facts in the derivation
(the maximiser $x^* = 2t$ of $g_t(x)e^x$ with monotone decay beyond it; the Stieltjes
bound $\tfrac32\int_M^\infty c\,t^{-3/2}dt = 3cM^{-1/2}$; the Gaussian second-moment
identity used by the h.o. control) were cross-checked symbolically via the
`sympy-verifier` MCP server before the run, as was the sine control's exact product
closed form (below) and the counting identity $R(50) - \big(\tfrac{50}{2\pi}(\log\tfrac{50}{2\pi}-1)+\tfrac78\big) = 7.0827$.

**Design-time disclosure (verbatim summary of the script header).** Control designs
(h.o. lattice, decoy site rule), target computations, and the matching validator were
calibrated in a controls-only dry run; no W1 stage was built before the first header
freeze — primary-side expectations were derived from F08's *published* table only. A code
smoke test at stages $(4, 6)$ then exposed three **control** defects, fixed with
bar-hardening changes only (the exact $\Gamma$ product closed form for the sine identity —
the dry-run guard had been vacuous, its coarse subgrid hitting only integer $t$ where both
sides vanish; the absolute half-spacing term in E4b's CERTIFIED rule, without which the
legacy/graph negatives pass by slow drift from absurd levels; stage-matched sine
candidates). Each change adds a conjunct against the primary or corrects a control-side
reference; none can flip a primary FAIL to PASS. Primary values seen during the smoke
test are quoted in the header for the record.

**Run-validity record (two runs; the control artifact disclosed).** The first full run
(log archived) was **invalidated by its own control line**: the bare-wedge decoy as first
designed re-spaced its uniform site grid at every stage, so its low-energy spectrum
re-arranged ($N^+(50) = 17, 17, 16, 14, 3$ across stages) and its E0-shape sequence
(`0.157 0.094 0.072 0.076 0.223`) failed the must-pass line — a harness artifact, not a
finding, per the pre-registered rule. The decoy was redesigned to a **nested** pinned
grid (spacing $\delta_0 = \log(M_4)/|Q_4| = 0.20200$ fixed once, sites only ever added —
mirroring the nestedness of the sieve inventory, which is the correct
"same-in-everything-but-arithmetic" control), and the run repeated. The W1 primary
numbers are identical between the two runs (deterministic code path; verified digit-level
on the E4a/HS2/HS1 tables). Everything below quotes the second (valid) run.

## Regression check

N00 targets reproduced: **yes** — §4 spot-values ($\gamma_1, \gamma_2, \gamma_{10}$,
$\sin(\pi\gamma_1)$, $\sin(\pi\gamma_1)/(\pi\gamma_1)$; consumed only in the regression
lines and in E4b's final evaluation, per I0.6); §2 legacy
$\lVert A'\rVert_{\mathrm{op}} = 9.27, 19.5, 36.3$ **and** the legacy trace anchor
$\mathrm{Tr}\,g_{0.2}(H_8') = 16.7494$ [N00: 16.7]; §3 graph stage $\mu_1 = 3.5419$,
#detached $= 4$, #detached-real $= 2$; **§1 adelic anchors through `adele_trace.py`**:
$W_\infty = 0.60303464961426464498$, $W_2 = 0.38013321408074931683$,
$\sum_p = 0.60303464960929003883$ ($t = 0.2$, $p \le 97$), balance
rhs/zero-side/discrepancy at $t = 0.05$ ($7.88\times10^{-37}$) and $t = 0.2$
($4.49\times10^{-37}$), truncation row $n = 8$ ($0.088009003$, $1.9894707$) — all
verbatim. F07 E0b anchors ($n = 4, 6$) and F08 pencil anchors ($n = 4$: min radius
$1.3387$, median $1.7411$; coherence $r_4(\mathrm{Re}\,z) - |\mathrm{Im}\,z| \le
-7.8\times10^{-2}$) reproduced through their own code paths. W1 closed-form self-test
worst case $3.2\times10^{-32}$; new $\langle u^2\rangle$ closed form vs quadrature
$7.5\times10^{-37}$; matching DP $=$ brute force on 60 seeded instances.

## The control battery (E4c/HS6) — every line behaved; the harness is valid

```
E4c CONTROL (positive) — harmonic oscillator compression on nested lattices
    R=2.4  dim=  9 (kept   9)  median disp to (j+1/2) = 1.51e-03   |trace res| = 2.34e-02
    R=3.2  dim= 13 (kept  13)  median disp to (j+1/2) = 8.48e-05   |trace res| = 2.12e-03
    R=4.0  dim= 21 (kept  21)  median disp to (j+1/2) = 4.76e-08   |trace res| = 2.11e-06
    R=4.8  dim= 29 (kept  28)  median disp to (j+1/2) = 3.97e-10   |trace res| = 2.72e-08
    R=5.6  dim= 37 (kept  34)  median disp to (j+1/2) = 6.06e-11   |trace res| = 1.57e-09
  h.o. positive control: PASSES (both metrics demonstrably passable)  (displacement: True, trace: True)
HS6 CONTROL (sine decoy) — internal consistency (must-pass), gamma-free part
  product identity vs Gamma closed form (mp, non-integer subgrid): max = 8.44e-33  [guard 1e-25]  -> OK
  internal moments |sum k^-2 - zeta(2)| over d = 609, 1219, 2438: 1.64e-03  8.20e-04  4.10e-04  |err*d - 1| = 2.05e-04  -> OK (decreasing, tail scale exact to 1%)
  vs arithmetic sigma(2m): off by >= 10x at every m: YES [as required]
  sine E4a t=0.05: residual = +6.9266e+00 vs envelope 1.5728e-02 -> outside [as required]
  sine E4a t=0.2: residual = +2.9633e+00 vs envelope 4.7656e-02 -> outside [as required]
  legacy E4a outside envelope at every stage/t: YES [as required]
  graph E4a outside envelope at every stage/t: YES [as required]
  decoy E0 shape: dev sequence = 0.157  0.171  0.068  0.033  0.024  -> PASSES E0 shape [as required]
VERDICT (excerpt)
  harness valid:            True
    positive h.o. control passes:        True
    sine internal passes / arith fails:  True / True
    legacy fails / graph fails:          True / True
    decoy passes E0 shape / fails E4b:   True / True
```

The positive control demonstrates the metrics reward genuine convergence at depth (median
displacement $1.5\times10^{-3} \to 6\times10^{-11}$; a compression family of nested spaces
converges monotonically by min–max). The sine decoy passes both internal-consistency
steps — its finite product matches the exact closed form
$\prod_{k\le d}(1 - t^2/k^2) = \mathrm{sinc}(\pi t)\,\Gamma(d{+}1{-}t)\Gamma(d{+}1{+}t)/\Gamma(d{+}1)^2$
to $8.4\times10^{-33}$, and its internal moments hit $\zeta(2)$ at the exact tail scale —
and **fails every arithmetic test by the density-class gap**, as S04 §5 demands. The
nested bare-wedge decoy passes E0's shape (its counting law is the same derived wedge
law) and fails E4b ([F11](PSC2-F11-e4b-matched-displacement.md)). The two negatives fail
everything. The harness is **valid, two-sidedly**. (HS3 stays backlog per the WP; its
schedule remains to be fixed before any target comparison.)

## Result (E4a, primary)

```
E4a — TRACE CONSISTENCY  Tr h_t(H_n) vs Z(t) = W_inf - sum_p W_p  [W1]
  t = 0.05   Z(t) = (9.17567009714715e-5 + 0.0j)   C(t) = 1.4235
      n     M_n      trace T_n      residual   envelope  res*sqrt(M)  within
      4      31     0.02722745    2.7136e-02 2.5566e-01       0.1511  YES
      6     127     0.02734154    2.7250e-02 1.2631e-01       0.3071  YES
      8     511     0.02735183    2.7260e-02 6.2970e-02       0.6162  YES
     10    2047     0.02735244    2.7261e-02 3.1462e-02       1.2334  YES
     12    8191     0.02735248    2.7261e-02 1.5728e-02       2.4672  NO
      band (0,15] share of trace at n=12: 2.735244e-02  (100.0%)
      band (15,30] share of trace at n=12: 4.375156e-08  (0.0%)
      band (30,50] share of trace at n=12: 8.881479e-23  (0.0%)
  t = 0.2   Z(t) = (8.86036436044729e-18 + 0.0j)   C(t) = 4.3130
      n     M_n      trace T_n      residual   envelope  res*sqrt(M)  within
      4      31     0.00000005    5.1834e-08 7.7464e-01       0.0000  YES
      6     127     0.00000005    5.2680e-08 3.8272e-01       0.0000  YES
      8     511     0.00000005    5.2757e-08 1.9080e-01       0.0000  YES
     10    2047     0.00000005    5.2761e-08 9.5329e-02       0.0000  YES
     12    8191     0.00000005    5.2762e-08 4.7656e-02       0.0000  YES
  E4a [W1]: FAIL — persistent EXCESS (quantified pollution mass)
    failing stages: (t=0.05, n=12, res=+2.7261e-02)
```

The numbers say: the stage trace **converges** — but to the wrong value. The residual at
$t = 0.05$ is positive at every stage and *stage-stable to five digits*
($0.027136 \to 0.027261$, converging upward), while the proven truncation envelope
shrinks as $M_n^{-1/2}$ and crosses it between $n = 10$ and $n = 12$; the scaled residual
$\rho_n\sqrt{M_n}$ grows $0.15 \to 2.47$ with no ceiling. A family whose only error were
sieve truncation would sit *inside* the envelope at every stage; this one carries a fixed
excess mass. Where the mass sits is measured, not guessed: 100.0% of the $t = 0.05$
trace lives in the band $(0, 15]$, and the final-evaluation inventory
([F11](PSC2-F11-e4b-matched-displacement.md)) attributes 100.2% of the excess to the two
stage eigenvalues **below $\gamma_1$** ($9.341$ and $11.831$ — inside the F09 resolved
band $[9.34, 50]$ but below the first zero ordinate $14.13$). At $t = 0.2$ the Gaussian
kills the low band and the gate passes trivially at every stage — the excess is a
low-energy phenomenon, exactly where the W1 counting law
$R(T) = \tfrac{T}{2\pi}\log\tfrac{T}{2\pi}$ exceeds the true zero count
$N(T) = \tfrac{T}{2\pi}(\log\tfrac{T}{2\pi} - 1) + \tfrac78 + S(T)$ by the linear term
$\tfrac{T}{2\pi}$ ($= 7.08$ at $T = 50$, symbolically checked; the family carries 17
eigenvalues on $(0, 50]$ where 10 ordinates live). The bare-wedge decoy fails E4a the
same way (excess $+1.65\times10^{-2}$, 100% in $(0,15]$) — the excess is a property of
the **wedge counting law**, not of the sieve inventory; the arithmetic placement neither
creates nor removes it.

## Verdict against the pre-registered criteria

**E4a: FAIL — the persistent-excess branch** ("persistent excess = quantified pollution
mass", the WP's own line): excess $+2.726\times10^{-2}$ in trace units at $t = 0.05$,
stage-stable, localised in $(0, 15]$, equal to the sub-$\gamma_1$ eigenvalue mass to
0.2%. The harness is valid (all controls behaved), so the verdict stands as a finding
about the W1 family, and it feeds the family-level decision of
[F11](PSC2-F11-e4b-matched-displacement.md).

## Tag

- Envelope-constant derivation ($C(t) = 12\,c_{\mathrm{RS}}\,g_t(\log 2)$ from S00 §5
  Prop 6.1 with $\varepsilon = \tfrac12$): **proven** (elementary; calculus steps
  cross-checked via the sympy-verifier; $c_{\mathrm{RS}}$ classical, cited).
- Sine-control product closed form: **proven** (classical Gamma reflection/recursion;
  cross-checked symbolically and to $8.4\times10^{-33}$ numerically).
- E4a measurements, control battery, and the FAIL/excess verdict: **verified** against
  the pre-registered criteria (deterministic run; regression anchors reproduced first;
  run-1 control artifact disclosed above).
- The reading "the excess is the wedge's counting surplus below $\gamma_1$": the counting
  arithmetic is **proven** (classical $N(T)$ vs the F07-derived $R(T)$); the
  identification of the measured excess with that surplus is **verified** at the computed
  stages (100.2% attribution; decoy comparison), not proven as an $n \to \infty$ limit.
- Any statement connecting this to zeros: **none made** (O6) — a trace-gate failure is a
  statement about this window design.

**Scope (do-not list compliance).** No $\gamma$-list outside the N00 regression lines and
E4b's final evaluation (I0.6); no unfolding; no fitted parameter (the envelope constant is
derived, not fitted). E4a consumed no new target data — its target is the N00 §1
arithmetic side. Nothing here bears on the truth of RH, which remains **open**.

## Propagation

Charter ledger updated: **yes** (T5 row → done; §4 ordering update appended; §6 ledger
rows added). WP05 status → done (this note + F11–F14). WP15 chartered (the pre-registered
escalation). README numerics/findings lists updated. Source doc correction notice
needed: **no** (S03/S04 state the gates; run-time status lives in the charter ledger per
PSC2-001 §1). N00 unchanged (anchors for future runs live in this note's Result block,
per F03–F09 precedent).
