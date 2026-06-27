---
title: Group Axioms & Examples
tag: abstract-algebra
summary: The four axioms defining a group, with standard examples.
links:
  - subgroups-cosets
  - cyclic-groups
  - group-homomorphisms
---

## Definition

A **group** is a set $G$ with a binary operation $\cdot$ satisfying:

1. **Closure:** $a, b \in G \Rightarrow a \cdot b \in G$
2. **Associativity:** $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
3. **Identity:** $\exists\, e \in G$ such that $e \cdot a = a \cdot e = a$
4. **Inverses:** $\forall\, a \in G,\; \exists\, a^{-1} \in G$ such that $a \cdot a^{-1} = e$

A group is **abelian** (commutative) if additionally $a \cdot b = b \cdot a$ for all $a, b$.

## Standard Examples

| Group | Operation | Abelian? |
|---|---|---|
| $(\mathbb{Z}, +)$ | addition | yes |
| $(\mathbb{Q}^*, \times)$ | multiplication | yes |
| $(GL_n(\mathbb{R}), \times)$ | matrix multiplication | no (for $n \geq 2$) |
| $(S_n, \circ)$ | permutation composition | no (for $n \geq 3$) |
| $(\mathbb{Z}/n\mathbb{Z}, +)$ | addition mod $n$ | yes |

## Order

The **order** of a group $|G|$ is its cardinality. The **order of an element** $a$ is the smallest $n \geq 1$ with $a^n = e$.

## Notes

- The identity element is unique; each element has a unique inverse.
- Non-abelian groups are the norm in higher algebra; commutativity must be stated explicitly.
