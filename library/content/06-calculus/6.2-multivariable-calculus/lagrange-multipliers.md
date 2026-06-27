---
title: Lagrange Multipliers
tag: multivariable-calculus
summary: A method for finding extrema of a function subject to equality constraints, without eliminating variables.
links:
  - partial-derivatives
  - grad-div-curl
  - optimisation
---

# Lagrange Multipliers

**Lagrange multipliers** provide an elegant method for optimising a function $f(x, y, \ldots)$ subject to one or more equality constraints $g(x, y, \ldots) = 0$. Rather than eliminating variables (which is often messy or impossible), the method exploits a geometric insight: at a constrained extremum, the gradient of $f$ must be parallel to the gradient of $g$. This parallelism is captured by introducing a scalar multiplier $\lambda$ (the Lagrange multiplier) and solving $\nabla f = \lambda \nabla g$ together with the constraint. The method extends naturally to multiple constraints and is the foundation of duality in optimisation theory.

## Statement

To extremise $f(\mathbf{x})$ subject to $g(\mathbf{x}) = 0$, solve the system:

$$\nabla f = \lambda\, \nabla g \qquad \text{and} \qquad g(\mathbf{x}) = 0$$

The solutions are the **candidate extrema**; evaluate $f$ at each and compare.

## Geometric Insight

At a constrained extremum, moving along the constraint surface cannot increase or decrease $f$. This means $\nabla f$ has no component along the constraint, i.e. $\nabla f \perp$ the constraint surface — which means $\nabla f \parallel \nabla g$ (since $\nabla g$ is normal to $g = 0$).

## Example: Maximise Area of Rectangle with Fixed Perimeter

Maximise $f(x,y) = xy$ subject to $g(x,y) = 2x + 2y - P = 0$.

$$\nabla f = (y, x), \qquad \nabla g = (2, 2)$$

$$y = 2\lambda, \quad x = 2\lambda \implies x = y$$

From the constraint: $x = y = P/4$. Maximum area $= P^2/16$ (square).

## Multiple Constraints

For constraints $g_1 = 0$, $g_2 = 0$:

$$\nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2$$

Each constraint introduces its own multiplier.

## The Lagrangian Function

$$\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) - \lambda\, g(\mathbf{x})$$

Setting all partial derivatives of $\mathcal{L}$ to zero recovers the Lagrange conditions.

## Application to Economics

Lagrange multipliers appear in constrained utility maximisation (consumer theory) and cost minimisation. The multiplier $\lambda$ has an economic interpretation: the **shadow price** — the marginal value of relaxing the constraint by one unit.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f(\mathbf{x})$ | the objective function to be optimised |
| $g(\mathbf{x}) = 0$ | the equality constraint |
| $\lambda$ (lambda) | the Lagrange multiplier |
| $\nabla f$ | gradient of $f$ — vector of partial derivatives |
| $\nabla g$ | gradient of the constraint function |
| $\mathcal{L}$ | the Lagrangian $f - \lambda g$ |
| Candidate extremum | a solution to the Lagrange system; must be tested further |
| Shadow price | economic interpretation of $\lambda$: rate of change of optimal value w.r.t. constraint |
| Normal vector | a vector perpendicular to a surface; $\nabla g$ is normal to $g=0$ |
| Constraint surface | the set of points satisfying $g(\mathbf{x}) = 0$ |
