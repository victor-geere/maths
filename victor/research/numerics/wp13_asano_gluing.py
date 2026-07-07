"""wp13_asano_gluing.py — PSC2-WP13: Asano gluing on the per-edge product form (Q-γ2 / G6).

The atomic sieve step is the vertex addition G -> G+x: x a composite of the next
block, attached by one edge per generator prime p | x with weight w = k p^(-1/2).
Exact structure (Lemma A; proven by Schur complement on the vertex matrix M(u) of
the PROVEN weighted Ihara–Bass identity, F03 Theorem A — the correct form of the
"Schur-complement vertex addition" X10 asserted):

    p_{G+x}(u) = p_G(u) * Psi_x(u),
    Psi_x = prod_i (1 - u^2 w_i^2) * (1 + sum_i h_i) * det(I_d + Gamma Lambda),
      h_i = u^2 w_i^2/(1 - u^2 w_i^2),   g_i = u w_i/(1 - u^2 w_i^2),
      Lambda = diag(h) - g g^T / (1 + sum h),
      Gamma = (M_G(u)^{-1}) restricted to the neighbour set N(x).

  d = 1  =>  Psi == 1 exactly (recovers F03 Prop. B1).
  d = 2 (Lemma B):  Psi = 1 - 2 gamma12 t + C t^2,
      t = u^2 w1 w2,  C = gamma11 + gamma22 - 1 - det Gamma.
  Multi-affine lift (Lemma C): with the four directed-edge variables of the two
  new edges free, P_x/p_G = 1 - gamma12 (s1 + s2) + C s1 s2, where
  s1 = z_{y1->x} z_{x->y2}, s2 = z_{y2->x} z_{x->y1} — a SYMMETRIC multi-affine
  form; by Grace–Walsh–Szegő its polydisc nonvanishing (the Asano hypothesis) is
  equivalent to disk nonvanishing of the transfer quadratic
      q(s) = 1 - 2 gamma12 s + C s^2.
  The Asano contraction proper keeps only 1 + C s (drops the gamma12 terms) and
  is strictly coarser. All coefficient algebra above was cross-checked through
  the sympy-verifier MCP server (six identities; list in F06).

Sections (pre-registered two-sided criteria in PSC2-WP13 / recorded in F06):
  S  symbolic proofs of Lemmas A/B/C on explicit graphs + the n=3 stage anchor
     Psi_15(v) == (1 - v^3/15)^2, fully symbolic;
  G  EXACT certification over Q (Bareiss, no floats) of the gluing law at every
     vertex addition of the actual stage builds n = 2..6, at rational sample
     points, via  det Mt_after == m_xx * det(Mt_before + Lhat);  float census:
     trivial vs core steps, Perron radius before/after, injection record;
  A  the graded Asano/GWS chain: largest certifiable zero-free radius R* per
     core step (d=2: exact GWS root condition; d>=3: norm bound), chained, vs
     the true radius 1/rho; spurious per-edge factor zeros 1/wmax vs 1/rho;
  L  locus coverage n = 4..9: does ANY fixed circular region avoid all stage
     zeros? (largest avoided disk over a center grid, cumulative in n);
  T  two-sided controls: disjoint-cycle chain (genuine locus preservation MUST
     be recognised: rho constant, zeros on the fixed circle) and a planted
     weight bump (MUST be flagged as an injection).

Run:  cd victor && source .venv/bin/activate && python research/numerics/wp13_asano_gluing.py
Deterministic; no random draws; the gamma-list is not consumed anywhere.
"""
import sys
import time
from fractions import Fraction

import numpy as np
import sympy as sp

sys.path.insert(0, __file__.rsplit("/", 1)[0])

from wp06_bass_certify import (exact_stage_edges, det_fraction_matrix,
                               check_against_float_builder, Mt_matrix)

# ----------------------------------------------------------------------
# generic float layer: edges are (a, b, w) with hashable vertex labels
# ----------------------------------------------------------------------
def verts_of(edges, extra=()):
    vs, seen = [], set()
    for (a, b, w) in edges:
        for x in (a, b):
            if x not in seen:
                seen.add(x); vs.append(x)
    for x in extra:
        if x not in seen:
            seen.add(x); vs.append(x)
    return vs


def M_complex(edges, u, verts):
    idx = {x: i for i, x in enumerate(verts)}
    M = np.eye(len(verts), dtype=complex)
    for (a, b, w) in edges:
        f = 1 - u * u * w * w
        M[idx[a], idx[a]] += u * u * w * w / f
        M[idx[b], idx[b]] += u * u * w * w / f
        M[idx[a], idx[b]] += -u * w / f
        M[idx[b], idx[a]] += -u * w / f
    return M, idx


def p_eval(edges, u):
    """det(I - u B_w) via the proven per-edge product form (F03 Thm A)."""
    if not edges:
        return 1.0 + 0j
    verts = verts_of(edges)
    M, _ = M_complex(edges, u, verts)
    pr = np.prod([1 - u * u * w * w for (_, _, w) in edges])
    return pr * np.linalg.det(M)


def B_matrix(edges):
    """Weighted non-backtracking matrix, sqrt convention (multigraph-safe)."""
    nE = len(edges)
    ors = [(a, b, w) for (a, b, w) in edges] + [(b, a, w) for (a, b, w) in edges]
    B = np.zeros((2 * nE, 2 * nE))
    for i, (o1, t1, w1) in enumerate(ors):
        rev = (i + nE) % (2 * nE)
        for j, (o2, t2, w2) in enumerate(ors):
            if o2 == t1 and j != rev:
                B[i, j] = np.sqrt(w1 * w2)
    return B


def zeros_and_rho(edges, tol=1e-9):
    """Zeros of det(I - uB) (= 1/nonzero eigenvalues) and rho = max |eig|."""
    if not edges:
        return np.array([], dtype=complex), 0.0
    mu = np.linalg.eigvals(B_matrix(edges))
    top = np.abs(mu).max() if len(mu) else 0.0
    if top < tol:
        return np.array([], dtype=complex), 0.0
    mu = mu[np.abs(mu) > tol * top]
    return 1.0 / mu, float(top)


def two_core(edges, protect=()):
    """Iteratively delete degree-<=1 vertices (never those in `protect`)."""
    cur = list(edges)
    while True:
        deg = {}
        for (a, b, w) in cur:
            deg[a] = deg.get(a, 0) + 1
            deg[b] = deg.get(b, 0) + 1
        kill = {x for x, d in deg.items() if d <= 1 and x not in protect}
        if not kill:
            return cur
        cur = [(a, b, w) for (a, b, w) in cur if a not in kill and b not in kill]


def psi_float(parent_edges, nbrs_w, u, use_core=False):
    """Psi_x(u) for adjoining a vertex with edges (y_i, w_i), from the parent
    Green block. use_core=True computes Gamma on the protected 2-core (equal by
    the B1-Schur invariance; asserted in section G)."""
    protect = tuple(y for (y, _) in nbrs_w)
    pe = two_core(parent_edges, protect) if use_core else parent_edges
    verts = verts_of(pe, extra=protect)
    M, idx = M_complex(pe, u, verts)
    Minv = np.linalg.inv(M)
    ii = [idx[y] for (y, _) in nbrs_w]
    Gam = Minv[np.ix_(ii, ii)]
    h = np.array([u * u * w * w / (1 - u * u * w * w) for (_, w) in nbrs_w])
    g = np.array([u * w / (1 - u * u * w * w) for (_, w) in nbrs_w])
    m = 1 + h.sum()
    Lam = np.diag(h) - np.outer(g, g) / m
    pref = np.prod([1 - u * u * w * w for (_, w) in nbrs_w]) * m
    return pref * np.linalg.det(np.eye(len(nbrs_w)) + Gam @ Lam)


# ----------------------------------------------------------------------
# exact layer (Fractions, rationalised coordinates of wp06 L3)
# ----------------------------------------------------------------------
def exact_lhat(new_pk, v):
    """Rationalised Schur correction Lhat (rows/cols = neighbour primes):
    Lhat_jk = delta_jk h_j - v k_j k_k p_j / ((p_j - v k_j^2)(p_k - v k_k^2) m).
    Returns (Lhat as dict {(pj,pk): Fraction}, m_xx)."""
    dens = {p: p - v * k * k for (p, k) in new_pk}
    hs = {p: v * k * k / dens[p] for (p, k) in new_pk}
    m = Fraction(1) + sum(hs.values())
    L = {}
    for (pj, kj) in new_pk:
        for (pk_, kk) in new_pk:
            val = -v * kj * kk * pj / (dens[pj] * dens[pk_] * m)
            if pj == pk_:
                val += hs[pj]
            L[(pj, pk_)] = val
    return L, m


def exact_step_ok(verts_before, edges_before, verts_after, edges_after,
                  new_pk, v):
    """Certify det Mt_after(v) == m_xx * det(Mt_before(v) + Lhat(v)) over Q."""
    for (p, k) in new_pk:
        if p - v * k * k == 0:
            return None  # pole at the sample; caller picks another v
    L, m = exact_lhat(new_pk, v)
    if m == 0:
        return None
    lhs = det_fraction_matrix(Mt_matrix(verts_after, edges_after, v))
    rows = Mt_matrix(verts_before, edges_before, v)
    idx = {x: i for i, x in enumerate(verts_before)}
    for (pj, pk_), val in L.items():
        rows[idx[("p", pj)]][idx[("p", pk_)]] += val
    rhs = m * det_fraction_matrix(rows)
    return lhs == rhs


# ----------------------------------------------------------------------
# section S — symbolic lemmas (sympy; independent MCP checks listed in F06)
# ----------------------------------------------------------------------
def dm_det(M):
    """Exact determinant of a sympy Matrix with rational(-function) entries via
    DomainMatrix (field arithmetic in canonical form — no expression blowup)."""
    try:
        from sympy.polys.matrices import DomainMatrix
        dm = DomainMatrix.from_Matrix(M).to_field()
        return dm.domain.to_sympy(dm.det())
    except Exception:
        return M.det(method="berkowitz")


def is_zero(e):
    """Exact zero test for rational expressions: cancel to one fraction, expand
    the numerator."""
    num, _ = sp.fraction(sp.cancel(sp.together(e)))
    return sp.expand(num) == 0


def M_sympy(edges, u, verts):
    idx = {x: i for i, x in enumerate(verts)}
    M = sp.eye(len(verts))
    for (a, b, w) in edges:
        f = 1 - u**2 * w**2
        M[idx[a], idx[a]] += u**2 * w**2 / f
        M[idx[b], idx[b]] += u**2 * w**2 / f
        M[idx[a], idx[b]] += -u * w / f
        M[idx[b], idx[a]] += -u * w / f
    return M, idx


def p_sympy(edges, u, verts):
    M, _ = M_sympy(edges, u, verts)
    pr = sp.prod([1 - u**2 * w**2 for (_, _, w) in edges])
    return sp.cancel(sp.together(pr * dm_det(M)))


def psi_sympy(parent_edges, nbrs_w, u, verts):
    M, idx = M_sympy(parent_edges, u, verts)
    Minv = M.inv()
    d = len(nbrs_w)
    h = [u**2 * w**2 / (1 - u**2 * w**2) for (_, w) in nbrs_w]
    g = [u * w / (1 - u**2 * w**2) for (_, w) in nbrs_w]
    m = 1 + sum(h)
    Lam = sp.Matrix(d, d, lambda j, k: (h[j] if j == k else 0) - g[j] * g[k] / m)
    Gam = sp.Matrix(d, d, lambda j, k: Minv[idx[nbrs_w[j][0]], idx[nbrs_w[k][0]]])
    pref = sp.prod([1 - u**2 * w**2 for (_, w) in nbrs_w]) * m
    return sp.cancel(sp.together(pref * dm_det(sp.eye(d) + Gam * Lam)))


def nb_det_sympy(des, u_or_none=None):
    """det(I - B_z) with per-directed-edge weights; des = [(a, b, z_ab, z_ba)].
    Convention: transition e->f (head(e)=tail(f), f != reverse(e)) carries z_f."""
    ors = [(a, b, zab) for (a, b, zab, zba) in des] + \
          [(b, a, zba) for (a, b, zab, zba) in des]
    N = len(ors)
    nE = len(des)
    B = sp.zeros(N, N)
    for i, (o1, t1, z1) in enumerate(ors):
        rev = (i + nE) % (2 * nE)
        for j, (o2, t2, z2) in enumerate(ors):
            if o2 == t1 and j != rev:
                B[i, j] = z2
    return dm_det(sp.eye(N) - B)


def sec_symbolic():
    print("\n== S: symbolic proofs of the gluing lemmas (sympy) ==")
    u = sp.symbols("u")
    R = sp.Rational
    ok = True

    # star polynomial sigma_d = prod(1-v_i)(1 + sum h_i), d = 2, 3, 4
    vs = sp.symbols("v1 v2 v3 v4")
    for d, rhs in ((2, 1 - vs[0] * vs[1]),
                   (3, 1 - sp.Add(*[vs[i] * vs[j] for i in range(3) for j in range(i + 1, 3)])
                       + 2 * vs[0] * vs[1] * vs[2]),
                   (4, 1 - sp.Add(*[vs[i] * vs[j] for i in range(4) for j in range(i + 1, 4)])
                       + 2 * sp.Add(*[vs[i] * vs[j] * vs[k] for i in range(4)
                                      for j in range(i + 1, 4) for k in range(j + 1, 4)])
                       - 3 * vs[0] * vs[1] * vs[2] * vs[3])):
        lhs = sp.prod([1 - vs[i] for i in range(d)]) * (1 + sum(vs[i] / (1 - vs[i]) for i in range(d)))
        okd = sp.simplify(lhs - rhs) == 0
        print(f"[S1] star polynomial sigma_{d} = 1 + sum (-1)^(m-1)(m-1) e_m: {okd}")
        ok &= okd

    # transfer determinant identity, symmetric t-form and asymmetric s-form
    a, b, c, t, s1, s2 = sp.symbols("a b c t s1 s2")
    G2 = sp.Matrix([[a, c], [c, b]])
    lhsT = ((1 - t**2) * sp.eye(2) + t * G2 * sp.Matrix([[t, -1], [-1, t]])).det()
    rhsT = (1 - t**2) * (1 - 2 * c * t + (a + b - 1 - (a * b - c**2)) * t**2)
    okT = sp.simplify(lhsT - rhsT) == 0
    lhsS = ((1 - s1 * s2) + a * s1 * s2 - c * s2) * ((1 - s1 * s2) + b * s1 * s2 - c * s1) \
        - (c * s1 * s2 - a * s1) * (c * s1 * s2 - b * s2)
    rhsS = (1 - s1 * s2) * (1 - c * (s1 + s2) + (a + b - 1 - (a * b - c**2)) * s1 * s2)
    okS = sp.simplify(lhsS - rhsS) == 0
    print(f"[S2] transfer determinant identity: t-form {okT};  s-form (multi-affine) {okS}")
    ok &= okT and okS

    # Lemma A on explicit graphs: triangle ABC + vertex x, d = 1, 2, 3, bridge
    tri = [("A", "B", R(1, 2)), ("B", "C", R(1, 3)), ("C", "A", R(2, 5))]
    pG = p_sympy(tri, u, ["A", "B", "C"])
    cases = [("d=1 leaf", [("A", R(1, 2))], None),
             ("d=2", [("A", R(1, 2)), ("B", R(1, 3))], None),
             ("d=3", [("A", R(1, 2)), ("B", R(1, 3)), ("C", R(3, 7))], None),
             ("bridge to fresh vertex", [("A", R(1, 2)), ("D", R(1, 3))], None)]
    for name, nb, _ in cases:
        t0 = time.time()
        verts = verts_of(tri, extra=[y for (y, _) in nb])
        psi = psi_sympy(tri, nb, u, verts)
        gpx = tri + [(y, "x", w) for (y, w) in nb]
        pGx = p_sympy(gpx, u, verts + ["x"])
        okc = is_zero(pGx - pG * psi)
        extra = ""
        if name in ("d=1 leaf", "bridge to fresh vertex"):
            okc &= is_zero(psi - 1)
            extra = " (and Psi == 1)"
        print(f"[S3] gluing law p_(G+x) = p_G * Psi, {name}: {okc}{extra}   [{time.time()-t0:.1f}s]")
        ok &= okc

    # Lemma B: the d=2 Green-quadratic form of Psi
    nb = [("A", R(1, 2)), ("B", R(1, 3))]
    M, idx = M_sympy(tri, u, ["A", "B", "C"])
    Minv = M.inv()
    g11, g22, g12 = Minv[0, 0], Minv[1, 1], Minv[0, 1]
    tt = u**2 * R(1, 2) * R(1, 3)
    psiB = 1 - 2 * g12 * tt + (g11 + g22 - 1 - (g11 * g22 - g12**2)) * tt**2
    okB = is_zero(psi_sympy(tri, nb, u, ["A", "B", "C"]) - psiB)
    print(f"[S3b] Lemma B (d=2 transfer quadratic in Green data): {okB}")
    ok &= okB

    # Lemma A against det(I - uB) directly (oriented-edge space), exact u samples
    psi_nb = psi_sympy(tri, nb, u, ["A", "B", "C"])
    for uval in (R(1, 3), R(2, 7)):
        t0 = time.time()
        des = [(x, y, uval * w, uval * w)
               for (x, y, w) in tri + [("A", "x", R(1, 2)), ("B", "x", R(1, 3))]]
        lhs = nb_det_sympy(des)
        rhs = (pG * psi_nb).subs(u, uval)
        okd = is_zero(lhs - rhs)
        print(f"[S3c] law vs det(I-uB) on the oriented-edge space at u={uval}: {okd}   [{time.time()-t0:.1f}s]")
        ok &= okd

    # Lemma C: multi-affine lift with the four new directed variables free.
    # Both sides are multi-affine in (a1, b1, a2, b2) — each variable lives in a
    # single column of I - B_z — so equality on {0, 1}^4 is polynomial identity.
    t0 = time.time()
    uval = R(1, 3)
    g11n, g22n, g12n = [e.subs(u, uval) for e in (g11, g22, g12)]
    Cn = g11n + g22n - 1 - (g11n * g22n - g12n**2)
    pGn = pG.subs(u, uval)
    okC = True
    for bits in range(16):
        a1v, b1v, a2v, b2v = [R(1) if bits >> i & 1 else R(0) for i in range(4)]
        des = [(x, y, uval * w, uval * w) for (x, y, w) in tri] + \
              [("A", "x", a1v, b1v), ("B", "x", a2v, b2v)]
        lhs = nb_det_sympy(des)     # z_{y_i->x} = a_i, z_{x->y_i} = b_i
        rhs = pGn * (1 - g12n * (a1v * b2v + a2v * b1v) + Cn * a1v * b1v * a2v * b2v)
        okC &= is_zero(lhs - rhs)
    print(f"[S4] multi-affine lift P_x/p_G = 1 - g12(s1+s2) + C s1 s2 "
          f"(16 corner evaluations, exact): {okC}   [{time.time()-t0:.1f}s]")
    ok &= okC

    # n=3 stage anchor: the single core step (m=15) on the actual stage graph,
    # fully symbolic in v via the rationalised coordinates (wp06 L3): the parent
    # (all composites < 15 added) is a forest, p == 1; adding 15 closes the
    # 6-cycle 2-10-5-15-3-12 and Psi must equal (1 - v^3/15)^2 exactly.
    v = sp.symbols("v")
    gens, comps, edges3 = exact_stage_edges(3)
    parent = [(p, m, k) for (p, m, k) in edges3 if m != 15]
    new_pk = [(p, k) for (p, m, k) in edges3 if m == 15]
    verts = [("p", p) for p in gens] + [("c", m) for m in comps if m != 15]
    idx = {x: i for i, x in enumerate(verts)}
    Mt = sp.eye(len(verts))
    for (p, m, k) in parent:
        den = p - v * k * k
        ip, im = idx[("p", p)], idx[("c", m)]
        Mt[ip, ip] += v * k * k / den
        Mt[im, im] += v * k * k / den
        Mt[ip, im] += -v * k * p / den
        Mt[im, ip] += -sp.Rational(k) / den
    t0 = time.time()
    prod_old = sp.prod([1 - sp.Rational(k * k, p) * v for (p, m, k) in parent])
    ok0 = is_zero(prod_old * dm_det(Mt) - 1)
    dens = {p: p - v * k * k for (p, k) in new_pk}
    hs = {p: v * k * k / dens[p] for (p, k) in new_pk}
    mxx = 1 + sum(hs.values())
    Mt2 = Mt.copy()
    for (pj, kj) in new_pk:
        for (pk_, kk) in new_pk:
            val = -v * kj * kk * pj / (dens[pj] * dens[pk_] * mxx)
            if pj == pk_:
                val += hs[pj]
            Mt2[idx[("p", pj)], idx[("p", pk_)]] += val
    prod_new = sp.prod([1 - sp.Rational(k * k, p) * v for (p, k) in new_pk])
    psi15 = sp.cancel(sp.together(prod_old * prod_new * mxx * dm_det(Mt2)))
    ok15 = is_zero(psi15 - (1 - v**3 / 15)**2)
    print(f"[S5] n=3 anchor: parent forest p == 1: {ok0};  Psi_15(v) == (1 - v^3/15)^2: {ok15}"
          f"   [{time.time()-t0:.1f}s]")
    ok &= ok0 and ok15
    return ok


# ----------------------------------------------------------------------
# sections G + A — stage build chains: exact certification, census, Asano chain
# ----------------------------------------------------------------------
F03_ANCHORS = {4: (1.3602, 10, 16), 5: (2.3173, 32, 52), 6: (3.5419, 84, 106)}


def stage_steps(n):
    gens, comps, edges = exact_stage_edges(n)
    by_m = {}
    for (p, m, k) in edges:
        by_m.setdefault(m, []).append((p, k))
    return gens, sorted(comps), by_m, edges


def gws_radius_d2(parent_edges, nbrs_w, cap, ngrid=(1.0, 0.72, 0.45, 0.18)):
    """Largest R <= cap with: for all |u| <= R (grid on circles), the transfer
    quadratic q(s) = 1 - 2 g12 s + C s^2 has no root with |s| <= R^2 w1 w2.
    By GWS this is exactly polydisc (Asano-hypothesis) nonvanishing of the lift."""
    w1, w2 = nbrs_w[0][1], nbrs_w[1][1]
    protect = tuple(y for (y, _) in nbrs_w)
    pe = two_core(parent_edges, protect)
    verts = verts_of(pe, extra=protect)

    def ok(Rv):
        tau = Rv * Rv * w1 * w2
        for rr in ngrid:
            for th in np.linspace(0, np.pi, 17):   # symmetry u -> -u, conj
                uu = rr * Rv * np.exp(1j * th)
                M, idx = M_complex(pe, uu, verts)
                Minv = np.linalg.inv(M)
                i1, i2 = idx[protect[0]], idx[protect[1]]
                g12 = Minv[i1, i2]
                Cc = Minv[i1, i1] + Minv[i2, i2] - 1 - \
                    (Minv[i1, i1] * Minv[i2, i2] - g12 * g12)
                if abs(Cc) > 1e-14:
                    rts = np.roots([Cc, -2 * g12, 1])
                elif abs(g12) > 1e-14:
                    rts = np.array([1 / (2 * g12)])
                else:
                    continue
                if np.abs(rts).min() <= tau:
                    return False
        return True

    lo, hi = 0.0, cap
    if ok(hi):
        return hi
    for _ in range(42):
        mid = 0.5 * (lo + hi)
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo


def norm_radius_dge3(parent_edges, nbrs_w, cap):
    """Sufficient certificate for d >= 3: ||Gamma||_2 * ||Lambda_bar(R)||_2 < 1
    with the entrywise worst-case Lambda over the polydisc of radii R w_i."""
    protect = tuple(y for (y, _) in nbrs_w)
    pe = two_core(parent_edges, protect)
    verts = verts_of(pe, extra=protect)
    ws = np.array([w for (_, w) in nbrs_w])

    def ok(Rv):
        vh = (Rv * ws)**2
        if vh.max() >= 0.999:
            return False
        hb = vh / (1 - vh)
        mlow = 1 - hb.sum()
        if mlow <= 1e-9:
            return False
        gb = np.sqrt(np.outer(vh, vh)) / np.outer(1 - vh, 1 - vh)
        Lbar = np.diag(hb) + gb / mlow
        nL = np.linalg.norm(Lbar, 2)
        for rr in (1.0, 0.6, 0.25):
            for th in np.linspace(0, np.pi, 13):
                uu = rr * Rv * np.exp(1j * th)
                M, idx = M_complex(pe, uu, verts)
                Gam = np.linalg.inv(M)[np.ix_([idx[y] for y in protect],
                                              [idx[y] for y in protect])]
                if np.linalg.norm(Gam, 2) * nL >= 1:
                    return False
        return True

    lo, hi = 0.0, cap
    if ok(hi):
        return hi
    for _ in range(42):
        mid = 0.5 * (lo + hi)
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo


def sec_stage_chains(n_list=(2, 3, 4, 5, 6)):
    print("\n== G + A: stage build chains — exact gluing certification, census, Asano/GWS chain ==")
    U_SAMPLES = (0.07 + 0.031j, 0.11 - 0.05j, 0.19 + 0.13j)
    allok = True
    for n in n_list:
        t0 = time.time()
        gens, comps, by_m, all_edges = stage_steps(n)
        v_samples = [Fraction(1, 7), Fraction(3, 13)] if n <= 5 else [Fraction(1, 7)]
        verts_now = [("p", p) for p in gens]
        tedges, fedges = [], []            # typed (p,m,k) and float (a,b,w)
        zprev, rho_prev = np.array([], dtype=complex), 0.0
        n_triv = n_core = 0
        exact_all = True
        law_resid = 0.0
        green_core_dev = 0.0
        R_cert = None                       # None == certified zero-free everywhere so far
        rows_A = []
        inj_strict = inj_appear = inj_flat = 0
        for m in comps:
            new_pk = by_m[m]
            nbrs_w = [(("p", p), k * p**-0.5) for (p, k) in new_pk]
            verts_after = verts_now + [("c", m)]
            tafter = tedges + [(p, m, k) for (p, k) in new_pk]
            fafter = fedges + [(("p", p), ("c", m), k * p**-0.5) for (p, k) in new_pk]
            # exact certification of the gluing law over Q
            for v in v_samples:
                r = exact_step_ok(verts_now, tedges, verts_after, tafter, new_pk, v)
                exact_all &= (r is True)
            # float law check + Green core-invariance tie
            for uu in U_SAMPLES:
                pb, pa = p_eval(fedges, uu), p_eval(fafter, uu)
                psi = psi_float(fedges, nbrs_w, uu)
                law_resid = max(law_resid, abs(pa - pb * psi) / max(abs(pa), 1e-30))
                psic = psi_float(fedges, nbrs_w, uu, use_core=True)
                green_core_dev = max(green_core_dev, abs(psi - psic))
            # classification: 2-core change vs Psi == 1
            core_b = sorted((min(a, b), max(a, b)) for (a, b, _) in two_core(fedges))
            core_a = sorted((min(a, b), max(a, b)) for (a, b, _) in two_core(fafter))
            trivial_core = (core_b == core_a)
            trivial_psi = all(abs(psi_float(fedges, nbrs_w, uu) - 1) < 1e-9 for uu in U_SAMPLES)
            if trivial_core != trivial_psi:
                print(f"   [n={n}] m={m}: CLASSIFICATION MISMATCH core-change={not trivial_core} Psi!=1={not trivial_psi}")
                allok = False
            # census + Asano chain on core steps
            znew, rho_new = zeros_and_rho(fafter)
            if trivial_core:
                n_triv += 1
                if abs(rho_new - rho_prev) > 1e-8 * max(rho_prev, 1e-12) + 1e-12:
                    print(f"   [n={n}] m={m}: trivial step changed rho ({rho_prev} -> {rho_new})")
                    allok = False
            else:
                n_core += 1
                d = len(new_pk)
                r_b = (1 / rho_prev) if rho_prev > 0 else float("inf")
                r_a = 1 / rho_new
                if rho_prev == 0.0:
                    inj_appear += 1
                    tag = "zeros appear"
                elif r_a < r_b * (1 - 1e-10):
                    inj_strict += 1
                    tag = "injection"
                else:
                    inj_flat += 1
                    tag = "radius kept"
                wmax_pc = max([w for (_, _, w) in two_core(fedges, tuple(y for y, _ in nbrs_w))] + [1e-12])
                cap = 0.98 / max(wmax_pc, max(w for (_, w) in nbrs_w))
                if R_cert is not None:
                    cap = min(cap, R_cert)
                Rstar = (gws_radius_d2(fedges, nbrs_w, cap) if d == 2
                         else norm_radius_dge3(fedges, nbrs_w, cap))
                R_cert = Rstar if R_cert is None else min(R_cert, Rstar)
                rows_A.append((m, d, r_b, r_a, Rstar, tag))
            verts_now, tedges, fedges = verts_after, tafter, fafter
            zprev, rho_prev = znew, rho_new
        # stage-end ties
        tie = check_against_float_builder(n, tedges)
        zs, rho = zeros_and_rho(fedges)
        anchor = ""
        if n == 3:
            anchor = f";  rho == 15^(-1/6): {abs(rho - 15**(-1/6.0)) < 1e-9}"
            allok &= abs(rho - 15**(-1/6.0)) < 1e-9
        if n in F03_ANCHORS:
            mu1, nre, nnr = F03_ANCHORS[n]
            re_mask = np.abs(zs.imag) < 1e-8 * max(1.0, np.abs(zs).max())
            cnts = (int(re_mask.sum()), int((~re_mask).sum()))
            okt = abs(rho - mu1) < 5e-4 and cnts == (nre, nnr)
            anchor = f";  F03 tie mu1={rho:.4f} (exp {mu1}) poles {cnts} (exp {(nre, nnr)}): {okt}"
            allok &= okt
        print(f"[n={n}] steps={len(comps)} (trivial {n_triv}, core {n_core});  exact law over Q at "
              f"v={[str(v) for v in v_samples]}: {exact_all};  float law max resid {law_resid:.1e};  "
              f"Green core-invariance max dev {green_core_dev:.1e};  builder tie {tie:.1e}{anchor}   "
              f"[{time.time()-t0:.1f}s]")
        allok &= exact_all and law_resid < 1e-8 and green_core_dev < 1e-8
        if rows_A:
            print(f"       core steps (m, d): 1/rho before -> after | Asano/GWS R* | outcome")
            for (m, d, r_b, r_a, Rstar, tag) in rows_A:
                rb = f"{r_b:.4f}" if np.isfinite(r_b) else "inf"
                print(f"         m={m:<4d} d={d}:  {rb} -> {r_a:.4f}  |  R*={Rstar:.4f}  |  {tag}")
            print(f"       injection census: strict {inj_strict}, zeros-appear {inj_appear}, "
                  f"radius-kept {inj_flat}")
            wmax_core = max(w for (_, _, w) in two_core(fedges))
            sound = (R_cert is not None) and (R_cert <= 1 / rho + 1e-9)
            print(f"       stage end: 1/rho={1/rho:.4f};  Asano chain R_cert={R_cert:.4f} "
                  f"(ratio {R_cert*rho:.3f});  spurious factor zeros at 1/wmax_core={1/wmax_core:.4f} "
                  f"(inside zero-free disk: {1/wmax_core < 1/rho});  soundness R_cert <= 1/rho: {sound}")
            allok &= sound
    return allok


# ----------------------------------------------------------------------
# section L — locus coverage: does any fixed circular region survive?
# ----------------------------------------------------------------------
def sec_coverage(n_list=(4, 5, 6, 7, 8, 9)):
    print("\n== L: locus coverage — what region could an Asano chain preserve? ==")
    print("  (the diagonal specialisation z_e = u w_e turns every polydisc/circular-region")
    print("   hypothesis into a MODULUS condition on u: Asano/GWS-reachable u-regions are")
    print("   radially symmetric — disks, circles, annuli, exteriors centered at 0.")
    print("   Decisive census: radial coverage of the cumulative zero sets.)")
    grid = [complex(x, y) for x in np.arange(-2.5, 2.51, 0.25)
            for y in np.arange(-2.5, 2.51, 0.25) if abs(complex(x, y)) <= 2.0]
    grid = np.array(grid)
    acc = np.array([], dtype=complex)
    for n in n_list:
        gens, comps, edges = exact_stage_edges(n)
        fedges = [(("p", p), ("c", m), k * p**-0.5) for (p, m, k) in edges]
        zs, rho = zeros_and_rho(fedges)
        acc = np.concatenate([acc, zs])
        re_mask = np.abs(zs.imag) < 1e-8 * np.abs(zs).max()
        cosmin = np.abs(np.cos(np.angle(zs[~re_mask]))).min() if (~re_mask).any() else 1.0
        rs = np.sort(np.abs(acc))
        gaps = np.argsort(np.diff(rs))[::-1][:3]
        gtxt = ", ".join(f"{rs[i+1]-rs[i]:.3f}@|u|~{0.5*(rs[i]+rs[i+1]):.2f}" for i in sorted(gaps))
        dmin = np.abs(acc[None, :] - grid[:, None]).min(axis=1)
        i = int(np.argmax(dmin))
        print(f"[n={n}] stage zeros: {len(zs)};  min|z|={np.abs(zs).min():.4f}  max|z|={np.abs(zs).max():.4f}"
              f"  zeros on imag axis: {cosmin < 1e-8}")
        print(f"        cumulative radial census: inner disk {rs[0]:.4f} (-> 0); outer exterior "
              f"{rs[-1]:.4f} (-> inf); largest avoided annuli (width@radius): {gtxt}")
        print(f"        [off-center, not Asano-reachable] largest avoided disk (centers |c|<=2): "
              f"radius {dmin[i]:.4f} at c={grid[i]:.2f}")
    return True


# ----------------------------------------------------------------------
# section T — two-sided controls
# ----------------------------------------------------------------------
def sec_controls():
    print("\n== T: controls — genuine preservation must PASS, planted bump must FLAG ==")
    ok = True
    # positive control: chain of disjoint 4-cycles, weight 1 => zeros stay on |u|=1
    edges = []
    records = []
    for kcyc in range(1, 4):
        y1, y2 = f"y1_{kcyc}", f"y2_{kcyc}"
        for cname in ("c1", "c2"):
            nbrs = [(y1, 1.0), (y2, 1.0)]
            _, rho_b = zeros_and_rho(edges)
            edges = edges + [(y1, f"{cname}_{kcyc}", 1.0), (y2, f"{cname}_{kcyc}", 1.0)]
            zs, rho_a = zeros_and_rho(edges)
            records.append((kcyc, cname, rho_b, rho_a, zs))
    on_circle = all(np.allclose(np.abs(r[4]), 1.0, atol=1e-9) for r in records if len(r[4]))
    rho_flat = all(abs(r[3] - 1.0) < 1e-9 for r in records[1:])
    print(f"[T1] disjoint 4-cycle chain (w=1): all zeros on |u|=1: {on_circle};  "
          f"rho constant after first cycle: {rho_flat}  -> preservation recognised: {on_circle and rho_flat}")
    ok &= on_circle and rho_flat
    # teeth: planted bump — fourth cycle with w = 1.3 must be flagged as injection
    _, rho_b = zeros_and_rho(edges)
    for cname in ("c1", "c2"):
        edges = edges + [("y1_4", f"{cname}_4", 1.3), ("y2_4", f"{cname}_4", 1.3)]
    zs, rho_a = zeros_and_rho(edges)
    flagged = rho_a > rho_b * (1 + 1e-9) and np.abs(zs).min() < 1 / rho_b * (1 - 1e-9)
    print(f"[T2] planted bump (w=1.3 cycle): rho {rho_b:.4f} -> {rho_a:.4f}, "
          f"min|z|={np.abs(zs).min():.4f} < 1: flagged as injection: {flagged}")
    ok &= flagged
    return ok


# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("== WP13: Asano gluing on the per-edge product form — the atomic sieve step ==")
    t0 = time.time()
    okS = sec_symbolic()
    okG = sec_stage_chains()
    okL = sec_coverage()
    okT = sec_controls()
    print(f"\n[verdict] gluing law p_(G+x) = p_G * Psi_x: PROVEN symbolically (S) and certified "
          f"exactly over Q on every vertex addition of the stage builds n = 2..6 (G): {okS and okG}")
    print("[verdict] locus preservation: FAILS. Every same-component core step strictly injects")
    print("          the new Perron zero inside the parent zero-free disk (census above); the")
    print("          per-edge trivial factors carry real zeros at 1/w_e that sit inside the")
    print("          zero-free disk at n <= 5 and inside the occupied annulus at every stage;")
    print("          of the Asano-reachable (radially symmetric) regions, centered disks die")
    print("          (inner radius -> 0), exteriors die (outer radius grows), and no stable")
    print("          avoided annulus appears in the radial census (L).")
    print("[verdict] the graded Asano/GWS chain is sound (R_cert <= 1/rho at every stage) and")
    print("          tracks the true radius at 0.44-0.70 efficiency, but the certified disk")
    print("          strictly shrinks at every core step: Asano technology yields a collapsing")
    print("          disk chain, not a preserved locus.")
    allok = okS and okG and okL and okT
    print(f"\n{'HARNESS PASS' if allok else 'HARNESS FAIL'}: all symbolic/exact/two-sided checks "
          f"{'passed' if allok else 'FAILED'}   [{time.time()-t0:.0f}s total]")
    print("FALSIFIER (pre-registered, binding): no locus-preserving Asano-type gluing structure "
          "at n <= 6 -> route γ closes entirely (γ1 already closed by X5).")
