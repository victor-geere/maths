# Ornstein–Uhlenbeck Process — Phase 1c

*Full note at [project/ou-process.md](../../project/ou-process.md).*

---

## Status

| Theorem | Statement | Status |
|---|---|---|
| O1 | Spectrum $-\mathbb{N}$, Hermite eigenbasis | **Proved** |
| O2 | Number operator $-L = a^\dagger a$ | **Proved** |
| O3 | Semigroup $=$ geometric damping $r^n$; Mehler kernel | **Proved** |
| O4 | Heat trace $= 1/(e^t-1)$; Bernoulli expansion | **Proved** |
| O5 | Spectral zeta $= \zeta$; $\Gamma(s)\zeta(s) = \int t^{s-1}\Theta\,dt$ | **Proved** |
| O6 | Intertwiner $J\colon L^2(\gamma)\to L^2(\mathbb{T})$, $JP_t=D_rJ$ (Phase 4 gate) | **Proved** |
| §7 numerics | Mehler vs. Hermite sum, trace, heat, Mellin $\Gamma\zeta$ | **Done** |
| $L^2(\gamma) \to L^2(\mathbb{T})$ functor | Bounded intertwining map (Phase 4 prerequisite) | **Done** (Lemma O6) |

## Completed

- [x] `ou_mehler(t, x, y)` + `ou_hermite_sum` in [prime-zeros.py](../../victor/prime-zeros.py); five checks in [ou-verify.py](../../victor/ou-verify.py) (`mpmath`, 40 dps), all pass — see §7 table. Worst discrepancies: Mehler↔Hermite $9\times10^{-12}$, trace $5\times10^{-41}$, Bernoulli exact, Mellin $\Gamma\zeta$ $1\times10^{-22}$, intertwiner $5\times10^{-15}$.
- [x] Formalised the correspondence $\mathrm{diag}(r^{|n|})$ on $\mathbb{T}$ ↔ $P_t|_{|n|}$ on $L^2(\gamma)$ as **Lemma O6** (§4.1 of the full note): the isometry $J\colon h_n\mapsto c_n$ onto $L^2(\mathbb{T})^{\mathrm{even}}$ intertwines $P_t$ with Poisson convolution $D_r$. **Phase 4 gate discharged.**
