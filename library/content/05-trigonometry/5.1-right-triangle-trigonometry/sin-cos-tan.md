---
title: Sine, Cosine, Tangent
tag: trigonometry
summary: The three primary trigonometric ratios defined on a right triangle and extended to all angles via the unit circle.
links:
  - pythagorean-theorem
  - special-angles
  - pythagorean-identities
  - csc-sec-cot
---

# Sine, Cosine, Tangent

The **sine**, **cosine**, and **tangent** are the three fundamental trigonometric functions. Originally defined as ratios of side lengths in a right triangle, they reveal the relationship between angles and lengths in any right-angled figure. Through the **unit circle** — a circle of radius 1 centred at the origin — these definitions extend seamlessly to all angles, including negative angles and those greater than 360°, making them indispensable tools across mathematics, physics, engineering, and signal processing.

## Right-Triangle Definitions

For a right triangle with acute angle $\theta$, opposite side $O$, adjacent side $A$, and hypotenuse $H$:

$$\sin\theta = \frac{O}{H} \qquad \cos\theta = \frac{A}{H} \qquad \tan\theta = \frac{O}{A} = \frac{\sin\theta}{\cos\theta}$$

Mnemonic: **SOH-CAH-TOA**.

## Unit Circle Definitions

Place angle $\theta$ at the origin, measured counter-clockwise from the positive $x$-axis. The terminal point on the unit circle is:

$$(\cos\theta,\; \sin\theta)$$

This definition works for **all** $\theta \in \mathbb{R}$.

## Key Values

| $\theta$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ |
|---|---|---|---|---|---|
| $\sin\theta$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ |
| $\cos\theta$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ |
| $\tan\theta$ | $0$ | $\frac{1}{\sqrt{3}}$ | $1$ | $\sqrt{3}$ | undef. |

## Signs by Quadrant (ASTC)

| Quadrant | Positive functions |
|---|---|
| I ($0°$–$90°$) | All |
| II ($90°$–$180°$) | Sine only |
| III ($180°$–$270°$) | Tangent only |
| IV ($270°$–$360°$) | Cosine only |

Mnemonic: **A**ll **S**tudents **T**ake **C**alculus.

## Periodicity

$$\sin(\theta + 2\pi) = \sin\theta, \qquad \cos(\theta + 2\pi) = \cos\theta, \qquad \tan(\theta + \pi) = \tan\theta$$

## Fundamental Identity

$$\sin^2\theta + \cos^2\theta = 1$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\sin\theta$ | sine of angle $\theta$ (opposite / hypotenuse) |
| $\cos\theta$ | cosine of angle $\theta$ (adjacent / hypotenuse) |
| $\tan\theta$ | tangent of angle $\theta$ ($\sin\theta / \cos\theta$) |
| $\theta$ (theta) | the angle under consideration |
| $O$ | length of the side opposite $\theta$ |
| $A$ | length of the side adjacent to $\theta$ |
| $H$ | length of the hypotenuse |
| Unit circle | circle of radius 1 centred at the origin |
| SOH-CAH-TOA | mnemonic for sin/cos/tan ratios |
| ASTC | mnemonic for sign of trig functions by quadrant |
| Hypotenuse | the longest side of a right triangle; opposite the right angle |
| Periodicity | property of repeating with a fixed period ($2\pi$ for sin/cos, $\pi$ for tan) |
| Quadrant | one of the four regions of the $xy$-plane divided by the axes |
