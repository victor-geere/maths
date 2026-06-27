---
title: Convolution Theorem
tag: harmonic-analysis
summary: The convolution theorem states that the Fourier transform converts convolution to pointwise multiplication, making it the key tool for signal filtering, differential equations, and probability (sums of independent random variables).
links:
  - fourier-transform
  - fourier-series
  - parseval-plancherel
  - dirichlet-fejer-kernels
---

# Convolution Theorem

The **convolution theorem** states that the Fourier transform converts the convolution of two functions into the pointwise product of their Fourier transforms: $\widehat{f * g} = \hat{f} \cdot \hat{g}$. This is one of the most useful facts in analysis and engineering. In signal processing, filtering a signal $f$ by a filter $g$ is exactly convolution $f * g$, and the convolution theorem reduces this to multiplication in frequency space — which is fast and transparent. In probability, the distribution of a sum $X + Y$ of independent random variables is the convolution of their densities, so the characteristic function of $X + Y$ is the product of the characteristic functions of $X$ and $Y$, making it easy to study sums. The theorem also underlies the fast Fourier transform's efficiency.

## Definition of Convolution

For $f, g \in L^1(\mathbb{R})$:
$$(f * g)(x) = \int_{-\infty}^\infty f(y)\,g(x-y)\,dy$$

On the circle $\mathbb{T}$:
$$(f * g)(\theta) = \frac{1}{2\pi}\int_0^{2\pi} f(\phi)\,g(\theta - \phi)\,d\phi$$

## Convolution Theorem

$$\widehat{f * g}(\xi) = \hat{f}(\xi)\cdot\hat{g}(\xi)$$

Conversely, multiplication becomes convolution: $\widehat{f \cdot g} = \hat{f} * \hat{g}$.

## Applications

- **Filtering**: output $= h * x$ where $h$ is the impulse response; $\hat{h}$ is the frequency response.
- **PDEs**: solve $u' + au = f$ via $\hat{u}(\xi) = \hat{f}(\xi)/(2\pi i \xi + a)$, then invert.
- **Probability**: $\varphi_{X+Y} = \varphi_X \cdot \varphi_Y$ for independent $X,Y$ (characteristic functions).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $(f*g)(x)$ | convolution: $\int f(y)g(x-y)\,dy$ |
| Convolution theorem | $\widehat{f*g} = \hat{f}\cdot\hat{g}$ |
| Impulse response $h$ | output when input is a Dirac delta $\delta$; defines a filter |
| Frequency response $\hat{h}(\xi)$ | how filter attenuates each frequency $\xi$ |
| Characteristic function $\varphi_X$ | $\mathbb{E}[e^{it X}]$; Fourier transform of distribution |
| $\varphi_{X+Y} = \varphi_X\cdot\varphi_Y$ | independence $\Rightarrow$ convolution of densities |
| Low-pass filter | $\hat{h} = \mathbf{1}_{|\xi| \leq B}$; removes high frequencies |
| Commutativity | $f * g = g * f$ |
| Associativity | $(f*g)*h = f*(g*h)$ |
