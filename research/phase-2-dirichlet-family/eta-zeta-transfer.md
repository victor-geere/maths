# η ↔ ζ Transfer Operator — Phase 2a

*Full note at [project/eta-zeta-transfer.md](../../project/eta-zeta-transfer.md).*

---

## Status

| Theorem | Statement | Status |
|---|---|---|
| E1 | Domain: $\eta(s)$ converges for $\Re s > 0$ | **Proved** |
| E2 | Multiplier: $\eta = (1-2^{1-s})\zeta$ | **Proved** |
| E3 | Transfer $=$ rotation by $\pi$: $K^\eta_r(\theta) = -K^\zeta_r(\theta+\pi)$ | **Proved** |
| E4 | Shared critical-strip zeros | **Proved** |
| Measure-level explicit-formula equality | Extra mass at $\{k\log 2\}$, coefficients $1/k$ | **Open** |
| §5 numerics | Rotation identity, extra zeros, transfer correction | **Open** |

## Open actions

- [ ] Implement `eta_kernel(r, theta)` in toolkit; verify E3 on a $\theta$-grid; check extra zeros and Dirichlet coefficients of the transfer correction. Fill §5 table.
- [ ] Prove (or cite) the measure-level statement: the measure $\mu^\eta - \mu^\zeta$ has point masses of weight $1/k$ at $\theta = k\log 2 \pmod{2\pi}$.
