---
title: Big-O Notation
tag: algorithms
summary: Asymptotic notation for describing the growth rate of functions — O, Ω, Θ, o, ω — the language for comparing algorithm efficiency.
links:
  - master-theorem
  - recurrence-relations
  - prime-counting
---

# Big-O Notation

**Big-O notation** is the mathematical language for comparing the growth rates of functions, used universally in computer science to describe algorithm efficiency. When we say an algorithm runs in $O(n^2)$ time, we mean its running time grows no faster than a constant multiple of $n^2$ for large $n$ — the constant and lower-order terms don't matter asymptotically. The full family of asymptotic notations ($O$, $\Omega$, $\Theta$, $o$, $\omega$) provides upper bounds, lower bounds, and tight bounds on growth rates, allowing precise comparisons between algorithms without specifying machine-dependent constants.

## Formal Definitions

Let $f, g : \mathbb{N} \to \mathbb{R}_{>0}$.

| Notation | Definition | Meaning |
|---|---|---|
| $f = O(g)$ | $\exists\, C > 0, N : n \geq N \Rightarrow f(n) \leq C\,g(n)$ | $f$ grows **at most** as fast as $g$ |
| $f = \Omega(g)$ | $\exists\, c > 0, N : n \geq N \Rightarrow f(n) \geq c\,g(n)$ | $f$ grows **at least** as fast as $g$ |
| $f = \Theta(g)$ | $f = O(g)$ and $f = \Omega(g)$ | $f$ and $g$ grow at the **same rate** |
| $f = o(g)$ | $\lim_{n\to\infty} f(n)/g(n) = 0$ | $f$ grows **strictly slower** than $g$ |
| $f = \omega(g)$ | $\lim_{n\to\infty} f(n)/g(n) = \infty$ | $f$ grows **strictly faster** than $g$ |

## Hierarchy of Common Growth Rates

$$O(1) \subset O(\log n) \subset O(n) \subset O(n\log n) \subset O(n^2) \subset O(n^3) \subset O(2^n) \subset O(n!)$$

## Rules

- **Constant factors:** $O(c\,f(n)) = O(f(n))$
- **Sum rule:** $O(f) + O(g) = O(\max(f,g))$
- **Product rule:** $O(f)\cdot O(g) = O(f \cdot g)$
- **Transitivity:** $f = O(g)$ and $g = O(h) \Rightarrow f = O(h)$

## Common Algorithm Complexities

| Complexity | Algorithm examples |
|---|---|
| $O(1)$ | Hash table lookup, array access |
| $O(\log n)$ | Binary search, balanced BST lookup |
| $O(n)$ | Linear scan, BFS/DFS |
| $O(n \log n)$ | Merge sort, heapsort |
| $O(n^2)$ | Bubble sort, naive matrix-vector |
| $O(n^3)$ | Naive matrix multiplication |
| $O(2^n)$ | Brute-force subset enumeration |
| $O(n!)$ | Brute-force permutation enumeration |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $O(g(n))$ | big-O: upper bound on growth rate |
| $\Omega(g(n))$ | big-Omega: lower bound on growth rate |
| $\Theta(g(n))$ | big-Theta: tight (both upper and lower) bound |
| $o(g(n))$ | little-o: strictly slower growth |
| $\omega(g(n))$ | little-omega: strictly faster growth |
| Asymptotic | behaviour as $n \to \infty$ |
| $C, c$ | positive constants in the definitions |
| $N$ | threshold beyond which the bound holds |
| $\log n$ | typically $\log_2 n$ in CS contexts |
| Worst-case complexity | the maximum running time over all inputs of size $n$ |
| Average-case complexity | expected running time over a distribution of inputs |
