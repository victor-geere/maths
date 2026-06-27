---
title: Class Field Theory
tag: algebraic-number-theory
summary: The complete classification of all abelian Galois extensions of a number field in terms of the arithmetic of the field itself — via ray class groups and the Artin map.
links:
  - artin-reciprocity
  - ideal-class-group
  - galois-number-fields
  - adeles-ideles
---

# Class Field Theory

**Class field theory** is the crowning achievement of classical algebraic number theory: it gives a complete description of all **abelian Galois extensions** of a number field $K$ purely in terms of the arithmetic of $K$ itself. The key slogan is: **abelian extensions of $K$ are controlled by generalised ideal class groups of $K$**. To each open subgroup $H$ of finite index in the idèle class group $C_K = \mathbb{A}_K^\times/K^\times$, there corresponds a unique abelian extension $L/K$, and the Artin map gives an isomorphism $C_K/H \cong \text{Gal}(L/K)$. This is the Galois correspondence for abelian extensions, analogous to but far deeper than the Galois correspondence for finite extensions. Class field theory was developed over decades by Hilbert, Takagi, Artin, and Chevalley, culminating in the adèlic formulation of Tate and Weil.

## The Main Theorem (Global)

There is a bijection between:

$$\left\{\begin{array}{c}\text{abelian extensions}\\ L/K\end{array}\right\} \longleftrightarrow \left\{\begin{array}{c}\text{open subgroups}\\ H \leq C_K \text{ of finite index}\end{array}\right\}$$

given by: $L \mapsto \ker(\text{Art}_{L/K} : C_K \to \text{Gal}(L/K))$ and $H \mapsto L = K^{\text{ab},H}$.

## Ray Class Fields

For a modulus $\mathfrak{m}$ of $K$ (an ideal times a set of real places), the **ray class field** $K(\mathfrak{m})$ is the abelian extension of $K$ whose Galois group is isomorphic to the **ray class group** $C_K(\mathfrak{m}) = I_K(\mathfrak{m}) / P_K(\mathfrak{m})$.

Examples:
- $K = \mathbb{Q}$, $\mathfrak{m} = (n)\infty$: $K(\mathfrak{m}) = \mathbb{Q}(\zeta_n)$ (Kronecker–Weber theorem)
- $K = \mathbb{Q}$: the Kronecker–Weber theorem says every abelian extension of $\mathbb{Q}$ is contained in some $\mathbb{Q}(\zeta_n)$

## Kronecker–Weber Theorem

Every abelian extension of $\mathbb{Q}$ is a subfield of a cyclotomic field $\mathbb{Q}(\zeta_n)$ for some $n$.

## Hilbert Class Field

The **Hilbert class field** $H_K$ is the maximal unramified abelian extension of $K$. Its Galois group satisfies:

$$\text{Gal}(H_K/K) \cong \text{Cl}(K)$$

Moreover: every ideal of $\mathcal{O}_K$ becomes principal in $\mathcal{O}_{H_K}$ (the **principal ideal theorem**).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $C_K = \mathbb{A}_K^\times/K^\times$ | idèle class group |
| Abelian extension | Galois extension with abelian Galois group |
| Open subgroup of $C_K$ | determines a unique abelian extension |
| Modulus $\mathfrak{m}$ | an ideal of $\mathcal{O}_K$ times a set of real embeddings |
| Ray class group $C_K(\mathfrak{m})$ | $I_K(\mathfrak{m})/P_K(\mathfrak{m})$; generalisesideal class group |
| Ray class field $K(\mathfrak{m})$ | the abelian extension with Galois group $\cong C_K(\mathfrak{m})$ |
| Kronecker–Weber theorem | every abelian extension of $\mathbb{Q}$ lies in $\mathbb{Q}(\zeta_n)$ |
| Hilbert class field $H_K$ | maximal unramified abelian extension; $\text{Gal}(H_K/K) \cong \text{Cl}(K)$ |
| Principal ideal theorem | every ideal becomes principal in $H_K$ |
| Artin map | isomorphism $C_K/H \cong \text{Gal}(L/K)$ |
