"""prime_graph_lab.py — corrected numerics for victor/prime-sieve.

Implements implementation.md (I1–I6) in the deliverable order of its final section.
Every experiment prints its non-vacuity guards and was pre-registered with success /
failure criteria (implementation.md I0.4). No rank-unfolding anywhere (rule I0.1).

Run:  cd victor && source .venv/bin/activate && python prime-sieve/prime_graph_lab.py
Sections can be selected: python prime-sieve/prime_graph_lab.py control bass gaps siegel \
                                 coupled fe qgamma1 cue flower
"""
import sys
import numpy as np
from math import log, pi, erf, sqrt
import mpmath as mp

mp.mp.dps = 30
RNG = np.random.default_rng(20260705)

# ----------------------------------------------------------------------
# sieve stage (shared logic with ../adele scripts)
# ----------------------------------------------------------------------
def sieve_primes(limit):
    if limit < 2:
        return np.array([], dtype=int)
    s = np.ones(limit + 1, dtype=bool)
    s[:2] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.flatnonzero(s)


def stage(n):
    """generators (primes < 2^n), composites in I_n, all primes <= M_n, M_n."""
    M = (1 << (n + 1)) - 1
    P = sieve_primes(M)
    gens = P[P < (1 << n)]
    inblock = set(P[P >= (1 << n)].tolist())
    comps = [m for m in range(1 << n, M + 1) if m not in inblock]
    return gens, comps, P, M


def factor_with(gens_set, m):
    """multiplicity dict of m over the generator primes (complete for composites in I_n)."""
    f = {}
    x = m
    for p in gens_set:
        if p * p > x:
            break
        k = 0
        while x % p == 0:
            x //= p
            k += 1
        if k:
            f[int(p)] = k
    if x > 1:
        f[int(x)] = f.get(int(x), 0) + 1
    return f


# ----------------------------------------------------------------------
# I1.1 bipartite divisor graph
# ----------------------------------------------------------------------
def build_bipartite(n, beta=0.5, quiet=False):
    gens, comps, P, M = stage(n)
    gi = {int(p): i for i, p in enumerate(gens)}
    W = np.zeros((len(gens), len(comps)))
    for j, m in enumerate(comps):
        for p, k in factor_with(gens, m).items():
            W[gi[p], j] += k * float(p) ** (-beta)
    edges = int((W > 0).sum())
    assert edges > 0, "D1 regression: bipartite graph must be non-empty"
    if not quiet:
        print(f"[build] n={n}: |P|={len(gens)} |C|={len(comps)} edges={edges}")
    return W, gens, comps, M


def one_mode(W):
    S = W @ W.T
    assert np.abs(S).sum() > 0, "D1 regression: coupling matrix is zero"
    return S


def nonbacktracking(W):
    """Weighted Hashimoto operator, convention B[(x->y),(y->z)] = w(y,z) [z != x],
    on the directed edges of the bipartite graph (spectrum-equivalent to the
    sqrt-split form by diagonal conjugation)."""
    Pn, Cn = W.shape
    edges = [(i, j) for i in range(Pn) for j in range(Cn) if W[i, j] != 0]
    nE = len(edges)
    col_edges = {}
    row_edges = {}
    for k, (i, j) in enumerate(edges):
        col_edges.setdefault(j, []).append(k)
        row_edges.setdefault(i, []).append(k)
    B = np.zeros((2 * nE, 2 * nE))
    # direction 1: p->m  (index k), direction 2: m->p (index nE+k)
    for k, (i, j) in enumerate(edges):
        for k2 in col_edges[j]:            # (m -> p2) following (p -> m)
            i2 = edges[k2][0]
            if i2 != i:
                B[k, nE + k2] = W[i2, j]
        for k2 in row_edges[i]:            # (p -> m2) following (m -> p)
            j2 = edges[k2][1]
            if j2 != j:
                B[nE + k, k2] = W[i, j2]
    assert np.abs(B).sum() > 0
    return B, edges


# ----------------------------------------------------------------------
# section: control  (I2.1 — proven region rate + strip divergence demo)
# ----------------------------------------------------------------------
def euler_control(s, M):
    return mp.fprod([1 - mp.power(int(p), -s) for p in sieve_primes(M)])


def sec_control(n_list=(6, 8, 10, 12)):
    print("\n== control (I2.1): |Euler_n(s)*zeta(s) - 1| — proven rate, then strip divergence ==")
    print("  sigma    n        |err|            predicted        ratio")
    for sig in (1.5, 2.0):
        s = mp.mpf(sig) + 1j * mp.mpf(7)
        for n in n_list:
            M = (1 << (n + 1)) - 1
            err = abs(euler_control(s, M) * mp.zeta(s) - 1)
            pred = mp.power(M, 1 - sig) / ((sig - 1) * mp.log(M))
            print(f"  {sig:4.2f}  {n:4d}   {mp.nstr(err, 6):>14}   {mp.nstr(pred, 6):>14}"
                  f"   {mp.nstr(err / pred, 4):>8}")
    print("  --- strip point s = 0.75 + 10i (P1.3 predicts NO convergence) ---")
    s = mp.mpf(0.75) + 10j
    for n in n_list:
        M = (1 << (n + 1)) - 1
        val = abs(euler_control(s, M) * mp.zeta(s) - 1)
        print(f"  0.75  {n:4d}   |Euler_n*zeta - 1| = {mp.nstr(val, 6)}")


# ----------------------------------------------------------------------
# section: bass  (obligation W, numeric half — which weighted Ihara–Bass form is true)
# ----------------------------------------------------------------------
def bass_candidates(A_w, B, u):
    """Return (lhs, candA, candB) at complex u for symmetric weighted adjacency A_w."""
    v = A_w.shape[0]
    iu, ju = np.nonzero(np.triu(A_w, 1))
    wts = A_w[iu, ju]
    m = len(wts)
    lhs = np.linalg.slogdet(np.eye(B.shape[0]) - u * B)
    # candidate A: naive Bass with weighted A, D = row sums
    Dw = np.diag(A_w.sum(1))
    cA_mat = np.eye(v) - u * A_w + u * u * (Dw - np.eye(v))
    sA = np.linalg.slogdet(cA_mat)
    candA = (m - v) * np.log(1 - u * u + 0j) + sA[1] + np.log(sA[0] + 0j)
    # candidate B: resolvent-type weighted Ihara–Bass
    #   det(I-uB) = prod_e (1 - u^2 w_e^2) * det(M(u)),
    #   M_xx = 1 + u^2 sum_y w_xy^2/(1-u^2 w_xy^2),  M_xy = -u w_xy/(1-u^2 w_xy^2)
    Mm = np.eye(v, dtype=complex)
    for x in range(v):
        acc = 0.0 + 0j
        for y in range(v):
            w = A_w[x, y]
            if w != 0:
                acc += u * u * w * w / (1 - u * u * w * w)
                Mm[x, y] += -u * w / (1 - u * u * w * w) if x != y else 0
        Mm[x, x] += acc
    sB = np.linalg.slogdet(Mm)
    candB = np.sum(np.log(1 - u * u * wts ** 2 + 0j)) + sB[1] + np.log(sB[0] + 0j)
    lhs_val = lhs[1] + np.log(lhs[0] + 0j)
    return lhs_val, candA, candB


def sec_bass():
    print("\n== bass (obligation W): which weighted Ihara–Bass identity holds numerically ==")
    # test graphs: random symmetric-weighted graph, and the actual bipartite stage n=5
    tests = []
    v = 8
    A = np.zeros((v, v))
    for x in range(v):
        for y in range(x + 1, v):
            if RNG.random() < 0.5:
                A[x, y] = A[y, x] = RNG.uniform(0.2, 1.5)
    tests.append(("random weighted (v=8)", A))
    W, gens, comps, M = build_bipartite(5, quiet=True)
    Pn, Cn = W.shape
    Af = np.zeros((Pn + Cn, Pn + Cn))
    Af[:Pn, Pn:] = W
    Af[Pn:, :Pn] = W.T
    tests.append((f"bipartite stage n=5 (v={Pn+Cn})", Af))
    for name, A_w in tests:
        # build Hashimoto for the full symmetric graph
        vtx = A_w.shape[0]
        dedges = [(x, y) for x in range(vtx) for y in range(vtx) if A_w[x, y] != 0]
        idx = {e: k for k, e in enumerate(dedges)}
        nd = len(dedges)
        B = np.zeros((nd, nd))
        for k, (x, y) in enumerate(dedges):
            for (y2, z), k2 in idx.items():
                if y2 == y and z != x:
                    B[k, k2] = A_w[y, z]
        errsA, errsB = [], []
        for _ in range(4):
            u = complex(RNG.uniform(0.02, 0.12), RNG.uniform(-0.08, 0.08))
            lhs, cA, cB = bass_candidates(A_w, B, u)
            errsA.append(abs(lhs - cA))
            errsB.append(abs(lhs - cB))
        print(f"  {name:32s}  max|lhs-candA| = {max(errsA):.3e}   max|lhs-candB| = {max(errsB):.3e}")
    print("  (candB = per-edge-factor resolvent form; candA = naive weighted Bass)")


# ----------------------------------------------------------------------
# section: gaps  (I4.1 with proper normalisations)
# ----------------------------------------------------------------------
def sec_gaps(n_list=(6, 7, 8, 9)):
    print("\n== gaps (I4.1): raw vs normalised one-mode; non-backtracking Ramanujan ratio ==")
    print("    n    g_raw     g_sym     mu1(B)     |mu2|(B)   |mu2|/sqrt(mu1)")
    for n in n_list:
        W, gens, comps, M = build_bipartite(n, quiet=True)
        S = one_mode(W)
        lam = np.linalg.eigvalsh(S)[::-1]
        g_raw = 1 - lam[1] / lam[0]
        d = S.sum(1)
        d[d == 0] = 1
        Ls = S / np.sqrt(np.outer(d, d))
        ls = np.linalg.eigvalsh(Ls)[::-1]
        g_sym = 1 - ls[1] / ls[0]
        B, edges = nonbacktracking(W)
        mu = np.linalg.eigvals(B)
        order = np.argsort(-np.abs(mu))
        mu1 = np.abs(mu[order[0]])
        # bipartite NB spectrum is symmetric under mu -> -mu: skip the mirrored Perron
        k = 1
        while k < len(order) and abs(mu[order[k]] + mu[order[0]]) < 1e-6 * mu1:
            k += 1
        mu2 = np.abs(mu[order[k]])
        print(f"  {n:4d}  {g_raw:8.5f}  {g_sym:8.5f}  {mu1:9.4f}  {mu2:9.4f}   {mu2/np.sqrt(mu1):8.4f}")
    print("  (Ramanujan-type benchmark: bulk of spec(B) within |mu| <= sqrt(mu1);"
          " ratio <= 1 means spectral-gap optimality of the detached part)")


# ----------------------------------------------------------------------
# section: siegel  (I4.2: detached eigenvalues of B — graph-Siegel tracking)
# ----------------------------------------------------------------------
def sec_siegel(n_list=(6, 7, 8, 9)):
    print("\n== siegel (I4.2): eigenvalues of B detached from the sqrt(mu1) disk ==")
    print("    n    #eigs   mu1       #detached  #detached-real   detached real list (top 6 |.|)")
    for n in n_list:
        W, gens, comps, M = build_bipartite(n, quiet=True)
        B, edges = nonbacktracking(W)
        mu = np.linalg.eigvals(B)
        mu1 = np.max(np.abs(mu))
        R = sqrt(mu1) * 1.02
        det_mask = np.abs(mu) > R
        detached = mu[det_mask]
        real_mask = np.abs(detached.imag) < 1e-8 * mu1
        dr = np.sort(np.abs(detached[real_mask]))[::-1]
        mirror = "yes" if np.min(np.abs(np.sort(mu.real) + np.sort(mu.real)[::-1])) < 1e-6 else "approx"
        print(f"  {n:4d}  {len(mu):6d}  {mu1:8.3f}  {det_mask.sum():8d}  {real_mask.sum():10d}"
              f"       {np.round(dr[:6], 3)}  (bipartite mirror: {mirror})")


# ----------------------------------------------------------------------
# section: coupled  (H* probe: theta-sweep of coupled place determinant, strip stability)
# ----------------------------------------------------------------------
def coupled_T(s, n, theta):
    """T(s;theta) = diag(p^-s, p <= M_n) + theta * C(s), coupling via composites in I_n:
    C_pq(s) = sum_{m in I_n, p != q, pq | m} a_p(m) a_q(m) (pq)^{s/2} m^{-s}."""
    gens, comps, P, M = stage(n)
    plist = [int(p) for p in P]
    pi_idx = {p: i for i, p in enumerate(plist)}
    N = len(plist)
    T = np.zeros((N, N), dtype=complex)
    for i, p in enumerate(plist):
        T[i, i] = complex(mp.power(p, -s))
    if theta != 0:
        C = np.zeros((N, N), dtype=complex)
        for m in comps:
            f = factor_with(sieve_primes(1 << n), m)
            pr = [(p, k) for p, k in f.items()]
            ms = complex(mp.power(m, -s))
            for a in range(len(pr)):
                for b in range(a + 1, len(pr)):
                    p, kp = pr[a]
                    q, kq = pr[b]
                    val = kp * kq * complex(mp.power(p * q, s / 2)) * ms
                    C[pi_idx[p], pi_idx[q]] += val
                    C[pi_idx[q], pi_idx[p]] += val
        T = T + theta * C
    return T


def detIminus(T):
    sgn, ld = np.linalg.slogdet(np.eye(T.shape[0], dtype=complex) - T)
    return sgn * np.exp(ld)


def sec_coupled(n_list=(8, 9, 10), thetas=(0.0, 0.25, 0.5, 1.0, -0.5)):
    print("\n== coupled (H* probe): stage-to-stage stability of D_n(s;theta) at strip point ==")
    s0 = mp.mpf("0.75") + 10j
    print(f"  s0 = 0.75 + 10i ;  metric r_n = |D_(n+1)-D_n|/|D_n|  (control theta=0 must NOT converge, P1.3)")
    print("  theta     " + "   ".join(f"r_{n}->{n+1}" for n in n_list[:-1]) + "    |D_last*zeta-1|")
    z = mp.zeta(s0)
    for th in thetas:
        Ds = []
        for n in n_list:
            Ds.append(detIminus(coupled_T(s0, n, th)))
        rs = [abs(Ds[i + 1] - Ds[i]) / abs(Ds[i]) for i in range(len(Ds) - 1)]
        final = abs(Ds[-1] * complex(z) - 1)
        print(f"  {th:5.2f}   " + "   ".join(f"{r:8.4f}" for r in rs) + f"    {final:10.4f}")
    print("  (theta=0 row is the control: same numbers as the bare Euler truncation)")


# ----------------------------------------------------------------------
# section: fe  (I2.3 functional-equation asymmetry sweep)
# ----------------------------------------------------------------------
def G_completed(s):
    return 0.5 * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)


def sec_fe(n=9, thetas=(0.0, 0.25, 0.5, 1.0)):
    print("\n== fe (I2.3): asymmetry of eta_n(s) = G(s)/D_n(s;theta) under s -> 1-s ==")
    grid = [mp.mpf("0.6") + 1j * t for t in (5, 10, 15)]
    print("  theta    median |eta(s)/eta(1-s) - 1|")
    for th in thetas:
        ratios = []
        for s in grid:
            Da = detIminus(coupled_T(s, n, th))
            Db = detIminus(coupled_T(1 - s, n, th))
            ga, gb = complex(G_completed(s)), complex(G_completed(1 - s))
            eta_a = ga / Da
            eta_b = gb / Db
            ratios.append(abs(eta_a / eta_b - 1))
        ratios.sort()
        print(f"  {th:5.2f}    {ratios[len(ratios)//2]:12.4f}   (grid Re s = 0.6, t = 5,10,15; n={n})")
    print("  (baseline theta=0 quantifies how far the bare truncation is from any FE)")


# ----------------------------------------------------------------------
# section: qgamma1  (route-gamma covering probe: spectral containment n -> n+1)
# ----------------------------------------------------------------------
def sec_qgamma1(pairs=((6, 7), (7, 8), (8, 9))):
    print("\n== qgamma1 (Q-γ1): is spec(S_n) approximately contained in spec(S_{n+1})? ==")
    print("   n->n+1   containment fraction (rel tol 2%)   [lift signature would be ~1.0]")
    for a, b in pairs:
        Sa = one_mode(build_bipartite(a, quiet=True)[0])
        Sb = one_mode(build_bipartite(b, quiet=True)[0])
        la = np.linalg.eigvalsh(Sa)
        lb = np.linalg.eigvalsh(Sb)
        la = la[np.abs(la) > 1e-8 * np.max(np.abs(la))]
        frac = np.mean([np.min(np.abs(lb - x)) < 0.02 * max(abs(x), 1e-12) for x in la])
        print(f"   {a}->{b}    {frac:6.3f}")


# ----------------------------------------------------------------------
# section: cue  (I3 raw-gap statistics, data-internal normalisation only)
# ----------------------------------------------------------------------
def sec_cue(n=8):
    print("\n== cue (I3): raw NB eigenvalue-angle gaps vs Wigner beta=2 surmise ==")
    W, gens, comps, M = build_bipartite(n, quiet=True)
    B, _ = nonbacktracking(W)
    mu = np.linalg.eigvals(B)
    mu = mu[np.abs(mu) > 1e-8]
    th = np.sort(np.angle(mu[mu.imag > 1e-9]))
    if len(th) < 20:
        print("  too few non-real eigenvalues"); return
    gaps = np.diff(th)
    gaps = gaps / gaps.mean()
    xs = np.sort(gaps)
    F_emp = np.arange(1, len(xs) + 1) / len(xs)
    F_cue = np.array([erf(2 * x / sqrt(pi)) - (4 * x / pi) * np.exp(-4 * x * x / pi) for x in xs])
    ks = np.max(np.abs(F_emp - F_cue))
    # Poisson comparison for context
    F_poi = 1 - np.exp(-xs)
    ksP = np.max(np.abs(F_emp - F_poi))
    print(f"  n={n}: N={len(xs)} gaps; KS to CUE = {ks:.4f}, KS to Poisson = {ksP:.4f}")


# ----------------------------------------------------------------------
# section: flower  (I6: quantum-graph amplitude probe + the mixing no-go witness)
# ----------------------------------------------------------------------
def sec_flower(primes=(2, 3, 5, 7, 11)):
    print("\n== flower (I6): Neumann flower amplitudes vs Lambda(m)/sqrt(m) ==")
    Bn = len(primes)
    nb = 2 * Bn                      # directed bonds
    back = 2.0 / nb - 1.0            # backscatter coefficient
    thru = 2.0 / nb                  # transmission coefficient
    print(f"  loops: {primes};  Neumann sigma: through={thru:.3f}, backscatter={back:.3f}")
    print("  -- pure prime powers p^k: orbit amplitude (thru)^k vs Lambda/sqrt(m) --")
    print("   m      amplitude      Lambda(m)/sqrt(m)    ratio")
    for p in primes[:3]:
        for k in (1, 2, 3):
            m = p ** k
            amp = thru ** k
            target = log(p) / sqrt(m)
            print(f"  {m:4d}   {amp:10.5f}   {target:12.5f}   {amp/target:10.4f}")
    print("  -- mixed two-letter orbits pq (Lambda(pq) = 0): amplitude must be 0 to match --")
    print("   p,q     |amplitude sigma_pq sigma_qp|   Lambda(pq)")
    for (p, q) in ((2, 3), (2, 5), (3, 5)):
        print(f"   {p},{q}     {thru*thru:12.5f}                 0")
    print("  Witness of the no-go (findings.md F8): any irreducible s-independent unitary")
    print("  scattering puts nonzero amplitude on some mixed orbit, whose length log(pq...) ")
    print("  is, by unique factorisation, shared by NO prime power — exact matching is")
    print("  impossible; reducible (diagonal) scattering = decoupled Euler product (P1.3).")


# ----------------------------------------------------------------------
SECTIONS = {
    "control": sec_control, "bass": sec_bass, "gaps": sec_gaps, "siegel": sec_siegel,
    "coupled": sec_coupled, "fe": sec_fe, "qgamma1": sec_qgamma1, "cue": sec_cue,
    "flower": sec_flower,
}

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a in SECTIONS] or list(SECTIONS)
    for a in args:
        SECTIONS[a]()
