---
title: Adjoint Functors
tag: category-theory
summary: A pair of functors F ⊣ G where morphisms into G(B) from A correspond naturally to morphisms into B from F(A) — one of the most pervasive and powerful patterns in mathematics.
links:
  - functors
  - natural-transformations
  - limits-colimits
  - yoneda-lemma
---

# Adjoint Functors

**Adjoint functors** are perhaps the most important concept in category theory after the notion of a category itself. A pair of functors $F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$ are **adjoint** ($F \dashv G$, read "$F$ is left adjoint to $G$") if there is a natural bijection:

$$\text{Hom}_\mathcal{D}(F(A), B) \cong \text{Hom}_\mathcal{C}(A, G(B))$$

This single equation captures free constructions, limits, exponentials, tensor products, and Galois connections in a unified framework. Mac Lane remarked that adjoint functors arise everywhere in mathematics. Limits are right adjoints; colimits are left adjoints; free algebras are left adjoints to forgetful functors; the tensor product is left adjoint to the internal hom.

## Definition

Functors $F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$ form an **adjunction** $F \dashv G$ if there is a natural isomorphism:

$$\text{Hom}_\mathcal{D}(F(A), B) \cong \text{Hom}_\mathcal{C}(A, G(B))$$

natural in both $A \in \mathcal{C}$ and $B \in \mathcal{D}$.

## Unit and Counit

An adjunction is equivalently given by:

- **Unit** $\eta : \text{id}_\mathcal{C} \Rightarrow G \circ F$: natural transformation with $\eta_A : A \to G(F(A))$
- **Counit** $\varepsilon : F \circ G \Rightarrow \text{id}_\mathcal{D}$: natural transformation with $\varepsilon_B : F(G(B)) \to B$

satisfying the **triangle identities:**
$(\varepsilon F) \circ (F\eta) = \text{id}_F$ and $(G\varepsilon) \circ (\eta G) = \text{id}_G$.

## Examples

| $F$ (left adjoint) | $G$ (right adjoint) | Bijection |
|---|---|---|
| Free group $F(S)$ | Forgetful $U$ | group homoms $F(S)\to G$ ↔ functions $S \to U(G)$ |
| $- \otimes B$ (tensor) | $\text{Hom}(B,-)$ | $\text{Hom}(A\otimes B, C) \cong \text{Hom}(A,\text{Hom}(B,C))$ |
| $\Delta$ (diagonal) | Product $\prod$ | morphisms into $A\times B$ ↔ pairs of morphisms |
| $\text{colim}$ | $\Delta$ (constant diagram) | morphisms from colimit ↔ cocones |
| Suspension $\Sigma$ | Loop space $\Omega$ | maps $\Sigma X \to Y$ ↔ maps $X \to \Omega Y$ |

## RAPL: Right Adjoints Preserve Limits

A right adjoint preserves all limits. A left adjoint preserves all colimits.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $F \dashv G$ | $F$ is left adjoint to $G$; $G$ is right adjoint to $F$ |
| $\text{Hom}(F(A),B) \cong \text{Hom}(A,G(B))$ | the adjunction bijection, natural in $A$ and $B$ |
| Unit $\eta : \text{id} \Rightarrow GF$ | natural transformation from identity to $G \circ F$ |
| Counit $\varepsilon : FG \Rightarrow \text{id}$ | natural transformation from $F \circ G$ to identity |
| Triangle identities | conditions on unit and counit that make them an adjunction |
| Forgetful functor | drops structure (e.g. **Grp** → **Set**); usually has a left adjoint |
| Free functor | left adjoint to a forgetful functor |
| $-\otimes B$ | tensor product with $B$; left adjoint to $\text{Hom}(B,-)$ |
| RAPL | Right Adjoints Preserve Limits |
| LAPC | Left Adjoints Preserve Colimits |
