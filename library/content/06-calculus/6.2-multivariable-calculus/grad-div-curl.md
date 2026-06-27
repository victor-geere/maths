---
title: Gradient, Divergence, Curl
tag: multivariable-calculus
summary: The three fundamental differential operators on scalar and vector fields in two and three dimensions.
links:
  - partial-derivatives
  - jacobian
  - greens-theorem
  - stokes-theorem
  - divergence-theorem
---

# Gradient, Divergence, Curl

The **gradient**, **divergence**, and **curl** are the three fundamental first-order differential operators acting on fields in $\mathbb{R}^2$ and $\mathbb{R}^3$. The **gradient** turns a scalar field into a vector field pointing in the direction of steepest increase. The **divergence** measures how much a vector field spreads out from a point (sources and sinks). The **curl** measures the rotation or swirling of a vector field around a point. Together with the **Laplacian** $\nabla^2 = \nabla \cdot \nabla$, they form the language of classical physics: electromagnetism (Maxwell's equations), fluid dynamics (Navier–Stokes), and heat flow are all written in these operators.

## The Del Operator

In $\mathbb{R}^3$:

$$\nabla = \frac{\partial}{\partial x}\mathbf{i} + \frac{\partial}{\partial y}\mathbf{j} + \frac{\partial}{\partial z}\mathbf{k}$$

## Gradient (of a Scalar Field $f$)

$$\nabla f = \left(\frac{\partial f}{\partial x},\, \frac{\partial f}{\partial y},\, \frac{\partial f}{\partial z}\right)$$

- Points in the direction of **steepest ascent** of $f$.
- $|\nabla f|$ is the rate of steepest increase.
- $\nabla f \perp$ the level surfaces of $f$.

## Divergence (of a Vector Field $\mathbf{F} = (P, Q, R)$)

$$\nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

- A **scalar** field.
- Positive divergence: net outflow (source); negative: net inflow (sink).
- $\nabla \cdot \mathbf{F} = 0$: the field is **incompressible** (solenoidal).

## Curl (of a Vector Field $\mathbf{F} = (P, Q, R)$)

$$\nabla \times \mathbf{F} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\\partial_x&\partial_y&\partial_z\\P&Q&R\end{vmatrix} = \left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z},\;\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x},\;\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)$$

- A **vector** field.
- $\nabla \times \mathbf{F} = \mathbf{0}$: the field is **irrotational** (conservative).

## Laplacian

$$\nabla^2 f = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$

Appears in the heat equation, wave equation, and Laplace's equation ($\nabla^2 f = 0$).

## Key Identities

$$\nabla \times (\nabla f) = \mathbf{0} \quad \text{(curl of gradient is zero)}$$
$$\nabla \cdot (\nabla \times \mathbf{F}) = 0 \quad \text{(divergence of curl is zero)}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\nabla$ (nabla/del) | the vector differential operator $(\partial_x, \partial_y, \partial_z)$ |
| $\nabla f$ | gradient of scalar field $f$: vector of partial derivatives |
| $\nabla \cdot \mathbf{F}$ | divergence of vector field $\mathbf{F}$: scalar measure of outflow |
| $\nabla \times \mathbf{F}$ | curl of vector field $\mathbf{F}$: vector measure of rotation |
| $\nabla^2 f$ | Laplacian of $f$: sum of second partial derivatives |
| $\mathbf{i}, \mathbf{j}, \mathbf{k}$ | unit vectors in the $x$, $y$, $z$ directions |
| Scalar field | a function assigning a number to each point in space |
| Vector field | a function assigning a vector to each point in space |
| Solenoidal | divergence-free field; $\nabla \cdot \mathbf{F} = 0$ |
| Irrotational | curl-free field; $\nabla \times \mathbf{F} = \mathbf{0}$; implies conservative |
| Conservative field | has a potential function $\phi$ with $\mathbf{F} = \nabla \phi$ |
| Level surface | the set of points where $f(x,y,z) = c$ (constant) |
