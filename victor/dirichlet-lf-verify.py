"""Numerical verification for project/dirichlet-series.md (Phase 2c).

Object: the character sine wave  Psi^chi_s(x) = sum_{n>=1} chi(n) n^{-s} sin(n pi x)
in H = L^2[0,2], with chi a Dirichlet character mod q.

Checks (10-digit) the three provable theorems and the Gauss-sum transfer:
  T2  energy   ||Psi^chi_s||^2            = L(2 sigma, chi0)         (principal char)
  T3  kernel   <Psi^chi1_s, Psi^chi2_s'>  = L(s + conj(s'), chi1 conj(chi2))
  Gauss-sum separability   chi(n) = tau(bar chi)^{-1} sum_a bar chi(a) e^{2 pi i a n / q}
  root number  eps(chi) = tau(chi) / (i^a sqrt q),  |eps| = 1

Example modulus q = 4: chi4 is the unique primitive char mod 4 (odd), L(s,chi4)=beta(s);
chi0 is the principal char mod 4.
"""
import mpmath as mp

mp.mp.dps = 30

q = 4
# characters mod 4 as dicts on residues 0..3
chi4 = {0: 0, 1: 1, 2: 0, 3: -1}      # primitive, odd  (Dirichlet beta)
chi0 = {0: 0, 1: 1, 2: 0, 3: 1}       # principal mod 4


def chi(c, n):
    return c[n % q]


def inner_product(c1, c2, s, sp, N=200000):
    """<Psi^{c1}_s, Psi^{c2}_{sp}> = sum_n c1(n) conj(c2(n)) n^{-(s + conj(sp))}.

    Uses the harmonics' orthonormality:  <sin(a pi x), sin(b pi x)>_{L^2[0,2]} = delta_ab.
    """
    e = s + mp.conj(sp)
    tot = mp.mpf(0)
    for n in range(1, N + 1):
        a = chi(c1, n) * mp.conj(chi(c2, n))
        if a != 0:
            tot += a * mp.power(n, -e)
    return tot


def L(c, s, N=200000):
    return mp.nsum(lambda n: chi(c, int(n)) * mp.power(n, -s), [1, N])


def gauss_sum(c):
    return mp.fsum(chi(c, a) * mp.e ** (2j * mp.pi * a / q) for a in range(q))


print("=== T2: energy ||Psi^chi4_s||^2 = L(2 sigma, chi0) ===")
s = mp.mpf(2)
lhs = inner_product(chi4, chi4, s, s)
# closed form: sum over odd n of n^{-4} = (1 - 2^{-4}) zeta(4)
rhs = (1 - mp.power(2, -4)) * mp.zeta(4)
print("  series      :", mp.nstr(lhs, 12))
print("  (1-2^-4)z(4):", mp.nstr(rhs, 12))
print("  diff        :", mp.nstr(abs(lhs - rhs), 3))

print()
print("=== T3 cross-character: <Psi^chi4_s, Psi^chi0_s'> = L(s+conj(s'), chi4) = beta(s+s') ===")
s, sp = mp.mpf(2), mp.mpf(2)
lhs = inner_product(chi4, chi0, s, sp)   # chi4 * conj(chi0) = chi4 on odd n
rhs = inner_product(chi4, {0:0,1:1,2:0,3:0}, 0, 0)  # placeholder, replace by beta(4)
beta4 = mp.nsum(lambda k: mp.power(-1, k) / mp.power(2 * k + 1, 4), [0, mp.inf])
print("  series      :", mp.nstr(lhs, 12))
print("  beta(4)     :", mp.nstr(beta4, 12))
print("  diff        :", mp.nstr(abs(lhs - beta4), 3))

print()
print("=== Gauss-sum separability: chi4(n) reconstructed from additive chars ===")
tau_bar = gauss_sum(chi4)   # bar chi4 = chi4 (real)
maxerr = mp.mpf(0)
for n in range(1, 13):
    recon = (1 / tau_bar) * mp.fsum(
        chi(chi4, a) * mp.e ** (2j * mp.pi * a * n / q) for a in range(q)
    )
    maxerr = max(maxerr, abs(recon - chi(chi4, n)))
print("  tau(chi4)   :", mp.nstr(gauss_sum(chi4), 12), " |tau| =", mp.nstr(abs(gauss_sum(chi4)), 6))
print("  max |recon - chi4(n)|, n=1..12 :", mp.nstr(maxerr, 3))

print()
print("=== root number eps(chi4) = tau / (i^a sqrt q), a=1 (odd) ===")
a = 1
eps = gauss_sum(chi4) / (1j ** a * mp.sqrt(q))
print("  eps(chi4)   :", mp.nstr(eps, 12), " |eps| =", mp.nstr(abs(eps), 6))

print()
print("=== sample value Psi^chi4_2(0.25), primes-style spot check ===")
val = mp.fsum(chi(chi4, n) * mp.power(n, -2) * mp.sin(n * mp.pi * mp.mpf('0.25'))
              for n in range(1, 5000))
print("  Psi^chi4_2(0.25) :", mp.nstr(val, 12))
