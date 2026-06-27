# Spectral Data Sheet

*One row per catalogue object. Fill in as each object's note is verified numerically.*

Columns: **object** | **kernel closed form** | **damping range** | **spectrum** $\{\lambda_n\}$ | **self-adjoint domain** | **dual object** | **explicit function** (explicit-formula / trace identity) | **Fredholm determinant** $\det(I-zT_K)=\prod_n(1-z\lambda_n)$ | **status**

---

| Object | Kernel closed form | Damping | Spectrum | S.a. domain | Dual | Explicit function (explicit-formula / trace identity) | Fredholm determinant $\det(I-zT_K)=\prod_n(1-z\lambda_n)$ | Status |
|---|---|---|---|---|---|---|---|---|
| Prime sine wave $\sum_p p^{-s}\sin(p\pi x)$ | none (no closed form) | $\Re s > \tfrac{1}{2}$ | $\{p^{-2\sigma}\}$ | $L^2[0,2]$, $\sigma > \tfrac{1}{2}$ | — | prime zeta $P(s)=\sum_p p^{-s}=\sum_{k\ge1}\tfrac{\mu(k)}{k}\log\zeta(ks)$; energy $\lVert\Psi_s\rVert^2=P(2\sigma)$ | $\prod_p(1-z\,p^{-2\sigma})$; $=1/\zeta(2\sigma)$ at $z=1$ (Euler product) | **Complete** (T1–T4 + §6) |
| Natural sine wave $\sum_n n^{-s}\sin(n\pi x)$ | $\mathrm{Im}\,\mathrm{Li}_s(e^{i\pi x})$ (Clausen; Dirichlet damping) | $\Re s > \tfrac{1}{2}$ | $\{n^{-2\sigma}\}$ | $L^2[0,2]$, $\sigma > \tfrac{1}{2}$ | $\zeta$ (energy $\zeta(2\sigma)$, kernel $\zeta(s+\overline{s'})$) | reproducing kernel $\langle\Psi_s,\Psi_{s'}\rangle=\zeta(s+\overline{s'})$; energy $\zeta(2\sigma)$ | $\prod_{n\ge1}(1-z\,n^{-2\sigma})$; $=\dfrac{\sin(\pi\sqrt z)}{\pi\sqrt z}$ at $\sigma=1$ | **Complete** (T1–T5 + §7) |
| Fibonacci $F_n$ | $2\,\Re\dfrac{re^{i\theta}}{1-re^{i\theta}-r^2e^{2i\theta}}$ | $r < 1/\varphi$ | $\{F_n r^n\}$ | $L^2(\mathbb{T})$, any $r < 1/\varphi$ | Lucas (open) | Binet $F_n=\dfrac{\varphi^n-(-\varphi)^{-n}}{\sqrt5}$; dual multiplier $L_n=F_{n-1}+F_{n+1}$ | $\prod_{n\ge1}(1-z\,F_n r^n)$; $q$-Pochhammer type ($q=\varphi r$), no elementary closed form | Proofs done; §6 open |
| OU / integers $\mathbb{N}$ | Mehler: $\dfrac{1}{\sqrt{1-r^2}}e^{(2rxy-r^2(x^2+y^2))/2(1-r^2)}$ | $r = e^{-t} < 1$ | $\{e^{-nt}\}$ | $L^2(\gamma)$, any $t > 0$ | Spectral zeta $= \zeta$ | Mellin trace $\Gamma(s)\zeta(s)=\int_0^\infty\dfrac{u^{s-1}}{e^u-1}\,du$ (primed heat trace) | $\prod_{n\ge0}(1-z\,e^{-nt})=(z;q)_\infty$, $q=e^{-t}$ ($q$-Pochhammer) | Proofs done; §7 open |
| Dirichlet eta (alternating) | $-K^\zeta_r(\theta+\pi)$ | $r < 1$ | alternating signs $\{(-1)^{n-1}n^{-1/2}r^n\}$ | $L^2(\mathbb{T})$ | $\zeta$ via rotation by $\pi$ | $\eta(s)=(1-2^{1-s})\zeta(s)=\sum_n(-1)^{n-1}n^{-s}$; transfer $=$ rotation by $\pi$ | $\prod_n(1-z(-1)^{n-1}n^{-1/2}r^n)$; $=$ ζ-magnitude det under $r\to-r$ | E1–E4 proved; §5 open |
| Zeta magnitude $n^{-1/2}$ (**geometric** damping $r^n$, cf. Dirichlet row above) | $2\,\Re\,\mathrm{Li}_{1/2}(re^{i\theta})$ | $r < 1$ | $\{n^{-1/2}r^n\}$ | $L^2(\mathbb{T})$ | Zeros via Weil | generating fn $\sum_n n^{-1/2}r^ne^{in\theta}=\mathrm{Li}_{1/2}(re^{i\theta})$; zeros via Weil (heuristic) | $\prod_{n\ge1}(1-z\,n^{-1/2}r^n)$; $q$-type, no elementary closed form | Heuristic |
| Riemann zeros $\gamma_n$ | $2\sum_n \gamma_n r^n \cos n\theta$ | $r < 1$ | $\{\gamma_n r^n\}$ | $L^2(\mathbb{T})$ | Prime powers via Weil | Riemann–Weil $\sum_\gamma\hat f(\gamma)=2\hat f(\tfrac{i}{2})-2\sum_n\tfrac{\Lambda(n)}{\sqrt n}f(\log n)+\text{arch}$ (verified) | damped $\prod_n(1-z\gamma_n r^n)$; true spectral det $=\xi(s)/\xi(0)=\prod_\rho(1-s/\rho)$ (Hadamard) | Transfer identity **verified** (~40 digits); positivity↔RH conditional |
| Prime powers $\Lambda(n)/n^{1/2}$ | none (no closed form) | Gaussian | von Mangoldt weights | — | Zeros via Weil ($\sigma=\tfrac12$) | von Mangoldt $\psi(x)=x-\sum_\rho\tfrac{x^\rho}{\rho}-\log2\pi-\tfrac12\log(1-x^{-2})$; $\sum_n\Lambda(n)n^{-s}=-\zeta'/\zeta(s)$ | tied to Euler product $\zeta(s)=\prod_p(1-p^{-s})^{-1}$; $\det(I-zP_\varepsilon)$ no elementary closed form | Transfer identity **verified** ([spectral-triple-verify.py](../../victor/spectral-triple-verify.py)) |
| General Dirichlet $L(s,\chi)$ ($\Psi^\chi_s=\sum_n\chi(n)n^{-s}\sin n\pi x$) | cosine/sine $\sum_n\chi(n)r^{\lvert n\rvert}e^{in\theta}$ (PD only for $\chi_0$) | $\Re s>\tfrac12$ (geom. $r<1$ on $\mathbb T$) | $\{\chi(n)n^{-2\sigma}\}$; energy $L(2\sigma,\chi_0)$ | $L^2[0,2]$, $\sigma>\tfrac12$ | $L(s+\overline{s'},\chi_1\bar\chi_2)$; transfer $=$ Gauss-sum rotation sum | kernel $\langle\Psi^{\chi_1}_s,\Psi^{\chi_2}_{s'}\rangle=L(s+\overline{s'},\chi_1\bar\chi_2)$; FE root number $\varepsilon(\chi)=\tau(\chi)/(i^a\sqrt q)$ | $\prod_{n\ge1}(1-z\chi(n)n^{-2\sigma})$; prime part $\prod_p(1-z\chi(p)p^{-2\sigma})=1/L(2\sigma,\chi)$ at $z=1$ | **Core complete** (D1–D5 + §6) |
| Collatz | (not assessed) | — | — | — | — | (not assessed) | (not assessed) | Feasibility pending |

---

## Template for a new row

When adding a new object, fill every column or write `(open)` — do not leave blank.

| Field | Content |
|---|---|
| Object | Name and defining formula |
| Kernel closed form | Explicit $K(\theta)=\sum \lambda_n e^{in\theta}$, or "none" with decay rate |
| Damping | The $r$, $t$, or $\sigma$ range where the series converges and $T_K$ is self-adjoint |
| Spectrum | $\{\lambda_n\}$ as an explicit sequence |
| Self-adjoint domain | The Hilbert space and parameter range |
| Dual | The dual object under the transfer operator, or "—" if none known |
| Explicit function | The explicit-formula / trace identity linking the spectrum to its dual (Mellin, Weil, Gauss-sum, …), or "(not assessed)" |
| Fredholm determinant | $\det(I-zT_K)=\prod_n(1-z\lambda_n)$; give the closed form ($q$-Pochhammer, $\sin$ product, Euler product, Hadamard, …) where one exists, else "no elementary closed form" |
| Status | **Complete** / **Proofs done; §N open** / **Heuristic** / **Not started** |
