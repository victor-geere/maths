---
title: Symmetric Groups & Permutations
tag: abstract-algebra
summary: Groups of bijections on a finite set and their cycle structure.
links:
  - group-axioms
  - quotient-groups
  - lagranges-theorem
---

## Definition

The **symmetric group** $S_n$ is the group of all bijections $\sigma : \{1,\ldots,n\} \to \{1,\ldots,n\}$ under composition.

$$|S_n| = n!$$

## Cycle Notation

A **$k$-cycle** $(a_1\; a_2 \cdots a_k)$ maps $a_1 \mapsto a_2 \mapsto \cdots \mapsto a_k \mapsto a_1$ and fixes all others.

Every permutation factors uniquely (up to order) into **disjoint cycles**.

**Example:** $(1\;3\;5)(2\;4)$ in $S_5$ sends $1\to3, 3\to5, 5\to1, 2\to4, 4\to2$.

## Transpositions

A **transposition** is a 2-cycle $(i\;j)$. Every permutation is a product of transpositions.

## Sign (Parity)

The **sign** $\text{sgn}(\sigma) \in \{+1, -1\}$:

- Even permutation: $\text{sgn}(\sigma) = +1$ (even number of transpositions)
- Odd permutation: $\text{sgn}(\sigma) = -1$

## Alternating Group

$A_n = \{\sigma \in S_n : \text{sgn}(\sigma) = +1\}$ is a normal subgroup with $|A_n| = n!/2$.

$A_n$ is **simple** for $n \geq 5$ (no proper normal subgroups), a key fact in Galois theory.

## Notes

- $S_1 \cong \{e\}$, $S_2 \cong \mathbb{Z}/2\mathbb{Z}$, $S_3 \cong D_3$ (dihedral group of order 6).
- By Cayley's theorem, every finite group embeds into some $S_n$.
