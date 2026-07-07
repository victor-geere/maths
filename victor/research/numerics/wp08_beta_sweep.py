r"""wp08_beta_sweep.py — PSC2-WP08 (G4): beta-sweep of the detached-spectrum census and
the numerical verification of every ingredient of the edge-purity (anti-Siegel) theorem
(PSC2-F05).

Objects (N00 par.3 / prime_graph_lab conventions): P_n = primes < 2^n; C_n = composites in
I_n = [2^n, 2^{n+1}); W[p,m] = v_p(m) p^{-beta}; B_w = weighted non-backtracking (Hashimoto)
operator on the 2|E| directed edges. By the proven grading identity (F03 Lemma L2 + Schur),
det(I - uB) = det(I - u^2 C) with C on the |E| states (p->m):
C[(p,m),(p',m')] = W[p',m] W[p',m'] [p'|m] [p' != p] [m' != m], so spec(B) minus {0} =
+-sqrt(spec(C) minus {0}) and the sweep runs on C (half dimension); leaf states are
nilpotent (F03 Prop B1), so C is built on the 2-core. Census (N00 par.3 convention,
unchanged): detached iff |mu| > 1.02 sqrt(mu1), i.e. |nu| > 1.02^2 mu1, mu1 = sqrt(rho(C)).

PRE-REGISTERED CRITERIA (fixed before any (n, beta) with beta != 1/2 or n = 10, 11 was
computed; beta = 1/2 rows at n <= 9 are the N00/F03 anchors):
  SWEEP GRID — beta in {0.30, 0.35, ..., 0.70} for n = 4..10; beta in {0.30, 0.50, 0.70}
  for n = 11 (coarse extension row).
  CENSUS — the WP's finding survives iff at EVERY grid point with n >= 5 the detached
  census is exactly 4 (2 real = the Perron pair +-mu1, 2 purely imaginary = +-i tau), i.e.
  in C-terms exactly one positive and one negative detached eigenvalue, both real.
  The n = 4 row is recorded but excluded from the verdict (parent census F03: 2 detached
  at beta = 1/2 — the imaginary pair has not yet detached); its beta-behaviour is reported.
  FALSIFIER (the WP's, two-sided; do not suppress — rule I0.4):
    - a beta at which a fifth eigenvalue detaches PERSISTENTLY (>= 6 B-detached at >= 3
      consecutive stages at the same beta) -> "PERSISTENT FIFTH" discovery branch;
    - a grid point with < 4 detached, a non-simple structure, or a detached non-real
      C-eigenvalue (a genuinely complex B-quadruple) -> "CENSUS BOUNDARY DRIFT" branch.
  THEOREM INGREDIENTS — consequences of the edge-purity theorem in PSC2-F05; each must
  hold at every computed stage (a violation is an audit finding against the proof).
  All are beta-independent (they concern the support/structure only):
    E1  bipartite stage graph connected
    E2  2-core nonempty, connected, min degree >= 2, and vertex 2 has core-degree >= 3
        (t6 := #multiples of 6 in I_n >= 3, giving K_{2,t6} inside the core)
    E3  witness cycles exist: two distinct multiples of 6 in I_n (4-cycle => closed
        C-walk of length 2) and a triple m1 in 6Z, m2 in 15Z, m3 in 10Z, pairwise
        distinct, in I_n (6-cycle => closed C-walk of length 3)
    E4  the C-state graph on the core is strongly connected (machine reachability)
    E5  Tr C = 0 exactly; Tr C^2 > 0; Tr C^3 > 0 (period gcd(2,3) = 1 => primitive)
    E6  Perron eigenvalue of C real, positive, simple, strictly dominant
        (peripheral gap 1 - |nu_2|/rho(C) > 0 reported per point)
  CONTROLS (two-sided):
    - classical positive control: census of unweighted K_{a,b} must match its closed-form
      NB spectrum (verified against direct diagonalization, see note below):
      {+-sqrt((a-1)(b-1))} u {+-i sqrt(b-1)}^(a-1) u {+-i sqrt(a-1)}^(b-1) u {+-1}^((a-1)(b-1));
      K_{2,5} -> 4 detached (2 real), K_{2,12} -> 4 with the imaginary pair AT the Perron
      modulus (period-4 degenerate comparator: no odd C-walk), K_{3,8} -> 6;
    - teeth: two weakly coupled copies of stage n = 6 (bridge weight 1e-3) must show
      >= 6 (expected 8) detached — the census demonstrably CAN see a fifth eigenvalue;
    - interpretive nulls at n = 8, beta = 1/2 (recorded, not pass/fail): (i) k == 1
      weights on the true divisor support (multiplicity effect); (ii) degree-preserving
      rewired support, weights p^{-beta}, 3 seeds (arithmetic-vs-generic support).
  REGRESSION (rule I0.5): the lab-B census at beta = 1/2, n = 6..9, built through
  prime_graph_lab's own builders, must reproduce N00 par.3 verbatim (mu1 = 3.5419,
  5.2810, 7.6871, 10.9663; detached 4, of which 2 real); the C-method nonzero |spec|
  must agree with the lab-B nonzero |spec| to 1e-8 at n = 5..7 for beta in
  {0.30, 0.50, 0.70} (method cross-validation; those beta != 1/2 points then also
  count as sweep data).

POST-FALSIFIER ADDENDUM (7 Jul 2026 — added AFTER the first full run fired the
PERSISTENT FIFTH branch; the pre-registered criteria above are unchanged). Two edits:
  (1) control fix: the first run's predicted K_{a,b} multiset omitted the +-1 family of
      multiplicity (a-1)(b-1) (and wrongly included zeros); corrected against direct
      diagonalization. Census counts were unaffected by the bug.
  (2) diagnostics D1-D3 appended to document the discovery branch (rule I0.4):
      D1 nu-ladders (top 12 by modulus) at the deviating grid points and at anchor
         neighbours — is the extra detached family isolated from the bulk?
      D2 hub-block comparison: rho of the C of the induced weighted subgraph on
         {p, q} u (common multiples) vs the full negative-nu ladder;
      D3 n = 12 anchor point (beta = 1/2) via sparse LM eigensolver (needs scipy;
         skipped with a notice if scipy is absent).

Run:  cd victor && source .venv/bin/activate && python research/numerics/wp08_beta_sweep.py
"""
import sys
from math import sqrt

sys.path.insert(0, __file__.rsplit("/", 1)[0])

import numpy as np

from prime_graph_lab import build_bipartite, nonbacktracking

RNG = np.random.default_rng(20260708)
BETAS = [0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70]
N_FULL = range(4, 11)          # full beta grid
N_COARSE = {11: [0.30, 0.50, 0.70]}
TOL_IM = 1e-8                  # relative tolerance for "real" / "purely imaginary"


# ----------------------------------------------------------------------
# graph plumbing
# ----------------------------------------------------------------------
def two_core(W):
    """Masks (rows, cols) of the 2-core of the bipartite graph supp(W)."""
    A = (W != 0)
    kr = np.ones(A.shape[0], bool)
    kc = np.ones(A.shape[1], bool)
    while True:
        dr = A[:, kc].sum(1) * kr
        dc = A[kr, :].sum(0) * kc
        drop_r = kr & (dr <= 1)
        drop_c = kc & (dc <= 1)
        if not drop_r.any() and not drop_c.any():
            return kr, kc
        kr &= ~drop_r
        kc &= ~drop_c


def build_C(W):
    """Two-step NB operator on the (p->m) states of W (use on the 2-core):
    C[(i,j),(i',j')] = W[i',j] W[i',j'] for i' != i, j' != j, both edges present."""
    Pn, Cn = W.shape
    edges = [(i, j) for i in range(Pn) for j in range(Cn) if W[i, j] != 0]
    idx = {e: k for k, e in enumerate(edges)}
    nbr_p = {i: np.flatnonzero(W[i]) for i in range(Pn)}
    nbr_c = {j: np.flatnonzero(W[:, j]) for j in range(Cn)}
    nE = len(edges)
    C = np.zeros((nE, nE))
    for k, (i, j) in enumerate(edges):
        for i2 in nbr_c[j]:
            if i2 == i:
                continue
            w1 = W[i2, j]
            for j2 in nbr_p[i2]:
                if j2 != j:
                    C[k, idx[(i2, j2)]] = w1 * W[i2, j2]
    assert nE == 0 or np.trace(C) == 0.0, "Tr C must vanish identically (E5)"
    return C, edges


def census_nu(nu):
    """Census in C-terms. Returns dict with mu1, counts (B-terms), purity, margins."""
    rho = float(np.max(nu.real))
    assert abs(np.max(np.abs(nu)) - rho) < 1e-9 * max(rho, 1e-30), \
        "Perron of C must be real positive (E6)"
    mu1 = sqrt(rho)
    thr = 1.02 ** 2 * mu1                       # |nu| threshold == (1.02 sqrt(mu1))^2
    det_mask = np.abs(nu) > thr
    d = nu[det_mask]
    real = np.abs(d.imag) < TOL_IM * rho
    npos = int((real & (d.real > 0)).sum())
    nneg = int((real & (d.real < 0)).sum())
    ncplx = int((~real).sum())
    bulk = nu[~det_mask]
    m_det = float(np.min(np.abs(d)) ** 0.5 / (1.02 * sqrt(mu1))) if len(d) else 0.0
    m_bulk = float(np.max(np.abs(bulk)) ** 0.5 / (1.02 * sqrt(mu1))) if len(bulk) else 0.0
    srt = np.sort(np.abs(nu))[::-1]
    gap_edge = 1.0 - (srt[1] / srt[0] if len(srt) > 1 else 0.0)   # E6 peripheral gap
    nu2 = -float(np.min(nu.real))                                  # most negative
    return dict(mu1=mu1, rho=rho, count=2 * int(det_mask.sum()), nreal=2 * npos,
                nimag=2 * nneg, ncplx=2 * ncplx, m_det=m_det, m_bulk=m_bulk,
                gap_edge=gap_edge, ratio_neg=nu2 / rho,
                tau_mu1=(sqrt(nu2) / mu1 if nu2 > 0 else 0.0))


def census_mu(mu):
    """Census straight from B-eigenvalues (N00 par.3 convention) — regression path."""
    mu1 = float(np.max(np.abs(mu)))
    R = 1.02 * sqrt(mu1)
    d = mu[np.abs(mu) > R]
    nreal = int((np.abs(d.imag) < TOL_IM * mu1).sum())
    nonreal = d[np.abs(d.imag) >= TOL_IM * mu1]
    max_re = float(np.max(np.abs(nonreal.real))) if len(nonreal) else 0.0
    return mu1, len(d), nreal, max_re


def stage_C(n, beta):
    W = build_bipartite(n, beta=beta, quiet=True)[0]
    kr, kc = two_core(W)
    return build_C(W[np.ix_(kr, kc)])


# ----------------------------------------------------------------------
# theorem ingredients (beta-independent: support/structure only)
# ----------------------------------------------------------------------
def strongly_connected(C):
    A = C != 0
    n = A.shape[0]
    for M in (A, A.T):
        r = np.zeros(n, bool)
        r[0] = True
        while True:
            r2 = r | (M @ r)
            if (r2 == r).all():
                break
            r = r2
        if not r.all():
            return False
    return True


def connected_bipartite(W):
    A = W != 0
    P, Cn = A.shape
    rp = np.zeros(P, bool)
    rc = np.zeros(Cn, bool)
    rp[0] = True
    while True:
        rc2 = rc | (A.T @ rp)
        rp2 = rp | (A @ rc2)
        if (rp2 == rp).all() and (rc2 == rc).all():
            break
        rp, rc = rp2, rc2
    return rp.all() and rc.all()


def ingredient_checks(n):
    W, gens, comps, M = build_bipartite(n, quiet=True)   # support is beta-independent
    lo, hi = 1 << n, (1 << (n + 1)) - 1
    e1 = connected_bipartite(W)
    kr, kc = two_core(W)
    Wc = W[np.ix_(kr, kc)]
    core_ok = Wc.size > 0 and connected_bipartite(Wc)
    degs = np.concatenate([(Wc != 0).sum(1), (Wc != 0).sum(0)])
    mult6 = [m for m in range(lo, hi + 1) if m % 6 == 0]
    t6 = len(mult6)
    i2 = int(np.flatnonzero(gens == 2)[0])
    e2 = core_ok and degs.min() >= 2 and t6 >= 3 and (Wc[0] != 0).sum() >= 3 \
        and kr[i2]                                     # vertex 2 survives with degree >= 3
    # E3 witnesses: two multiples of 6; a pairwise-distinct triple in 6Z/15Z/10Z
    m15 = [m for m in range(lo, hi + 1) if m % 15 == 0]
    m10 = [m for m in range(lo, hi + 1) if m % 10 == 0]
    triple = next(((a, b, c) for a in mult6 for b in m15 for c in m10
                   if a != b and b != c and a != c), None)
    e3 = t6 >= 2 and triple is not None
    C, edges = build_C(Wc)
    e4 = strongly_connected(C)
    tr2 = float(np.einsum("ij,ji->", C, C))
    tr3 = float(np.trace(C @ C @ C))
    e5 = np.trace(C) == 0.0 and tr2 > 0 and tr3 > 0
    return dict(e1=e1, e2=e2, e3=e3, e4=e4, e5=e5, t6=t6, triple=triple,
                nE=len(edges), core=(int(kr.sum()), int(kc.sum())),
                pruned=int((~kr).sum() + (~kc).sum()))


# ----------------------------------------------------------------------
# controls
# ----------------------------------------------------------------------
def control_kab():
    ok = True
    print("[control] unweighted K_{a,b} vs closed-form NB spectrum "
          "{+-sqrt((a-1)(b-1)), +-i sqrt(b-1) x(a-1), +-i sqrt(a-1) x(b-1), +-1 x(a-1)(b-1)}:")
    for (a, b), want in (((2, 5), (4, 2)), ((2, 12), (4, 2)), ((3, 8), (6, 2))):
        B, _ = nonbacktracking(np.ones((a, b)))
        mu = np.linalg.eigvals(B)
        pred = np.array([sqrt((a - 1) * (b - 1)), sqrt((a - 1) * (b - 1))]
                        + [sqrt(b - 1)] * 2 * (a - 1) + [sqrt(a - 1)] * 2 * (b - 1)
                        + [1.0] * 2 * (a - 1) * (b - 1))
        match = np.allclose(np.sort(np.abs(mu)), np.sort(pred), atol=1e-8)
        mu1, dct, drl, _ = census_mu(mu)
        edge = abs(sqrt(b - 1) - mu1) < 1e-9   # imaginary pair AT the edge (K_{2,b})
        ok &= match and (dct, drl) == want
        print(f"   K_{a},{b}: |spectrum| matches closed form: {match};  census {dct} "
              f"({drl} real) (expected {want[0]} ({want[1]} real))"
              + ("  [imaginary pair AT Perron modulus - period-4 comparator]" if edge else ""))
    return ok


def control_teeth():
    W = build_bipartite(6, quiet=True)[0]
    P, Cn = W.shape
    Wb = np.zeros((2 * P, 2 * Cn))
    Wb[:P, :Cn] = W
    Wb[P:, Cn:] = W
    Wb[P, 0] = 1e-3                              # weak bridge copy2-prime -> copy1-composite
    kr, kc = two_core(Wb)
    C, _ = build_C(Wb[np.ix_(kr, kc)])
    nu = np.linalg.eigvals(C)
    c = census_nu(nu)
    ok = c["count"] >= 6
    print(f"[teeth] two weakly coupled copies of stage n=6: detached = {c['count']} "
          f"({c['nreal']} real, {c['nimag']} imaginary) >= 6: {ok}  (expected 8)")
    return ok


def swap_rewire(W, seed, nswap_factor=20):
    """Degree-preserving double-edge swaps on the bipartite support."""
    rng = np.random.default_rng(seed)
    A = (W != 0).astype(bool).copy()
    edges = list(zip(*np.nonzero(A)))
    target = nswap_factor * len(edges)
    done = trials = 0
    while done < target and trials < 50 * target:
        trials += 1
        k1, k2 = rng.integers(0, len(edges), 2)
        (i1, j1), (i2, j2) = edges[k1], edges[k2]
        if i1 == i2 or j1 == j2 or A[i1, j2] or A[i2, j1]:
            continue
        A[i1, j1] = A[i2, j2] = False
        A[i1, j2] = A[i2, j1] = True
        edges[k1], edges[k2] = (i1, j2), (i2, j1)
        done += 1
    return A


def control_nulls(n=8, beta=0.5):
    gens = build_bipartite(n, quiet=True)[1]
    W = build_bipartite(n, beta=beta, quiet=True)[0]
    pw = gens.astype(float) ** (-beta)
    print(f"[nulls] interpretive controls at n={n}, beta={beta} (recorded, not pass/fail):")
    Wk1 = (W != 0) * pw[:, None]                 # (i) true support, k == 1 weights
    kr, kc = two_core(Wk1)
    c = census_nu(np.linalg.eigvals(build_C(Wk1[np.ix_(kr, kc)])[0]))
    print(f"   k==1 weights, true divisor support:   detached {c['count']} "
          f"({c['nreal']} real, {c['nimag']} imag)  tau/mu1={c['tau_mu1']:.3f}")
    for seed in (1, 2, 3):                       # (ii) rewired support
        A = swap_rewire(W, seed)
        Wr = A * pw[:, None]
        kr, kc = two_core(Wr)
        Cn_, _ = build_C(Wr[np.ix_(kr, kc)])
        c = census_nu(np.linalg.eigvals(Cn_))
        print(f"   rewired support (seed {seed}), w=p^-b:      detached {c['count']} "
              f"({c['nreal']} real, {c['nimag']} imag)  tau/mu1={c['tau_mu1']:.3f}")


# ----------------------------------------------------------------------
# regression (rule I0.5)
# ----------------------------------------------------------------------
def regression():
    ok = True
    n00 = {6: 3.5419, 7: 5.2810, 8: 7.6871, 9: 10.9663}
    print("[regress] lab-B census at beta=1/2 vs N00 par.3 (must be mu1 match to 1e-3, 4/2):")
    for n in (6, 7, 8, 9):
        W = build_bipartite(n, quiet=True)[0]
        mu = np.linalg.eigvals(nonbacktracking(W)[0])
        mu1, dct, drl, max_re = census_mu(mu)
        good = abs(mu1 - n00[n]) < 1e-3 and (dct, drl) == (4, 2)
        ok &= good
        print(f"   n={n}: mu1={mu1:.4f} (N00 {n00[n]});  detached {dct} ({drl} real);  "
              f"|Re| of non-real detached = {max_re:.1e}: {'ok' if good else 'MISMATCH'}")
    print("[regress] C-method vs lab-B nonzero |spec| (rel 1e-8), n=5..7 x beta={0.3,0.5,0.7}:")
    worst = 0.0
    for n in (5, 6, 7):
        for beta in (0.30, 0.50, 0.70):
            W = build_bipartite(n, beta=beta, quiet=True)[0]
            muB = np.linalg.eigvals(nonbacktracking(W)[0])
            C, _ = stage_C(n, beta)
            s = np.sqrt(np.linalg.eigvals(C).astype(complex))
            muC = np.concatenate([s, -s])
            a = np.sort(np.abs(muB[np.abs(muB) > 1e-8]))
            b = np.sort(np.abs(muC[np.abs(muC) > 1e-8]))
            dev = np.max(np.abs(a - b) / np.maximum(a, 1e-12)) if len(a) == len(b) else np.inf
            worst = max(worst, dev)
            ok &= dev < 1e-8
    print(f"   worst relative deviation: {worst:.2e}  (< 1e-8: {worst < 1e-8})")
    return ok


# ----------------------------------------------------------------------
# post-falsifier diagnostics (addendum; see header)
# ----------------------------------------------------------------------
def diag_ladder(n, beta, k=12):
    C, _ = stage_C(n, beta)
    nu = np.linalg.eigvals(C)
    rho = np.max(nu.real)
    mu1 = sqrt(rho)
    order = np.argsort(-np.abs(nu))[:k]
    out = []
    for ix in order:
        v = nu[ix]
        cls = "R+" if abs(v.imag) < TOL_IM * rho and v.real > 0 else \
              ("R-" if abs(v.imag) < TOL_IM * rho else "C ")
        out.append(f"{cls}{sqrt(abs(v)) / (1.02 * sqrt(mu1)):.3f}")
    print(f"   [D1 n={n:2d} beta={beta:.2f}] " + "  ".join(out))


def diag_hubs(n, beta, pairs=((2, 3), (2, 5), (3, 5), (2, 7))):
    """rho(C) of the induced weighted subgraph on {p,q} u (common multiples): the
    two-prime alternation makes its spectrum {+-h}, h = the hub-block strength."""
    W, gens, comps, M = build_bipartite(n, beta=beta, quiet=True)
    gi = {int(p): i for i, p in enumerate(gens)}
    line = []
    for (p, q) in pairs:
        cols = [j for j in range(len(comps)) if W[gi[p], j] != 0 and W[gi[q], j] != 0]
        Ws = W[np.ix_([gi[p], gi[q]], cols)]
        kr, kc = two_core(Ws)
        if kr.sum() == 0:
            line.append(f"({p},{q}): -")
            continue
        Cs, _ = build_C(Ws[np.ix_(kr, kc)])
        nus = np.linalg.eigvals(Cs)
        line.append(f"({p},{q}): t={len(cols)} h={float(np.max(nus.real)):.1f}")
    C, _ = stage_C(n, beta)
    nu = np.linalg.eigvals(C)
    rho = np.max(nu.real)
    negs = np.sort(nu.real[np.abs(nu.imag) < TOL_IM * rho])[:3]
    print(f"   [D2 n={n:2d} beta={beta:.2f}] rho={rho:.1f}; most negative nu: "
          f"{np.round(negs, 1)};  isolated hub strengths: " + "  ".join(line))


def diag_n12(beta=0.5, k=24):
    try:
        import scipy.sparse as sp
        import scipy.sparse.linalg as spl
    except ImportError:
        print("   [D3] scipy not installed - n=12 anchor point skipped")
        return
    n = 12
    W = build_bipartite(n, beta=beta, quiet=True)[0]
    kr, kc = two_core(W)
    Wc = W[np.ix_(kr, kc)]
    Pn, Cn = Wc.shape
    edges = [(i, j) for i in range(Pn) for j in range(Cn) if Wc[i, j] != 0]
    idx = {e: kk for kk, e in enumerate(edges)}
    nbr_p = {i: np.flatnonzero(Wc[i]) for i in range(Pn)}
    nbr_c = {j: np.flatnonzero(Wc[:, j]) for j in range(Cn)}
    rows, cols, vals = [], [], []
    for kk, (i, j) in enumerate(edges):
        for i2 in nbr_c[j]:
            if i2 == i:
                continue
            w1 = Wc[i2, j]
            for j2 in nbr_p[i2]:
                if j2 != j:
                    rows.append(kk)
                    cols.append(idx[(i2, j2)])
                    vals.append(w1 * Wc[i2, j2])
    C = sp.csr_matrix((vals, (rows, cols)), shape=(len(edges), len(edges)))
    nu = spl.eigs(C, k=k, which="LM", return_eigenvectors=False, tol=1e-10)
    rho = float(np.max(nu.real))
    mu1 = sqrt(rho)
    thr = 1.02 ** 2 * mu1
    d = nu[np.abs(nu) > thr]
    real = np.abs(d.imag) < 1e-7 * rho
    out = []
    for ix in np.argsort(-np.abs(nu))[:8]:
        v = nu[ix]
        cls = "R+" if abs(v.imag) < 1e-7 * rho and v.real > 0 else \
              ("R-" if abs(v.imag) < 1e-7 * rho else "C ")
        out.append(f"{cls}{sqrt(abs(v)) / (1.02 * sqrt(mu1)):.3f}")
    print(f"   [D3 n=12 beta={beta}] nE={len(edges)}  mu1={mu1:.4f}  detached "
          f"{2 * len(d)} ({2 * int((real & (d.real > 0)).sum())} real, "
          f"{2 * int((real & (d.real < 0)).sum())} imag);  top ladder: " + "  ".join(out))


# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("== WP08 (G4): beta-sweep of the detached census + edge-purity theorem ingredients ==")
    allok = control_kab()
    allok &= control_teeth()
    allok &= regression()

    print("\n-- theorem ingredients E1-E5 per stage (beta-independent) --")
    for n in list(N_FULL) + sorted(N_COARSE):
        r = ingredient_checks(n)
        good = r["e1"] and r["e2"] and r["e3"] and r["e4"] and r["e5"]
        allok &= good
        print(f"   n={n:2d}: connected={r['e1']}  core|P|,|C|={r['core']} (pruned {r['pruned']}) "
              f"deg>=2+hub={r['e2']} (t6={r['t6']})  witnesses={r['e3']} (triple {r['triple']})  "
              f"strong-conn={r['e4']}  TrC=0,TrC^2>0,TrC^3>0={r['e5']}"
              + ("" if good else "  INGREDIENT VIOLATION"))

    print("\n-- census sweep --")
    print("    n  beta   nE    mu1      det  real  imag  cplx   m_det   m_bulk   "
          "|nu2|/rho  tau/mu1  edge-gap")
    per_beta_counts = {b: {} for b in BETAS}
    drift_points = []
    fifth_watch = 0.0
    for n in list(N_FULL) + sorted(N_COARSE):
        for beta in N_COARSE.get(n, BETAS):
            C, edges = stage_C(n, beta)
            c = census_nu(np.linalg.eigvals(C))
            per_beta_counts[beta][n] = c["count"]
            fifth_watch = max(fifth_watch, c["m_bulk"])
            pure = (c["ncplx"] == 0)
            good = (c["count"], c["nreal"], c["nimag"]) == (4, 2, 2) and pure
            if n >= 5 and not good:
                drift_points.append((n, beta, c["count"], c["nreal"], c["nimag"], c["ncplx"]))
            print(f"   {n:2d}  {beta:.2f}  {len(edges):4d}  {c['mu1']:7.4f}   {c['count']:2d}"
                  f"    {c['nreal']:2d}    {c['nimag']:2d}    {c['ncplx']:2d}   "
                  f"{c['m_det']:6.3f}   {c['m_bulk']:6.3f}    {c['ratio_neg']:6.4f}   "
                  f"{c['tau_mu1']:6.4f}   {c['gap_edge']:.4f}"
                  + ("" if (good or n == 4) else "  <-- DEVIATION"))

    control_nulls()

    # pre-registered verdicts
    fifth = []
    for b, row in per_beta_counts.items():
        ns = sorted(k for k in row if k >= 5)
        run = 0
        for n in ns:
            run = run + 1 if row[n] >= 6 else 0
            if run >= 3:
                fifth.append(b)
                break
    survives = not drift_points and not fifth
    print(f"\n[verdict] deviating grid points (n >= 5): {drift_points if drift_points else 'none'}")
    print(f"[verdict] persistent-fifth betas: {fifth if fifth else 'none'};  "
          f"fifth-watch: max bulk |mu|/threshold over sweep = {fifth_watch:.3f}")
    print(f"[verdict] pre-registered census verdict: "
          f"{'SURVIVES (4 = 2 real + 2 imaginary at every grid point, all beta)' if survives else ('PERSISTENT FIFTH (falsifier branch)' if fifth else 'CENSUS BOUNDARY DRIFT (falsifier branch)')}")

    print("\n-- post-falsifier diagnostics (addendum; criteria above unchanged) --")
    for (n, beta) in ((8, 0.30), (9, 0.35), (10, 0.30), (10, 0.50), (11, 0.50), (11, 0.70)):
        diag_ladder(n, beta)
    for (n, beta) in ((10, 0.50), (11, 0.50), (10, 0.30)):
        diag_hubs(n, beta)
    diag_n12()

    print(f"\nWP08 HARNESS + CONTROLS + INGREDIENTS {'PASS' if allok else 'FAIL'};  "
          f"CENSUS: {'SURVIVES' if survives else ('PERSISTENT FIFTH' if fifth else 'BOUNDARY DRIFT')}"
          + ("" if survives else "  (discovery branch - documented in PSC2-F05)"))
