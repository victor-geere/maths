---
title: Master Theorem
tag: algorithms
summary: A formula that directly solves divide-and-conquer recurrences T(n) = aT(n/b) + f(n) in three cases based on how f(n) compares to n^(log_b a).
links:
  - recurrence-relations
  - big-o-notation
  - generating-functions
---

# Master Theorem

The **Master Theorem** provides a recipe for solving recurrences of the form $T(n) = a\,T(n/b) + f(n)$ that arise from **divide-and-conquer** algorithms: the problem of size $n$ is split into $a$ subproblems of size $n/b$, and $f(n)$ is the work done outside the recursive calls. Rather than requiring the full machinery of generating functions or characteristic equations, the theorem delivers an asymptotic solution in three cases based on how $f(n)$ compares to the "branching overhead" $n^{\log_b a}$. The theorem instantly gives the running time of merge sort, binary search, fast matrix multiplication, and hundreds of other algorithms.

## The Recurrence

$$T(n) = a\,T\!\left(\frac{n}{b}\right) + f(n), \quad a \geq 1,\; b > 1$$

- $a$: number of subproblems
- $b$: factor by which problem size is reduced
- $f(n)$: work at the current level

## Three Cases

Let $c^* = \log_b a$ (the **critical exponent**).

| Case | Condition | Solution |
|---|---|---|
| **Case 1** | $f(n) = O(n^{c^* - \varepsilon})$ for some $\varepsilon > 0$ | $T(n) = \Theta(n^{c^*})$ |
| **Case 2** | $f(n) = \Theta(n^{c^*} \log^k n)$ for $k \geq 0$ | $T(n) = \Theta(n^{c^*}\log^{k+1} n)$ |
| **Case 3** | $f(n) = \Omega(n^{c^* + \varepsilon})$ and regularity | $T(n) = \Theta(f(n))$ |

Regularity for Case 3: $a\,f(n/b) \leq c\,f(n)$ for some $c < 1$ and large $n$.

## Applications

| Algorithm | Recurrence | Solution |
|---|---|---|
| Merge Sort | $T(n) = 2T(n/2) + n$ | $\Theta(n \log n)$ — Case 2 |
| Binary Search | $T(n) = T(n/2) + 1$ | $\Theta(\log n)$ — Case 2 |
| Strassen's Matrix Mult. | $T(n) = 7T(n/2) + n^2$ | $\Theta(n^{\log_2 7}) \approx \Theta(n^{2.81})$ — Case 1 |
| Naive Matrix Mult. | $T(n) = 8T(n/2) + n^2$ | $\Theta(n^3)$ — Case 1 |

## Derivation Intuition

The recursion tree has $\log_b n$ levels. At level $i$, there are $a^i$ subproblems each of size $n/b^i$, contributing $a^i f(n/b^i)$ work. The total is:

$$T(n) = \sum_{i=0}^{\log_b n} a^i f\!\left(\frac{n}{b^i}\right)$$

The dominant term depends on whether $f$ grows faster, slower, or at the same rate as $n^{c^*}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $a$ | number of subproblems per recursive call |
| $b$ | factor by which size decreases per level |
| $f(n)$ | non-recursive work per level |
| $c^* = \log_b a$ | critical exponent; separates the three cases |
| $\Theta(g(n))$ | tight asymptotic bound: $T(n)$ grows exactly like $g(n)$ |
| $O(g(n))$ | upper bound: $T(n)$ grows no faster than $g(n)$ |
| $\Omega(g(n))$ | lower bound: $T(n)$ grows at least as fast as $g(n)$ |
| Case 1 | leaves dominate: $f$ grows slower than $n^{c^*}$ |
| Case 2 | leaves and root roughly tied: $f \approx n^{c^*}$ |
| Case 3 | root dominates: $f$ grows faster than $n^{c^*}$ |
| Divide-and-conquer | algorithm strategy: split, recurse, combine |
| Recursion tree | visualisation of the recursive calls and their costs |
