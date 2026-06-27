# Computational Toolkit — Specification

*Status: **partial**. `victor/prime-zeros.py` supplies `channels`, `sign_aware_helix`, and `quaternion_cone`. The three functions below are not yet implemented.*

---

## Existing functions (in `victor/prime-zeros.py`)

| Function | Inputs | Outputs |
|---|---|---|
| `channels(omega, eps, sigma, n_max)` | frequency grid, mollifier, bandwidth, prime-power cutoff | `Z, P, G` arrays |
| `sign_aware_helix(omega, R)` | grid, signal | `amp, phi, flips, x, y, z` |
| `quaternion_cone(Z, P, G)` | three channels | cone indicator $Z^2-(P^2+G^2)$ |

---

## Functions to implement

### `fibonacci_kernel(r, theta)`

Compute $K_r(\theta) = 2\,\Re\dfrac{re^{i\theta}}{1-re^{i\theta}-r^2e^{2i\theta}}$ using the closed form (Theorem F2).

**Verification checks** (to fill §6 of `project/fibonacci-kernel.md`):

- `K_r(0)` equals truncated sum $2\sum_{n=1}^N F_n r^n$ to 10 digits.
- Minimum over $\theta$-grid $\ge 0$ (positive definiteness).
- FFT of sampled $K_r$ matches eigenvalues $\lambda_n = F_n r^n$.
- $\|K_r\|_2^2 = \sum_n \lambda_n^2$ (Parseval).

### `ou_mehler(t, x, y)`

Compute the Mehler kernel $p_t(x,y) = \dfrac{1}{\sqrt{1-r^2}} \exp\!\left(\dfrac{2rxy - r^2(x^2+y^2)}{2(1-r^2)}\right)$, $r = e^{-t}$.

Requires `mpmath` for the Mellin / $\Gamma(s)\zeta(s)$ check.

**Verification checks** (to fill §7 of `project/ou-process.md`):

- Mehler closed form vs. truncated Hermite sum $\sum_{n=0}^N e^{-nt} H_n(x) H_n(y) / n!$.
- Heat trace $\mathrm{tr}(P_t) = 1/(e^t-1)$ vs. numerical sum.
- Bernoulli coefficients of $t/(e^t-1)$ expansion.
- Mellin: $\int_0^\infty t^{s-1} \mathrm{tr}(P_t)\,dt = \Gamma(s)\zeta(s)$ to 8 digits at $s=2$.

### `eta_kernel(r, theta)`

Compute $K^\eta_r(\theta) = -K^\zeta_r(\theta+\pi)$ (Theorem E3: rotation by $\pi$).

**Verification checks** (to fill §5 of `project/eta-zeta-transfer.md`):

- Rotation identity: $K^\eta_r(\theta) + K^\zeta_r(\theta+\pi) \approx 0$ on grid.
- Extra zeros at $\theta = k\log 2 \pmod{2\pi}$ (transfer correction poles).
- Dirichlet coefficients of transfer correction $= 1/k$.

---

## Dependencies

```
numpy        # array ops
matplotlib   # plotting (optional)
mpmath       # high-precision Mellin integral (ou_mehler verification)
```

Install: `pip install -r victor/requirements.txt mpmath`
