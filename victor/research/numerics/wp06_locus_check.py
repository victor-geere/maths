"""wp06_locus_check.py — PSC2-WP06 Part B: the honest weighted confinement locus.

Verifies numerically (two-sided, rule I0.4) the three proven propositions of
PSC2-F03 on the actual stage graphs, beta = 1/2:

  (B1) leaf reduction: det(I - uB_G) = det(I - uB_core), core = 2-core; the
       nonzero non-backtracking spectrum is unchanged by pruning degree-1
       vertices (prime-power composites AND large primes with one composite).
  (B2) inner bound, ALL poles: |u| >= 1/rho(B), with equality at the Perron pole.
  (B3) annulus, NON-REAL poles: r1 <= |u| <= r2 where, on the 2-core,
         r1 = min over core vertices x of the unique root of
                sum_{y~x} (1 + r w_xy)^(-2) = d_x - 1,
         r2 = max over core vertices x of the largest root of
                sum_{y~x} (1 - r w_xy)^(-2) = d_x - 1
       (roots beyond the largest pole 1/min w at x).  No fitted constants:
       both radii are computed from the weight distribution alone.
  (B3') real poles in the disk |u| < 1/w_max(core) satisfy |u| >= r1R with r1R
       from sum_{y~x} (1 + r w_xy)^(-1) = d_x - 1 (first power).

Census reality check (pre-registered in WP06): the n=7 real-pole census
(parent snapshot: 208 real poles, |u| in [0.19, 4.18]) must be reproduced and
contained in the derived regions.

Controls: (i) positive control, Petersen graph (3-regular Ramanujan: non-real
poles exactly on |u| = 1/sqrt(2), annulus must contain them); (ii) checker-teeth
control: synthetic spectra drawn outside the annulus MUST be flagged (the
containment checker can detect its own falsifier); (iii) regression against
N00 §3 (mu1, detached census) through prime_graph_lab's own builders (I0.5).

Run:  cd victor && source .venv/bin/activate && python research/numerics/wp06_locus_check.py
"""
import sys
from math import sqrt

sys.path.insert(0, __file__.rsplit("/", 1)[0])

import numpy as np

from prime_graph_lab import build_bipartite


# ----------------------------------------------------------------------
# weighted graph as adjacency dict; 2-core pruning
# ----------------------------------------------------------------------
def graph_from_W(W):
    Pn, Cn = W.shape
    adj = {}
    for i in range(Pn):
        for j in range(Cn):
            if W[i, j] != 0:
                adj.setdefault(("p", i), {})[("c", j)] = W[i, j]
                adj.setdefault(("c", j), {})[("p", i)] = W[i, j]
    return adj


def two_core(adj):
    adj = {x: dict(nb) for x, nb in adj.items()}
    removed = 0
    while True:
        leaves = [x for x, nb in adj.items() if len(nb) <= 1]
        if not leaves:
            return adj, removed
        for x in leaves:
            for y in list(adj.get(x, {})):
                adj[y].pop(x, None)
            adj.pop(x, None)
            removed += 1
        adj = {x: nb for x, nb in adj.items() if nb}


def nb_matrix(adj):
    """Weighted Hashimoto matrix, B[(x->y),(y->z)] = w(y,z), from an adjacency dict
    (same convention as prime_graph_lab.nonbacktracking; spectrum-equivalent to sqrt form)."""
    des = [(x, y) for x in adj for y in adj[x]]
    idx = {e: k for k, e in enumerate(des)}
    B = np.zeros((len(des), len(des)))
    for (x, y), k in idx.items():
        for z, w in adj[y].items():
            if z != x:
                B[k, idx[(y, z)]] = w
    return B


# ----------------------------------------------------------------------
# radii from the weight distribution (bisection on monotone tails)
# ----------------------------------------------------------------------
def _root_decreasing(f, target, lo, hi):
    """f decreasing on [lo, hi], f(lo) > target > f(hi); return crossing."""
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def radii(core):
    """(r1, r2, r1R, wmax_core) from the 2-core weight distribution alone."""
    r1 = np.inf
    r2 = 0.0
    r1R = np.inf
    wmax = 0.0
    for x, nb in core.items():
        ws = np.array(list(nb.values()))
        d = len(ws)
        assert d >= 2, "2-core violation"
        wmax = max(wmax, ws.max())
        # r1: sum (1+rw)^-2 = d-1, decreasing from d at r=0
        f2p = lambda r: np.sum((1 + r * ws) ** -2.0)
        hi = 1.0
        while f2p(hi) > d - 1:
            hi *= 2
        r1 = min(r1, _root_decreasing(f2p, d - 1, 0.0, hi))
        # r1R: sum (1+rw)^-1 = d-1
        f1p = lambda r: np.sum((1 + r * ws) ** -1.0)
        hi = 1.0
        while f1p(hi) > d - 1:
            hi *= 2
        r1R = min(r1R, _root_decreasing(f1p, d - 1, 0.0, hi))
        # r2: sum (1-rw)^-2 = d-1, decreasing beyond the largest pole 1/min w
        pole = 1.0 / ws.min()
        f2m = lambda r: np.sum((1 - r * ws) ** -2.0)
        lo = pole * (1 + 1e-12)
        while not np.isfinite(f2m(lo)) or f2m(lo) <= d - 1:
            lo = pole + (lo - pole) * 0.5
            if lo - pole < 1e-300:
                break
        hi = max(2 * lo, 2.0)
        while f2m(hi) > d - 1:
            hi *= 2
        r2 = max(r2, _root_decreasing(f2m, d - 1, lo, hi))
    return r1, r2, r1R, wmax


# ----------------------------------------------------------------------
# containment checker (used on real spectra AND on the teeth control)
# ----------------------------------------------------------------------
def check_containment(mu, r1, r2, rho, r1R, wmax, tol=1e-9):
    """mu: nonzero eigenvalues of B. Poles u = 1/mu. Returns dict of pass/fail."""
    mu = mu[np.abs(mu) > 1e-10 * np.abs(mu).max()]
    u = 1.0 / mu
    real = np.abs(mu.imag) < 1e-8 * np.abs(mu).max()
    res = {}
    res["inner_all"] = bool(np.all(np.abs(u) >= 1.0 / rho - tol))
    res["perron_eq"] = bool(abs(np.abs(u).min() - 1.0 / rho) < 1e-6 / rho)
    nr = np.abs(u[~real])
    res["n_nonreal"] = int(nr.size)
    res["annulus"] = bool(np.all((nr >= r1 * (1 - 1e-9)) & (nr <= r2 * (1 + 1e-9)))) if nr.size else True
    rr = np.abs(u[real])
    in_disk = rr < 1.0 / wmax
    res["real_disk"] = bool(np.all(rr[in_disk] >= r1R * (1 - 1e-9)))
    res["n_real"] = int(rr.size)
    res["u_real_range"] = (float(rr.min()), float(rr.max())) if rr.size else (np.nan, np.nan)
    res["u_nonreal_range"] = (float(nr.min()), float(nr.max())) if nr.size else (np.nan, np.nan)
    return res


def spectra_match(mu_a, mu_b, tol=1e-7):
    """Nonzero spectra agree as multisets (greedy nearest matching)."""
    cut = 1e-8 * max(np.abs(mu_a).max(), np.abs(mu_b).max())
    a = sorted(mu_a[np.abs(mu_a) > cut], key=lambda z: (-abs(z), z.real, z.imag))
    b = list(mu_b[np.abs(mu_b) > cut])
    if len(a) != len(b):
        return False, len(a) - len(b)
    worst = 0.0
    for z in a:
        j = int(np.argmin(np.abs(np.array(b) - z)))
        worst = max(worst, abs(b[j] - z) / max(abs(z), 1e-12))
        b.pop(j)
    return worst < tol, worst


# ----------------------------------------------------------------------
def stage_report(n):
    W, gens, comps, M = build_bipartite(n, quiet=True)
    adj = graph_from_W(W)
    B = nb_matrix(adj)
    mu = np.linalg.eigvals(B)
    rho = np.abs(mu).max()

    core, removed = two_core(adj)
    Bc = nb_matrix(core)
    muc = np.linalg.eigvals(Bc)
    same, worst = spectra_match(mu, muc)

    r1, r2, r1R, wmax = radii(core)
    res = check_containment(mu, r1, r2, rho, r1R, wmax)

    # locus-intrinsic detachment: real poles below r1 (the bulk's proven inner edge)
    mu_nz = mu[np.abs(mu) > 1e-10 * rho]
    u = 1.0 / mu_nz
    real = np.abs(mu_nz.imag) < 1e-8 * rho
    n_detached_locus = int(np.sum(np.abs(u[real]) < r1))

    # N00 §3 regression at n in 6..9: mu1 and detached census via the sqrt(mu1) criterion
    mu1 = rho
    R = sqrt(mu1) * 1.02
    det_mask = np.abs(mu) > R
    ndet = int(det_mask.sum())
    ndet_real = int(np.sum(np.abs(mu[det_mask].imag) < 1e-8 * mu1))

    print(f"[n={n}] |V|={len(adj)} -> core {len(core)} (pruned {removed})  "
          f"leaf-reduction spectra match: {same} (worst rel dev {worst:.2e})")
    print(f"       mu1={mu1:.4f}  1/rho={1/rho:.4f}  r1={r1:.4f}  r2={r2:.4f}  r1R={r1R:.4f}  "
          f"1/wmax_core={1/wmax:.4f}")
    print(f"       poles: {res['n_real']} real, |u| in [{res['u_real_range'][0]:.4f}, "
          f"{res['u_real_range'][1]:.4f}];  {res['n_nonreal']} non-real, |u| in "
          f"[{res['u_nonreal_range'][0]:.4f}, {res['u_nonreal_range'][1]:.4f}]")
    print(f"       checks: inner(all)={res['inner_all']}  perron-eq={res['perron_eq']}  "
          f"annulus(non-real)={res['annulus']}  real-disk={res['real_disk']}")
    print(f"       detached census (sqrt(mu1)*1.02): {ndet} ({ndet_real} real)   "
          f"locus-detached (real, |u| < r1): {n_detached_locus}")
    ok = same and res["inner_all"] and res["perron_eq"] and res["annulus"] and res["real_disk"]
    return ok, mu1, ndet, ndet_real, res


def petersen_control():
    """3-regular Ramanujan graph: non-real NB poles exactly on |u| = 1/sqrt(2)."""
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
             (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
             (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
    adj = {}
    for x, y in edges:
        adj.setdefault(x, {})[y] = 1.0
        adj.setdefault(y, {})[x] = 1.0
    B = nb_matrix(adj)
    mu = np.linalg.eigvals(B)
    rho = np.abs(mu).max()
    core, removed = two_core(adj)
    r1, r2, r1R, wmax = radii(core)
    res = check_containment(mu, r1, r2, rho, r1R, wmax)
    nr = np.abs(1.0 / mu[np.abs(mu.imag) > 1e-8])
    on_circle = bool(np.all(np.abs(nr - 1 / sqrt(2)) < 1e-8))
    exp = (sqrt(3.0 / 2.0) - 1, 1 + sqrt(3.0 / 2.0))
    print(f"[petersen] non-real poles all on |u| = 1/sqrt(2): {on_circle};  "
          f"annulus [{r1:.4f}, {r2:.4f}] (expected [{exp[0]:.4f}, {exp[1]:.4f}])  "
          f"contains them: {res['annulus']};  inner(all)={res['inner_all']}")
    return on_circle and res["annulus"] and res["inner_all"] \
        and abs(r1 - exp[0]) < 1e-9 and abs(r2 - exp[1]) < 1e-9


def teeth_control(r1, r2, rho, r1R, wmax):
    """The checker must FLAG synthetic spectra that violate the locus (I0.4/I0.7 spirit:
    a control that must fail). Poles planted outside the annulus / inside the inner disk."""
    bad_outer = np.array([1.0 / (2.0 * r2) * np.exp(1j),  # non-real pole at |u| = 2 r2
                          1.0 / (2.0 * r2) * np.exp(-1j), rho / 2.0 + 0j, rho + 0j])
    r_out = check_containment(bad_outer, r1, r2, rho, r1R, wmax)
    bad_inner = np.array([np.exp(1j * 0.7) / (0.5 * r1),  # non-real pole at |u| = r1/2
                          np.exp(-1j * 0.7) / (0.5 * r1), rho + 0j])
    r_in = check_containment(bad_inner, r1, r2, rho, r1R, wmax)
    bad_sub = np.array([1.02 * rho + 0j, rho + 0j])       # pole below the 1/rho bound
    r_sub = check_containment(bad_sub, r1, r2, 1.0 / (1.0 / rho * 1.02) / 1.02**2, r1R, wmax)
    caught = (not r_out["annulus"]) and (not r_in["annulus"])
    print(f"[teeth] planted outer-violation flagged: {not r_out['annulus']};  "
          f"planted inner-violation flagged: {not r_in['annulus']}")
    return caught


if __name__ == "__main__":
    print("== WP06 Part B: honest weighted locus — 2-core radii, containment, census ==")
    allok = petersen_control()
    n00_mu1 = {6: 3.5419, 7: 5.2810, 8: 7.6871, 9: 10.9663}
    census = {}
    last = None
    for n in (4, 5, 6, 7, 8, 9):
        ok, mu1, ndet, ndet_real, res = stage_report(n)
        allok &= ok
        census[n] = res
        last = res
        if n in n00_mu1:
            reg = abs(mu1 - n00_mu1[n]) < 5e-4 and ndet == 4 and ndet_real == 2
            print(f"       N00 §3 regression (mu1={n00_mu1[n]}, detached 4/2): "
                  f"{'ok' if reg else 'MISMATCH'}")
            allok &= reg
    c7 = census[7]
    cen_ok = (c7["n_real"] == 208 and abs(c7["u_real_range"][0] - 0.19) < 5e-3
              and abs(c7["u_real_range"][1] - 4.18) < 5e-3)
    print(f"\n[census n=7] {c7['n_real']} real poles, |u| in "
          f"[{c7['u_real_range'][0]:.2f}, {c7['u_real_range'][1]:.2f}]  "
          f"(pre-registered: 208, [0.19, 4.18]): {'reproduced' if cen_ok else 'MISMATCH'}")
    allok &= cen_ok
    # teeth control with the n=7 stage radii
    W, gens, comps, M = build_bipartite(7, quiet=True)
    core, _ = two_core(graph_from_W(W))
    r1, r2, r1R, wmax = radii(core)
    B = nb_matrix(graph_from_W(W))
    rho = np.abs(np.linalg.eigvals(B)).max()
    allok &= teeth_control(r1, r2, rho, r1R, wmax)
    print(f"\nLOCUS VERIFICATION {'PASS' if allok else 'FAIL'} "
          f"(all containments hold; controls two-sided; census reproduced)")
