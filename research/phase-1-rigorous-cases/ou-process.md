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
| §7 numerics | Mehler vs. Hermite sum, trace, heat, Mellin $\Gamma\zeta$ | **Open** |
| $L^2(\gamma) \to L^2(\mathbb{T})$ functor | Bounded intertwining map (Phase 4 prerequisite) | **Open** |

## Open actions

- [ ] Implement `ou_mehler(t, x, y)` in toolkit (requires `mpmath`); run four checks and fill §7.
- [ ] Formalise the index-level correspondence $\mathrm{diag}(r^{|n|})$ on $\mathbb{T}$ ↔ $P_t|_{|n|}$ on $L^2(\gamma)$ as a bounded intertwining map; write it up as a lemma before Phase 4 begins.
