---
title: Short-Time Fourier Transform
tag: harmonic-analysis
summary: The STFT analyses a signal's frequency content locally in time by computing Fourier transforms of windowed segments; it produces a spectrogram showing how spectral content evolves.
links:
  - fourier-transform
  - uncertainty-principle
  - wavelets
  - wavelet-transform
---

# Short-Time Fourier Transform

The **Short-Time Fourier Transform (STFT)** analyses the frequency content of a signal as it evolves in time. It multiplies the signal $f$ by a sliding window function $g(x - b)$ (localising around time $b$) and takes the Fourier transform of the windowed segment:
$$(\mathrm{STFT}_g f)(b, \xi) = \int_{-\infty}^\infty f(x)\,\overline{g(x-b)}\,e^{-2\pi i \xi x}\,dx$$
The result is a function of both time $b$ and frequency $\xi$, giving a **time-frequency representation**. The squared magnitude $|\mathrm{STFT}_g f(b,\xi)|^2$ is the **spectrogram**, visualising how the signal's spectral energy is distributed across time and frequency. The fundamental limitation is the **Heisenberg uncertainty principle**: narrow windows give good time resolution but poor frequency resolution, and vice versa.

## Definition

Let $g \in L^2(\mathbb{R})$ be a window function (e.g., Gaussian or Hann window). The STFT is:
$$(V_g f)(b, \xi) = \langle f, M_\xi T_b g \rangle = \int f(x)\overline{g(x-b)}e^{-2\pi i\xi x}\,dx$$

where $T_b g(x) = g(x-b)$ (translation) and $M_\xi g(x) = e^{2\pi i\xi x}g(x)$ (modulation).

## Reconstruction (Inversion)

$$f(x) = \frac{1}{\|g\|^2}\int\int (V_g f)(b,\xi)\,g(x-b)\,e^{2\pi i\xi x}\,db\,d\xi$$

## Spectrogram

$$S_f(b,\xi) = |(V_g f)(b,\xi)|^2$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $g(x-b)$ | window function centred at time $b$ |
| $(V_g f)(b,\xi)$ | STFT: Fourier transform of $f$ in window around $b$ |
| Spectrogram $|V_g f|^2$ | time-frequency energy density |
| Time resolution | width of window $g$ in time |
| Frequency resolution | width of $\hat{g}$ in frequency |
| Uncertainty principle | $\Delta t \cdot \Delta\omega \geq 1/(4\pi)$ |
| $T_b g$ | translation: $g(\cdot - b)$ |
| $M_\xi g$ | modulation: $e^{2\pi i\xi\cdot}g$ |
| Gabor transform | STFT with Gaussian window $g = e^{-\pi x^2}$ |
| Wigner distribution | phase-space representation; not always non-negative |
