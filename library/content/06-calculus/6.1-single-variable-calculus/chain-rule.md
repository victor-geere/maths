---
title: Chain Rule
tag: calculus
summary: Derivative of f(g(x)) is f′(g(x)) · g′(x).
links:
  - derivative-definition
  - jacobian
  - partial-derivatives
---

## Key Formula

$$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$

## Notes

The chain rule differentiates **composed functions**: $h = f \circ g$.

### Leibniz form

If $y = f(u)$ and $u = g(x)$:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

This notation makes the rule look like "cancelling" $du$ — a useful mnemonic, though not literally true.

### Iterated chain rule

For $f \circ g \circ h$:

$$\frac{d}{dx}[f(g(h(x)))] = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x)$$

### Common patterns

| $h(x)$ | $h'(x)$ |
|---|---|
| $\sin(x^2)$ | $2x\cos(x^2)$ |
| $e^{3x}$ | $3e^{3x}$ |
| $\ln(x^2+1)$ | $\frac{2x}{x^2+1}$ |
| $(x^3-1)^5$ | $15x^2(x^3-1)^4$ |

### Higher dimensions

For $f: \mathbb{R}^n \to \mathbb{R}^m$ and $g: \mathbb{R}^k \to \mathbb{R}^n$, the derivative of $f \circ g$ at $x$ is the [[jacobian|Jacobian]] matrix product:

$$D(f \circ g)(x) = Df(g(x)) \cdot Dg(x)$$
