---
title: Topos Theory
tag: category-theory
summary: A category that behaves like the category of sets — with a subobject classifier taking the role of the power set — providing a foundation for mathematics and a bridge to logic.
links:
  - abelian-categories
  - yoneda-lemma
  - opposite-categories
  - limits-colimits
---

# Topos Theory

A **topos** (plural: topoi or toposes) is a category that captures the essential properties of the category **Set** of sets, while allowing for radically different "universes" of mathematics. Every topos has a **subobject classifier** $\Omega$ — an object playing the role of the set of truth values — and the internal logic of a topos need not be classical: it can be intuitionistic, or correspond to sheaves on a space. Grothendieck topoi arise as categories of sheaves on a site and are the natural setting for algebraic geometry; elementary topoi (Lawvere–Tierney) axiomatise the categorical essence of "set theory." Topos theory provides a unified framework that simultaneously generalises set theory, point-set topology, and algebraic geometry, and reveals deep connections between geometry and logic.

## Grothendieck Topos

A **Grothendieck topos** is a category equivalent to the category of sheaves $\text{Sh}(\mathcal{C}, J)$ on a site $(\mathcal{C}, J)$, where $J$ is a Grothendieck topology.

Key example: $\text{Sh}(X) =$ sheaves on a topological space $X$.

## Elementary Topos (Lawvere–Tierney)

An **elementary topos** is a category $\mathcal{E}$ satisfying:

1. Has all finite limits
2. Has **exponential objects** $B^A$ for each pair $A, B$
3. Has a **subobject classifier** $\Omega$ with a morphism $\text{true} : 1 \to \Omega$

## Subobject Classifier

The **subobject classifier** $\Omega$ satisfies: for every monomorphism $m : U \hookrightarrow A$, there is a unique **characteristic morphism** $\chi_U : A \to \Omega$ making the following a pullback:

$$U \hookrightarrow 1 \xrightarrow{\text{true}} \Omega \leftarrow A$$

In **Set**: $\Omega = \{\text{true}, \text{false}\}$, and $\chi_U(a) = \text{true} \iff a \in U$.

## Internal Logic

Every topos has an **internal language** — a higher-order intuitionistic type theory — in which the objects of the topos interpret types and morphisms interpret terms. The subobject classifier $\Omega$ is the object of propositions.

## Examples

| Topos | Interpretation |
|---|---|
| **Set** | classical sets |
| $\text{Sh}(X)$ | sheaves on topological space $X$ |
| $[\mathcal{C}^{\text{op}}, \textbf{Set}]$ | presheaves on $\mathcal{C}$ |
| $G$-Sets | sets with $G$-action |
| Smooth sets | sets with smooth structure |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Topos | category with finite limits, exponentials, and a subobject classifier |
| $\Omega$ | subobject classifier — the object of truth values |
| $\text{true} : 1 \to \Omega$ | the "true" morphism from terminal object to $\Omega$ |
| $\chi_U : A \to \Omega$ | characteristic morphism of subobject $U \hookrightarrow A$ |
| Exponential $B^A$ | internal hom: object representing morphisms $A \to B$ |
| Site | a category with a Grothendieck topology |
| Grothendieck topology | a notion of "covering" on a category |
| $\text{Sh}(\mathcal{C},J)$ | sheaves on site $(\mathcal{C},J)$ — a Grothendieck topos |
| Internal language | the type-theoretic logic internal to a topos |
| Intuitionistic logic | logic without the law of excluded middle; the logic of topoi |
| Pullback | limit over a cospan; used in defining the subobject classifier |
