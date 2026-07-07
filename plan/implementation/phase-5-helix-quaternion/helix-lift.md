# Sign-Aware Helix Lift — Phase 5

*Full proposal at [project/helix-quaternion-proposal.md](../../project/helix-quaternion-proposal.md). Implementation in `victor/prime-zeros.py` (`sign_aware_helix`).*

---

## What is proved (H1–H3)

| Theorem | Statement | Status |
|---|---|---|
| H1 | $\mathcal{H} = \{(\cos t, \sin t, t)\} \subset \mathbb{C} \times \mathbb{R}_t$ is the universal cover of $\mathbb{T}$ | **Proved** |
| H2 | A negative value $-a = a e^{i\pi}$ on the circle becomes a half-turn on $\mathcal{H}$; negativity = odd winding number $\lfloor \Theta/\pi \rfloor$ | **Proved** |
| H3 | On the critical line, the η cumulative phase $\Theta_n = \pi(n-1) - b\log n$ winds without bound, crossing $2\pi, 4\pi, \dots$ | **Proved** |

## What is implemented

`sign_aware_helix(omega, R)` in `victor/prime-zeros.py`:
- Tracks sign flips of $R$ as half-turns (each flip adds $\pi$ to the cumulative winding $\phi$).
- Maps $(|R|, \phi)$ to Cartesian helix coordinates $(x, y, z) = (|R|\cos\phi,\ |R|\sin\phi,\ \phi)$.
- Blue points: $R \ge 0$; red points: $R < 0$ (wound past a $\pi$ multiple).

## Remaining work

The helix lift handles the circle indefiniteness geometrically but the *self-adjointness claim* for the lifted operator requires the quaternionic module (H4). See [quaternionic-module.md](quaternionic-module.md).
