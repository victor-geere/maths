# Computational Toolkit — Specification

*Status: **partial**. `victor/prime-zeros.py` supplies `channels`, `sign_aware_helix`, `quaternion_cone`, and (Phase 1c) `ou_mehler` + `ou_hermite_sum`. The `fibonacci_kernel` and `eta_kernel` functions below are not yet implemented.*

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

### `ou_mehler(t, x, y)` — **DONE**

Computes the Mehler kernel $p_t(x,y) = \dfrac{1}{\sqrt{1-r^2}} \exp\!\left(\dfrac{2rxy - r^2(x^2+y^2)}{2(1-r^2)}\right)$, $r = e^{-t}$. Implemented in `victor/prime-zeros.py` alongside `ou_hermite_sum(t, x, y, n_max)` (truncated Hermite bilinear series). The `mpmath` Mellin / $\Gamma(s)\zeta(s)$ check lives in `victor/ou-verify.py`.

**Verification checks** (§7 of `project/ou-process.md` — all pass):

- [x] Mehler closed form vs. truncated Hermite sum $\sum_{n=0}^N e^{-nt} He_n(x) He_n(y) / n!$ — worst $9\times10^{-12}$ (N=80).
- [x] Heat trace $\mathrm{tr}(P_t) = 1/(1-e^t{}^{-1})$ vs. eigenvalue sum **and** Mehler diagonal integral — $5\times10^{-41}$.
- [x] Bernoulli coefficients of $t/(e^t-1)$ expansion — exact.
- [x] Mellin: $\int_0^\infty t^{s-1}\,\Theta(t)\,dt = \Gamma(s)\zeta(s)$, $\Theta=1/(e^t-1)$ — $1\times10^{-22}$ at $s=2,3,\tfrac32,2+3i$.
- [x] (bonus) Intertwiner $JP_t=D_rJ$ via Poisson convolution (Lemma O6) — $5\times10^{-15}$.

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
