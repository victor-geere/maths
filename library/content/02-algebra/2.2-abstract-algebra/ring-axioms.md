---
title: Ring Axioms
tag: abstract-algebra
summary: Algebraic structures with two operations generalising integers.
links:
  - group-axioms
  - ideals
  - field-axioms
---

## Definition

A **ring** $(R, +, \cdot)$ satisfies:

1. $(R, +)$ is an **abelian group** (with identity $0$)
2. Multiplication is **associative**: $(ab)c = a(bc)$
3. **Distributivity** (both sides): $a(b+c) = ab + ac$ and $(a+b)c = ac + bc$

A ring with a **multiplicative identity** $1$ is called a **unital ring** (or ring with unity).

A **commutative ring** has $ab = ba$ for all $a, b$.

## Examples

| Ring | Commutative? | Unity? |
|---|---|---|
| $\mathbb{Z}$ | yes | yes ($1$) |
| $\mathbb{Z}/n\mathbb{Z}$ | yes | yes |
| $\mathbb{R}[x]$ | yes | yes |
| $M_n(\mathbb{R})$ | no (n≥2) | yes ($I_n$) |
| $2\mathbb{Z}$ | yes | no |

## Special Elements

- **Unit:** $a$ with a multiplicative inverse $a^{-1} \in R$.
- **Zero divisor:** $a \neq 0$ with $ab = 0$ for some $b \neq 0$.
- **Nilpotent:** $a^n = 0$ for some $n \geq 1$.

## Integral Domain

A commutative unital ring with **no zero divisors**. Examples: $\mathbb{Z}$, $\mathbb{R}[x]$, any field.

## Notes

- Every field is an integral domain, but not conversely ($\mathbb{Z}$ is an integral domain but not a field).
- The study of ideals and quotient rings mirrors the group-theoretic story.
