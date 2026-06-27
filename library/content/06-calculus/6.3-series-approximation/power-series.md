---
title: Power Series
tag: calculus
summary: Infinite series of the form Σ aₙ(x−c)ⁿ that represent functions within a radius of convergence.
links:
  - convergence
  - taylor-series
  - fourier-series
---

# Power Series

A **power series** is an infinite series of the form $\sum_{n=0}^\infty a_n(x-c)^n$, where $c$ is the **centre** and the $a_n$ are coefficients. Unlike a polynomial, a power series has infinitely many terms and converges only for $x$ close enough to $c$ — within the **radius of convergence** $R$. Inside this radius, a power series defines a smooth function that can be differentiated and integrated term by term, just like a polynomial. Power series are the bridge between analytic functions and their polynomial approximations, and they underlie the Taylor series representation of elementary functions such as $e^x$, $\sin x$, and $\ln(1+x)$.

## Definition

$$\sum_{n=0}^\infty a_n(x - c)^n = a_0 + a_1(x-c) + a_2(x-c)^2 + \cdots$$

## Radius and Interval of Convergence

The series converges absolutely for $|x - c| < R$ and diverges for $|x - c| > R$.

**Ratio Test:** $R = \lim_{n\to\infty}\left|\frac{a_n}{a_{n+1}}\right|$ (when the limit exists).

**Root Test (Hadamard):** $R = \dfrac{1}{\limsup_{n\to\infty}|a_n|^{1/n}}$.

At $|x-c| = R$ (the endpoints), convergence must be checked separately.

## Term-by-Term Operations

Inside the radius of convergence:

$$\frac{d}{dx}\sum_{n=0}^\infty a_n(x-c)^n = \sum_{n=1}^\infty n\,a_n(x-c)^{n-1}$$

$$\int\sum_{n=0}^\infty a_n(x-c)^n\,dx = \sum_{n=0}^\infty \frac{a_n}{n+1}(x-c)^{n+1} + C$$

Both operations preserve the radius of convergence.

## Standard Power Series

| Function | Power series (about $c=0$) | Radius |
|---|---|---|
| $e^x$ | $\sum_{n=0}^\infty \frac{x^n}{n!}$ | $\infty$ |
| $\sin x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | $\infty$ |
| $\cos x$ | $\sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}$ | $\infty$ |
| $\ln(1+x)$ | $\sum_{n=1}^\infty \frac{(-1)^{n+1} x^n}{n}$ | $1$ |
| $\frac{1}{1-x}$ | $\sum_{n=0}^\infty x^n$ | $1$ |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $a_n$ | coefficient of the $n$-th term |
| $c$ | centre of the power series |
| $R$ | radius of convergence |
| Interval of convergence | the set of $x$ for which the series converges; $|x-c| < R$ with endpoints checked separately |
| $\limsup$ | limit superior — the largest accumulation point of a sequence |
| Converges absolutely | the series $\sum |a_n(x-c)^n|$ converges |
| Ratio test | compares successive term sizes to find $R$ |
| Root test (Hadamard) | uses $|a_n|^{1/n}$ to find $R$ |
| Term-by-term differentiation | differentiating each term of the series independently |
| $n!$ | $n$ factorial: $n! = 1 \cdot 2 \cdots n$ |
| Analytic function | a function representable by a convergent power series near every point |
