"""Numerical verification for project/ou-process.md section 7.

Four checks on the Ornstein-Uhlenbeck semigroup P_t = e^{tL}, L = d^2/dx^2 - x d/dx
on L^2(R, gamma), gamma(dx) = e^{-x^2/2} dx / sqrt(2 pi):

  1. Mehler closed form M_t(x, y) vs. truncated Hermite bilinear sum (Theorem O3).
  2. Heat trace Tr P_t = 1/(1 - e^{-t}), three ways: eigenvalue sum, closed form,
     and the Mehler diagonal integral int M_t(x, x) gamma(dx)         (Theorem O4).
  3. Bernoulli coefficients: Taylor of t/(e^t - 1) recovers B_k        (Theorem O4).
  4. Mellin trace identity Gamma(s) zeta(s) = int_0^inf t^{s-1} Theta(t) dt with the
     primed trace Theta(t) = 1/(e^t - 1); plus zeta(-k) = -B_{k+1}/(k+1) (Theorem O5).

Run:  python ou-verify.py
Deps: numpy, mpmath.
"""

import importlib.util
import os

import mpmath as mp
import numpy as np

mp.mp.dps = 40  # 40 significant digits

# Load the sibling module whose filename contains a dash (cannot be imported normally).
_spec = importlib.util.spec_from_file_location(
    "prime_zeros", os.path.join(os.path.dirname(__file__), "prime-zeros.py"))
pz = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pz)


def check_1_mehler_vs_hermite():
    """M_t(x, y) closed form vs. truncated Hermite bilinear series."""
    print("=" * 70)
    print("CHECK 1  Mehler closed form vs. truncated Hermite sum")
    print("-" * 70)
    print(f"{'t':>5} {'x':>5} {'y':>5} {'N':>4} {'closed form':>20} {'Hermite sum':>20} {'|diff|':>10}")
    worst = 0.0
    for t in (0.3, 0.7, 1.5):
        for (x, y) in ((0.4, -0.9), (1.2, 1.1), (-2.0, 0.5)):
            closed = float(pz.ou_mehler(t, x, y))
            N = 80
            approx = float(pz.ou_hermite_sum(t, x, y, N))
            d = abs(closed - approx)
            worst = max(worst, d)
            print(f"{t:>5.2f} {x:>5.1f} {y:>5.1f} {N:>4d} {closed:>20.12f} {approx:>20.12f} {d:>10.1e}")
    print(f"\n  worst |closed - Hermite_N| over grid (N=80): {worst:.2e}")
    return worst


def check_2_trace():
    """Tr P_t three ways: geometric sum, closed form, Mehler diagonal integral."""
    print("=" * 70)
    print("CHECK 2  Heat trace  Tr P_t = 1/(1 - e^{-t})")
    print("-" * 70)
    print(f"{'t':>5} {'closed 1/(1-e^-t)':>20} {'eig sum r^n':>20} {'int M_t(x,x)dgamma':>22} {'max|diff|':>10}")
    worst = 0.0
    for t in (0.5, 1.0, 2.0):
        r = mp.e ** (-mp.mpf(t))
        closed = 1 / (1 - r)
        eig = mp.nsum(lambda n: r ** n, [0, mp.inf])
        # int M_t(x, x) e^{-x^2/2}/sqrt(2 pi) dx, computed in high precision.
        r2 = r * r

        def integrand(x, r=r, r2=r2):
            mehler = mp.e ** ((2 * r * x * x - r2 * (x * x + x * x)) / (2 * (1 - r2))) / mp.sqrt(1 - r2)
            return mehler * mp.e ** (-x * x / 2) / mp.sqrt(2 * mp.pi)

        quad = mp.quad(integrand, [-mp.inf, 0, mp.inf])
        d = max(abs(closed - eig), abs(closed - quad))
        worst = max(worst, float(d))
        print(f"{t:>5.2f} {mp.nstr(closed, 14):>20} {mp.nstr(eig, 14):>20} {mp.nstr(quad, 14):>22} {float(d):>10.1e}")
    print(f"\n  worst trace discrepancy: {worst:.2e}")
    return worst


def check_3_bernoulli():
    """Taylor coefficients of t/(e^t - 1) are B_k / k!; recover B_k."""
    print("=" * 70)
    print("CHECK 3  Bernoulli coefficients of  t/(e^t - 1) = sum B_k t^k / k!")
    print("-" * 70)
    coeffs = mp.taylor(lambda t: t / (mp.e ** t - 1) if t != 0 else mp.mpf(1), 0, 8)
    print(f"{'k':>3} {'a_k (taylor)':>22} {'B_k recovered':>20} {'B_k exact':>16} {'|diff|':>10}")
    worst = 0.0
    for k, a in enumerate(coeffs):
        Bk = a * mp.factorial(k)
        exact = mp.bernoulli(k)
        d = abs(Bk - exact)
        worst = max(worst, float(d))
        print(f"{k:>3} {mp.nstr(a, 16):>22} {mp.nstr(Bk, 14):>20} {mp.nstr(exact, 12):>16} {float(d):>10.1e}")
    print(f"\n  worst |B_k recovered - exact| (k<=8): {worst:.2e}")
    return worst


def check_4_mellin():
    """Gamma(s) zeta(s) = int_0^inf t^{s-1}/(e^t-1) dt; zeta(-k) = -B_{k+1}/(k+1)."""
    print("=" * 70)
    print("CHECK 4  Mellin trace identity  Gamma(s) zeta(s) = int_0^inf t^{s-1} Theta(t) dt")
    print("-" * 70)

    def theta(t):
        return 1 / (mp.e ** t - 1)

    print(f"{'s':>7} {'mellin integral':>24} {'Gamma(s) zeta(s)':>24} {'|diff|':>10}")
    worst = 0.0
    for s in (mp.mpf(2), mp.mpf(3), mp.mpf("1.5"), mp.mpf(2) + 1j * mp.mpf(3)):
        integral = mp.quad(lambda t, s=s: t ** (s - 1) * theta(t), [0, 1, mp.inf])
        rhs = mp.gamma(s) * mp.zeta(s)
        d = abs(integral - rhs)
        worst = max(worst, float(d))
        print(f"{mp.nstr(s, 6):>7} {mp.nstr(integral, 16):>24} {mp.nstr(rhs, 16):>24} {float(d):>10.1e}")

    # zeta(-k) = -B_{k+1}/(k+1) holds in the B_1 = +1/2 convention. mpmath uses
    # B_1 = -1/2, which differs ONLY at k=0 (B_2, B_3, ... are convention-free);
    # there we check zeta(0) = -1/2 directly below instead.
    print("\n  Negative-integer values via zeta(-k) = -B_{k+1}/(k+1)  (k >= 1):")
    print(f"  {'k':>3} {'zeta(-k)':>16} {'-B_{k+1}/(k+1)':>18} {'|diff|':>10}")
    for k in range(1, 6):
        zk = mp.zeta(-k)
        bern = -mp.bernoulli(k + 1) / (k + 1)
        d = abs(zk - bern)
        worst = max(worst, float(d))
        print(f"  {k:>3} {mp.nstr(zk, 12):>16} {mp.nstr(bern, 12):>18} {float(d):>10.1e}")
    print(f"\n  zeta(0)  = {mp.nstr(mp.zeta(0), 12)}  (expect -1/2)")
    print(f"  zeta(-1) = {mp.nstr(mp.zeta(-1), 12)}  (expect -1/12 = {mp.nstr(mp.mpf(-1)/12, 12)})")
    print(f"\n  worst Mellin / special-value discrepancy: {worst:.2e}")
    return worst


def check_5_intertwiner():
    """Lemma O6: the circle damping D_r (Poisson convolution) acts on cos(n theta)
    by r^n, mirroring P_t He_n = r^n He_n. Confirms J P_t = D_r J at the index level
    and the Poisson closed form P_r(theta) = (1-r^2)/(1-2r cos theta + r^2)."""
    print("=" * 70)
    print("CHECK 5  Intertwiner J P_t = D_r J  (Lemma O6: OU -> circle recipe)")
    print("-" * 70)
    r = 0.6
    th = np.linspace(0, 2 * np.pi, 4000, endpoint=False)
    M = 6000
    m = np.arange(-M, M + 1)
    poisson_sum = np.sum(r ** np.abs(m)[:, None] * np.exp(1j * m[:, None] * th[None, :]), axis=0).real
    poisson_closed = (1 - r ** 2) / (1 - 2 * r * np.cos(th) + r ** 2)
    e_poisson = float(np.max(np.abs(poisson_sum - poisson_closed)))
    print(f"  Poisson kernel: |sum_|m|<={M} r^|m| e^{{im th}} - (1-r^2)/(1-2r cos+r^2)|  max = {e_poisson:.1e}")
    print(f"  {'n':>3} {'max | D_r cos(n th) - r^n cos(n th) |':>40}")
    worst = e_poisson
    for n in (0, 1, 3, 5, 8):
        f = np.cos(n * th)
        conv = np.array([np.mean((1 - r ** 2) / (1 - 2 * r * np.cos(th[i] - th) + r ** 2) * f)
                         for i in range(len(th))])
        err = float(np.max(np.abs(conv - r ** n * np.cos(n * th))))
        worst = max(worst, err)
        print(f"  {n:>3} {err:>40.1e}")
    print(f"\n  worst intertwiner / Poisson discrepancy: {worst:.2e}")
    return worst


if __name__ == "__main__":
    w1 = check_1_mehler_vs_hermite()
    print()
    w2 = check_2_trace()
    print()
    w3 = check_3_bernoulli()
    print()
    w4 = check_4_mellin()
    print()
    w5 = check_5_intertwiner()
    print("\n" + "=" * 70)
    print("SUMMARY (worst absolute discrepancy per check)")
    print(f"  1 Mehler vs Hermite : {w1:.2e}")
    print(f"  2 trace (3 ways)    : {w2:.2e}")
    print(f"  3 Bernoulli coeffs  : {w3:.2e}")
    print(f"  4 Mellin Gamma-zeta : {w4:.2e}")
    print(f"  5 intertwiner (O6)  : {w5:.2e}")
    print("=" * 70)
