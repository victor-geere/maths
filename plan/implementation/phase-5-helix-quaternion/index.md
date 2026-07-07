# Phase 5 — Helix Lift and Quaternionic Time

*Status: **exploratory / conjectural**. Nothing here bears on RH. H1–H3 are proved; H4 is an open conjecture.*

Full proposal at [project/helix-quaternion-proposal.md](../../project/helix-quaternion-proposal.md).

---

## Motivation

When a kernel is indefinite (negative eigenvalues), Bochner fails and $T_K$ is not positive semidefinite on $L^2(\mathbb{T})$. The η kernel and the zeros↔primes transfer kernel both have this problem. This phase proposes lifting the circle $\mathbb{T}$ to the helix $\mathcal{H}$ (its universal cover) so that sign encodes winding, and promoting the winding axis to the quaternionic $j$-direction.

## Status

| Result | Status |
|---|---|
| H1 Helix $=$ universal cover of $\mathbb{T}$ | **Proved** |
| H2 Sign $=$ half-turn; negativity $=$ odd winding number | **Proved** |
| H3 η phase winds past $2\pi$ on the critical line | **Proved** |
| H4 $D_t = -j\partial_t$ self-adjoint in S-spectrum; cone restored | **Conjecture** |
| Sign-aware helix in `prime-zeros.py` | **Done** |
| Quaternionic Hilbert module definition | **Open** |
| S-spectrum / slice-regular self-adjointness of $D_t$ | **Open** |
| Cone-restoration claim (H4 part 3) numerical test on η | **Open** |

## Open actions

- [ ] Define the quaternionic Hilbert module: see [quaternionic-module.md](quaternionic-module.md).
- [ ] Attempt proof that $D_t = -j\partial_t$ is self-adjoint in the S-spectrum sense (H4 part 2).
- [ ] Numerical test: run `eta_kernel` helix lift in `prime-zeros.py`; check cone indicator $Z^2-(P^2+G^2) \ge 0$.
