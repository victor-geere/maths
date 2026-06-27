---
title: Bisection Method
tag: numerical-methods
summary: A guaranteed root-finding algorithm that repeatedly halves an interval known to contain a root, converging linearly to the solution.
links:
  - newton-raphson
  - continuity
  - big-o-notation
---

# Bisection Method

The **bisection method** is the simplest and most robust algorithm for finding a root of a continuous function $f$ — a value $x^*$ where $f(x^*) = 0$. Starting from an interval $[a, b]$ where $f(a)$ and $f(b)$ have opposite signs (guaranteeing a root exists by the Intermediate Value Theorem), the method evaluates $f$ at the midpoint $m = (a+b)/2$ and discards the half that does not contain the root. Repeating this halving process converges to the root at a guaranteed linear rate: each iteration gains exactly one binary digit of precision. Bisection is slower than Newton–Raphson but requires no derivatives and never diverges — making it the reliable fallback when faster methods fail.

## Algorithm

**Input:** $f$, interval $[a,b]$ with $f(a)\cdot f(b) < 0$, tolerance $\varepsilon$.

1. Set $m = (a + b)/2$
2. If $|b - a| < \varepsilon$ or $f(m) = 0$: **return** $m$
3. If $f(a)\cdot f(m) < 0$: set $b \leftarrow m$; else set $a \leftarrow m$
4. Go to step 1

## Convergence

After $n$ iterations, the error satisfies:

$$|x^* - m_n| \leq \frac{b - a}{2^{n+1}}$$

To achieve tolerance $\varepsilon$ requires at most $n = \lceil\log_2\!\left(\frac{b-a}{\varepsilon}\right)\rceil$ iterations.

**Order of convergence:** linear ($p = 1$), with convergence factor $1/2$ per iteration.

## Guarantees

- **Always converges** if $f$ is continuous and $f(a)\cdot f(b) < 0$
- **No derivative** of $f$ needed
- Finds a root in $[a,b]$ — but not necessarily the closest one or a specific one if there are multiple

## Example

Find $\sqrt{2}$ by solving $f(x) = x^2 - 2 = 0$ on $[1, 2]$.

| Iter | $a$ | $b$ | $m$ | $f(m)$ |
|---|---|---|---|---|
| 1 | 1.0 | 2.0 | 1.5 | 0.25 |
| 2 | 1.0 | 1.5 | 1.25 | −0.4375 |
| 3 | 1.25 | 1.5 | 1.375 | −0.109 |

After 50 iterations: precision $\approx 10^{-15}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f(x)$ | the function whose root we seek |
| Root / zero | a value $x^*$ with $f(x^*) = 0$ |
| $[a,b]$ | the bracket containing the root |
| $m = (a+b)/2$ | midpoint of the current interval |
| $\varepsilon$ | tolerance — the desired precision |
| $f(a)\cdot f(b) < 0$ | sign change condition; guarantees a root in $[a,b]$ (IVT) |
| IVT | Intermediate Value Theorem |
| Linear convergence | error decreases by a constant factor (here $1/2$) per iteration |
| $\lceil x \rceil$ | ceiling of $x$: smallest integer $\geq x$ |
| Order of convergence $p$ | $p=1$ for bisection (linear); $p=2$ for Newton (quadratic) |
