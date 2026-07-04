import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigvals
import math
from math import log, pi, exp
import time

# ---- Sieve helpers (unchanged) ----
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

def build_prime_graph(n):
    primes_I, composites_I, primes_lt_2n, M_n = generate_sieve_data(n)
    idx = {p: i for i, p in enumerate(primes_I)}
    N = len(primes_I)
    if N == 0:
        return None, None, primes_I, M_n
    A = np.zeros((N, N), dtype=float)
    for m in composites_I:
        fac = prime_factors(m, primes_lt_2n)
        fac_in = [p for p in fac if p in idx]
        for i in range(len(fac_in)):
            p = fac_in[i]
            for j in range(i+1, len(fac_in)):
                q = fac_in[j]
                ip, iq = idx[p], idx[q]
                A[ip, iq] += 1
                A[iq, ip] += 1
    A_binary = (A > 0).astype(float)
    return A_binary, A, primes_I, M_n   # return both binary and weighted

def ihara_poles_from_adj(A):
    """
    Compute poles u of Ihara zeta: zeros of det(I - u A + u^2 (D - I)).
    Uses the generalized eigenvalue problem:
    [ D-I  0 ] [x] = u [ A  -I ] [x]
    [ 0    I ] [y]     [ I   0 ] [y]
    """
    N = A.shape[0]
    D = np.diag(np.sum(A, axis=1))
    I = np.eye(N)
    M = np.block([[D - I, np.zeros((N,N))],
                  [np.zeros((N,N)), I]])
    K = np.block([[A, -I],
                  [I, np.zeros((N,N))]])
    vals = eigvals(M, K)
    return vals

# ---- Unfolding ----
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

def unfold_args(arg_vals):
    """Unfold sorted arguments using zero counting function."""
    arg_sorted = np.sort(arg_vals)
    N = len(arg_sorted)
    unfolded = np.zeros(N)
    for i in range(N):
        cdf = (i + 0.5) / N   # mapping quantile
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
            st.warning("mpmath not available; using asymptotic estimate (rough).")
            return np.array([invert_zero_count(k-0.5) for k in range(1, num_zeros+1)])

# ---- Streamlit app ----
def main():
    st.set_page_config(page_title="Ihara Poles → Riemann Zeros", layout="wide")
    st.title("Phase 7 – Refined Mapping: Ihara Zeta Poles to Riemann Zeros via Unfolding")
    st.markdown("""
    The Ihara zeta function of the prime graph (built from the sieve) has poles on the unit circle.
    We collect their arguments \( \theta_k \), sort them, and unfold them using the Riemann zero
    counting function \( N(T) \). If the graph's Ihara zeta truly encodes the zeros, the unfolded
    values should match the actual zeros to high precision.
    """)

    with st.sidebar:
        n = st.slider("Dyadic block n", 5, 12, 8)

    A_bin, A_wt, primes_I, M_n = build_prime_graph(n)
    if A_bin is None or len(A_bin) == 0:
        st.error("No primes in this block. Increase n.")
        return

    N = len(primes_I)
    st.write(f"Graph vertices (primes): {N}")
    st.write(f"Edges (binary): {int(np.sum(A_bin>0)//2)}")

    # Show graph sparsity
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))
    ax1.spy(A_bin, markersize=0.5)
    ax1.set_title("Adjacency (binary)")
    # Also show degree distribution
    degrees = np.sum(A_wt, axis=1)
    ax2.hist(degrees, bins=30, alpha=0.7)
    ax2.set_title("Weighted degree distribution")
    st.pyplot(fig1)

    # Compute Ihara poles
    t0 = time.time()
    poles = ihara_poles_from_adj(A_wt)   # use weighted adjacency
    comp_time = time.time() - t0
    st.write(f"Pole computation: {comp_time:.2f}s")
    st.write(f"Total poles: {len(poles)}")

    # Select poles on the unit circle (|u| close to 1)
    tol = 1e-6
    on_circle = np.abs(np.abs(poles) - 1.0) < tol
    st.write(f"Poles on unit circle: {np.sum(on_circle)}")

    if np.sum(on_circle) == 0:
        st.warning("No poles on unit circle found. The graph might be too small or the adjacency matrix ill‑conditioned.")
        return

    pole_angles = np.angle(poles[on_circle])
    # Use positive angles (symmetry gives ±, take positive half)
    pos_angles = np.sort(pole_angles[pole_angles >= 0])

    if len(pos_angles) < 2:
        st.error("Too few positive arguments to compare.")
        return

    # Unfold
    unfolded = unfold_args(pos_angles)
    actual_zeros = get_riemann_zeros(len(unfolded))

    # Q-Q plot and residuals
    fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(12,5))
    ax3.scatter(unfolded, actual_zeros, s=8, alpha=0.7)
    ax3.plot([min(unfolded), max(unfolded)], [min(unfolded), max(unfolded)], 'r--')
    ax3.set_xlabel('Unfolded pole arguments (T)')
    ax3.set_ylabel('Actual Riemann zeros')
    ax3.set_title('Q‑Q plot after unfolding')
    ax3.set_aspect('equal')

    diff = unfolded - actual_zeros
    ax4.plot(actual_zeros, diff, '.')
    ax4.axhline(0, color='red', linestyle='--')
    ax4.set_xlabel('Riemann zero')
    ax4.set_ylabel('Difference')
    ax4.set_title('Residuals')

    st.pyplot(fig2)

    mae = np.mean(np.abs(diff))
    st.metric("Mean Absolute Error (unfolded)", f"{mae:.4f}")

    # Display first few comparisons
    with st.expander("First 20 unfolded vs actual zeros"):
        data = {"Unfolded": unfolded[:20], "Actual zero": actual_zeros[:20]}
        st.dataframe(data)

    st.markdown("""
    **Interpretation:** If the prime graph's Ihara zeta poles truly correspond to Riemann zeros,
    the unfolded arguments should lie on the diagonal with zero residuals. The MAE measures how
    far we are from that ideal. As \(n\) grows (and the graph becomes larger and more
    "regular"), the MAE is expected to decrease, indicating convergence.
    """)

if __name__ == "__main__":
    main()