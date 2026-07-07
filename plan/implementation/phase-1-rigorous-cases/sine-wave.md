# Natural / Zeta Sine Wave — Phase 1d

*Status: **complete**. Full note at [project/sine-wave.md](../../project/sine-wave.md).*

---

## Summary

$\Psi_s = \sum_{n\ge1} n^{-s} \sin(n\pi x)$ in $L^2[0,2]$ — the prime sine wave
([Phase 1a](prime-sine-wave.md)) with $\mathbb P\to\mathbb N$ and prime zeta
$P\to$ Riemann zeta $\zeta$.

| Theorem | Statement | Status |
|---|---|---|
| T1 | Domain: $\sigma > \tfrac{1}{2}$ | **Proved** |
| T2 | Energy $= \zeta(2\sigma)$ | **Proved** |
| T3 | Reproducing kernel $= \zeta(s+\overline{s'})$ | **Proved** |
| T4 | Boundary blow-up at $\sigma=\tfrac12$: simple pole $\frac1{2\sigma-1}+\gamma$; harmonic line rate $\log N$ | **Proved** |
| T5 | Closed form $\mathrm{Im}\,\mathrm{Li}_s(e^{i\pi x})$ (Clausen); $\Psi_1(x)=\tfrac{\pi(1-x)}2$ | **Proved** |

§7 numerical verification ([`victor/sine-wave-verify.py`](../../victor/sine-wave-verify.py)):
$\|\Psi_2\|^2=\zeta(4)=\pi^4/90$ to 10 digits, $\langle\Psi_2,\Psi_3\rangle=\zeta(5)$,
$\zeta(2\sigma)-\frac1{2\sigma-1}\to\gamma$, and the Clausen closed form — all pass.

## What is new versus the prime case

- **Closed form (T5).** The all-$\mathbb N$ sum is the imaginary part of a
  polylogarithm on the unit circle (a Clausen function); the prime case has none.
- **Fundamental mode present.** $\langle\Psi_s,\sin\pi x\rangle = 1$ (vs. $0$ for
  primes, since $1\notin\mathbb P$).
- **Stronger boundary.** Simple pole (rate $1/(2\sigma-1)$) and harmonic line rate
  $\log N$, vs. the prime case's logarithmic singularity and Mertens' $\log\log N$.

## Scope

Five unconditional theorems. As in Phase 1a, the note explicitly does **not** bear
on RH (§8): the critical line $\sigma=\tfrac12$ is forced by the **pole** of $\zeta$
at $z=1$, while the nontrivial zeros lie at $0<\sigma<\tfrac12$ — strictly inside
the region where $\Psi_s\notin H$, and never reached by the construction.
