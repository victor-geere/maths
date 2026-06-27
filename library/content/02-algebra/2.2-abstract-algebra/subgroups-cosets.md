---
title: Subgroups & Cosets
tag: abstract-algebra
summary: Substructures of groups and the partition of a group by a subgroup.
links:
  - group-axioms
  - lagranges-theorem
  - quotient-groups
---

## Subgroups

A subset $H \subseteq G$ is a **subgroup** (written $H \leq G$) if:

1. $e \in H$
2. $a, b \in H \Rightarrow ab \in H$
3. $a \in H \Rightarrow a^{-1} \in H$

**Subgroup criterion:** $H \neq \emptyset$ and $a, b \in H \Rightarrow ab^{-1} \in H$.

## Cosets

For $H \leq G$ and $g \in G$:

- **Left coset:** $gH = \{gh : h \in H\}$
- **Right coset:** $Hg = \{hg : h \in H\}$

The left cosets of $H$ **partition** $G$: every element of $G$ belongs to exactly one left coset.

## Key Properties

- All cosets of $H$ have the same size: $|gH| = |H|$.
- $gH = H$ iff $g \in H$.
- Two left cosets are either equal or disjoint.

## Example

In $G = (\mathbb{Z}_6, +)$, $H = \{0, 2, 4\}$ is a subgroup. The left cosets are:
- $0 + H = \{0, 2, 4\}$
- $1 + H = \{1, 3, 5\}$

These two cosets partition $\mathbb{Z}_6$.

## Index

The **index** $[G : H]$ is the number of distinct left cosets of $H$ in $G$.

$$[G : H] = |G| / |H| \quad \text{(when } G \text{ is finite)}$$
