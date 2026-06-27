---
title: Units & Dirichlet's Unit Theorem
tag: algebraic-number-theory
summary: The group of units 𝒪_K× is finitely generated of rank r₁ + r₂ − 1, where r₁ and r₂ count the real and complex embeddings of K.
links:
  - ring-of-integers
  - number-fields
  - minkowskis-theorem
---

# Units & Dirichlet's Unit Theorem

A **unit** in $\mathcal{O}_K$ is an element with a multiplicative inverse also in $\mathcal{O}_K$ — equivalently, an element of norm $\pm 1$. In $\mathbb{Z}$ the only units are $\pm 1$; in $\mathbb{Z}[i]$ they are $\pm 1, \pm i$; but in $\mathbb{Z}[\sqrt{2}]$ there are infinitely many: $1 + \sqrt{2}$ is a unit (its inverse is $-(1-\sqrt{2}) = \sqrt{2}-1$) and all powers $(1+\sqrt{2})^n$ are also units. **Dirichlet's Unit Theorem** gives the complete structure: $\mathcal{O}_K^\times$ is a finitely generated abelian group of rank $r = r_1 + r_2 - 1$, where $r_1$ and $r_2$ count the real and complex embeddings. The **fundamental units** generate the free part and can be found by continued fractions (for quadratic fields) or more sophisticated algorithms.

## Units

$\alpha \in \mathcal{O}_K$ is a **unit** iff $N_{K/\mathbb{Q}}(\alpha) = \pm 1$.

The **unit group** $\mathcal{O}_K^\times$ is the group of all units under multiplication.

## Dirichlet's Unit Theorem

$$\mathcal{O}_K^\times \cong \mu_K \times \mathbb{Z}^{r_1 + r_2 - 1}$$

where:
- $\mu_K$ is the finite group of **roots of unity** in $K$ (the torsion subgroup)
- $r_1$ = number of real embeddings
- $r_2$ = number of pairs of complex embeddings
- The rank is $r = r_1 + r_2 - 1$

## Rank in Common Cases

| Field $K$ | $r_1$ | $r_2$ | Rank $r$ |
|---|---|---|---|
| $\mathbb{Q}$ | 1 | 0 | 0 ($\mathcal{O}_K^\times = \{\pm 1\}$) |
| $\mathbb{Q}(\sqrt{-d})$, $d>0$ | 0 | 1 | 0 (finitely many units) |
| $\mathbb{Q}(\sqrt{d})$, $d>0$ | 2 | 0 | 1 (one fundamental unit) |
| $\mathbb{Q}(\zeta_5)$ | 0 | 2 | 1 |
| Totally real cubic | 3 | 0 | 2 |

## Regulator

The **regulator** $R_K$ is the absolute value of the determinant of the matrix of logarithms of embeddings of a set of fundamental units. It appears in the **analytic class number formula**:

$$\lim_{s\to1}(s-1)\zeta_K(s) = \frac{2^{r_1}(2\pi)^{r_2}h_K R_K}{w_K\sqrt{|\text{disc}(K)|}}$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{O}_K^\times$ | unit group of $\mathcal{O}_K$ |
| Unit | element with $N_{K/\mathbb{Q}}(\alpha) = \pm 1$ |
| $r_1$ | number of real embeddings of $K$ |
| $r_2$ | number of pairs of complex embeddings |
| Rank $r = r_1+r_2-1$ | rank of the free part of $\mathcal{O}_K^\times$ |
| $\mu_K$ | roots of unity in $K$ (torsion subgroup) |
| Fundamental unit | a generator of the free part when $r=1$ |
| Regulator $R_K$ | volume of the unit lattice in log-embedding space |
| $\zeta_K(s)$ | Dedekind zeta function of $K$ |
| Class number formula | formula relating $h_K$, $R_K$, $\text{disc}$, $w_K$ via $\zeta_K$ |
| $w_K = |\mu_K|$ | number of roots of unity in $K$ |
