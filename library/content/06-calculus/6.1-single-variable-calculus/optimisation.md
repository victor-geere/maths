---
title: Optimisation
tag: calculus
summary: Finding the maximum or minimum values of a function using derivatives to locate and classify critical points.
links:
  - derivative-definition
  - mean-value-theorem
  - implicit-differentiation
---

# Optimisation

**Optimisation** is the art of finding the best possible outcome — the maximum profit, minimum cost, shortest path, or largest enclosed area. In calculus, optimisation rests on a fundamental observation: at any local maximum or minimum of a smooth function, the tangent line is horizontal, so the derivative equals zero. By finding where $f'(x) = 0$ (the **critical points**) and then classifying each as a maximum, minimum, or neither, we can systematically locate the optimal values. This approach extends to constrained optimisation via Lagrange multipliers and to functions of several variables.

## Procedure for Single-Variable Optimisation

1. **Find the domain** of the function.
2. **Differentiate:** compute $f'(x)$.
3. **Critical points:** solve $f'(x) = 0$ or note where $f'(x)$ is undefined.
4. **Classify** each critical point using the first or second derivative test.
5. **Check endpoints** if the domain is a closed interval.
6. **Compare values** to identify the global maximum and minimum.

## First Derivative Test

At a critical point $c$:
- If $f'$ changes from $+$ to $-$: **local maximum**
- If $f'$ changes from $-$ to $+$: **local minimum**
- If $f'$ does not change sign: **inflection point** (neither)

## Second Derivative Test

At a critical point $c$ where $f'(c) = 0$:

$$f''(c) < 0 \implies \text{local maximum}$$
$$f''(c) > 0 \implies \text{local minimum}$$
$$f''(c) = 0 \implies \text{inconclusive (use first derivative test)}$$

## Extreme Value Theorem

If $f$ is continuous on a closed interval $[a, b]$, then $f$ **attains** both its global maximum and global minimum — either at a critical point in $(a,b)$ or at an endpoint.

## Example: Maximum Area Rectangle

Enclose area $A = xy$ with perimeter $2x + 2y = P$ (fixed). Substituting $y = (P/2 - x)$:

$$A(x) = x\!\left(\frac{P}{2} - x\right) = \frac{Px}{2} - x^2$$

$A'(x) = \frac{P}{2} - 2x = 0 \implies x = \frac{P}{4}$, so $y = \frac{P}{4}$: a **square** maximises area.

## Example: Minimising Material

Cylindrical can of volume $V = \pi r^2 h$ (fixed). Surface area $SA = 2\pi r^2 + 2\pi r h$. Substituting $h = V/(\pi r^2)$ and differentiating yields $r = \sqrt[3]{V/(2\pi)}$, giving $h = 2r$: height equals diameter.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f'(x)$ | first derivative of $f$ at $x$ |
| $f''(x)$ | second derivative of $f$ at $x$ |
| Critical point | a point where $f'(x) = 0$ or $f'(x)$ is undefined |
| Local maximum | $f(c) \geq f(x)$ for $x$ near $c$ |
| Local minimum | $f(c) \leq f(x)$ for $x$ near $c$ |
| Global maximum | the largest value of $f$ on its entire domain |
| Global minimum | the smallest value of $f$ on its entire domain |
| Inflection point | where $f$ changes concavity; $f''(c) = 0$ (necessary, not sufficient) |
| Extreme Value Theorem | continuous $f$ on $[a,b]$ attains its max and min |
| Closed interval $[a,b]$ | includes both endpoints $a$ and $b$ |
| Concavity | whether the curve bends upward ($f''>0$) or downward ($f''<0$) |
