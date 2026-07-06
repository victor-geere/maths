"""CORRECTED 5 Jul 2026 — see notes.md §2 and findings.md.

Two defects were found and fixed in this file (audit trail per repo convention):
  D1: the original build_prime_graph joined primes *inside* I_n via composites of I_n —
      impossible (p*q >= 2^{2n} > M_n), so the graph was empty and every reported pole
      was the (u^2-1)^N artifact of a degenerate pencil. Fixed: vertices are now the
      generator primes p < 2^n, coupled through the composites in I_n (cross-scale,
      mirroring adele/phase3.md Def 3.2).
  D2: unfold_eigenvalues mapped ranks through the zero-counting function, ignoring its
      input entirely — it "matched" the zeros for any data. It is retired below and kept
      only as a stub with a warning. No unfolding is used as evidence (implementation.md I0.1).
Honest pipeline: prime_graph_lab.py. This app now shows raw pole data only.
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
from math import log, pi, exp
from scipy.linalg import eigvals, block_diag
import time

# ------------------------------------------------------------
# Sieve helpers (as before)
# ------------------------------------------------------------
def sieve_of_eratosthenes(limit):
    if limit < 2:
        return np.array([], dtype=int)
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            is_prime[p*p : limit+1 : p] = False
    return np.flatnonzero(is_prime)

def prime_factors(x, primes):
    factors = {}
    y = x
    for p in primes:
        if p * p > y:
            break
        if y % p == 0:
            cnt = 0
            while y % p == 0:
                y //= p
                cnt += 1
            factors[p] = cnt
    if y > 1:
        factors[y] = factors.get(y, 0) + 1
    return factors

def rad(x, primes):
    if x == 1:
        return 1
    rad_val = 1
    y = x
    for p in primes:
        if p * p > y:
            break
        if y % p == 0:
            rad_val *= p
            while y % p == 0:
                y //= p
    if y > 1:
        rad_val *= y
    return rad_val

def generate_sieve_data(n):
    M_n = (1 << (n + 1)) - 1
    all_primes = sieve_of_eratosthenes(M_n)
    primes_lt_2n = all_primes[all_primes < (1 << n)]
    I_n_low = 1 << n
    I_n_high = M_n
    primes_in_I = all_primes[(all_primes >= I_n_low) & (all_primes <= I_n_high)].tolist()
    all_int = np.arange(I_n_low, I_n_high + 1)
    composites_in_I = all_int[~np.isin(all_int, primes_in_I)].tolist()
    return primes_in_I, composites_in_I, primes_lt_2n, M_n

# ------------------------------------------------------------
# Build the "prime graph" adjacency from sieve
# ------------------------------------------------------------
def build_prime_graph(n):
    """CORRECTED (D1): vertices are the generator primes p < 2^n; an edge {p,q} is added
    when a composite m in I_n is divisible by both. The original version used the primes
    *in* I_n as vertices, which provably yields the empty graph (pq >= 2^{2n} > M_n)."""
    primes_I, composites_I, primes_lt_2n, M_n = generate_sieve_data(n)
    verts = [int(p) for p in primes_lt_2n]
    idx = {p: i for i, p in enumerate(verts)}
    N = len(verts)
    if N == 0:
        return None, verts, M_n
    A = np.zeros((N, N), dtype=float)
    for m in composites_I:
        fac = prime_factors(m, primes_lt_2n)
        fac_in = [p for p in fac if p in idx]
        # add edges between every pair of distinct generator primes that co-divide m
        for i in range(len(fac_in)):
            p = fac_in[i]
            for j in range(i+1, len(fac_in)):
                q = fac_in[j]
                ip, iq = idx[p], idx[q]
                A[ip, iq] += 1
                A[iq, ip] += 1
    A_binary = (A > 0).astype(float)
    assert A_binary.sum() > 0, "D1 regression guard: graph must be non-empty"
    return A_binary, verts, M_n

# ------------------------------------------------------------
# Ihara zeta function poles via Hashimoto matrix
# ------------------------------------------------------------
def ihara_poles(A):
    """
    Return the poles u of the Ihara zeta Z(u) for graph with adjacency A.
    Poles are the reciprocals of eigenvalues of the 2m x 2m Hashimoto edge-matrix,
    where m = number of edges. We use an equivalent but simpler method:
    poles are the solutions u to det(I - u A + u^2 (D - I)) = 0.
    This can be turned into a generalized eigenvalue problem:
    | D - I   0 |  | x | = u |  A   -I |  | x |
    |  0      I |  | y |     |  I    0 |  | y |
    (see e.g. Terras "Zeta functions of graphs").
    We compute eigenvalues u = λ of this generalized problem.
    """
    N = A.shape[0]
    D = np.diag(np.sum(A, axis=1))
    I = np.eye(N)
    # Build block matrices
    M11 = D - I
    M12 = np.zeros((N,N))
    M21 = np.zeros((N,N))
    M22 = I
    M = np.block([[M11, M12],
                  [M21, M22]])
    K11 = A
    K12 = -I
    K21 = I
    K22 = np.zeros((N,N))
    K = np.block([[K11, K12],
                  [K21, K22]])
    # Generalized eigenvalue problem M x = u K x
    # Use scipy.linalg.eigvals to solve
    vals = eigvals(M, K)
    # Keep only finite real-ish poles? We'll take all, but later filter.
    return vals

# ------------------------------------------------------------
# Unfolding and Riemann zeros (unchanged)
# ------------------------------------------------------------
def zero_count(t):
    if t <= 1e-10:
        return 0.0
    return (t/(2*pi)) * (log(t/(2*pi)) - 1) + 7/8

def invert_zero_count(target, tol=1e-12, max_iter=50):
    if target <= 0:
        return 0.0
    T = 2*pi * exp(1)
    for _ in range(max_iter):
        N = zero_count(T)
        dN = (1/(2*pi)) * log(T/(2*pi))
        if dN == 0:
            break
        Tnew = T - (N - target) / dN
        if abs(Tnew - T) < tol:
            return Tnew
        T = Tnew
    return T

def unfold_eigenvalues(eigvals):
    """RETIRED (D2): this mapped ranks through the zero-counting function and ignored its
    input values entirely — identical output for any data. Kept as a stub so old imports
    fail loudly instead of silently fabricating matches."""
    raise RuntimeError("unfold_eigenvalues is retired (defect D2, see notes.md §2.2); "
                       "use raw pole data — implementation.md rule I0.1")

def get_riemann_zeros(num_zeros):
    try:
        import mpmath
        return np.array([float(mpmath.zetazero(k).imag) for k in range(1, num_zeros+1)])
    except ImportError:
        known = [14.134725142, 21.022039639, 25.010857580, 30.424876126,
                 32.935061588, 37.586178159, 40.918719012, 43.327073281,
                 48.005150881, 49.773832478, 52.970321478, 56.446247697,
                 59.347044003, 60.831778525, 65.112544048, 67.079810529,
                 69.546401711, 72.067157674, 75.704690699, 77.144840069,
                 79.337375020, 82.910380854, 84.735492981, 87.425274613,
                 88.809111208, 92.491899271, 94.651344041, 96.209967348,
                 98.831194218, 101.317851006]
        if num_zeros <= len(known):
            return np.array(known[:num_zeros])
        else:
            st.warning("mpmath not available – using asymptotic estimate.")
            return np.array([invert_zero_count(k-0.5) for k in range(1, num_zeros+1)])

# ------------------------------------------------------------
# Streamlit app
# ------------------------------------------------------------
def main():
    st.set_page_config(page_title="Ihara Zeta from Sieve", layout="wide")
    st.title("Phase 7 – Ihara Zeta Function of the Prime Graph")
    st.markdown("""
    We construct a finite graph whose vertices are the primes in a dyadic block.
    Edges are drawn whenever two primes co‑divide a composite number in the block
    (as given by the composite‑generator sieve).  
    The **Ihara zeta function** of this graph is
    \[
    Z(u) = \det\!\big( I - u\,A + u^2\,(D - I) \big)^{-1},
    \]
    and its poles are computed via a generalised eigenvalue problem.
    After a suitable rescaling, these poles are expected to approach the
    non‑trivial zeros of the Riemann zeta function.
    """)

    with st.sidebar:
        n = st.slider("Dyadic block index n", 5, 12, 8)

    # Build graph
    A, primes_I, M_n = build_prime_graph(n)
    if A is None or len(A) == 0:
        st.error("No primes in this block. Increase n.")
        return

    N = len(primes_I)
    st.write(f"Graph vertices (primes in Iₙ): {N}")
    st.write(f"Edges (co‑divisibility pairs): {int(np.sum(A>0)//2)}")
    st.write(f"Mₙ = {M_n}")

    # Compute Ihara poles
    t0 = time.time()
    poles = ihara_poles(A)
    # Poles are complex; we take those with small imaginary part? Not yet.
    # For comparison with Riemann zeros, we expect poles on the unit circle? Actually,
    # Ihara poles for a finite graph satisfy |u| <= 1, with some on the circle (the Ramanujan condition).
    # But we want to map them to the critical line. A common trick: u = p^{-s}? We'll instead
    # look at the argument: the Ihara zeta is Z(u) = ∏ (1 - λ_i u + u^2) ... for each eigenvalue λ_i of A.
    # The poles u satisfy u^2 - λ_i u + 1 = 0 ⇒ u = (λ_i ± sqrt(λ_i^2 - 4))/2.
    # For |λ_i| ≤ 2, u lies on the unit circle; for |λ_i| > 2, u is real.
    # The connection to the Riemann zeta is through a Mellin transform; we can map u = p^{-s}.
    # For now, we simply take the argument θ = arg(u) and relate it to the imaginary part of zeros.
    # A rough idea: if u = e^{iθ}, then s = 1/2 + i θ/(2π)? This is ad hoc.
    # A better mapping comes from the "determinant formula" for the prime graph's Ihara zeta,
    # which is related to the Hasse-Weil zeta function. We'll use the following: 
    # The Ihara zeta satisfies Z(u) = (1-u^2)^{-(N-1)} ∏_{i=1}^N (1 - λ_i u + u^2)^{-1}.
    # The poles are the zeros of each factor (1 - λ_i u + u^2). Those are exactly u = e^{±iφ} when |λ_i|≤2.
    # The Riemann zeta zeros are encoded in the "limit" of these λ_i. So we can take the phase φ_i
    # from the complex poles and map them to the zero imaginary parts using the density: the number of
    # poles with argument < φ should match the zero counting function N(T) with T = something.
    # We'll use a simple unfolding: sort the phases of the poles that lie on the unit circle,
    # and map them via the zero counting function.
    compute_time = time.time() - t0
    st.write(f"Pole computation time: {compute_time:.2f}s")

    # ---- CORRECTED analysis (D2 retired): raw pole data only, no target-fitting ----
    st.warning("Evidence rules (implementation.md I0): no unfolding, no fits against the "
               "Riemann zeros. Panels below show raw pole data. The old unit-circle claim "
               "was defect M1 (the correct regular-graph locus is |u| = q^{-1/2}; the "
               "weighted locus is governed by the weighted Ihara–Bass identity, findings.md F2).")

    finite = poles[np.isfinite(poles)]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.hist(np.abs(finite), bins=60)
    ax1.set_xlabel('|u| of Ihara pole'); ax1.set_ylabel('count')
    ax1.set_title('Raw pole modulus distribution')
    nonreal = finite[np.abs(finite.imag) > 1e-9]
    ax2.hist(np.angle(nonreal), bins=60)
    ax2.set_xlabel('arg(u) (non-real poles)'); ax2.set_ylabel('count')
    ax2.set_title('Raw pole angle distribution')
    st.pyplot(fig)

    n_real = int(np.sum(np.abs(finite.imag) <= 1e-9))
    st.write(f"Poles: {len(finite)} finite; {n_real} real; "
             f"|u| range [{np.abs(finite).min():.4f}, {np.abs(finite).max():.4f}]")

    st.markdown("""
    **Note.** Any relationship between this graph's Ihara zeta and the Riemann zeta function
    must be established through the corrected path ([path.md](path.md): determinant
    convergence C1, then the Hurwitz dictionary P2), never by rank-fitting pole data to the
    zeros. The honest pipeline is `prime_graph_lab.py`; current measured baselines are in
    [findings.md](findings.md).
    """)

if __name__ == "__main__":
    main()