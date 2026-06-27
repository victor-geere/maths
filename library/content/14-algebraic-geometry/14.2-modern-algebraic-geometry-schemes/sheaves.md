---
title: Sheaves
tag: algebraic-geometry
summary: A sheaf assigns data (functions, sections) to open sets of a space in a way that is consistent on overlaps — the fundamental tool for tracking local-to-global information.
links:
  - schemes
  - sheaf-cohomology
  - topos-theory
  - divisors-line-bundles
---

# Sheaves

A **sheaf** on a topological space $X$ is a systematic way of assigning algebraic data (sets, groups, rings, modules) to each open set of $X$, with the data on overlapping sets being consistent. Sheaves encode the idea that **local data can be glued to global data**: if you know a function on each piece of an open cover, and the pieces agree on overlaps, you can assemble them into a global function. This local-to-global principle is fundamental in geometry and analysis: holomorphic functions, differential forms, and sections of vector bundles are all sheaves. Grothendieck elevated sheaves to the foundation of algebraic geometry — schemes are built from sheaves of rings — and sheaf cohomology measures the obstruction to constructing global sections from local ones.

## Presheaf

A **presheaf** $\mathcal{F}$ of abelian groups on $X$ is an assignment:

- For each open $U \subseteq X$: an abelian group $\mathcal{F}(U)$ (the **sections** over $U$)
- For each inclusion $V \subseteq U$: a restriction map $\rho_{UV} : \mathcal{F}(U) \to \mathcal{F}(V)$

satisfying $\rho_{UU} = \text{id}$ and $\rho_{VW} \circ \rho_{UV} = \rho_{UW}$.

## Sheaf Axioms

A presheaf $\mathcal{F}$ is a **sheaf** if it satisfies:

1. **Identity:** if $\{U_i\}$ covers $U$ and $s, t \in \mathcal{F}(U)$ agree on each $U_i$, then $s = t$
2. **Gluing:** if $s_i \in \mathcal{F}(U_i)$ agree on overlaps ($\rho(s_i)|_{U_i \cap U_j} = \rho(s_j)|_{U_i \cap U_j}$), there exists $s \in \mathcal{F}(U)$ restricting to each $s_i$

## Standard Examples

| Sheaf | Space $X$ | $\mathcal{F}(U)$ |
|---|---|---|
| $\mathcal{O}_X$ (structure sheaf) | manifold or variety | smooth/regular functions on $U$ |
| $\mathcal{C}^\infty_X$ | smooth manifold | $C^\infty$ functions on $U$ |
| $\Omega^k_X$ | smooth manifold | $k$-forms on $U$ |
| Constant sheaf $\underline{\mathbb{Z}}$ | any space | locally constant $\mathbb{Z}$-valued functions |

## Stalks

The **stalk** of $\mathcal{F}$ at a point $x$ is the direct limit of $\mathcal{F}(U)$ over all open sets containing $x$:

$$\mathcal{F}_x = \varinjlim_{U \ni x} \mathcal{F}(U)$$

Elements of $\mathcal{F}_x$ are called **germs**.

## Morphisms and Exact Sequences

A **morphism** $\phi : \mathcal{F} \to \mathcal{G}$ of sheaves is a collection of group homomorphisms $\phi_U : \mathcal{F}(U) \to \mathcal{G}(U)$ compatible with restrictions. Sheaves form an **abelian category**.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mathcal{F}$ | a sheaf (or presheaf) |
| $\mathcal{F}(U)$ | sections of $\mathcal{F}$ over open set $U$ |
| $\Gamma(U, \mathcal{F}) = \mathcal{F}(U)$ | alternative notation for sections |
| $\rho_{UV}$ | restriction map $\mathcal{F}(U) \to \mathcal{F}(V)$ for $V \subseteq U$ |
| Gluing | assembling compatible local sections into a global section |
| Stalk $\mathcal{F}_x$ | direct limit of $\mathcal{F}(U)$ over neighbourhoods of $x$ |
| Germ | an element of the stalk $\mathcal{F}_x$ |
| $\mathcal{O}_X$ | structure sheaf of a variety or scheme: ring of regular functions |
| $\varinjlim$ | direct limit (colimit over a directed system) |
| Abelian category | the category of sheaves; exact sequences make sense |
| Presheaf | satisfies functoriality but not the sheaf axioms |
