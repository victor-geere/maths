---
title: Dirichlet & Fejér Kernels
tag: harmonic-analysis
summary: The Dirichlet kernel is the summation kernel for partial Fourier sums; the Fejér kernel is its Cesàro average and is an approximate identity, explaining why Cesàro means converge better than partial sums.
links:
  - fourier-series
  - parseval-plancherel
  - convolution-theorem
  - uniform-convergence
---

# Dirichlet & Fejér Kernels

The **Dirichlet kernel** $D_N$ and **Fejér kernel** $F_N$ are the convolution kernels controlling convergence of Fourier series on the circle $\mathbb{T} = [0, 2\pi)$. The $N$-th partial sum $S_N f = D_N * f$ is the convolution of $f$ with $D_N$; convergence of Fourier series is thus controlled by properties of $D_N$. The Dirichlet kernel has poor pointwise convergence properties (its $L^1$ norm grows as $\log N$), leading to the Gibbs phenomenon and even divergence for continuous $f$. The **Fejér kernel** $F_N = \frac{1}{N}\sum_{n=0}^{N-1} D_n$ is the arithmetic mean, and it is a genuine approximate identity ($F_N \geq 0$, $\|F_N\|_1 = 1$, concentrated near 0), ensuring that Cesàro means converge uniformly for continuous $f$.

## Dirichlet Kernel

$$D_N(\theta) = \sum_{n=-N}^{N} e^{in\theta} = \frac{\sin((N+\tfrac{1}{2})\theta)}{\sin(\tfrac{1}{2}\theta)}$$

The $N$-th partial Fourier sum: $S_N f(\theta) = (D_N * f)(\theta) = \frac{1}{2\pi}\int_0^{2\pi} f(\phi) D_N(\theta - \phi)\,d\phi$.

Properties: $\int D_N = 2\pi$, but $\|D_N\|_1 \sim \frac{4}{\pi^2}\log N \to \infty$ (not an approximate identity).

## Fejér Kernel

$$F_N(\theta) = \frac{1}{N}\sum_{n=0}^{N-1} D_n(\theta) = \frac{1}{N}\left(\frac{\sin(N\theta/2)}{\sin(\theta/2)}\right)^2$$

Properties: $F_N \geq 0$, $\|F_N\|_1 = 1$, $F_N \to 0$ uniformly on $[\delta, 2\pi-\delta]$ for any $\delta > 0$.

**Fejér's theorem**: For $f \in C(\mathbb{T})$, $\sigma_N f = F_N * f \to f$ uniformly.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbb{T}$ | circle group $[0,2\pi)$ or $\mathbb{R}/2\pi\mathbb{Z}$ |
| $D_N(\theta)$ | Dirichlet kernel: $\sum_{n=-N}^N e^{in\theta}$ |
| $S_N f$ | $N$-th partial Fourier sum: $D_N * f$ |
| $F_N(\theta)$ | Fejér kernel: $\frac{1}{N}\sum_{k=0}^{N-1}D_k(\theta)$ |
| $\sigma_N f$ | $N$-th Cesàro mean: $F_N * f$ |
| Approximate identity | $k_N \geq 0$, $\int k_N = 1$, concentrated near 0 |
| Gibbs phenomenon | overshoot of partial sums near a jump discontinuity |
| $\|D_N\|_1 \sim C\log N$ | $L^1$ norm of Dirichlet kernel grows logarithmically |
| Fejér's theorem | Cesàro means of Fourier series converge uniformly for $f \in C(\mathbb{T})$ |
| Convolution $f * g$ | $(f*g)(\theta) = \frac{1}{2\pi}\int f(\phi)g(\theta-\phi)\,d\phi$ |
