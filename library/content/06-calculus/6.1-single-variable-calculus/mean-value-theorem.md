---
title: Mean Value Theorem
tag: calculus
summary: A differentiable function on [a,b] must have at least one interior point where the instantaneous rate equals the average rate over the interval.
links:
  - derivative-definition
  - continuity
  - optimisation
---

# Mean Value Theorem

The **Mean Value Theorem (MVT)** is one of the central theorems of differential calculus. It guarantees that for any smooth arc between two points, there is at least one point on the arc where the tangent line is exactly parallel to the secant line connecting the endpoints. In other words, the instantaneous rate of change must equal the average rate of change somewhere in between. The theorem is the rigorous foundation for connecting local behaviour (derivatives) to global behaviour (net change), and it underpins major results including L'Hôpital's Rule, Taylor's theorem, and the fundamental theorem of calculus.

## Statement

If $f$ is **continuous** on $[a, b]$ and **differentiable** on $(a, b)$, then there exists at least one $c \in (a, b)$ such that:

$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

The right-hand side is the slope of the secant line between $(a, f(a))$ and $(b, f(b))$.

## Geometric Interpretation

There is a point $c$ where the tangent to the curve is **parallel** to the chord joining the endpoints.

## Rolle's Theorem (Special Case)

If additionally $f(a) = f(b)$, then there exists $c \in (a, b)$ with $f'(c) = 0$ (a horizontal tangent). This is Rolle's Theorem, from which the MVT is proved.

## Proof Sketch

Apply Rolle's Theorem to the auxiliary function:

$$h(x) = f(x) - \left[f(a) + \frac{f(b)-f(a)}{b-a}(x-a)\right]$$

$h$ satisfies $h(a) = h(b) = 0$, so Rolle's gives $h'(c) = 0$ at some $c$, which yields $f'(c) = \frac{f(b)-f(a)}{b-a}$.

## Consequences

- **Monotonicity:** if $f'(x) > 0$ on $(a,b)$, then $f$ is strictly increasing on $[a,b]$.
- **Constant functions:** if $f'(x) = 0$ everywhere, then $f$ is constant.
- **Error bounds:** $|f(b) - f(a)| \leq M|b - a|$ where $M = \sup|f'|$ on $(a,b)$.

## Example

$f(x) = x^2$ on $[1, 3]$. Average rate $= (9-1)/(3-1) = 4$. We need $f'(c) = 2c = 4$, so $c = 2 \in (1,3)$. ✓

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f'(c)$ | derivative of $f$ at the point $c$ |
| $[a, b]$ | closed interval from $a$ to $b$ (endpoints included) |
| $(a, b)$ | open interval from $a$ to $b$ (endpoints excluded) |
| Continuous on $[a,b]$ | no breaks or jumps; includes behaviour at endpoints |
| Differentiable on $(a,b)$ | $f'(x)$ exists at every interior point |
| Secant line | the straight line joining two points on a curve |
| Tangent line | the line touching the curve at a single point with slope $f'$ |
| Rolle's Theorem | MVT when $f(a) = f(b)$: guarantees $f'(c) = 0$ for some $c$ |
| Monotonicity | property of being consistently increasing or decreasing |
| $\sup$ | supremum — the least upper bound |
