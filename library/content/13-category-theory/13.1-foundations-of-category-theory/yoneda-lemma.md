---
title: Yoneda Lemma
tag: category-theory
summary: Every object is completely determined by the morphisms into (or out of) it — the most fundamental result of category theory, yielding a fully faithful embedding of any category into its presheaf category.
links:
  - natural-transformations
  - functors
  - opposite-categories
  - adjoint-functors
---

# Yoneda Lemma

The **Yoneda lemma** is the most fundamental result of category theory. It states that an object $A$ in a category $\mathcal{C}$ is completely determined by the functor $\text{Hom}(A, -)$ — the collection of all morphisms out of $A$. More precisely, natural transformations from the hom functor $\text{Hom}(A, -)$ to any functor $F : \mathcal{C} \to \textbf{Set}$ are in bijection with elements of $F(A)$. This means that to understand an object, it suffices to understand all maps into (or out of) it — a principle variously expressed as "an object is known by its arrows" or "objects have no internal structure beyond their relationships." The Yoneda embedding is fully faithful, embedding $\mathcal{C}$ into the category of presheaves, where objects are represented by functors.

## Statement

For any category $\mathcal{C}$, functor $F : \mathcal{C} \to \textbf{Set}$, and object $A \in \mathcal{C}$:

$$\text{Nat}(\text{Hom}(A, -), F) \cong F(A)$$

naturally in both $A$ and $F$.

The bijection sends a natural transformation $\eta : \text{Hom}(A,-) \Rightarrow F$ to the element $\eta_A(\text{id}_A) \in F(A)$.

## Proof Sketch

Given $\eta \in \text{Nat}(\text{Hom}(A,-), F)$ and $f : A \to B$, naturality forces $\eta_B(f) = F(f)(\eta_A(\text{id}_A))$. So $\eta$ is completely determined by the single element $\eta_A(\text{id}_A) \in F(A)$.

## Yoneda Embedding

The **Yoneda embedding** is the functor:

$$\mathcal{y} : \mathcal{C} \to [\mathcal{C}^{\text{op}}, \textbf{Set}], \quad A \mapsto \text{Hom}(-, A)$$

It is **fully faithful**: morphisms $A \to B$ correspond exactly to natural transformations $\text{Hom}(-,A) \Rightarrow \text{Hom}(-,B)$.

## Consequences

- Every **presheaf** on $\mathcal{C}$ is a "generalised object" of $\mathcal{C}$
- **Representable functors:** $F$ is representable if $F \cong \text{Hom}(A,-)$ for some $A$. The Yoneda lemma is the tool for proving representability
- **Universal elements:** giving an element of $F(A)$ is the same as giving a natural transformation $\text{Hom}(A,-) \Rightarrow F$

## Example

The Yoneda lemma in **Set**: $\text{Nat}(\text{Hom}(\{*\},-), F) \cong F(\{*\})$ — natural transformations from the representable functor are elements of $F$ at a point.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\text{Hom}(A,-)$ | hom functor: $B \mapsto \text{Hom}(A,B)$; covariant, $\mathcal{C} \to \textbf{Set}$ |
| $\text{Nat}(F,G)$ | set of natural transformations from functor $F$ to functor $G$ |
| $\eta_A(\text{id}_A)$ | the distinguished element of $F(A)$ corresponding to $\eta$ |
| Yoneda embedding $\mathcal{y}$ | $A \mapsto \text{Hom}(-,A)$; fully faithful functor $\mathcal{C} \to [\mathcal{C}^{\text{op}},\textbf{Set}]$ |
| Fully faithful | injective and surjective on hom-sets; an embedding |
| Representable functor | $F \cong \text{Hom}(A,-)$ for some object $A$ |
| Presheaf | a functor $\mathcal{C}^{\text{op}} \to \textbf{Set}$ |
| $[\mathcal{C}^{\text{op}},\textbf{Set}]$ | the presheaf category on $\mathcal{C}$ |
| Universal element | an element $u \in F(A)$ such that every $x \in F(B)$ arises uniquely from a map $A \to B$ |
| "Objects are their arrows" | the philosophical content of the Yoneda lemma |
