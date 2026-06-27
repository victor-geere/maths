---
title: Cohomology of Sheaves
tag: algebraic-geometry
summary: Sheaf cohomology groups H^i(X, ℱ) measure the obstruction to extending local sections globally and are the main computational tool in algebraic geometry.
links:
  - sheaves
  - schemes
  - riemann-roch
  - divisors-line-bundles
---

# Cohomology of Sheaves

**Sheaf cohomology** is the fundamental tool for computing global invariants from local data in algebraic geometry. The zeroth cohomology group $H^0(X, \mathcal{F})$ is simply the group of global sections of $\mathcal{F}$. The higher groups $H^i(X, \mathcal{F})$ for $i \geq 1$ measure the **obstruction** to patching local sections together into global ones — they vanish when the local-to-global principle holds, and their non-vanishing encodes subtle geometric information. Computed via injective resolutions or Čech cohomology, sheaf cohomology unifies singular cohomology, de Rham cohomology, and Dolbeault cohomology as special cases, and provides the cohomological framework for the Riemann–Roch theorem, the Kodaira vanishing theorem, and Serre duality.

## Definition via Derived Functors

The global sections functor $\Gamma(X, -) : \text{Sh}(X) \to \text{Ab}$ is left exact but not exact. Its **right derived functors** are:

$$H^i(X, \mathcal{F}) = R^i\Gamma(X, \mathcal{F})$$

These are computed by taking an injective resolution $0 \to \mathcal{F} \to \mathcal{I}^0 \to \mathcal{I}^1 \to \cdots$ and applying $\Gamma$:

$$H^i(X,\mathcal{F}) = H^i(0 \to \Gamma\mathcal{I}^0 \to \Gamma\mathcal{I}^1 \to \cdots)$$

## Čech Cohomology

For a nice (affine) cover $\{U_i\}$ of $X$, the **Čech cohomology** $\check{H}^i(\{U_i\}, \mathcal{F})$ agrees with sheaf cohomology and is more computable: it uses the Čech complex with cochains $c = \{c_{i_0\cdots i_p} \in \mathcal{F}(U_{i_0}\cap\cdots\cap U_{i_p})\}$.

## Key Theorems

**Serre's theorem (affine):** if $X$ is affine, then $H^i(X, \mathcal{F}) = 0$ for all $i > 0$ and quasi-coherent $\mathcal{F}$.

**Cohomology of projective space:**

$$H^i(\mathbb{P}^n, \mathcal{O}(d)) = \begin{cases} \binom{n+d}{n} & i=0, d\geq 0 \\ 0 & 0 < i < n \\ \binom{-d-1}{n} & i=n, d\leq -(n+1) \end{cases}$$

**Serre duality:** for a smooth projective $n$-fold $X$:

$$H^i(X, \mathcal{F})^\vee \cong H^{n-i}(X, \mathcal{F}^\vee \otimes \omega_X)$$

where $\omega_X = \Omega^n_X$ is the **dualising sheaf**.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $H^i(X, \mathcal{F})$ | $i$-th sheaf cohomology group |
| $H^0(X,\mathcal{F}) = \Gamma(X,\mathcal{F})$ | global sections of $\mathcal{F}$ |
| $R^i\Gamma$ | $i$-th right derived functor of global sections |
| Injective resolution | exact sequence $0 \to \mathcal{F} \to \mathcal{I}^0 \to \mathcal{I}^1 \to \cdots$ |
| Čech cohomology | cohomology computed from a cover; agrees with sheaf cohomology for nice covers |
| $\mathcal{O}(d)$ | the line bundle on $\mathbb{P}^n$ of degree $d$ (twist by $d$) |
| Quasi-coherent sheaf | generalisation of a module; well-behaved on schemes |
| Serre duality | $H^i(X,\mathcal{F}) \cong H^{n-i}(X, \mathcal{F}^\vee \otimes \omega_X)^\vee$ |
| $\omega_X = \Omega^n_X$ | dualising sheaf (canonical bundle) |
| $\mathcal{F}^\vee = \mathcal{H}om(\mathcal{F}, \mathcal{O}_X)$ | dual sheaf |
| Left exact functor | $0\to A\to B\to C$ implies $0\to FA\to FB\to FC$ but not necessarily exactness at $FC$ |
