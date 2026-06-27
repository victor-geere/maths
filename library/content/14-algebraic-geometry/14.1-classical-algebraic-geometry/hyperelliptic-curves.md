---
title: Hyperelliptic Curves
tag: algebraic-geometry
summary: Algebraic curves of genus g ≥ 2 admitting a degree-2 map to ℙ¹, given by y² = f(x) for a squarefree polynomial f of degree 2g+1 or 2g+2.
links:
  - elliptic-curves
  - riemann-roch
  - plane-curves
---

# Hyperelliptic Curves

A **hyperelliptic curve** is an algebraic curve $C$ of genus $g \geq 2$ that admits a degree-2 map $\pi : C \to \mathbb{P}^1$ — a two-to-one cover of the projective line. In affine coordinates, such curves have the form $y^2 = f(x)$ where $f$ is a squarefree polynomial of degree $2g+1$ or $2g+2$. Elliptic curves ($g=1$) are the boundary case: they are hyperelliptic in a degenerate sense (the degree-2 map is given by the $x$-coordinate). Hyperelliptic curves are the most tractable curves of higher genus: their Jacobians are principally polarised abelian varieties of dimension $g$, their arithmetic can be computed explicitly using Cantor's algorithm, and they appear in cryptography (hyperelliptic curve cryptography), number theory, and the theory of modular forms.

## Definition

A **hyperelliptic curve** of genus $g \geq 1$ over a field $k$ (char $\neq 2$) is a smooth projective curve birationally equivalent to:

$$C : y^2 = f(x), \quad f \in k[x], \quad \deg f \in \{2g+1, 2g+2\}, \quad f \text{ squarefree}$$

The **hyperelliptic involution** $\iota : (x,y) \mapsto (x,-y)$ is the deck transformation of $\pi : C \to \mathbb{P}^1$.

## Genus and Degree

| $\deg f$ | Genus $g$ |
|---|---|
| 3 or 4 | 1 (elliptic) |
| 5 or 6 | 2 |
| 7 or 8 | 3 |
| $2g+1$ or $2g+2$ | $g$ |

## Ramification

By Riemann–Hurwitz: $\pi : C \to \mathbb{P}^1$ ramifies over the roots of $f$ (and the point at $\infty$ if $\deg f$ is odd). There are $2g+2$ ramification points.

## Jacobian

The **Jacobian** $\text{Jac}(C)$ is a $g$-dimensional abelian variety — a group variety generalising the group law on elliptic curves. The Jacobian is principally polarised.

## Divisor Class Group

On $C$, every element of $\text{Jac}(C) = \text{Pic}^0(C)$ can be represented by a divisor $D - g\cdot\infty$ where $D$ is an effective divisor of degree $g$, and the algorithm for adding divisors (Cantor's algorithm) makes the group law explicit.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $y^2 = f(x)$ | affine model of a hyperelliptic curve |
| $\deg f$ | $2g+1$ or $2g+2$ for genus-$g$ hyperelliptic curve |
| Squarefree | $f$ has no repeated roots |
| $\pi : C \to \mathbb{P}^1$ | the degree-2 hyperelliptic map |
| Hyperelliptic involution $\iota$ | $(x,y) \mapsto (x,-y)$; deck transformation of $\pi$ |
| Ramification point | a point where $\pi$ is not locally two-to-one; root of $f$ |
| Riemann–Hurwitz formula | $2g-2 = 2(2\cdot(-2)) + \#\text{ramification}$ relating genus to branching |
| Jacobian $\text{Jac}(C)$ | the $g$-dimensional abelian variety attached to $C$ |
| $\text{Pic}^0(C)$ | the Picard group of degree-0 divisor classes; equals $\text{Jac}(C)$ |
| Cantor's algorithm | explicit algorithm for arithmetic in $\text{Jac}(C)$ |
| Abelian variety | a projective algebraic group (generalises elliptic curves) |
