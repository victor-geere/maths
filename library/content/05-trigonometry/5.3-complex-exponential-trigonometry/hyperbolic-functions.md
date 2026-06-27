---
title: Hyperbolic Functions (sinh, cosh, tanh)
tag: trigonometry
summary: The hyperbolic analogues of sine, cosine, and tangent, defined via the natural exponential function.
links:
  - eulers-formula
  - sin-cos-tan
  - complex-numbers
  - inverse-trig
---

# Hyperbolic Functions (sinh, cosh, tanh)

The **hyperbolic functions** are the natural analogues of the circular trigonometric functions, obtained by replacing the unit circle $x^2 + y^2 = 1$ with the unit hyperbola $x^2 - y^2 = 1$. They are defined directly in terms of the exponential function and satisfy identities that closely mirror those of $\sin$ and $\cos$ — with occasional sign differences. Hyperbolic functions appear throughout applied mathematics: in the shape of a hanging cable (the catenary), in solutions to the wave equation and heat equation, in special relativity, and as antiderivatives in calculus.

## Definitions

$$\sinh x = \frac{e^x - e^{-x}}{2}, \qquad \cosh x = \frac{e^x + e^{-x}}{2}, \qquad \tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

The reciprocal hyperbolic functions:

$$\text{csch}\, x = \frac{1}{\sinh x}, \qquad \text{sech}\, x = \frac{1}{\cosh x}, \qquad \coth x = \frac{1}{\tanh x}$$

## Fundamental Identity

$$\cosh^2 x - \sinh^2 x = 1$$

(Compare: $\cos^2\theta + \sin^2\theta = 1$ for circular trig — note the sign change.)

## Further Identities

$$\sinh(x \pm y) = \sinh x \cosh y \pm \cosh x \sinh y$$

$$\cosh(x \pm y) = \cosh x \cosh y \pm \sinh x \sinh y$$

$$\sinh 2x = 2\sinh x \cosh x, \qquad \cosh 2x = \cosh^2 x + \sinh^2 x$$

## Connection to Circular Functions (via Complex Numbers)

$$\sin(ix) = i\sinh x, \qquad \cos(ix) = \cosh x$$

So hyperbolic functions are circular trig functions evaluated at purely imaginary angles.

## Derivatives and Integrals

$$\frac{d}{dx}\sinh x = \cosh x, \qquad \frac{d}{dx}\cosh x = \sinh x, \qquad \frac{d}{dx}\tanh x = \text{sech}^2 x$$

$$\int \cosh x\, dx = \sinh x + C, \qquad \int \sinh x\, dx = \cosh x + C$$

## Catenary

The shape of a uniform cable hanging under gravity is:

$$y = a\cosh\!\left(\frac{x}{a}\right)$$

## Inverse Hyperbolic Functions

$$\text{arcsinh}\, x = \ln\!\left(x + \sqrt{x^2+1}\right), \qquad \text{arccosh}\, x = \ln\!\left(x + \sqrt{x^2-1}\right) \quad (x \geq 1)$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\sinh x$ | hyperbolic sine: $(e^x - e^{-x})/2$ |
| $\cosh x$ | hyperbolic cosine: $(e^x + e^{-x})/2$ |
| $\tanh x$ | hyperbolic tangent: $\sinh x / \cosh x$ |
| $\text{sech}\, x$ | hyperbolic secant: $1/\cosh x$ |
| $\text{csch}\, x$ | hyperbolic cosecant: $1/\sinh x$ |
| $\coth x$ | hyperbolic cotangent: $\cosh x / \sinh x$ |
| $e$ | Euler's number ($\approx 2.71828$), base of natural logarithm |
| $e^x$ | exponential function |
| Unit hyperbola | the curve $x^2 - y^2 = 1$ |
| Catenary | the shape of a freely hanging chain or cable |
| Imaginary argument | evaluating a function at $ix$ where $i^2=-1$ |
| $\text{arcsinh}, \text{arccosh}$ | inverse hyperbolic sine and cosine |
| $\ln$ | natural logarithm (log base $e$) |
