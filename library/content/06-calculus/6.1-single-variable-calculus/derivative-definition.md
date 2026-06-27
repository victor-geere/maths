---
title: Derivative
tag: calculus
summary: Instantaneous rate of change as a limit of difference quotients.
links:
  - limits
  - chain-rule
  - fundamental-theorem-calculus
  - partial-derivatives
---

## Key Formula

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

## Notes

The derivative measures the **instantaneous slope** of $f$ at $x$ — the limit of secant-line slopes as the second point approaches $x$.

### Notation

All of the following mean the same thing:

$$f'(x) \quad \frac{df}{dx} \quad \frac{d}{dx}[f(x)] \quad Df(x) \quad \dot{f}(x)$$

### Differentiability

$f$ is differentiable at $x$ if and only if:

1. $f$ is [[limits|continuous]] at $x$
2. The left-hand and right-hand limits of the difference quotient agree

Differentiability is **stronger** than continuity — every differentiable function is continuous, but not vice versa (e.g. $|x|$ at $x=0$).

### Basic rules

| Rule | Formula |
|---|---|
| Power | $\frac{d}{dx}x^n = nx^{n-1}$ |
| Sum | $(f+g)' = f' + g'$ |
| Product | $(fg)' = f'g + fg'$ |
| Quotient | $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$ |
| [[chain-rule\|Chain]] | $\frac{d}{dx}f(g(x)) = f'(g(x))\cdot g'(x)$ |

The [[fundamental-theorem-calculus|Fundamental Theorem of Calculus]] connects derivatives to integrals.
