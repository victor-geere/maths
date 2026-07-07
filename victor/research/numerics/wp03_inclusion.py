"""wp03_inclusion.py — PSC2-WP03 (E2): the inclusion criterion on the W1 family —
stage resolution function r_n(lambda), spectral gaps, and the graph-density verdict.

THE OBJECT.  E2b asks whether every point of spec(D) = R (ambient of S03 Lemma 1.1,
fixed once by E2a in the finding note) is a limit of stage eigenvalues of
H^{G,w}_n = P_n D P_n on the W1 wedge spaces V_n of PSC2-WP02b/F07.  The finding
note proves (Lemma 1 + Theorem 2):

    dist(lambda, spec H_n)  <=  r_n(lambda) := min_{0 != v in V_n} ||(D-lambda)v||/||v||,

and:  graph-norm stage density of {V_n} on any core of D  ==>  r_n(lambda) -> 0 for
every lambda in spec(D)  ==>  full spectral inclusion.  Contrapositive: if r_n(lambda)
is bounded below on a window, graph-norm stage density FAILS there — the E2b hypothesis
is unavailable, which is the WP03 falsifier branch ("window incompatible with a common
core"), quantified.  r_n is exactly computable from the delivered pencil matrices:

    r_n(lambda)^2 = min eig ( Qt - 2 lambda Bt + lambda^2 I )      (whitened, Gram -> I),

the SAME matrices as F08's second-order pencil, evaluated at real lambda.  At F08's
pencil roots z the quasi-mode identity gives r_n(Re z) <= |Im z|: the F08 radii are
pointwise upper bounds for r_n — the two runs must be coherent.

PRE-REGISTERED OPERATIONALISATION (fixed in this header before the run; the WP03
falsifier text is the bar, this only operationalises it):
  * Stages n = 4, 6, 8, 10, 12 (the E0b stages).  Window [0, 50] (the E4b window).
  * Profile grid: lambda = 0(0.5)50 for n <= 10 (101 points); n = 12 at
    lambda = 0(5)50 (11 points; the n=12 role is agreement with n=10, F08-fingerprint).
    r_n is 1-Lipschitz in lambda (proven in the finding), so the continuum floor on
    [0, 50] is certified as  c_n := (grid min) - h/2  with h the grid step.
  * Probe set (fixed from F08's published n=12 table before this run):
      lambda_P = { 5.0 (low-energy hole), 10.586 (midpoint of eigenvalues 1-2),
                   26.182 (midpoint of eigenvalues 6-7, the largest [0,50] gap) }.
    Genealogy of r_n(lambda_P) and dist(lambda_P, spec H_n) across stages.
  * MUST-HOLD theorem checks (mechanical; failure = code bug, run invalid):
      T-a  dist(lambda, spec H_n) <= r_n(lambda) + 1e-6 (1+|lambda|)   [Lemma 1]
      T-b  r_n(lambda) <= b_n(lambda) + 1e-8  and  dist <= b_n(lambda) + 1e-6,
           b_n(lambda) := min over single modes sqrt(1/(4 sg_k^2) + (tau_k-lambda)^2)
           [Theorem 4's explicit coarse-inclusion bound; psi_k in V_n]
      T-c  operator inequality Q - B^2 >= -1e-7 ||Q||  (Cauchy-Schwarz, n <= 10).
  * CONTROLS (two-sided; identical r/dist code path where applicable):
      must-pass (a) prototype finite-place filtration (S00 Prop 6.1(1), Theorem 3 of
          the finding): r(log 97) = min_{q <= M_n} |log q - log 97| must be > 1 at
          n = 4 and EXACTLY 0 for n >= 6 — the exhausting-filtration pattern.
      must-pass (b) exhausting archimedean Gabor family (site u = 0, sigma_k = 2^(k-1),
          k = 1..5, ladder tau_j = (j+1/2) pi / sigma_k <= 55, J-symmetrised, same
          whitened-pencil code path): grid-median of r over [0, 50] strictly
          decreasing in k AND final <= 0.15 — the r-metric is demonstrably passable
          by a complete family.  Report its counting shape N(50)/N(25) (linear ~ 2,
          i.e. the E0-killed shape) as the trade-off datum, report-only.
      witnesses (c) sub-wedge probes phi = psi_{a,sigma,tau} (unit coherent states):
          phi_gap = (0, 2.0, 10.586), phi_mid = (0, 0.35, 25.0),
          phi_far = (5.0, 0.35, 25.0);  report dist(phi, V_n) = sqrt(1 - ||P_n phi||^2);
          pre-registered witness line: dist(phi_far, V_n) >= 0.5 at every stage
          (deep sub-wedge state never approximated => P_n -/-> I on H).
  * VERDICT RULE (mechanical):  with c_n the certified floors and m_n the grid minima
    on [0, 50]:
      FALSIFIER BRANCH ("window incompatible", quantified)  iff
          min_n c_n >= 0.5  AND  m_last >= 0.75 m_first;
      E2B-OPEN BRANCH (strict inclusion route stays live)   iff  m_last <= 0.5 m_first;
      otherwise INDETERMINATE (report as such).
    Either way O6 binds: nothing here is evidence about zeros; spec(D) = R carries
    no arithmetic (E2a).
  * REGRESSION (I0.5) first: w1.selftest(); e0.regression() (gamma-list ONLY there);
    F07 anchors n = 4, 6 (dev, dim, trace ratio) via wp04.w1_regression();
    F08 anchors at n = 4 (min radius 1.3387, median radius 1.7411) through the
    wp04 pencil code path, tolerance 5e-4.
  * Moving-window context (report-only): max gap between consecutive positive
    eigenvalues inside the derived E0b window per stage (the asymptotic-inclusion
    picture at the top of the window; not a gate).

Deterministic (no RNG).  Run:  python wp03_inclusion.py  [fast]   ('fast' drops n=12;
per F08 precedent the criteria apply to the computed stages unchanged.)
"""

import sys
import time
from math import log, pi, sqrt

import numpy as np

import e0_density_gate as e0            # N00 regression harness (I0.5); sets dps 35
import wp02b_rewindow as w1             # W1 builder: closed forms, blocks, self-test
import wp04_certified_enclosures as wp04  # aligned stage build + whitened pencil

WINDOW = 50.0
BANDS = (0.0, 15.0, 30.0, 50.0)
PROBES = (5.0, 10.586, 26.182)          # pre-registered (F08 n=12 table)
GRID_H = 0.5                            # profile step, n <= 10
GRID_H12 = 5.0                          # spot grid, n = 12
STAGES_FULL = (4, 6, 8, 10, 12)
STAGES_FAST = (4, 6, 8, 10)
FLOOR_BAR = 0.5                         # pre-registered branch thresholds
TREND_HI, TREND_LO = 0.75, 0.5


# ----------------------------------------------------------------------
# 1. the three quantities: r_n(lambda), dist(lambda, spec), b_n(lambda)
# ----------------------------------------------------------------------
def r_of_lambda(B, Q, lam):
    """Stage resolution r_n(lambda) = min_{unit v in V_n} ||(D-lambda)v||, exactly:
    sqrt of the smallest eigenvalue of the whitened M(lambda) = Q - 2 lam B + lam^2."""
    M = Q - (2.0 * lam) * B + (lam * lam) * np.eye(B.shape[0])
    return sqrt(max(np.linalg.eigvalsh(M)[0], 0.0))


def dist_spec(s_pos, lam):
    """dist(lambda, spec H_n) with spec = {+/- s_i} (E1 pairing, F01)."""
    return float(min(np.abs(s_pos - lam).min(), np.abs(s_pos + lam).min()))


def single_mode_bound(st, lam):
    """Theorem 4's bound b_n(lambda): best single coherent state psi_k in V_n
    (modes carry +tau; the mirrored -tau states cover lambda < 0)."""
    return float(np.sqrt(1.0 / (4.0 * st["sg"] ** 2)
                         + (st["tau"] - lam) ** 2).min())


# ----------------------------------------------------------------------
# 2. sub-wedge probes: dist(phi, V_n) via closed-form cross-Gram
# ----------------------------------------------------------------------
def probe_distance(st, maps, a, sg, tau):
    """dist(phi, V_n) for the unit coherent state phi = psi_{a, sg, tau}:
    sqrt(1 - ||Xe^H c_e||^2 - ||Xo^H c_o||^2), c the cross-Gram in the e/o basis."""
    Xe, Xo, ne, no = maps
    N = len(st["a"])
    ce = np.empty(N, complex)
    co = np.empty(N, complex)
    for k in range(N):
        d1 = complex(w1._pair(st["a"][k], st["sg"][k], st["tau"][k], a, sg, tau)[0])
        d2 = complex(w1._pair(-st["a"][k], st["sg"][k], -st["tau"][k], a, sg, tau)[0])
        ce[k] = d1 + d2
        co[k] = d1 - d2
    proj2 = float(np.linalg.norm(Xe.conj().T @ ce) ** 2
                  + np.linalg.norm(Xo.conj().T @ co) ** 2)
    return sqrt(max(1.0 - proj2, 0.0))


# ----------------------------------------------------------------------
# 3. controls
# ----------------------------------------------------------------------
def prototype_control(stages):
    """Must-pass (a): the finite-place filtration exhausts its operator core
    (S00 Prop 6.1(1)): r(log 97) hits 0 exactly once 97 <= M_n."""
    print("  (a) prototype finite-place filtration  A_n = P_n A P_n  on l^2_Lambda:")
    lam = log(97.0)
    ok = True
    for n in stages:
        Q, M = e0.inventory(n)
        r = float(np.abs(np.log(Q.astype(float)) - lam).min())
        exact = " (exact: log 97 in spec once M_n >= 97)" if r == 0.0 else ""
        print(f"        n={n:2d}  M_n={M:6d}   r(log 97) = {r:.6f}{exact}")
        ok &= (r > 1.0) if n == 4 else (r == 0.0)
    print(f"      -> {'PASSES (exhausting filtration: r -> 0, Theorem 3)' if ok else '** FAILS — HARNESS INVALID **'}")
    return ok


def gabor_member(k, tau_max=55.0):
    """Exhausting Gabor family member k: sigma = 2^(k-1), single site u = 0,
    ladder tau_j = (j+1/2) pi/sigma <= tau_max, J-symmetrised, same block code."""
    sg = 2.0 ** (k - 1)
    dt = pi / sg
    tau = np.arange(dt / 2.0, tau_max, dt)
    a = np.zeros_like(tau)
    sgv = np.full_like(tau, sg)
    S1, D1, Q1 = w1._block(a, sgv, tau, mirror=False)
    S2, D2, Q2 = w1._block(a, sgv, tau, mirror=True)
    st = dict(a=a, sg=sgv, tau=tau,
              Se=2 * (S1 + S2), So=2 * (S1 - S2), K=2 * (D1 - D2),
              Qe=2 * (Q1 + Q2), Qo=2 * (Q1 - Q2))
    return st, sg


def gabor_control():
    """Must-pass (b): a complete (exhausting) archimedean family drives r -> 0 on
    [0, 50] through the identical whitened-pencil code path."""
    print("  (b) exhausting Gabor family (u = 0, sigma_k = 2^(k-1), ladder pi/sigma):")
    lams = np.arange(0.0, WINDOW + GRID_H / 2, GRID_H)
    med_seq, cnt = [], {}
    for k in range(1, 6):
        st, sg = gabor_member(k)
        B, Q, maps, s, dropped = wp04.build_pencil(st)
        rr = np.array([r_of_lambda(B, Q, la) for la in lams])
        med_seq.append(float(np.median(rr)))
        cnt[k] = (int((st["tau"] <= 25.0).sum()), int((st["tau"] <= 50.0).sum()))
        print(f"        k={k}  sigma={sg:5.1f}  dim={B.shape[0]:4d} (dropped {dropped})"
              f"   r on [0,50]: median = {med_seq[-1]:.4f}   min = {rr.min():.4f}"
              f"   max = {rr.max():.4f}")
    dec = all(med_seq[i + 1] < med_seq[i] for i in range(len(med_seq) - 1))
    ok = dec and med_seq[-1] <= 0.15
    n25, n50 = cnt[5]
    print(f"      counting shape (report-only): N(50)/N(25) = {n50}/{n25} = "
          f"{n50 / n25:.2f} — linear, the E0-killed shape (F02): completeness on the")
    print(f"      window is bought at the counting law the density gate forbids.")
    print(f"      -> {'PASSES (metric is demonstrably passable: median '
          + ' -> '.join(f'{v:.3f}' for v in med_seq) + ')' if ok else '** FAILS — HARNESS INVALID **'}")
    return ok


# ----------------------------------------------------------------------
# 4. the primary measurement
# ----------------------------------------------------------------------
def stage_measurement(n):
    t0 = time.time()
    st = wp04.build_w1_stage(n)
    B, Q, maps, s_pos, dropped = wp04.build_pencil(st)
    d = B.shape[0]

    if n <= 10:                                        # T-c guard
        wQ = np.linalg.eigvalsh(Q - B @ B)
        assert wQ.min() > -1e-7 * np.abs(Q).max(), "Q - B^2 >= 0 violated"

    h = GRID_H if n <= 10 else GRID_H12
    lams = np.arange(0.0, WINDOW + h / 2, h)
    rr = np.empty(len(lams))
    dd = np.empty(len(lams))
    for i, la in enumerate(lams):
        rr[i] = r_of_lambda(B, Q, la)
        dd[i] = dist_spec(s_pos, la)
        bnd = single_mode_bound(st, la)
        assert dd[i] <= rr[i] + 1e-6 * (1 + la), "T-a violated (Lemma 1) — code bug"
        assert rr[i] <= bnd + 1e-8, "T-b violated (r <= b) — code bug"
        assert dd[i] <= bnd + 1e-6, "T-b violated (dist <= b) — code bug"

    in_win = s_pos[(s_pos > 0) & (s_pos <= WINDOW)]
    gaps = np.diff(np.sort(in_win))
    bands = [float(np.median(rr[(lams >= lo) & (lams < hi)]))
             for lo, hi in zip(BANDS[:-1], BANDS[1:])]

    # moving-window context (report-only)
    d_n, T_lo, T_w, _dev, _prof = e0.e0_metric(np.sort(s_pos)[::-1])
    sw = np.sort(s_pos[(s_pos >= T_lo) & (s_pos <= T_w)])
    maxgap_win = float(np.diff(sw).max()) if len(sw) > 1 else float("nan")

    probes_r = [r_of_lambda(B, Q, la) for la in PROBES]
    probes_d = [dist_spec(s_pos, la) for la in PROBES]
    pd_gap = probe_distance(st, maps, 0.0, 2.0, 10.586)
    pd_mid = probe_distance(st, maps, 0.0, 0.35, 25.0)
    pd_far = probe_distance(st, maps, 5.0, 0.35, 25.0)

    print(f"  [W1] n={n:2d}  M_n={st['M']:6d}  dim={d:5d} (dropped {dropped:3d})  "
          f"grid h={h:.1f}   #eigs in (0,{WINDOW:.0f}]={len(in_win):3d}   "
          f"[{time.time() - t0:7.1f}s]")
    print(f"       r_n on [0,50]:  min={rr.min():7.4f}  certified floor "
          f"c_n = min - h/2 ={rr.min() - h / 2:7.4f}   bands [0,15|15,30|30,50] "
          f"median = {bands[0]:7.4f} {bands[1]:7.4f} {bands[2]:7.4f}")
    print(f"       r_n at probes (5.0, 10.586, 26.182)     = "
          f"{probes_r[0]:8.4f} {probes_r[1]:8.4f} {probes_r[2]:8.4f}")
    print(f"       dist(., spec) at probes                 = "
          f"{probes_d[0]:8.4f} {probes_d[1]:8.4f} {probes_d[2]:8.4f}")
    print(f"       smallest positive eigenvalue = {in_win.min() if len(in_win) else float('nan'):8.4f}"
          f"   max gap in (0,50] = {gaps.max() if len(gaps) else float('nan'):7.4f}"
          f"   max gap in E0b window [{T_lo:7.2f},{T_w:9.2f}] = {maxgap_win:7.4f}")
    print(f"       sub-wedge probes dist(phi, V_n):  phi_gap = {pd_gap:.4f}   "
          f"phi_mid = {pd_mid:.4f}   phi_far = {pd_far:.4f}")
    return dict(n=n, h=h, lams=lams, rr=rr, dd=dd, in_win=np.sort(in_win),
                probes_r=probes_r, probes_d=probes_d,
                pd=(pd_gap, pd_mid, pd_far), floor=rr.min() - h / 2,
                gmin=float(rr.min()))


def genealogy(results):
    print("\n  genealogy across stages (rows: quantity at the pre-registered probes):")
    hdr = "    quantity                 " + "".join(f"  n={r['n']:>2d}    " for r in results)
    print(hdr)
    for j, la in enumerate(PROBES):
        line = f"    r_n({la:6.3f})            "
        for r in results:
            line += f" {r['probes_r'][j]:8.4f}"
        print(line)
    for j, la in enumerate(PROBES):
        line = f"    dist({la:6.3f}, spec)    "
        for r in results:
            line += f" {r['probes_d'][j]:8.4f}"
        print(line)
    for j, name in enumerate(("phi_gap", "phi_mid", "phi_far")):
        line = f"    dist({name}, V_n)      "
        for r in results:
            line += f" {r['pd'][j]:8.4f}"
        print(line)
    line = "    grid min of r_n          "
    for r in results:
        line += f" {r['gmin']:8.4f}"
    print(line)
    line = "    certified floor c_n      "
    for r in results:
        line += f" {r['floor']:8.4f}"
    print(line)
    last = results[-1]
    prev = results[-2]
    k = min(len(last["in_win"]), len(prev["in_win"]))
    shift = float(np.abs(last["in_win"][:k] - prev["in_win"][:k]).max())
    print(f"\n  eigenvalues in (0, 50] at n={last['n']} vs n={prev['n']}: "
          f"counts {len(last['in_win'])} vs {len(prev['in_win'])}, "
          f"max |shift| (index-matched) = {shift:.2e}  (F08 fingerprint: "
          f"stage growth no longer moves the window)")


# ----------------------------------------------------------------------
# 5. main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    fast = "fast" in sys.argv
    stages = STAGES_FAST if fast else STAGES_FULL

    w1.selftest()                        # closed-form S/D/Q validation (F07 harness)
    e0.regression()                      # N00 anchors (I0.5); gamma-list ONLY here
    wp04.w1_regression()                 # F07 E0b anchors (n = 4, 6)

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
    # coherence of the two runs: r_n(Re z) <= |Im z| at every matched F08 root
    coh = max(r_of_lambda(B4, Q4, c) - r for (_s, c, r, _j) in rows4)
    print(f"  coherence with F08 (quasi-mode identity): max r_4(Re z) - |Im z| over "
          f"matched roots = {coh:.2e}  [must be <= 0]")
    assert coh <= 1e-9, "F08 coherence violated"
    print("  F08 regression PASSED")

    print("=" * 78)
    print(f"E2 — STAGE RESOLUTION r_n(lambda) AND SPECTRAL GAPS ON [0, {WINDOW:.0f}]"
          f"  [W1 family]")
    print("=" * 78)
    results = [stage_measurement(n) for n in stages]
    genealogy(results)

    print("=" * 78)
    print("E2 — CONTROLS (must-pass: prototype filtration, exhausting Gabor family)")
    print("=" * 78)
    proto_ok = prototype_control(stages)
    gabor_ok = gabor_control()

    floors = [r["floor"] for r in results]
    gmins = [r["gmin"] for r in results]
    far_ok = all(r["pd"][2] >= 0.5 for r in results)
    falsifier = (min(floors) >= FLOOR_BAR) and (gmins[-1] >= TREND_HI * gmins[0])
    e2b_open = gmins[-1] <= TREND_LO * gmins[0]

    print("=" * 78)
    print("VERDICT (mechanical application of the pre-registered rule)")
    print("=" * 78)
    print(f"  harness valid:            {proto_ok and gabor_ok}  "
          f"(prototype passes: {proto_ok}; Gabor exhausting family passes: {gabor_ok})")
    print(f"  theorem checks T-a/T-b/T-c: PASSED at every grid point (asserted)")
    print(f"  certified floors c_n on [0,50]: "
          + "  ".join(f"{v:.4f}" for v in floors)
          + f"   [bar {FLOOR_BAR}]")
    print(f"  grid-min trend m_last/m_first = {gmins[-1] / gmins[0]:.3f}"
          f"   [falsifier branch iff >= {TREND_HI}; E2b-open iff <= {TREND_LO}]")
    print(f"  sub-wedge witness (phi_far >= 0.5 at every stage): {far_ok}")
    if falsifier:
        print("  E2b on W1, fixed windows:  FALSIFIER BRANCH — graph-norm stage density")
        print("     fails on [0, 50] at every computed stage (certified floor), with the")
        print("     profile stage-stable (F08 fingerprint).  The WP03 falsifier fires in")
        print("     quantified form: the W1 window is incompatible with the E2b hypothesis")
        print("     on fixed windows; this constrains the WINDOW DESIGN (the wedge's fixed")
        print("     aperture), not the theorem's ambition.  Theorems 2-4 of the finding")
        print("     stand proven; the prototype (control a) realises the E2b pattern.")
    elif e2b_open:
        print("  E2b on W1, fixed windows:  E2B-OPEN BRANCH — r_n decreasing; the strict")
        print("     inclusion route stays live; re-derive the finding accordingly.")
    else:
        print("  E2b on W1, fixed windows:  INDETERMINATE — report profiles as measured;")
        print("     no branch claimed; the bar does not move post hoc.")
    print("  O6 (binding): spec(D) = R on this ambient; NOTHING here is evidence about")
    print("     zeros.  The constraint feeds WP05's E4b design (resolution budget) and")
    print("     the pre-registered prolate-pencil escalation (F02 redesign note).")
