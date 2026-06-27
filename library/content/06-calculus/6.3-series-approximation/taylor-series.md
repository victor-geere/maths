---
title: Taylor Series
tag: analysis
summary: Represent a smooth function as an infinite polynomial around a point.
links:
  - derivative-definition
  - eulers-formula
  - convergence
---

## Key Formula

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

## Notes

A Taylor series expands $f$ around the point $a$ using all its derivatives there.  
The special case $a = 0$ is the **Maclaurin series**.

### Essential series (Maclaurin)

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

$$\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$$

$$\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \cdots$$

$$\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots \quad (|x| \leq 1,\; x\neq -1)$$

$$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + \cdots \quad (|x| < 1)$$

### Lagrange remainder

The error after $n$ terms is:

$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

for some $c$ between $a$ and $x$. Used to bound approximation error.

### Connection to Euler's formula

Substituting $x = i\theta$ into the series for $e^x$ and separating real/imaginary parts yields [[eulers-formula|Euler's formula]]:

$$e^{i\theta} = \cos\theta + i\sin\theta$$

The [[convergence|radius of convergence]] determines where the series is valid.
