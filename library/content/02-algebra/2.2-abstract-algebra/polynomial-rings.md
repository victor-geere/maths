---
title: Polynomial Rings
tag: abstract-algebra
summary: Rings formed by polynomials with coefficients in another ring.
links:
  - ring-axioms
  - ideals
  - field-axioms
---

## Definition

For a commutative ring $R$, the **polynomial ring** $R[x]$ consists of all formal polynomials:

$$f = a_n x^n + \cdots + a_1 x + a_0, \quad a_i \in R$$

with pointwise addition and standard polynomial multiplication.

## Key Properties

- $R[x]$ is commutative iff $R$ is commutative.
- If $R$ is an integral domain, so is $R[x]$.
- $\deg(fg) = \deg f + \deg g$ when $R$ is an integral domain.

## Division Algorithm in $F[x]$

When $F$ is a field, $F[x]$ is a **Euclidean domain**: for $f, g \in F[x]$ with $g \neq 0$:

$$f = gq + r, \quad \deg r < \deg g$$

## Irreducibility

$p(x) \in F[x]$ is **irreducible** if it has no proper factorisation. Analogous to prime numbers.

- In $\mathbb{R}[x]$: irreducibles are linear factors and quadratics with negative discriminant.
- In $\mathbb{C}[x]$: every non-constant polynomial splits into linear factors.

## Quotient Construction

$F[x]/(p(x))$ is a **field** iff $p(x)$ is irreducible over $F$.

**Example:** $\mathbb{R}[x]/(x^2+1) \cong \mathbb{C}$.

## Notes

- $\mathbb{Z}[x]$ and $F[x]$ are UFDs (unique factorisation domains).
- Polynomial rings in multiple variables: $R[x_1, \ldots, x_n]$.
