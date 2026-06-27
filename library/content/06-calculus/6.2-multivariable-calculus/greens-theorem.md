---
title: Green's Theorem
tag: multivariable-calculus
summary: Relates a line integral around a closed planar curve to a double integral over the enclosed region.
links:
  - double-integrals
  - grad-div-curl
  - stokes-theorem
---

# Green's Theorem

**Green's Theorem** is the fundamental theorem of calculus for two-dimensional vector fields. It equates a **line integral** around a simple closed curve $C$ (traversed counter-clockwise) to a **double integral** over the region $D$ it encloses. This connection between boundary behaviour and interior behaviour is the first instance of a powerful pattern — continued in Stokes' Theorem and the Divergence Theorem — that pervades all of mathematical physics. Green's Theorem is used to evaluate difficult line integrals via area integrals (and vice versa), to compute areas by line integrals, and to derive conservation laws.

## Statement

Let $C$ be a positively oriented (counter-clockwise), simple closed curve and $D$ the region it encloses. If $P$ and $Q$ have continuous partial derivatives on $D$:

$$\oint_C P\,dx + Q\,dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dA$$

## Circulation and Flux Forms

**Circulation form** (as above): measures rotation of the field around $C$.

**Flux form:** if $\mathbf{F} = (P, Q)$ and $\mathbf{n}$ is the outward normal to $C$:

$$\oint_C \mathbf{F}\cdot\mathbf{n}\,ds = \iint_D \left(\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y}\right)dA = \iint_D \nabla\cdot\mathbf{F}\,dA$$

## Computing Area

$$A(D) = \oint_C x\,dy = -\oint_C y\,dx = \frac{1}{2}\oint_C (x\,dy - y\,dx)$$

## Example

Evaluate $\oint_C (y^2\,dx + x^2\,dy)$ where $C$ is the square $[0,1]^2$ traversed counter-clockwise.

$$\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 2x - 2y$$

$$\iint_D (2x-2y)\,dA = \int_0^1\!\int_0^1 (2x-2y)\,dx\,dy = 0$$

## Connection to Curl

The integrand $\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$ is the $z$-component of $\nabla \times \mathbf{F}$ for a 2D field $\mathbf{F} = (P, Q, 0)$ — so Green's Theorem is Stokes' Theorem in the plane.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\oint_C$ | line integral around a closed curve $C$ |
| $P\,dx + Q\,dy$ | the line integral element of a vector field $(P, Q)$ |
| $D$ | the region enclosed by $C$ |
| $dA$ | area element over $D$ |
| Positively oriented | counter-clockwise traversal so $D$ is on the left |
| Simple closed curve | a curve that does not cross itself and returns to its start |
| $\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$ | the scalar curl (or vorticity) in 2D |
| Flux | the rate at which a field flows across the boundary |
| Circulation | the line integral of a field tangent to the boundary |
| $\nabla \times \mathbf{F}$ | curl of $\mathbf{F}$; its $z$-component appears in Green's Theorem |
| $\nabla \cdot \mathbf{F}$ | divergence of $\mathbf{F}$; appears in the flux form |
