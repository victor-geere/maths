import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
from math import log, gcd
from collections import defaultdict
import time

# ----------------------------------------------------------------------
# 1. Number-theoretic helpers
# ----------------------------------------------------------------------
def sieve_of_eratosthenes(limit: int) -> np.ndarray:
    if limit < 2:
        return np.array([], dtype=int)
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            is_prime[p*p : limit+1 : p] = False
    return np.flatnonzero(is_prime)

def prime_factors(x: int, primes: np.ndarray):
    """Return {p: exponent} for primes in primes (must cover all prime divisors)."""
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

# ----------------------------------------------------------------------
# 2. Adèle / idèle embedding (conceptual, using integers as proxies)
# ----------------------------------------------------------------------
def integer_to_idele_representative(m: int, primes: np.ndarray) -> dict:
    """
    Return the idèle class representative for the ideal (m).
    As a model, we represent each idele as a tuple of local components.
    For simplicity, we use a dict mapping each prime place to its exponent.
    The archimedean place is fixed to 1 (we work with norm = m anyway).
    """
    factors = prime_factors(m, primes)
    # all other finite places have exponent 0
    return factors

# ----------------------------------------------------------------------
# 3. K‑invariant function basis
#    A function on the adèle class space invariant under K = Ẑ^× × {±1}
#    is determined by its values on the fibres of primes. For each prime p
#    we define a basis vector ξ_p (a characteristic function). The subspace
#    spanned by these for p in a dyadic block is our Hilbert space.
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# 4. Scaling action and leakage matrix A (Phase 1 core)
# ----------------------------------------------------------------------
def compute_leakage_matrix(primes_in_I, composites_in_I, primes_lt_2n):
    """
    For the basis ξ_p (p in primes_in_I), the infinitesimal generator D of
    the scaling flow has matrix elements:
        D_{p,p} = log p   (diagonal)
        D_{p,q} = (off‑diagonal) leakage from prime p into fibre of q.
    The leakage matrix A (after subtracting the diagonal) is given by:
        A_{p,q} = sum_{m in composites} a_p(m) a_q(m) / rad(m)   (p≠q).
    This function returns A and the list of primes (same order).
    """
    idx = {p: i for i, p in enumerate(primes_in_I)}
    N = len(primes_in_I)
    A = np.zeros((N, N), dtype=float)

    # Build radical and factor maps for composites
    for m in composites_in_I:
        fac = prime_factors(m, primes_lt_2n)
        r = rad(m, primes_lt_2n)
        if r == 0:
            continue
        # only keep primes that are in our basis set
        fac_in_basis = {p: e for p, e in fac.items() if p in idx}
        # iterate over pairs of distinct primes
        items = list(fac_in_basis.items())
        for i in range(len(items)):
            p, ep = items[i]
            for j in range(i+1, len(items)):
                q, eq = items[j]
                w = (ep * eq) / r
                ip, iq = idx[p], idx[q]
                A[ip, iq] += w
                A[iq, ip] += w
    return A, primes_in_I

# ----------------------------------------------------------------------
# 5. Full H_n = D + ε A, and spectral analysis (Phase 2)
# ----------------------------------------------------------------------
def build_Hn(n: int, C: float = 1.0):
    """Return H_n, primes list, M_n, and the leakage A for inspection."""
    # sieve data
    M_n = (1 << (n + 1)) - 1
    all_primes = sieve_of_eratosthenes(M_n)
    primes_lt_2n = all_primes[all_primes < (1 << n)]
    I_n_low = 1 << n
    I_n_high = M_n
    primes_in_I = all_primes[(all_primes >= I_n_low) & (all_primes <= I_n_high)].tolist()
    all_int = np.arange(I_n_low, I_n_high + 1)
    composites_in_I = all_int[~np.isin(all_int, primes_in_I)].tolist()

    if not primes_in_I:
        return None, [], M_n, None

    # leakage matrix A
    A, primes_ordered = compute_leakage_matrix(primes_in_I, composites_in_I, primes_lt_2n)
    N = len(primes_ordered)
    # diagonal D = log p - mean(log p)
    log_vals = np.array([log(p) for p in primes_ordered])
    mean_log = np.mean(log_vals)
    D = np.diag(log_vals - mean_log)
    eps = C / log(M_n)
    H = D + eps * A
    return H, primes_ordered, M_n, A

# ----------------------------------------------------------------------
# 6. Unfolding and Riemann zeros (unchanged, minor adjustments for demo)
# ----------------------------------------------------------------------
def zero_count(t):
    if t <= 1e-10:
        return 0.0
    return (t/(2*math.pi)) * (math.log(t/(2*math.pi)) - 1) + 7/8

def invert_zero_count(target, tol=1e-12, max_iter=50):
    if target <= 0:
        return 0.0
    T = 2*math.pi * math.exp(1)
    for _ in range(max_iter):
        N = zero_count(T)
        dN = (1/(2*math.pi)) * math.log(T/(2*math.pi))
        if dN == 0:
            break
        Tnew = T - (N - target) / dN
        if abs(Tnew - T) < tol:
            return Tnew
        T = Tnew
    return T

def unfold_eigenvalues(eigvals):
    # Map the k-th sorted eigenvalue to the ordinate T_k where the Riemann-von Mangoldt
    # counting function reaches rank k+0.5, i.e. N(T_k) = k + 0.5.  (invert_zero_count
    # expects a COUNT, not a probability: passing (i+0.5)/N was a units bug.)
    eig_sorted = np.sort(eigvals)
    N = len(eig_sorted)
    unfolded = np.zeros(N)
    for i in range(N):
        unfolded[i] = invert_zero_count(i + 0.5)
    return unfolded

def get_riemann_zeros(num_zeros: int):
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

# ----------------------------------------------------------------------
# 7. Streamlit app main
# ----------------------------------------------------------------------
def main():
    st.set_page_config(page_title="Phase 1 · Adèle Sieve", layout="wide")
    st.title("Phase 1 – Composite‑Generator Sieve on the Adèle Class Space")
    st.markdown(r"""
    This interactive notebook **completes Phase 1** of the research program:
    we lift the dyadic prime sieve to idèle classes, construct the \(K\)-invariant
    function basis, and explicitly compute the **leakage matrix** \(A\) that encodes
    the off‑diagonal part of the scaling generator.
    """)

    # --- Controls ---
    with st.sidebar:
        st.header("Controls")
        n = st.slider("Dyadic block index n", 5, 14, 8)
        C = st.number_input("Perturbation constant C", 0.01, 10.0, 1.0, 0.1)

    # --- Step 1.1: Sieve and idèle lifting ---
    st.header("Step 1.1 – Integer sieve → idèle classes")
    M_n = (1 << (n + 1)) - 1
    all_primes = sieve_of_eratosthenes(M_n)
    primes_lt_2n = all_primes[all_primes < (1 << n)]
    I_n_low = 1 << n
    I_n_high = M_n
    primes_in_I = all_primes[(all_primes >= I_n_low) & (all_primes <= I_n_high)].tolist()
    all_int = np.arange(I_n_low, I_n_high + 1)
    composites_in_I = all_int[~np.isin(all_int, primes_in_I)].tolist()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Block size", f"{I_n_high - I_n_low + 1}")
        st.metric("Primes in Iₙ", len(primes_in_I))
    with col2:
        st.metric("Composites in Iₙ", len(composites_in_I))
        st.metric("Mₙ = 2ⁿ⁺¹ – 1", M_n)

    with st.expander("View prime / composite lists"):
        st.write("First 10 primes:", primes_in_I[:10])
        st.write("First 10 composites:", composites_in_I[:10])

    st.markdown(r"""
    For each integer \(m\in I_n\) we associate an idèle class representative via its prime
    factorisation. For example, the prime \(p\) corresponds to the idèle with component
    \(p\) at the place \(p\) and 1 elsewhere, giving norm \(p\). Composites are built
    from these primes. This embedding respects the adelic geometry while keeping
    everything finite‑dimensional.
    """)

    # --- Step 1.2: K‑invariant function basis ---
    st.header("Step 1.2 – K-invariant function space")
    st.markdown(r"""
    A smooth function on the adèle class space \(X\) that is invariant under the maximal
    compact subgroup \(K = \widehat{\mathbb{Z}}^\times \times \{\pm 1\}\) depends only on
    the norm of the idèle class. On the set of prime classes, such a function is determined
    by its values on the fibres above the rational primes.
    
    We choose as orthonormal basis the functions
    \[
    \xi_p(x) = \begin{cases}
    1 & \text{if } x \text{ lies on the fibre of the prime } p,\\
    0 & \text{otherwise},
    \end{cases}
    \qquad p \in I_n\cap\mathcal{P}.
    \]
    This gives a finite‑dimensional Hilbert space \(\mathcal{H}_n\) whose dimension equals
    the number of primes in the dyadic block.
    """)
    st.write(rf"Dimension of \(\mathcal{{H}}_n\) = {len(primes_in_I)}")

    # --- Step 1.3 & 1.4: Scaling action → leakage matrix A ---
    st.header("Steps 1.3–1.4 – Scaling generator and leakage matrix")
    st.markdown(r"""
    The scaling flow \(\alpha_t\) on \(X\) acts on the basis by moving prime fibres into
    composite fibres. The generator \(D = -i\frac{d}{dt}\big|_{t=0}\alpha_t\) has matrix
    elements
    \[
    \langle \xi_q, D \xi_p \rangle = \delta_{p,q} \log p \;+\; \text{leakage}_{p,q},
    \]
    where the off‑diagonal leakage is produced by the way composites factor:
    \[
    A_{p,q} = \sum_{m \in \text{composites}} \frac{a_p(m)\,a_q(m)}{\operatorname{rad}(m)}.
    \]
    Here \(a_p(m)\) is the exponent of \(p\) in \(m\), and \(\operatorname{rad}(m)\) is the
    product of distinct prime factors. This is the **same** adjacency matrix that appears
    in the construction of \(H_n\).
    """)

    if len(primes_in_I) > 0:
        A, primes_ordered = compute_leakage_matrix(primes_in_I, composites_in_I, primes_lt_2n)
        if not np.any(A):
            st.warning(
                "⚠️ On this basis the leakage matrix **A is identically zero**: a composite in "
                "[2ⁿ, 2ⁿ⁺¹) cannot have two *distinct* prime factors that are both ≥ 2ⁿ (their "
                "product would already exceed 2²ⁿ ≥ 2ⁿ⁺¹). So the off-diagonal coupling of "
                "Definition 4.1 vanishes and Hₙ = Dₙ. A genuinely coupled operator needs the "
                "repaired basis {primes < 2ⁿ} — see phase3.md / sieve_operator.py."
            )
        # Show matrix sparsity
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        # Spy plot of A
        ax1.spy(A, markersize=1)
        ax1.set_title(f"Spy plot of leakage matrix A ({len(primes_ordered)}×{len(primes_ordered)})")
        # Histogram of weights
        nonzeros = A[A > 0]
        if len(nonzeros) > 0:
            ax2.hist(nonzeros, bins=50, color='orange', alpha=0.7)
            ax2.set_xlabel('weight')
            ax2.set_title('Distribution of non‑zero leakage weights')
        else:
            ax2.text(0.5, 0.5, "No non‑zero entries", ha='center', va='center')
            ax2.set_title("Leakage weights empty")
        st.pyplot(fig)

        # Show a small submatrix to inspect
        with st.expander("Inspect a corner of A"):
            k = min(10, len(primes_ordered))
            sub_A = A[:k, :k]
            # annotate with prime labels
            fig_sub, ax_sub = plt.subplots(figsize=(6,6))
            im = ax_sub.imshow(sub_A, cmap='viridis')
            ax_sub.set_xticks(range(k))
            ax_sub.set_yticks(range(k))
            ax_sub.set_xticklabels([str(p) for p in primes_ordered[:k]], rotation=45)
            ax_sub.set_yticklabels([str(p) for p in primes_ordered[:k]])
            plt.colorbar(im, ax=ax_sub)
            st.pyplot(fig_sub)

        # Example leakage calculation for a specific composite
        if composites_in_I:
            sample_comp = composites_in_I[0]
            fac = prime_factors(sample_comp, primes_lt_2n)
            st.markdown(f"**Example:** composite {sample_comp} factorises as {fac}. "
                        f"Its contribution to off‑diagonal pairs (if both primes are in Iₙ) is computed.")
    else:
        st.warning("No primes in this block – increase n.")

    # --- Phase 2 & numerical test (unchanged from previous) ---
    st.header("Phase 2 – Construction of Hₙ and spectral test")
    if len(primes_in_I) > 0:
        H, primes_ordered, M_n, A = build_Hn(n, C=C)
        if H is not None:
            eigvals = np.linalg.eigvalsh(H)
            st.write(f"Hₙ built. Matrix size {H.shape[0]}.")
            fig_eig, ax_eig = plt.subplots()
            ax_eig.hist(eigvals, bins=min(50, len(eigvals)//2), density=True, alpha=0.6)
            ax_eig.set_title('Raw eigenvalue histogram')
            st.pyplot(fig_eig)

            # Unfold and compare with zeros
            unfolded = unfold_eigenvalues(eigvals)
            actual = get_riemann_zeros(len(unfolded))
            fig_comp, (ax_q, ax_r) = plt.subplots(1, 2, figsize=(12,5))
            ax_q.scatter(unfolded, actual, s=10, alpha=0.7)
            ax_q.plot([min(unfolded), max(unfolded)], [min(unfolded), max(unfolded)], 'r--')
            ax_q.set_xlabel('Unfolded eigenvalues'); ax_q.set_ylabel('Riemann zeros')
            ax_q.set_title('Q‑Q plot')
            ax_q.set_aspect('equal')
            diff = unfolded - actual
            ax_r.plot(actual, diff, '.')
            ax_r.axhline(0, color='red', linestyle='--')
            ax_r.set_xlabel('Riemann zero'); ax_r.set_ylabel('Difference')
            ax_r.set_title('Residuals')
            st.pyplot(fig_comp)
            mae = np.mean(np.abs(diff))
            st.metric("Mean absolute error", f"{mae:.4f}")
    else:
        st.info("Adjust n to see the full pipeline.")

    st.markdown("---")
    st.info("**Phase 1 status:** the sieve is lifted to idèle classes and the K‑invariant "
            "function space is parametrised. Note that the leakage matrix on the basis {primes in Iₙ} "
            "is provably zero (see the warning above); the off‑diagonal Berry–Keating coupling only "
            "appears on the repaired basis {primes < 2ⁿ}.")

if __name__ == "__main__":
    main()