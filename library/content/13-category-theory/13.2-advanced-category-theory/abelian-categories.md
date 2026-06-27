---
title: Abelian Categories
tag: category-theory
summary: Categories with a zero object, kernels, cokernels, and exact sequences — the correct abstract setting for homological algebra.
links:
  - categories-morphisms
  - limits-colimits
  - monads
---

# Abelian Categories

An **abelian category** is a category that abstracts the key properties of the category **Ab** of abelian groups — and more generally of **$R$-Mod** (modules over a ring) — that make homological algebra possible. The axioms guarantee that kernels and cokernels exist, that images and coimages coincide (so the **first isomorphism theorem** holds), and that short exact sequences are the fundamental building blocks of the theory. In an abelian category one can define chain complexes, homology groups, derived functors (Ext, Tor), and spectral sequences, all in full generality. This abstraction means a single theorem in an abelian category applies simultaneously to abelian groups, modules over a ring, sheaves of abelian groups on a topological space, and representations of a group.

## Definition

A category $\mathcal{A}$ is **abelian** if:

1. It has a **zero object** $0$
2. It has all **finite products** and **coproducts**
3. Every morphism has a **kernel** and a **cokernel**
4. Every **monomorphism** is a kernel; every **epimorphism** is a cokernel

Equivalently: $\mathcal{A}$ is preadditive (hom-sets are abelian groups), has a zero object, finite biproducts, and every morphism has a kernel and cokernel, with the canonical map $\text{coim}(f) \to \text{im}(f)$ being an isomorphism.

## Key Properties

- **Hom-sets are abelian groups** and composition is bilinear
- **First Isomorphism Theorem:** $\text{coim}(f) \cong \text{im}(f)$ for every morphism $f$
- **Snake Lemma** and **Five Lemma** hold
- **Short exact sequences** $0 \to A \to B \to C \to 0$ are the fundamental objects
- **Long exact sequences** in homology arise from short exact sequences

## Examples of Abelian Categories

| Category | Objects |
|---|---|
| **Ab** | Abelian groups |
| **$R$-Mod** | Left modules over a ring $R$ |
| **Sh$(X)$** | Sheaves of abelian groups on space $X$ |
| **QCoh$(X)$** | Quasi-coherent sheaves on scheme $X$ |
| **Rep$_k(G)$** | $k$-representations of group $G$ |

## Derived Categories

The **derived category** $D(\mathcal{A})$ is obtained from the category of chain complexes in $\mathcal{A}$ by formally inverting quasi-isomorphisms. It is the natural home for derived functors.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Zero object $0$ | both initial and terminal |
| Kernel of $f$ | the equaliser of $f$ and the zero morphism |
| Cokernel of $f$ | the coequaliser of $f$ and the zero morphism |
| Monomorphism | left-cancellable morphism (categorical analogue of injective) |
| Epimorphism | right-cancellable morphism (categorical analogue of surjective) |
| $\text{im}(f)$ | image of $f$: kernel of the cokernel |
| $\text{coim}(f)$ | coimage of $f$: cokernel of the kernel |
| Short exact sequence | $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ with $\ker g = \text{im} f$ |
| Derived category $D(\mathcal{A})$ | formal inversion of quasi-isomorphisms in complexes over $\mathcal{A}$ |
| Preadditive | hom-sets are abelian groups, composition is bilinear |
| Biproduct | simultaneous product and coproduct (coincide in abelian categories) |
