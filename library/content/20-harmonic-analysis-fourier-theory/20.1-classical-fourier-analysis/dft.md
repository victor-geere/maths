---
title: Discrete Fourier Transform (DFT)
tag: harmonic-analysis
summary: The DFT converts a finite sequence of N complex numbers into N frequency components via a matrix multiplication by the N×N DFT matrix; it is the discrete analogue of the Fourier series and computed efficiently by the FFT.
links:
  - fft
  - fourier-series
  - fourier-transform
  - convolution-theorem
---

# Discrete Fourier Transform (DFT)

The **Discrete Fourier Transform (DFT)** of a sequence $x_0, x_1, \ldots, x_{N-1} \in \mathbb{C}$ is the sequence $X_0, X_1, \ldots, X_{N-1}$ defined by:
$$X_k = \sum_{n=0}^{N-1} x_n\,\omega_N^{-kn}, \quad \omega_N = e^{2\pi i/N}, \quad k = 0,\ldots, N-1$$
It is the exact discrete analogue of the Fourier series: just as the Fourier series decomposes a periodic function into complex exponentials, the DFT decomposes a periodic discrete signal into $N$ complex exponentials with frequencies $k/N$. The DFT is a **unitary** transformation (up to scaling), satisfying the discrete Parseval's theorem. It can be represented as multiplication by the $N \times N$ DFT matrix $F_N$, but is computed far more efficiently (in $O(N \log N)$ operations) via the Fast Fourier Transform.

## Definition

Let $\omega_N = e^{2\pi i/N}$. For $x = (x_0, \ldots, x_{N-1})$:
$$X_k = \sum_{n=0}^{N-1} x_n\,\omega_N^{-nk}, \quad k = 0, \ldots, N-1$$

**Inverse DFT**: $x_n = \frac{1}{N}\sum_{k=0}^{N-1} X_k\,\omega_N^{nk}$.

## DFT Matrix

$X = F_N x$ where $(F_N)_{kn} = \omega_N^{-kn}$. $F_N$ is unitary (up to $1/\sqrt{N}$): $F_N^* F_N = N I$.

## Discrete Parseval

$$\sum_{n=0}^{N-1} |x_n|^2 = \frac{1}{N}\sum_{k=0}^{N-1}|X_k|^2$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\omega_N = e^{2\pi i/N}$ | primitive $N$-th root of unity |
| $X_k$ | $k$-th DFT coefficient; amplitude of frequency $k/N$ |
| DFT matrix $F_N$ | $(k,n)$-entry is $\omega_N^{-kn}$ |
| Inverse DFT | $x_n = \frac{1}{N}\sum_k X_k\omega_N^{nk}$ |
| Discrete Parseval | $\sum|x_n|^2 = \frac{1}{N}\sum|X_k|^2$ |
| Circular convolution | $(x * y)_n = \sum_{k} x_k y_{n-k \bmod N}$; DFT converts to product |
| Nyquist frequency | $N/2$; highest meaningful frequency in DFT of real signal |
| Zero-padding | append zeros to $x$ to increase frequency resolution |
| Spectral leakage | artifact from non-integer number of periods in window |
