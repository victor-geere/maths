# Spectral Data Sheet

*One row per catalogue object. Fill in as each object's note is verified numerically.*

Columns: **object** | **kernel closed form** | **damping range** | **spectrum** $\{\lambda_n\}$ | **self-adjoint domain** | **dual object** | **status**

---

| Object | Kernel closed form | Damping | Spectrum | S.a. domain | Dual | Status |
|---|---|---|---|---|---|---|
| Prime sine wave $\sum_p p^{-s}\sin(p\pi x)$ | none (no closed form) | $\Re s > \tfrac{1}{2}$ | $\{p^{-2\sigma}\}$ | $L^2[0,2]$, $\sigma > \tfrac{1}{2}$ | — | **Complete** (T1–T4 + §6) |
| Fibonacci $F_n$ | $2\,\Re\dfrac{re^{i\theta}}{1-re^{i\theta}-r^2e^{2i\theta}}$ | $r < 1/\varphi$ | $\{F_n r^n\}$ | $L^2(\mathbb{T})$, any $r < 1/\varphi$ | Lucas (open) | Proofs done; §6 open |
| OU / integers $\mathbb{N}$ | Mehler: $\dfrac{1}{\sqrt{1-r^2}}e^{(2rxy-r^2(x^2+y^2))/2(1-r^2)}$ | $r = e^{-t} < 1$ | $\{e^{-nt}\}$ | $L^2(\gamma)$, any $t > 0$ | Spectral zeta $= \zeta$ | Proofs done; §7 open |
| Dirichlet eta (alternating) | $-K^\zeta_r(\theta+\pi)$ | $r < 1$ | alternating signs | $L^2(\mathbb{T})$ | $\zeta$ via rotation by $\pi$ | E1–E4 proved; §5 open |
| Zeta magnitude $n^{-1/2}$ | $2\,\Re\,\mathrm{Li}_{1/2}(re^{i\theta})$ | $r < 1$ | $\{n^{-1/2}r^n\}$ | $L^2(\mathbb{T})$ | Zeros via Weil | Heuristic |
| Riemann zeros $\gamma_n$ | $2\sum_n \gamma_n r^n \cos n\theta$ | $r < 1$ | $\{\gamma_n r^n\}$ | $L^2(\mathbb{T})$ | Prime powers via Weil | Heuristic (Thm 6.1 conditional) |
| Prime powers $\Lambda(n)/\sqrt{n}$ | none (no closed form) | Gaussian | von Mangoldt weights | — | Zeros via Weil | Heuristic |
| General Dirichlet $L(s,\chi)$ | (not assessed) | — | — | — | — | Not started |
| Collatz | (not assessed) | — | — | — | — | Feasibility pending |

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
| Status | **Complete** / **Proofs done; §N open** / **Heuristic** / **Not started** |
