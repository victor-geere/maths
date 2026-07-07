# Fibonacci Kernel — Phase 1b

*Full note at [project/fibonacci-kernel.md](../../project/fibonacci-kernel.md).*

---

## Status

| Theorem | Statement | Status |
|---|---|---|
| F1 | Domain: positive definite iff $r < 1/\varphi$ | **Proved** |
| F2 | Closed form: $K_r(\theta) = 2\,\Re\frac{re^{i\theta}}{1-re^{i\theta}-r^2e^{2i\theta}}$ | **Proved** |
| F3 | Spectrum: eigenvalues $\lambda_n = F_{|n|}r^{|n|}$ | **Proved** |
| F4 | Total mass: $K_r(0) = \frac{2r}{1-r-r^2}$ | **Proved** |
| §6 numerics | $K_r(0)$, PD grid, eigenvalues vs. FFT, Parseval | **Open** |
| Lucas transfer multiplier | $L_n = F_{n-1}+F_{n+1}$ as bounded multiplier + trace identity | **Open** |

## Open actions

- [ ] Implement `fibonacci_kernel(r, theta)` in toolkit (closed form F2); run four checks and fill §6.
- [ ] State and prove: $L_n r^n = (F_{n-1}+F_{n+1})r^n$ defines a bounded multiplier $M: T^F_r \to T^L_r$ on $L^2(\mathbb{T})$. Write down the explicit-formula trace identity it implies.
