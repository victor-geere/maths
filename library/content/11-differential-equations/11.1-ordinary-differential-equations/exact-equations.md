---
title: Exact Equations
tag: ode
summary: ODEs of the form M dx + N dy = 0 where M and N are the partial derivatives of a potential function F, solved by finding F such that dF = 0.
links:
  - separable-odes
  - linear-first-order
  - partial-derivatives
---

# Exact Equations

An **exact ODE** is one that can be written as the total differential of some potential function $F(x, y)$: the equation $M\,dx + N\,dy = 0$ is exact if there exists $F$ such that $\partial F/\partial x = M$ and $\partial F/\partial y = N$. When this holds, the general solution is simply $F(x, y) = C$ — a family of level curves of $F$. The exactness condition $\partial M/\partial y = \partial N/\partial x$ (equality of mixed partials) is both necessary and sufficient. When an equation is not exact, an **integrating factor** can sometimes make it exact, connecting this technique to the linear first-order method.

## Definition

The equation $M(x,y)\,dx + N(x,y)\,dy = 0$ is **exact** if:

$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$

This is the condition that the vector field $(M, N)$ is conservative (curl-free in 2D).

## Solution Method

1. **Check exactness:** verify $M_y = N_x$.
2. **Find the potential $F$:** integrate $M$ with respect to $x$:

$$F(x,y) = \int M(x,y)\,dx + g(y)$$

3. **Determine $g(y)$:** differentiate $F$ with respect to $y$ and set equal to $N$:

$$F_y = \frac{\partial}{\partial y}\int M\,dx + g'(y) = N(x,y)$$

Solve for $g'(y)$ and integrate.

4. **Write the solution:** $F(x,y) = C$.

## Example

$(2xy + 1)\,dx + (x^2 + \cos y)\,dy = 0$.

Check: $M_y = 2x = N_x$ ✓

$F = \int(2xy+1)\,dx = x^2y + x + g(y)$

$F_y = x^2 + g'(y) = x^2 + \cos y \implies g'(y) = \cos y \implies g(y) = \sin y$

Solution: $x^2y + x + \sin y = C$.

## When Not Exact: Integrating Factor

If $M_y \neq N_x$, look for $\mu(x)$ or $\mu(y)$ such that $\mu M\,dx + \mu N\,dy = 0$ is exact:

$$\mu(x) = e^{\int \frac{M_y - N_x}{N}\,dx} \quad \text{(if this depends only on } x\text{)}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $M(x,y)\,dx + N(x,y)\,dy = 0$ | standard form of a first-order ODE |
| Exact equation | $M_y = N_x$; the vector field $(M,N)$ is conservative |
| $F(x,y)$ | potential function: $F_x = M$, $F_y = N$ |
| $\partial M/\partial y = M_y$ | partial derivative of $M$ with respect to $y$ |
| $\partial N/\partial x = N_x$ | partial derivative of $N$ with respect to $x$ |
| $g(y)$ | function of $y$ only that appears when integrating $M$ w.r.t. $x$ |
| Solution curve | $F(x,y) = C$: a level curve of the potential |
| $C$ | integration constant |
| Integrating factor $\mu$ | function making a non-exact equation exact |
| Conservative field | a vector field $(M,N)$ with $M_y = N_x$; has a potential |
