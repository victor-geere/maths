---
title: Newton–Raphson Method
tag: numerical-methods
summary: A quadratically convergent root-finding algorithm that iteratively refines an estimate using the tangent line to the curve at each point.
links:
  - bisection-method
  - derivative-definition
  - taylor-series
---

# Newton–Raphson Method

The **Newton–Raphson method** is the workhorse of numerical root-finding: starting from an initial guess $x_0$, each iteration follows the tangent line to $y = f(x)$ at the current point down to the $x$-axis, using that intercept as the next approximation. When it works, it converges **quadratically** — the number of correct decimal digits roughly doubles each iteration — making it far faster than bisection. The trade-off is that it requires the derivative $f'(x)$ and can fail if the initial guess is poor, the derivative is zero near the root, or the function has multiple roots. Despite this, its speed makes it the default choice in scientific computing, optimization algorithms, and the engine behind many modern solvers.

## Iteration Formula

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

**Derivation:** the tangent line at $(x_n, f(x_n))$ is $y = f(x_n) + f'(x_n)(x - x_n)$. Setting $y = 0$ gives $x_{n+1}$.

## Convergence

Near a **simple root** $x^*$ (where $f(x^*) = 0$ and $f'(x^*) \neq 0$):

$$|x_{n+1} - x^*| \approx \frac{|f''(x^*)|}{2|f'(x^*)|}|x_n - x^*|^2$$

**Order of convergence:** quadratic ($p = 2$) — each step squares the error.

## Failure Modes

| Scenario | What can happen |
|---|---|
| $f'(x_n) = 0$ | Division by zero; method breaks down |
| Poor initial guess | May converge to wrong root or diverge |
| Multiple root | Convergence slows to linear |
| Oscillation | Two points trading places without converging |

## Newton's Method for $\sqrt{a}$

Solve $f(x) = x^2 - a = 0$: $f'(x) = 2x$.

$$x_{n+1} = x_n - \frac{x_n^2 - a}{2x_n} = \frac{x_n + a/x_n}{2}$$

Starting from $x_0 = 1$, $a = 2$: $x_1 = 1.5$, $x_2 = 1.4167$, $x_3 = 1.41422\ldots$ (correct to 5 d.p. after 3 steps).

## Secant Method

If $f'$ is unavailable, approximate $f'(x_n) \approx \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$. Convergence is superlinear (order $\approx 1.618$, the golden ratio).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $x_{n+1} = x_n - f(x_n)/f'(x_n)$ | Newton–Raphson iteration |
| $f'(x_n)$ | derivative of $f$ at $x_n$; slope of the tangent |
| Simple root | $f(x^*)=0$ and $f'(x^*)\neq 0$ |
| Multiple root | $f(x^*)=0$ and $f'(x^*)=0$; convergence degrades |
| Quadratic convergence | $|e_{n+1}| \approx C|e_n|^2$; digits double per step |
| $e_n = x_n - x^*$ | error at step $n$ |
| Secant method | Newton without $f'$: uses finite-difference approximation |
| Order of convergence $p$ | $p=2$ for Newton; $p\approx 1.618$ for secant |
| Tangent line | the linear approximation to $f$ at $x_n$ |
| Divergence | when iterates grow without bound or cycle |
