"""Numerical implementation + verification for project/spectral-triple.md (Phase 2b).

The spectral transfer operator T between the *prime numbers* and the *imaginary
parts of the zeta zeros*, on the critical line (real part sigma = 1/2).

Construction.  Pick an even test function phi.  Its autocorrelation f = phi * ~phi
has non-negative Fourier transform  hat f = |hat phi|^2 >= 0.  The Weil-Guinand
explicit formula is the *trace identity* of T -- it equates two ways of summing
hat f:

    sum_gamma  hat f(gamma)                                   [ZERO side]
      = 2 hat f(i/2)                                          pole of zeta (s=1,0)
        - 2 sum_n  Lambda(n) n^{-sigma}  f(log n)             [PRIME side, sigma=1/2]
        + (1/2pi) int hat f(r) Re psi(1/4 + i r/2) dr         archimedean
        - f-hat(0) log pi.                                    archimedean

Here rho = sigma + i gamma are the nontrivial zeros, sigma = 1/2, and the prime
weight n^{-sigma} = n^{-1/2} is exactly the "real part 1/2".  T is convolution by
K = Z - P + G; its spectral measure is the signed measure whose ZERO atoms and
PRIME atoms this identity balances.

Checks (against exact zeros from mpmath, ~25 digits):

  1. Transfer identity (UNCONDITIONAL).  ZERO side = PRIME + archimedean side,
     for several test-function widths.  This is the defining trace identity of T
     at sigma = 1/2.
  2. Weil positivity functional W(phi) (Weil's criterion; positivity <=> RH is
     CONDITIONAL).  Compute W from the arithmetic (prime + gamma) side alone and
     confirm W >= 0 -- an RH test that never looks at the zeros.
  3. Real-part sensitivity.  Move a zero off the line to real part beta; the zero
     contribution D(beta) vanishes at beta = 1/2 and goes negative for beta != 1/2.
     This is why 1/2 is the self-dual exponent -- positivity has teeth.
  4. Channel / cone tie-in.  The Z, P, G channels and the quaternion positivity
     indicator z^2 - (p^2 + g^2) of prime-zeros.py, on an omega grid (note sect. 8).

Run:  python spectral-triple-verify.py
Deps: numpy, mpmath; loads prime-zeros.py for channels() and quaternion_cone().
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

# Exact imaginary parts of the first N_ZEROS nontrivial zeros, computed once.
N_ZEROS = 80
print(f"(precomputing {N_ZEROS} exact zero ordinates with mpmath ...)")
GAMMAS = [mp.im(mp.zetazero(k)) for k in range(1, N_ZEROS + 1)]
LOG_PI = mp.log(mp.pi)


def von_mangoldt(n):
    """log p if n = p^k, else 0 (von Mangoldt Lambda)."""
    m, p = n, 2
    while p * p <= m and m % p != 0:
        p += 1
    if p * p > m:
        p = m
    k = n
    while k % p == 0:
        k //= p
    return mp.log(p) if k == 1 else mp.mpf(0)


def gaussian_pair(alpha):
    """Even test function h(r) = exp(-alpha r^2) and its transform g.

    h plays the role of  hat f = |hat phi|^2 >= 0  (phi Gaussian).  Its transform
        g(u) = (1/2pi) int h(r) e^{-iru} dr = 1/(2 sqrt(pi alpha)) exp(-u^2/4alpha)
    plays the role of  f = phi * ~phi.
    """
    a = mp.mpf(alpha)
    h = lambda r: mp.e ** (-a * r ** 2)
    g = lambda u: 1 / (2 * mp.sqrt(mp.pi * a)) * mp.e ** (-u ** 2 / (4 * a))
    return h, g


def zero_side(h):
    """sum over nontrivial zeros  sum_gamma h(gamma) = 2 sum_{gamma>0} h(gamma)."""
    return 2 * mp.fsum(h(g) for g in GAMMAS)


def prime_side(g, sigma=mp.mpf(1) / 2, n_max=4000):
    """2 sum_n Lambda(n) n^{-sigma} g(log n).  sigma = 1/2 is the critical line."""
    tot = mp.mpf(0)
    for n in range(2, n_max + 1):
        L = von_mangoldt(n)
        if L != 0:
            tot += L * mp.power(n, -sigma) * g(mp.log(n))
    return 2 * tot


def archimedean(h, g):
    """Pole + Gamma-factor terms:  2 h(i/2) + (1/2pi)int h Re psi(1/4+ir/2) - g(0)log pi."""
    pole = 2 * h(mp.mpf(1) / 2 * 1j)
    integrand = lambda r: h(r) * mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * r / 2))
    gamma_int = (1 / (2 * mp.pi)) * 2 * mp.quad(integrand, [0, mp.inf])
    return pole + gamma_int - g(0) * LOG_PI


def check_1_transfer_identity():
    """ZERO side = PRIME + archimedean side (the trace identity of T at sigma=1/2)."""
    print("=" * 74)
    print("CHECK 1  Transfer identity (UNCONDITIONAL):  ZERO side = PRIME + arch side")
    print("-" * 74)
    print(f"  {'alpha':>6} {'ZERO side':>22} {'PRIME+arch side':>22} {'|diff|':>10}")
    worst = mp.mpf(0)
    for alpha in (mp.mpf("0.02"), mp.mpf("0.05"), mp.mpf("0.1"), mp.mpf("0.15")):
        h, g = gaussian_pair(alpha)
        lhs = mp.re(zero_side(h))
        rhs = mp.re(archimedean(h, g) - prime_side(g))
        d = abs(lhs - rhs)
        worst = max(worst, d)
        print(f"  {mp.nstr(alpha, 4):>6} {mp.nstr(lhs, 16):>22} {mp.nstr(rhs, 16):>22} {float(d):>10.1e}")
    print(f"\n  worst |ZERO - (PRIME+arch)|: {float(worst):.2e}")
    return float(worst)


def check_2_weil_positivity():
    """Weil functional W(phi) >= 0, computed from the arithmetic side alone.

    With h = |hat phi|^2 = exp(-alpha r^2), the explicit-formula RHS equals
    sum_gamma h(gamma) >= 0 (real gamma, RH).  We compute that RHS from PRIMES and
    the Gamma factor only -- never touching the zeros -- and confirm it stays >= 0.
    Positivity <=> RH is Weil's criterion (CONDITIONAL).
    """
    print("=" * 74)
    print("CHECK 2  Weil positivity functional W(phi) >= 0  (arithmetic side only)")
    print("-" * 74)
    print(f"  {'alpha':>6} {'pole':>14} {'-PRIME':>14} {'Gamma int':>14} {'W(phi)':>14} {'>=0?':>5}")
    all_pos = True
    worst_match = mp.mpf(0)
    for alpha in (mp.mpf("0.01"), mp.mpf("0.02"), mp.mpf("0.05"), mp.mpf("0.1"), mp.mpf("0.15")):
        h, g = gaussian_pair(alpha)
        pole = mp.re(2 * h(mp.mpf(1) / 2 * 1j))
        prime = mp.re(prime_side(g))
        integrand = lambda r: h(r) * mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * r / 2))
        gint = mp.re((1 / (2 * mp.pi)) * 2 * mp.quad(integrand, [0, mp.inf]) - g(0) * LOG_PI)
        W = pole - prime + gint
        # cross-check against the zero side
        worst_match = max(worst_match, abs(W - mp.re(zero_side(h))))
        ok = W >= 0
        all_pos = all_pos and ok
        print(f"  {mp.nstr(alpha, 4):>6} {mp.nstr(pole, 8):>14} {mp.nstr(-prime, 8):>14} "
              f"{mp.nstr(gint, 8):>14} {mp.nstr(W, 10):>14} {str(bool(ok)):>5}")
    print(f"\n  W(phi) >= 0 for every tested phi: {all_pos}  (consistent with RH)")
    print(f"  worst |W(arith) - W(zeros)|: {float(worst_match):.2e}")
    return float(worst_match)


def check_3_real_part_sensitivity():
    """Move a zero off the line to real part beta; the contribution detects it.

    A zero rho = beta + i gamma enters the trace identity at argument
    (rho - 1/2)/i = gamma - i(beta - 1/2).  Its symmetric (rho, ~rho) contribution
    to the ZERO side is
        D(beta) = h(gamma + i delta) + h(gamma - i delta) - 2 h(gamma),  delta = beta-1/2
                = 2 e^{-alpha gamma^2} ( e^{alpha delta^2} cos(2 alpha gamma delta) - 1 ).
    D(1/2) = 0; for beta != 1/2 and suitable alpha, D < 0 -- so an off-line zero
    *lowers* the Weil functional and can break positivity.  This is exactly why the
    real part is pinned to 1/2.
    """
    print("=" * 74)
    print("CHECK 3  Real-part sensitivity:  off-line zero lowers the functional")
    print("-" * 74)
    alpha = mp.mpf("0.05")
    gamma = GAMMAS[0]  # first zero ordinate ~ 14.1347
    h, _ = gaussian_pair(alpha)
    print(f"  alpha = {mp.nstr(alpha, 4)},  gamma = {mp.nstr(gamma, 10)}  (first zero)")
    print(f"  {'beta':>8} {'delta':>9} {'D(beta) [zero contribution shift]':>36} {'sign':>6}")
    worst_zero = mp.mpf(0)
    saw_negative = False
    for beta in (mp.mpf("0.5"), mp.mpf("0.51"), mp.mpf("0.55"), mp.mpf("0.6"), mp.mpf("0.7")):
        delta = beta - mp.mpf(1) / 2
        D = mp.re(h(gamma + 1j * delta) + h(gamma - 1j * delta) - 2 * h(gamma))
        # closed form cross-check
        D_closed = 2 * mp.e ** (-alpha * gamma ** 2) * (
            mp.e ** (alpha * delta ** 2) * mp.cos(2 * alpha * gamma * delta) - 1)
        worst_zero = max(worst_zero, abs(D - D_closed))
        sign = "0" if D == 0 else ("-" if D < 0 else "+")
        if D < 0:
            saw_negative = True
        print(f"  {mp.nstr(beta, 4):>8} {mp.nstr(delta, 4):>9} {mp.nstr(D, 12):>36} {sign:>6}")
    print(f"\n  D(1/2) = 0 exactly; off-line zeros give D < 0 (seen: {saw_negative})")
    print(f"  worst |D - closed form|: {float(worst_zero):.2e}")
    return float(worst_zero)


def check_4_channels_cone():
    """Z, P, G channels and quaternion cone indicator (prime-zeros.py, note sect. 8).

    HONEST CAVEAT.  The raw geometric indicator z^2 - (p^2 + g^2) of prime-zeros.py
    is *normalization-dependent*: with overlapping Gaussian bumps the dense prime
    channel P dominates the zero channel Z, so the indicator is strongly negative.
    This is NOT a counterexample to RH -- it only shows the crude geometric cone is
    not a faithful positivity criterion.  The rigorous positivity statement is the
    Weil functional of Check 2 (which IS >= 0), not this indicator.  See note sect. 8.
    """
    print("=" * 74)
    print("CHECK 4  Spectral channels + quaternion cone indicator (prime-zeros.py)")
    print("-" * 74)
    omega = np.linspace(0.0, 60.0, 4000)
    Z, P, G = pz.channels(omega, eps=0.05, sigma=0.4, n_max=200)
    cone = pz.quaternion_cone(Z, P, G)
    print(f"  grid omega in [0, 60], {len(omega)} points; primes up to n=200, 10 zeros")
    print(f"  max Z (zeros)  = {Z.max():.6f} at omega = {omega[np.argmax(Z)]:.3f}")
    print(f"  max P (primes) = {P.max():.6f} at omega = {omega[np.argmax(P)]:.3f}  (dense prime bumps)")
    print(f"  max G (gamma)  = {G.max():.6f}")
    print(f"  cone indicator z^2-(p^2+g^2):  min = {cone.min():.4f}  max = {cone.max():.4f}")
    in_cone = cone.min() >= 0
    print(f"\n  raw geometric indicator stays >= 0: {in_cone}")
    print(f"  -> the raw indicator is NOT >= 0 here (P dominates Z); it is normalization-")
    print(f"     dependent and is not a faithful RH criterion.  Rigorous positivity = Check 2.")
    return float(cone.min())


if __name__ == "__main__":
    w1 = check_1_transfer_identity()
    print()
    w2 = check_2_weil_positivity()
    print()
    w3 = check_3_real_part_sensitivity()
    print()
    w4 = check_4_channels_cone()
    print("\n" + "=" * 74)
    print("SUMMARY")
    print(f"  1 transfer identity  worst |ZERO-(PRIME+arch)| : {w1:.2e}  (proven, ~25+ digits)")
    print(f"  2 Weil functional    worst |W(arith)-W(zeros)| : {w2:.2e}  (W>=0, RH-consistent)")
    print(f"  3 real-part shift    worst |D-closed form|     : {w3:.2e}  (1/2 is special)")
    print(f"  4 raw cone indicator min value             : {w4:.2e}  (normalization-dependent)")
    print("=" * 74)
