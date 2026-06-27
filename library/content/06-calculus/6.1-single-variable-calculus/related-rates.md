---
title: Related Rates
tag: calculus
summary: Finding the rate of change of one quantity by relating it via an equation to another quantity whose rate is known, then differentiating with respect to time.
links:
  - implicit-differentiation
  - chain-rule
  - derivative-definition
---

# Related Rates

**Related rates** problems ask: if one measurable quantity is changing at a known rate, how fast is a related quantity changing? The key insight is that any equation connecting two quantities — whether geometric (Pythagoras, similar triangles) or physical (volume formula, Boyle's law) — becomes an equation between their rates of change when we differentiate both sides with respect to time $t$. This is simply the chain rule applied to a real-world relationship. Related rates appear throughout physics and engineering: the speed of a shadow, the rate at which a balloon deflates, the changing angle of elevation of a rocket.

## Method

1. Draw a diagram and assign variables to all changing quantities.
2. Write an equation connecting the variables (geometric identity, physical law, etc.).
3. Differentiate both sides with respect to time $t$ (implicit differentiation).
4. Substitute the known values and rates; solve for the unknown rate.

## Example: Ladder Sliding Down a Wall

A 10 m ladder leans against a wall. The base slides away at $2$ m/s. How fast is the top sliding down when the base is $6$ m from the wall?

Let $x$ = distance of base from wall, $y$ = height of top. Pythagoras:

$$x^2 + y^2 = 100$$

Differentiate with respect to $t$:

$$2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$$

When $x = 6$: $y = 8$. Substituting $\frac{dx}{dt} = 2$:

$$2(6)(2) + 2(8)\frac{dy}{dt} = 0 \implies \frac{dy}{dt} = -\frac{3}{2} \text{ m/s}$$

The top slides down at $1.5$ m/s.

## Example: Expanding Ripple

A stone dropped in a pond creates a circular ripple with radius growing at $3$ cm/s. How fast is the area increasing when $r = 10$ cm?

$$A = \pi r^2 \implies \frac{dA}{dt} = 2\pi r \frac{dr}{dt} = 2\pi(10)(3) = 60\pi \approx 188.5 \text{ cm}^2/\text{s}$$

## Common Geometric Formulas Used

| Shape | Formula |
|---|---|
| Circle | $A = \pi r^2$, $C = 2\pi r$ |
| Sphere | $V = \tfrac{4}{3}\pi r^3$, $SA = 4\pi r^2$ |
| Cone | $V = \tfrac{1}{3}\pi r^2 h$ |
| Right triangle | $a^2 + b^2 = c^2$ |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\frac{dx}{dt}$ | rate of change of $x$ with respect to time $t$ |
| $\frac{dy}{dt}$ | rate of change of $y$ with respect to time |
| $t$ | time variable |
| Related rates | rates of change of quantities linked by an equation |
| Chain rule | $\frac{d}{dt}[f(x(t))] = f'(x)\frac{dx}{dt}$ |
| Implicit differentiation | differentiating an equation without solving for one variable first |
| $A$ | area |
| $V$ | volume |
| $r$ | radius |
| $h$ | height |
| $SA$ | surface area |
