"""Numerical verification for project/sine-wave.md section 7.

The natural sine wave in H = L^2[0, 2] is

    Psi_s(x) = sum_{n>=1} sin(n pi x) / n^s ,   phi_n(x) = sin(n pi x) orthonormal.

Five checks, all unconditional (no RH):

  1. Energy / Parseval (T2):  ||Psi_s||^2 = zeta(2 sigma).  Grid integral of the
     truncated series vs. zeta(2 sigma); plus the exact zeta(4) = pi^4/90.
  2. Kernel (T3):  <Psi_s, Psi_s'> = zeta(s + conj s').  Grid integrals for the
     real pair (2, 3) -> zeta(5) and the tau-independence of the energy.
  3. Fundamental mode (T4 corollary, reversed vs. primes):  <Psi_s, sin(pi x)> = 1.
  4. Boundary (T4):  zeta(2 sigma) - 1/(2 sigma - 1) -> gamma as sigma -> 1/2+,
     and the harmonic line rate H_N - log N -> gamma.
  5. Closed form (T5):  Psi_s(x) = Im Li_s(e^{i pi x}); truncated sum vs. polylog
     at s = 2, and the s = 1 sawtooth Psi_1(x) = pi(1 - x)/2.

Run:  python sine-wave-verify.py
Deps: numpy, mpmath.
"""

import mpmath as mp
import numpy as np

mp.mp.dps = 40  # 40 significant digits for the special-function checks


def _psi_grid(sigma_list, x, n_max):
    """Truncated Psi_s on the grid x for each real s in sigma_list.

    Returns a dict {s: array}.  Psi_s(x) = sum_{n<=n_max} sin(n pi x)/n^s.
    """
    out = {s: np.zeros_like(x) for s in sigma_list}
    for n in range(1, n_max + 1):
        sin_term = np.sin(n * np.pi * x)
        for s in sigma_list:
            out[s] += sin_term / n ** s
    return out


def check_1_energy():
    """||Psi_s||^2 = zeta(2 sigma) via grid integral; exact zeta(4) = pi^4/90."""
    print("=" * 70)
    print("CHECK 1  Energy / Parseval (T2):  ||Psi_s||^2 = zeta(2 sigma)")
    print("-" * 70)
    N, G = 2000, 200001
    x = np.linspace(0.0, 2.0, G)
    psi = _psi_grid([2.0, 3.0], x, N)
    print(f"  (truncation N={N}, grid points={G})")
    print(f"  {'s':>4} {'int Psi_s^2 dx':>22} {'zeta(2 sigma)':>22} {'|diff|':>10}")
    worst = 0.0
    for s in (2.0, 3.0):
        integral = np.trapezoid(psi[s] ** 2, x)
        ref = float(mp.zeta(2 * s))
        d = abs(integral - ref)
        worst = max(worst, d)
        print(f"  {s:>4.1f} {integral:>22.12f} {ref:>22.12f} {d:>10.1e}")
    # Exact closed value at s = 2.
    z4_num = mp.zeta(4)
    z4_exact = mp.pi ** 4 / 90
    print(f"\n  zeta(4) = {mp.nstr(z4_num, 14)}  pi^4/90 = {mp.nstr(z4_exact, 14)}"
          f"  |diff| = {float(abs(z4_num - z4_exact)):.1e}")
    print(f"\n  worst |grid integral - zeta(2 sigma)|: {worst:.2e}")
    return worst


def check_2_kernel():
    """<Psi_s, Psi_s'> = zeta(s + conj s'): real pair (2,3); tau-independence."""
    print("=" * 70)
    print("CHECK 2  Kernel (T3):  <Psi_s, Psi_s'> = zeta(s + conj s')")
    print("-" * 70)
    N, G = 2000, 200001
    x = np.linspace(0.0, 2.0, G)
    psi = _psi_grid([2.0, 3.0], x, N)
    integral = np.trapezoid(psi[2.0] * psi[3.0], x)
    ref = float(mp.zeta(5))
    d23 = abs(integral - ref)
    print(f"  <Psi_2, Psi_3> = {integral:.12f}   zeta(5) = {ref:.12f}   |diff| = {d23:.1e}")

    # tau-independence of the energy: <Psi_s, Psi_s> = zeta(2 sigma) for s = sigma + i tau.
    # Coefficient form (exact partial-sum identity): sum_{n<=N} |n^{-s}|^2 = sum n^{-2 sigma}.
    print("\n  Energy depends only on sigma (T2):  ||Psi_{sigma+i tau}||^2 = zeta(2 sigma)")
    print(f"  {'sigma':>6} {'tau':>5} {'sum_{n<=1e5} n^-2sigma':>24} {'zeta(2 sigma)':>20} {'|diff|':>10}")
    worst = d23
    for sigma, tau in ((2.0, 0.0), (2.0, 7.0), (1.5, 3.0)):
        part = mp.fsum(mp.mpf(n) ** (-2 * sigma) for n in range(1, 100001))
        ref2 = mp.zeta(2 * sigma)
        d = float(abs(part - ref2))
        worst = max(worst, d)
        print(f"  {sigma:>6.2f} {tau:>5.1f} {mp.nstr(part, 14):>24} {mp.nstr(ref2, 14):>20} {d:>10.1e}")
    print(f"\n  worst kernel discrepancy: {worst:.2e}")
    return worst


def check_3_fundamental():
    """<Psi_s, sin(pi x)> = 1 (reversed vs. primes, where it is 0)."""
    print("=" * 70)
    print("CHECK 3  Fundamental mode (reversed vs. primes):  <Psi_s, sin(pi x)> = 1")
    print("-" * 70)
    N, G = 2000, 200001
    x = np.linspace(0.0, 2.0, G)
    psi = _psi_grid([2.0, 3.0], x, N)
    print(f"  {'s':>4} {'<Psi_s, sin(pi x)>':>22} {'expected':>10} {'|diff|':>10}")
    worst = 0.0
    for s in (2.0, 3.0):
        integral = np.trapezoid(psi[s] * np.sin(np.pi * x), x)
        d = abs(integral - 1.0)
        worst = max(worst, d)
        print(f"  {s:>4.1f} {integral:>22.12f} {1.0:>10.1f} {d:>10.1e}")
    print(f"\n  worst |<Psi_s, sin pi x> - 1|: {worst:.2e}")
    return worst


def check_4_boundary():
    """zeta(2 sigma) - 1/(2 sigma - 1) -> gamma; harmonic H_N - log N -> gamma."""
    print("=" * 70)
    print("CHECK 4  Boundary (T4):  pole constant and harmonic line rate -> gamma")
    print("-" * 70)
    gamma = mp.euler
    print(f"  gamma (Euler-Mascheroni) = {mp.nstr(gamma, 14)}")
    print(f"\n  (1) zeta(2 sigma) - 1/(2 sigma - 1) -> gamma  as sigma -> 1/2+")
    print(f"  {'sigma':>8} {'zeta(2s) - 1/(2s-1)':>24} {'|.- gamma|':>12}")
    worst = 0.0
    for sigma in (mp.mpf("0.6"), mp.mpf("0.55"), mp.mpf("0.51"), mp.mpf("0.501"), mp.mpf("0.5001")):
        z = mp.mpf(2) * sigma
        val = mp.zeta(z) - 1 / (z - 1)
        d = float(abs(val - gamma))
        worst = max(worst, d)
        print(f"  {mp.nstr(sigma, 6):>8} {mp.nstr(val, 16):>24} {d:>12.1e}")

    print(f"\n  (2) harmonic line rate:  H_N - log N -> gamma")
    print(f"  {'N':>9} {'H_N - log N':>22} {'|.- gamma|':>12}")
    for N in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6):
        HN = mp.harmonic(N)
        val = HN - mp.log(N)
        d = float(abs(val - gamma))
        # convergence here is ~1/(2N), so it is *not* part of the tight worst-case
        print(f"  {N:>9d} {mp.nstr(val, 14):>22} {d:>12.1e}")
    print(f"\n  worst |pole-constant - gamma| (check (1)): {worst:.2e}")
    return worst


def check_5_closed_form():
    """Psi_s(x) = Im Li_s(e^{i pi x}); s=2 vs truncated sum; s=1 sawtooth."""
    print("=" * 70)
    print("CHECK 5  Closed form (T5):  Psi_s(x) = Im Li_s(e^{i pi x})")
    print("-" * 70)

    def psi_trunc(s, x, N):
        return mp.fsum(mp.sin(n * mp.pi * x) / mp.mpf(n) ** s for n in range(1, N + 1))

    print("  s = 2 (Clausen):  truncated sum  vs  Im Li_2(e^{i pi x})")
    print(f"  {'x':>6} {'sum_{n<=20000}':>22} {'Im Li_2(e^{i pi x})':>24} {'|diff|':>10}")
    worst = 0.0
    for x in (mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.8"), mp.mpf("1.3")):
        z = mp.e ** (1j * mp.pi * x)
        closed = mp.im(mp.polylog(2, z))
        approx = psi_trunc(2, x, 20000)
        d = float(abs(closed - approx))
        worst = max(worst, d)
        print(f"  {mp.nstr(x, 4):>6} {mp.nstr(approx, 14):>22} {mp.nstr(closed, 14):>24} {d:>10.1e}")

    print("\n  s = 1 sawtooth:  Im Li_1(e^{i pi x}) = Im(-log(1 - e^{i pi x}))  vs  pi(1 - x)/2")
    print(f"  {'x':>6} {'Im(-log(1-e^{ipix}))':>24} {'pi(1 - x)/2':>18} {'|diff|':>10}")
    for x in (mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("1.0"), mp.mpf("1.5")):
        z = mp.e ** (1j * mp.pi * x)
        closed = mp.im(-mp.log(1 - z))
        sawtooth = mp.pi * (1 - x) / 2
        d = float(abs(closed - sawtooth))
        worst = max(worst, d)
        print(f"  {mp.nstr(x, 4):>6} {mp.nstr(closed, 16):>24} {mp.nstr(sawtooth, 12):>18} {d:>10.1e}")
    print(f"\n  worst closed-form discrepancy: {worst:.2e}")
    return worst


if __name__ == "__main__":
    w1 = check_1_energy()
    print()
    w2 = check_2_kernel()
    print()
    w3 = check_3_fundamental()
    print()
    w4 = check_4_boundary()
    print()
    w5 = check_5_closed_form()
    print("\n" + "=" * 70)
    print("SUMMARY (worst absolute discrepancy per check)")
    print(f"  1 energy = zeta(2 sigma)   : {w1:.2e}")
    print(f"  2 kernel = zeta(s+conj s') : {w2:.2e}")
    print(f"  3 fundamental mode = 1     : {w3:.2e}")
    print(f"  4 boundary constant gamma  : {w4:.2e}")
    print(f"  5 closed form Im Li_s      : {w5:.2e}")
    print("=" * 70)
