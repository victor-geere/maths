---
title: Z-Transform
tag: harmonic-analysis
summary: The Z-transform maps a discrete-time sequence x[n] to a function X(z) of a complex variable z; it is the discrete analogue of the Laplace transform and is the primary tool for analysing digital filters and difference equations.
links:
  - dft
  - laplace-transform
  - convolution-theorem
  - fourier-transform
---

# Z-Transform

The **Z-transform** of a discrete sequence $x[n]$ is:
$$X(z) = \sum_{n=-\infty}^\infty x[n]\,z^{-n}$$
for complex $z$ in a region of convergence. It is the discrete analogue of the Laplace transform and the fundamental tool for analysing **discrete-time linear systems** and **digital filters**. Just as the Laplace transform converts differential equations into algebraic equations, the Z-transform converts difference equations into polynomial equations in $z$. Evaluating $X(z)$ on the unit circle $z = e^{i\omega}$ gives the **discrete-time Fourier transform (DTFT)**: $X(e^{i\omega}) = \sum_n x[n]e^{-i\omega n}$, the frequency response of the sequence.

## Definition & Region of Convergence

$$X(z) = \mathcal{Z}\{x[n]\} = \sum_{n=-\infty}^{\infty} x[n]\,z^{-n}$$

The **region of convergence (ROC)** is the set of $z \in \mathbb{C}$ for which the series converges absolutely.

## Key Properties

| Property | Formula |
|---|---|
| Linearity | $\mathcal{Z}\{ax+by\} = aX + bY$ |
| Time shift | $\mathcal{Z}\{x[n-k]\} = z^{-k}X(z)$ |
| Convolution | $\mathcal{Z}\{x*y\} = X(z)Y(z)$ |
| Initial value | $x[0] = \lim_{z\to\infty} X(z)$ |

## Transfer Function

For a digital filter with difference equation $y[n] = \sum_k b_k x[n-k] - \sum_k a_k y[n-k]$, the **transfer function** is:
$$H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_k b_k z^{-k}}{1 + \sum_k a_k z^{-k}}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $X(z) = \sum_n x[n]z^{-n}$ | Z-transform |
| Region of convergence (ROC) | set of $z$ where series converges |
| Unit circle $|z|=1$ | evaluating there gives DTFT |
| $z^{-1}$ | unit delay operator in Z-domain |
| Transfer function $H(z)$ | $Y(z)/X(z)$; characterises a linear filter |
| Poles of $H(z)$ | zeros of denominator; determine stability |
| FIR filter | finite impulse response; $H(z)$ is a polynomial |
| IIR filter | infinite impulse response; $H(z)$ is a rational function |
| DTFT | discrete-time Fourier transform: $X(e^{i\omega})$ |
| Inverse Z-transform | $x[n] = \frac{1}{2\pi i}\oint X(z)z^{n-1}\,dz$ |
