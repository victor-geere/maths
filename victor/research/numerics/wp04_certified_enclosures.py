"""wp04_certified_enclosures.py — PSC2-WP04 (E3b): certified enclosures from the
second-order relative spectrum of the pencil (P_n D P_n, P_n D^2 P_n) on the W1 family.

THE OBJECT.  The second-order relative spectrum of the ambient D = -i d/du on
L^2(R, du) (S03 Lemma 1.1 normal form) relative to the W1 wedge stage spaces V_n of
PSC2-WP02b / F07, computed from the delivered pencil matrices:
    z in spec2(D, V_n)  iff  det( Q - 2 z B + z^2 S ) = 0  on V_n,
with S the Gram matrix, B_ij = <v_i, D v_j>, Q_ij = <v_i, D^2 v_j> = <D v_i, D v_j>
(exact closed forms at dps 35, imported unchanged from wp02b_rewindow).

THE THEOREM (imported, classical — proven).  Shargorodsky 2000 (geometry of higher-
order relative spectra and projection methods); Levitin–Shargorodsky 2004 (spectral
pollution and second-order relative spectra of self-adjoint operators); refinements
Boulton–Levitin 2007, Boulton–Strauss 2011; survey Davies–Plum 2004.  For self-adjoint
A and ANY finite-dimensional trial space L:
    z in spec2(A, L)   ==>   spec(A) n [Re z - |Im z|, Re z + |Im z|]  !=  empty,
with no norm-resolvent hypothesis: the enclosure is pollution-free BY THEOREM.
Exact quasi-mode identity (one line): if z = x + i y, y != 0, solves the pencil with
eigenvector u in V_n, then testing P_n (D - z)^2 u = 0 against u itself gives
    <u, (D - x) u> = 0   and   || (D - x) u || = |y| * ||u||     (exactly).

HONESTY CLAUSE (binding on the interpretation; stated before the run).  On THIS
ambient spec(D) = R (purely a.c., Lemma 1.1), so the interval statement is trivially
true and nothing is discovered about spec(D).  What the run certifies is
  (i)  the enclosure machinery itself, validated against closed forms, mpmath.eig and
       independent quadrature, and
  (ii) the radii |Im z| = certified resolution of the W1 family: each matched pencil
       root exhibits a normalised quasi-mode u in V_n with ||(D - Re z) u|| = |Im z|.
The radii and their stage genealogy are the deliverable (feeds WP05 / HS7).
O6 binds: NOTHING here is evidence about zeros; the arithmetic content of the E-track
is decided at E4b / WP05.

CROSS-SCIENCE NOTE (cite in the finding).  Second-order relative spectra were built
to kill spectral pollution for compressed Dirac operators in relativistic quantum
chemistry (Levitin–Shargorodsky 2004; Boulton–Boussaid 2010 for Dirac); we reuse the
technology on the adelic Dirac normal form.

PRE-REGISTERED CRITERIA (fixed before the run; operationalising the WP04 bar,
which does not move):
  * Certified intervals: for each positive stage eigenvalue s_i <= 50 of H^{G,w}_n,
    take the pencil root z minimising |z - s_i|; the certified interval is
    [Re z - |Im z|, Re z + |Im z|], radius r_i = |Im z|.
  * Stage statistic rho_n := median r_i over the matched intervals on [0, 50].
  * PASS iff rho_n is strictly decreasing over >= 3 consecutive computed stages
    (the WP's "radii decreasing in n over at least three consecutive stages on the
    window [0, 50]"); the last-three behaviour is reported as context.
  * FALSIFIER (stagnation): no such run of three stages, while E0b stands passed
    (F07) — the compression sees the right density but cannot localise; report the
    per-band medians (bands [0,15), [15,30), [30,50]) as the obstruction fingerprint
    (the WP points at the archimedean window's band-limit dual as the bottleneck).
  * Stages n = 4, 6, 8, 10, 12 (the E0b stages).  Fallback fixed in advance: if the
    n = 12 companion eigenproblem exceeds the compute budget ('fast' flag), the run
    reports n = 4..10 and the criterion applies to the computed stages unchanged.
  * Controls (identical code path — solver, matching, median, verdict):
      must-FAIL  (a) fixed-basis decoy: the n = 4 W1 pencil presented as four
                     successive stages (radii cannot decrease);
      must-FAIL  (b) constant-radius synthetic pencil Q = B^2 + c^2 I, c = 0.8 at
                     every stage (radii identically c);
      must-PASS  (c) shrinking-radius synthetic pencil, c_n = 2 / log M_n (radii
                     identically c_n, strictly decreasing).
    Any control misbehaving invalidates the run (harness artifact, not a finding).
  * Validity guards (run-invalid if violated; not the gate):
      - n = 4 matched-interval centres and radii from mpmath.eig (dps 35) companion
        eigenvalues agree with float64 to <= 1e-8 * T_4 (all-root max distance is
        reported as information only);
      - single-coherent-state closed form z = tau +/- i/(2 sigma) reproduced to
        1e-12 relative;
      - Rayleigh consistency z = beta + i sqrt(q - beta^2), beta = u*Bu, q = u*Qu,
        spot-checked on 3 matched roots per stage for n <= 10, <= 1e-6 * T_n;
      - final-evaluation truth cross-check (I0.6): independent dense-grid quadrature
        of ||(D - Re z) u|| vs |Im z| * ||u|| on the 3 sampled matched roots at
        n = 4, relative tolerance 1e-6 (truth = direct numerical integration of the
        assembled coherent-state sum, independent of the closed-form matrix elements);
      - operator inequalities at every stage: Q - B^2 >= 0 (Cauchy-Schwarz for the
        compression) and tr H^2 <= tr P D^2 P;  non-vacuity: ranks > 0, >= 12 matched
        intervals per stage.
  * Regression (I0.5): e0_density_gate.regression() N00 anchors, then the F07 E0b
    anchors at n = 4, 6 (dev = 0.118, 0.104; dim = 44, 164; trH^2/trPD2P = 0.9899,
    0.9959) reproduced through the F07 code path before any new number counts.
  * No gamma-list anywhere outside the N00 regression line (I0.6); no fitted
    parameter; the reported rate fit rho_n ~ C (log M_n)^(-alpha) is report-only.

Deterministic (no RNG).  Run:  python wp04_certified_enclosures.py  [fast]
"""

import sys
import time
from math import log, sqrt

import numpy as np
import mpmath as mp

import e0_density_gate as e0           # N00 regression harness (I0.5)
import wp02b_rewindow as w1            # W1 builder: closed forms, blocks, self-test

mp.mp.dps = 35

WINDOW = 50.0                          # the WP04 window [0, 50]
BANDS = (0.0, 15.0, 30.0, 50.0)        # obstruction-fingerprint bands (pre-registered)
STAGES_FULL = (4, 6, 8, 10, 12)
STAGES_FAST = (4, 6, 8, 10)


# ----------------------------------------------------------------------
# 1. stage build (aligned mode data) and pencil assembly
# ----------------------------------------------------------------------
def build_w1_stage(n):
    """w1.build_stage with the (a, sigma, tau) mode arrays kept ALIGNED (build_stage
    sorts tau for the ladder law; the pencil eigenvectors need the aligned order)."""
    (a, sg, tau), M, T_n, sites = w1.wedge_modes(n)
    S1, D1, Q1 = w1._block(a, sg, tau, mirror=False)
    S2, D2, Q2 = w1._block(a, sg, tau, mirror=True)
    return dict(n=n, M=M, T_n=T_n, a=a, sg=sg, tau=tau, sites=sites,
                Se=2 * (S1 + S2), So=2 * (S1 - S2), K=2 * (D1 - D2),
                Qe=2 * (Q1 + Q2), Qo=2 * (Q1 - Q2))


def _whiten(S):
    w, U = np.linalg.eigh(S)
    keep = w > w1.DROP_TOL * w.max()
    return U[:, keep] / np.sqrt(w[keep]), int((~keep).sum())


def build_pencil(st):
    """Whitened pencil (B, Q) on V_n (Gram -> I), stage spectrum {+/- s_i}, and the
    whitening maps for eigenvector reconstruction."""
    Xe, drop_e = _whiten(st["Se"])
    Xo, drop_o = _whiten(st["So"])
    Kt = Xe.conj().T @ st["K"] @ Xo
    Qe = Xe.conj().T @ st["Qe"] @ Xe
    Qo = Xo.conj().T @ st["Qo"] @ Xo
    ne, no = Kt.shape
    assert ne > 0 and no > 0, "non-vacuity guard: empty parity block"
    assert np.abs(Kt).sum() > 0, "non-vacuity guard: H == 0"
    d = ne + no
    B = np.zeros((d, d), complex)
    Q = np.zeros((d, d), complex)
    B[:ne, ne:] = Kt
    B[ne:, :ne] = Kt.conj().T
    Q[:ne, :ne] = Qe
    Q[ne:, ne:] = Qo
    B = (B + B.conj().T) / 2
    Q = (Q + Q.conj().T) / 2
    s = np.sort(np.linalg.svd(Kt, compute_uv=False))
    return B, Q, (Xe, Xo, ne, no), s, drop_e + drop_o


def second_order_roots(B, Q, scale):
    """spec2 via the companion linearisation of w^2 I - 2 w (B/scale) + Q/scale^2,
    z = scale * w (scale = T_n, derived — keeps the companion well-balanced)."""
    d = B.shape[0]
    C = np.zeros((2 * d, 2 * d), complex)
    C[:d, :d] = 2 * B / scale
    C[:d, d:] = -Q / scale ** 2
    C[d:, :d] = np.eye(d)
    return scale * np.linalg.eigvals(C)


# ----------------------------------------------------------------------
# 2. matching, metric, verdict (pre-registered)
# ----------------------------------------------------------------------
def certified_intervals(s_pos, roots, window=WINDOW):
    """For each positive stage eigenvalue s <= window: nearest pencil root, interval
    [Re z - |Im z|, Re z + |Im z|].  Returns rows (s, centre, radius, root_index)."""
    rows = []
    for s in s_pos[(s_pos > 0) & (s_pos <= window)]:
        j = int(np.argmin(np.abs(roots - s)))
        z = roots[j]
        rows.append((float(s), float(z.real), float(abs(z.imag)), j))
    return rows


def band_medians(rows):
    out = []
    for lo, hi in zip(BANDS[:-1], BANDS[1:]):
        r = [rr[2] for rr in rows if lo <= rr[0] < hi]
        out.append(float(np.median(r)) if r else float("nan"))
    return out


def has_decreasing_run(rhos, k=3):
    """True iff rho is strictly decreasing over >= k consecutive stages."""
    run = best = 1
    for i in range(1, len(rhos)):
        run = run + 1 if rhos[i] < rhos[i - 1] else 1
        best = max(best, run)
    return best >= k


# ----------------------------------------------------------------------
# 3. validity guards: Rayleigh consistency and independent quadrature
# ----------------------------------------------------------------------
def pencil_eigvec(B, Q, z):
    """Eigenvector of the quadratic pencil at root z: smallest eigenvector of M^H M,
    M = Q - 2 z B + z^2 I."""
    d = B.shape[0]
    M = Q - 2 * z * B + (z * z) * np.eye(d)
    w, U = np.linalg.eigh(M.conj().T @ M)
    return U[:, 0]


def rayleigh_check(B, Q, roots, rows, T_n):
    """z = beta + i sqrt(q - beta^2) with beta = u*Bu, q = u*Qu — exact for the true
    eigenpair; spot-checked on 3 matched roots (low / mid / high)."""
    worst = 0.0
    picks = [rows[0], rows[len(rows) // 2], rows[-1]]
    vecs = []
    for (_s, _c, _r, j) in picks:
        z = roots[j]
        if z.imag < 0:
            z = z.conjugate()
        u = pencil_eigvec(B, Q, z)
        beta = (u.conj() @ B @ u).real
        q = (u.conj() @ Q @ u).real
        zp = beta + 1j * sqrt(max(q - beta * beta, 0.0))
        worst = max(worst, abs(zp - z) / T_n)
        vecs.append((z, u))
    return worst, vecs


def quadrature_check(st, maps, zu_pairs):
    """FINAL-EVALUATION truth cross-check (I0.6): rebuild u(x) as an explicit
    coherent-state sum and verify ||(D - Re z) u|| = |Im z| ||u|| by dense-grid
    quadrature (independent of the closed-form matrix elements).  n = 4 only."""
    Xe, Xo, ne, no = maps
    a, sg, tau = st["a"], st["sg"], st["tau"]
    h = 2.5e-4
    x = np.arange(-10.0, 10.0 + h, h)
    worst = 0.0
    for z, u in zu_pairs:
        ce = Xe @ u[:ne]
        co = Xo @ u[ne:]
        A = np.concatenate([a, -a, a, -a])
        SG = np.concatenate([sg, sg, sg, sg])
        TAU = np.concatenate([tau, -tau, tau, -tau])
        C = np.concatenate([ce, ce, co, -co])
        pref = (2 * np.pi * SG ** 2) ** -0.25
        psi = (C * pref)[:, None] * np.exp(
            -(x[None, :] - A[:, None]) ** 2 / (4 * SG[:, None] ** 2)
            + 1j * TAU[:, None] * x[None, :])
        ufun = psi.sum(axis=0)
        dufun = (psi * (-(x[None, :] - A[:, None]) / (2 * SG[:, None] ** 2)
                        + 1j * TAU[:, None])).sum(axis=0)
        res2 = h * (np.abs(-1j * dufun - z.real * ufun) ** 2).sum()
        nrm2 = h * (np.abs(ufun) ** 2).sum()
        ratio = sqrt(res2 / nrm2)
        worst = max(worst, abs(ratio - abs(z.imag)) / abs(z.imag))
    return worst


# ----------------------------------------------------------------------
# 4. certification at n = 4: mpmath.eig + single-coherent-state closed form
# ----------------------------------------------------------------------
def certification(st4, B, Q, s_pos):
    print("=" * 78)
    print("CERTIFICATION — n=4 pencil vs mpmath.eig (dps 35); single-state closed form")
    print("=" * 78)
    T4 = st4["T_n"]
    roots64 = second_order_roots(B, Q, T4)
    rows64 = certified_intervals(s_pos, roots64)

    d = B.shape[0]
    C = np.zeros((2 * d, 2 * d), complex)
    C[:d, :d] = 2 * B / T4
    C[:d, d:] = -Q / T4 ** 2
    C[d:, :d] = np.eye(d)
    Cm = mp.matrix(2 * d, 2 * d)
    for i in range(2 * d):
        for j in range(2 * d):
            Cm[i, j] = mp.mpc(C[i, j])
    E = mp.eig(Cm, left=False, right=False)
    if isinstance(E, tuple):
        E = E[0]
    roots_mp = np.array([complex(w) * T4 for w in E])
    rows_mp = certified_intervals(s_pos, roots_mp)
    dc = max(abs(r64[1] - rmp[1]) for r64, rmp in zip(rows64, rows_mp))
    dr = max(abs(r64[2] - rmp[2]) for r64, rmp in zip(rows64, rows_mp))
    dall = max(np.min(np.abs(roots_mp - z)) for z in roots64)
    print(f"  matched intervals (float64 vs mp.eig): max |d centre| = {dc:.3e}   "
          f"max |d radius| = {dr:.3e}   [guard 1e-8*T_4 = {1e-8 * T4:.1e}]")
    print(f"  all-roots max min-distance = {dall:.3e}  (information only)")
    assert dc <= 1e-8 * T4 and dr <= 1e-8 * T4, "mp.eig certification failed"

    # single coherent state: pencil root z = tau +/- i/(2 sigma), radius 1/(2 sigma)
    a0, s0, t0 = 0.9, 0.31, 17.0
    Sv, Dv, Qv = w1._pair(a0, s0, t0, a0, s0, t0)
    b1 = np.array([[complex(Dv / Sv)]])
    q1 = np.array([[complex(Qv / Sv)]])
    z1 = second_order_roots(b1, q1, max(t0, 1.0))
    z1 = z1[np.argmax(z1.imag)]
    rel = abs(z1 - (t0 + 1j / (2 * s0))) / abs(t0 + 1j / (2 * s0))
    print(f"  single coherent state (a={a0}, sigma={s0}, tau={t0}): root = "
          f"{z1.real:.12f} + {z1.imag:.12f} i   vs   tau + i/(2 sigma) "
          f"(radius {1 / (2 * s0):.12f});  rel diff = {rel:.3e}")
    assert rel < 1e-12, "single-state closed-form certification failed"
    print("  certification PASSED")


# ----------------------------------------------------------------------
# 5. regression (I0.5): N00 anchors + F07 E0b anchors through the F07 code path
# ----------------------------------------------------------------------
def w1_regression():
    print("=" * 78)
    print("REGRESSION (I0.5, continued) — F07 E0b anchors reproduced (W1 code path)")
    print("=" * 78)
    targets = {4: (0.118, 44, 0.9899), 6: (0.104, 164, 0.9959)}
    ok = True
    for n, (dev_t, dim_t, tr_t) in targets.items():
        st = w1.build_stage(n, verbose=False)
        sp = w1.stage_spectrum(st)
        _, _, _, dev, _ = e0.e0_metric(sp["s"])
        tr = sp["tr_H2"] / sp["tr_PD2P"]
        print(f"  n={n}: dev = {dev:.3f}  dim = {sp['dim']}  trH^2/trPD2P = {tr:.4f}"
              f"   [F07: {dev_t:.3f}, {dim_t}, {tr_t:.4f}]")
        ok &= (abs(dev - dev_t) < 5e-4 and sp["dim"] == dim_t and abs(tr - tr_t) < 2e-4)
    print(f"  W1 regression {'PASSED' if ok else '** FAILED — STOP: reportable finding **'}")
    assert ok


# ----------------------------------------------------------------------
# 6. the primary run
# ----------------------------------------------------------------------
def stage_enclosures(n, do_quad=False):
    t0 = time.time()
    st = build_w1_stage(n)
    B, Q, maps, s_pos, dropped = build_pencil(st)
    d = B.shape[0]
    T_n = st["T_n"]

    # operator inequalities (guards, not the gate)
    wQ = np.linalg.eigvalsh(Q - B @ B)
    assert wQ.min() > -1e-7 * np.abs(Q).max(), "Q - B^2 >= 0 violated"
    trH2 = 2 * float((s_pos ** 2).sum())
    trQ = float(np.trace(Q).real)
    assert trH2 <= trQ * (1 + 1e-10), "compression trace inequality violated"

    roots = second_order_roots(B, Q, T_n)
    rows = certified_intervals(s_pos, roots)
    assert len(rows) >= 12, "non-vacuity guard: too few matched intervals"
    radii = np.array([r[2] for r in rows])
    rho = float(np.median(radii))
    bands = band_medians(rows)
    n_distinct = len({r[3] for r in rows})

    ray_worst, vecs = (rayleigh_check(B, Q, roots, rows, T_n)
                       if n <= 10 else (float("nan"), []))
    bench = float(np.min(1.0 / (2.0 * st["sg"][st["tau"] <= WINDOW + 5])))

    print(f"  [W1] n={n:2d}  M_n={st['M']:6d}  T_n={T_n:9.2f}  dim={d:5d} "
          f"(dropped {dropped:3d})  pencil roots={2 * d:5d}  "
          f"matched(<= {WINDOW:.0f})={len(rows):3d} (distinct {n_distinct:3d})")
    print(f"       radii: min={radii.min():7.4f}  median={rho:7.4f}  "
          f"max={radii.max():7.4f}   bands [0,15|15,30|30,50] = "
          f"{bands[0]:7.4f} {bands[1]:7.4f} {bands[2]:7.4f}")
    extra = f"rayleigh(3 roots) = {ray_worst:.2e}   " if n <= 10 else ""
    print(f"       {extra}single-state benchmark = {bench:.4f}   "
          f"trH^2/trPD2P = {trH2 / trQ:.4f}   [{time.time() - t0:7.1f}s]")
    if n <= 10:
        assert ray_worst <= 1e-6, "Rayleigh consistency guard failed"

    if do_quad:
        qworst = quadrature_check(st, maps, vecs)
        print(f"       FINAL-EVALUATION truth check (I0.6, independent quadrature): "
              f"max rel |quad - |Im z|| = {qworst:.3e}  [guard 1e-6]")
        assert qworst <= 1e-6, "quadrature truth check failed"

    return dict(n=n, M=st["M"], T_n=T_n, rows=rows, rho=rho, bands=bands,
                st4=(st, B, Q, s_pos) if n == 4 else None)


def genealogy(results):
    print(f"\n  genealogy of certified intervals on [0, {WINDOW:.0f}] "
          f"(rows: k-th positive stage eigenvalue; entries: radius |Im z|):")
    K = max(len(r["rows"]) for r in results)
    hdr = "    k " + "".join(f"   n={r['n']:>2d}   " for r in results)
    print(hdr)
    for k in range(K):
        line = f"  {k + 1:3d} "
        for r in results:
            line += f" {r['rows'][k][2]:8.4f} " if k < len(r["rows"]) else "     -    "
        print(line)
    last = results[-1]
    print(f"\n  certified intervals at n={last['n']} (centre +/- radius; every one "
          f"intersects spec(D) by theorem — trivially true on this ambient):")
    for k, (s, c, r, _j) in enumerate(last["rows"]):
        print(f"    k={k + 1:2d}  s={s:8.3f}   [{c - r:9.3f}, {c + r:9.3f}]"
              f"   centre={c:8.3f}  radius={r:7.4f}")


def rate_report(results):
    rhos = [r["rho"] for r in results]
    Ms = [r["M"] for r in results]
    print(f"\n  rho (median radius) sequence over stages "
          f"{tuple(r['n'] for r in results)}:  "
          + "  ".join(f"{v:.4f}" for v in rhos))
    rat = [rhos[i + 1] / rhos[i] for i in range(len(rhos) - 1)]
    print("  successive ratios rho_{k+1}/rho_k:  "
          + "  ".join(f"{v:.3f}" for v in rat))
    al = np.polyfit(np.log(np.log(np.array(Ms, float))), np.log(rhos), 1)[0]
    print(f"  report-only rate fit  rho_n ~ C (log M_n)^(-alpha):  alpha = {-al:.2f}")
    return rhos


# ----------------------------------------------------------------------
# 7. controls (identical code path: solver -> matching -> median -> verdict)
# ----------------------------------------------------------------------
def _synthetic_rho(c):
    centres = np.arange(0.5, 60.0, 1.0)
    Bs = np.diag(centres).astype(complex)
    Qs = Bs @ Bs + (c ** 2) * np.eye(len(centres))
    roots = second_order_roots(Bs, Qs, 60.0)
    rows = certified_intervals(centres, roots)
    return float(np.median([r[2] for r in rows]))


def controls_report(st4pack, n_stages):
    print("=" * 78)
    print("E3b — CONTROLS (must-fail: fixed-basis decoy, constant-radius synthetic; "
          "must-pass: shrinking-radius synthetic)")
    print("=" * 78)
    st, B, Q, s_pos = st4pack
    fixed = []
    for _k in range(4):                     # the n=4 pencil as four fake stages
        roots = second_order_roots(B, Q, st["T_n"])
        rows = certified_intervals(s_pos, roots)
        fixed.append(float(np.median([r[2] for r in rows])))
    fixed_pass = has_decreasing_run(fixed)
    print(f"  fixed-basis decoy    rho = {'  '.join(f'{v:.4f}' for v in fixed)}"
          f"   -> {'** PASSES — HARNESS BROKEN **' if fixed_pass else 'FAILS [as required]'}")

    const = [_synthetic_rho(0.8) for _ in n_stages]
    const_pass = has_decreasing_run(const)
    print(f"  constant-radius      rho = {'  '.join(f'{v:.4f}' for v in const)}"
          f"   -> {'** PASSES — HARNESS BROKEN **' if const_pass else 'FAILS [as required]'}")

    shrink = [_synthetic_rho(2.0 / log((1 << (n + 1)) - 1)) for n in n_stages]
    shrink_pass = has_decreasing_run(shrink)
    print(f"  shrinking-radius     rho = {'  '.join(f'{v:.4f}' for v in shrink)}"
          f"   -> {'PASSES (metric is demonstrably passable)' if shrink_pass else '** FAILS — HARNESS INVALID **'}")
    return (not fixed_pass) and (not const_pass), shrink_pass


# ----------------------------------------------------------------------
# 8. main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    fast = "fast" in sys.argv
    stages = STAGES_FAST if fast else STAGES_FULL

    w1.selftest()                       # closed-form S/D/Q validation (F07 harness)
    e0.regression()                     # N00 anchors (I0.5); gamma-list ONLY here
    w1_regression()                     # F07 E0b anchors

    print("=" * 78)
    print("E3b — CERTIFIED ENCLOSURES  pencil (P_n D P_n, P_n D^2 P_n)  [W1 family]")
    print("=" * 78)
    results = [stage_enclosures(n, do_quad=(n == 4)) for n in stages]

    st4pack = results[0]["st4"]
    certification(st4pack[0], st4pack[1], st4pack[2], st4pack[3])

    genealogy(results)
    rhos = rate_report(results)
    must_fail_ok, pos_ok = controls_report(st4pack, stages)

    ok = has_decreasing_run(rhos)
    last3 = rhos[-3:]
    last3_dec = all(last3[i + 1] < last3[i] for i in range(2))
    print("=" * 78)
    print("VERDICT (mechanical application of the pre-registered rule)")
    print("=" * 78)
    print(f"  harness valid:            {must_fail_ok and pos_ok}  "
          f"(must-fail controls fail: {must_fail_ok}; positive control passes: {pos_ok})")
    print(f"  E3b radii gate:           {'PASS' if ok else 'FAIL'} "
          f"(>= 3 consecutive stages with strictly decreasing median radius)")
    print(f"  context: last-three strictly decreasing = {last3_dec}")
    if ok:
        print("  -> Certified-resolution radii decrease across stages as required; the")
        print("     interval genealogy above is the WP05 / HS7 feed.  O6 (binding): this")
        print("     is a statement about the W1 family's resolution, NOT about zeros.")
    else:
        print("  -> WP04 falsifier (stagnation): the compression sees the right density")
        print("     (E0b passed, F07) but cannot localise on [0, 50].  Obstruction")
        print("     fingerprint = the per-band medians above; the WP points at the")
        print("     archimedean window's band-limit dual.  Prolate-pencil route promoted")
        print("     per the pre-registration; the bar does not move post hoc.")
