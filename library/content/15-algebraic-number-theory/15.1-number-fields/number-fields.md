---
title: Algebraic Numbers & Number Fields
tag: algebraic-number-theory
summary: An algebraic number satisfies a polynomial equation over ℚ; a number field is a finite extension of ℚ, providing the natural setting for algebraic number theory.
links:
  - ring-of-integers
  - galois-theory
  - field-extensions
---

# Algebraic Numbers & Number Fields

An **algebraic number** is a complex number that is a root of a non-zero polynomial with rational coefficients. The square root $\sqrt{2}$, the golden ratio, and every $n$-th root of unity are algebraic; $\pi$ and $e$ are not (they are **transcendental**). A **number field** $K$ is a field that contains $\mathbb{Q}$ and has finite dimension as a vector space over $\mathbb{Q}$ — equivalently, $K = \mathbb{Q}(\alpha_1, \ldots, \alpha_r)$ for algebraic numbers $\alpha_i$. Number fields are the central objects of algebraic number theory: they generalise $\mathbb{Q}$ just as algebraic curves generalise lines, and the arithmetic of ideals in their ring of integers — factorisation, ramification, class groups — governs their number-theoretic behaviour.

## Algebraic Numbers

$\alpha \in \mathbb{C}$ is **algebraic over $\mathbb{Q}$** if there exists a non-zero $f \in \mathbb{Q}[x]$ with $f(\alpha) = 0$.

The **minimal polynomial** $\text{min}_\mathbb{Q}(\alpha)$ is the unique monic polynomial of lowest degree in $\mathbb{Q}[x]$ with $\alpha$ as a root.

The **degree** of $\alpha$ is $[\mathbb{Q}(\alpha):\mathbb{Q}] = \deg \text{min}_\mathbb{Q}(\alpha)$.

## Number Fields

A **number field** is a field $K$ with $\mathbb{Q} \subseteq K$ and $[K:\mathbb{Q}] = n < \infty$.

**Primitive element theorem:** $K = \mathbb{Q}(\alpha)$ for some single algebraic $\alpha$ with $[K:\mathbb{Q}] = \deg(\text{min}_\mathbb{Q}(\alpha))$.

## Standard Examples

| Field $K$ | Generator | $[K:\mathbb{Q}]$ |
|---|---|---|
| $\mathbb{Q}(\sqrt{d})$ | $\sqrt{d}$ ($d$ squarefree) | 2 (quadratic field) |
| $\mathbb{Q}(\sqrt[3]{2})$ | $\sqrt[3]{2}$ | 3 |
| $\mathbb{Q}(\zeta_n)$ | $n$-th root of unity | $\phi(n)$ (cyclotomic field) |
| $\mathbb{Q}(\sqrt{2}, \sqrt{3})$ | — | 4 |

## Embeddings

A degree-$n$ number field $K$ has exactly $n$ field embeddings $\sigma : K \hookrightarrow \mathbb{C}$:
- $r_1$ real embeddings (into $\mathbb{R}$)
- $r_2$ pairs of complex conjugate embeddings

where $r_1 + 2r_2 = n$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\alpha \in \overline{\mathbb{Q}}$ | $\alpha$ is algebraic over $\mathbb{Q}$ |
| $\overline{\mathbb{Q}}$ | the algebraic closure of $\mathbb{Q}$: all algebraic numbers |
| $\text{min}_\mathbb{Q}(\alpha)$ | minimal polynomial of $\alpha$ over $\mathbb{Q}$ |
| $[K:\mathbb{Q}] = n$ | degree of number field $K$ over $\mathbb{Q}$ |
| $\mathbb{Q}(\alpha)$ | the smallest field containing both $\mathbb{Q}$ and $\alpha$ |
| Quadratic field | $[K:\mathbb{Q}] = 2$; of the form $\mathbb{Q}(\sqrt{d})$ |
| Cyclotomic field | $\mathbb{Q}(\zeta_n)$ where $\zeta_n = e^{2\pi i/n}$ |
| $\phi(n)$ | Euler's totient function |
| $r_1$ | number of real embeddings of $K$ |
| $r_2$ | number of pairs of complex embeddings |
| Transcendental | not algebraic; e.g. $\pi$, $e$ |
