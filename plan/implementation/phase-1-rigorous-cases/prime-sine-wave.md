# Prime Sine Wave — Phase 1a

*Status: **complete**. Full note at [project/prime-sine-wave.md](../../project/prime-sine-wave.md).*

---

## Summary

$\Psi_s = \sum_p p^{-s} \sin(p\pi x)$ in $L^2[0,2]$.

| Theorem | Statement | Status |
|---|---|---|
| T1 | Domain: $\sigma > \tfrac{1}{2}$ | **Proved** |
| T2 | Energy $= P(2\sigma)$ | **Proved** |
| T3 | Reproducing kernel $= P(s+\overline{s'})$ | **Proved** |
| T4 | Boundary blow-up at $\sigma=\tfrac{1}{2}$ (Mertens rate) | **Proved** |

§6 numerical verification: $\|\Psi_2\|^2 = P(4)$ to 10 digits — **done**.

## Scope

This note proves four unconditional theorems. It explicitly does **not** imply anything about RH (see §7 of the full note): the critical line $\sigma=\tfrac{1}{2}$ appears as the abscissa of convergence of the prime zeta function $P(s)$, not from any zero condition.
