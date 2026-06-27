---
title: Fractals & Self-Similarity
tag: dynamical-systems
summary: A fractal is a set with fine structure at all scales and a non-integer Hausdorff dimension; self-similar fractals are fixed points of iterated function systems and arise naturally in dynamical systems.
links:
  - hausdorff-dimension
  - julia-mandelbrot
  - iterated-function-systems
  - chaos
  - logistic-map
---

# Fractals & Self-Similarity

A **fractal** is a geometric object exhibiting **self-similarity**: it looks like copies of itself at every scale. Unlike smooth curves or surfaces, fractals have a **non-integer Hausdorff dimension** that quantifies how they fill space in a way intermediate between a line and a surface. The concept was systematised by Benoit Mandelbrot (1977), who argued that fractal geometry is the true geometry of nature: coastlines, clouds, trees, snowflakes, and blood vessels all display fractal structure. In mathematics, fractals arise as **limit sets** of dynamical systems (Julia sets, the Lorenz attractor), as **Cantor-like sets** in number theory, and as the self-similar fixed points of **iterated function systems**.

## Self-Similarity

A set $F \subset \mathbb{R}^n$ is **self-similar** if it is the union of scaled copies of itself:
$$F = \bigcup_{i=1}^N f_i(F)$$
where each $f_i$ is a contraction (e.g., a scaled rotation or reflection). The **similarity dimension** $d$ satisfies:
$$\sum_{i=1}^N r_i^d = 1$$
where $r_i = \mathrm{Lip}(f_i)$ is the contraction ratio.

## Examples

| Fractal | Dimension |
|---|---|
| Cantor set | $\log 2 / \log 3 \approx 0.631$ |
| Sierpiński triangle | $\log 3 / \log 2 \approx 1.585$ |
| Koch snowflake curve | $\log 4 / \log 3 \approx 1.262$ |
| Mandelbrot set boundary | $\approx 2$ |

## Cantor Set

Remove the middle third of $[0,1]$ and repeat: the Cantor set $C$ has Lebesgue measure 0, is uncountable, and has Hausdorff dimension $\log 2/\log 3$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Fractal | self-similar set with non-integer Hausdorff dimension |
| Self-similarity | set is union of scaled copies of itself |
| Hausdorff dimension $d_H$ | generalises dimension; can be non-integer |
| Similarity dimension | solution to $\sum r_i^d = 1$ for IFS |
| Contraction ratio $r_i$ | Lipschitz constant of $f_i$; $r_i < 1$ |
| Cantor set | $[0,1]$ with middle thirds removed; dim $= \log 2/\log 3$ |
| Sierpiński triangle | self-similar triangle; dim $= \log 3/\log 2$ |
| Koch curve | snowflake curve; dim $= \log 4/\log 3$ |
| IFS (iterated function system) | finite set of contractions whose attractor is a fractal |
| Mandelbrot set | set of $c \in \mathbb{C}$ for which $0$ does not escape under $z\mapsto z^2+c$ |
