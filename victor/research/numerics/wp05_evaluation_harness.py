"""wp05_evaluation_harness.py — PSC2-WP05 (E4 + HS gates): the evaluation harness on
the W1 family — trace consistency (E4a), matched displacement (E4b, final evaluation),
paired-product gate (HS1), moment gate (HS2), enclosure genealogy (HS7), and the full
control battery (E4c/HS6).

THE OBJECT.  The W1 wedge family H^{G,w}_n = P_n D P_n of PSC2-WP02b/F07 on the fixed
ambient L^2(R, du), D = -i d/du (E2a record, F09), with spectra {+/- s_i} exact (F01/F07)
and the F08 pencil (P_n D P_n, P_n D^2 P_n) for the certified intervals.  This WP is
where the family's arithmetic content is DECIDED (O6): E0b certified only the counting
law; whether the sieve inventory's placement of the wedge ladders carries arithmetic
beyond that law is exactly what E4a/E4b + the decoy battery test.

BINDING RESOLUTION BUDGET (stated in advance, F08 + F09; fixed before any run):
  (a) certified-enclosure radii on [0, 50] floor at ~1.72 and do not improve with stage
      (F08 genealogy; published);
  (b) certified quasi-mode floor r_n(lambda) >= 0.73 on [0, 50] at every computed stage
      (F09; grid minima ~0.98) — no trial vector in V_n localises better;
  (c) permanent spectral hole (-9.34, 9.34): no stage eigenvalue below ~9.34; published
      stage mobility (index-matched max shift n=10 -> 12) is 9.2e-4.
  PRICING (mechanical consequences, fixed now):
  * The E4b statistic on [0, 50] starts (predicted from F08's PUBLISHED n=12 table
    against the 10 ordinates <= 50) at median ~0.68 — BELOW floor (b).  The entire
    dynamic range of the E4b statistic on this window is therefore sub-resolution:
    no displacement improvement smaller than RES_FLOOR = 0.73 can be certified as
    genuine localisation (it is not resolvable against the family's own certified
    energy fuzziness).  The budget is hence UNMEETABLE as a certified-localisation
    claim on [0, 50] unless the run measures actual cumulative improvement >= 0.73
    (which would falsify the frozen-spectrum picture).  Per the pre-registered
    escalation (F02 redesign note / WP02b falsifier branch / F08 / F09): if E4b does
    not certify, the E-track candidate moves to the prolate pencil (new WP).
  * Handling of the hole (c): all zero ordinates <= 50 lie above the hole edge
    (gamma_1 = 14.13... > 9.34, N00 §4), so the hole blocks no match on this window;
    stage eigenvalues in the band [9.34, 14.13) are surplus and are reported in the
    final-evaluation pollution inventory.

COMPONENTS AND PRE-REGISTERED CRITERIA (the WP's own lines, operationalised; the bar
does not move):
  WP: "E4a residual within C M_n^{-1/2}, C derived from S00 §5 Prop 6.1; E4b and HS2
  monotone over >= 3 stages; HS1 divergence-while-E4a-passes is the quantified-pollution
  branch, reported as such; every control behaves per its must-pass/must-fail line."

  E4a (trace consistency; gamma-free).  Gaussian pair h_t(r) = e^{-t r^2},
    g_t(x) = e^{-x^2/4t} / (2 sqrt(pi t)), t in {0.05, 0.2} (the two N00 §1 balance
    instances).  Stage trace T_n(t) := sum over the FULL stage spectrum {+/- s_i} of
    h_t (+ ker * h_t(0), ker reported; F07: ker = 0).  Target (gamma-free, consumes no
    new data): Z(t) := W_inf(g_t) - sum_p W_p(g_t) computed place-by-place by
    adele_trace.py (p <= 16383) and asserted against the N00 §1 literals in regression.
    Envelope derived from S00 §5 Prop 6.1 (eps = 1/2): for x >= log 2,
    g_t(x) e^x is decreasing (maximiser x* = 2t < log 2 for t <= 0.34), so
    |g_t(x)| <= 2 g_t(log 2) e^{-x}; two-sided arithmetic tail
    <= 2 * [2 g_t(log 2)] * c_RS * 3 * M_n^{-1/2} =: C(t) M_n^{-1/2},
    C(t) = 12 * 1.03883 * g_t(log 2)  (psi(x) < 1.03883 x, Rosser-Schoenfeld 1962).
    => C(0.05) = 1.4235, C(0.2) = 4.3131.
    PASS iff |T_n(t) - Z(t)| <= C(t) M_n^{-1/2} at EVERY computed stage for BOTH t.
    Branch on failure: persistent excess (residual > 0 at every failing stage)
    = quantified pollution mass; persistent deficit = quantified spectral loss;
    per-band shares of the residual reported ([0,15|15,30|30,50], F08 bands).
  E4b (matched displacement; FINAL EVALUATION ONLY, I0.6 — the gamma-list appears in
    this component and nowhere else outside the regression lines).  Targets: the zero
    ordinates gamma_k <= 50 (mpmath.zetazero; 10 of them).  Candidates: stage
    eigenvalues in (0, 50].  Matching: monotone (order-preserving) min-total-|.|
    assignment of every target to a distinct candidate — L1-optimal for sorted
    sequences; validated in-run against brute force on 60 random small instances
    (seed 20260707, deterministic).  Statistic: med_n := median matched displacement.
    RULES (fixed now):
      LETTER  (the WP's line): med_n strictly decreasing over >= 3 consecutive stages.
      CERTIFIED (budget-priced): LETTER and cumulative decrease over the decreasing
        run >= RES_FLOOR = 0.73 (floor (b): smaller improvements are sub-resolution)
        and final med <= half the mean target spacing on the window (target-derived,
        ~1.98: a "localisation" claim must at least reach sub-spacing scale — the
        absolute term that makes slowly-drifting far-off spectra fail, see the
        legacy/graph controls).
      BEATS-DECOY: med(decoy) - med(W1) >= RES_FLOOR at each of the last 3 computed
        stages (density-matched comparison; see decoy below).
      COUNTING-LAW-ONLY branch (the WP's closure line) iff NOT CERTIFIED and NOT
        BEATS-DECOY.
    Density hygiene (from the design dry-run, disclosed): absolute displacement levels
    are NOT comparable across density classes — an overdense spectrum wins matching
    trivially (the sine decoy's integers, 50 candidates on (0,50] vs 10 targets, sits
    near median ~0.13 by density alone).  Absolute levels are reported with the
    in-window candidate count as density witness; verdicts use only the
    improvement-based rules above and the density-matched decoy.
  HS1 (paired-product gate; gamma-free).  Xi_n(t) = Xi(0) prod_{s_i > 0}(1 - t^2/s_i^2)
    over the FULL positive spectrum vs Xi(t) = xi(1/2 + it) computed independently via
    mpmath (dps 35; no zero list), xi(s) = s(s-1)/2 pi^{-s/2} Gamma(s/2) zeta(s).
    Grid t = 0 (0.25) 30 (the falsifier's window).  Metric M1_n := median over the grid
    of |log(|Xi_n(t)| / |Xi(t)|)| (finite-value points; exclusions counted), with
    per-band medians [0,10|10,20|20,30].  CONVERGENT iff M1_n strictly decreasing over
    >= 3 consecutive stages AND final <= log 1.5; else DIVERGENT, classified jointly
    with E4a per the WP (divergence-while-E4a-passes = quantified determinant-level
    pollution; divergence-with-E4a-excess = consistent L3/L4 pollution).
  HS2 (moment gate; gamma-free).  sigma_n(2m) := sum_{s_i > 0} s_i^{-2m} vs
    sigma(2m) := -m [t^{2m}] log(Xi(t)/Xi(0)) computed from the Taylor expansion of xi
    at s = 1/2 via mpmath (S04 §3; no zero list), m in {1, 2, 3}.
    PASS iff |sigma_n(2m) - sigma(2m)| strictly decreasing over >= 3 consecutive
    stages for EVERY m.  (Design-time identity check: the Taylor targets reproduce
    log(Xi(t)/Xi(0)) at t = 0.5 to 6e-16.)
  HS7 (enclosure genealogy; gamma-free).  Certified intervals per stage from the F08
    pencil code path (wp04, unchanged).  Link rule between consecutive stages, per
    aligned index k: intervals overlap AND |centre shift| <= (r_k,n + r_k,n+1)/2.
    Report: unbroken chains across all computed stages, breaks (localise pollution),
    per-chain total centre drift, shared-interval multiplicities.  Report-only (no
    pass bar in the WP); guard: F08 n=4 anchors (min radius 1.3387, median 1.7411,
    tol 5e-4) and the r/radius coherence check reproduced first.
  E4c/HS6 (controls; identical code paths — any control misbehaving = RUN INVALID):
    POSITIVE (harmonic oscillator compression): H_ho = (D^2 + u^2)/2 compressed on
      nested phase-space lattices of coherent states (sigma = 2^{-1/2}, lattice step
      delta = 1.6, disk radii R = 2.4, 3.2, 4.0, 4.8, 5.6), spectrum {j + 1/2} known
      (gamma-free targets).  Must-pass: median |low-8 eigenvalue - (j+1/2)| (same
      matching code) strictly decreasing over >= 3 consecutive stages AND final
      <= 0.01; trace-analog residual |Tr h_.05 - sum_j h_.05(j+1/2)| likewise
      (final <= 0.01).  [Min-max: nested spaces => monotone convergence from above.]
    DECOY (bare wedge, the WP's "bare prolate/xp compression"): same builder code
      path as W1 with the sieve inventory REPLACED by a uniform site grid — K = |Q_n|+1
      sites equally spaced on [0, log M_n], same derived widths (midpoint rule), same
      wedge boundary tau_min(u) = 2pi e^{u-1}, same ladder spacings 2pi/w (4pi/w_0 at
      the self-mirrored 0-site), same cap T_n = 2pi M_n^{2/3} — wedge phase-space
      support with NO arithmetic inventory.  Must-pass E0's shape (e0_density_gate
      metric, F07 rule verbatim: last-3 dev strictly decreasing AND final <= 0.05);
      must-fail E4b (NOT CERTIFIED under the rules above).  W1 must beat it
      (BEATS-DECOY) or the family closes as counting-law-only.
    SINE (HS6, S04 §5): spectrum Z_{>0}, stage-matched (E4b candidates {1..d_n} per
      W1 stage; internal checks at d_ref = #positive W1 eigenvalues at the last
      computed stage).  Must-pass internal consistency: (i) exact product identity
      prod_{k<=d}(1 - t^2/k^2) = sinc(pi t) Gamma(d+1-t) Gamma(d+1+t) / Gamma(d+1)^2
      (cross-checked via the sympy-verifier at d = 3), mp arithmetic on the
      non-integer subgrid, guard 1e-25; (ii) internal moments
      |sum_{k<=d} k^{-2} - zeta(2)| decreasing over d_ref/4, d_ref/2, d_ref with the
      exact tail scale |err * d - 1| <= 0.01.  Must-fail every arithmetic test:
      E4a residual outside the last-stage envelope for both t; E4b NOT CERTIFIED;
      HS2 off by factor >= 10 at every m (the density-class gap).
    NEGATIVES: legacy H_n' (S00 §2.3 via sieve_operator.build_Hn_repaired, n = 8, 10,
      12; regression anchor Tr g_.2(H_8') = 16.7, N00 §2) and graph one-mode (singular
      values of the weighted divisor stage, n = 6, 8, 9) — must fail E4a (outside
      envelope at every stage) and E4b (NOT CERTIFIED).
  BACKLOG (not run, recorded): HS3 Sylvester-denominator schedule — stays backlog per
    the WP; schedule must be fixed before any target comparison.

  Stages n = 4, 6, 8, 10, 12 (the E0b stages).  'fast' drops n = 12 (F08/F09
  precedent: criteria apply to the computed stages unchanged).  Overall W1 verdict
  (mechanical): ARITHMETIC iff E4a PASS and E4b CERTIFIED and HS2 PASS;
  COUNTING-LAW-ONLY iff the E4b closure branch fires; else MIXED (report as measured).
  O6 binds throughout: no outcome here is evidence about zeros; RH is open.

REGRESSION (I0.5) before any new number counts: w1.selftest(); e0.regression()
  (gamma-list allowed ONLY there and in E4b's final evaluation); wp04.w1_regression()
  (F07 anchors); F08 pencil anchors at n=4 + r/radius coherence (wp03 block); N00 §1
  adelic anchors (W_inf, W_2, sum_p at t=0.2; balance rhs/zero-side/discrepancy at
  t = 0.05, 0.2; truncation-rate row n=8) through adele_trace.py; N00 §2 legacy trace
  anchor 16.7; <u^2> closed form vs quadrature (guard 1e-25); matching DP vs brute
  force (60 instances).

DESIGN-TIME DISCLOSURE.  Control designs (h.o. lattice, decoy site rule), target
  computations (Z(t), sigma(2m), envelope constants) and the matching validator were
  calibrated in a controls-only dry run; no W1 stage was built before the first
  header freeze — all primary-side expectations above derive from F08's published
  table only.  A code smoke test at stages (4, 6) then exposed three CONTROL defects
  (a vacuous sine product-identity guard — the dry-run subgrid hit only integer t,
  where both sides vanish identically; legacy/graph negatives passing the certified
  rule by slow drift from absurd levels; a scale-fragile sine staging), fixed as:
  the exact Gamma closed form, the absolute half-spacing term in CERTIFIED, and
  stage-matched sine candidates.  Each fix strengthens or leaves unchanged the
  primary's bar (the CERTIFIED rule gained a conjunct — it can only flip a primary
  PASS to FAIL, never the reverse).  Primary values seen during that smoke test, and
  quoted here for the record: E4b medians 0.8076 (n=4), 0.7456 (n=6); E4a within
  envelope at n = 4, 6; HS1 M1 ~ 1.34-1.45; HS2 errors of order 1e-2 — all consistent
  with the F08-published-table predictions above and consumed by no rule.

Deterministic (matching validator seeded 20260707; everything else seed-free).
Run:  python -u wp05_evaluation_harness.py  [fast]
"""

import sys
import time
from math import pi, log, exp, sqrt
from itertools import combinations

import numpy as np
import mpmath as mp

import e0_density_gate as e0            # N00 regression harness (I0.5); sets dps 35
import wp02b_rewindow as w1             # W1 builder: closed forms, blocks, self-test
import wp04_certified_enclosures as wp04  # aligned stage build + whitened pencil
import adele_trace as at                # N00 §1 adelic anchors + E4a target
import sieve_operator as so             # legacy comparator (N00 §2)
import prime_graph_lab as pgl           # graph one-mode control (N00 §3)

mp.mp.dps = 35

WINDOW = 50.0
BANDS = (0.0, 15.0, 30.0, 50.0)
STAGES_FULL = (4, 6, 8, 10, 12)
STAGES_FAST = (4, 6, 8, 10)
E4A_T = (0.05, 0.2)
C_RS = 1.03883                          # Rosser-Schoenfeld: psi(x) < 1.03883 x, x > 0
RES_FLOOR = 0.73                        # F09 certified quasi-mode floor on [0, 50]
HS1_GRID = np.arange(0.0, 30.0 + 1e-9, 0.25)
HS1_BAR = float(np.log(1.5))
HS2_M = (1, 2, 3)
HO_STAGES = (2.4, 3.2, 4.0, 4.8, 5.6)   # h.o. lattice disk radii
HO_DELTA, HO_SG = 1.6, 1.0 / sqrt(2.0)
DECOY_E0_BAR = 0.05


# ----------------------------------------------------------------------
# 1. shared utilities
# ----------------------------------------------------------------------
def h_t(lam, t):
    return np.exp(-t * np.asarray(lam, dtype=float) ** 2)


def g_t(x, t):
    return exp(-x * x / (4.0 * t)) / (2.0 * sqrt(pi * t))


def envelope_C(t):
    """C(t) = 12 c_RS g_t(log 2) — derivation in the header (Prop 6.1, eps = 1/2)."""
    return 12.0 * C_RS * g_t(log(2.0), t)


def match_dp(lams, gams):
    """Monotone min-total-|.| assignment of each target (gams, sorted) to a distinct
    candidate (lams, sorted); L1-optimal.  Returns (total, matched displacements)."""
    L, G = len(lams), len(gams)
    INF = float("inf")
    cost = np.full((G + 1, L + 1), INF)
    cost[0, :] = 0.0
    take = np.zeros((G + 1, L + 1), dtype=bool)
    for gi in range(1, G + 1):
        for li in range(gi, L + 1):
            c_take = cost[gi - 1, li - 1] + abs(lams[li - 1] - gams[gi - 1])
            c_skip = cost[gi, li - 1]
            if c_take <= c_skip:
                cost[gi, li] = c_take
                take[gi, li] = True
            else:
                cost[gi, li] = c_skip
    disp, gi, li = [], G, L
    while gi > 0:
        if take[gi, li]:
            disp.append(abs(lams[li - 1] - gams[gi - 1]))
            gi -= 1
        li -= 1
    return float(cost[G, L]), np.array(sorted(disp))


def matching_validator():
    """In-run guard: DP == brute force on 60 random small instances (deterministic)."""
    rng = np.random.default_rng(20260707)
    for _ in range(60):
        L = int(rng.integers(3, 8))
        G = int(rng.integers(1, L + 1))
        lams = np.sort(rng.uniform(0, 10, L))
        gams = np.sort(rng.uniform(0, 10, G))
        best = min(sum(abs(lams[list(c)][k] - gams[k]) for k in range(G))
                   for c in combinations(range(L), G))
        got, _ = match_dp(lams, gams)
        assert abs(got - best) < 1e-9, "matching DP != brute force — code bug"
    print("  matching validator: DP == brute force on 60 seeded instances  OK")


def pair_u2(a1, s1, t1, a2, s2, t2):
    """<psi1, u^2 psi2> = S * m2 (complex second moment of the Gaussian overlap);
    same derivation as w1._pair (h.o. control needs the u^2 form)."""
    a1, s1, t1, a2, s2, t2 = map(mp.mpf, (a1, s1, t1, a2, s2, t2))
    al, be = 1 / (4 * s1 * s1), 1 / (4 * s2 * s2)
    ga = al + be
    dt = t2 - t1
    ubar = (al * a1 + be * a2) / ga
    pref = (2 * mp.pi * s1 * s1) ** mp.mpf("-0.25") \
         * (2 * mp.pi * s2 * s2) ** mp.mpf("-0.25") * mp.sqrt(mp.pi / ga)
    E = mp.exp(-al * be * (a1 - a2) ** 2 / ga - dt * dt / (4 * ga) + 1j * dt * ubar)
    S = pref * E
    m1 = ubar + 1j * dt / (2 * ga)
    m2 = m1 * m1 + 1 / (2 * ga)
    return S, S * m2


def xi_fun(s):
    return s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Xi_fun(t):
    return xi_fun(mp.mpf("0.5") + 1j * mp.mpf(t))


def has_run(seq, k=3):
    """True iff seq is strictly decreasing over >= k consecutive entries; also
    returns the cumulative decrease over the best such run."""
    run = best = 1
    start = best_start = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[i - 1]:
            run += 1
        else:
            run, start = 1, i
        if run > best:
            best, best_start = run, start
    ok = best >= k
    drop = (seq[best_start] - seq[best_start + best - 1]) if ok else 0.0
    return ok, float(drop)


# ----------------------------------------------------------------------
# 2. regression battery (I0.5)
# ----------------------------------------------------------------------
def adelic_regression():
    print("=" * 78)
    print("REGRESSION (I0.5, continued) — N00 §1 adelic anchors (adele_trace code path)")
    print("=" * 78)
    t = mp.mpf("0.2")
    a_pole, a_int = at.local_archimedean(t)
    w_inf = a_pole + a_int
    w2 = at.local_finite(2, t)
    sum_p = at.arithmetic_side(97, t)
    print(f"  W_inf = {mp.nstr(w_inf, 20)}   [N00: 0.60303464961426464498]")
    print(f"  W_2   = {mp.nstr(w2, 20)}   [N00: 0.38013321408074931683]")
    print(f"  sum_p (p<=97) = {mp.nstr(sum_p, 20)}   [N00: 0.60303464960929003883]")
    ok = (abs(w_inf - mp.mpf("0.60303464961426464498")) < mp.mpf("1e-18")
          and abs(w2 - mp.mpf("0.38013321408074931683")) < mp.mpf("1e-18")
          and abs(sum_p - mp.mpf("0.60303464960929003883")) < mp.mpf("1e-18"))
    targets = {"0.05": ("0.00009175670097147148537", mp.mpf("1e-23")),
               "0.2": ("8.860364360447289769e-18", mp.mpf("1e-35"))}
    Z = {}
    for ts, (lit, tol) in targets.items():
        a_pole, a_int, arith, zeros, rhs = at.balance(mp.mpf(ts))
        disc = abs(rhs - zeros)
        Z[float(ts)] = rhs
        print(f"  t={ts}: rhs = {mp.nstr(rhs, 20)}  zero side = {mp.nstr(zeros, 20)}"
              f"  discrepancy = {mp.nstr(disc, 3)}")
        ok &= abs(rhs - mp.mpf(lit)) < tol and disc < mp.mpf("1e-34")
    # truncation-rate row n=8 (N00 §1)
    eps = mp.mpf("0.5")
    target = -mp.zeta(1 + eps, derivative=1) / mp.zeta(1 + eps)
    M = (1 << 9) - 1
    s = mp.mpf(0)
    for p in at.primes_up_to(M):
        lp = mp.log(p)
        k = 1
        while p ** k <= M:
            s += lp * (p ** k) ** (-(1 + eps))
            k += 1
    err = abs(target - s)
    print(f"  truncation row n=8: |error| = {mp.nstr(err, 8)}  "
          f"|error|*M^0.5 = {mp.nstr(err * M ** eps, 8)}   [N00: 0.088009003, 1.9894707]")
    ok &= abs(err - mp.mpf("0.088009003")) < mp.mpf("1e-8")
    print(f"  (gamma values consumed only inside the balance regression, per I0.6)")
    print(f"  adelic regression {'PASSED' if ok else '** FAILED — STOP: reportable finding **'}")
    assert ok
    return Z


def legacy_trace_regression():
    """N00 §2 anchor: Tr g(H_8') = 16.7 with sieve_operator's own g-side convention."""
    t = 0.2
    g = lambda x: 1.0 / (2 * np.sqrt(np.pi * t)) * np.exp(-x ** 2 / (4 * t))
    H, basis, _, _ = so.build_Hn_repaired(8, C=1.0)
    ev = np.linalg.eigvalsh(H)
    tr = float(g(ev).sum())
    print(f"  legacy trace anchor: Tr g_0.2(H_8') = {tr:.4f}   [N00 §2: 16.7]")
    assert abs(tr - 16.7) < 0.1
    return True


def u2_selftest():
    def psi(a, s, tt, x):
        a, s, tt = mp.mpf(a), mp.mpf(s), mp.mpf(tt)   # convert BEFORE arithmetic
        return ((2 * mp.pi * s * s) ** mp.mpf("-0.25")
                * mp.exp(-(x - a) ** 2 / (4 * s * s) + 1j * tt * x))
    worst = mp.mpf(0)
    for (a1, s1, t1, a2, s2, t2) in [(0.7, 0.25, 3.0, 1.1, 0.30, 5.5),
                                     (0.0, 0.71, 0.0, 1.2, 0.71, 0.0),
                                     (-1.6, 0.71, 1.6, 1.6, 0.71, -3.2)]:
        _, U = pair_u2(a1, s1, t1, a2, s2, t2)
        q = mp.quad(lambda x: mp.conj(psi(a1, s1, t1, x)) * x * x * psi(a2, s2, t2, x),
                    sorted([-30, a1, a2, 30]))
        worst = max(worst, abs(U - q))
    print(f"  <u^2> closed form vs mpmath.quad: worst = {mp.nstr(worst, 3)}  [guard 1e-25]")
    assert worst < mp.mpf("1e-25")


def f08_pencil_regression():
    print("=" * 78)
    print("REGRESSION (I0.5, continued) — F08 pencil anchors at n=4 (wp04 code path)")
    print("=" * 78)
    st4 = wp04.build_w1_stage(4)
    B4, Q4, maps4, s4, _ = wp04.build_pencil(st4)
    roots4 = wp04.second_order_roots(B4, Q4, st4["T_n"])
    rows4 = wp04.certified_intervals(s4, roots4)
    radii4 = np.array([r[2] for r in rows4])
    print(f"  n=4: min radius = {radii4.min():.4f}  median radius = "
          f"{np.median(radii4):.4f}   [F08: 1.3387, 1.7411]")
    assert abs(radii4.min() - 1.3387) < 5e-4 and abs(np.median(radii4) - 1.7411) < 5e-4
    coh = max(sqrt(max(np.linalg.eigvalsh(
        Q4 - (2.0 * c) * B4 + (c * c) * np.eye(B4.shape[0]))[0], 0.0)) - r
        for (_s, c, r, _j) in rows4)
    print(f"  coherence (quasi-mode identity): max r_4(Re z) - |Im z| = {coh:.2e}"
          f"  [must be <= 0]")
    assert coh <= 1e-9
    print("  F08 regression PASSED")


# ----------------------------------------------------------------------
# 3. stage data: spectrum + certified intervals per stage (one build each)
# ----------------------------------------------------------------------
def w1_stage_data(n):
    t0 = time.time()
    st = wp04.build_w1_stage(n)
    B, Q, maps, s_pos, dropped = wp04.build_pencil(st)
    roots = wp04.second_order_roots(B, Q, st["T_n"])
    rows = wp04.certified_intervals(s_pos, roots)
    assert len(rows) >= 12, "non-vacuity guard: too few matched intervals"
    dim = B.shape[0]
    ker = dim - 2 * len(s_pos[s_pos > 1e-10 * s_pos.max()])
    d, T_lo, T_w, dev, _ = e0.e0_metric(s_pos)
    in_win = np.sort(s_pos[(s_pos > 0) & (s_pos <= WINDOW)])
    print(f"  [W1] n={n:2d}  M_n={st['M']:6d}  T_n={st['T_n']:9.2f}  dim={dim:5d} "
          f"(dropped {dropped:3d})  ker={ker:2d}  d_n={d:5d}  N+(50)={len(in_win):3d}  "
          f"E0b dev={dev:6.3f}  [{time.time() - t0:7.1f}s]")
    return dict(n=n, M=st["M"], T_n=st["T_n"], s_pos=np.sort(s_pos), ker=ker,
                rows=rows, in_win=in_win, dev=dev, d=d)


def decoy_delta0():
    """Pinned decoy spacing, derived once from the n=4 inventory: log(M_4)/|Q_4|."""
    Q4, M4 = e0.inventory(4)
    return log(M4) / len(Q4)


def decoy_stage_data(n):
    """Bare-wedge decoy: NESTED uniform site grid (pinned spacing delta_0, extended
    to [0, log M_n] as the stage grows — sites are only ever added, mirroring the
    nestedness of the sieve inventory), identical width/ladder/cap rules to W1."""
    t0 = time.time()
    _Q, M = e0.inventory(n)
    d0 = decoy_delta0()
    K = int(log(M) / d0) + 1
    u = np.arange(K) * d0
    T_n = 2 * pi * M ** (2.0 / 3.0)
    a, sg, tau = [], [], []
    for i, ui in enumerate(u):
        tmin = 2 * pi * exp(ui - 1.0)
        dt = (4 * pi / d0) if i == 0 else (2 * pi / d0)
        j = 0
        while True:
            tt = tmin + (j + 0.5) * dt
            if tt > T_n:
                break
            a.append(ui)
            sg.append(d0 / 2.0)
            tau.append(tt)
            j += 1
    a, sg, tau = np.array(a), np.array(sg), np.array(tau)
    S1, D1, Q1 = w1._block(a, sg, tau, mirror=False)
    S2, D2, Q2 = w1._block(a, sg, tau, mirror=True)
    st = dict(Se=2 * (S1 + S2), So=2 * (S1 - S2), K=2 * (D1 - D2),
              Qe=2 * (Q1 + Q2), Qo=2 * (Q1 - Q2))
    sp = w1.stage_spectrum(st)
    s_pos = sp["s"]
    d, T_lo, T_w, dev, _ = e0.e0_metric(s_pos)
    in_win = np.sort(s_pos[(s_pos > 0) & (s_pos <= WINDOW)])
    print(f"  [decoy] n={n:2d}  sites={K:5d}  modes={len(a):5d}  dim={sp['dim']:5d}  "
          f"ker={sp['ker']:2d}  d_n={d:5d}  N+(50)={len(in_win):3d}  "
          f"E0 dev={dev:6.3f}  [{time.time() - t0:7.1f}s]")
    return dict(n=n, M=M, s_pos=np.sort(s_pos), in_win=in_win, dev=dev, d=d,
                ker=sp["ker"])


# ----------------------------------------------------------------------
# 4. E4a — trace consistency (gamma-free)
# ----------------------------------------------------------------------
def e4a_report(stages_data, Z, label="W1"):
    print("=" * 78)
    print(f"E4a — TRACE CONSISTENCY  Tr h_t(H_n) vs Z(t) = W_inf - sum_p W_p  [{label}]")
    print("=" * 78)
    verdicts = {}
    for t in E4A_T:
        C = envelope_C(t)
        zt = float(mp.re(Z[t]))
        print(f"  t = {t}   Z(t) = {mp.nstr(Z[t], 15)}   C(t) = {C:.4f}")
        print(f"    {'n':>3} {'M_n':>7} {'trace T_n':>14} {'residual':>13} "
              f"{'envelope':>10} {'res*sqrt(M)':>12}  within")
        rows = []
        for sd in stages_data:
            tr = float(2.0 * h_t(sd["s_pos"], t).sum() + sd["ker"] * 1.0)
            res = tr - zt
            env = C / sqrt(sd["M"])
            ok = abs(res) <= env
            rows.append((sd["n"], res, env, ok))
            print(f"    {sd['n']:>3} {sd['M']:>7} {tr:>14.8f} {res:>13.4e} "
                  f"{env:>10.4e} {res * sqrt(sd['M']):>12.4f}  {'YES' if ok else 'NO'}")
        verdicts[t] = rows
        # per-band shares of the last-stage residual (F08 bands)
        sd = stages_data[-1]
        tot = 2.0 * h_t(sd["s_pos"], t).sum()
        for lo, hi in zip(BANDS[:-1], BANDS[1:]):
            m = (sd["s_pos"] > lo) & (sd["s_pos"] <= hi)
            share = 2.0 * h_t(sd["s_pos"][m], t).sum()
            print(f"      band ({lo:.0f},{hi:.0f}] share of trace at n={sd['n']}: "
                  f"{share:.6e}  ({100 * share / tot if tot else 0:.1f}%)")
    all_ok = all(ok for rows in verdicts.values() for (_n, _r, _e, ok) in rows)
    fails = [(t, n, r) for t, rows in verdicts.items()
             for (n, r, e, ok) in rows if not ok]
    if all_ok:
        branch = "PASS"
    elif all(r > 0 for (_t, _n, r) in fails):
        branch = "FAIL — persistent EXCESS (quantified pollution mass)"
    elif all(r < 0 for (_t, _n, r) in fails):
        branch = "FAIL — persistent DEFICIT (quantified spectral loss)"
    else:
        branch = "FAIL — mixed sign (report as measured)"
    print(f"  E4a [{label}]: {branch}")
    if fails:
        print(f"    failing stages: " + "  ".join(f"(t={t}, n={n}, res={r:+.4e})"
                                                  for (t, n, r) in fails))
    return all_ok, branch, verdicts


# ----------------------------------------------------------------------
# 5. HS2 — moment gate (gamma-free)
# ----------------------------------------------------------------------
def hs2_targets():
    Xi0 = Xi_fun(0)
    f = lambda tt: mp.log(xi_fun(mp.mpf("0.5") + 1j * tt) / Xi0)
    co = mp.taylor(f, 0, 2 * max(HS2_M))
    sig = {2 * m: -m * mp.re(co[2 * m]) for m in HS2_M}
    odd_worst = max(abs(co[k]) for k in range(1, 2 * max(HS2_M), 2))
    assert odd_worst < mp.mpf("1e-20"), "Xi Taylor not even — code bug"
    return sig, Xi0


def hs2_report(stages_data, sig, label="W1"):
    print("=" * 78)
    print(f"HS2 — MOMENT GATE  sigma_n(2m) vs sigma(2m) from xi Taylor  [{label}]")
    print("=" * 78)
    for m in HS2_M:
        print(f"  sigma({2 * m}) target = {mp.nstr(sig[2 * m], 12)}")
    errs = {m: [] for m in HS2_M}
    print(f"    {'n':>3} " + " ".join(f"{'sigma_n(' + str(2 * m) + ')':>14} "
                                      f"{'|err|':>11}" for m in HS2_M))
    for sd in stages_data:
        line = f"    {sd['n']:>3} "
        for m in HS2_M:
            sn = float((sd["s_pos"][sd["s_pos"] > 0] ** (-2.0 * m)).sum())
            err = abs(sn - float(sig[2 * m]))
            errs[m].append(err)
            line += f"{sn:>14.6e} {err:>11.4e} "
        print(line)
    per_m = {m: has_run(errs[m], 3)[0] for m in HS2_M}
    ok = all(per_m.values())
    print(f"  HS2 [{label}]: {'PASS' if ok else 'FAIL'} "
          f"(per-m decreasing runs >= 3: "
          + ", ".join(f"m={m}: {per_m[m]}" for m in HS2_M) + ")")
    return ok, errs


# ----------------------------------------------------------------------
# 6. HS1 — paired-product gate (gamma-free)
# ----------------------------------------------------------------------
def hs1_report(stages_data, Xi0, label="W1"):
    print("=" * 78)
    print(f"HS1 — PAIRED-PRODUCT GATE  Xi_n(t) vs Xi(t) on [0, 30]  [{label}]")
    print("=" * 78)
    logXi = np.array([float(mp.log(abs(Xi_fun(t)))) if t >= 0 else 0.0
                      for t in HS1_GRID])
    logXi0 = float(mp.log(abs(Xi0)))
    meds = []
    for sd in stages_data:
        s2 = sd["s_pos"][sd["s_pos"] > 0] ** 2
        fac = 1.0 - HS1_GRID[:, None] ** 2 / s2[None, :]
        with np.errstate(divide="ignore"):
            logXin = logXi0 + np.log(np.abs(fac)).sum(axis=1)
        ratio = logXin - logXi
        finite = np.isfinite(ratio)
        M1 = float(np.median(np.abs(ratio[finite])))
        meds.append(M1)
        bands = []
        for lo, hi in ((0, 10), (10, 20), (20, 30)):
            m = finite & (HS1_GRID >= lo) & (HS1_GRID < hi)
            bands.append(float(np.median(np.abs(ratio[m]))))
        print(f"    n={sd['n']:>2}  M1 = median|log(|Xi_n|/|Xi|)| = {M1:8.4f}   "
              f"bands [0,10|10,20|20,30] = {bands[0]:8.4f} {bands[1]:8.4f} "
              f"{bands[2]:8.4f}   excluded pts = {int((~finite).sum())}")
    dec, _ = has_run(meds, 3)
    conv = dec and meds[-1] <= HS1_BAR
    print(f"  HS1 [{label}]: {'CONVERGENT' if conv else 'DIVERGENT'} "
          f"(decreasing run >= 3: {dec}; final M1 = {meds[-1]:.4f} vs bar {HS1_BAR:.4f})")
    return conv, meds


# ----------------------------------------------------------------------
# 7. HS7 — enclosure genealogy (gamma-free)
# ----------------------------------------------------------------------
def hs7_report(stages_data):
    print("=" * 78)
    print("HS7 — ENCLOSURE GENEALOGY  persistence chains of certified intervals  [W1]")
    print("=" * 78)
    K = min(len(sd["rows"]) for sd in stages_data)
    ns = [sd["n"] for sd in stages_data]
    print(f"  aligned interval count across stages: {K}  "
          f"(per stage: {[len(sd['rows']) for sd in stages_data]})")
    breaks = []
    drifts = []
    for k in range(K):
        chain_ok = True
        drift = 0.0
        for j in range(len(stages_data) - 1):
            _s1, c1, r1, _ = stages_data[j]["rows"][k]
            _s2, c2, r2, _ = stages_data[j + 1]["rows"][k]
            overlap = (c1 - r1) <= (c2 + r2) and (c2 - r2) <= (c1 + r1)
            near = abs(c2 - c1) <= 0.5 * (r1 + r2)
            drift += abs(c2 - c1)
            if not (overlap and near):
                chain_ok = False
                breaks.append((k + 1, ns[j], ns[j + 1]))
        drifts.append(drift)
    print(f"  unbroken chains across all computed stages: {K - len(set(b[0] for b in breaks))} / {K}")
    if breaks:
        for (k, n1, n2) in breaks:
            print(f"    BREAK at interval k={k} between n={n1} and n={n2} "
                  f"(localised pollution event)")
    else:
        print("    no chain breaks — the certified genealogy is fully persistent")
    print(f"  per-chain total centre drift: min = {min(drifts):.4f}  "
          f"median = {float(np.median(drifts)):.4f}  max = {max(drifts):.4f}")
    last = stages_data[-1]
    from collections import Counter
    mult = Counter(j for (_s, _c, _r, j) in last["rows"])
    shared = {j: c for j, c in mult.items() if c > 1}
    print(f"  shared-interval multiplicities at n={last['n']}: "
          f"{sorted(shared.values(), reverse=True) if shared else 'none'} "
          f"({len(shared)} shared intervals; F08 fingerprint)")
    return len(breaks), drifts


# ----------------------------------------------------------------------
# 8. controls (gamma-free parts)
# ----------------------------------------------------------------------
def ho_control():
    print("=" * 78)
    print("E4c CONTROL (positive) — harmonic oscillator compression on nested lattices")
    print("=" * 78)
    targets = np.arange(8) + 0.5
    true_tr = float(sum(exp(-0.05 * (j + 0.5) ** 2) for j in range(300)))
    meds, tres = [], []
    for R in HO_STAGES:
        m = int(R / HO_DELTA) + 1
        pts = [(i * HO_DELTA, j * HO_DELTA)
               for i in range(-m, m + 1) for j in range(-m, m + 1)
               if (i * i + j * j) * HO_DELTA ** 2 <= R * R + 1e-12]
        N = len(pts)
        S = np.zeros((N, N), complex)
        H = np.zeros((N, N), complex)
        for i in range(N):
            for j in range(i, N):
                a1, t1 = pts[i]
                a2, t2 = pts[j]
                Sv, Dv, Qv = w1._pair(a1, HO_SG, t1, a2, HO_SG, t2)
                _, Uv = pair_u2(a1, HO_SG, t1, a2, HO_SG, t2)
                S[i, j] = complex(Sv)
                H[i, j] = complex(Qv + Uv) / 2.0
                if j > i:
                    S[j, i] = np.conj(S[i, j])
                    H[j, i] = np.conj(H[i, j])
        w, U = np.linalg.eigh(S)
        keep = w > 1e-10 * w.max()
        X = U[:, keep] / np.sqrt(w[keep])
        ev = np.sort(np.linalg.eigvalsh(X.conj().T @ H @ X))
        _tot, disp = match_dp(ev, targets)          # same matching code path
        med = float(np.median(disp))
        tr = float(np.exp(-0.05 * ev ** 2).sum())
        meds.append(med)
        tres.append(abs(tr - true_tr))
        print(f"    R={R:.1f}  dim={N:3d} (kept {int(keep.sum()):3d})  "
              f"median disp to (j+1/2) = {med:.2e}   |trace res| = {tres[-1]:.2e}")
    ok_med = has_run(meds, 3)[0] and meds[-1] <= 0.01
    ok_tr = has_run(tres, 3)[0] and tres[-1] <= 0.01
    ok = ok_med and ok_tr
    print(f"  h.o. positive control: "
          f"{'PASSES (both metrics demonstrably passable)' if ok else '** FAILS — HARNESS INVALID **'}"
          f"  (displacement: {ok_med}, trace: {ok_tr})")
    return ok


def sine_internal(d_ref, sig):
    print("=" * 78)
    print("HS6 CONTROL (sine decoy) — internal consistency (must-pass), gamma-free part")
    print("=" * 78)
    d = int(d_ref)
    ks = np.arange(1.0, d + 1)
    # exact closed form: prod_{k<=d}(1 - t^2/k^2)
    #                  = sinc(pi t) * Gamma(d+1)^2 / (Gamma(d+1-t) Gamma(d+1+t))
    worst = mp.mpf(0)
    for t in HS1_GRID[1::8]:                       # non-integer subgrid (mp product)
        tt = mp.mpf(float(t))
        prod = mp.mpf(1)
        for k in range(1, d + 1):
            prod *= (1 - tt * tt / k ** 2)
        closed = (mp.sin(mp.pi * tt) / (mp.pi * tt)
                  * mp.exp(mp.loggamma(d + 1 - tt) + mp.loggamma(d + 1 + tt)
                           - 2 * mp.loggamma(d + 1)))
        worst = max(worst, abs(prod - closed))
    ok_prod = worst <= mp.mpf("1e-25")
    print(f"  product identity vs Gamma closed form (mp, non-integer subgrid): "
          f"max = {mp.nstr(worst, 3)}  [guard 1e-25]  -> {'OK' if ok_prod else '** FAIL **'}")
    errs = []
    for dd in (d // 4, d // 2, d):
        errs.append(abs(float(sum(mp.mpf(1) / k ** 2 for k in range(1, dd + 1))
                          - mp.zeta(2))))
    tail_ok = abs(errs[-1] * d - 1.0) <= 0.01      # err = 1/d - 1/(2d^2) + O(d^-3)
    ok_mom = errs[0] > errs[1] > errs[2] and tail_ok
    print(f"  internal moments |sum k^-2 - zeta(2)| over d = {d // 4}, {d // 2}, {d}: "
          + "  ".join(f"{e:.2e}" for e in errs)
          + f"  |err*d - 1| = {abs(errs[-1] * d - 1.0):.2e}"
          + f"  -> {'OK (decreasing, tail scale exact to 1%)' if ok_mom else '** FAIL **'}")
    # arithmetic moment must-fail (density-class gap)
    fail_m = all(abs(float((ks ** (-2.0 * m)).sum()) - float(sig[2 * m]))
                 >= 10 * abs(float(sig[2 * m])) for m in HS2_M)
    print(f"  vs arithmetic sigma(2m): off by >= 10x at every m: "
          f"{'YES [as required]' if fail_m else '** NO — HARNESS BROKEN **'}")
    return ok_prod and ok_mom, fail_m


def decoy_e0_shape(decoy_data):
    devs = [dd["dev"] for dd in decoy_data]
    last3 = devs[-3:]
    dec = all(last3[i + 1] < last3[i] for i in range(len(last3) - 1))
    ok = dec and devs[-1] <= DECOY_E0_BAR
    print(f"  decoy E0 shape: dev sequence = "
          + "  ".join(f"{v:.3f}" for v in devs)
          + f"  -> {'PASSES E0 shape [as required]' if ok else '** FAILS — HARNESS INVALID **'}")
    return ok


# ----------------------------------------------------------------------
# 9. FINAL EVALUATION (I0.6) — the gamma-list enters here and nowhere else
# ----------------------------------------------------------------------
def final_evaluation(w1_data, decoy_data, sine_spec, legacy_specs, graph_specs, Z):
    print("=" * 78)
    print("E4b — MATCHED DISPLACEMENT ON [0, 50]  (FINAL EVALUATION, I0.6: the")
    print("      gamma-list is consumed HERE ONLY, as pre-registered)")
    print("=" * 78)
    gams = []
    k = 1
    while True:
        g = float(mp.im(mp.zetazero(k)))
        if g > WINDOW:
            break
        gams.append(g)
        k += 1
    gams = np.array(gams)
    print(f"  targets: {len(gams)} ordinates <= {WINDOW:.0f} "
          f"(gamma_1 = {gams[0]:.6f} ... gamma_{len(gams)} = {gams[-1]:.6f})")
    hole_ok = gams[0] > 9.34
    print(f"  hole handling (budget item c): gamma_1 > 9.34 hole edge: {hole_ok} "
          f"— the hole blocks no match on this window")

    def family_meds(data):
        meds, counts = [], []
        for sd in data:
            cand = sd["in_win"]
            counts.append(len(cand))
            if len(cand) >= len(gams):
                _tot, disp = match_dp(cand, gams)
                meds.append(float(np.median(disp)))
            else:
                meds.append(float("inf"))
        return meds, counts

    w1_meds, w1_counts = family_meds(w1_data)
    dc_meds, dc_counts = family_meds(decoy_data)
    print(f"    {'n':>3} {'W1 N+(50)':>10} {'W1 med':>9} {'decoy N+(50)':>13} "
          f"{'decoy med':>10} {'decoy-W1':>9}")
    for i, sd in enumerate(w1_data):
        print(f"    {sd['n']:>3} {w1_counts[i]:>10} {w1_meds[i]:>9.4f} "
              f"{dc_counts[i]:>13} {dc_meds[i]:>10.4f} "
              f"{dc_meds[i] - w1_meds[i]:>9.4f}")

    # pollution inventory: W1 sub-gamma_1 surplus at the last stage
    sd = w1_data[-1]
    sub = sd["in_win"][sd["in_win"] < gams[0]]
    t = 0.05
    share = float(2.0 * h_t(sub, t).sum())
    tot_res = float(2.0 * h_t(sd["s_pos"], t).sum() + sd["ker"]) - float(mp.re(Z[t]))
    print(f"  pollution inventory at n={sd['n']}: {len(sub)} eigenvalues below gamma_1 "
          f"({', '.join(f'{v:.3f}' for v in sub)});")
    print(f"    their share of the E4a t=0.05 excess: {share:.4e} of {tot_res:.4e} "
          f"({100 * share / tot_res if tot_res else 0:.1f}%)")
    # interval coverage (report-only; coverage is weak evidence by construction)
    rows = sd["rows"]
    cov = sum(1 for g in gams if any(c - r <= g <= c + r for (_s, c, r, _j) in rows))
    tot_len = sum(2 * r for (_s, _c, r, _j) in
                  {j: rw for rw in rows for j in [rw[3]]}.values())
    print(f"  certified-interval coverage of the {len(gams)} ordinates at n={sd['n']}: "
          f"{cov}/{len(gams)}  (report-only: intervals cover ~{tot_len:.0f} of the "
          f"{WINDOW:.0f}-window — coverage is not evidence)")

    # mechanical rules; localisation scale derived from the targets themselves
    half_spacing = (gams[-1] - gams[0]) / (len(gams) - 1) / 2.0

    def certified_rule(meds):
        letter, drop = has_run(meds, 3)
        cert = letter and drop >= RES_FLOOR and meds[-1] <= half_spacing
        return letter, drop, cert

    print(f"  localisation scale (half mean target spacing, target-derived): "
          f"{half_spacing:.4f}")
    letter, drop, certified = certified_rule(w1_meds)
    last3 = range(len(w1_meds) - 3, len(w1_meds))
    beats = all(dc_meds[i] - w1_meds[i] >= RES_FLOOR for i in last3)
    closes = (not certified) and (not beats)
    print(f"  E4b LETTER rule (median strictly decreasing over >= 3 stages): "
          f"{letter} (cumulative decrease over best run = {drop:.4f})")
    print(f"  E4b CERTIFIED rule (LETTER and decrease >= RES_FLOOR = {RES_FLOOR} and "
          f"final <= {half_spacing:.2f}): {certified}")
    print(f"  BEATS-DECOY (decoy - W1 >= {RES_FLOOR} at each of last 3 stages): {beats}")
    print(f"  -> W1 E4b: {'CERTIFIED PASS' if certified else 'NOT CERTIFIED'};  "
          f"counting-law-only branch fires: {closes}")

    # decoy must-fail E4b
    dc_letter, dc_drop, dc_cert = certified_rule(dc_meds)
    print(f"  decoy E4b: letter = {dc_letter} (drop {dc_drop:.4f}), certified = "
          f"{dc_cert}  -> {'FAILS E4b [as required]' if not dc_cert else '** PASSES — HARNESS BROKEN **'}")

    # sine / legacy / graph must-fail lines (same certified rule, own stage sequences)
    others = {}
    sine_meds = []
    for sd in w1_data:                       # stage-matched: spectrum {1..d_n}
        d_n = len(sd["s_pos"][sd["s_pos"] > 0])
        cand = np.arange(1.0, min(d_n, int(WINDOW)) + 1)
        if len(cand) >= len(gams):
            _t, disp = match_dp(cand, gams)
            sine_meds.append(float(np.median(disp)))
        else:
            sine_meds.append(float("inf"))
    _sl, _sd, s_cert = certified_rule(sine_meds)
    others["sine"] = (sine_meds, s_cert)
    print(f"  sine decoy meds (stage-matched d_n) = "
          + "  ".join(f"{v:.4f}" for v in sine_meds)
          + f"  in-window candidates = {min(len(sine_spec), int(WINDOW))} "
          f"(density witness)  certified = {s_cert} "
          f"-> {'FAILS [as required]' if not s_cert else '** BROKEN **'}")
    print(f"    (absolute sine level may sit below W1 by density alone — S04 §5:")
    print(f"     levels are not comparable across density classes; rules are")
    print(f"     improvement-based and the decoy comparison is density-matched)")
    for name, specs in (("legacy", legacy_specs), ("graph", graph_specs)):
        meds = []
        for (nn, spec) in specs:
            cand = np.sort(spec[(spec > 0) & (spec <= WINDOW)])
            if len(cand) >= len(gams):
                _t, disp = match_dp(cand, gams)
                meds.append(float(np.median(disp)))
            else:
                meds.append(float("inf"))
        _l, _d, cert = certified_rule(meds)
        others[name] = (meds, cert)
        print(f"  {name} meds = " + "  ".join(f"{v:9.4f}" for v in meds)
              + f"   certified = {cert} "
              f"-> {'FAILS [as required]' if not cert else '** BROKEN **'}")
    return dict(gams=gams, w1_meds=w1_meds, dc_meds=dc_meds, letter=letter,
                drop=drop, certified=certified, beats=beats, closes=closes,
                dc_cert=dc_cert, others=others, cov=cov)


# ----------------------------------------------------------------------
# 10. main
# ----------------------------------------------------------------------
def run(stages):
    w1.selftest()                        # closed-form S/D/Q validation (F07 harness)
    e0.regression()                      # N00 anchors (I0.5)
    wp04.w1_regression()                 # F07 E0b anchors (n = 4, 6)
    f08_pencil_regression()              # F08 anchors + coherence
    Z = adelic_regression()              # N00 §1 anchors; E4a target Z(t)
    print("=" * 78)
    print("REGRESSION (I0.5, continued) — legacy trace anchor, <u^2> forms, matching")
    print("=" * 78)
    legacy_trace_regression()
    u2_selftest()
    matching_validator()

    print("=" * 78)
    print("E4 — STAGE DATA  [W1 primary]  (spectra + certified intervals, F08 code path)")
    print("=" * 78)
    w1_data = [w1_stage_data(n) for n in stages]

    print("=" * 78)
    print("E4c CONTROL (decoy) — bare wedge: uniform sites, identical ladder rules")
    print("=" * 78)
    decoy_data = [decoy_stage_data(n) for n in stages]

    # gamma-free component reports
    e4a_ok, e4a_branch, _ = e4a_report(w1_data, Z, "W1")
    sig, Xi0 = hs2_targets()
    hs2_ok, _ = hs2_report(w1_data, sig, "W1")
    hs1_ok, hs1_meds = hs1_report(w1_data, Xi0, "W1")
    n_breaks, drifts = hs7_report(w1_data)

    # decoy gamma-free report lines (context for the family comparison)
    _dc_e4a_ok, dc_e4a_branch, _ = e4a_report(decoy_data, Z, "decoy")
    _dc_hs2_ok, _ = hs2_report(decoy_data, sig, "decoy")

    # controls, gamma-free parts
    ho_ok = ho_control()
    d_ref = len(w1_data[-1]["s_pos"][w1_data[-1]["s_pos"] > 0])
    sine_spec = np.arange(1.0, d_ref + 1)
    sine_int_ok, sine_mom_fail = sine_internal(d_ref, sig)
    # sine E4a must-fail (last-stage envelope, both t)
    sine_fail_e4a = True
    for t in E4A_T:
        res = float(2.0 * h_t(sine_spec, t).sum()) - float(mp.re(Z[t]))
        env = envelope_C(t) / sqrt(w1_data[-1]["M"])
        sine_fail_e4a &= abs(res) > env
        print(f"  sine E4a t={t}: residual = {res:+.4e} vs envelope {env:.4e} "
              f"-> {'outside [as required]' if abs(res) > env else '** inside — BROKEN **'}")
    # legacy + graph spectra and E4a must-fail
    legacy_specs, graph_specs = [], []
    legacy_fail = graph_fail = True
    for nn in (8, 10, 12):
        H, basis, _, _ = so.build_Hn_repaired(nn, C=1.0)
        ev = np.linalg.eigvalsh(H)
        legacy_specs.append((nn, np.abs(ev)))
        for t in E4A_T:
            res = float(h_t(ev, t).sum()) - float(mp.re(Z[t]))
            legacy_fail &= abs(res) > envelope_C(t) / sqrt((1 << (nn + 1)) - 1)
    print(f"  legacy E4a outside envelope at every stage/t: "
          f"{'YES [as required]' if legacy_fail else '** NO — BROKEN **'}")
    for nn in (6, 8, 9):
        W, *_ = pgl.build_bipartite(nn, quiet=True)
        s = np.linalg.svd(W, compute_uv=False)
        graph_specs.append((nn, s))
        for t in E4A_T:
            res = float(2.0 * h_t(s, t).sum()) - float(mp.re(Z[t]))
            graph_fail &= abs(res) > envelope_C(t) / sqrt((1 << (nn + 1)) - 1)
    print(f"  graph E4a outside envelope at every stage/t: "
          f"{'YES [as required]' if graph_fail else '** NO — BROKEN **'}")
    decoy_e0_ok = decoy_e0_shape(decoy_data)

    # FINAL EVALUATION (gamma-list here only)
    fe = final_evaluation(w1_data, decoy_data, sine_spec, legacy_specs,
                          graph_specs, Z)

    print("=" * 78)
    print("VERDICT (mechanical application of the pre-registered rules)")
    print("=" * 78)
    harness_ok = (ho_ok and sine_int_ok and sine_mom_fail and sine_fail_e4a
                  and (not fe["others"]["sine"][1]) and legacy_fail and graph_fail
                  and (not fe["others"]["legacy"][1])
                  and (not fe["others"]["graph"][1])
                  and decoy_e0_ok and (not fe["dc_cert"]))
    print(f"  harness valid:            {harness_ok}")
    print(f"    positive h.o. control passes:        {ho_ok}")
    print(f"    sine internal passes / arith fails:  {sine_int_ok} / "
          f"{sine_mom_fail and sine_fail_e4a and not fe['others']['sine'][1]}")
    print(f"    legacy fails / graph fails:          "
          f"{legacy_fail and not fe['others']['legacy'][1]} / "
          f"{graph_fail and not fe['others']['graph'][1]}")
    print(f"    decoy passes E0 shape / fails E4b:   {decoy_e0_ok} / {not fe['dc_cert']}")
    print(f"  E4a [W1]:                 {e4a_branch}")
    print(f"  E4b [W1]:                 letter = {fe['letter']} "
          f"(drop {fe['drop']:.4f}); CERTIFIED = {fe['certified']}; "
          f"beats-decoy = {fe['beats']}")
    print(f"  HS1 [W1]:                 {'CONVERGENT' if hs1_ok else 'DIVERGENT'}"
          f" — jointly with E4a: "
          f"{'quantified determinant-level pollution (diverges while E4a passes)' if (not hs1_ok) and e4a_ok else ('consistent L3/L4 pollution (diverges with E4a excess)' if not hs1_ok else 'consistent')}")
    print(f"  HS2 [W1]:                 {'PASS' if hs2_ok else 'FAIL'}")
    print(f"  HS7 [W1]:                 {n_breaks} chain breaks; median drift = "
          f"{float(np.median(drifts)):.4f} (report-only)")
    arithmetic = e4a_ok and fe["certified"] and hs2_ok
    print(f"  W1 FAMILY VERDICT:        "
          f"{'ARITHMETIC (all of E4a, E4b-certified, HS2 pass)' if arithmetic else ('COUNTING LAW ONLY (pre-registered closure branch)' if fe['closes'] else 'MIXED — report as measured')}")
    if not arithmetic:
        print("  -> Pre-registered escalation: the E-track candidate moves to the")
        print("     genuinely quadratic PROLATE PENCIL (Connes-Moscovici; F02 redesign")
        print("     note / WP02b falsifier branch) — a new WP with its own")
        print("     pre-registration.  The harness itself is the WP05 deliverable and")
        print("     remains valid for any successor candidate.")
    print("  O6 (binding): no outcome here is evidence about zeros; a family-level")
    print("     kill is a statement about THIS window design.  RH is open.")


if __name__ == "__main__":
    run(STAGES_FAST if "fast" in sys.argv else STAGES_FULL)
