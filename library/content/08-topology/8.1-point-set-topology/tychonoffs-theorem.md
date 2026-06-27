---
title: Tychonoff's Theorem
tag: topology
summary: An arbitrary product of compact topological spaces is compact in the product topology.
links:
  - compactness
  - topological-spaces
  - separation-axioms
  - bases-subbases
---

# Tychonoff's Theorem

**Tychonoff's Theorem** is one of the deepest and most far-reaching results in topology. It states that the product of any collection of compact spaces — even an uncountably infinite collection — is compact in the product topology. This is remarkable: compactness is a "finiteness" property, and it survives taking products over arbitrarily large index sets. The theorem is equivalent to the **Axiom of Choice**, so it cannot be proved without some form of choice principle. It has applications throughout analysis (Banach–Alaoglu theorem, proofs in functional analysis), logic (compactness theorem for propositional logic), and algebra (profinite groups as inverse limits).

## Statement

Let $\{X_\alpha\}_{\alpha \in A}$ be any collection of topological spaces, each compact. Then the product space:

$$X = \prod_{\alpha \in A} X_\alpha$$

equipped with the **product topology** is compact.

## Special Cases

- Finite product of compact spaces: compact (follows from the tube lemma, without the Axiom of Choice).
- $[0,1]^{\mathbb{R}}$ (uncountable product of $[0,1]$): compact by Tychonoff.
- $\{0,1\}^{\mathbb{N}}$ (Cantor space): compact (homeomorphic to the Cantor set).

## Proof Strategy (Alexander Subbasis Theorem)

A space is compact iff every open cover by **subbasis** elements has a finite subcover. Using this:
1. Assume $\prod X_\alpha$ has a subbasis cover with no finite subcover.
2. Use Zorn's Lemma (equivalent to the Axiom of Choice) to extend this to a maximal such cover.
3. Derive a contradiction by projecting to each factor and using compactness of $X_\alpha$.

## Equivalence with Axiom of Choice

Tychonoff's theorem (in full generality) is **equivalent** to the Axiom of Choice over ZF set theory. For Hausdorff spaces, it is equivalent to the Boolean Prime Ideal theorem (a weaker choice principle).

## Applications

- **Banach–Alaoglu:** the closed unit ball in the weak-* topology of a dual space is compact.
- **Profinite groups:** inverse limits of finite groups are compact.
- **Logic:** the compactness theorem for first-order logic.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\prod_{\alpha \in A} X_\alpha$ | product of spaces $X_\alpha$ over index set $A$ |
| Product topology | coarsest topology making all projections $\pi_\alpha$ continuous |
| Compact | every open cover has a finite subcover |
| Axiom of Choice | for any collection of non-empty sets, a simultaneous choice function exists |
| Zorn's Lemma | a partially ordered set where every chain has an upper bound has a maximal element |
| Subbasis | a generating family for a topology (intersections then unions) |
| Alexander Subbasis Theorem | compactness can be verified using subbasis covers |
| Cantor space | $\{0,1\}^{\mathbb{N}}$ — countable product of two-point spaces |
| Banach–Alaoglu theorem | unit ball in dual space is weak-* compact |
| ZF | Zermelo–Fraenkel set theory (without the Axiom of Choice) |
