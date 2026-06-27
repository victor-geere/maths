---
title: Adèles & Idèles
tag: algebraic-number-theory
summary: The adèle ring 𝔸_K combines all completions of K simultaneously; the idèle group 𝔸_K× is its unit group — together they encode all local information and simplify global number theory.
links:
  - local-fields
  - p-adic-numbers
  - class-field-theory
---

# Adèles & Idèles

The **adèle ring** $\mathbb{A}_K$ of a number field $K$ is the "simultaneous" combination of all its completions: the real/complex embeddings and all the $p$-adic completions, constrained so that all but finitely many components are $p$-adic integers. The **idèle group** $\mathbb{A}_K^\times$ consists of elements of $\mathbb{A}_K$ with multiplicative inverses. By embedding $K$ diagonally into $\mathbb{A}_K$, number theory becomes a single global object: the **adèlic approach** to $L$-functions (Tate's thesis), the proof of the product formula $\prod_v |x|_v = 1$, and the formulation of global class field theory all live naturally in the adèlic language. Adèles and idèles are to number fields what the ring of all power series expansions is to algebraic geometry.

## The Adèle Ring

For a number field $K$ with places $v$ (real, complex, and $p$-adic for each prime):

$$\mathbb{A}_K = \mathbb{R}^{r_1} \times \mathbb{C}^{r_2} \times \prod_{\mathfrak{p}}'\ K_\mathfrak{p}$$

where $\prod'$ is the **restricted product**: tuples $(x_v)_v$ with $x_\mathfrak{p} \in \mathcal{O}_{K_\mathfrak{p}}$ for all but finitely many $\mathfrak{p}$.

## Embedding of $K$

$K$ embeds diagonally into $\mathbb{A}_K$:

$$K \hookrightarrow \mathbb{A}_K, \quad \alpha \mapsto (\sigma_1(\alpha), \ldots, |\alpha|_\mathfrak{p}, \ldots)$$

The **product formula** says this image satisfies $\prod_v |\alpha|_v = 1$ for all $\alpha \in K^*$.

## Idèle Group

$$\mathbb{A}_K^\times = \{(x_v)_v \in \mathbb{A}_K : x_v \neq 0 \text{ for all }v\text{ and } x_\mathfrak{p} \in \mathcal{O}_\mathfrak{p}^\times \text{ for a.e. }\mathfrak{p}\}$$

## Class Group via Idèles

There is a surjection:

$$\mathbb{A}_K^\times / K^\times \to \text{Cl}(K)$$

More precisely, $\text{Cl}(K) \cong \mathbb{A}_{K,f}^\times / K^\times \hat{\mathcal{O}}_K^\times$ where $\mathbb{A}_{K,f}$ is the finite adèles.

## Global Class Field Theory (Adèlic)

The **global Artin map** is a continuous homomorphism:

$$\text{Art}_K : \mathbb{A}_K^\times \to \text{Gal}(K^{\text{ab}}/K)$$

with kernel $K^\times \cdot (K_\infty^\times)^0$ — giving a complete description of all abelian extensions.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbb{A}_K$ | adèle ring of $K$: restricted product of all completions |
| $\mathbb{A}_K^\times$ | idèle group of $K$ |
| Restricted product $\prod'$ | tuples $(x_v)$ with $x_v \in \mathcal{O}_v$ for all but finitely many $v$ |
| Place $v$ | an equivalence class of absolute values; real, complex, or $\mathfrak{p}$-adic |
| $K_\mathfrak{p}$ | completion of $K$ at prime $\mathfrak{p}$ (a local field) |
| Product formula | $\prod_v |\alpha|_v = 1$ for $\alpha \in K^*$ |
| Finite adèles $\mathbb{A}_{K,f}$ | adèles without the archimedean places |
| $K^{\text{ab}}$ | maximal abelian extension of $K$ |
| Global Artin map | $\text{Art}_K : \mathbb{A}_K^\times \to \text{Gal}(K^{\text{ab}}/K)$ |
| Tate's thesis | uses adèles to prove analytic continuation and functional equation of $L(s, \chi)$ |
