---
title: Orthogonality Relations
tag: representation-theory
summary: The orthogonality relations are inner product formulas showing that irreducible characters form an orthonormal basis for class functions, providing the key tool for decomposing representations.
links:
  - characters
  - linear-representations
  - fourier-series
---

# Orthogonality Relations

The orthogonality relations are the central computational engine of representation theory. They assert that the irreducible characters of a finite group form an **orthonormal basis** for the space of class functions under a natural inner product — just as Fourier exponentials form an orthonormal basis for periodic functions. This analogy is deep: representation theory on finite groups is genuinely a form of Fourier analysis, with the group algebra playing the role of $L^2$ and the irreducible representations playing the role of frequencies. The orthogonality relations make it possible to decompose any representation mechanically by computing inner products.

## The Inner Product on Class Functions

For a finite group $G$ over $\mathbb{C}$, define:
$$\langle f_1, f_2 \rangle = \frac{1}{|G|} \sum_{g \in G} f_1(g)\overline{f_2(g)}$$

This is a Hermitian inner product on $\mathrm{Cl}(G)$, the space of class functions $G \to \mathbb{C}$.

## First Orthogonality Relation (Characters)

Let $\chi_i, \chi_j$ be irreducible characters of $G$. Then:
$$\langle \chi_i, \chi_j \rangle = \frac{1}{|G|} \sum_{g \in G} \chi_i(g)\overline{\chi_j(g)} = \delta_{ij}$$

The irreducible characters form an **orthonormal set** in $\mathrm{Cl}(G)$. Since their count equals the number of conjugacy classes, they form an **orthonormal basis**.

## Second Orthogonality Relation (Column Orthogonality)

For conjugacy classes $C_s, C_t$:
$$\sum_{i=1}^r \chi_i(g_s)\overline{\chi_i(g_t)} = \frac{|G|}{|C_s|}\delta_{st}$$

where $g_s \in C_s$ is any representative.

## Applications

- **Decomposition**: the multiplicity of $\chi_i$ in $\chi_V$ is $m_i = \langle \chi_V, \chi_i \rangle$.
- **Dimension formula**: $\sum_{i=1}^r (\dim V_i)^2 = |G|$.
- **Irreducibility test**: $\rho$ is irreducible $\iff$ $\langle \chi_\rho, \chi_\rho \rangle = 1$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathrm{Cl}(G)$ | space of class functions $G \to \mathbb{C}$ |
| $\langle f_1, f_2 \rangle$ | inner product: $\frac{1}{|G|}\sum_g f_1(g)\overline{f_2(g)}$ |
| $\delta_{ij}$ | Kronecker delta: 1 if $i=j$, else 0 |
| Orthonormal basis | set of vectors with $\langle e_i, e_j\rangle = \delta_{ij}$ spanning the space |
| $\chi_i$ | $i$-th irreducible character |
| Conjugacy class $C_s$ | equivalence class $\{hg_sh^{-1}\}$ |
| $|C_s|$ | size of conjugacy class $C_s$ |
| Column orthogonality | second relation: $\sum_i \chi_i(g_s)\overline{\chi_i(g_t)} = \frac{|G|}{|C_s|}\delta_{st}$ |
| Dimension formula | $\sum_i (\dim V_i)^2 = |G|$ |
