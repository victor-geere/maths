---
title: Group Homomorphisms
tag: abstract-algebra
summary: Structure-preserving maps between groups, their kernels and images.
links:
  - group-axioms
  - quotient-groups
  - cyclic-groups
---

## Definition

A map $\phi : G \to H$ is a **group homomorphism** if:

$$\phi(ab) = \phi(a)\phi(b) \quad \text{for all } a, b \in G$$

## Kernel and Image

- **Kernel:** $\ker(\phi) = \{g \in G : \phi(g) = e_H\}$ — always a normal subgroup of $G$.
- **Image:** $\text{Im}(\phi) = \{\phi(g) : g \in G\}$ — a subgroup of $H$.

## Types

| Name | Property |
|---|---|
| Monomorphism | injective |
| Epimorphism | surjective |
| Isomorphism | bijective |
| Endomorphism | $G = H$ |
| Automorphism | bijective endomorphism |

## Key Properties

- $\phi(e_G) = e_H$
- $\phi(g^{-1}) = \phi(g)^{-1}$
- $\phi$ is injective $\iff \ker(\phi) = \{e_G\}$

## First Isomorphism Theorem

$$G / \ker(\phi) \cong \text{Im}(\phi)$$

## Example

$\phi : (\mathbb{Z}, +) \to (\mathbb{Z}/n\mathbb{Z}, +)$, $\phi(k) = k \bmod n$.

- $\ker(\phi) = n\mathbb{Z}$
- $\text{Im}(\phi) = \mathbb{Z}/n\mathbb{Z}$
- By the first isomorphism theorem: $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}/n\mathbb{Z}$ ✓
