---
title: Derived Categories
tag: homological-algebra
summary: The derived category D(A) of an abelian category is obtained by formally inverting quasi-isomorphisms of chain complexes; it is the natural setting for derived functors, Fourier–Mukai transforms, and homological mirror symmetry.
links:
  - chain-complexes
  - derived-functors
  - spectral-sequences
  - sheaves
  - sheaf-cohomology
---

# Derived Categories

The **derived category** $\mathbf{D}(\mathcal{A})$ of an abelian category $\mathcal{A}$ is the universal construction that formally inverts **quasi-isomorphisms** — chain maps that induce isomorphisms on all homology groups. In the derived category, two chain complexes are isomorphic if they are quasi-isomorphic, making their homology the fundamental invariant. Derived categories were introduced by Grothendieck and Verdier in the 1960s to give a clean framework for sheaf cohomology and duality (Verdier duality). Today they are central to algebraic geometry (Fourier–Mukai transforms, derived algebraic geometry), representation theory (derived equivalences between algebras, Beilinson–Bernstein–Deligne–Gabber), and mirror symmetry.

## Construction

Start with the **category of chain complexes** $\mathrm{Ch}(\mathcal{A})$.

1. Pass to the **homotopy category** $\mathbf{K}(\mathcal{A})$: objects are chain complexes, morphisms are chain maps modulo homotopy equivalence.
2. **Localise** $\mathbf{K}(\mathcal{A})$ at quasi-isomorphisms: formally invert all maps $f: C_\bullet \to D_\bullet$ inducing $H_n(f)$ isomorphisms.

The result is $\mathbf{D}(\mathcal{A})$.

## Triangulated Structure

$\mathbf{D}(\mathcal{A})$ is a **triangulated category**: it has a shift functor $[1]$ and **distinguished triangles** $A \to B \to C \to A[1]$ playing the role of short exact sequences.

## Derived Functors Revisited

Right-derived functors $RF: \mathbf{D}^+(\mathcal{A}) \to \mathbf{D}^+(\mathcal{B})$ are exact functors of triangulated categories extending $F$. They compute $R^nF(M) = H^n(RF(M))$.

## Derived Equivalences

An equivalence $\mathbf{D}^b(\mathcal{A}) \simeq \mathbf{D}^b(\mathcal{B})$ of bounded derived categories is much weaker than an equivalence of abelian categories. Famous examples: Beilinson's equivalence $\mathbf{D}^b(\mathrm{Coh}(\mathbb{P}^n)) \simeq \mathbf{D}^b(A_n\text{-mod})$; Fourier–Mukai transforms for abelian varieties.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathbf{D}(\mathcal{A})$ | derived category of abelian category $\mathcal{A}$ |
| Quasi-isomorphism | chain map inducing isomorphisms on all $H_n$ |
| $\mathbf{K}(\mathcal{A})$ | homotopy category: complexes modulo chain homotopy |
| Triangulated category | category with shift $[1]$ and distinguished triangles |
| Distinguished triangle $A \to B \to C \to A[1]$ | analogue of short exact sequence |
| $RF$ | total right-derived functor as exact functor on $\mathbf{D}$ |
| $\mathbf{D}^+(\mathcal{A})$ | complexes bounded below; $\mathbf{D}^b$: bounded |
| Derived equivalence | equivalence $\mathbf{D}^b(\mathcal{A}) \simeq \mathbf{D}^b(\mathcal{B})$ |
| Fourier–Mukai transform | integral transform defining derived equivalence for varieties |
| Verdier duality | duality functor $D$ on $\mathbf{D}^b$ of constructible sheaves |
