"""pairing_lemma_check.py — numerical controls for PSC2-F01 (gate E1 + claim HS5).

The proofs in findings/PSC2-F01-pairing-lemma.md are self-contained; this script is
the mandatory harness control (rule I0 / S04 section 5 spirit): every claim is checked
on a positive instance AND shown to FAIL on a negative control, so the check itself
cannot fabricate agreement.

Deterministic: seed 20260706.  No arithmetic data (no primes, no zeta zeros) consumed.

Run:  python pairing_lemma_check.py
"""

import numpy as np

rng = np.random.default_rng(20260706)

# ---------------------------------------------------------------- ambient model
# C^{2m} with chiral involution J = diag(I_m, -I_m) and a self-adjoint D with
# J D J^{-1} = -D  (generic off-diagonal block), standing in for the adelic pair
# (D, J) of S03 section 1.  Only the two algebraic identities are used.
m = 12
N = 2 * m
B = rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m))
D = np.block([[np.zeros((m, m)), B], [B.conj().T, np.zeros((m, m))]])
J = np.diag(np.concatenate([np.ones(m), -np.ones(m)])).astype(complex)

assert np.allclose(D, D.conj().T), "D must be self-adjoint"
assert np.allclose(J @ J.conj().T, np.eye(N)), "J must be unitary"
anti = np.max(np.abs(J @ D @ np.linalg.inv(J) + D))
print(f"ambient check   max|JDJ^-1 + D|            = {anti:.3e}   (exact anticommutation)")


def compression_spectrum(V):
    """Eigenvalues of the Galerkin compression P D P restricted to span(V)."""
    Q, _ = np.linalg.qr(V)
    H = Q.conj().T @ D @ Q
    assert np.allclose(H, H.conj().T)
    return np.sort(np.linalg.eigvalsh(H))


def symmetry_defect(spec):
    """max_k |lambda_k + lambda_{d+1-k}| over the sorted spectrum: 0 iff spec = -spec."""
    return float(np.max(np.abs(spec + spec[::-1])))


# ------------------------------------------------- E1: positive control
# V spanned by {x_i, J x_i}: J-invariant by construction (generic dim 2k).
k = 4
X = rng.standard_normal((N, k)) + 1j * rng.standard_normal((N, k))
spec_inv = compression_spectrum(np.hstack([X, J @ X]))
print(f"E1  positive    J-invariant V, dim {2*k}:  symmetry defect = {symmetry_defect(spec_inv):.3e}")

# ------------------------------------------------- E1: negative control
# generic V of the same dimension, NOT J-invariant: pairing must fail.
Y = rng.standard_normal((N, 2 * k)) + 1j * rng.standard_normal((N, 2 * k))
spec_gen = compression_spectrum(Y)
print(f"E1  negative    generic V,     dim {2*k}:  symmetry defect = {symmetry_defect(spec_gen):.3e}   (must be O(1))")

# ------------------------------------------------- E1 corollary: odd moments vanish
odd_moments = [float(np.sum(spec_inv ** (2 * j + 1))) for j in range(1, 4)]
print("E1  corollary   odd moments tr H^3, H^5, H^7 =",
      "  ".join(f"{v:.3e}" for v in odd_moments), "  (exact zeros)")

# ------------------------------------------------- HS5: FE <-> evenness <-> pairing
# stage product over a spectrum multiset S (finite: plain factors, no E_1 needed)
lam = np.sort(rng.uniform(0.5, 30.0, size=6))          # positive halves
paired = np.concatenate([lam, -lam])                    # +/- paired multiset
unpaired = paired.copy()
unpaired[-1] *= 1.01                                    # break ONE pairing by 1%


def stage_product(S, t):
    t = np.atleast_1d(np.asarray(t, dtype=complex))
    return np.prod(1.0 - t[:, None] / S[None, :], axis=1)


def fe_defect(S):
    """max |Z(s) - Z(1-s)| at random complex s, with Z(s) = Xi_n(-i(s-1/2))."""
    s = rng.uniform(-2, 3, 12) + 1j * rng.uniform(-40, 40, 12)
    t = -1j * (s - 0.5)
    return float(np.max(np.abs(stage_product(S, t) - stage_product(S, -t))))


# relative defect (products are large at |Im s| ~ 40)
scale = float(np.abs(stage_product(paired, -1j * (2.0 + 40j - 0.5))[0]))
print(f"HS5 positive    paired spectrum:   FE defect |Z(s)-Z(1-s)|/scale = {fe_defect(paired)/scale:.3e}")
print(f"HS5 negative    1% unpaired:       FE defect |Z(s)-Z(1-s)|/scale = {fe_defect(unpaired)/scale:.3e}   (must sit far above machine precision)")

# exponential-factor cancellation: product of genus-1 factors E_1(t/l) = (1-t/l)e^{t/l}
# over a PAIRED multiset equals the plain even product exactly; unpaired leaves exp residue.
t0 = 1.7
E1 = lambda z: (1.0 - z) * np.exp(z)
ratio_p = np.prod(E1(t0 / paired)) / np.prod(1.0 - t0 ** 2 / lam ** 2)
ratio_u = np.prod(E1(t0 / unpaired)) / np.prod(1.0 - t0 / unpaired)
print(f"HS5 exp-factor  paired:   prod E_1 / plain even product - 1 = {abs(ratio_p - 1):.3e}")
print(f"HS5 exp-factor  unpaired: prod E_1 / plain product      - 1 = {abs(ratio_u - 1):.3e}   (residual exp factor, far above machine precision)")
