"""wp02b_rewindow.py — W1 wedge builder + gate E0b (the rewindowed density gate) for PSC2-WP02b.

THE OBJECT.  The wedge-windowed sieve-Galerkin compression H^{G,w}_n = P_n D P_n of
PSC2-WP02b: ambient L^2(R, du) (u = log x), D = -i d/du, J = parity, J D J^{-1} = -D.
F02's proven no-go lemma killed every fixed basis whose phase-space cells are frequency
intervals centred on tau = 0 (concave counting law).  W1 realises F02's redesign note:
Berry-Keating wedge support |u| <= 1 + log(|tau|/2pi), with the sieve inventory entering
as TRANSLATION LENGTHS (mode frequencies switch on at tau_min(u_q) = 2pi e^{u_q - 1}),
not as bump positions.

STAGE BASIS V_n (J-invariant BY CONSTRUCTION; E1 pairing exact, F01 C-c):
  * sites: u_0 = 0 (archimedean) and u_q = log q for prime powers q <= M_n = 2^{n+1}-1;
  * tiling widths w_i = (u_{i+1} - u_{i-1})/2 (0-site: mirror neighbour -log 2, w_0 = log 2;
    last site: left gap); Gaussian width sigma_i = w_i / 2 — all derived, nothing chosen;
  * wedge ladders: psi_{i,j}(u) = (2 pi sigma_i^2)^{-1/4} exp(-(u-u_i)^2/(4 sigma_i^2))
    e^{i tau_j u}, tau_j = tau_min(u_i) + (j + 1/2) dtau_i <= T_n, tau_min(u) = 2pi e^{u-1},
    dtau_i = 2pi/w_i, EXCEPT the self-mirrored 0-site: dtau_0 = 4pi/w_0 (its cos/sin pair
    shares one physical cell — Planck counting, one-sided);
  * cap T_n = 2 pi M_n^{2/3} (derived power of the sieve cutoff, fixed in the WP);
  * symmetrisation e = psi + J psi, o = psi - J psi, J psi_{a,s,t} = psi_{-a,s,-t}.
Derived law (zero fitted parameters): one Planck cell per state tiling the wedge gives
  N_pred(T) = #{(i,j): tau_j <= T} ~ (T/2pi) log(T/2pi)  exactly (the +1 in the wedge
extent cancels the -T/2pi term); the density ~ log(T/2pi)/2pi is INCREASING — the law is
convex, structurally outside F02's no-go class (mechanical check below).

PRE-REGISTERED CRITERIA — inherited from WP02 VERBATIM (the bar does not move):
  N+(T) := #{lambda in spec : 0 < lambda <= T};  R(T) := (T/2pi) log(T/2pi);
  window W_n = [T_lo, T_win], R(T_lo) = sqrt(d_n), R(T_win) = d_n, d_n = #positive eigs;
  dev_n = max over 200-point geometric grid of |N+/R - 1|;
  E0b PASS iff dev strictly decreasing over the last three stages AND final dev <= 0.05.
  Stages n = 4, 6, 8, 10, 12.  MUST-FAIL controls and the smooth-law positive control are
  the identical code path of e0_density_gate.py.  O6 (binding): a PASS is NOT evidence
  about zeros — it certifies only that the redesign repaired the killed component and
  reopens the E-track.  Falsifier branches: see PSC2-WP02b.

Deterministic (no RNG).  Run:  python wp02b_rewindow.py  [fast]
"""

import sys
from math import pi, log, exp, sqrt

import numpy as np
import mpmath as mp

import e0_density_gate as e0          # gate harness reused verbatim (sets dps 35)

mp.mp.dps = 35
TWO_PI = 2 * pi
EXP_CUT = 120.0                       # skip pairs with Gaussian exponent < -EXP_CUT
DROP_TOL = 1e-8                       # relative Gram-eigenvalue drop threshold


# ----------------------------------------------------------------------
# 1. the W1 wedge inventory: sites, widths, ladders
# ----------------------------------------------------------------------
def wedge_modes(n):
    """Return (a, sg, tau) arrays for the stage-n W1 basis, plus (M, T_n, site data)."""
    Q, M = e0.inventory(n)
    u = np.concatenate([[0.0], np.log(Q.astype(float))])
    w = np.empty_like(u)
    w[0] = u[1]                                    # 0-site symmetric cell: log 2
    w[1:-1] = (u[2:] - u[:-2]) / 2.0               # midpoint tiling widths
    w[-1] = u[-1] - u[-2]                          # last site: left gap
    T_n = TWO_PI * M ** (2.0 / 3.0)
    a, sg, tau = [], [], []
    for i, (ui, wi) in enumerate(zip(u, w)):
        t0 = TWO_PI * exp(ui - 1.0)                # wedge boundary at the site centre
        dt = (4 * pi / wi) if i == 0 else (2 * pi / wi)
        j = 0
        while True:
            t = t0 + (j + 0.5) * dt
            if t > T_n:
                break
            a.append(ui); sg.append(wi / 2.0); tau.append(t)
            j += 1
    return (np.array(a), np.array(sg), np.array(tau)), M, T_n, (u, w)


def n_pred(tau_sorted, T):
    """The derived parameter-free law: the enumerated ladder count (no coefficient)."""
    return int(np.searchsorted(tau_sorted, T, side="right"))


def convexity_check(a_w_data, T_n):
    """Pre-registered mechanical check: the wedge density sum_{tau_min<T} w_i/2pi is
    nondecreasing in T (the law is convex — outside F02's no-go class)."""
    u, w = a_w_data
    tmin = TWO_PI * np.exp(u - 1.0)
    grid = np.linspace(TWO_PI, T_n, 400)
    slope = [(w[tmin <= T].sum()) / TWO_PI for T in grid]
    return all(slope[k + 1] >= slope[k] - 1e-15 for k in range(len(slope) - 1))


# ----------------------------------------------------------------------
# 2. closed-form matrix elements (mpmath, dps 35)
#    psi_{a,s,t}(u) = (2 pi s^2)^{-1/4} exp(-(u-a)^2/(4 s^2)) e^{i t u}
# ----------------------------------------------------------------------
def _pair(a1, s1, t1, a2, s2, t2):
    """Exact closed forms: returns (S, D, Q) = (<p1,p2>, <p1,D p2>, <p1,D^2 p2>) as mpc."""
    a1, s1, t1, a2, s2, t2 = map(mp.mpf, (a1, s1, t1, a2, s2, t2))
    al, be = 1 / (4 * s1 * s1), 1 / (4 * s2 * s2)
    ga = al + be
    dt = t2 - t1
    ubar = (al * a1 + be * a2) / ga
    pref = (2 * mp.pi * s1 * s1) ** mp.mpf("-0.25") \
         * (2 * mp.pi * s2 * s2) ** mp.mpf("-0.25") * mp.sqrt(mp.pi / ga)
    E = mp.exp(-al * be * (a1 - a2) ** 2 / ga - dt * dt / (4 * ga) + 1j * dt * ubar)
    S = pref * E
    m1 = ubar + 1j * dt / (2 * ga)                 # complex first moment <u>
    m2 = m1 * m1 + 1 / (2 * ga)                    # complex second moment <u^2>
    D = S * (t2 + 1j * (m1 - a2) / (2 * s2 * s2))
    Q = S * (1 / (2 * s2 * s2) + t2 * t2
             + 1j * t2 * (m1 - a2) / (s2 * s2)
             - (m2 - 2 * a2 * m1 + a2 * a2) / (4 * s2 ** 4))
    return S, D, Q


def _pref_expo(a1, s1, t1, a2, s2, t2):
    """Float prefilter: the (positive) Gaussian exponent of |<p1,p2>|."""
    al, be = 1 / (4 * s1 ** 2), 1 / (4 * s2 ** 2)
    ga = al + be
    return al * be * (a1 - a2) ** 2 / ga + (t2 - t1) ** 2 / (4 * ga)


def _block(a, sg, tau, mirror):
    """Assemble S/D/Q matrices for pairs (psi_k, psi_l) [mirror=False] or
    (psi_k, J psi_l) = (psi_k, psi_{-a_l, s_l, -t_l}) [mirror=True], with the float
    prefilter and Hermitian/anti-Hermitian fill (D J is anti-Hermitian; S, Q, D, SJ, QJ
    Hermitian)."""
    N = len(a)
    a2 = -a if mirror else a
    t2 = -tau if mirror else tau
    al = 1 / (4 * sg ** 2)
    ga = al[:, None] + al[None, :]
    expo = (al[:, None] * al[None, :] / ga) * (a[:, None] - a2[None, :]) ** 2 \
         + (t2[None, :] - tau[:, None]) ** 2 / (4 * ga)
    S = np.zeros((N, N), complex); D = np.zeros((N, N), complex)
    Q = np.zeros((N, N), complex)
    idx = np.argwhere(expo < EXP_CUT)
    for k, l in idx:
        if l < k:
            continue                               # fill lower triangle by symmetry
        Sv, Dv, Qv = _pair(a[k], sg[k], tau[k], a2[l], sg[l], t2[l])
        S[k, l] = complex(Sv); D[k, l] = complex(Dv); Q[k, l] = complex(Qv)
        if l > k:
            S[l, k] = np.conj(S[k, l])
            Q[l, k] = np.conj(Q[k, l])
            D[l, k] = -np.conj(D[k, l]) if mirror else np.conj(D[k, l])
    return S, D, Q


def build_stage(n, verbose=True):
    (a, sg, tau), M, T_n, sites = wedge_modes(n)
    N = len(a)
    S1, D1, Q1 = _block(a, sg, tau, mirror=False)
    S2, D2, Q2 = _block(a, sg, tau, mirror=True)
    Se, So = 2 * (S1 + S2), 2 * (S1 - S2)          # Gram, even/odd parity blocks
    K = 2 * (D1 - D2)                              # graded block <e_k, D o_l>
    Qe, Qo = 2 * (Q1 + Q2), 2 * (Q1 - Q2)          # D^2 blocks
    if verbose:
        print(f"  [W1] n={n:2d}  M_n={M:6d}  T_n={T_n:9.2f}  #sites(active)="
              f"{len(np.unique(a)):5d}  modes N={N:5d}  dim V_n={2 * N:5d}")
    return dict(n=n, M=M, T_n=T_n, a=a, sg=sg, tau=np.sort(tau), sites=sites,
                Se=Se, So=So, K=K, Qe=Qe, Qo=Qo)


def stage_spectrum(st):
    """Whiten each parity block, SVD the graded block: spectrum = {+/- s_i} exactly (E1)."""
    out, X = {}, {}
    for tag, S in (("+", st["Se"]), ("-", st["So"])):
        w, U = np.linalg.eigh(S)
        keep = w > DROP_TOL * w.max()
        X[tag] = U[:, keep] / np.sqrt(w[keep])
        out["rank" + tag] = int(keep.sum()); out["drop" + tag] = int((~keep).sum())
    assert out["rank+"] > 0 and out["rank-"] > 0, "non-vacuity guard: empty parity block"
    Kt = X["+"].conj().T @ st["K"] @ X["-"]
    assert np.abs(Kt).sum() > 0, "non-vacuity guard: H == 0"
    s = np.linalg.svd(Kt, compute_uv=False)
    out["tr_H2"] = 2 * float((s ** 2).sum())
    out["tr_PD2P"] = float(np.real(np.trace(X["+"].conj().T @ st["Qe"] @ X["+"])
                                   + np.trace(X["-"].conj().T @ st["Qo"] @ X["-"])))
    out.update(s=np.sort(s)[::-1], Kt=Kt)
    out["dim"] = out["rank+"] + out["rank-"]
    out["ker"] = out["dim"] - 2 * int((s > 1e-10 * s.max()).sum())
    return out


# ----------------------------------------------------------------------
# 3. self-test: closed forms vs direct mpmath quadrature (dps 35)
# ----------------------------------------------------------------------
def psi_fun(a, s, t, x):
    a, s, t = mp.mpf(a), mp.mpf(s), mp.mpf(t)
    return ((2 * mp.pi * s * s) ** mp.mpf("-0.25")
            * mp.exp(-(x - a) ** 2 / (4 * s * s) + 1j * t * x))


def selftest():
    print("=" * 78)
    print("W1 SELF-TEST — closed-form matrix elements vs mpmath.quad (dps 35)")
    print("=" * 78)
    probes = [(0.7, 0.25, 3.0, 1.1, 0.30, 5.5),
              (0.0, 0.35, 2.3, 0.69, 0.27, 9.1),
              (2.1, 0.05, 40.0, 2.2, 0.08, 43.0),
              (0.9, 0.15, 7.0, -1.25, 0.30, -6.0)]      # incl. a mirrored pair
    worst = {"S": 0, "D": 0, "Q": 0, "H": 0}
    for (a1, s1, t1, a2, s2, t2) in probes:
        pts = sorted([-30, a1, a2, 30])
        S, D, Q = _pair(a1, s1, t1, a2, s2, t2)
        f = lambda x: mp.conj(psi_fun(a1, s1, t1, x)) * psi_fun(a2, s2, t2, x)
        worst["S"] = max(worst["S"], abs(S - mp.quad(f, pts)))
        fD = lambda x: mp.conj(psi_fun(a1, s1, t1, x)) \
            * (-1j) * mp.diff(lambda y: psi_fun(a2, s2, t2, y), x)
        worst["D"] = max(worst["D"], abs(D - mp.quad(fD, pts)))
        fQ = lambda x: (mp.conj(mp.diff(lambda y: psi_fun(a1, s1, t1, y), x))
                        * mp.diff(lambda y: psi_fun(a2, s2, t2, y), x))
        worst["Q"] = max(worst["Q"], abs(Q - mp.quad(fQ, pts)))
        Dba = _pair(a2, s2, t2, a1, s1, t1)[1]           # Hermiticity of D
        worst["H"] = max(worst["H"], abs(D - mp.conj(Dba)))
    for k, v in worst.items():
        print(f"  max |closed-form - quad|  {k:>2}: {mp.nstr(v, 3)}")
        assert v < mp.mpf("1e-25"), f"self-test failure in {k}"

    # assembled miniature stage: every entry of Se/So/K vs direct quadrature
    a = np.array([0.0, 0.69, 1.10])
    sg = np.array([0.30, 0.25, 0.20])
    tau = np.array([2.5, 6.0, 11.0])
    S1, D1, _ = _block(a, sg, tau, mirror=False)
    S2, D2, _ = _block(a, sg, tau, mirror=True)
    Se, So, K = 2 * (S1 + S2), 2 * (S1 - S2), 2 * (D1 - D2)
    ev = [lambda x, k=k: psi_fun(a[k], sg[k], tau[k], x)
          + psi_fun(-a[k], sg[k], -tau[k], x) for k in range(3)]
    od = [lambda x, k=k: psi_fun(a[k], sg[k], tau[k], x)
          - psi_fun(-a[k], sg[k], -tau[k], x) for k in range(3)]
    pts = sorted([-30.0] + list(a) + list(-a) + [30.0])
    eS = eK = 0.0
    for i in range(3):
        for j in range(3):
            qe = mp.quad(lambda x: mp.conj(ev[i](x)) * ev[j](x), pts)
            qo = mp.quad(lambda x: mp.conj(od[i](x)) * od[j](x), pts)
            eS = max(eS, abs(Se[i, j] - complex(qe)), abs(So[i, j] - complex(qo)))
            qk = mp.quad(lambda x: mp.conj(ev[i](x))
                         * (-1j) * mp.diff(lambda y: od[j](y), x), pts)
            eK = max(eK, abs(K[i, j] - complex(qk)))
    print(f"  assembled miniature stage:  max|S - quad| = {eS:.3e}   "
          f"max|K - quad| = {eK:.3e}")
    assert eS < 1e-12 and eK < 1e-12, "assembled-entry self-test failure"
    print("  self-test PASSED")


def precision_report():
    """float64 pipeline vs full-mpmath complex SVD on the n=4 stage (dps 35)."""
    print("=" * 78)
    print("PRECISION — float64 singular values vs mpmath svd_c (dps 35), stage n=4")
    print("=" * 78)
    st = build_stage(4, verbose=False)
    sp = stage_spectrum(st)
    Kt = sp["Kt"]
    s64 = np.sort(np.linalg.svd(Kt, compute_uv=False))[::-1]
    A = mp.matrix(Kt.shape[0], Kt.shape[1])
    for i in range(Kt.shape[0]):
        for j in range(Kt.shape[1]):
            A[i, j] = mp.mpc(Kt[i, j])
    smp = mp.svd_c(A, compute_uv=False)
    smp = np.sort(np.array([float(x) for x in smp]))[::-1]
    rel = np.max(np.abs(s64 - smp[: len(s64)]) / smp[0])
    print(f"  n=4: dim={sp['dim']}, max relative singular-value difference = {rel:.3e}")
    assert rel < 1e-12


# ----------------------------------------------------------------------
# 4. reports
# ----------------------------------------------------------------------
def primary_report(stages=(4, 6, 8, 10, 12)):
    print("=" * 78)
    print("E0b — PRIMARY  H^{G,w}_n = P_n D P_n  (W1: wedge ladders on the sieve sites)")
    print("=" * 78)
    devs, profiles = [], {}
    for n in stages:
        st = build_stage(n)
        cx = convexity_check(st["sites"], st["T_n"])
        sp = stage_spectrum(st)
        d, T_lo, T_w, dev, prof = e0.e0_metric(sp["s"])
        devs.append(dev)
        profiles[n] = (st, sp, prof, (d, T_lo, T_w))
        pred_dev = max(abs(np.searchsorted(np.sort(sp["s"]), T, side="right")
                           - n_pred(st["tau"], T)) for T in prof[0]) / d
        print(f"       dim={sp['dim']:5d} (dropped {sp['drop+'] + sp['drop-']:3d} redundant)"
              f"  ker={sp['ker']:3d}  d_n={d:5d}  trH^2/trPD2P={sp['tr_H2']/sp['tr_PD2P']:.4f}"
              f"  convex={cx}")
        print(f"       window=[{T_lo:8.2f},{T_w:9.2f}]  dev={dev:10.3f}"
              f"   |N+ - N_pred|/d (derived law) = {pred_dev:.3f}")
        assert cx, "convexity check failed — design error, not a gate result"
        assert sp["tr_H2"] <= sp["tr_PD2P"] * (1 + 1e-10), "compression trace inequality"
    n_last = stages[-1]
    st, sp, (grid, ratio), _ = profiles[n_last]
    print(f"\n  ratio profile N+(T)/R(T) at n={n_last} (sampled over the derived window):")
    for k in np.linspace(0, len(grid) - 1, 8).astype(int):
        print(f"    T = {grid[k]:9.2f}   N+/R = {ratio[k]:9.3f}")
    print(f"\n  dev sequence over stages {stages}:  "
          + "  ".join(f"{v:.3f}" for v in devs))
    ok = e0.verdict(devs)
    print(f"  E0b PRIMARY: {'PASS' if ok else 'FAIL'} "
          f"(pre-registered: last-3 strictly decreasing AND final <= 0.05)")
    return devs, ok, profiles


if __name__ == "__main__":
    fast = "fast" in sys.argv
    selftest()
    e0.regression()
    precision_report()
    stages = (4, 6, 8, 10) if fast else (4, 6, 8, 10, 12)
    devs, ok, profiles = primary_report(stages)
    d_ref = profiles[stages[-1]][3][0]
    all_fail, pos_ok = e0.controls_report(d_ref)
    print("=" * 78)
    print("VERDICT (mechanical application of the pre-registered rule)")
    print("=" * 78)
    print(f"  harness valid:            {pos_ok and all_fail}  "
          f"(positive control passes: {pos_ok}; all must-fail controls fail: {all_fail})")
    print(f"  E0b, primary H^{{G,w}}_n:   {'PASS' if ok else 'FAIL'}")
    if ok:
        print("  -> O6 (pre-registered): a PASS is NOT evidence about zeros; it certifies")
        print("     the redesign repaired the killed component and REOPENS the E-track")
        print("     (WP03-WP05 unpause; WP04 first, per the F02 ordering note).")
    else:
        print("  -> WP02b falsifier: consult the pre-registered branches (ladder-tracking")
        print("     vs not); the E-track stays paused; the bar does not move post hoc.")
