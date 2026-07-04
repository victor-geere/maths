"""
adele_trace.py — the Weil explicit formula realised as a trace over the adèle class space
X = A_Q / Q^x, decomposed place by place (Connes 1999), with the finite places enumerated by
the composite-generator sieve.

This is the Phase 6 "fix" for the vacuous finite-matrix operator of Phase 3: instead of building
a matrix H_n on a finite-dimensional Hilbert space of prime *positions*, we compute the geometric
(local) side of the trace formula directly on X.  Each place v of Q contributes one local
distribution:

    * archimedean place infinity  ->  pole term + (-g(0) log pi) + Gamma-factor integral;
    * each finite place p         ->  W_p(g) = 2 * sum_{k>=1} (log p) p^{-k/2} g(k log p),
                                      the p-adic principal-value integral of the scaling action
                                      = the prime-power (von Mangoldt) contribution of p alone.

The total arithmetic side is  sum_{p} W_p(g)  — a genuine sum over places, not over a basis of
vectors.  Balanced against the archimedean local term it reproduces the zero side  sum_rho h(gamma_rho)
to full precision.  The sieve of Phase 1 supplies the places p <= M_n stage by stage, with a
proven truncation error (prime-side.md Prop 6.1), demonstrated in `truncation_rate`.

Requires mpmath.  Run:  python adele/adele_trace.py
"""

import mpmath as mp

mp.mp.dps = 35


# ----------------------------------------------------------------------
# Gaussian test pair  h(r) = e^{-t r^2},  g(x) = (1/2 sqrt(pi t)) e^{-x^2/4t}
# (g is the Fourier transform normalisation used in prime-side.md Fact 4.1)
# ----------------------------------------------------------------------
def h_test(r, t):
    return mp.e ** (-t * r ** 2)


def g_test(x, t):
    return 1 / (2 * mp.sqrt(mp.pi * t)) * mp.e ** (-x ** 2 / (4 * t))


# ----------------------------------------------------------------------
# Sieve of the finite places (primes) up to M
# ----------------------------------------------------------------------
def primes_up_to(M):
    if M < 2:
        return []
    sieve = bytearray([1]) * (M + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(M ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p:M + 1:p] = bytearray(len(range(p * p, M + 1, p)))
    return [i for i in range(2, M + 1) if sieve[i]]


# ----------------------------------------------------------------------
# Local terms of the Connes trace formula
# ----------------------------------------------------------------------
def local_finite(p, t):
    """W_p(g) = 2 sum_{k>=1} (log p) p^{-k/2} g(k log p)  — the p-adic place contribution."""
    lp = mp.log(p)
    total, k = mp.mpf(0), 1
    while True:
        term = lp * p ** (mp.mpf(-k) / 2) * g_test(k * lp, t)
        total += term
        if k > 1 and term < mp.mpf(10) ** (-(mp.mp.dps + 8)):
            break
        k += 1
    return 2 * total


def local_archimedean(t):
    """Archimedean place: pole term - g(0) log pi + (1/2pi) int h(r) Re psi(1/4 + i r/2) dr."""
    pole = h_test(mp.mpf("0.5") * 1j, t) + h_test(-mp.mpf("0.5") * 1j, t)   # = 2 e^{t/4}
    g0log = g_test(0, t) * mp.log(mp.pi)
    integrand = lambda r: h_test(r, t) * mp.re(mp.digamma(mp.mpf("0.25") + 1j * r / 2))
    integral = mp.quad(integrand, [-mp.inf, 0, mp.inf]) / (2 * mp.pi)
    return pole - g0log, integral


def arithmetic_side(M, t):
    """sum over finite places p <= M of the local term W_p — the adelic geometric prime side."""
    return mp.fsum(local_finite(p, t) for p in primes_up_to(M))


def zero_side(t, n_zeros=40):
    """sum_rho h(gamma_rho) = 2 sum_{gamma>0} e^{-t gamma^2}, truncated where negligible."""
    total = mp.mpf(0)
    for k in range(1, n_zeros + 1):
        g = mp.im(mp.zetazero(k))
        term = h_test(g, t)
        total += term
        if term < mp.mpf(10) ** (-(mp.mp.dps + 8)):
            break
    return 2 * total


# ----------------------------------------------------------------------
# Reports
# ----------------------------------------------------------------------
def place_breakdown(t=mp.mpf("0.2"), M=97):
    print("=" * 72)
    print(f"PLACE-BY-PLACE geometric side of the Connes trace formula  (t={t})")
    print("=" * 72)
    print(f"  {'place':>8} {'local term W_v(g)':>34}")
    a_pole, a_int = local_archimedean(t)
    print(f"  {'infinity':>8} {mp.nstr(a_pole + a_int, 20):>34}   (pole + Gamma integral)")
    running = mp.mpf(0)
    for p in primes_up_to(M):
        w = local_finite(p, t)
        running += w
        print(f"  {p:>8} {mp.nstr(w, 20):>34}")
    print(f"  {'sum p':>8} {mp.nstr(running, 20):>34}   (arithmetic side, p<= %d)" % M)


def truncation_rate(eps=mp.mpf("0.5")):
    """prime-side.md Prop 6.1: sum_{q<=M} Lambda(q) q^{-1-eps} -> -zeta'/zeta(1+eps),
    tail <= C M^{-eps}.  Show |target - partial| * M^{eps} stays bounded."""
    print("\n" + "=" * 72)
    print(f"TRUNCATION RATE (Prop 6.1):  sum_q<=M_n Lambda(q) q^-(1+eps) -> -zeta'/zeta(1+eps)")
    print(f"                             error should be O(M_n^-eps),  here eps={eps}")
    print("=" * 72)
    target = -mp.zeta(1 + eps, derivative=1) / mp.zeta(1 + eps)
    print(f"  target -zeta'/zeta(1+{eps}) = {mp.nstr(target, 20)}")
    print(f"  {'n':>3} {'M_n':>9} {'partial sum':>24} {'|error|':>14} {'|error|*M_n^eps':>16}")
    for n in range(8, 21, 2):
        M = (1 << (n + 1)) - 1
        s = mp.mpf(0)
        for p in primes_up_to(M):
            lp = mp.log(p)
            k = 1
            while p ** k <= M:
                s += lp * (p ** k) ** (-(1 + eps))
                k += 1
        err = abs(target - s)
        print(f"  {n:>3} {M:>9} {mp.nstr(s, 18):>24} {mp.nstr(err, 8):>14} "
              f"{mp.nstr(err * M ** eps, 8):>16}")


def balance(t):
    a_pole, a_int = local_archimedean(t)
    arith = arithmetic_side((1 << 14) - 1, t)     # p <= 16383, far beyond needed for Gaussian
    zeros = zero_side(t)
    rhs = a_pole + a_int - arith
    return a_pole, a_int, arith, zeros, rhs


def balance_report():
    print("\n" + "=" * 72)
    print("EXPLICIT-FORMULA BALANCE  (adelic):  sum_rho h(gamma) == W_infinity - sum_p W_p")
    print("=" * 72)
    for t in (mp.mpf("0.05"), mp.mpf("0.2")):
        a_pole, a_int, arith, zeros, rhs = balance(t)
        print(f"\n  t = {t}")
        print(f"    W_inf pole part  h(i/2)+h(-i/2)-g(0)log pi : {mp.nstr(a_pole, 18)}")
        print(f"    W_inf Gamma integral                       : {mp.nstr(a_int, 18)}")
        print(f"    arithmetic side  sum_p W_p(g)              : {mp.nstr(arith, 18)}")
        print(f"    right side  W_inf - arithmetic             : {mp.nstr(rhs, 20)}")
        print(f"    zero side   sum_rho h(gamma_rho)           : {mp.nstr(zeros, 20)}")
        print(f"    discrepancy                                : {mp.nstr(abs(rhs - zeros), 6)}")


if __name__ == "__main__":
    place_breakdown()
    balance_report()
    truncation_rate()
