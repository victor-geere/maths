---
title: Partial Derivatives
tag: calculus
summary: Rate of change with respect to one variable, all others held constant.
links:
  - derivative-definition
  - jacobian
  - chain-rule
---

## Key Formula

$$\frac{\partial f}{\partial x}(x,y) = \lim_{h \to 0} \frac{f(x+h,\,y) - f(x,\,y)}{h}$$

## Notes

A partial derivative applies the usual single-variable [[derivative-definition|derivative]] while treating all other variables as constants.

### Gradient

The **gradient** vector collects all partial derivatives:

$$\nabla f = \left(\frac{\partial f}{\partial x_1},\, \frac{\partial f}{\partial x_2},\, \ldots,\, \frac{\partial f}{\partial x_n}\right)$$

$\nabla f$ points in the direction of **steepest ascent**; its magnitude is the rate of increase in that direction.

### Hessian matrix

The **Hessian** $H_{ij} = \dfrac{\partial^2 f}{\partial x_i \partial x_j}$ is the analogue of the second derivative for multivariable functions.

Used to classify critical points: if $\nabla f(\mathbf{x}_0) = \mathbf{0}$, then $\mathbf{x}_0$ is:
- a **local min** if $H$ is positive definite
- a **local max** if $H$ is negative definite
- a **saddle point** if $H$ is indefinite

### Clairaut's theorem

If $\dfrac{\partial^2 f}{\partial x \partial y}$ and $\dfrac{\partial^2 f}{\partial y \partial x}$ are both continuous, then they are equal — **mixed partials commute**.

### Directional derivative

The rate of change of $f$ in the direction of unit vector $\hat{u}$:

$$D_{\hat{u}}\,f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \hat{u}$$

### Chain rule

For $f(\mathbf{x}(t))$:

$$\frac{d}{dt}f(\mathbf{x}(t)) = \nabla f \cdot \mathbf{x}'(t) = \sum_i \frac{\partial f}{\partial x_i}\frac{dx_i}{dt}$$

The full multivariable version uses the [[jacobian|Jacobian]].
