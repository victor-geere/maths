---
title: Julia Sets & Mandelbrot Set
tag: dynamical-systems
summary: Julia sets are the fractal boundaries of the filled Julia sets of complex polynomials z²+c; the Mandelbrot set parametrises which Julia sets are connected, and its boundary has Hausdorff dimension 2.
links:
  - fractals
  - hausdorff-dimension
  - iterated-maps
  - complex-numbers
  - chaos
---

# Julia Sets & Mandelbrot Set

The iteration of the simple complex quadratic $f_c(z) = z^2 + c$ for a parameter $c \in \mathbb{C}$ produces the most famous fractals in mathematics. The **Julia set** $J_c$ of $f_c$ is the boundary between initial points $z_0$ whose orbits remain bounded and those that escape to infinity. It is a fractal that can be a connected, intricate curve (when $0$ does not escape) or a totally disconnected Cantor-like dust (when $0$ escapes). The **Mandelbrot set** $\mathcal{M}$ is the set of parameters $c$ for which $J_c$ is connected, equivalently for which $0$ does not escape under $f_c$. Its boundary has Hausdorff dimension $2$ (Shishikura, 1998) and contains infinitely many smaller copies of itself at every scale.

## Julia Sets

For $f_c(z) = z^2 + c$, the **filled Julia set** is:
$$K_c = \{z_0 \in \mathbb{C} : \text{orbit of }z_0\text{ is bounded}\}$$

The **Julia set** $J_c = \partial K_c$ (topological boundary).

- $c \in \mathcal{M}$: $J_c$ is connected.
- $c \notin \mathcal{M}$: $J_c$ is a Cantor set (totally disconnected).

## Mandelbrot Set

$$\mathcal{M} = \{c \in \mathbb{C} : f_c^n(0) \not\to \infty\}$$

Equivalently, $c \in \mathcal{M}$ iff the orbit of $0$ remains bounded. Key fact: $c \notin \mathcal{M}$ iff $|f_c^n(0)| > 2$ for some $n$ (escape criterion).

## Structure

- The main cardioid corresponds to $f_c$ having a stable fixed point.
- Bulbs of period $n$ correspond to stable $n$-cycles.
- **Mandelbrot's theorem (Douady–Hubbard)**: $\mathcal{M}$ is connected and simply connected.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f_c(z) = z^2 + c$ | complex quadratic map with parameter $c \in \mathbb{C}$ |
| Orbit of $z_0$ | sequence $z_0, f_c(z_0), f_c^2(z_0), \ldots$ |
| Filled Julia set $K_c$ | $\{z_0 : $ orbit bounded$\}$ |
| Julia set $J_c = \partial K_c$ | boundary of filled Julia set |
| Mandelbrot set $\mathcal{M}$ | $\{c : $ orbit of $0$ bounded$\}$ |
| Escape criterion | $|f_c^n(0)| > 2 \Rightarrow c \notin \mathcal{M}$ |
| Connected Julia set | $J_c$ connected $\Leftrightarrow c \in \mathcal{M}$ |
| Cantor dust | disconnected Julia set when $c \notin \mathcal{M}$ |
| Cardioid (main body) | $c = \frac{\mu}{2} - \frac{\mu^2}{4}$; stable fixed point region |
| Hausdorff dimension of $\partial\mathcal{M}$ | equals 2 (Shishikura 1998) |
