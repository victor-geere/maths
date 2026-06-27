---
title: Stirling Numbers
tag: discrete
summary: Two families of numbers — of the first and second kind — counting permutations by cycle structure and set partitions by block count.
links:
  - permutations
  - combinations
  - catalan-numbers
---

# Stirling Numbers

**Stirling numbers** come in two related families, both connected to counting combinatorial structures involving $n$ labelled objects. **Stirling numbers of the first kind** $\genfrac{[}{]}{0pt}{}{n}{k}$ count permutations of $n$ objects with exactly $k$ cycles. **Stirling numbers of the second kind** $\genfrac{\{}{\}}{0pt}{}{n}{k}$ count the number of ways to partition $n$ labelled objects into exactly $k$ non-empty unlabelled subsets (set partitions). Despite their different definitions, they are connected by elegant inversion formulas, appear in combinatorial identities relating ordinary and falling powers, and arise naturally in analysis through expansions of $x^n$ in terms of falling factorials.

## Stirling Numbers of the Second Kind $S(n,k) = \genfrac{\{}{\}}{0pt}{}{n}{k}$

$S(n,k)$ = number of ways to partition a set of $n$ elements into exactly $k$ non-empty subsets.

**Recurrence:**

$$S(n, k) = k \cdot S(n-1, k) + S(n-1, k-1)$$

**Boundary:** $S(n,1) = 1$, $S(n,n) = 1$, $S(n,0) = 0$ for $n > 0$.

**Explicit formula:**

$$S(n,k) = \frac{1}{k!}\sum_{j=0}^k (-1)^{k-j}\binom{k}{j}j^n$$

**Bell number:** $B_n = \sum_{k=0}^n S(n,k)$ = total number of set partitions of $[n]$.

## Stirling Numbers of the First Kind $c(n,k) = \genfrac{[}{]}{0pt}{}{n}{k}$

$c(n,k)$ = number of permutations of $n$ objects with exactly $k$ cycles (unsigned).

**Recurrence:**

$$c(n, k) = (n-1)\cdot c(n-1, k) + c(n-1, k-1)$$

**Boundary:** $c(n,1) = (n-1)!$, $c(n,n) = 1$.

## Connection to Falling/Rising Factorials

$$x^n = \sum_{k=0}^n S(n,k)\, x^{\underline{k}} \quad \text{(ordinary powers in terms of falling factorials)}$$

$$x^{\underline{n}} = \sum_{k=0}^n (-1)^{n-k} c(n,k)\, x^k$$

where $x^{\underline{k}} = x(x-1)\cdots(x-k+1)$ is the falling factorial.

## Small Values of $S(n,k)$

| $n \backslash k$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | 1 | | | |
| 2 | 1 | 1 | | |
| 3 | 1 | 3 | 1 | |
| 4 | 1 | 7 | 6 | 1 |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $S(n,k)$ or $\genfrac{\{}{\}}{0pt}{}{n}{k}$ | Stirling number of the second kind: set partitions of $[n]$ into $k$ blocks |
| $c(n,k)$ or $\genfrac{[}{]}{0pt}{}{n}{k}$ | Stirling number of the first kind: permutations of $[n]$ with $k$ cycles |
| Bell number $B_n$ | total number of set partitions of $\{1,\ldots,n\}$ |
| Set partition | division of $[n]$ into non-empty, disjoint subsets (blocks) |
| Cycle | a cyclic sequence in a permutation |
| Falling factorial $x^{\underline{k}}$ | $x(x-1)(x-2)\cdots(x-k+1)$ |
| $[n]$ | the set $\{1, 2, \ldots, n\}$ |
| Inversion formula | the relationship between first and second kind via alternating sums |
