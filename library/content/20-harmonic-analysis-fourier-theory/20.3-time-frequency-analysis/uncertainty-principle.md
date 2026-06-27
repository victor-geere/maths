---
title: Uncertainty Principle (Heisenberg)
tag: harmonic-analysis
summary: The Heisenberg uncertainty principle states that a function and its Fourier transform cannot both be arbitrarily concentrated; the product of their effective widths is bounded below by 1/(4π).
links:
  - fourier-transform
  - parseval-plancherel
  - stft
  - wavelets
---

# Uncertainty Principle (Heisenberg)

The **Heisenberg uncertainty principle** in harmonic analysis states that a nonzero function $f \in L^2(\mathbb{R})$ and its Fourier transform $\hat{f}$ cannot both be sharply concentrated. The precise statement: $\Delta_x(f) \cdot \Delta_\xi(f) \geq \frac{1}{4\pi}$, where $\Delta_x$ and $\Delta_\xi$ measure the spread of $f$ in time and frequency respectively. In quantum mechanics this is Heisenberg's uncertainty principle for position and momentum: $\sigma_x \sigma_p \geq \hbar/2$. The mathematical version is an exact inequality, with equality achieved only by Gaussian functions $f(x) = Ce^{-\pi\alpha x^2}$ (which are also eigenfunctions of the Fourier transform). The principle governs all time-frequency analysis: it explains why the STFT cannot achieve arbitrarily good resolution in both time and frequency simultaneously.

## Uncertainty Inequality

Define the **time spread** around $x_0 = \int x|f(x)|^2\,dx/\|f\|_2^2$:
$$\Delta_x(f)^2 = \frac{\int (x - x_0)^2|f(x)|^2\,dx}{\|f\|_2^2}$$

and similarly $\Delta_\xi(f)$ using $\hat{f}$.

**Theorem**: For $0 \neq f \in L^2(\mathbb{R})$:
$$\Delta_x(f) \cdot \Delta_\xi(f) \geq \frac{1}{4\pi}$$

Equality iff $f(x) = C e^{-\alpha(x-x_0)^2}e^{2\pi i\xi_0 x}$ for $\alpha > 0$.

## Proof (Sketch)

Use the Cauchy–Schwarz inequality on $\langle x f, f\rangle$ and $\langle \xi\hat{f},\hat{f}\rangle$, combined with the commutation relation $[x, -i\partial_x/(2\pi)]f = -if/(2\pi)$ (the canonical commutation relation).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\Delta_x(f)$ | RMS time spread: $\left(\frac{\int(x-x_0)^2|f|^2}{\|f\|_2^2}\right)^{1/2}$ |
| $\Delta_\xi(f)$ | RMS frequency spread |
| $\Delta_x \cdot \Delta_\xi \geq 1/(4\pi)$ | Heisenberg uncertainty inequality |
| Gaussian $e^{-\pi\alpha x^2}$ | achieves equality; its own Fourier transform (scaled) |
| Canonical commutation relation | $[x, -i\partial_x/(2\pi)] = -i/(2\pi)$; source of the bound |
| $\sigma_x\sigma_p \geq \hbar/2$ | quantum mechanics version |
| Time-bandwidth product | $\Delta t \cdot \Delta f \geq 1/(4\pi)$ |
| Gabor atom | Gaussian window STFT achieves minimum uncertainty |
| Wavepacket | spatially localised wave; subject to uncertainty bound |
