import numpy as np

# --- Input data ---------------------------------------------------------

# First nontrivial Riemann zeta zeros (positive imaginary parts).
zeros = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
    37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
]


def von_mangoldt_terms(n_max):
    """Prime-power positions log(n) and weights Lambda(n)/sqrt(n).

    Lambda(n) is the von Mangoldt function: log(p) when n = p**k, else 0.
    Returns two aligned lists (same length, position[i] <-> weight[i]).
    """
    positions, weights = [], []
    for n in range(2, n_max + 1):
        m, p = n, 2
        # Find the smallest prime factor p of n.
        while p * p <= m and m % p != 0:
            p += 1
        if p * p > m:
            p = m  # n itself is prime
        # n is a prime power iff repeatedly dividing by p reaches 1.
        k = n
        while k % p == 0:
            k //= p
        if k == 1:
            positions.append(np.log(n))
            weights.append(np.log(p) / np.sqrt(n))
    return positions, weights


def channels(omega, eps=0.05, sigma=0.2, n_max=100):
    """The three explicit-formula channels (Z, P, G) on the omega grid.

    These are the three real channels of the spectral quaternion
    K = Z - i P + j G (spectral-triple.html sect. 9 uses +i P; here the i-channel
    carries -P so K mirrors the subtraction in R = Z - P + G):

      Z : zero contributions (positive), a Gaussian bump at each zero ordinate.
      P : prime-power contributions (von Mangoldt weighted), subtracted in R.
      G : smooth archimedean / Gamma term (approximate); the j (time) channel.
    """
    prime_logs, prime_weights = von_mangoldt_terms(n_max)
    Z = np.zeros_like(omega)
    for g in zeros:
        Z += np.exp(-eps * g) * np.exp(-((omega - g) / sigma) ** 2)
    P = np.zeros_like(omega)
    for pos, weight in zip(prime_logs, prime_weights):
        P += weight * np.exp(-eps * pos) * np.exp(-((omega - pos) / sigma) ** 2)
    G = 0.1 * np.exp(-0.03 * omega)
    return Z, P, G


def sign_aware_helix(omega, R):
    """Lift the (possibly negative) signal R to a helix that records sign as winding.

    On the circle a negative value -a = a * e^{i pi} is indistinguishable from a
    positive value rotated by half a turn. Here each sign flip of R adds pi to a
    cumulative winding angle, so accumulated negativity becomes genuine rotation
    beyond 2 pi along the climbing (time) axis z = phi. The radius is |R| >= 0, so
    positivity is restored as amplitude. (See helix-quaternion-proposal.md, Def H3.)

    Returns (amp, phi, flips, x, y, z).
    """
    amp = np.abs(R)
    s = np.sign(R)
    # Forward-fill zeros with the previous nonzero sign so they do not spuriously flip.
    idx = np.where(s != 0, np.arange(len(s)), 0)
    np.maximum.accumulate(idx, out=idx)
    s_filled = s[idx]
    # Cumulative count of genuine sign changes (each contributes a half-turn, pi).
    flips = np.concatenate(([0], np.cumsum(np.abs(np.diff(s_filled)) > 0)))
    phi = omega + np.pi * flips           # base angle + accumulated half-turns
    x = amp * np.cos(phi)
    y = amp * np.sin(phi)
    z = phi                               # climb by total winding (time axis)
    return amp, phi, flips, x, y, z


def quaternion_cone(Z, P, G):
    """Quaternionic positivity indicator z^2 - (p^2 + g^2) (Theorem 9.1).

    With the spectral quaternion K = Z - i P + j G (the i-channel carries -P so it
    mirrors the subtraction in R = Z - P + G), K lies in the closure of the
    positive cone iff Z >= 0 and sqrt(P^2 + G^2) <= Z, i.e. the indicator >= 0.
    The sign of the i-channel does not affect the cone, which depends on P^2; the
    j-axis carries the G (archimedean / time) channel.
    """
    return Z ** 2 - (P ** 2 + G ** 2)


# --- Ornstein-Uhlenbeck / Mehler kernel (project/ou-process.md, Phase 1c) ------


def ou_mehler(t, x, y):
    """Mehler kernel M_t(x, y) of the OU semigroup P_t = e^{tL} (Theorem O3).

    Closed form, valid for t > 0 with r = e^{-t} in (0, 1):

        M_t(x, y) = (1 - r^2)^{-1/2} exp( (2 r x y - r^2 (x^2 + y^2)) / (2 (1 - r^2)) ).

    This is the density of the OU transition kernel against the Gaussian gamma,
    reproducing P_t f(x) = \\int M_t(x, y) f(y) gamma(dy) with P_t He_n = r^n He_n.
    Accepts scalar or numpy-array x, y (broadcasting).
    """
    r = np.exp(-t)
    r2 = r * r
    return np.exp((2 * r * x * y - r2 * (x ** 2 + y ** 2)) / (2 * (1 - r2))) / np.sqrt(1 - r2)


def ou_hermite_sum(t, x, y, n_max):
    """Truncated Mehler bilinear series sum_{n<=N} (r^n / n!) He_n(x) He_n(y).

    Probabilists' Hermite polynomials He_n (numpy.polynomial.hermite_e), evaluated
    via their three-term recurrence. Converges to ou_mehler(t, x, y) as n_max -> oo
    (Mehler's formula). Used as the independent cross-check of the closed form.
    """
    r = np.exp(-t)
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    total = np.zeros(np.broadcast(x, y).shape)
    # He_0 = 1, He_1 = z, He_{n+1}(z) = z He_n(z) - n He_{n-1}(z).
    hx_prev, hx_cur = np.ones_like(x), x.copy()
    hy_prev, hy_cur = np.ones_like(y), y.copy()
    rn, fact = 1.0, 1.0          # r^n and n! for the current n
    total = total + rn / fact * hx_prev * hy_prev   # n = 0 term
    for n in range(1, n_max + 1):
        rn *= r
        fact *= n
        total = total + rn / fact * hx_cur * hy_cur
        hx_prev, hx_cur = hx_cur, x * hx_cur - n * hx_prev
        hy_prev, hy_cur = hy_cur, y * hy_cur - n * hy_prev
    return total


# --- Build the curves ---------------------------------------------------

eps = 0.05
omega = np.linspace(0, 100, 5000)
Z, P, G = channels(omega, eps=eps)
R = Z - P + G                             # the explicit-formula signal

amp, phi, flips, hx, hy, hz = sign_aware_helix(omega, R)
cone = quaternion_cone(Z, P, G)

# Spectral quaternion K = Z - i P + j G as a 4-vector (a, b, c, d) = a + b i +
# c j + d k. The i-channel carries -P so K mirrors R = Z - P + G exactly.
q_spectral = np.stack([Z, -P, G, np.zeros_like(Z)], axis=1)

# j-time lift: the quaternionic exponential amp * (cos phi + j sin phi), i.e. the
# helix embedded in the (1, j) plane of H. As a 4-vector (a, b, c, d) = a + b i +
# c j + d k this is (amp cos phi, 0, amp sin phi, 0).
q_time = np.stack([amp * np.cos(phi), np.zeros_like(phi),
                   amp * np.sin(phi), np.zeros_like(phi)], axis=1)


if __name__ == "__main__":
    prime_logs, _ = von_mangoldt_terms(100)
    n_flips = int(flips[-1])
    print(f"{len(zeros)} zeros, {len(prime_logs)} prime-power terms")
    print(f"R range: [{R.min():.4f}, {R.max():.4f}]")
    print(f"peak at omega = {omega[np.argmax(R)]:.4f}")
    print(f"sign flips of R: {n_flips}  ->  total winding "
          f"{phi.max() / (2 * np.pi):.2f} x 2pi  "
          f"(naive helix: {omega.max() / (2 * np.pi):.2f} x 2pi)")
    in_cone = cone.min() >= 0
    print(f"quaternion cone min: {cone.min():.4f}  "
          f"({'stays >= 0 (in cone)' if in_cone else 'goes negative (outside cone)'})")

    try:
        import matplotlib.pyplot as plt

        fig = plt.figure(figsize=(11, 5))

        # Sign-aware helix, coloured by sign of R (red = wound a half-turn past).
        ax = fig.add_subplot(1, 2, 1, projection="3d")
        pos = R >= 0
        ax.plot(hx, hy, hz, lw=0.4, color="0.7")
        ax.scatter(hx[pos], hy[pos], hz[pos], s=2, c="tab:blue", label="R >= 0")
        ax.scatter(hx[~pos], hy[~pos], hz[~pos], s=2, c="tab:red",
                   label="R < 0 (wound past)")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("winding phi (time)")
        ax.set_title("Sign-aware helix lift")
        ax.legend(loc="upper left", fontsize=8)

        # Quaternion positivity cone indicator.
        ax2 = fig.add_subplot(1, 2, 2)
        ax2.plot(omega, cone, lw=0.8, color="tab:purple")
        ax2.axhline(0, color="tab:red", lw=1, ls="--")
        ax2.set_xlabel("omega")
        ax2.set_ylabel("z^2 - (p^2 + g^2)")
        ax2.set_title("Quaternion positivity cone indicator")

        plt.tight_layout()
        plt.show()
    except ModuleNotFoundError:
        print("(install matplotlib to view the helix and cone)")
