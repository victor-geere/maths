---
title: Double & Half-Angle Formulas
tag: trigonometry
summary: Formulas for trigonometric functions of 2θ and θ/2 derived from the sum and difference identities.
links:
  - sum-difference-formulas
  - pythagorean-identities
  - product-to-sum
---

# Double & Half-Angle Formulas

The **double-angle formulas** express $\sin 2\theta$, $\cos 2\theta$, and $\tan 2\theta$ purely in terms of $\sin\theta$ and $\cos\theta$. They follow immediately from the sum formulas by setting $A = B = \theta$. The **half-angle formulas** go in the reverse direction: they express the trig functions of $\theta/2$ in terms of those of $\theta$, and they are derived from the double-angle formulas for cosine by solving for $\sin^2$ or $\cos^2$. Together these formulas are essential for integration (reducing powers of trig functions), solving trig equations, and simplifying complicated expressions.

## Double-Angle Formulas

### Sine
$$\sin 2\theta = 2\sin\theta\cos\theta$$

### Cosine (three equivalent forms)
$$\cos 2\theta = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$$

### Tangent
$$\tan 2\theta = \frac{2\tan\theta}{1 - \tan^2\theta}$$

## Power-Reduction Formulas

Rearranging the cosine double-angle formulas:

$$\cos^2\theta = \frac{1 + \cos 2\theta}{2}, \qquad \sin^2\theta = \frac{1 - \cos 2\theta}{2}$$

These are used to integrate $\sin^2\theta$ and $\cos^2\theta$.

## Half-Angle Formulas

Replace $\theta$ by $\theta/2$ in the power-reduction formulas:

$$\sin\frac{\theta}{2} = \pm\sqrt{\frac{1-\cos\theta}{2}}$$

$$\cos\frac{\theta}{2} = \pm\sqrt{\frac{1+\cos\theta}{2}}$$

$$\tan\frac{\theta}{2} = \pm\sqrt{\frac{1-\cos\theta}{1+\cos\theta}} = \frac{\sin\theta}{1+\cos\theta} = \frac{1-\cos\theta}{\sin\theta}$$

The sign $\pm$ is determined by the quadrant of $\theta/2$.

## Example

Find $\cos 2\theta$ when $\sin\theta = 3/5$ (and $\theta$ is in quadrant I, so $\cos\theta = 4/5$):

$$\cos 2\theta = \cos^2\theta - \sin^2\theta = \frac{16}{25} - \frac{9}{25} = \frac{7}{25}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $2\theta$ | double angle (twice $\theta$) |
| $\theta/2$ | half angle (half of $\theta$) |
| $\sin 2\theta$ | sine of the double angle |
| $\cos 2\theta$ | cosine of the double angle |
| $\tan 2\theta$ | tangent of the double angle |
| Power-reduction formulas | expressions for $\sin^2\theta$ and $\cos^2\theta$ using $\cos 2\theta$ |
| $\pm$ | sign depends on the quadrant of the half-angle |
| Quadrant | one of the four regions of the plane; determines signs of trig functions |
| Integration | finding antiderivatives; power-reduction is used to integrate $\sin^2$ and $\cos^2$ |
