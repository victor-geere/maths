---
title: Dimension Theory (Krull Dimension)
tag: commutative-algebra
summary: The Krull dimension of a ring is the supremum of lengths of chains of prime ideals; it equals the geometric dimension of the associated variety and is the fundamental invariant of commutative rings.
links:
  - prime-maximal-ideals
  - noetherian-rings
  - localisation
  - affine-varieties
---

# Dimension Theory (Krull Dimension)

The **Krull dimension** of a commutative ring $R$ is the supremum of the lengths of chains of prime ideals $\mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ in $R$. This purely ring-theoretic notion captures the geometric concept of dimension: the Krull dimension of the coordinate ring $k[V]$ of an irreducible affine variety $V$ equals the geometric dimension of $V$. For example, $\dim k[x_1,\ldots,x_n] = n$. Dimension theory is the core of commutative algebra — it drives the theory of Cohen–Macaulay rings, regular local rings, and the intersection theory in algebraic geometry. The **Noether normalisation lemma** and the **principal ideal theorem** are the main tools for computing and bounding it.

## Definition

$$\dim R = \sup\{n : \exists \text{ chain } \mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_n \text{ in } \mathrm{Spec}(R)\}$$

The **height** of a prime $\mathfrak{p}$: $\mathrm{ht}(\mathfrak{p}) = \dim R_\mathfrak{p}$ = length of longest chain below $\mathfrak{p}$.

## Examples

| Ring | Krull dimension |
|---|---|
| Field $k$ | 0 |
| $\mathbb{Z}$ | 1 |
| $k[x_1,\ldots,x_n]$ | $n$ |
| $\mathbb{Z}[x]$ | 2 |
| Local Artinian ring | 0 |

## Principal Ideal Theorem (Krull)

If $R$ is Noetherian and $f \in R$ is not a unit or zero divisor, then every minimal prime $\mathfrak{p}$ over $(f)$ satisfies $\mathrm{ht}(\mathfrak{p}) = 1$.

More generally: if $I = (f_1,\ldots,f_r)$ and $\mathfrak{p}$ is minimal over $I$, then $\mathrm{ht}(\mathfrak{p}) \leq r$.

## Noether Normalisation

Any finitely generated $k$-algebra $A$ has a finite integral extension $k[y_1,\ldots,y_d] \hookrightarrow A$ with $d = \dim A$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\dim R$ | Krull dimension: supremum of prime chain lengths |
| $\mathrm{ht}(\mathfrak{p})$ | height of prime $\mathfrak{p}$: dimension of $R_\mathfrak{p}$ |
| Prime chain | $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ |
| Minimal prime over $I$ | prime $\mathfrak{p} \supseteq I$ with no prime strictly between them |
| Principal ideal theorem | minimal primes over $(f)$ have height $\leq 1$ |
| Noether normalisation | finite integral $k[y_1,\ldots,y_d] \hookrightarrow A$, $d = \dim A$ |
| Cohen–Macaulay ring | depth equals Krull dimension at every prime |
| Regular local ring | $(R,\mathfrak{m})$ with $\dim R = \dim_k \mathfrak{m}/\mathfrak{m}^2$ |
| Artinian ring | $\dim R = 0$; every prime is maximal |
