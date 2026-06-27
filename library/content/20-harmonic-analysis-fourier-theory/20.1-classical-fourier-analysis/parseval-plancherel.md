---
title: Parseval's & Plancherel's Theorems
tag: harmonic-analysis
summary: Parseval's theorem equates the L² norm of a function with the L² norm of its Fourier coefficients; Plancherel's theorem is the continuous analogue, showing the Fourier transform is a unitary isomorphism on L²(ℝ).
links:
  - fourier-series
  - fourier-transform
  - convolution-theorem
  - hilbert-spaces
---

# Parseval's & Plancherel's Theorems

**Parseval's theorem** (for Fourier series) and **Plancherel's theorem** (for the Fourier transform on $\mathbb{R}$) are energy-conservation statements: the total "energy" $\|f\|_2^2$ of a signal equals the sum/integral of the squared magnitudes of its frequency components. These theorems establish that the Fourier transform and Fourier series are **unitary** operations on $L^2$ spaces — they preserve inner products and norms. This is the precise mathematical statement of the physical principle that Fourier analysis decomposes energy into frequencies without loss. Both results follow from the completeness of the orthonormal system $\{e^{in\theta}\}$ in $L^2(\mathbb{T})$ and the unitarity of the Fourier transform on $L^2(\mathbb{R})$.

## Parseval's Theorem (Fourier Series)

For $f \in L^2(\mathbb{T})$ with Fourier coefficients $\hat{f}(n) = \frac{1}{2\pi}\int_0^{2\pi} f(\theta)e^{-in\theta}\,d\theta$:

$$\|f\|_{L^2(\mathbb{T})}^2 = \sum_{n=-\infty}^\infty |\hat{f}(n)|^2$$

More generally (Parseval's identity):
$$\langle f, g \rangle = \sum_{n \in \mathbb{Z}} \hat{f}(n)\overline{\hat{g}(n)}$$

## Plancherel's Theorem (Fourier Transform)

For $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$, the Fourier transform extends to a **unitary isomorphism** $\mathcal{F}: L^2(\mathbb{R}) \to L^2(\mathbb{R})$:
$$\|\hat{f}\|_{L^2(\mathbb{R})} = \|f\|_{L^2(\mathbb{R})}$$

$$\langle \hat{f}, \hat{g}\rangle_{L^2(\mathbb{R})} = \langle f, g \rangle_{L^2(\mathbb{R})}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\hat{f}(n)$ | $n$-th Fourier coefficient of $f \in L^2(\mathbb{T})$ |
| $\|f\|_2^2 = \int |f|^2$ | $L^2$-norm squared (energy) |
| Parseval's theorem | $\|f\|_2^2 = \sum_n |\hat{f}(n)|^2$ (Fourier series) |
| Plancherel's theorem | $\|\hat{f}\|_2 = \|f\|_2$ (Fourier transform on $\mathbb{R}$) |
| Unitary operator | isometric isomorphism of Hilbert spaces |
| $\langle f,g\rangle = \int f\bar{g}$ | $L^2$ inner product |
| Completeness of $\{e^{in\theta}\}$ | every $f \in L^2(\mathbb{T})$ expanded in Fourier series |
| Energy conservation | Fourier transform preserves total energy |
| Isometry | $\|\mathcal{F}f\| = \|f\|$; norm-preserving |
