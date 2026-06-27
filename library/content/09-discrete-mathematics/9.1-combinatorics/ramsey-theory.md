---
title: Ramsey Theory
tag: discrete
summary: The study of inevitable structure in large enough combinatorial objects — complete disorder is impossible at sufficient scale.
links:
  - pigeonhole
  - combinations
  - graphs-basics
---

# Ramsey Theory

**Ramsey theory** studies a profound phenomenon: in any sufficiently large combinatorial structure, some kind of order must appear — complete disorder is impossible above a critical scale. The canonical example is Ramsey's theorem: for any $r, s$, there is a number $R(r,s)$ such that any 2-colouring of the edges of the complete graph $K_N$ (with $N \geq R(r,s)$) must contain either a red $K_r$ or a blue $K_s$. The theory, initiated by Frank Ramsey in 1928, has deep connections to logic, number theory, and combinatorics, and computing the exact Ramsey numbers is famously difficult — the problem is "more an embarrassment than a challenge" in the words of Erdős.

## Ramsey Numbers

$R(r, s)$ is the smallest $N$ such that every 2-colouring of the edges of $K_N$ contains either a red complete subgraph $K_r$ or a blue complete subgraph $K_s$.

**Known values:**

| $(r, s)$ | $R(r, s)$ |
|---|---|
| $(3, 3)$ | 6 |
| $(3, 4)$ | 9 |
| $(3, 5)$ | 14 |
| $(4, 4)$ | 18 |
| $(3, 6)$ | 18 |

$R(5, 5)$ is unknown; only $43 \leq R(5,5) \leq 48$ is currently established.

## Diagonal Bounds (Erdős–Szekeres)

$$R(r, s) \leq \binom{r+s-2}{r-1}$$

In particular, $R(r,r) \leq \binom{2r-2}{r-1} \leq 4^r$.

Lower bound (probabilistic): $R(r, r) > 2^{r/2}$.

## Schur's Theorem

For any $k$-colouring of $\{1, \ldots, N\}$ (for sufficiently large $N$), there always exist $x, y, z$ of the same colour with $x + y = z$.

## Van der Waerden's Theorem

For any $k$ and $\ell$, there exists $W(k, \ell)$ such that any $k$-colouring of $\{1, \ldots, W(k,\ell)\}$ contains a monochromatic arithmetic progression of length $\ell$.

## Hales–Jewett Theorem

The combinatorial essence underlying many Ramsey-type results: for any $t$ and $k$, there is a dimension $n$ such that any $k$-colouring of the $n$-dimensional hypercube $[t]^n$ contains a monochromatic combinatorial line.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $R(r, s)$ | Ramsey number: minimum $N$ to guarantee red $K_r$ or blue $K_s$ in any 2-colouring of $K_N$ |
| $K_n$ | complete graph on $n$ vertices (every pair connected) |
| 2-colouring of edges | each edge coloured red or blue |
| Monochromatic | all edges/elements of the same colour |
| Diagonal Ramsey number | $R(r,r)$: both colours are the same size |
| Schur's theorem | monochromatic solution to $x+y=z$ exists in large enough coloured $\mathbb{N}$ |
| Van der Waerden's theorem | monochromatic arithmetic progressions must appear |
| Arithmetic progression | $a, a+d, a+2d, \ldots$ for fixed $a$ and common difference $d$ |
| Hales–Jewett theorem | combinatorial line exists in any coloured high-dimensional grid |
| Probabilistic method | proving existence by showing a random object has the desired property with positive probability |
