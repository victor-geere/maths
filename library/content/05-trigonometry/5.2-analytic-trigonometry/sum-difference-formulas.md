---
title: Sum & Difference Formulas
tag: trigonometry
summary: Exact formulas for sin(A±B) and cos(A±B) expressing compound angles in terms of single-angle values.
links:
  - pythagorean-identities
  - double-half-angle
  - sin-cos-tan
  - eulers-formula
---

# Sum & Difference Formulas

The **sum and difference formulas** express the sine or cosine of a sum (or difference) of two angles in terms of the sines and cosines of those individual angles. They allow the evaluation of trigonometric functions at non-standard angles by splitting them into known special angles, and they are the engine from which the double-angle formulas, half-angle formulas, and product-to-sum identities are all derived. An elegant proof uses Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$, making these formulas a bridge between real trigonometry and complex exponentials.

## The Formulas

### Sine

$$\sin(A + B) = \sin A \cos B + \cos A \sin B$$

$$\sin(A - B) = \sin A \cos B - \cos A \sin B$$

### Cosine

$$\cos(A + B) = \cos A \cos B - \sin A \sin B$$

$$\cos(A - B) = \cos A \cos B + \sin A \sin B$$

### Tangent

$$\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}$$

$$\tan(A - B) = \frac{\tan A - \tan B}{1 + \tan A \tan B}$$

## Proof via Euler's Formula

$$e^{i(A+B)} = e^{iA}\,e^{iB} = (\cos A + i\sin A)(\cos B + i\sin B)$$

Expanding and separating real and imaginary parts yields both formulas simultaneously.

## Derivation of Key Values

**Example:** $\sin 75° = \sin(45° + 30°)$

$$= \sin 45°\cos 30° + \cos 45°\sin 30° = \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\cdot\frac{1}{2} = \frac{\sqrt{6}+\sqrt{2}}{4}$$

## Cofunction Identities

Setting $B = 90°$ in the difference formula:

$$\sin(90° - A) = \cos A, \qquad \cos(90° - A) = \sin A$$

These justify calling sine and cosine "cofunctions" — each is the complement of the other.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $A, B$ | two angles being added or subtracted |
| $\sin(A \pm B)$ | sine of the sum/difference |
| $\cos(A \pm B)$ | cosine of the sum/difference |
| $\tan(A \pm B)$ | tangent of the sum/difference |
| Compound angle | a sum or difference of two angles, e.g. $A + B$ |
| Cofunction identity | $\sin(90°-\theta) = \cos\theta$ and vice versa |
| Euler's formula | $e^{i\theta} = \cos\theta + i\sin\theta$ |
| $i$ | the imaginary unit ($i^2 = -1$) |
| $e^{iA}$ | complex exponential evaluated at $iA$ |
| Surd | exact irrational number expressed with roots |
