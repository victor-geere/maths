---
title: Normal Subgroups & Quotient Groups
tag: abstract-algebra
summary: Subgroups whose cosets form a group, and the resulting quotient structure.
links:
  - subgroups-cosets
  - group-homomorphisms
  - lagranges-theorem
---

## Normal Subgroups

A subgroup $N \leq G$ is **normal** (written $N \trianglelefteq G$) if:

$$gNg^{-1} = N \quad \text{for all } g \in G$$

Equivalently, left and right cosets coincide: $gN = Ng$.

## Quotient Group

If $N \trianglelefteq G$, the set of left cosets $G/N = \{gN : g \in G\}$ forms a group under:

$$(aN)(bN) = (ab)N$$

This is the **quotient group** $G/N$. Its order is $|G/N| = [G : N] = |G|/|N|$.

## First Isomorphism Theorem

For any group homomorphism $\phi : G \to H$:

$$G/\ker(\phi) \cong \text{Im}(\phi)$$

This is the most fundamental structural result in group theory.

## Examples

- $\mathbb{Z}/n\mathbb{Z}$: integers mod $n$ is the quotient of $(\mathbb{Z}, +)$ by $n\mathbb{Z}$.
- In an abelian group, **every subgroup is normal**.
- $A_n \trianglelefteq S_n$ (alternating group is always normal in symmetric group).

## Notes

- Normal subgroups are precisely the kernels of homomorphisms.
- The quotient construction "collapses" $N$ to the identity, creating a simpler group.
