---
title: Products & Coproducts
tag: category-theory
summary: The categorical generalisation of Cartesian products and disjoint unions — defined by universal mapping properties rather than explicit set-theoretic constructions.
links:
  - categories-morphisms
  - opposite-categories
  - limits-colimits
  - initial-terminal-objects
---

# Products & Coproducts

The **product** and **coproduct** are the categorical generalisations of Cartesian products and disjoint unions. Rather than being defined by their elements, they are defined by **universal properties**: the product $A \times B$ is the object that "maps in" from any object with maps to both $A$ and $B$; the coproduct $A + B$ is the object that "maps out" to any object receiving maps from both $A$ and $B$. These are dual notions — coproduct is the product in $\mathcal{C}^{\text{op}}$. The same definition of product applies in **Set** (Cartesian product), **Grp** (direct product), **Top** (product topology), and **Vect** (direct sum), while coproducts realise as disjoint unions, free products, disjoint unions with topology, and direct sums — all captured by the same categorical abstraction.

## Product

The **product** of objects $A$ and $B$ is an object $A \times B$ together with **projection morphisms** $\pi_1 : A \times B \to A$ and $\pi_2 : A \times B \to B$, such that for any object $C$ and morphisms $f : C \to A$, $g : C \to B$, there exists a **unique** morphism $\langle f, g \rangle : C \to A \times B$ with $\pi_1 \circ \langle f,g\rangle = f$ and $\pi_2 \circ \langle f,g\rangle = g$.

## Coproduct

The **coproduct** of $A$ and $B$ is an object $A + B$ (or $A \sqcup B$) with **injection morphisms** $\iota_1 : A \to A+B$ and $\iota_2 : B \to A+B$, such that for any $C$ with $f : A \to C$, $g : B \to C$, there exists unique $[f,g] : A+B \to C$ with $[f,g] \circ \iota_1 = f$ and $[f,g] \circ \iota_2 = g$.

## Examples

| Category | Product $A \times B$ | Coproduct $A + B$ |
|---|---|---|
| **Set** | Cartesian product $\{(a,b)\}$ | Disjoint union $A \sqcup B$ |
| **Grp** | Direct product $G \times H$ | Free product $G * H$ |
| **Ab** | Direct product $A \oplus B$ | Direct sum $A \oplus B$ (coincide) |
| **Top** | Product topology | Disjoint union topology |
| **Vect$_k$** | Direct sum $V \oplus W$ | Direct sum $V \oplus W$ (coincide) |
| **Set** with $n$ objects | $n$-fold product | $n$-fold disjoint union |

## Finite Products and the Terminal Object

A **terminal object** is the empty product (product of zero objects), i.e. $\prod_\emptyset = 1$.

Similarly, the **initial object** is the empty coproduct.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $A \times B$ | product of $A$ and $B$ |
| $\pi_1, \pi_2$ | projection morphisms from the product |
| $\langle f, g\rangle$ | the unique morphism into the product induced by $f$ and $g$ |
| $A + B$ or $A \sqcup B$ | coproduct of $A$ and $B$ |
| $\iota_1, \iota_2$ | injection morphisms into the coproduct |
| $[f,g]$ | the unique morphism out of the coproduct induced by $f$ and $g$ |
| Universal property | characterisation by a unique factorisation condition |
| $A \oplus B$ | direct sum — coincides with product and coproduct in abelian categories |
| Free product $G * H$ | coproduct in **Grp**: presentations are concatenated |
| Dual | product and coproduct are dual (one is the other in $\mathcal{C}^{\text{op}}$) |
