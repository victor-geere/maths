---
title: Separation Axioms (T0–T4)
tag: topology
summary: A hierarchy of conditions — T0 through T4 — requiring that distinct points or closed sets can be "separated" by open sets.
links:
  - topological-spaces
  - open-closed-sets
  - urysohns-lemma
  - compactness
---

# Separation Axioms (T0–T4)

The **separation axioms** form a hierarchy of conditions on a topological space that progressively strengthen how well distinct points and closed sets can be "told apart" by open sets. A space with more separation has a richer open-set structure, enabling stronger theorems. The axioms are labelled $T_0$ through $T_4$ (the $T$ stands for the German *Trennungsaxiom*, "separation axiom"). Most spaces encountered in analysis satisfy at least $T_2$ (Hausdorff), which ensures limits of sequences are unique. The separation axioms clarify precisely which properties of metric spaces are essential and which are special to the metric structure.

## The Hierarchy

### $T_0$ (Kolmogorov)
For any two distinct points $x \neq y$, at least one has a neighbourhood not containing the other.

### $T_1$ (Fréchet)
For any two distinct points, each has a neighbourhood not containing the other. Equivalently: every singleton $\{x\}$ is closed.

### $T_2$ (Hausdorff)
Any two distinct points have **disjoint** open neighbourhoods. This is the most important separation axiom.

$$x \neq y \implies \exists\, U \ni x,\; V \ni y : U \cap V = \emptyset$$

### $T_3$ (Regular Hausdorff)
$T_1$ plus: any point and disjoint closed set can be separated by disjoint open sets.

### $T_4$ (Normal Hausdorff)
$T_1$ plus: any two disjoint closed sets can be separated by disjoint open sets.

## Hierarchy

$$T_4 \implies T_3 \implies T_2 \implies T_1 \implies T_0$$

Every metric space is $T_4$ (normal).

## Key Theorems for $T_4$ Spaces

**Urysohn's Lemma:** $X$ is normal iff for any disjoint closed $A, B$, there is a continuous $f : X \to [0,1]$ with $f|_A = 0$ and $f|_B = 1$.

**Tietze Extension Theorem:** $X$ is normal iff every continuous function $f : A \to \mathbb{R}$ on a closed $A \subseteq X$ extends to a continuous $F : X \to \mathbb{R}$.

## Examples

| Space | Highest $T_n$ |
|---|---|
| Any metric space | $T_4$ |
| $\mathbb{R}$ with finite complement topology | $T_1$ (not $T_2$) |
| Sierpiński space $\{0, 1\}$ with $\tau = \{\emptyset, \{1\}, \{0,1\}\}$ | $T_0$ (not $T_1$) |
| Compact Hausdorff space | $T_4$ |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $T_0$ | Kolmogorov: topologically distinguishable points |
| $T_1$ | Fréchet: singletons are closed |
| $T_2$ | Hausdorff: distinct points have disjoint neighbourhoods |
| $T_3$ | Regular: $T_1$ + point and closed set separated by open sets |
| $T_4$ | Normal: $T_1$ + disjoint closed sets separated by open sets |
| Hausdorff space | a $T_2$ space; limits of sequences are unique |
| Normal space | a $T_4$ space; enables Urysohn's lemma |
| Urysohn's Lemma | normal spaces admit continuous functions separating closed sets |
| Tietze Extension | normal spaces allow continuous extensions from closed subsets |
| Sierpiński space | the simplest $T_0$ space that is not $T_1$ |
| Trennungsaxiom | German for "separation axiom" (source of the $T$ prefix) |
