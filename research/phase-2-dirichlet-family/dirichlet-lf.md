# General Dirichlet Series and $L$-functions — Phase 2c

*Status: **not started**. This is a stub. When work begins, create `project/dirichlet-series.md` following the template of `project/prime-sine-wave.md`.*

---

## Scope

Extend the spectral recipe uniformly to:

- General Dirichlet series $\sum a_n n^{-s}$ with $a_n \ge 0$ and polynomial growth.
- Dirichlet $L$-functions $L(s,\chi) = \sum_{n=1}^\infty \chi(n) n^{-s}$ for a primitive character $\chi$.
- (Stretch) Higher $L$-functions (automorphic forms, Artin $L$-functions).

## Key questions to settle

1. **Kernel.** For $L(s,\chi)$, does the damped symmetrised sequence $\{|\chi(n)| r^n\}$ give a positive definite kernel? (It will if $|\chi(n)| \ge 0$; the sign issues arise only when $\chi(n)$ is complex.)

2. **Functional equation ↔ kernel symmetry.** The functional equation $L(s,\chi) \leftrightarrow L(1-s,\bar\chi)$ should translate into a symmetry of the kernel under $r \to r^{-1}$ or $\theta \to -\theta$. Make this precise.

3. **Transfer operator.** Is there a clean bounded multiplier $M_\chi: T^{\mathbf{1}}_r \to T^\chi_r$ analogous to the $\eta \leftrightarrow \zeta$ rotation-by-$\pi$? What is its kernel in terms of Gauss sums?

4. **Explicit formula.** State the Dirichlet $L$-function analogue of the Weil explicit formula and identify the archimedean ($\Gamma$) correction.

## Deliverable outline (once started)

```
§0  Summary table (one row per L-function)
§1  Setup: Dirichlet characters, L(s,chi) as a Dirichlet series
§2  Kernel construction and positive definiteness
§3  Functional equation as kernel symmetry
§4  Transfer operator and Gauss-sum multiplier
§5  Explicit formula
§6  Numerical verification
§7  Scope and honest limits
```

## Prerequisites

- Phases 1b, 1c numerics complete.
- η↔ζ measure-level equality settled (Phase 2a).
