---
title: Induced Representations
tag: representation-theory
summary: Given a representation of a subgroup, the induced representation constructs a representation of the full group by formally extending the action, governed by Frobenius reciprocity.
links:
  - linear-representations
  - characters
  - subgroups-cosets
  - representations-symmetric-group
---

# Induced Representations

**Induction** is the process of building a representation of a group $G$ from a representation of a subgroup $H \leq G$. If $\sigma: H \to GL(W)$ is a representation of $H$, the **induced representation** $\mathrm{Ind}_H^G \sigma$ is a representation of $G$ on a larger vector space, constructed by "spreading" the $H$-action over the cosets $G/H$. Induction and its adjoint operation, **restriction**, are the key tools for moving between representations at different levels of a group-subgroup hierarchy. The fundamental relationship between them is **Frobenius reciprocity**, which is a cornerstone of the whole theory.

## Construction

Let $H \leq G$ with $[G:H] = n$ and $\sigma: H \to GL(W)$ a representation. Choose coset representatives $g_1, \ldots, g_n$ with $G = \bigsqcup_{i=1}^n g_i H$. The induced representation is:

$$\mathrm{Ind}_H^G W = k[G] \otimes_{k[H]} W \cong \bigoplus_{i=1}^n g_i \otimes W$$

as a vector space, with $\dim(\mathrm{Ind}_H^G W) = [G:H] \cdot \dim W$.

The action of $g \in G$ permutes the cosets: if $gg_i = g_{\sigma(g,i)} h_{g,i}$ with $h_{g,i} \in H$, then:
$$g \cdot (g_i \otimes w) = g_{\sigma(g,i)} \otimes \sigma(h_{g,i})w$$

## Induced Character Formula

The character of the induced representation is:
$$\chi_{\mathrm{Ind}_H^G \sigma}(g) = \frac{1}{|H|} \sum_{\substack{x \in G \\ x^{-1}gx \in H}} \chi_\sigma(x^{-1}gx)$$

## Frobenius Reciprocity

For representations $\rho$ of $G$ and $\sigma$ of $H$:
$$\langle \mathrm{Ind}_H^G \sigma,\, \rho \rangle_G = \langle \sigma,\, \mathrm{Res}_H^G \rho \rangle_H$$

This says: the multiplicity of $\rho$ in $\mathrm{Ind}_H^G \sigma$ equals the multiplicity of $\sigma$ in the restriction of $\rho$ to $H$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $H \leq G$ | $H$ is a subgroup of $G$ |
| $[G:H]$ | index of $H$ in $G$: number of cosets $gH$ |
| $G/H$ | set of left cosets of $H$ in $G$ |
| $\mathrm{Ind}_H^G \sigma$ | representation of $G$ induced from $\sigma$ on $H$ |
| $\mathrm{Res}_H^G \rho$ | restriction of $G$-representation $\rho$ to $H$ |
| $k[G] \otimes_{k[H]} W$ | tensor product over $k[H]$: construction of induced module |
| Coset representatives | elements $g_1,\ldots,g_n$ with $G = \bigsqcup g_i H$ |
| Frobenius reciprocity | $\langle \mathrm{Ind}_H^G\sigma, \rho\rangle_G = \langle\sigma, \mathrm{Res}_H^G\rho\rangle_H$ |
| $\chi_{\mathrm{Ind}}(g)$ | character of induced rep, summed over elements conjugating $g$ into $H$ |
