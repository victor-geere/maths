---
title: Genus & Riemann–Roch Theorem
tag: algebraic-geometry
summary: The genus classifies smooth projective curves; the Riemann–Roch theorem computes the dimension of spaces of meromorphic functions with prescribed poles.
links:
  - plane-curves
  - elliptic-curves
  - divisors-line-bundles
  - euler-characteristic
---

# Genus & Riemann–Roch Theorem

The **genus** $g$ is the most important topological invariant of a smooth projective curve: it counts the number of "holes" when the curve is viewed as a compact Riemann surface — a torus has $g=1$, a sphere $g=0$, a surface with two handles $g=2$. The **Riemann–Roch theorem** is the central tool for computing dimensions of spaces of functions and differential forms with prescribed singularities on a curve of genus $g$. It gives an exact formula:

$$\ell(D) - \ell(K-D) = \deg D + 1 - g$$

relating a **divisor** $D$ (a formal sum of points) to the spaces of meromorphic functions with poles only at specified points. This theorem controls what functions can live on a curve and has applications ranging from the classification of algebraic curves to the theory of algebraic codes (Goppa codes).

## Genus

The **geometric genus** of a smooth projective curve $C$ over $\mathbb{C}$:

- Topologically: the number of handles on the corresponding Riemann surface
- Algebraically: $g = \dim H^0(C, \Omega^1_C) = \dim H^1(C, \mathcal{O}_C)$

**Formula for plane curves:** for a smooth curve of degree $d$ in $\mathbb{P}^2$:

$$g = \frac{(d-1)(d-2)}{2}$$

## Divisors

A **divisor** on a smooth curve $C$ is a formal integer linear combination of points:

$$D = \sum_{P \in C} n_P [P], \quad n_P \in \mathbb{Z}, \text{ finitely many nonzero}$$

**Degree:** $\deg D = \sum n_P$.

**Effective divisor:** $n_P \geq 0$ for all $P$ (written $D \geq 0$).

## Riemann–Roch Theorem

For a smooth projective curve $C$ of genus $g$ and a divisor $D$:

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

where:
- $\ell(D) = \dim H^0(C, \mathcal{O}(D))$: dimension of the space of meromorphic functions with poles $\leq D$
- $K_C$: the **canonical divisor** (divisor of a non-zero meromorphic 1-form)
- $\deg K_C = 2g - 2$

## Consequences

- If $\deg D > 2g-2$: $\ell(K-D) = 0$, so $\ell(D) = \deg D + 1 - g$
- **Riemann's inequality:** $\ell(D) \geq \deg D + 1 - g$
- For $D = 0$: $\ell(0) = 1$, $\ell(K) = g$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $g$ | genus of the curve |
| $D = \sum n_P[P]$ | divisor on $C$: formal sum of points with integer multiplicities |
| $\deg D = \sum n_P$ | degree of divisor $D$ |
| $D \geq 0$ | effective divisor: all $n_P \geq 0$ |
| $\ell(D) = h^0(\mathcal{O}(D))$ | dimension of space of meromorphic functions with poles at most $D$ |
| $K_C$ | canonical divisor: divisor of a meromorphic 1-form |
| $\deg K_C = 2g-2$ | degree of the canonical divisor |
| $H^0(C, \mathcal{O}(D))$ | global sections of the line bundle $\mathcal{O}(D)$ |
| $H^1(C, \mathcal{O}_C)$ | first cohomology of the structure sheaf; dimension equals $g$ |
| $\Omega^1_C$ | sheaf of regular 1-forms (holomorphic differentials) |
| Riemann–Roch | $\ell(D) - \ell(K-D) = \deg D + 1 - g$ |
