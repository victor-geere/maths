---
title: Initial & Terminal Objects
tag: category-theory
summary: An initial object has a unique morphism to every object; a terminal object receives a unique morphism from every object — the simplest universal properties.
links:
  - categories-morphisms
  - opposite-categories
  - products-coproducts
  - limits-colimits
---

# Initial & Terminal Objects

**Initial** and **terminal objects** are the simplest examples of **universal properties** — a cornerstone concept in category theory. An **initial object** $0$ has a unique morphism from it to every other object; a **terminal object** $1$ has a unique morphism from every other object to it. These are dual notions: the terminal objects of $\mathcal{C}$ are the initial objects of $\mathcal{C}^{\text{op}}$. Both are unique up to unique isomorphism when they exist. The universality makes them canonical: in **Set**, the empty set is initial (the unique map from $\emptyset$ to any set) and any singleton is terminal. This pattern repeats across mathematics — zero objects, empty products, trivial groups — all captured by the same categorical definition.

## Definitions

An object $0 \in \mathcal{C}$ is **initial** if for every object $A \in \mathcal{C}$, there exists a **unique** morphism $!_A : 0 \to A$.

An object $1 \in \mathcal{C}$ is **terminal** if for every object $A \in \mathcal{C}$, there exists a **unique** morphism $!^A : A \to 1$.

## Uniqueness Up to Isomorphism

If $0$ and $0'$ are both initial, there is a unique isomorphism $0 \cong 0'$. (The composite of the unique maps $0 \to 0' \to 0$ must be $\text{id}_0$ by uniqueness.) Same for terminal objects.

## Examples

| Category | Initial object | Terminal object |
|---|---|---|
| **Set** | $\emptyset$ (empty set) | $\{*\}$ (any singleton) |
| **Grp** | $\{e\}$ (trivial group) | $\{e\}$ (trivial group) |
| **Top** | $\emptyset$ | $\{*\}$ |
| **Ring** (with 1) | $\mathbb{Z}$ | $\{0\}$ (zero ring) |
| **Vect$_k$** | $\{0\}$ (zero space) | $\{0\}$ (zero space) |
| A poset | minimum element (if exists) | maximum element (if exists) |

## Zero Object

An object that is both initial and terminal is a **zero object** (or null object). Categories with a zero object include **Grp**, **Ab**, **Vect$_k$**, and **$R$-Mod**.

## Universal Property

Both notions exemplify the **universal property** pattern: an object specified (up to unique isomorphism) by a mapping property involving all other objects. Limits, colimits, products, and adjunctions all follow this pattern.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Initial object $0$ | unique morphism $0 \to A$ for every $A$ |
| Terminal object $1$ | unique morphism $A \to 1$ for every $A$ |
| $!_A : 0 \to A$ | the unique morphism from the initial object to $A$ |
| $!^A : A \to 1$ | the unique morphism from $A$ to the terminal object |
| Zero object | both initial and terminal; has unique maps to and from every object |
| Universal property | a characterisation of an object by morphism conditions |
| Unique up to isomorphism | any two objects satisfying the same universal property are isomorphic |
| $\mathbb{Z}$ | the integers — the initial object in **Ring** (with 1) |
| $\emptyset$ | the empty set — the initial object in **Set** |
| $\{*\}$ | a one-element set — the terminal object in **Set** |
