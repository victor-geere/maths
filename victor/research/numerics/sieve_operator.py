"""
sieve_operator.py — numerical core for the "Prime Sieve on the Adèle Class Space" program.

Standalone (no Streamlit). Implements, for the dyadic block I_n = [2^n, 2^{n+1}-1]:

  * the composite-generator sieve (primes = gaps in the composite generator);
  * Phase 1 diagnostic:  Fourier decay of the normalised prime measure  ->  O(1/log M_n);
  * Phase 3:             the Sieving Laplacian  H_n = D_n + eps_n A  (Def 4.1 of the plan);
  * Phase 4:             eps-scaling, unfolding of Spec(H_n), and comparison with Riemann zeros.

Run:  python sieve_operator.py
This prints the tables that are quoted (verbatim) in phase1.md / phase3.md / phase4.md.
"""

import numpy as np
from math import log, exp, pi

# ----------------------------------------------------------------------
# 1. Number-theoretic helpers
# ----------------------------------------------------------------------
def sieve_of_eratosthenes(limit: int) -> np.ndarray:
    if limit < 2:
        return np.array([], dtype=int)
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p: limit + 1: p] = False
    return np.flatnonzero(is_prime)


def prime_factors(x: int, primes: np.ndarray) -> dict:
    """Return {p: exponent}. `primes` must cover all prime divisors of x."""
    factors, y = {}, x
    for p in primes:
        if p * p > y:
            break
        if y % p == 0:
            c = 0
            while y % p == 0:
                y //= p
                c += 1
            factors[int(p)] = c
    if y > 1:
        factors[int(y)] = factors.get(int(y), 0) + 1
    return factors


def rad(x: int, primes: np.ndarray) -> int:
    if x == 1:
        return 1
    r, y = 1, x
    for p in primes:
        if p * p > y:
            break
        if y % p == 0:
            r *= int(p)
            while y % p == 0:
                y //= p
    if y > 1:
        r *= int(y)
    return r


# ----------------------------------------------------------------------
# 2. The dyadic sieve block
# ----------------------------------------------------------------------
def generate_sieve_data(n: int):
    """Primes in I_n, composites in I_n, primes < 2^n, and M_n = 2^{n+1}-1."""
    M_n = (1 << (n + 1)) - 1
    all_primes = sieve_of_eratosthenes(M_n)
    primes_lt_2n = all_primes[all_primes < (1 << n)]
    lo, hi = 1 << n, M_n
    primes_in_I = all_primes[(all_primes >= lo) & (all_primes <= hi)].tolist()
    all_int = np.arange(lo, hi + 1)
    composites_in_I = all_int[~np.isin(all_int, primes_in_I)].tolist()
    return primes_in_I, composites_in_I, primes_lt_2n, M_n


# ----------------------------------------------------------------------
# 3. Phase 1 diagnostic: equidistribution of the normalised prime measure
#    mu_n = (1/k_n) sum_{p<=M_n} delta_{p/M_n};  hat mu_n(k) = O_k(1/log M_n).
# ----------------------------------------------------------------------
def prime_measure_fourier(n: int, ks=(1, 2, 3)):
    M_n = (1 << (n + 1)) - 1
    primes = sieve_of_eratosthenes(M_n).astype(float)
    k_n = len(primes)
    out = {}
    for k in ks:
        c = np.mean(np.exp(2j * pi * k * primes / M_n))
        out[k] = abs(c)
    return M_n, k_n, out


# ----------------------------------------------------------------------
# 4. Phase 3: the Sieving Laplacian  H_n = D_n + eps_n A
# ----------------------------------------------------------------------
def compute_leakage_matrix(primes_in_I, composites_in_I, primes_lt_2n):
    """A_{p,q} = sum_{m composite in I_n} a_p(m) a_q(m) / rad(m), off-diagonal (Def 4.1)."""
    idx = {p: i for i, p in enumerate(primes_in_I)}
    N = len(primes_in_I)
    A = np.zeros((N, N))
    for m in composites_in_I:
        fac = prime_factors(m, primes_lt_2n)
        r = rad(m, primes_lt_2n)
        if r == 0:
            continue
        items = [(p, e) for p, e in fac.items() if p in idx]
        for i in range(len(items)):
            p, ep = items[i]
            for j in range(i + 1, len(items)):
                q, eq = items[j]
                w = (ep * eq) / r
                A[idx[p], idx[q]] += w
                A[idx[q], idx[p]] += w
    return A


def compute_leakage_matrix_repaired(primes_lt_2n, composites_in_I):
    """REPAIR of Def 4.1: couple primes p,q < 2^n through composites m in I_n.

    The plan's basis V_n = {primes in I_n} makes A identically zero, because a
    composite m in [2^n, 2^{n+1}) cannot have two DISTINCT prime factors both
    >= 2^n (their product would be >= 2^{2n} >> 2^{n+1}).  Using the sieve
    primes p < 2^n as the basis instead gives a genuinely coupled matrix.
    """
    basis = [int(p) for p in primes_lt_2n]
    idx = {p: i for i, p in enumerate(basis)}
    N = len(basis)
    A = np.zeros((N, N))
    for m in composites_in_I:
        fac = prime_factors(m, primes_lt_2n)
        r = rad(m, primes_lt_2n)
        if r == 0:
            continue
        items = [(p, e) for p, e in fac.items() if p in idx]
        for i in range(len(items)):
            p, ep = items[i]
            for j in range(i + 1, len(items)):
                q, eq = items[j]
                w = (ep * eq) / r
                A[idx[p], idx[q]] += w
                A[idx[q], idx[p]] += w
    return A, basis


def build_Hn_repaired(n: int, C: float = 1.0):
    """The repaired Sieving Laplacian H_n' = D_n' + eps_n A' on basis {primes < 2^n}."""
    _, composites_in_I, primes_lt_2n, M_n = generate_sieve_data(n)
    A, basis = compute_leakage_matrix_repaired(primes_lt_2n, composites_in_I)
    if not basis:
        return None, [], M_n, None
    log_vals = np.array([log(p) for p in basis])
    D = np.diag(log_vals - log_vals.mean())
    eps = C / log(M_n)
    return D + eps * A, basis, M_n, A


def build_Hn(n: int, C: float = 1.0):
    primes_in_I, composites_in_I, primes_lt_2n, M_n = generate_sieve_data(n)
    if not primes_in_I:
        return None, [], M_n, None
    A = compute_leakage_matrix(primes_in_I, composites_in_I, primes_lt_2n)
    log_vals = np.array([log(p) for p in primes_in_I])
    D = np.diag(log_vals - log_vals.mean())          # trace-zero diagonal
    eps = C / log(M_n)
    H = D + eps * A
    return H, primes_in_I, M_n, A


# ----------------------------------------------------------------------
# 5. Phase 4: unfolding and Riemann-zero comparison
# ----------------------------------------------------------------------
def zero_count(t: float) -> float:
    if t <= 1e-10:
        return 0.0
    return (t / (2 * pi)) * (log(t / (2 * pi)) - 1) + 7 / 8


def invert_zero_count(target: float, tol=1e-12, max_iter=60) -> float:
    if target <= 0:
        return 0.0
    T = 2 * pi * exp(1)
    for _ in range(max_iter):
        N = zero_count(T)
        dN = (1 / (2 * pi)) * log(T / (2 * pi))
        if dN == 0:
            break
        Tn = T - (N - target) / dN
        if abs(Tn - T) < tol:
            return Tn
        T = Tn
    return T


def get_riemann_zeros(num_zeros: int) -> np.ndarray:
    try:
        import mpmath
        return np.array([float(mpmath.zetazero(k).imag) for k in range(1, num_zeros + 1)])
    except ImportError:
        return np.array([invert_zero_count(k - 0.5) for k in range(1, num_zeros + 1)])


# ----------------------------------------------------------------------
# 6. Report
# ----------------------------------------------------------------------
def phase1_report():
    print("=" * 72)
    print("PHASE 1  —  Fourier decay of the normalised prime measure  |hat mu_n(k)|")
    print("           (Theorem 3.1: O_k(1/log M_n));  ratio col should be ~ constant")
    print("=" * 72)
    print(f"{'n':>3} {'M_n':>9} {'k_n=pi(M_n)':>12} {'|mu(1)|':>10} {'|mu(2)|':>10} "
          f"{'|mu(3)|':>10} {'|mu(1)|*logM_n':>14}")
    for n in range(8, 21):
        M_n, k_n, c = prime_measure_fourier(n)
        print(f"{n:>3} {M_n:>9} {k_n:>12} {c[1]:>10.5f} {c[2]:>10.5f} "
              f"{c[3]:>10.5f} {c[1] * log(M_n):>14.4f}")


def phase3_report():
    print("\n" + "=" * 72)
    print("PHASE 3  —  the Sieving Laplacian  H_n = D_n + eps_n A   (eps_n = 1/log M_n)")
    print("=" * 72)
    print(f"{'n':>3} {'M_n':>9} {'N=|V_n|':>9} {'eps_n':>9} {'||A||_op':>10} "
          f"{'min eig H':>11} {'max eig H':>11}")
    for n in range(8, 17):
        H, primes, M_n, A = build_Hn(n, C=1.0)
        if H is None:
            continue
        ev = np.linalg.eigvalsh(H)
        a_op = np.linalg.norm(A, 2) if A.size else 0.0
        eps = 1.0 / log(M_n)
        print(f"{n:>3} {M_n:>9} {len(primes):>9} {eps:>9.5f} {a_op:>10.4f} "
              f"{ev.min():>11.5f} {ev.max():>11.5f}")


def phase4_report():
    print("\n" + "=" * 72)
    print("PHASE 4  —  spectral shift vs eps (does off-diagonal move the spectrum?)")
    print("=" * 72)
    n = 14
    H0, primes, M_n, A = build_Hn(n, C=0.0)
    ev0 = np.linalg.eigvalsh(H0)
    print(f"n={n}, M_n={M_n}, N={len(primes)}, std(diag spectrum)={ev0.std():.5f}")
    print(f"{'C':>6} {'eps_n':>10} {'std(Spec)':>12} {'mean|shift|':>12}")
    for C in (0.0, 0.5, 1.0, 2.0, 5.0, 10.0):
        H, _, _, _ = build_Hn(n, C=C)
        ev = np.linalg.eigvalsh(H)
        shift = np.mean(np.abs(ev - ev0))
        print(f"{C:>6.1f} {C / log(M_n):>10.5f} {ev.std():>12.5f} {shift:>12.6f}")

    print("\n  Unfolding Spec(H_n) and comparing with Riemann zeros (imag parts):")
    print("  (raw eigenvalue *density* in I_n is ~exponential; zeros' is ~log.")
    print("   The plan CONJECTURES an affine rescaling reconciles them — tested here.)")
    H, primes, M_n, A = build_Hn(n, C=1.0)
    ev = np.sort(np.linalg.eigvalsh(H))
    zeros = get_riemann_zeros(len(ev))
    # affine fit  gamma ~ alpha*ev + beta  (least squares) then report residual
    alpha, beta = np.polyfit(ev, zeros, 1)
    pred = alpha * ev + beta
    rms = np.sqrt(np.mean((pred - zeros) ** 2))
    print(f"  best affine fit gamma ~ {alpha:.4f} * lambda + {beta:.4f}")
    print(f"  RMS residual over {len(ev)} eigenvalues: {rms:.4f}  "
          f"(zeros span {zeros.min():.2f}..{zeros.max():.2f})")
    print(f"  first 6 zeros:      {np.round(zeros[:6], 3)}")
    print(f"  first 6 fitted:     {np.round(pred[:6], 3)}")


def repair_report():
    print("\n" + "=" * 72)
    print("REPAIR CHECK  —  Def 4.1 basis V_n={primes in I_n} gives A==0 (see phase3.md)")
    print("               V_n={primes < 2^n} instead gives a genuinely coupled A")
    print("=" * 72)
    print(f"{'n':>3} {'dim V':>7} {'||A||_op':>10} {'nnz(A)':>9} {'eps_n*||A||':>12}")
    for n in range(8, 15, 2):
        pI, cI, plt2n, M_n = generate_sieve_data(n)
        A, basis = compute_leakage_matrix_repaired(plt2n, cI)
        op = np.linalg.norm(A, 2) if A.size else 0.0
        eps = 1.0 / log(M_n)
        print(f"{n:>3} {len(basis):>7} {op:>10.4f} {int((A != 0).sum()):>9} {eps * op:>12.4f}")
    print("  -> eps_n*||A|| grows past 1: the off-diagonal is NOT a small perturbation.")


def repaired_trace_report():
    """Produce Tr g(H_n') for the repaired operator, split into diagonal + off-diagonal
    correction, and set it beside the *honest* arithmetic (von Mangoldt) side that the
    explicit formula actually uses.  They are different objects — this is precisely why the
    fix lives in adèle space (phase6.md / adele_trace.py), not in a finite matrix."""
    t = 0.2
    g = lambda x: 1.0 / (2 * np.sqrt(np.pi * t)) * np.exp(-x ** 2 / (4 * t))
    print("\n" + "=" * 72)
    print(f"REPAIRED-OPERATOR TRACE  Tr g(H_n'),  Gaussian g,  t={t}   (see phase4.md §4.5)")
    print("=" * 72)
    hdr = "{:>3} {:>6} {:>13} {:>13} {:>14} {:>13}".format(
        "n", "dim", "Tr g(diag)", "Tr g(H_rep)", "off-diag corr", "arith side")
    print(hdr)
    for n in range(8, 15):
        primes_in_I, composites_in_I, primes_lt_2n, M_n = generate_sieve_data(n)
        H, basis, _, _ = build_Hn_repaired(n, C=1.0)
        ev = np.linalg.eigvalsh(H)
        log_vals = np.array([log(p) for p in basis])
        diag = log_vals - log_vals.mean()
        tr_full = g(ev).sum()
        tr_diag = g(diag).sum()
        # honest arithmetic side truncated by the sieve: 2 sum_{q<=M_n} Lambda(q)/sqrt(q) g(log q)
        arith = 0.0
        for p in primes_lt_2n.tolist() + primes_in_I:
            lp = log(p)
            k = 1
            while p ** k <= M_n:
                arith += 2 * lp / (p ** k) ** 0.5 * g(k * lp)
                k += 1
        print(f"{n:>3} {len(basis):>6} {tr_diag:>13.6f} {tr_full:>13.6f} "
              f"{tr_full - tr_diag:>14.6f} {arith:>13.6f}")
    print("  -> Tr g(H_n') (a finite matrix on prime *positions*) does NOT converge to the")
    print("     arithmetic side; the correct trace is the adelic per-place sum (phase6).")


if __name__ == "__main__":
    phase1_report()
    phase3_report()
    phase4_report()
    repair_report()
    repaired_trace_report()
