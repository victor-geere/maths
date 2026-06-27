---
title: Fast Fourier Transform (FFT)
tag: harmonic-analysis
summary: The FFT computes the N-point DFT in O(N log N) operations rather than O(N²) by recursively splitting the DFT into smaller DFTs; it is one of the most important algorithms in science and engineering.
links:
  - dft
  - convolution-theorem
  - fourier-transform
---

# Fast Fourier Transform (FFT)

The **Fast Fourier Transform (FFT)** is an algorithm that computes the $N$-point DFT in $O(N \log N)$ operations, compared to $O(N^2)$ for the naive matrix multiplication. The key idea (Cooley–Tukey, 1965, though known to Gauss) is to recursively split an $N$-point DFT (when $N = 2^m$) into two $N/2$-point DFTs using the **butterfly** operation. The resulting divide-and-conquer recursion gives $T(N) = 2T(N/2) + O(N)$, solving to $T(N) = O(N \log N)$. The FFT is one of the most important algorithms ever discovered, enabling real-time digital signal processing, fast polynomial multiplication, fast convolution, and large-integer multiplication.

## Cooley–Tukey Radix-2 FFT

For $N = 2^m$, split $x$ into even and odd indexed subsequences:
$$X_k = \sum_{n=0}^{N/2-1} x_{2n}\,\omega_N^{-2nk} + \omega_N^{-k}\sum_{n=0}^{N/2-1} x_{2n+1}\,\omega_N^{-2nk}$$
$$= E_k + \omega_N^{-k}\,O_k$$

where $E_k$ (resp. $O_k$) is the $k$-th DFT of the even (resp. odd) subsequence, and $\omega_N^{-2} = \omega_{N/2}$.

**Butterfly**: $X_k = E_k + \omega_N^{-k}O_k$, $X_{k+N/2} = E_k - \omega_N^{-k}O_k$.

## Complexity

$T(N) = 2T(N/2) + O(N)$ gives $T(N) = O(N\log_2 N)$.

For $N = 2^{20} \approx 10^6$: FFT needs $\sim 2\times10^7$ ops vs $10^{12}$ for naive — a factor of $50{,}000$.

## Applications

Fast polynomial multiplication, fast integer multiplication (Schönhage–Strassen), convolution, spectral analysis, JPEG/MP3 compression, radar, MRI.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $N = 2^m$ | FFT works most simply for power-of-2 sizes |
| $E_k, O_k$ | DFTs of even and odd halves |
| Butterfly operation | $X_k = E_k + W^k O_k$, $X_{k+N/2} = E_k - W^k O_k$ |
| $W = \omega_N^{-1} = e^{-2\pi i/N}$ | twiddle factor |
| Radix-2 | split into 2 sub-problems |
| Twiddle factor $\omega_N^{-k}$ | phase factor in butterfly |
| Bit-reversal permutation | reordering of input needed for in-place FFT |
| $O(N\log N)$ | FFT complexity |
| Fast polynomial mult | $(p\cdot q)(x) = \mathrm{IFFT}(\mathrm{FFT}(p)\cdot\mathrm{FFT}(q))$ |
