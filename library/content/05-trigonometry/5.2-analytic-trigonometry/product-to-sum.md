---
title: Product-to-Sum & Sum-to-Product
tag: trigonometry
summary: Identities that convert products of trig functions into sums, and sums into products.
links:
  - sum-difference-formulas
  - double-half-angle
  - pythagorean-identities
---

# Product-to-Sum & Sum-to-Product

The **product-to-sum** identities rewrite a product of two trigonometric functions (like $\sin A \cos B$) as a sum of simpler trig terms. Conversely, the **sum-to-product** identities do the reverse. Both families are obtained directly by adding or subtracting the sum and difference formulas. They are particularly important in integration (converting hard-to-integrate products into easy sums), in signal processing (where they model beating phenomena between two frequencies), and in Fourier analysis.

## Product-to-Sum Identities

$$\sin A \cos B = \frac{1}{2}\bigl[\sin(A+B) + \sin(A-B)\bigr]$$

$$\cos A \sin B = \frac{1}{2}\bigl[\sin(A+B) - \sin(A-B)\bigr]$$

$$\cos A \cos B = \frac{1}{2}\bigl[\cos(A+B) + \cos(A-B)\bigr]$$

$$\sin A \sin B = -\frac{1}{2}\bigl[\cos(A+B) - \cos(A-B)\bigr] = \frac{1}{2}\bigl[\cos(A-B) - \cos(A+B)\bigr]$$

## Sum-to-Product Identities

$$\sin P + \sin Q = 2\sin\!\left(\frac{P+Q}{2}\right)\cos\!\left(\frac{P-Q}{2}\right)$$

$$\sin P - \sin Q = 2\cos\!\left(\frac{P+Q}{2}\right)\sin\!\left(\frac{P-Q}{2}\right)$$

$$\cos P + \cos Q = 2\cos\!\left(\frac{P+Q}{2}\right)\cos\!\left(\frac{P-Q}{2}\right)$$

$$\cos P - \cos Q = -2\sin\!\left(\frac{P+Q}{2}\right)\sin\!\left(\frac{P-Q}{2}\right)$$

## Derivation

Adding the sum and difference formulas for sine:

$$\sin(A+B) + \sin(A-B) = 2\sin A\cos B$$

Dividing by 2 gives the first product-to-sum identity. The others follow analogously.

## Application: Beats in Physics

Two sound waves of slightly different frequencies $f_1$ and $f_2$:

$$\cos(2\pi f_1 t) + \cos(2\pi f_2 t) = 2\cos\!\left(\pi(f_1-f_2)t\right)\cos\!\left(\pi(f_1+f_2)t\right)$$

The fast oscillation (carrier) is modulated by a slow envelope — perceived as "beating."

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $A, B, P, Q$ | angles in the identities |
| Product-to-sum | identity converting $\sin A\cos B$ (etc.) into a sum |
| Sum-to-product | identity converting $\sin P + \sin Q$ (etc.) into a product |
| Carrier frequency | the fast oscillation $(f_1+f_2)/2$ in the beats formula |
| Beating | acoustic phenomenon when two close frequencies interfere |
| $f_1, f_2$ | two frequencies |
| Fourier analysis | decomposing signals into sums of sines and cosines |
| Integration | antidifferentiation; product-to-sum converts hard products into easy sums |
