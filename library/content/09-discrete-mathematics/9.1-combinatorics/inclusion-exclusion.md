---
title: Inclusion–Exclusion Principle
tag: discrete
summary: A formula for the size of a union of sets by alternately adding and subtracting the sizes of intersections of all subcollections.
links:
  - combinations
  - permutations
  - pigeonhole
---

# Inclusion–Exclusion Principle

The **Inclusion–Exclusion Principle** provides an exact formula for the number of elements in the union of several sets. The naive approach — just adding the sizes — overcounts elements appearing in multiple sets. The principle corrects this by systematically including single-set counts, then excluding pairwise intersections (which were double-counted), then re-including triple intersections (which were over-excluded), and so on, alternating signs with each level. It is one of the most versatile tools in combinatorics, used to count derangements, solve Euler's totient function, count surjections, and solve many inclusion–exclusion-flavoured competition problems.

## Statement

For finite sets $A_1, A_2, \ldots, A_n$:

$$\left|A_1 \cup A_2 \cup \cdots \cup A_n\right| = \sum_{i}|A_i| - \sum_{i<j}|A_i \cap A_j| + \sum_{i<j<k}|A_i \cap A_j \cap A_k| - \cdots$$

In compact form:

$$\left|\bigcup_{i=1}^n A_i\right| = \sum_{\emptyset \neq S \subseteq [n]} (-1)^{|S|+1}\left|\bigcap_{i \in S} A_i\right|$$

## Two-Set Case

$$|A \cup B| = |A| + |B| - |A \cap B|$$

## Three-Set Case

$$|A \cup B \cup C| = |A|+|B|+|C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C|$$

## Complement Form

The number of elements in **none** of $A_1, \ldots, A_n$ (within a universe $U$):

$$\left|\overline{A_1} \cap \cdots \cap \overline{A_n}\right| = \sum_{S \subseteq [n]} (-1)^{|S|}\left|\bigcap_{i \in S} A_i\right|$$

## Application: Derangements

A **derangement** of $\{1, \ldots, n\}$ is a permutation with no fixed points. Applying inclusion–exclusion:

$$D_n = n!\sum_{k=0}^n \frac{(-1)^k}{k!} \approx \frac{n!}{e}$$

## Application: Euler's Totient

$$\phi(n) = n\prod_{p \mid n}\left(1 - \frac{1}{p}\right)$$

derived by inclusion–exclusion over the prime factors of $n$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $|A|$ | cardinality of set $A$ — number of elements |
| $A \cup B$ | union: elements in $A$ or $B$ (or both) |
| $A \cap B$ | intersection: elements in both $A$ and $B$ |
| $\overline{A}$ | complement of $A$ in universe $U$ |
| $[n]$ | the set $\{1, 2, \ldots, n\}$ |
| $S \subseteq [n]$ | a subset of $\{1, \ldots, n\}$ |
| $(-1)^{|S|+1}$ | alternating sign factor |
| Derangement $D_n$ | permutation of $\{1,\ldots,n\}$ with no fixed points |
| Fixed point | element $i$ with $\sigma(i) = i$ in a permutation $\sigma$ |
| $\phi(n)$ | Euler's totient: count of integers in $\{1,\ldots,n\}$ coprime to $n$ |
| Universe $U$ | the ambient set containing all $A_i$ |
