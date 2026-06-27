---
title: Euler's Formula
tag: analysis
summary: e^{iθ} = cos θ + i sin θ — connecting exponentials to trigonometry.
links:
  - complex-numbers
  - taylor-series
---

## Key Formula

$$e^{i\theta} = \cos\theta + i\sin\theta$$

## Notes

Euler's formula is one of the most celebrated results in mathematics, connecting five fundamental constants in **Euler's identity**:

$$e^{i\pi} + 1 = 0$$

### Derivation via Taylor series

Substitute $x = i\theta$ into the [[taylor-series|Maclaurin series]] for $e^x$:

$$e^{i\theta} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \cdots$$

Using $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, $\ldots$ and separating real/imaginary parts:

$$= \underbrace{\left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots\right)}_{\cos\theta} + i\underbrace{\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots\right)}_{\sin\theta}$$

### Applications

**Trig identities** — $e^{i(\alpha+\beta)} = e^{i\alpha}e^{i\beta}$ immediately gives the angle addition formulas:

$$\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$$

**Rotation in $\mathbb{C}$** — multiplying a [[complex-numbers|complex number]] $z$ by $e^{i\theta}$ rotates it by angle $\theta$ in the plane.

**Fourier analysis** — the functions $e^{in\theta}$ form an orthonormal basis for $L^2([0,2\pi])$.

**Solving ODEs** — complex exponentials replace sines and cosines, simplifying calculations for linear differential equations with constant coefficients.
