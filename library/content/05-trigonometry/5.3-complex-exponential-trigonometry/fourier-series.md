---
title: Fourier Series
tag: analysis
summary: Representing a periodic function as an infinite sum of sines and cosines weighted by Fourier coefficients.
links:
  - convergence
  - sin-cos-tan
  - pythagorean-identities
  - eulers-formula
---

# Fourier Series

A **Fourier series** expresses a periodic function as an infinite sum of simple oscillations — sines and cosines at integer multiples of the fundamental frequency. The idea, introduced by Joseph Fourier in 1807 in the context of heat conduction, revealed that almost any periodic signal can be decomposed into its frequency components. This decomposition is the mathematical foundation of signal processing, acoustics, image compression, quantum mechanics, and the solution of differential equations on bounded domains. The coefficients of the series — the **Fourier coefficients** — measure how much of each frequency is present in the function.

## Definition

For a function $f$ periodic with period $2L$, the Fourier series is:

$$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^\infty \left[a_n \cos\!\left(\frac{n\pi x}{L}\right) + b_n \sin\!\left(\frac{n\pi x}{L}\right)\right]$$

## Fourier Coefficients

$$a_0 = \frac{1}{L}\int_{-L}^{L} f(x)\, dx$$

$$a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos\!\left(\frac{n\pi x}{L}\right)dx, \quad n \geq 1$$

$$b_n = \frac{1}{L}\int_{-L}^{L} f(x)\sin\!\left(\frac{n\pi x}{L}\right)dx, \quad n \geq 1$$

## Orthogonality

The key property behind the formulas:

$$\int_{-L}^{L}\cos\!\left(\frac{m\pi x}{L}\right)\cos\!\left(\frac{n\pi x}{L}\right)dx = L\,\delta_{mn}, \qquad \int_{-L}^{L}\sin\!\left(\frac{m\pi x}{L}\right)\sin\!\left(\frac{n\pi x}{L}\right)dx = L\,\delta_{mn}$$

$$\int_{-L}^{L}\cos\!\left(\frac{m\pi x}{L}\right)\sin\!\left(\frac{n\pi x}{L}\right)dx = 0 \quad \text{for all } m, n$$

## Complex Form

Using $e^{in\pi x/L} = \cos(n\pi x/L) + i\sin(n\pi x/L)$:

$$f(x) \sim \sum_{n=-\infty}^{\infty} c_n\, e^{in\pi x/L}, \qquad c_n = \frac{1}{2L}\int_{-L}^{L} f(x)\, e^{-in\pi x/L}\,dx$$

## Convergence (Dirichlet Conditions)

The Fourier series converges to $f(x)$ wherever $f$ is continuous. At a jump discontinuity, it converges to the **average** of the left and right limits.

## Parseval's Theorem

$$\frac{1}{L}\int_{-L}^{L}|f(x)|^2\, dx = \frac{a_0^2}{2} + \sum_{n=1}^\infty (a_n^2 + b_n^2)$$

Total energy of $f$ equals the sum of squared amplitudes of its frequency components.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $a_0, a_n, b_n$ | Fourier coefficients (amplitudes of each frequency component) |
| $c_n$ | complex Fourier coefficient |
| $n$ | harmonic number (integer multiple of the fundamental frequency) |
| $L$ | half the period; the function repeats every $2L$ |
| $\sim$ | "has Fourier series" (convergence is a separate question) |
| Fundamental frequency | $1/(2L)$ — the lowest frequency in the series |
| Harmonic | a frequency that is an integer multiple of the fundamental |
| Orthogonality | two functions are orthogonal if their product integrates to zero |
| $\delta_{mn}$ | Kronecker delta: 1 if $m=n$, 0 otherwise |
| Jump discontinuity | a point where $f$ has a finite jump; series converges to the midpoint |
| Parseval's theorem | energy equality: $\|f\|^2 = \sum |c_n|^2$ |
| Dirichlet conditions | sufficient conditions for the Fourier series to converge pointwise |
| $e^{in\pi x/L}$ | complex exponential basis function |
