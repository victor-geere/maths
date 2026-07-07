"""wp07_gap_census.py — PSC2-WP07 (G3): normalised-gap census to n = 15 and the
numerical verification of every ingredient of the uniform-gap theorem (PSC2-F04).

Objects (N00 §3 / prime_graph_lab conventions): P_n = primes < 2^n; C_n = composites in
I_n = [2^n, 2^{n+1}); W[p,m] = v_p(m) p^{-1/2}; one-mode S = W W^T on P_n;
d_p = row sums of S; L = D^{-1/2} S D^{-1/2} (top eigenvalue exactly 1, since D^{-1}S is
row-stochastic); g_sym(n) = 1 - lambda_2(L); g_raw(n) = 1 - lambda_2(S)/lambda_1(S).

PRE-REGISTERED CRITERIA (fixed before any n >= 10 was computed; n = 6..9 are N00 anchors):
  CENSUS — conjecture G3 survives iff min_{4<=n<=15} g_sym >= 0.40 and the last four
  stages are not strictly decreasing; otherwise census drift: record, falsifier branch.
  PROOF INGREDIENTS — the following are consequences of the theorem in PSC2-F04 and must
  hold at every computed stage (a violation is an audit finding against the proof):
    I1  S[p,2] >= 2^{-5/2} * 2^n * p^{-3/2}          for every p in P_n
    I2  d_p    <= 45     * 2^n * p^{-3/2}            claimed for n >= 10 (ratio reported all n)
    I3  sum_p d_p >= S[2,2] >= 2^{n-2}
    I4  min_{p,q} P^2(p,q)/pi(q) >= theta := 2^{-11/2} / 45^3   (n >= 10)
    I5  lambda_2(L) <= sqrt(1 - theta)   (with I4 this is the Dobrushin chain; loose)
  CONTROLS (two-sided, rule I0.4/I0.7 spirit):
    - Dobrushin teeth: seeded random reversible chain must satisfy |lambda_2| <= delta(P);
      a planted two-block chain with weak coupling must show g_sym < 0.02 (the metric
      detects near-disconnection — the census cannot pass vacuously).
    - N00 §3 regression: g_raw/g_sym at n = 6..9 must match to 2e-5, and the fast S-builder
      must agree with prime_graph_lab.build_bipartite's S to 1e-10 at n = 6..9.
  Also reported: the proof's convergent constant A = sum_q q^{-1/2}/(q-1) (primes), evaluated
  with a rigorous integer tail bound; and the measured sharpness of I1/I2.

Run:  cd victor && source .venv/bin/activate && python research/numerics/wp07_gap_census.py
"""
import sys
from math import sqrt

sys.path.insert(0, __file__.rsplit("/", 1)[0])

import numpy as np

from prime_graph_lab import build_bipartite, one_mode

RNG = np.random.default_rng(20260707)
NMAX = 15
C_D = 45.0
THETA = 2.0 ** (-5.5) / C_D ** 3


def spf_sieve(limit):
    spf = np.zeros(limit + 1, dtype=np.int64)
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    return spf


def stage_S(n, spf):
    """Dense one-mode S on P_n, built by accumulation over composites (fast builder)."""
    lo, hi = 1 << n, (1 << (n + 1)) - 1
    primes = np.flatnonzero((spf[: lo] == np.arange(lo)) & (np.arange(lo) >= 2))
    pidx = {int(p): i for i, p in enumerate(primes)}
    nP = len(primes)
    S = np.zeros((nP, nP))
    ncomp = 0
    for m in range(lo, hi + 1):
        if spf[m] == m:          # prime in the block: not a composite
            continue
        ncomp += 1
        x, fac = m, []
        while x > 1:
            p = int(spf[x])
            k = 0
            while x % p == 0:
                x //= p
                k += 1
            fac.append((pidx[p], k * float(p) ** -0.5))
        for i, wi in fac:
            for j, wj in fac:
                S[i, j] += wi * wj
    assert ncomp > 0 and np.abs(S).sum() > 0, "vacuity guard"
    return S, primes


def gaps_from_S(S):
    lam = np.linalg.eigvalsh(S)[::-1]
    g_raw = 1 - lam[1] / lam[0]
    d = S.sum(1)
    assert d.min() > 0, "isolated prime (contradicts hub lemma)"
    Ls = S / np.sqrt(np.outer(d, d))
    ls = np.linalg.eigvalsh(Ls)[::-1]
    assert abs(ls[0] - 1.0) < 1e-10, "top eigenvalue must be exactly 1 (stochastic similarity)"
    return g_raw, 1 - ls[1], d, ls


def ingredient_checks(n, S, primes, d, ls):
    p32 = primes.astype(float) ** 1.5
    twon = float(1 << n)
    i2 = int(np.flatnonzero(primes == 2)[0])
    r1 = (S[:, i2] * p32 / twon).min() / 2.0 ** -2.5          # I1: must be >= 1
    r2 = (d * p32 / twon).max() / C_D                          # I2: must be <= 1 (n >= 10)
    r3 = S[i2, i2] / (twon / 4.0)                              # I3: must be >= 1
    P = S / d[:, None]
    pi = d / d.sum()
    P2 = P @ P
    r4 = (P2 / pi[None, :]).min() / THETA                      # I4: must be >= 1 (n >= 10)
    r5 = ls[1] / sqrt(1 - THETA)                               # I5: must be <= 1
    return r1, r2, r3, r4, r5


def constant_A(limit=10 ** 6):
    """A = sum over primes q of q^{-1/2}/(q-1); exact partial sum + integer tail bound
    sum_{k>limit} k^{-3/2} k/(k-1) <= 1.000002 * 2/sqrt(limit)."""
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    q = np.flatnonzero(sieve).astype(float)
    partial = float(np.sum(q ** -0.5 / (q - 1)))
    tail = 1.000002 * 2.0 / sqrt(limit)
    return partial, partial + tail


def dobrushin_controls():
    # random reversible chain (seeded): |lambda_2| <= delta(P) must hold
    k = 40
    Wsym = RNG.uniform(0.1, 1.0, (k, k))
    Wsym = Wsym + Wsym.T
    d = Wsym.sum(1)
    P = Wsym / d[:, None]
    lam = np.sort(np.abs(np.linalg.eigvals(P)))[::-1]
    delta = max(0.5 * np.abs(P[i] - P[j]).sum() for i in range(k) for j in range(k))
    ok_a = lam[1] <= delta + 1e-12
    # planted two-block chain, eps coupling: metric must detect near-disconnection
    eps = 1e-3
    B = np.ones((k, k)) * eps
    B[: k // 2, : k // 2] = 1.0
    B[k // 2:, k // 2:] = 1.0
    db = B.sum(1)
    Lb = B / np.sqrt(np.outer(db, db))
    lb = np.linalg.eigvalsh(Lb)[::-1]
    g_block = 1 - lb[1]
    ok_b = g_block < 0.02
    print(f"[teeth] random reversible: |lam2|={lam[1]:.4f} <= delta={delta:.4f}: {ok_a};   "
          f"two-block eps={eps}: g_sym={g_block:.5f} < 0.02 (detected): {ok_b}")
    return ok_a and ok_b


if __name__ == "__main__":
    print("== WP07 (G3): normalised-gap census n = 4..15 + uniform-gap theorem ingredients ==")
    print(f"   theorem constants: C_d = {C_D:.0f}, theta = 2^(-11/2)/C_d^3 = {THETA:.3e}, "
          f"proven uniform gap c0 >= theta/2 = {THETA/2:.3e} (n >= 10)")
    Ap, Atot = constant_A()
    print(f"   proof constant A = sum_q q^(-1/2)/(q-1): partial(1e6) = {Ap:.6f}, "
          f"with tail bound <= {Atot:.6f}  (proof uses A <= 1.35: {Atot <= 1.35})")
    allok = dobrushin_controls()

    spf = spf_sieve((1 << (NMAX + 1)) - 1)
    n00 = {6: (0.80627, 0.55061), 7: (0.78667, 0.53722),
           8: (0.81016, 0.56641), 9: (0.80372, 0.56004)}
    print("\n    n   |P_n|    g_raw     g_sym     I1>=1     I2<=1     I3>=1     I4>=1     I5<=1")
    gs = {}
    for n in range(4, NMAX + 1):
        S, primes = stage_S(n, spf)
        if 6 <= n <= 9:   # regression: fast builder vs prime_graph_lab (rule I0.5)
            Sl = one_mode(build_bipartite(n, quiet=True)[0])
            assert np.abs(S - Sl).max() < 1e-10, "fast builder disagrees with build_bipartite"
        g_raw, g_sym, d, ls = gaps_from_S(S)
        r1, r2, r3, r4, r5 = ingredient_checks(n, S, primes, d, ls)
        gs[n] = g_sym
        flag = ""
        if n in n00:
            reg = abs(g_raw - n00[n][0]) < 2e-5 and abs(g_sym - n00[n][1]) < 2e-5
            flag = "  N00: ok" if reg else "  N00: MISMATCH"
            allok &= reg
        ok = (r1 >= 1) and (r3 >= 1) and (r5 <= 1) and (n < 10 or (r2 <= 1 and r4 >= 1))
        allok &= ok
        print(f"   {n:2d}  {len(primes):5d}   {g_raw:.5f}   {g_sym:.5f}   "
              f"{r1:7.3f}   {r2:7.3f}   {r3:7.3f}   {r4:9.3e}   {r5:.5f}{flag}"
              + ("" if ok else "  INGREDIENT VIOLATION"))

    tail = [gs[n] for n in range(NMAX - 3, NMAX + 1)]
    drifting = all(tail[i] > tail[i + 1] for i in range(3))
    gmin = min(gs.values())
    census_pass = (gmin >= 0.40) and not drifting
    print(f"\n[census] min g_sym over n=4..{NMAX}: {gmin:.5f} (>= 0.40: {gmin >= 0.40});  "
          f"last four stages strictly decreasing: {drifting}")
    print(f"[census] pre-registered verdict: {'SURVIVES' if census_pass else 'DRIFT — falsifier branch'}")
    allok &= census_pass
    print(f"\nWP07 CENSUS + INGREDIENTS {'PASS' if allok else 'FAIL'}")
