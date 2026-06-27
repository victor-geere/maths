---
title: Catalan Numbers
tag: discrete
summary: A sequence 1, 1, 2, 5, 14, 42, … counting an extraordinary variety of combinatorial structures including valid parenthesisations, binary trees, and polygon triangulations.
links:
  - combinations
  - generating-functions
  - stirling-numbers
---

# Catalan Numbers

The **Catalan numbers** $C_0 = 1, C_1 = 1, C_2 = 2, C_3 = 5, C_4 = 14, C_5 = 42, \ldots$ are one of the most remarkable sequences in combinatorics. They arise in dozens of apparently unrelated counting problems: the number of ways to fully parenthesise a product of $n+1$ factors, the number of full binary trees with $n+1$ leaves, the number of monotone lattice paths that don't cross the diagonal, the number of triangulations of a convex $(n+2)$-gon, and many more. This "Catalan coincidence" is not accidental — all these problems share the same recursive structure, and the Catalan numbers are the unique solution to that recursion.

## Formula

$$C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)!\,n!}$$

## Recurrence

$$C_0 = 1, \qquad C_n = \sum_{k=0}^{n-1} C_k C_{n-1-k} \quad (n \geq 1)$$

This "convolution recurrence" reflects a first-return decomposition: split after the $k$-th step.

## Generating Function

The ordinary generating function $C(x) = \sum_{n=0}^\infty C_n x^n$ satisfies:

$$C(x) = 1 + x\,C(x)^2 \implies C(x) = \frac{1 - \sqrt{1-4x}}{2x}$$

## Values

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $C_n$ | 1 | 1 | 2 | 5 | 14 | 42 | 132 |

## Combinatorial Interpretations (all counted by $C_n$)

- Ways to parenthesise $n+1$ factors: $(ab)c$ vs $a(bc)$
- Full binary trees with $n+1$ leaves
- Triangulations of a convex $(n+2)$-gon
- Monotone lattice paths from $(0,0)$ to $(n,n)$ not going above the diagonal
- Stack-sortable permutations of $\{1,\ldots,n\}$ (avoiding $231$)
- Sequences $a_1, \ldots, a_{2n}$ of $n$ ones and $n$ negative-ones with all partial sums $\geq 0$

## Growth Rate

$$C_n \sim \frac{4^n}{n^{3/2}\sqrt{\pi}} \quad \text{as } n \to \infty$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $C_n$ | the $n$-th Catalan number: $\frac{1}{n+1}\binom{2n}{n}$ |
| $\binom{2n}{n}$ | central binomial coefficient |
| Recurrence | $C_n = \sum_{k=0}^{n-1}C_k C_{n-1-k}$ — convolution of earlier terms |
| Generating function $C(x)$ | satisfies $C(x) = 1 + xC(x)^2$ |
| Full binary tree | a tree where each internal node has exactly 2 children |
| Triangulation | division of a polygon into triangles by non-crossing diagonals |
| Lattice path | a path on $\mathbb{Z}^2$ using unit steps right and up |
| Monotone path | one using only right and up steps |
| Diagonal | the path from $(0,0)$ to $(n,n)$; Catalan paths stay below it |
| Pattern-avoiding permutation | avoids a specified sub-sequence order |
| $\sim$ | asymptotically equal: ratio tends to 1 as $n\to\infty$ |
