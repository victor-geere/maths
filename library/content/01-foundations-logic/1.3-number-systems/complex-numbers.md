---
title: Complex Numbers
tag: algebra
summary: Extension of the reals with i² = −1; the complex plane.
links:
  - eulers-formula
  - polynomial-roots
  - quadratic-formula
---

## Key Formula

$$z = a + bi = r\,e^{i\theta}$$

## Notes

The complex numbers $\mathbb{C} = \{a + bi \mid a,b \in \mathbb{R}\}$ extend the reals by adjoining $i$, a square root of $-1$.

### Two representations

| Form | Expression | When useful |
|---|---|---|
| Rectangular | $z = a + bi$ | Addition, subtraction |
| Polar / Euler | $z = re^{i\theta}$ | Multiplication, powers, roots |

$$r = |z| = \sqrt{a^2 + b^2}, \qquad \theta = \arg(z) = \operatorname{atan2}(b, a)$$

### Conjugate

$\bar{z} = a - bi$. Key identity: $z\bar{z} = |z|^2$.  
Division: $\dfrac{z_1}{z_2} = \dfrac{z_1 \bar{z}_2}{|z_2|^2}$.

### Multiplication in polar form

$$r_1 e^{i\theta_1} \cdot r_2 e^{i\theta_2} = r_1 r_2\, e^{i(\theta_1 + \theta_2)}$$

Multiplication **rotates** and **scales** — the geometric heart of complex arithmetic.

### De Moivre's theorem

$$(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$$

Useful for computing $n$th roots and deriving multiple-angle identities.

[[eulers-formula|Euler's formula]] $e^{i\theta} = \cos\theta + i\sin\theta$ unifies these representations.
