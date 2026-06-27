---
title: Classification of Simple Lie Algebras
tag: representation-theory
summary: Over ℂ, every simple Lie algebra is isomorphic to one of four classical infinite families or five exceptional algebras, determined entirely by its Dynkin diagram.
links:
  - lie-algebras
  - root-systems
  - highest-weight
  - representations-sl2
---

# Classification of Simple Lie Algebras

A **simple Lie algebra** is a non-abelian Lie algebra with no proper non-trivial ideals. Over the complex numbers, these are completely classified: there are exactly four infinite families — $\mathfrak{sl}_{n+1}$ ($A_n$), $\mathfrak{so}_{2n+1}$ ($B_n$), $\mathfrak{sp}_{2n}$ ($C_n$), $\mathfrak{so}_{2n}$ ($D_n$) — and five exceptional algebras $\mathfrak{g}_2, \mathfrak{f}_4, \mathfrak{e}_6, \mathfrak{e}_7, \mathfrak{e}_8$. This classification, completed by Wilhelm Killing and Élie Cartan in the 1890s, is one of the deepest results in mathematics, achieved by reducing the problem to the combinatorial classification of Dynkin diagrams. It has ramifications throughout geometry, physics (Grand Unified Theories), and the Langlands programme.

## Strategy of Classification

Given a complex semisimple Lie algebra $\mathfrak{g}$:
1. Choose a **Cartan subalgebra** $\mathfrak{h}$ (maximal abelian, all $\mathrm{ad}_H$ semisimple).
2. Decompose: $\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi} \mathfrak{g}_\alpha$ (root space decomposition).
3. Extract the root system $\Phi \subset \mathfrak{h}^*$.
4. The isomorphism class of $\mathfrak{g}$ is determined by $\Phi$ (up to isomorphism).
5. Classify irreducible root systems via Dynkin diagrams.

## The Classical Families

| Dynkin type | Simple Lie algebra | Associated Lie group |
|---|---|---|
| $A_n$ ($n\geq 1$) | $\mathfrak{sl}_{n+1}(\mathbb{C})$ | $SL_{n+1}(\mathbb{C})$ |
| $B_n$ ($n\geq 2$) | $\mathfrak{so}_{2n+1}(\mathbb{C})$ | $SO_{2n+1}(\mathbb{C})$ |
| $C_n$ ($n\geq 3$) | $\mathfrak{sp}_{2n}(\mathbb{C})$ | $Sp_{2n}(\mathbb{C})$ |
| $D_n$ ($n\geq 4$) | $\mathfrak{so}_{2n}(\mathbb{C})$ | $SO_{2n}(\mathbb{C})$ |

## Exceptional Algebras

| Algebra | Dimension | Notes |
|---|---|---|
| $\mathfrak{g}_2$ | 14 | automorphisms of octonions |
| $\mathfrak{f}_4$ | 52 | |
| $\mathfrak{e}_6$ | 78 | appears in string theory |
| $\mathfrak{e}_7$ | 133 | |
| $\mathfrak{e}_8$ | 248 | appears in heterotic string theory |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Simple Lie algebra | non-abelian with no proper ideals |
| Semisimple | direct sum of simple algebras; Killing form non-degenerate |
| Cartan subalgebra $\mathfrak{h}$ | maximal abelian subalgebra with semisimple adjoint action |
| Root space decomposition | $\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_\alpha \mathfrak{g}_\alpha$ |
| $\mathfrak{g}_\alpha$ | root space: $\{X \in \mathfrak{g} : [H,X] = \alpha(H)X\ \forall H\}$ |
| $A_n$ | type of $\mathfrak{sl}_{n+1}$, rank $n$ |
| $B_n, C_n, D_n$ | orthogonal and symplectic families |
| Exceptional algebras | $\mathfrak{g}_2, \mathfrak{f}_4, \mathfrak{e}_6, \mathfrak{e}_7, \mathfrak{e}_8$ |
| Dynkin diagram | graph that uniquely determines the simple Lie algebra up to isomorphism |
