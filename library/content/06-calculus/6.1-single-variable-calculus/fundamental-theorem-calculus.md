---
title: Fundamental Theorem of Calculus
tag: calculus
summary: Differentiation and integration are inverse operations.
links:
  - derivative-definition
  - riemann-integral
  - limits
---

## Key Formula

$$\int_a^b f(x)\,dx = F(b) - F(a) \qquad \text{where } F' = f$$

## Notes

The FTC is the central result of calculus — it unifies the two apparently separate operations of differentiation and integration.

### Part 1 — differentiation of an integral

Define the accumulation function:

$$F(x) = \int_a^x f(t)\,dt$$

If $f$ is continuous on $[a,b]$, then $F$ is differentiable and $F'(x) = f(x)$.

In other words, **integration followed by differentiation returns the original function**.

### Part 2 — evaluating definite integrals

If $F$ is any antiderivative of $f$ (i.e. $F' = f$) on $[a,b]$, then:

$$\int_a^b f(x)\,dx = F(b) - F(a) = \Big[F(x)\Big]_a^b$$

This converts the [[riemann-integral|Riemann limit]] process into a purely algebraic calculation.

### Intuition

The net area under a **rate-of-change** curve equals the **total change** in the quantity — the same reason that integrating velocity gives displacement.

### Corollary — substitution rule

If $u = g(x)$ and $f, g$ satisfy suitable conditions:

$$\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$$

This is the integral counterpart of the [[derivative-definition|chain rule]].
