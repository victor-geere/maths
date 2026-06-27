---
title: Algebraic Groups
tag: representation-theory
summary: An algebraic group is a group that is also an algebraic variety with smooth group operations; it includes matrix groups like GLₙ and is the setting for Chevalley's structure theory and the geometric Langlands programme.
links:
  - lie-groups
  - affine-varieties
  - root-systems
  - highest-weight
  - schemes
---

# Algebraic Groups

An **algebraic group** is a group $G$ that is simultaneously an algebraic variety, with multiplication and inversion given by morphisms of varieties. This merges two worlds: the algebraic structure of groups and the geometric structure of varieties. Over $\mathbb{C}$, every algebraic group gives a Lie group (by analytification), but algebraic groups also make sense over finite fields and $p$-adic fields, where Lie-group methods are not available. **Linear algebraic groups** — closed subgroups of $GL_n$ over an algebraically closed field — are the central objects: their structure theory (Borel subgroups, root data, Weyl groups) parallels Lie theory but works in arbitrary characteristic, and their representations govern modular representation theory and the geometric Langlands programme.

## Definition

An **affine algebraic group** over a field $k$ is an affine variety $G$ over $k$ with morphisms:
$$m: G \times G \to G, \quad \iota: G \to G, \quad e: \mathrm{Spec}(k) \to G$$
satisfying the group axioms (associativity, identity, inverse) as equalities of morphisms.

## Examples

| Algebraic group | Description |
|---|---|
| $GL_n$ | invertible $n\times n$ matrices; $k[GL_n] = k[x_{ij}, \det^{-1}]$ |
| $SL_n$ | $\det = 1$ |
| $\mathbb{G}_m = GL_1$ | multiplicative group; $k[\mathbb{G}_m] = k[t,t^{-1}]$ |
| $\mathbb{G}_a$ | additive group; $k[\mathbb{G}_a] = k[t]$ |
| $T = (\mathbb{G}_m)^n$ | algebraic torus |

## Structure Theory

- **Borel subgroup** $B \subseteq G$: maximal connected solvable subgroup; $G/B$ is a projective variety (flag variety).
- **Torus** $T \subseteq B$: maximal torus; its characters $X^*(T) = \mathrm{Hom}(T, \mathbb{G}_m)$ form a free abelian group.
- **Root data**: the pair $(X^*(T), \Phi, X_*(T), \Phi^\vee)$ determines $G$ up to isomorphism.

## Representations

Representations of $G$ are algebraic group homomorphisms $G \to GL(V)$ (morphisms of varieties). Over $\mathbb{C}$ these match representations of $\mathfrak{g}$ for connected $G$, but in characteristic $p$ the theory is richer and more subtle (modular representations).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Algebraic group $G$ | group object in the category of algebraic varieties |
| Affine algebraic group | algebraic group that is an affine variety |
| $GL_n$ | general linear group as algebraic group |
| $\mathbb{G}_m$ | multiplicative group $GL_1$ |
| $\mathbb{G}_a$ | additive group $(k,+)$ as algebraic group |
| Algebraic torus $T$ | product of copies of $\mathbb{G}_m$ |
| Borel subgroup $B$ | maximal connected solvable subgroup |
| Flag variety $G/B$ | projective homogeneous space; parametrises flags |
| Character group $X^*(T)$ | $\mathrm{Hom}(T,\mathbb{G}_m)$; free abelian group |
| Root datum | combinatorial data $(X^*,\Phi,X_*,\Phi^\vee)$ classifying reductive groups |
