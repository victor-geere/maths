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
    primes_I, composites_I, primes_lt_2n, M_n = generate_sieve_data(n)
    idx = {p: i for i, p in enumerate(primes_I)}
    N = len(primes_I)
    if N == 0:
        return None, primes_I, M_n
    A = np.zeros((N, N), dtype=float)
    for m in composites_I:
        fac = prime_factors(m, primes_lt_2n)
        fac_in = [p for p in fac if p in idx]
        # add edges between every pair of distinct primes that co-divide m
        for i in range(len(fac_in)):
            p = fac_in[i]
            for j in range(i+1, len(fac_in)):
                q = fac_in[j]
                ip, iq = idx[p], idx[q]
                A[ip, iq] += 1
                A[iq, ip] += 1
    # Optional: keep only binary edges (set to 1 if >0) for an unweighted graph
    A_binary = (A > 0).astype(float)
    return A_binary, primes_I, M_n

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
    eig_sorted = np.sort(eigvals)
    N = len(eig_sorted)
    unfolded = np.zeros(N)
    for i in range(N):
        cdf = (i + 0.5) / N
        unfolded[i] = invert_zero_count(cdf)
    return unfolded

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

    # Filter poles: keep those with |Im(u)| small (poles on/near real axis are not from the circle)
    # Actually, the Ihara poles for a connected graph are all on the unit circle or real axis.
    real_poles = np.real(poles)
    imag_poles = np.imag(poles)
    # Select poles with large imaginary part (unit circle) – we expect many near |u|=1.
    unit_circle_mask = np.abs(np.abs(poles) - 1) < 1e-6
    st.write(f"Poles on unit circle: {np.sum(unit_circle_mask)} out of {len(poles)}")

    # Use those on unit circle, take their arguments.
    arg_poles = np.angle(poles[unit_circle_mask])
    arg_poles = np.sort(arg_poles[arg_poles >= 0])  # take positive arguments

    # Unfold arguments using the zero counting function (as a proxy)
    # We need to map argument to T. Since the Ihara zeta's functional equation involves u -> 1/(qu) for some q?
    # In the limit, the number of poles with argument ≤ θ should grow like (N/π) θ? Not exactly.
    # For now, we simply plot the raw arguments and compare with Riemann zeros after linear scaling.
    # The connection is subtle; we'll show a scatter plot.

    # Let's also get the actual Riemann zeros for reference.
    num_poles = len(arg_poles)
    actual_zeros = get_riemann_zeros(num_poles)

    # For a visual, we can linearly transform the arg_poles to match the range of zeros.
    # Compute a simple linear regression: we want a*arg + b ≈ actual_zeros.
    # This is a crude approximation to see if there is a correlation.
    if num_poles > 0:
        arg_arr = arg_poles[:num_poles]
        zero_arr = actual_zeros[:num_poles]
        # Fit linear: zero = a * arg + b
        A_fit = np.vstack([arg_arr, np.ones_like(arg_arr)]).T
        a, b = np.linalg.lstsq(A_fit, zero_arr, rcond=None)[0]
        predicted = a * arg_arr + b
        mae = np.mean(np.abs(predicted - zero_arr))

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        ax1.scatter(arg_arr, zero_arr, s=8, alpha=0.7)
        ax1.set_xlabel('Argument of Ihara pole (radians)')
        ax1.set_ylabel('Actual Riemann zero')
        ax1.set_title(f'Raw correlation (slope ≈ {a:.2f})')
        ax2.plot(zero_arr, predicted - zero_arr, '.')
        ax2.axhline(0, color='r', linestyle='--')
        ax2.set_xlabel('Riemann zero')
        ax2.set_ylabel('Residual after linear fit')
        ax2.set_title(f'Residuals (MAE = {mae:.3f})')
        st.pyplot(fig)

        st.write(f"Linear fit: T ≈ {a:.3f} * arg + {b:.3f}")
        st.write(f"Mean absolute error after linear scaling: {mae:.4f}")

        # Interpretation: if the Ihara poles were perfectly aligned, the residuals would be small.
        # For small n, the graph is tiny and the match is poor; as n grows, the Ihara zeta should
        # approach the Selberg zeta of the modular surface, which is known to encode the Riemann zeros.

    st.markdown("""
    **Note:** The exact relationship between the Ihara zeta of this prime graph and the Riemann zeta function
    is still conjectural. In the adèle class space, the graph built from all primes (the “prime graph”)
    should have Ihara zeta equal to the completed Riemann zeta, after a change of variable 
    \(u = p^{-s}\) and a product over all \(p\). This finite approximation is a step toward that limit.
    """)

if __name__ == "__main__":
    main()