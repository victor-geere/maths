---
title: Wavelets
tag: harmonic-analysis
summary: Wavelets are functions obtained by dilating and translating a single mother wavelet; they form bases of L²(ℝ) that give simultaneous time-frequency localisation, overcoming the limitations of the Fourier transform.
links:
  - wavelet-transform
  - fourier-transform
  - frames-riesz-bases
  - uncertainty-principle
---

# Wavelets

**Wavelets** are rapidly decaying oscillating functions $\psi_{a,b}(x) = \frac{1}{\sqrt{a}}\psi\left(\frac{x-b}{a}\right)$ obtained by dilating (by $a > 0$) and translating (by $b \in \mathbb{R}$) a fixed **mother wavelet** $\psi$. Unlike Fourier exponentials (which have perfect frequency localisation but no time localisation), wavelets are **localised in both time and frequency**, satisfying the Heisenberg uncertainty bound. This makes them ideal for analysing signals with non-stationary features — transients, singularities, abrupt changes — and they form the basis of modern signal compression (JPEG 2000, FBI fingerprint database). An **orthonormal wavelet basis** (Daubechies, 1988) gives a complete orthonormal system $\{\psi_{j,k}\}_{j,k \in \mathbb{Z}}$ for $L^2(\mathbb{R})$ with compact support.

## Continuous Wavelet Transform

For a mother wavelet $\psi$ with $\int \psi = 0$ and $C_\psi = \int_0^\infty \frac{|\hat{\psi}(\xi)|^2}{\xi}\,d\xi < \infty$ (admissibility):
$$(Wf)(a,b) = \frac{1}{\sqrt{a}}\int_{-\infty}^\infty f(x)\overline{\psi\left(\frac{x-b}{a}\right)}\,dx$$

Inversion: $f(x) = \frac{1}{C_\psi}\int_0^\infty\int_{-\infty}^\infty (Wf)(a,b)\psi_{a,b}(x)\,\frac{db\,da}{a^2}$.

## Discrete Wavelet Basis

For dyadic scaling $a = 2^{-j}$, $b = k2^{-j}$:
$$\psi_{j,k}(x) = 2^{j/2}\psi(2^j x - k)$$

Under the **multiresolution analysis (MRA)** framework (Mallat), the $\{\psi_{j,k}\}$ form an orthonormal basis of $L^2(\mathbb{R})$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Mother wavelet $\psi$ | basic wavelet shape; $\int\psi = 0$ |
| $\psi_{a,b}(x) = a^{-1/2}\psi((x-b)/a)$ | dilated/translated wavelet |
| Scale $a$ | controls frequency: small $a$ = high frequency |
| Translation $b$ | controls time localisation |
| CWT $(Wf)(a,b)$ | continuous wavelet transform |
| Admissibility condition | $C_\psi < \infty$; ensures invertibility |
| Dyadic wavelet | $a = 2^{-j}$, $b = k2^{-j}$; discrete grid |
| MRA | multiresolution analysis; Mallat's framework |
| Daubechies wavelets | compactly supported orthonormal wavelets |
| JPEG 2000 | image compression using wavelets |
