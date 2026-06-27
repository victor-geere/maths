---
title: Representations of sl₂
tag: representation-theory
summary: The Lie algebra sl₂ has a complete, explicit classification of irreducible representations indexed by a non-negative integer (the highest weight), making it the prototype for all of highest-weight theory.
links:
  - lie-algebras
  - highest-weight
  - root-systems
  - simple-lie-algebras
---

# Representations of sl₂

The Lie algebra $\mathfrak{sl}_2 = \mathfrak{sl}_2(\mathbb{C})$ is the simplest non-abelian simple Lie algebra, consisting of $2\times 2$ traceless complex matrices. Despite (or because of) its simplicity, its representation theory is a complete and explicit prototype for the entire theory of highest-weight representations. Every simple $\mathfrak{sl}_2$-module is finite-dimensional, irreducible, and uniquely determined by its **highest weight** $n \in \mathbb{Z}_{\geq 0}$, with dimension $n+1$. This structure generalises: the representation theory of any semisimple Lie algebra reduces — via root space decompositions and the embedding of $\mathfrak{sl}_2$ along each root — to the $\mathfrak{sl}_2$ case.

## The Algebra

$\mathfrak{sl}_2 = \mathrm{span}\{e, f, h\}$ with brackets:
$$[h,e] = 2e, \quad [h,f] = -2f, \quad [e,f] = h$$

Standard generators: $e = \begin{pmatrix}0&1\\0&0\end{pmatrix}$, $f = \begin{pmatrix}0&0\\1&0\end{pmatrix}$, $h = \begin{pmatrix}1&0\\0&{-1}\end{pmatrix}$.

## Weight Space Decomposition

In any finite-dimensional $\mathfrak{sl}_2$-module $V$, the operator $\rho(h)$ is diagonalisable with integer eigenvalues (**weights**):
$$V = \bigoplus_{k \in \mathbb{Z}} V_k, \quad V_k = \{v \in V : h\cdot v = kv\}$$

The operators $e$ and $f$ shift weights: $e: V_k \to V_{k+2}$, $f: V_k \to V_{k-2}$.

## Irreducible Representations $V(n)$

For each $n \in \mathbb{Z}_{\geq 0}$, there is a unique irreducible module $V(n)$ of dimension $n+1$, with basis $\{v_n, v_{n-2}, \ldots, v_{-n}\}$ (weight vectors) and:
$$h \cdot v_k = k v_k, \quad f \cdot v_k = v_{k-2}, \quad e \cdot v_k = \frac{n+k+2}{2}\cdot\frac{n-k}{2}\, v_{k+2}$$

The **highest weight vector** $v_n$ satisfies $e \cdot v_n = 0$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathfrak{sl}_2$ | Lie algebra of $2\times 2$ traceless matrices |
| $e, f, h$ | standard basis: raising, lowering, Cartan element |
| $[h,e]=2e,\,[h,f]=-2f,\,[e,f]=h$ | defining brackets of $\mathfrak{sl}_2$ |
| Weight | eigenvalue of $h$ acting on a module |
| Weight space $V_k$ | $\{v : h\cdot v = kv\}$ |
| $e$ (raising operator) | shifts weight by $+2$ |
| $f$ (lowering operator) | shifts weight by $-2$ |
| Highest weight $n$ | largest weight; $e\cdot v_n = 0$ |
| $V(n)$ | irreducible module of highest weight $n$, dimension $n+1$ |
| Highest weight vector | $v \in V_n$ with $e\cdot v = 0$ |
