---
title: Iterated Function Systems
tag: dynamical-systems
summary: An iterated function system (IFS) is a finite set of contractions on a complete metric space; by Banach's theorem the IFS has a unique compact attractor, which is typically a self-similar fractal.
links:
  - fractals
  - hausdorff-dimension
  - iterated-maps
---

# Iterated Function Systems

An **iterated function system (IFS)** is a finite collection $\{f_1, \ldots, f_N\}$ of **contractions** on a complete metric space $(X, d)$. By the **Banach fixed-point theorem** applied to the Hutchinson operator on the hyperspace of compact sets, every IFS has a unique **attractor** $A \subseteq X$: a compact set satisfying $A = \bigcup_{i=1}^N f_i(A)$. This attractor is typically a **self-similar fractal**. IFS provide a clean mathematical framework for all classical self-similar fractals (Cantor set, Sierpiński triangle, Koch curve) and are the basis of **fractal image compression**. Random IFS — where at each step a contraction $f_i$ is chosen with probability $p_i$ — produce fractal measures and model natural phenomena like fern shapes.

## Definition

A **contraction** on $(X, d)$ is $f: X \to X$ with **Lipschitz constant** $r < 1$:
$$d(f(x), f(y)) \leq r \cdot d(x,y) \quad \forall x, y \in X$$

An **IFS** is $\mathcal{F} = \{f_1, \ldots, f_N\}$ with contraction ratios $r_i < 1$.

## Hutchinson Operator & Attractor

The **Hutchinson operator** $T$ on compact subsets $\mathcal{K}(X)$ (with Hausdorff metric) is:
$$T(K) = \bigcup_{i=1}^N f_i(K)$$

$T$ is a contraction on $(\mathcal{K}(X), d_H)$ with ratio $r = \max_i r_i$. By Banach's theorem:

**Theorem**: There is a unique compact **attractor** $A \in \mathcal{K}(X)$ with $T(A) = A = \bigcup_{i=1}^N f_i(A)$.

## Similarity Dimension

If each $f_i$ is a similarity with ratio $r_i$ and the open set condition holds:
$$\sum_{i=1}^N r_i^s = 1 \quad \Rightarrow \quad d_H(A) = s$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Contraction $f$ | Lipschitz map with constant $r < 1$ |
| Lipschitz constant $r$ | $d(f(x),f(y)) \leq r\,d(x,y)$ |
| IFS $\{f_1,\ldots,f_N\}$ | finite collection of contractions |
| Attractor $A$ | unique compact fixed set: $A = \bigcup f_i(A)$ |
| Hutchinson operator $T$ | $T(K) = \bigcup f_i(K)$; contraction on $\mathcal{K}(X)$ |
| Hausdorff metric $d_H$ | distance between compact sets: $\max(\sup_A d_A, \sup_B d_B)$ |
| Open set condition | separation condition on IFS |
| Similarity dimension $s$ | solution to $\sum r_i^s = 1$ |
| Random IFS | choose $f_i$ with probability $p_i$; produces fractal measure |
| Banach fixed-point theorem | contraction on complete metric space has unique fixed point |
