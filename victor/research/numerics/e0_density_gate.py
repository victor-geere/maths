"""e0_density_gate.py — N0 stage builder + gate E0 (the density gate) for PSC2-WP02.

THE OBJECT.  The sieve-Galerkin compression H^G_n = P_n D P_n of S03 §3(c), realised on
the norm coordinate of the idele class group:  ambient  L^2(R, du)  (u = log x; unitarily
equivalent to the dilation generator on L^2(R_+, dx), S03 Lemma 1.1), D = -i d/du,
J = parity (u -> -u, the s <-> 1-s symmetry), J D J^{-1} = -D exactly.

STAGE BASIS V_n (J-invariant BY CONSTRUCTION — this discharges the residual obligation of
PSC2-F01, which assumed J V_n = V_n without constructing it):
  * finite places: for each prime power q = p^k <= M_n (the sieve inventory, M_n = 2^{n+1}-1)
    a normalised Gaussian bump g_q at u = log q with width sigma_q = gap_q / 2 (half the
    distance to the nearest other inventory point — derived from the inventory, not chosen),
    symmetrised into even/odd pairs  e_q = g_q + J g_q,  o_q = g_q - J g_q;
  * archimedean place: Mellin-Hermite modes h_j, j < m_n, m_n = #{j : sqrt(2j+1) <= L_n},
    L_n = log M_n  (the phase-space disk of radius L_n; the O(L_n^2) block of S03 §4).
Matrix elements of D and D^2 are exact closed forms (Gaussian integrals + Hermite ladder
algebra), evaluated with mpmath at dps 35 and validated against direct quadrature below.
In the parity grading H^G_n is exactly off-diagonal (F01 corollary C-c), so its spectrum is
{ +/- s_i } with s_i the singular values of the graded block: E1 pairing is EXACT here.

PRE-REGISTERED CRITERIA (fixed before any run; copied into PSC2-F02 verbatim).
  Counting convention:  N+(T) := #{ lambda in spec : 0 < lambda <= T }  for +/- paired
  spectra; for the (unpaired) legacy control  N+(T) := #{ |lambda| <= T } / 2.
  Target (the WP's own denominator):  R(T) := (T/2pi) log(T/2pi).
  Derived window (bookkeeping, S03 §4 — a computation, never a fit):
      W_n := [T_lo, T_n]  with  R(T_lo) = sqrt(d_n),  R(T_n) = d_n,
      d_n := #{ positive eigenvalues of the stage } .
  Deviation metric:  dev_n := max over a 200-point geometric grid in W_n of
      | N+(T) / R(T)  -  1 | .
  E0 PASS  iff  dev_n is strictly decreasing over the last three computed stages
           AND  dev at the last stage <= 0.05.
  MUST-FAIL controls (each must NOT pass, same metric): legacy H_n' (S00 §2.3, eps = 1/||A'||);
  graph one-mode (singular values of the weighted divisor stage W, S02 §6 / F4);
  sine decoy spec = Z_{>0} (rule I0.7).
  HARNESS VALIDITY: a synthetic spectrum sampled from the smooth law itself (lambda_k with
  R(lambda_k) = k - 1/2; no gamma-list consumed) must PASS with dev decreasing in d — i.e.
  the metric is demonstrably passable; otherwise the run is invalid.
  Non-vacuity guards: dim V_n > 0, H != 0, Gram ranks > 0 (rule I0.2).
  No gamma-list, no N(T)-unfolding, no fitted parameter anywhere in the construction (I0.1/I0.6).

Deterministic (no RNG).  Run:  python e0_density_gate.py
"""

import sys
from math import pi, log, exp, sqrt, asin

import numpy as np
import mpmath as mp

import sieve_operator as so            # legacy comparator conventions (N00 §2)
import prime_graph_lab as pgl          # graph stage conventions (N00 §3); sets dps=30

mp.mp.dps = 35                          # WP02 requirement (set AFTER imports)

TWO_PI = 2 * pi


# ----------------------------------------------------------------------
# 1. sieve inventory
# ----------------------------------------------------------------------
def inventory(n):
    """Prime powers q = p^k <= M_n with their von Mangoldt data, M_n = 2^{n+1}-1."""
    M = (1 << (n + 1)) - 1
    primes = so.sieve_of_eratosthenes(M)
    Q = []
    for p in primes:
        q = int(p)
        while q <= M:
            Q.append(q)
            q *= int(p)
    Q.sort()
    return np.array(Q, dtype=np.int64), M


def bump_data(Q):
    """u_q = log q and derived widths sigma_q = gap_q/2 (nearest-neighbour half-gap)."""
    u = np.log(Q.astype(float))
    gaps = np.empty_like(u)
    if len(u) == 1:
        gaps[0] = u[0]
    else:
        d = np.diff(u)
        gaps[0] = d[0]
        gaps[-1] = d[-1]
        gaps[1:-1] = np.minimum(d[:-1], d[1:])
    return u, gaps / 2.0


# ----------------------------------------------------------------------
# 2. closed-form matrix elements (mpmath, dps 35)
#    normalised Gaussian  g_{a,s}(u) = (pi s^2)^{-1/4} exp(-(u-a)^2 / (2 s^2))
#    Hermite functions    h_j(u) = H_j(u) e^{-u^2/2} / sqrt(2^j j! sqrt(pi))
#    convention: <f, D g> = i * Rpart  with D = -i d/du and f, g real.
# ----------------------------------------------------------------------
def gg_S(a, sa, b, sb):
    """<g_a, g_b>"""
    a, sa, b, sb = map(mp.mpf, (a, sa, b, sb))
    s2 = sa * sa + sb * sb
    return mp.sqrt(2 * sa * sb / s2) * mp.exp(-(a - b) ** 2 / (2 * s2))


def gg_R(a, sa, b, sb):
    """Rpart of <g_a, D g_b>  =  (a-b)/(sa^2+sb^2) * S"""
    a, sa, b, sb = map(mp.mpf, (a, sa, b, sb))
    s2 = sa * sa + sb * sb
    return (a - b) / s2 * gg_S(a, sa, b, sb)


def gg_D2(a, sa, b, sb):
    """<g_a, D^2 g_b> = [1/s2 - (a-b)^2/s2^2] * S"""
    a, sa, b, sb = map(mp.mpf, (a, sa, b, sb))
    s2 = sa * sa + sb * sb
    return (1 / s2 - (a - b) ** 2 / s2 ** 2) * gg_S(a, sa, b, sb)


def hermite_gauss_I(jmax, a, s):
    """I_j = <h_j, g_{a,s}>, j = 0..jmax, by the exact three-term recursion
       I_{j+1} = [ a sqrt(2/(j+1)) I_j - (1-s^2) sqrt(j/(j+1)) I_{j-1} ] / (1+s^2),
       I_0 = sqrt(2s/(1+s^2)) exp(-a^2/(2(1+s^2)))."""
    a, s = mp.mpf(a), mp.mpf(s)
    s2p = 1 + s * s
    I = [mp.sqrt(2 * s / s2p) * mp.exp(-a * a / (2 * s2p))]
    if jmax >= 1:
        I.append(a * mp.sqrt(mp.mpf(2)) * I[0] / s2p)
    for j in range(1, jmax):
        nxt = (a * mp.sqrt(mp.mpf(2) / (j + 1)) * I[j]
               - (1 - s * s) * mp.sqrt(mp.mpf(j) / (j + 1)) * I[j - 1]) / s2p
        I.append(nxt)
    return I     # list of mpf, length jmax+1


def hg_R(j, I):
    """Rpart of <h_j, D g> = sqrt(j/2) I_{j-1} - sqrt((j+1)/2) I_{j+1}   (needs I up to j+1)."""
    lo = mp.sqrt(mp.mpf(j) / 2) * I[j - 1] if j >= 1 else mp.mpf(0)
    return lo - mp.sqrt(mp.mpf(j + 1) / 2) * I[j + 1]


def hg_D2(j, I):
    """<h_j, D^2 g> = (j+1/2) I_j - sqrt((j+1)(j+2))/2 I_{j+2} - sqrt(j(j-1))/2 I_{j-2}."""
    v = (j + mp.mpf(1) / 2) * I[j] - mp.sqrt(mp.mpf((j + 1) * (j + 2))) / 2 * I[j + 2]
    if j >= 2:
        v -= mp.sqrt(mp.mpf(j * (j - 1))) / 2 * I[j - 2]
    return v


# ----------------------------------------------------------------------
# 3. the N0 stage builder
#    even block:  { e_q } + { h_j : j even },   odd block:  { o_q } + { h_j : j odd }
#    returns Gram S+, S-, graded D block R (rows even, cols odd; H entry = i R),
#    and D^2 blocks for the compression-trace check.
# ----------------------------------------------------------------------
EXP_CUT = 120.0          # skip pairs whose Gaussian exponent < -EXP_CUT (< 1e-52)


def _pair_terms(u, sg):
    """Closed-form bump-bump blocks: for a,b > 0 returns dicts of the 'direct' (a,b) and
    'mirror' (a,-b) contributions to S, R, D2, with a float prefilter for negligible pairs."""
    nq = len(u)
    Sd = np.zeros((nq, nq)); Sm = np.zeros((nq, nq))
    Rd = np.zeros((nq, nq)); Rm = np.zeros((nq, nq))
    Dd = np.zeros((nq, nq)); Dm = np.zeros((nq, nq))
    s2 = sg[:, None] ** 2 + sg[None, :] ** 2
    for (dmat, Smat, Rmat, Dmat, sign) in (((u[:, None] - u[None, :]), Sd, Rd, Dd, +1),
                                           ((u[:, None] + u[None, :]), Sm, Rm, Dm, -1)):
        expo = dmat ** 2 / (2 * s2)
        idx = np.argwhere(expo < EXP_CUT)
        for i, j in idx:
            a, b = u[i], sign * u[j]
            S = gg_S(a, sg[i], b, sg[j])
            Smat[i, j] = float(S)
            Rmat[i, j] = float((mp.mpf(a) - b) / mp.mpf(s2[i, j]) * S)
            Dmat[i, j] = float((1 / mp.mpf(s2[i, j])
                                - (mp.mpf(a) - b) ** 2 / mp.mpf(s2[i, j]) ** 2) * S)
    return Sd, Sm, Rd, Rm, Dd, Dm


def build_stage(n, verbose=True):
    Q, M = inventory(n)
    u, sg = bump_data(Q)
    nq = len(Q)
    L = log(M)
    m = len([j for j in range(4 * int(L * L)) if sqrt(2 * j + 1) <= L])
    he = [j for j in range(m) if j % 2 == 0]      # even Hermite indices
    ho = [j for j in range(m) if j % 2 == 1]      # odd Hermite indices
    ne, no = nq + len(he), nq + len(ho)

    # bump-bump closed forms (dps 35 entries -> float64 matrices)
    Sd, Sm, Rd, Rm, Dd, Dm = _pair_terms(u, sg)

    # Hermite-bump columns: I_j(u_q, sg_q) for j = 0..m+1
    Iq = [hermite_gauss_I(m + 1, u[k], sg[k]) for k in range(nq)]

    # --- Gram blocks ---
    Sp = np.zeros((ne, ne)); Sn = np.zeros((no, no))
    Sp[:nq, :nq] = 2 * (Sd + Sm)
    Sn[:nq, :nq] = 2 * (Sd - Sm)
    for k in range(nq):
        ce = [2 * float(Iq[k][j]) for j in he]
        co = [2 * float(Iq[k][j]) for j in ho]
        Sp[k, nq:] = ce; Sp[nq:, k] = ce
        Sn[k, nq:] = co; Sn[nq:, k] = co
    Sp[nq:, nq:] = np.eye(len(he)); Sn[nq:, nq:] = np.eye(len(ho))

    # --- graded D block:  <even_i, D odd_j> = i * R[i, j] ---
    R = np.zeros((ne, no))
    R[:nq, :nq] = 2 * (Rd - Rm)                                   # <e_a, D o_b>
    for k in range(nq):                                           # <e_a, D h_odd>
        R[k, nq:] = [-2 * float(hg_R(j, Iq[k])) for j in ho]
        R[nq:, k] = [2 * float(hg_R(j, Iq[k])) for j in he]       # <h_even, D o_b>
    for r, j in enumerate(he):                                    # <h_even, D h_odd>
        for c, k in enumerate(ho):
            if j == k - 1:
                R[nq + r, nq + c] = -sqrt(k / 2.0)
            elif j == k + 1:
                R[nq + r, nq + c] = sqrt((k + 1) / 2.0)

    # --- D^2 blocks (deliverable + compression-trace check) ---
    D2p = np.zeros((ne, ne)); D2n = np.zeros((no, no))
    D2p[:nq, :nq] = 2 * (Dd + Dm)
    D2n[:nq, :nq] = 2 * (Dd - Dm)
    for k in range(nq):
        ce = [2 * float(hg_D2(j, Iq[k])) for j in he]
        co = [2 * float(hg_D2(j, Iq[k])) for j in ho]
        D2p[k, nq:] = ce; D2p[nq:, k] = ce
        D2n[k, nq:] = co; D2n[nq:, k] = co
    for blk, idxs, off in ((D2p, he, nq), (D2n, ho, nq)):
        for r, j in enumerate(idxs):
            for c, k in enumerate(idxs):
                if j == k:
                    blk[off + r, off + c] = j + 0.5
                elif j == k + 2:
                    blk[off + r, off + c] = -sqrt((k + 1) * (k + 2)) / 2.0
                elif j == k - 2:
                    blk[off + r, off + c] = -sqrt((j + 1) * (j + 2)) / 2.0

    if verbose:
        print(f"  [N0] n={n:2d}  M_n={M:6d}  |Q_n|={nq:5d}  L_n={L:6.3f}  m_n={m:3d}"
              f"  dim V_n={ne + no:5d}")
    return dict(n=n, M=M, Q=Q, u=u, sg=sg, L=L, m=m, he=he, ho=ho,
                Sp=Sp, Sn=Sn, R=R, D2p=D2p, D2n=D2n)


DROP_TOL = 1e-8      # relative Gram-eigenvalue drop threshold (redundancy is reported)


def stage_spectrum(st):
    """Canonical orthonormalisation per parity block, then spectrum = { +/- s_i } with
    s_i = singular values of the orthonormalised graded block.  Exact E1 pairing."""
    out = {}
    Xs = {}
    for tag, S in (("+", st["Sp"]), ("-", st["Sn"])):
        w, U = np.linalg.eigh(S)
        keep = w > DROP_TOL * w.max()
        Xs[tag] = U[:, keep] / np.sqrt(w[keep])
        out["rank" + tag] = int(keep.sum())
        out["drop" + tag] = int((~keep).sum())
    assert out["rank+"] > 0 and out["rank-"] > 0, "non-vacuity guard: empty parity block"
    Rt = Xs["+"].T @ st["R"] @ Xs["-"]
    assert np.abs(Rt).sum() > 0, "non-vacuity guard: H == 0"
    s = np.linalg.svd(Rt, compute_uv=False)
    tr_H2 = 2 * float((s ** 2).sum())
    tr_PD2P = float(np.trace(Xs["+"].T @ st["D2p"] @ Xs["+"])
                    + np.trace(Xs["-"].T @ st["D2n"] @ Xs["-"]))
    out.update(s=np.sort(s)[::-1], tr_H2=tr_H2, tr_PD2P=tr_PD2P, Rt=Rt)
    out["dim"] = out["rank+"] + out["rank-"]
    out["ker"] = out["dim"] - 2 * int((s > 1e-10 * s.max()).sum())
    return out


# ----------------------------------------------------------------------
# 4. the E0 harness (pre-registered; see module docstring)
# ----------------------------------------------------------------------
def R_smooth(T):
    return (T / TWO_PI) * log(T / TWO_PI) if T > TWO_PI else 0.0


def R_inverse(target):
    T = TWO_PI * exp(1.0)
    for _ in range(80):
        f = R_smooth(T) - target
        df = (log(T / TWO_PI) + 1) / TWO_PI
        T2 = T - f / df
        if abs(T2 - T) < 1e-12:
            break
        T = max(T2, TWO_PI * 1.0001)
    return T


def e0_metric(pos_spec):
    """dev over the derived window; returns (d, T_lo, T_n, dev, grid_profile)."""
    lam = np.sort(pos_spec[pos_spec > 0])
    d = len(lam)
    assert d > 0, "non-vacuity guard: empty positive spectrum"
    T_lo, T_n = R_inverse(sqrt(d)), R_inverse(d)
    grid = np.geomspace(T_lo, T_n, 200)
    Ns = np.searchsorted(lam, grid, side="right")
    Rs = np.array([R_smooth(T) for T in grid])
    ratio = Ns / Rs
    dev = float(np.abs(ratio - 1).max())
    return d, T_lo, T_n, dev, (grid, ratio)


def weyl_prediction(st, spec, T):
    """Derived (parameter-free) semiclassical law: one Planck cell of area 2pi per basis
    state; inventory site q -> cell |tau| <= pi/gap_q; Hermite mode j -> shell radius
    sqrt(2j+1) in the disk.  One-sided count."""
    gaps = 2 * st["sg"]
    fin = np.minimum(T * gaps / pi, 1.0).sum()
    arch = sum((2 / pi) * asin(min(1.0, T / sqrt(2 * j + 1))) for j in range(st["m"]))
    return fin + arch


def verdict(devs):
    last = devs[-3:]
    dec = all(last[i + 1] < last[i] for i in range(len(last) - 1)) and len(last) == 3
    return dec and last[-1] <= 0.05


# ----------------------------------------------------------------------
# 5. self-test: closed forms vs direct mpmath quadrature (dps 35)
# ----------------------------------------------------------------------
def h_fun(j, x):
    return (mp.hermite(j, x) * mp.exp(-x * x / 2)
            / mp.sqrt(mp.mpf(2) ** j * mp.factorial(j) * mp.sqrt(mp.pi)))


def g_fun(a, s, x):
    a, s = mp.mpf(a), mp.mpf(s)
    return (mp.pi * s * s) ** mp.mpf("-0.25") * mp.exp(-(x - a) ** 2 / (2 * s * s))


def selftest():
    print("=" * 78)
    print("N0 SELF-TEST — closed-form matrix elements vs mpmath.quad (dps 35)")
    print("=" * 78)
    worst = {"S": 0, "R": 0, "D2": 0, "I": 0}
    probes = [(0.9, 0.15, 1.25, 0.3), (2.1, 0.05, 2.2, 0.08), (0.7, 0.2, -1.1, 0.25)]
    for (a, sa, b, sb) in probes:
        pts = sorted([-30, a, b, 30])           # breakpoints at the bump centres
        f = lambda x: g_fun(a, sa, x) * g_fun(b, sb, x)
        worst["S"] = max(worst["S"], abs(gg_S(a, sa, b, sb) - mp.quad(f, pts)))
        fd = lambda x: -g_fun(a, sa, x) * mp.diff(lambda y: g_fun(b, sb, y), x)
        worst["R"] = max(worst["R"], abs(gg_R(a, sa, b, sb) - mp.quad(fd, pts)))
        f2 = lambda x: (mp.diff(lambda y: g_fun(a, sa, y), x)
                        * mp.diff(lambda y: g_fun(b, sb, y), x))
        worst["D2"] = max(worst["D2"], abs(gg_D2(a, sa, b, sb) - mp.quad(f2, pts)))
    for (j, a, s) in [(0, 0.69, 0.2), (5, 0.69, 0.2), (12, 3.2, 0.05), (17, 2.0, 0.3)]:
        pts = sorted([-30, 0, a, 30])
        I = hermite_gauss_I(j + 2, a, s)
        fI = lambda x: h_fun(j, x) * g_fun(a, s, x)
        worst["I"] = max(worst["I"], abs(I[j] - mp.quad(fI, pts)))
        fD2 = lambda x: (mp.diff(lambda y: h_fun(j, y), x)
                         * mp.diff(lambda y: g_fun(a, s, y), x))
        worst["D2"] = max(worst["D2"], abs(hg_D2(j, I) - mp.quad(fD2, pts)))
    for k, v in worst.items():
        print(f"  max |closed-form - quad|  {k:>2}: {mp.nstr(v, 3)}")
        assert v < mp.mpf("1e-25"), f"self-test failure in {k}"

    # assembled-entry check on a miniature stage (every entry of S+/-, R, D2+/- vs quad)
    u = np.log(np.array([2.0, 3.0, 4.0, 5.0, 7.0]))
    sg = np.array([0.18, 0.14, 0.11, 0.16, 0.12])
    st = dict(Q=None, u=u, sg=sg, m=4, he=[0, 2], ho=[1, 3])
    Sd, Sm, Rd, Rm, Dd, Dm = _pair_terms(u, sg)
    nq = len(u)
    Iq = [hermite_gauss_I(6, u[k], sg[k]) for k in range(nq)]
    cols_e = [lambda x, k=k: g_fun(u[k], sg[k], x) + g_fun(-u[k], sg[k], x) for k in range(nq)]
    cols_e += [lambda x, j=j: h_fun(j, x) for j in st["he"]]
    cols_o = [lambda x, k=k: g_fun(u[k], sg[k], x) - g_fun(-u[k], sg[k], x) for k in range(nq)]
    cols_o += [lambda x, j=j: h_fun(j, x) for j in st["ho"]]
    ne, no = len(cols_e), len(cols_o)
    Sp = np.zeros((ne, ne)); R = np.zeros((ne, no))
    Sp[:nq, :nq] = 2 * (Sd + Sm)
    for k in range(nq):
        ce = [2 * float(Iq[k][j]) for j in st["he"]]
        Sp[k, nq:] = ce; Sp[nq:, k] = ce
    Sp[nq:, nq:] = np.eye(2)
    R[:nq, :nq] = 2 * (Rd - Rm)
    for k in range(nq):
        R[k, nq:] = [-2 * float(hg_R(j, Iq[k])) for j in st["ho"]]
        R[nq:, k] = [2 * float(hg_R(j, Iq[k])) for j in st["he"]]
    for r, j in enumerate(st["he"]):
        for c, k in enumerate(st["ho"]):
            if j == k - 1:
                R[nq + r, nq + c] = -sqrt(k / 2.0)
            elif j == k + 1:
                R[nq + r, nq + c] = sqrt((k + 1) / 2.0)
    pts = sorted([-30, 30] + list(u) + list(-u) + [0])   # breakpoints at all bump centres
    eS = eR = 0.0
    for i in range(ne):
        for j in range(ne):
            q = mp.quad(lambda x: cols_e[i](x) * cols_e[j](x), pts)
            eS = max(eS, abs(Sp[i, j] - float(q)))
    for i in range(ne):
        for j in range(no):
            q = mp.quad(lambda x: -cols_e[i](x)
                        * mp.diff(lambda y: cols_o[j](y), x), pts)
            eR = max(eR, abs(R[i, j] - float(q)))
    print(f"  assembled miniature stage:  max|S+ - quad| = {eS:.3e}   max|R - quad| = {eR:.3e}")
    assert eS < 1e-12 and eR < 1e-12, "assembled-entry self-test failure"
    print("  self-test PASSED")


# ----------------------------------------------------------------------
# 6. regression against N00 (rule I0.5)
# ----------------------------------------------------------------------
def regression():
    print("=" * 78)
    print("REGRESSION (I0.5) — N00 anchors reproduced before any new number counts")
    print("=" * 78)
    g1, g2, g10 = (mp.im(mp.zetazero(k)) for k in (1, 2, 10))
    print(f"  gamma_1  = {mp.nstr(g1, 12)}   gamma_2 = {mp.nstr(g2, 12)}   "
          f"gamma_10 = {mp.nstr(g10, 12)}")
    print(f"  sin(pi gamma_1) = {mp.nstr(mp.sin(mp.pi * g1), 10)}   "
          f"sin(pi g1)/(pi g1) = {mp.nstr(mp.sin(mp.pi * g1) / (mp.pi * g1), 7)}")
    print("  [N00 §4 targets: 14.1347251417, 21.0220396388, 49.7738324777, "
          "0.4107272152, 0.009249457]")
    print("  (gamma values consumed ONLY in this regression line, per I0.6)")
    ops = []
    for nn in (8, 10, 12):
        _, cI, plt2n, _ = so.generate_sieve_data(nn)
        A, basis = so.compute_leakage_matrix_repaired(plt2n, cI)
        ops.append(np.linalg.norm(A, 2))
    print(f"  legacy ||A'||_op  n=8,10,12  = {ops[0]:.2f}, {ops[1]:.1f}, {ops[2]:.1f}"
          f"   [N00 §2: 9.27, 19.5, 36.3]")
    W, gens, comps, M = pgl.build_bipartite(6, quiet=True)
    B, _ = pgl.nonbacktracking(W)
    mu = np.linalg.eigvals(B)
    mu1 = np.max(np.abs(mu))
    det = np.abs(mu) > sqrt(mu1) * 1.02
    real = np.abs(mu[det].imag) < 1e-8 * mu1
    print(f"  graph NB n=6: mu1 = {mu1:.4f}  #detached = {det.sum()}  "
          f"#detached-real = {real.sum()}   [N00 §3: 3.5419, 4, 2]")
    ok = (abs(ops[0] - 9.27) < 0.01 and abs(ops[1] - 19.5) < 0.1 and abs(ops[2] - 36.3) < 0.1
          and abs(mu1 - 3.5419) < 0.001 and det.sum() == 4 and real.sum() == 2)
    print(f"  regression {'PASSED' if ok else '** FAILED — STOP: reportable finding **'}")
    assert ok


# ----------------------------------------------------------------------
# 7. reports
# ----------------------------------------------------------------------
def primary_report(stages=(4, 6, 8, 10, 12)):
    print("=" * 78)
    print("E0 — PRIMARY  H^G_n = P_n D P_n  (N0: sieve inventory bumps + Hermite disk)")
    print("=" * 78)
    devs = []
    profiles = {}
    for n in stages:
        st = build_stage(n)
        sp = stage_spectrum(st)
        d, T_lo, T_n, dev, prof = e0_metric(sp["s"])
        devs.append(dev)
        profiles[n] = (st, sp, prof, (d, T_lo, T_n))
        pred_dev = max(abs(np.searchsorted(np.sort(sp["s"]), T, side="right")
                           - weyl_prediction(st, sp, T)) for T in prof[0]) / d
        print(f"       dim={sp['dim']:5d} (dropped {sp['drop+'] + sp['drop-']:3d} redundant)"
              f"  ker={sp['ker']:2d}  d_n={d:5d}  trH^2/trPD2P={sp['tr_H2']/sp['tr_PD2P']:.4f}")
        print(f"       window=[{T_lo:8.2f},{T_n:9.2f}]  dev={dev:10.3f}"
              f"   |N+ - N_pred|/d (derived law) = {pred_dev:.3f}")
        assert sp["tr_H2"] <= sp["tr_PD2P"] * (1 + 1e-10), "compression trace inequality violated"
    n_last = stages[-1]
    st, sp, (grid, ratio), _ = profiles[n_last]
    print(f"\n  ratio profile N+(T)/R(T) at n={n_last} "
          f"(sampled over the derived window):")
    for k in np.linspace(0, len(grid) - 1, 8).astype(int):
        print(f"    T = {grid[k]:9.2f}   N+/R = {ratio[k]:9.3f}")
    print(f"\n  dev sequence over stages {stages}:  " +
          "  ".join(f"{v:.3f}" for v in devs))
    ok = verdict(devs)
    print(f"  E0 PRIMARY: {'PASS' if ok else 'FAIL'} "
          f"(pre-registered: last-3 strictly decreasing AND final <= 0.05)")
    return devs, ok, profiles


def controls_report(d_ref):
    print("=" * 78)
    print("E0 — CONTROLS (must-fail: legacy, graph one-mode, sine decoy; "
          "must-pass: smooth-law sample)")
    print("=" * 78)
    results = {}

    for nn in (8, 10, 12):    # legacy comparator, corrected normalisation eps = 1/||A'||
        _, cI, plt2n, M = so.generate_sieve_data(nn)
        A, basis = so.compute_leakage_matrix_repaired(plt2n, cI)
        lv = np.log(np.array(basis, dtype=float))
        H = np.diag(lv - lv.mean()) + (1.0 / np.linalg.norm(A, 2)) * A
        ev = np.linalg.eigvalsh(H)
        lam = np.sort(np.abs(ev))                      # unpaired: N+ := #{|l|<=T}/2
        d = len(lam) / 2
        T_lo, T_n = R_inverse(sqrt(d)), R_inverse(d)
        grid = np.geomspace(T_lo, T_n, 200)
        dev = float(np.abs(np.searchsorted(lam, grid, side="right") / 2
                           / np.array([R_smooth(T) for T in grid]) - 1).max())
        results[f"legacy n={nn}"] = dev

    for nn in (6, 8, 9):      # graph one-mode: singular values of the weighted stage W
        W, *_ = pgl.build_bipartite(nn, quiet=True)
        s = np.linalg.svd(W, compute_uv=False)
        _, _, _, dev, _ = e0_metric(s)
        results[f"graph n={nn}"] = dev

    lam = np.arange(1, int(d_ref) + 1, dtype=float)    # sine decoy (I0.7)
    _, _, _, dev, _ = e0_metric(lam)
    results["sine decoy"] = dev

    print(f"  {'control':>16}   dev        verdict")
    all_fail = True
    for k, v in results.items():
        failed = not (v <= 0.05)
        all_fail &= failed
        print(f"  {k:>16}   {v:9.3f}   {'FAILS E0 [as required]' if failed else '** PASSES — HARNESS BROKEN **'}")

    print("  harness positive control (smooth-law sample; no gamma-list):")
    pos_devs = []
    for d in (int(d_ref / 16), int(d_ref / 4), int(d_ref)):
        lam = np.array([R_inverse(k - 0.5) for k in range(1, d + 1)])
        _, _, _, dev, _ = e0_metric(lam)
        pos_devs.append(dev)
        print(f"    d = {d:5d}   dev = {dev:.4f}")
    pos_ok = all(pos_devs[i + 1] < pos_devs[i] for i in range(2)) and pos_devs[-1] <= 0.05
    print(f"    -> {'PASSES (metric is demonstrably passable)' if pos_ok else '** FAILS — HARNESS INVALID **'}")
    return all_fail, pos_ok


def precision_report():
    """float64 pipeline vs full-mpmath SVD on the n=4 stage (dps 35)."""
    print("=" * 78)
    print("PRECISION — float64 singular values vs mpmath svd_r (dps 35), stage n=4")
    print("=" * 78)
    st = build_stage(4, verbose=False)
    sp = stage_spectrum(st)
    Rt = sp["Rt"]
    s64 = np.sort(np.linalg.svd(Rt, compute_uv=False))[::-1]
    smp = mp.svd_r(mp.matrix(Rt.tolist()), compute_uv=False)
    smp = np.sort(np.array([float(x) for x in smp]))[::-1]
    rel = np.max(np.abs(s64 - smp[: len(s64)]) / smp[0])
    print(f"  n=4: dim={sp['dim']}, max relative singular-value difference = {rel:.3e}")
    assert rel < 1e-12


if __name__ == "__main__":
    fast = "fast" in sys.argv
    selftest()
    regression()
    precision_report()
    stages = (4, 6, 8, 10) if fast else (4, 6, 8, 10, 12)
    devs, ok, profiles = primary_report(stages)
    d_ref = profiles[stages[-1]][3][0]
    all_fail, pos_ok = controls_report(d_ref)
    print("=" * 78)
    print("VERDICT (mechanical application of the pre-registered rule)")
    print("=" * 78)
    print(f"  harness valid:            {pos_ok and all_fail}  "
          f"(positive control passes: {pos_ok}; all must-fail controls fail: {all_fail})")
    print(f"  E0, primary H^G_n:        {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("  -> WP02 falsifier branch: the primary candidate is KILLED at E0;")
        print("     E-track stops pending a redesigned window; weight shifts to WP06-08, WP12.")
