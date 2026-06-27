---
title: Pythagorean Identities
tag: trigonometry
summary: The three fundamental trigonometric identities derived from the Pythagorean theorem on the unit circle.
links:
  - sin-cos-tan
  - csc-sec-cot
  - sum-difference-formulas
  - pythagorean-theorem
---

# Pythagorean Identities

The **Pythagorean identities** are three algebraic relationships between the trigonometric functions that hold for every angle $\theta$. They are direct consequences of the Pythagorean theorem applied to the unit circle: any point on the unit circle has coordinates $(\cos\theta, \sin\theta)$ and is at distance 1 from the origin, so $\cos^2\theta + \sin^2\theta = 1$ exactly. The other two identities follow by dividing through by $\sin^2\theta$ or $\cos^2\theta$. These identities are the most-used tool in simplifying trigonometric expressions and are the starting point for proving nearly every other trig identity.

## The Three Identities

### Identity 1 — The Fundamental Identity

$$\sin^2\theta + \cos^2\theta = 1$$

Derivation: the unit circle definition gives $(\cos\theta)^2 + (\sin\theta)^2 = 1^2$.

### Identity 2 — Divide by $\cos^2\theta$

$$\tan^2\theta + 1 = \sec^2\theta$$

### Identity 3 — Divide by $\sin^2\theta$

$$1 + \cot^2\theta = \csc^2\theta$$

## Common Rearrangements

| Original | Useful rearrangement |
|---|---|
| $\sin^2\theta + \cos^2\theta = 1$ | $\sin^2\theta = 1 - \cos^2\theta$ |
| $\tan^2\theta + 1 = \sec^2\theta$ | $\tan^2\theta = \sec^2\theta - 1$ |
| $1 + \cot^2\theta = \csc^2\theta$ | $\cot^2\theta = \csc^2\theta - 1$ |

## Example — Simplifying

Simplify $\dfrac{\sin^2\theta}{1 - \sin^2\theta}$:

$$\frac{\sin^2\theta}{1-\sin^2\theta} = \frac{\sin^2\theta}{\cos^2\theta} = \tan^2\theta$$

## Example — Proving an Identity

Prove $\sec^2\theta - \tan^2\theta = 1$:

$$\sec^2\theta - \tan^2\theta = (\tan^2\theta + 1) - \tan^2\theta = 1 \quad \square$$

## Useful Factorisation Pattern

$$\sin^2\theta - \cos^2\theta = (\sin\theta - \cos\theta)(\sin\theta + \cos\theta)$$

$$(\sin\theta + \cos\theta)^2 = 1 + 2\sin\theta\cos\theta$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\sin^2\theta$ | $(\sin\theta)^2$ — the sine squared (not $\sin(\theta^2)$) |
| $\cos^2\theta$ | $(\cos\theta)^2$ |
| $\tan^2\theta$ | $(\tan\theta)^2$ |
| $\sec^2\theta$ | $(\sec\theta)^2 = 1/\cos^2\theta$ |
| $\csc^2\theta$ | $(\csc\theta)^2 = 1/\sin^2\theta$ |
| $\cot^2\theta$ | $(\cot\theta)^2 = \cos^2\theta/\sin^2\theta$ |
| Unit circle | circle of radius 1; a point on it has coordinates $(\cos\theta, \sin\theta)$ |
| Identity | an equation true for all values of the variable |
| Simplify | rewrite in a shorter or more standard form |
| Rearrangement | algebraic manipulation to isolate one term |
