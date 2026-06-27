---
title: Cosecant, Secant, Cotangent
tag: trigonometry
summary: The three reciprocal trigonometric functions — the multiplicative inverses of sine, cosine, and tangent.
links:
  - sin-cos-tan
  - pythagorean-identities
  - special-angles
---

# Cosecant, Secant, Cotangent

The **cosecant**, **secant**, and **cotangent** are the reciprocals of the three primary trigonometric functions. While they are encountered less frequently in elementary work, they appear naturally in integration, in trigonometric identities, and in physics (especially in optics and mechanics). Understanding them as simple reciprocals — not as independent definitions — is the key to working with them fluently.

## Definitions

$$\csc\theta = \frac{1}{\sin\theta} \qquad \sec\theta = \frac{1}{\cos\theta} \qquad \cot\theta = \frac{1}{\tan\theta} = \frac{\cos\theta}{\sin\theta}$$

In terms of right-triangle sides (opposite $O$, adjacent $A$, hypotenuse $H$):

$$\csc\theta = \frac{H}{O} \qquad \sec\theta = \frac{H}{A} \qquad \cot\theta = \frac{A}{O}$$

## Key Values

| $\theta$ | $30°$ | $45°$ | $60°$ | $90°$ |
|---|---|---|---|---|
| $\csc\theta$ | $2$ | $\sqrt{2}$ | $\frac{2}{\sqrt{3}}$ | $1$ |
| $\sec\theta$ | $\frac{2}{\sqrt{3}}$ | $\sqrt{2}$ | $2$ | undef. |
| $\cot\theta$ | $\sqrt{3}$ | $1$ | $\frac{1}{\sqrt{3}}$ | $0$ |

## Pythagorean Identities (Reciprocal Forms)

Dividing $\sin^2\theta + \cos^2\theta = 1$ by $\sin^2\theta$ and $\cos^2\theta$ respectively:

$$1 + \cot^2\theta = \csc^2\theta$$

$$\tan^2\theta + 1 = \sec^2\theta$$

## Domains

| Function | Undefined when | Domain |
|---|---|---|
| $\csc\theta$ | $\sin\theta = 0$, i.e. $\theta = n\pi$ | $\mathbb{R} \setminus \{n\pi\}$ |
| $\sec\theta$ | $\cos\theta = 0$, i.e. $\theta = \frac{\pi}{2} + n\pi$ | $\mathbb{R} \setminus \{\frac{\pi}{2}+n\pi\}$ |
| $\cot\theta$ | $\sin\theta = 0$, i.e. $\theta = n\pi$ | $\mathbb{R} \setminus \{n\pi\}$ |

## Periodicity

$$\csc(\theta + 2\pi) = \csc\theta, \qquad \sec(\theta + 2\pi) = \sec\theta, \qquad \cot(\theta + \pi) = \cot\theta$$

## Use in Integration

$$\int \sec\theta\, d\theta = \ln|\sec\theta + \tan\theta| + C$$

$$\int \csc\theta\, d\theta = -\ln|\csc\theta + \cot\theta| + C$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\csc\theta$ | cosecant — reciprocal of $\sin\theta$ |
| $\sec\theta$ | secant — reciprocal of $\cos\theta$ |
| $\cot\theta$ | cotangent — reciprocal of $\tan\theta$ |
| Reciprocal | the multiplicative inverse: reciprocal of $x$ is $1/x$ |
| $n\pi$ | any integer multiple of $\pi$ |
| Domain | the set of values for which a function is defined |
| Undefined | the function has no value (division by zero) |
| Pythagorean identities | the three identities $\sin^2+\cos^2=1$, $1+\cot^2=\csc^2$, $\tan^2+1=\sec^2$ |
| $H, O, A$ | hypotenuse, opposite, adjacent sides of a right triangle |
