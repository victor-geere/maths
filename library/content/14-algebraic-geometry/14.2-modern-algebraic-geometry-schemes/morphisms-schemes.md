---
title: Morphisms of Schemes
tag: algebraic-geometry
summary: Maps between schemes that respect the local ring structure — classified by properties like finiteness, flatness, smoothness, and properness that control geometric behaviour.
links:
  - schemes
  - sheaves
  - rational-maps
---

# Morphisms of Schemes

A **morphism of schemes** $f : X \to Y$ is a continuous map on the underlying topological spaces together with a compatible map of sheaves of rings $f^\# : \mathcal{O}_Y \to f_*\mathcal{O}_X$. For affine schemes, morphisms correspond exactly to ring homomorphisms in the opposite direction: $\text{Hom}(\text{Spec}(A), \text{Spec}(B)) \cong \text{Hom}_{\text{Ring}}(B, A)$. The classification of morphisms by their geometric properties — **finite**, **flat**, **smooth**, **proper**, **étale** — is fundamental to the structure theory of schemes and underlies all of modern algebraic geometry. These properties generalise the classical notions of finiteness, ramification, and compactness to the full generality of the scheme-theoretic setting.

## Definition

A **morphism** $f : (X, \mathcal{O}_X) \to (Y, \mathcal{O}_Y)$ of schemes is a pair:

- A continuous map $f : X \to Y$ of topological spaces
- A morphism of sheaves of rings $f^\# : \mathcal{O}_Y \to f_*\mathcal{O}_X$ (a ring map on each open set, compatible with $f$)

such that the induced maps on stalks are **local ring homomorphisms**.

## Affine Case

$$\text{Hom}_{\text{Sch}}(\text{Spec}(A), \text{Spec}(B)) \cong \text{Hom}_{\text{Ring}}(B, A)$$

Morphisms of affine schemes are equivalent (contravariantly) to ring homomorphisms.

## Key Classes of Morphisms

| Property | Geometric meaning |
|---|---|
| **Finite** | locally $A \to B$ with $B$ a finite $A$-module |
| **Flat** | fibres vary continuously in families; $B$ is a flat $A$-module |
| **Smooth** | fibres are smooth varieties; generalises submersion |
| **Étale** | smooth of relative dimension 0; local isomorphism |
| **Proper** | generalises compact; closed map with proper fibres |
| **Open immersion** | isomorphism onto an open subscheme |
| **Closed immersion** | corresponds to a surjective ring map $A \twoheadrightarrow A/I$ |

## Base Change

Given $f : X \to S$ and $g : T \to S$, the **fibre product** $X \times_S T$ is the scheme whose points are pairs $(x,t)$ with $f(x) = g(t)$. This is the fundamental tool for studying families and fibres.

## Fibres

The **fibre** of $f : X \to Y$ over a point $y \in Y$ is $X_y = X \times_Y \text{Spec}(k(y))$ where $k(y)$ is the residue field at $y$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f : X \to Y$ | morphism of schemes |
| $f^\#$ | the sheaf map $\mathcal{O}_Y \to f_*\mathcal{O}_X$ |
| $f_*\mathcal{O}_X$ | pushforward sheaf: $(f_*\mathcal{O}_X)(U) = \mathcal{O}_X(f^{-1}U)$ |
| Local ring homomorphism | maps the maximal ideal into the maximal ideal |
| Flat morphism | $B$ is flat as an $A$-module; fibres vary in algebraic families |
| Étale morphism | smooth of relative dimension 0; local isomorphism |
| Proper morphism | universally closed with finite fibres; generalises compact |
| Fibre product $X \times_S T$ | the scheme fitting into a pullback square over base $S$ |
| Residue field $k(y)$ | $\mathcal{O}_{Y,y}/\mathfrak{m}_y$ at point $y \in Y$ |
| Base change | replacing the base scheme $S$ by another $T$ via $T \to S$ |
| Closed immersion | morphism corresponding to $A \to A/I$ (imposing equations) |
