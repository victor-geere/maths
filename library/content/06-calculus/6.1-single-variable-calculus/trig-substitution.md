---
title: Trigonometric Substitution
tag: calculus
summary: Eliminating square roots of quadratic expressions from integrals by substituting a trigonometric function for x.
links:
  - integration-by-substitution
  - pythagorean-identities
  - integration-by-parts
---

# Trigonometric Substitution

**Trigonometric substitution** is a specialised integration technique for integrals containing expressions of the form $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, or $\sqrt{x^2 - a^2}$. By substituting $x = a\sin\theta$, $x = a\tan\theta$, or $x = a\sec\theta$ respectively, the Pythagorean identities convert the square root into a simple trig function, transforming the integral into one in $\theta$ that can be handled by standard techniques. After integrating, a reference triangle is used to back-substitute and express the answer in terms of $x$.

## The Three Standard Substitutions

| Expression | Substitution | Identity used |
|---|---|---|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$, $\theta \in [-\pi/2, \pi/2]$ | $1 - \sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$, $\theta \in (-\pi/2, \pi/2)$ | $1 + \tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$, $\theta \in [0, \pi/2)$ | $\sec^2\theta - 1 = \tan^2\theta$ |

## Example: $\int \sqrt{1 - x^2}\,dx$

Let $x = \sin\theta$, $dx = \cos\theta\,d\theta$:

$$\int \sqrt{1-\sin^2\theta}\,\cos\theta\,d\theta = \int\cos^2\theta\,d\theta = \frac{\theta}{2} + \frac{\sin 2\theta}{4} + C$$

Back-substitute $\theta = \arcsin x$, $\sin 2\theta = 2x\sqrt{1-x^2}$:

$$= \frac{\arcsin x}{2} + \frac{x\sqrt{1-x^2}}{2} + C$$

## Example: $\int \frac{dx}{\sqrt{x^2+4}}$

Let $x = 2\tan\theta$, $dx = 2\sec^2\theta\,d\theta$:

$$\int\frac{2\sec^2\theta}{2\sec\theta}\,d\theta = \int\sec\theta\,d\theta = \ln|\sec\theta + \tan\theta| + C$$

Back-substitute $\sec\theta = \sqrt{x^2+4}/2$, $\tan\theta = x/2$:

$$= \ln\!\left|\frac{\sqrt{x^2+4}+x}{2}\right| + C = \ln\!\left|x + \sqrt{x^2+4}\right| + C'$$

## Reference Triangle

Draw a right triangle matching the substitution to read off all trig values needed for back-substitution:

- For $x = a\sin\theta$: opposite = $x$, hypotenuse = $a$, adjacent = $\sqrt{a^2-x^2}$.
- For $x = a\tan\theta$: opposite = $x$, adjacent = $a$, hypotenuse = $\sqrt{x^2+a^2}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\sqrt{a^2 - x^2}$ | square root of a difference of squares; suggests $x = a\sin\theta$ |
| $\sqrt{a^2 + x^2}$ | square root of a sum of squares; suggests $x = a\tan\theta$ |
| $\sqrt{x^2 - a^2}$ | square root of a difference, $x$ larger; suggests $x = a\sec\theta$ |
| $a$ | the constant in the quadratic expression |
| $\theta$ | the new variable after substitution |
| $dx$ | differential of $x$ — replaced by the differential of the trig expression |
| Pythagorean identity | $\sin^2+\cos^2=1$, $\tan^2+1=\sec^2$, $\sec^2-1=\tan^2$ |
| Back-substitution | converting the answer in $\theta$ back to $x$ |
| Reference triangle | a right triangle used to read off trig values during back-substitution |
| $\arcsin x$ | the inverse sine of $x$ |
| $C$ | constant of integration |
