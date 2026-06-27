---
title: Characters
tag: representation-theory
summary: The character of a representation is the trace function on group elements; characters classify representations completely and carry all essential information about the decomposition.
links:
  - linear-representations
  - orthogonality-relations
  - group-axioms
  - eigenvalues
---

# Characters

The **character** of a linear representation $\rho: G \to GL(V)$ is the function $\chi_\rho: G \to k$ defined by $\chi_\rho(g) = \mathrm{tr}(\rho(g))$, the trace of the matrix $\rho(g)$. Characters are remarkably powerful: they are class functions (constant on conjugacy classes), they completely determine a representation up to equivalence over $\mathbb{C}$, and they turn the complex task of classifying representations into a combinatorial problem involving an orthonormal basis of class functions. The number of distinct irreducible characters equals the number of conjugacy classes of the group, giving a fundamental bridge between group structure and linear algebra.

## Definition

For a representation $\rho: G \to GL(V)$:
$$\chi_\rho(g) = \mathrm{tr}(\rho(g))$$

**Key properties:**
- $\chi_\rho(e) = \dim V$ (degree of $\rho$)
- $\chi_\rho(hgh^{-1}) = \chi_\rho(g)$ — characters are **class functions**
- $\chi_{\rho_1 \oplus \rho_2} = \chi_{\rho_1} + \chi_{\rho_2}$
- $\chi_{\rho_1 \otimes \rho_2} = \chi_{\rho_1} \cdot \chi_{\rho_2}$
- $\chi_{\rho^*}(g) = \overline{\chi_\rho(g)}$ (dual representation)

## The Character Table

For a finite group $G$ over $\mathbb{C}$, the **character table** is the square matrix whose rows are the distinct irreducible characters $\chi_1, \ldots, \chi_r$ and whose columns are the conjugacy classes $C_1, \ldots, C_r$. It encodes the entire representation theory of $G$.

## Determining Representations

Two complex representations are equivalent if and only if they have the same character. The multiplicity of irreducible $V_i$ in $V$ is:
$$m_i = \langle \chi_V, \chi_i \rangle = \frac{1}{|G|} \sum_{g \in G} \chi_V(g)\overline{\chi_i(g)}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\chi_\rho(g) = \mathrm{tr}(\rho(g))$ | character of representation $\rho$ at $g$ |
| $\mathrm{tr}(A)$ | trace: sum of diagonal entries of matrix $A$ |
| Class function | function constant on each conjugacy class of $G$ |
| Conjugacy class | set $\{hgh^{-1} : h \in G\}$ for fixed $g$ |
| Character table | matrix of values $\chi_i(C_j)$ for irreducible $\chi_i$ and class $C_j$ |
| $\chi_{\rho^*}$ | character of the dual (contragredient) representation |
| $\langle \chi, \psi \rangle$ | inner product of class functions: $\frac{1}{|G|}\sum_g \chi(g)\overline{\psi(g)}$ |
| Multiplicity $m_i$ | how many copies of irreducible $V_i$ appear in $V$ |
| $\chi_1 \cdot \chi_2$ | pointwise product; character of tensor product representation |
