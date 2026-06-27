---
title: Inverse Trig Functions
tag: trigonometry
summary: The functions arcsin, arccos, arctan — the inverses of sine, cosine, and tangent restricted to principal-value domains.
links:
  - sin-cos-tan
  - pythagorean-identities
  - sum-difference-formulas
---

# Inverse Trig Functions

The **inverse trigonometric functions** — $\arcsin$, $\arccos$, $\arctan$ (also written $\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$) — answer the question: *given a ratio, what angle produces it?* Since sine and cosine are periodic and not one-to-one on all of $\mathbb{R}$, we must restrict them to a **principal-value branch** to define a genuine inverse. The resulting functions are essential for solving trigonometric equations, for computing angles in applied problems, and as antiderivatives in calculus.

## Definitions and Principal Domains

| Function | Definition | Domain | Range |
|---|---|---|---|
| $\arcsin x$ | the angle in $[-\pi/2, \pi/2]$ whose sine is $x$ | $[-1, 1]$ | $[-\pi/2,\, \pi/2]$ |
| $\arccos x$ | the angle in $[0, \pi]$ whose cosine is $x$ | $[-1, 1]$ | $[0,\, \pi]$ |
| $\arctan x$ | the angle in $(-\pi/2, \pi/2)$ whose tangent is $x$ | $\mathbb{R}$ | $(-\pi/2,\, \pi/2)$ |

## Key Values

| $x$ | $\arcsin x$ | $\arccos x$ | $\arctan x$ |
|---|---|---|---|
| $0$ | $0$ | $\pi/2$ | $0$ |
| $1/2$ | $\pi/6$ | $\pi/3$ | — |
| $\sqrt{2}/2$ | $\pi/4$ | $\pi/4$ | — |
| $\sqrt{3}/2$ | $\pi/3$ | $\pi/6$ | — |
| $1$ | $\pi/2$ | $0$ | — |
| $-1$ | $-\pi/2$ | $\pi$ | — |

## Identities

$$\arcsin x + \arccos x = \frac{\pi}{2}$$

$$\arctan x + \arctan\frac{1}{x} = \frac{\pi}{2} \quad (x > 0)$$

$$\sin(\arcsin x) = x \quad \text{for } x \in [-1,1]$$

$$\arcsin(\sin\theta) = \theta \quad \text{only for } \theta \in [-\pi/2, \pi/2]$$

## Derivatives

$$\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}, \quad |x| < 1$$

$$\frac{d}{dx}\arccos x = -\frac{1}{\sqrt{1-x^2}}, \quad |x| < 1$$

$$\frac{d}{dx}\arctan x = \frac{1}{1+x^2}$$

## Integrals

$$\int \frac{dx}{\sqrt{1-x^2}} = \arcsin x + C$$

$$\int \frac{dx}{1+x^2} = \arctan x + C$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\arcsin x$ / $\sin^{-1} x$ | inverse sine of $x$ (principal value in $[-\pi/2,\pi/2]$) |
| $\arccos x$ / $\cos^{-1} x$ | inverse cosine of $x$ (principal value in $[0,\pi]$) |
| $\arctan x$ / $\tan^{-1} x$ | inverse tangent of $x$ (principal value in $(-\pi/2,\pi/2)$) |
| Principal-value branch | the restricted domain on which the inverse is single-valued |
| Domain | the set of inputs for which a function is defined |
| Range | the set of output values a function can produce |
| $\sin^{-1} x$ | alternative notation for $\arcsin x$ (not $1/\sin x$) |
| Periodic | repeating with a fixed period; trig functions must be restricted before inverting |
| Antiderivative | the function whose derivative gives the integrand |
| One-to-one | every output value comes from exactly one input; required for an inverse to exist |
