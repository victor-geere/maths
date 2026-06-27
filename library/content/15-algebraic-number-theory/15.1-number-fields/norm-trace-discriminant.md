---
title: Norm, Trace & Discriminant
tag: algebraic-number-theory
summary: Three fundamental quantities attached to elements and extensions of number fields — the norm is a multiplicative integer, the trace an additive integer, and the discriminant measures ramification.
links:
  - ring-of-integers
  - number-fields
  - ramification
---

# Norm, Trace & Discriminant

The **norm** and **trace** of an element $\alpha$ in a number field $K/\mathbb{Q}$ are the determinant and trace of the multiplication-by-$\alpha$ map on $K$ viewed as a $\mathbb{Q}$-vector space. They are the most basic arithmetic invariants: the norm is always a rational number (an integer if $\alpha \in \mathcal{O}_K$) and is multiplicative, making it a powerful tool for studying ideals and units. The **discriminant** measures how "spread out" an integral basis is — equivalently, it detects which primes ramify in $K$. Small discriminant means the field is "close to $\mathbb{Q}$", while large discriminant signals complex ramification behaviour. These three quantities appear in virtually every computation in algebraic number theory.

## Norm and Trace of an Element

For $\alpha \in K$ with embeddings $\sigma_1,\ldots,\sigma_n : K \hookrightarrow \mathbb{C}$:

$$N_{K/\mathbb{Q}}(\alpha) = \prod_{i=1}^n \sigma_i(\alpha) = \det(\text{mult}_\alpha)$$

$$\text{Tr}_{K/\mathbb{Q}}(\alpha) = \sum_{i=1}^n \sigma_i(\alpha) = \text{tr}(\text{mult}_\alpha)$$

For $\alpha \in \mathcal{O}_K$: $N_{K/\mathbb{Q}}(\alpha) \in \mathbb{Z}$ and $\text{Tr}_{K/\mathbb{Q}}(\alpha) \in \mathbb{Z}$.

## Properties

- **Multiplicativity of norm:** $N_{K/\mathbb{Q}}(\alpha\beta) = N_{K/\mathbb{Q}}(\alpha) \cdot N_{K/\mathbb{Q}}(\beta)$
- **Additivity of trace:** $\text{Tr}(\alpha + \beta) = \text{Tr}(\alpha) + \text{Tr}(\beta)$
- For the minimal polynomial $x^n + a_{n-1}x^{n-1} + \cdots + a_0$ of $\alpha$:
  - $N_{K/\mathbb{Q}}(\alpha) = (-1)^n a_0$
  - $\text{Tr}_{K/\mathbb{Q}}(\alpha) = -a_{n-1}$

## Quadratic Fields

For $K = \mathbb{Q}(\sqrt{d})$ and $\alpha = a + b\sqrt{d}$:

$$N(\alpha) = a^2 - db^2, \qquad \text{Tr}(\alpha) = 2a$$

## Discriminant

For an integral basis $\{\omega_1,\ldots,\omega_n\}$ of $\mathcal{O}_K$:

$$\text{disc}(K/\mathbb{Q}) = \det\bigl(\text{Tr}(\omega_i\omega_j)\bigr)_{i,j} = \det(\sigma_i(\omega_j))^2$$

**Ramification criterion:** a prime $p \in \mathbb{Z}$ **ramifies** in $K$ iff $p \mid \text{disc}(K/\mathbb{Q})$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $N_{K/\mathbb{Q}}(\alpha)$ | norm of $\alpha$: product of all conjugates |
| $\text{Tr}_{K/\mathbb{Q}}(\alpha)$ | trace of $\alpha$: sum of all conjugates |
| $\sigma_i(\alpha)$ | the $i$-th conjugate of $\alpha$ (image under $i$-th embedding) |
| $\text{mult}_\alpha$ | the $\mathbb{Q}$-linear map $x \mapsto \alpha x$ on $K$ |
| Conjugates | images of $\alpha$ under the $n$ embeddings $K \hookrightarrow \mathbb{C}$ |
| $\text{disc}(K/\mathbb{Q})$ | discriminant of $K$: $\det(\text{Tr}(\omega_i\omega_j))$ |
| Integral basis | a $\mathbb{Z}$-basis for $\mathcal{O}_K$ |
| Ramifies | prime $p$ ramifies in $K$ iff $p \mid \text{disc}(K/\mathbb{Q})$ |
| Quadratic field | $K = \mathbb{Q}(\sqrt{d})$; $N(a+b\sqrt{d}) = a^2-db^2$ |
