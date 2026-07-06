"""CORRECTED 5 Jul 2026 — see notes.md §2 and findings.md.

D1 fixed: the original graph (primes in I_n coupled via composites in I_n) is provably
empty; vertices are now the generator primes p < 2^n. D2 fixed: rank-unfolding against
the zero-counting function is retired (it ignored its input — identical output for any
data — and its range was capped below the second zero). This app now reports raw-gap
statistics with data-internal normalisation only (implementation.md I0/I3).
Honest pipeline: prime_graph_lab.py.
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigvals
import math
from math import log, pi, exp, erf, sqrt
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
    """CORRECTED (D1): vertices = generator primes p < 2^n, coupled through composites
    in I_n. The original block-internal version is provably empty (pq >= 2^{2n} > M_n)."""
    primes_I, composites_I, primes_lt_2n, M_n = generate_sieve_data(n)
    verts = [int(p) for p in primes_lt_2n]
    idx = {p: i for i, p in enumerate(verts)}
    N = len(verts)
    if N == 0:
        return None, None, verts, M_n
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
    assert A_binary.sum() > 0, "D1 regression guard: graph must be non-empty"
    return A_binary, A, verts, M_n   # return both binary and weighted

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
    """RETIRED (D2): ignored its input (rank-quantiles only) and could not exceed
    N^{-1}(1) ~ 14.9 — every reported 'match' was fabricated. Fails loudly now."""
    raise RuntimeError("unfold_args is retired (defect D2, see notes.md §2.2); "
                       "use raw gaps with data-internal normalisation — rule I0.1/I3")

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
    st.title("Corrected: Raw Ihara Pole Statistics of the (fixed) Prime Graph")
    st.markdown("""
    The graph now couples the generator primes p < 2^n through the composites in the dyadic
    block (defect D1 fixed). We show **raw** pole data and gap statistics with data-internal
    normalisation only — the former unfolding step was defect D2 (input-independent) and is
    retired. See notes.md §2 and findings.md.
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

    # ---- CORRECTED analysis (D2 retired): raw-gap statistics, data-internal only ----
    st.warning("Evidence rules (implementation.md I0/I3): unfolding against the Riemann "
               "counting function is retired (defect D2). Below: raw non-real pole angle "
               "gaps, normalised by their own mean, against RMT reference curves.")

    finite = poles[np.isfinite(poles)]
    nonreal = finite[np.abs(finite.imag) > 1e-9]
    th = np.sort(np.angle(nonreal))
    th = th[th > 0]
    if len(th) < 20:
        st.error("Too few non-real poles for gap statistics.")
        return

    gaps = np.diff(th)
    gaps = gaps / gaps.mean()           # data-internal normalisation only
    xs = np.sort(gaps)
    F_emp = np.arange(1, len(xs) + 1) / len(xs)
    F_cue = np.array([erf(2*x/sqrt(pi)) - (4*x/pi)*np.exp(-4*x*x/pi) for x in xs])
    F_poi = 1 - np.exp(-xs)
    ks_cue = float(np.max(np.abs(F_emp - F_cue)))
    ks_poi = float(np.max(np.abs(F_emp - F_poi)))

    fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 5))
    ax3.hist(gaps, bins=40, density=True, alpha=0.6, label='raw gaps (mean-normalised)')
    ss = np.linspace(0, 4, 200)
    ax3.plot(ss, (32/np.pi**2)*ss**2*np.exp(-4*ss**2/np.pi), 'r-', label='Wigner β=2 (CUE)')
    ax3.plot(ss, np.exp(-ss), 'g--', label='Poisson')
    ax3.legend(); ax3.set_xlabel('normalised gap'); ax3.set_title('Raw angle-gap density')
    ax4.plot(xs, F_emp - F_cue, label=f'KS to CUE = {ks_cue:.3f}')
    ax4.plot(xs, F_emp - F_poi, label=f'KS to Poisson = {ks_poi:.3f}')
    ax4.axhline(0, color='k', lw=0.5); ax4.legend(); ax4.set_title('CDF differences')
    st.pyplot(fig2)

    st.markdown("""
    **Interpretation (honest):** these statistics are a *consistency diagnostic only* —
    RMT agreement, even if it appeared, would not be evidence about zero locations
    (research-findings §8). Baseline measured values are recorded in
    [findings.md](findings.md) (F9): at current weightings the gaps match neither CUE nor
    Poisson; the locus is structure-dominated.
    """)

if __name__ == "__main__":
    main()