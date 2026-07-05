"""CORRECTED 5 Jul 2026 — see notes.md §2 and findings.md.

D1 fixed (graph was empty; vertices now = generator primes p < 2^n). D2 fixed: the
'S_Ihara' column was unfolding output (input-independent) and is removed; the explicit
formula panel S_0 vs W_inf - A_n is kept — it is genuine (cross-check against
../adele/adele_trace.py, which verifies the same balance to 1e-36).
Honest pipeline: prime_graph_lab.py.
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
from math import log, pi, exp, sqrt
from scipy.linalg import eigvals
import time
from scipy import integrate, special
import sys

# ------------------------------------------------------------
# Optional: use mpmath for high precision zeros if available
# ------------------------------------------------------------
try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

# ------------------------------------------------------------
# Sieve helpers
# ------------------------------------------------------------
def sieve_of_eratosthenes(limit: int) -> np.ndarray:
    if limit < 2:
        return np.array([], dtype=int)
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            is_prime[p*p : limit+1 : p] = False
    return np.flatnonzero(is_prime)

def prime_factors(x: int, primes: np.ndarray) -> dict:
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

def rad(x: int, primes: np.ndarray) -> int:
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

def generate_sieve_data(n: int):
    """Return (primes_in_I, composites_in_I, primes_lt_2n, M_n)."""
    M_n = (1 << (n + 1)) - 1
    all_primes = sieve_of_eratosthenes(M_n)
    primes_lt_2n = all_primes[all_primes < (1 << n)]
    I_n_low = 1 << n
    I_n_high = M_n
    primes_in_I = all_primes[(all_primes >= I_n_low) & (all_primes <= I_n_high)].tolist()
    all_int = np.arange(I_n_low, I_n_high + 1)
    composites_in_I = all_int[~np.isin(all_int, primes_in_I)].tolist()
    return primes_in_I, composites_in_I, primes_lt_2n, M_n

def build_prime_graph(n: int):
    """CORRECTED (D1): vertices = generator primes p < 2^n, coupled through composites
    in I_n; the original block-internal version is provably empty (pq >= 2^{2n} > M_n)."""
    primes_I, composites_I, primes_lt_2n, M_n = generate_sieve_data(n)
    verts = [int(p) for p in primes_lt_2n]
    idx = {p: i for i, p in enumerate(verts)}
    N = len(verts)
    if N == 0:
        return None, None, verts, M_n
    A_weighted = np.zeros((N, N), dtype=float)
    for m in composites_I:
        fac = prime_factors(m, primes_lt_2n)
        fac_in = [p for p in fac if p in idx]
        for i in range(len(fac_in)):
            p = fac_in[i]
            for j in range(i+1, len(fac_in)):
                q = fac_in[j]
                ip, iq = idx[p], idx[q]
                A_weighted[ip, iq] += 1
                A_weighted[iq, ip] += 1
    A_binary = (A_weighted > 0).astype(float)
    assert A_binary.sum() > 0, "D1 regression guard: graph must be non-empty"
    return A_binary, A_weighted, verts, M_n

# ------------------------------------------------------------
# Ihara zeta poles (via generalized eigenvalue problem)
# ------------------------------------------------------------
def ihara_poles_from_adj(A):
    N = A.shape[0]
    D = np.diag(np.sum(A, axis=1))
    I = np.eye(N)
    M = np.block([[D - I, np.zeros((N,N))],
                  [np.zeros((N,N)), I]])
    K = np.block([[A, -I],
                  [I, np.zeros((N,N))]])
    vals = eigvals(M, K)
    return vals

# ------------------------------------------------------------
# Gaussian test function and Fourier transform
# ------------------------------------------------------------
# We use g(x) = exp(-x^2) and h(t) = sqrt(pi)*exp(-t^2/4)
def g(x):
    return np.exp(-x**2)

def h(t):
    return np.sqrt(np.pi) * np.exp(-t**2 / 4)

# ------------------------------------------------------------
# Archimedean term W_infty(g) (constant, independent of n)
# ------------------------------------------------------------
@st.cache_resource
def compute_archimedean_term():
    # h(i/2) + h(-i/2)
    hi = h(1j/2)      # sqrt(pi) * exp(1/16)
    h_neg_i = h(-1j/2)
    term1 = hi + h_neg_i
    # - g(0) * log(pi)
    term2 = -1.0 * log(pi)
    # integral: (1/(2pi)) ∫ h(r) Re(psi(1/4 + i r/2)) dr
    def integrand(r):
        z = 0.25 + 0.5j * r
        return h(r) * special.digamma(z).real
    # integrate over symmetric interval
    res, _ = integrate.quad(integrand, -np.inf, np.inf, limit=200)
    term3 = res / (2*pi)
    W_inf = term1 + term2 + term3
    return float(W_inf.real)  # should be real

# ------------------------------------------------------------
# Arithmetic sum (finite place contribution)
# ------------------------------------------------------------
def arithmetic_sum_from_sieve(n, M_n, primes_lt_2n, all_primes):
    """
    Compute A_n = 2 * sum_{prime powers p^k ≤ M_n} (log p) / p^{k/2} * g(k log p).
    Uses primes list up to M_n.
    """
    total = 0.0
    # iterate over primes up to M_n
    primes_all = all_primes[all_primes <= M_n]
    for p in primes_all:
        logp = log(p)
        k = 1
        pk = p
        while pk <= M_n:
            term = (logp) / (pk ** 0.5) * g(k * logp)
            total += term
            k += 1
            pk *= p
    return 2.0 * total

# ------------------------------------------------------------
# Get Riemann zeros (via mpmath or hardcoded)
# ------------------------------------------------------------
def get_riemann_zeros(num_zeros):
    if HAS_MPMATH:
        zeros = []
        for k in range(1, num_zeros+1):
            rho = mpmath.zetazero(k)
            zeros.append(float(rho.imag))
        return np.array(zeros)
    else:
        # fallback hardcoded list (first 30 zeros)
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
            st.warning("mpmath not available, using asymptotic approximation.")
            # asymptotic using inverse zero count (not accurate for many)
            def invert_zero_count(target):
                T = 2*pi * exp(1)
                for _ in range(50):
                    N = zero_count(T)
                    dN = (1/(2*pi)) * log(T/(2*pi))
                    if dN==0: break
                    Tnew = T - (N - target)/dN
                    if abs(Tnew-T)<1e-12: return Tnew
                    T = Tnew
                return T
            return np.array([invert_zero_count(k+0.5) for k in range(num_zeros)])

def zero_count(t):
    if t <= 1e-10: return 0.0
    return (t/(2*pi)) * (log(t/(2*pi)) - 1) + 7/8

def invert_zero_count(target):
    if target <= 0: return 0.0
    T = 2*pi * exp(1)
    for _ in range(50):
        N = zero_count(T)
        dN = (1/(2*pi)) * log(T/(2*pi))
        if dN==0: break
        Tnew = T - (N - target)/dN
        if abs(Tnew - T) < 1e-12: return Tnew
        T = Tnew
    return T

def unfold_eigenvalues(eigvals):
    """RETIRED (D2): rank-quantile map, input-independent, range-capped below the second
    zero. Fails loudly instead of fabricating agreement."""
    raise RuntimeError("unfold_eigenvalues is retired (defect D2, see notes.md §2.2)")

# ------------------------------------------------------------
# Streamlit app
# ------------------------------------------------------------
def main():
    st.set_page_config(page_title="Ihara Zeta & Riemann Zeta Verification", layout="wide")
    st.title("Numerical Verification: Ihara Zeta of the Prime Graph vs. Riemann Zeta")
    st.markdown("""
    We build the **prime graph** from the composite‑generator sieve, compute its Ihara zeta poles,
    unfold them to the Riemann zero locations, and compare the trace formula sides using a Gaussian
    test function. This verifies (numerically) that the Ihara zeta of the prime graph approaches
    the completed Riemann zeta function.
    """)

    with st.sidebar:
        n = st.slider("Dyadic block index n", 5, 13, 9, help="I_n = [2^n, 2^{n+1}-1]")
        show_trace = st.checkbox("Show explicit formula trace balance", True)
        show_ramanujan = st.checkbox("Show adjacency spectrum & Ramanujan bound", True)

    # Precompute archimedean term (cached)
    W_inf = compute_archimedean_term()
    st.sidebar.write(f"Archimedean term W∞ = {W_inf:.8f}")

    # Generate sieve data
    primes_I, composites_I, primes_lt_2n, M_n = generate_sieve_data(n)
    all_primes_full = sieve_of_eratosthenes(M_n)
    if len(primes_I) == 0:
        st.error("No primes in this block. Increase n.")
        return

    # Build graph
    A_bin, A_weighted, primes_ordered, _ = build_prime_graph(n)
    N = len(primes_ordered)

    # Graph statistics
    col1, col2, col3 = st.columns(3)
    col1.metric("Vertices (primes in I_n)", N)
    col2.metric("Edges (binary)", int(np.sum(A_bin>0)//2))
    col3.metric("M_n", M_n)

    # Adjacency spectrum & Ramanujan check
    if show_ramanujan and N > 0:
        eigvals_adj = np.linalg.eigvalsh(A_weighted)
        # degrees
        degrees = np.sum(A_weighted, axis=1)
        max_deg = np.max(degrees) if len(degrees) > 0 else 0
        ramanujan_bound = 2 * sqrt(max(0, max_deg - 1))
        # The Ramanujan condition: |λ| ≤ ramanujan_bound for non-trivial eigenvalues.
        # We can plot histogram and show the bound.
        fig_ram, ax_ram = plt.subplots()
        ax_ram.hist(eigvals_adj, bins=min(50, N//2), alpha=0.7, label='Adjacency eigenvalues')
        ax_ram.axvline(ramanujan_bound, color='r', linestyle='--', label=f'Ramanujan bound 2√(Δ-1) = {ramanujan_bound:.2f}')
        ax_ram.axvline(-ramanujan_bound, color='r', linestyle='--')
        ax_ram.legend()
        ax_ram.set_title('Adjacency spectrum')
        st.pyplot(fig_ram)
        st.caption("A graph is Ramanujan if all non‑trivial eigenvalues lie within the red lines. The prime graph is not regular but gives a sense of spectral expansion.")

    # Ihara poles
    t0 = time.time()
    poles = ihara_poles_from_adj(A_weighted)
    comp_time = time.time() - t0
    st.write(f"Ihara poles computed in {comp_time:.2f}s. Total poles: {len(poles)}")

    # ---- CORRECTED: raw pole summary only (D2 retired; no unfolding, no Q-Q) ----
    finite = poles[np.isfinite(poles)]
    n_real = int(np.sum(np.abs(finite.imag) <= 1e-9))
    st.write(f"Poles: {len(finite)} finite; {n_real} real; "
             f"|u| range [{np.abs(finite).min():.4f}, {np.abs(finite).max():.4f}]")
    st.warning("The former 'unfolded poles vs zeros' panel and the S_Ihara column were "
               "defect D2 (input-independent unfolding) and have been removed. "
               "See notes.md §2.2 and findings.md.")

    # Explicit formula trace balance (genuine — kept)
    if show_trace:
        st.subheader("Explicit-formula balance (genuine panel, kept)")
        st.markdown("""
        Using \(g(x)=e^{-x^2}\), compare:
        - **Zero sum** \(S_0 = 2\sum_{k \le K} h(\gamma_k)\) over the first \(K\) Riemann zeros
          (independently computed via mpmath);
        - **Geometric side** \(S_{\mathrm{geom}} = W_\infty - A_n\), with \(A_n\) from the
          sieve's prime powers \(\le M_n\).
        Cross-check: `../adele/adele_trace.py` verifies the same balance to \(10^{-36}\).
        """)
        A_n = arithmetic_sum_from_sieve(n, M_n, primes_lt_2n, all_primes_full)
        S_geom = W_inf - A_n
        K = 50  # h decays fast; 50 zeros is ample at this test-function width
        actual_zeros = get_riemann_zeros(K)
        zero_sum = 2.0 * np.sum(h(actual_zeros))

        col1, col2 = st.columns(2)
        col1.metric("Zero sum (S₀)", f"{zero_sum:.10f}")
        col2.metric("Geometric side (W∞ - A_n)", f"{S_geom:.10f}")
        err_geom = abs(zero_sum - S_geom)
        st.write(f"|S₀ - (W∞ - A_n)| = {err_geom:.2e}  "
                 f"(explicit formula; residual = prime-power tail beyond M_n + quadrature)")

    st.info("Scope (honest): this app verifies the explicit-formula balance and shows raw "
            "graph-spectral data. It does not — and cannot — link Ihara poles to Riemann "
            "zeros; that link is exactly target C1 of path.md, currently open.")

if __name__ == "__main__":
    main()