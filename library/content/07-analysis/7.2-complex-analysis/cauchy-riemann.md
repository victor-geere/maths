---
title: Cauchy–Riemann Equations
tag: complex-analysis
summary: The pair of partial differential equations that are necessary and sufficient for a function to be holomorphic.
links:
  - holomorphic-functions
  - partial-derivatives
  - cauchys-integral-theorem
---

# Cauchy–Riemann Equations

The **Cauchy–Riemann equations** are the essential test for holomorphicity. Writing a complex function $f(z) = u(x,y) + iv(x,y)$ in terms of its real part $u$ and imaginary part $v$ (where $z = x + iy$), the equations state that the partial derivatives of $u$ and $v$ must satisfy a precise coupling. Geometrically, this coupling means that $f$ preserves angles and infinitesimally scales areas uniformly — it is a **conformal mapping**. The equations were studied by Euler, d'Alembert, Cauchy, and Riemann, and they form the bridge between real multivariable calculus and the elegant world of complex analysis.

## The Equations

If $f = u + iv$ is holomorphic, then at every point:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \qquad \text{and} \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

**Compact form using complex partial derivatives:**

$$\frac{\partial f}{\partial \bar{z}} = 0, \quad \text{where } \frac{\partial}{\partial \bar{z}} = \frac{1}{2}\!\left(\frac{\partial}{\partial x} + i\frac{\partial}{\partial y}\right)$$

## Sufficiency

If $u$ and $v$ have continuous first partial derivatives on an open set $U$ and satisfy the C–R equations, then $f = u + iv$ is holomorphic on $U$.

## The Complex Derivative in Terms of Real Parts

$$f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x} = \frac{\partial v}{\partial y} - i\frac{\partial u}{\partial y}$$

## Harmonic Functions

If $f = u + iv$ is holomorphic, both $u$ and $v$ are **harmonic** (satisfy Laplace's equation):

$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0 \qquad \nabla^2 v = 0$$

Moreover, $v$ is the **harmonic conjugate** of $u$: given $u$ harmonic, $v$ can be recovered (up to a constant) from the C–R equations.

## Example

$f(z) = z^2 = (x^2 - y^2) + i(2xy)$. So $u = x^2 - y^2$ and $v = 2xy$:

$$\frac{\partial u}{\partial x} = 2x = \frac{\partial v}{\partial y} \checkmark \qquad \frac{\partial u}{\partial y} = -2y = -\frac{\partial v}{\partial x} \checkmark$$

Holomorphic, as expected.

$f(z) = \bar{z} = x - iy$: $u = x$, $v = -y$. Then $\partial u/\partial x = 1$ but $\partial v/\partial y = -1$. Fails — not holomorphic.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f(z) = u + iv$ | decomposition into real part $u$ and imaginary part $v$ |
| $z = x + iy$ | complex variable with real part $x$ and imaginary part $y$ |
| $\partial u/\partial x$ | partial derivative of $u$ with respect to $x$ |
| C–R equations | Cauchy–Riemann: $u_x = v_y$, $u_y = -v_x$ |
| $\partial/\partial\bar{z}$ | Cauchy–Riemann operator; zero iff $f$ is holomorphic |
| $\bar{z}$ | complex conjugate $x - iy$ |
| Harmonic function | satisfies Laplace's equation $\nabla^2 u = 0$ |
| $\nabla^2$ | Laplacian $= \partial^2/\partial x^2 + \partial^2/\partial y^2$ |
| Harmonic conjugate | the imaginary part $v$ of a holomorphic function, given its real part $u$ |
| Conformal mapping | angle-preserving complex function; holomorphic functions with $f'\neq 0$ are conformal |
