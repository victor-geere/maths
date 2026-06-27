---
title: Divisors & Line Bundles
tag: algebraic-geometry
summary: Divisors are formal sums of codimension-1 subvarieties; line bundles (invertible sheaves) are their geometric counterpart, classified by the Picard group.
links:
  - sheaves
  - riemann-roch
  - schemes
  - sheaf-cohomology
---

# Divisors & Line Bundles

**Divisors** are the algebraic geometry analogue of codimension-1 submanifolds: formal integer linear combinations of irreducible codimension-1 subvarieties of a scheme. They encode zeros and poles of rational functions and parametrise sections of **line bundles** — rank-1 locally free sheaves that can be thought of as "twisted trivial bundles." The correspondence between divisors and line bundles (via the exponential/Picard group sequence) is one of the central tools of algebraic geometry. The **Picard group** $\text{Pic}(X)$ classifies line bundles up to isomorphism and captures global geometric information: for a smooth projective curve, $\text{Pic}^0(X)$ is the Jacobian variety. The Riemann–Roch theorem is naturally formulated in terms of divisors and their associated line bundles.

## Weil Divisors

A **Weil divisor** on a normal variety $X$ is a formal sum:

$$D = \sum_Z n_Z [Z]$$

where the sum is over irreducible codimension-1 subvarieties $Z \subseteq X$ and $n_Z \in \mathbb{Z}$ with only finitely many nonzero.

**Effective divisor:** $n_Z \geq 0$ for all $Z$ (written $D \geq 0$).

## Principal Divisors

For a rational function $f \in k(X)^*$:

$$\text{div}(f) = \sum_Z v_Z(f)[Z]$$

where $v_Z(f)$ is the **order of vanishing** of $f$ along $Z$ (negative for poles).

**Linear equivalence:** $D \sim D'$ if $D - D' = \text{div}(f)$ for some $f$.

The **class group** is $\text{Cl}(X) = \text{Div}(X) / \text{PDiv}(X)$.

## Cartier Divisors and Line Bundles

On a smooth variety, **Cartier divisors** (locally defined by a single equation) correspond to **line bundles** (invertible sheaves $\mathcal{L}$ with $\mathcal{L} \otimes \mathcal{L}^{-1} \cong \mathcal{O}_X$).

For a Cartier divisor $D$: the associated line bundle is $\mathcal{O}(D)$ with sections $H^0(X, \mathcal{O}(D)) = \{f \in k(X) : \text{div}(f) + D \geq 0\}$.

## Picard Group

$$\text{Pic}(X) = \{\text{line bundles on } X\} / \text{isomorphism}$$

with group operation given by tensor product. For smooth $X$: $\text{Pic}(X) \cong \text{Cl}(X)$.

## Ample and Very Ample Line Bundles

- **Very ample $\mathcal{L}$:** gives an embedding $X \hookrightarrow \mathbb{P}^N$ via sections of $\mathcal{L}$
- **Ample $\mathcal{L}$:** some tensor power $\mathcal{L}^{\otimes n}$ is very ample

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $D = \sum n_Z[Z]$ | Weil divisor: formal sum of codimension-1 subvarieties |
| $D \geq 0$ | effective divisor: all $n_Z \geq 0$ |
| $v_Z(f)$ | order of vanishing of $f$ along $Z$ |
| $\text{div}(f)$ | principal divisor of rational function $f$ |
| $D \sim D'$ | linear equivalence: $D - D' = \text{div}(f)$ |
| $\text{Cl}(X)$ | divisor class group |
| Cartier divisor | locally principal divisor; corresponds to a line bundle |
| Line bundle $\mathcal{L}$ | rank-1 locally free $\mathcal{O}_X$-module (invertible sheaf) |
| $\mathcal{O}(D)$ | line bundle associated to Cartier divisor $D$ |
| $\text{Pic}(X)$ | Picard group: isomorphism classes of line bundles |
| Very ample | induces an embedding $X \hookrightarrow \mathbb{P}^N$ |
| Ample | a power is very ample; generates positivity in algebraic geometry |
