---
title: Wavelet Transform
tag: harmonic-analysis
summary: The wavelet transform decomposes a signal into time-frequency components at multiple scales using dilated/translated copies of a mother wavelet; it is an isometry on L²(ℝ) and the foundation of multiresolution analysis.
links:
  - wavelets
  - stft
  - frames-riesz-bases
  - uncertainty-principle
  - fourier-transform
---

# Wavelet Transform

The **wavelet transform** (continuous or discrete) decomposes a signal into components at multiple **scales** (frequencies) and **positions** (times) simultaneously, using scaled and translated copies of a **mother wavelet**. Unlike the STFT which uses a fixed window, the wavelet transform uses shorter windows at high frequencies and longer windows at low frequencies — automatically adapted to the signal's local structure. The **continuous wavelet transform (CWT)** is an isometry from $L^2(\mathbb{R})$ into $L^2(\mathbb{R}^+ \times \mathbb{R}, da\,db/a^2)$, and the **discrete wavelet transform (DWT)** using dyadic scales gives an orthonormal basis decomposition, efficiently computed by Mallat's pyramid algorithm in $O(N)$ operations (faster than FFT's $O(N\log N)$).

## Continuous Wavelet Transform

The CWT of $f \in L^2(\mathbb{R})$ with admissible mother wavelet $\psi$:
$$(W_\psi f)(a,b) = \langle f, \psi_{a,b}\rangle = \int f(x)\,\frac{1}{\sqrt{a}}\overline{\psi\!\left(\frac{x-b}{a}\right)}dx, \quad a > 0$$

**Isometry**: $\|W_\psi f\|_{L^2(da\,db/a^2)} = C_\psi^{1/2}\|f\|_{L^2}$.

## Discrete Wavelet Transform & Mallat Algorithm

For dyadic DWT, the **scaling function** $\phi$ and **mother wavelet** $\psi$ satisfy two-scale relations. The DWT computes approximate coefficients $c_j[k] = \langle f, \phi_{j,k}\rangle$ and detail coefficients $d_j[k] = \langle f, \psi_{j,k}\rangle$ by iterated filtering:
- **Analysis**: split into low-pass (scaling) and high-pass (wavelet) via filter banks, then downsample.
- **Synthesis**: upsample and recombine.

Complexity: $O(N)$ for $N$-point signal.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\psi_{a,b}$ | wavelet at scale $a$, position $b$: $a^{-1/2}\psi((x-b)/a)$ |
| $(W_\psi f)(a,b)$ | CWT coefficient at scale $a$, position $b$ |
| Admissibility $C_\psi < \infty$ | condition on $\psi$ ensuring invertibility |
| Scale $a$ | inversely related to frequency: $a \ll 1$ is high freq |
| DWT | discrete wavelet transform on dyadic grid |
| Scaling function $\phi$ | generates approximation spaces $V_j$ |
| Detail coefficients $d_j[k]$ | $\langle f, \psi_{j,k}\rangle$; wavelet coefficients at scale $j$ |
| Mallat algorithm | $O(N)$ filter-bank implementation of DWT |
| Low-pass filter $h$ | extracts scaling coefficients |
| High-pass filter $g$ | extracts wavelet / detail coefficients |
