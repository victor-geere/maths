---
title: Galois Theory (Overview)
tag: abstract-algebra
summary: Connecting field extensions to group theory to determine polynomial solvability.
links:
  - field-extensions
  - field-axioms
  - symmetric-groups
  - quotient-groups
---

## Central Idea

Galois theory establishes a correspondence between:

- **Intermediate fields** $F \subseteq K \subseteq E$
- **Subgroups** of the **Galois group** $\text{Gal}(E/F)$

## Galois Group

For a **Galois extension** $E/F$ (normal + separable), the Galois group is:

$$\text{Gal}(E/F) = \{\sigma : E \to E \mid \sigma \text{ is a field automorphism fixing } F\}$$

Under composition, this forms a group of order $[E:F]$.

## Fundamental Theorem of Galois Theory

There is an **order-reversing bijection**:

$$\{\text{intermediate fields } K\} \longleftrightarrow \{\text{subgroups } H \leq \text{Gal}(E/F)\}$$

$$K \longmapsto \text{Gal}(E/K), \qquad H \longmapsto E^H \text{ (fixed field)}$$

## Solvability by Radicals

A polynomial $f \in \mathbb{Q}[x]$ is **solvable by radicals** iff its Galois group (over $\mathbb{Q}$) is a **solvable group**.

- Degree $\leq 4$: Galois groups are always solvable → explicit formulas exist (e.g. quadratic, cubic, quartic formulas).
- Degree $\geq 5$: generic polynomials have Galois group $S_5$, which is **not solvable** → no general radical formula (Abel–Ruffini theorem).

## Example

$f(x) = x^2 - 2$ over $\mathbb{Q}$: splitting field $\mathbb{Q}(\sqrt{2})$, $\text{Gal} \cong \mathbb{Z}/2\mathbb{Z}$.

## Notes

- Galois theory resolved the centuries-old question of which polynomial equations are solvable.
- It unifies number theory, algebra, and geometry at a deep level.
