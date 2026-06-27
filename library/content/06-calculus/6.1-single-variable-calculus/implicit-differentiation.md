---
title: Implicit Differentiation
tag: calculus
summary: Differentiating equations in which y is not isolated as an explicit function of x, treating y as a function of x and applying the chain rule.
links:
  - derivative-definition
  - chain-rule
  - related-rates
---

# Implicit Differentiation

Most differentiation is **explicit**: we have $y = f(x)$ and differentiate directly. But many important curves — circles, ellipses, the folium of Descartes — are defined by an equation $F(x, y) = 0$ where $y$ cannot be easily isolated. **Implicit differentiation** handles these cases by differentiating both sides of the equation with respect to $x$, treating $y$ as a function of $x$ and applying the chain rule whenever $y$ appears. The result is an equation involving $\frac{dy}{dx}$, which can then be solved algebraically. This technique is essential for finding tangent lines to implicit curves and underlies the derivation of the inverse function derivatives.

## Method

Given an equation $F(x, y) = 0$:

1. Differentiate both sides with respect to $x$.
2. Apply the chain rule to any term involving $y$: $\frac{d}{dx}[g(y)] = g'(y)\frac{dy}{dx}$.
3. Collect all $\frac{dy}{dx}$ terms on one side and solve.

## Example: Circle

$$x^2 + y^2 = r^2$$

Differentiate:

$$2x + 2y\frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{x}{y}$$

At the point $(3, 4)$ on the circle $x^2+y^2=25$: slope $= -3/4$.

## Example: Folium of Descartes

$$x^3 + y^3 = 3xy$$

Differentiate:

$$3x^2 + 3y^2\frac{dy}{dx} = 3y + 3x\frac{dy}{dx}$$

$$\frac{dy}{dx}(3y^2 - 3x) = 3y - 3x^2 \implies \frac{dy}{dx} = \frac{y - x^2}{y^2 - x}$$

## Inverse Function Derivatives via Implicit Differentiation

If $y = \arcsin x$, then $\sin y = x$. Differentiating:

$$\cos y \cdot \frac{dy}{dx} = 1 \implies \frac{dy}{dx} = \frac{1}{\cos y} = \frac{1}{\sqrt{1 - x^2}}$$

## Higher Derivatives

Apply the technique twice (differentiating the expression for $dy/dx$ again) to find $d^2y/dx^2$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\frac{dy}{dx}$ | derivative of $y$ with respect to $x$ |
| $F(x, y) = 0$ | implicit equation defining a curve |
| Implicit function | $y$ defined by an equation relating it to $x$, not solved explicitly |
| Explicit function | $y$ expressed directly as $y = f(x)$ |
| Chain rule | $\frac{d}{dx}[g(y)] = g'(y)\frac{dy}{dx}$ when $y$ depends on $x$ |
| Tangent line | the line touching a curve at a point with the slope $dy/dx$ |
| $d^2y/dx^2$ | second derivative — rate of change of the slope |
| $\arcsin x$ | inverse sine function |
| Folium of Descartes | the curve $x^3 + y^3 = 3xy$ |
| $r$ | radius of a circle |
