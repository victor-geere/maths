---
title: Fourier Transform on ℝ
tag: harmonic-analysis
summary: The Fourier transform decomposes a function on ℝ into its frequency components via an integral; it is a unitary isomorphism on L²(ℝ) that converts differentiation to multiplication and convolution to pointwise product.
links:
  - parseval-plancherel
  - convolution-theorem
  - fourier-series
  - laplace-transform
---

# Fourier Transform on ℝ

The **Fourier transform** converts a function $f: \mathbb{R} \to \mathbb{C}$ into its **frequency representation** $\hat{f}: \mathbb{R} \to \mathbb{C}$, with $\hat{f}(\xi)$ measuring the amplitude and phase of frequency $\xi$ in $f$. For $f \in L^1(\mathbb{R})$:
$$\hat{f}(\xi) = \int_{-\infty}^\infty f(x)\,e^{-2\pi i \xi x}\,dx$$
The Fourier transform extends to a **unitary isomorphism** of $L^2(\mathbb{R})$ onto itself (Plancherel theorem), converts differentiation into multiplication by $2\pi i\xi$, and converts convolution into pointwise product. It is the central tool of signal processing, quantum mechanics (momentum representation), and PDE theory (where constant-coefficient PDEs become algebraic equations in frequency space).

## Definition & Inversion

For $f \in L^1(\mathbb{R})$:
$$\hat{f}(\xi) = \mathcal{F}[f](\xi) = \int_{\mathbb{R}} f(x)\,e^{-2\pi i \xi x}\,dx$$

**Inversion formula**: $f(x) = \int_{\mathbb{R}} \hat{f}(\xi)\,e^{2\pi i \xi x}\,d\xi$ (when $\hat{f} \in L^1$).

## Key Properties

| Property | Formula |
|---|---|
| Linearity | $\widehat{af+bg} = a\hat{f} + b\hat{g}$ |
| Translation | $\widehat{f(\cdot - a)}(\xi) = e^{-2\pi i a\xi}\hat{f}(\xi)$ |
| Modulation | $\widehat{e^{2\pi i b\cdot}f}(\xi) = \hat{f}(\xi - b)$ |
| Differentiation | $\widehat{f'}(\xi) = 2\pi i\xi\,\hat{f}(\xi)$ |
| Convolution | $\widehat{f*g} = \hat{f}\cdot\hat{g}$ |
| Scaling | $\widehat{f(a\cdot)}(\xi) = \frac{1}{|a|}\hat{f}(\xi/a)$ |
| Gaussian | $\hat{g}(\xi) = g(\xi)$ where $g(x) = e^{-\pi x^2}$ |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\hat{f}(\xi)$ | Fourier transform of $f$ at frequency $\xi$ |
| $\xi$ | frequency variable (dual to position $x$) |
| $e^{-2\pi i\xi x}$ | Fourier kernel; complex exponential |
| Inversion formula | recovers $f$ from $\hat{f}$ |
| $L^1(\mathbb{R})$ | absolutely integrable functions |
| $L^2(\mathbb{R})$ | square-integrable; Fourier transform is unitary here |
| Plancherel theorem | $\|\hat{f}\|_2 = \|f\|_2$; FT is $L^2$-isometry |
| Schwartz class $\mathcal{S}$ | smooth rapidly decaying functions; FT maps $\mathcal{S}$ to $\mathcal{S}$ |
| Tempered distribution | dual of $\mathcal{S}$; FT extends here |
| Convolution theorem | $\widehat{f*g} = \hat{f}\cdot\hat{g}$ |
