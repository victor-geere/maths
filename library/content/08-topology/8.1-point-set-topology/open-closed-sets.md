---
title: Open & Closed Sets
tag: topology
summary: The fundamental building blocks of topology — open sets define the structure of a topological space, and closed sets are their complements.
links:
  - topological-spaces
  - metric-spaces
  - compactness
  - connectedness
---

# Open & Closed Sets

**Open sets** and **closed sets** are the foundational objects from which all of topology is built. In a metric space, an open set is one where every point has a small ball entirely contained within it — no point is on the "edge". A closed set is one that contains all its limit points. But the revolutionary insight of point-set topology is that these intuitive notions can be abstracted: rather than defining openness via a metric, we can simply *declare* which sets are open, subject to three axioms. This shifts the focus from distance to the qualitative structure of nearness, enabling topology to study shape and continuity in spaces where no natural distance exists.

## Open Sets in a Metric Space

In a metric space $(X, d)$, a set $U \subseteq X$ is **open** if:

$$\forall\, x \in U,\; \exists\, \varepsilon > 0 : B(x, \varepsilon) \subseteq U$$

Every point has a neighbourhood ball fitting inside $U$.

## Closed Sets

A set $F \subseteq X$ is **closed** if its complement $X \setminus F$ is open.

Equivalently, $F$ is closed iff it contains all its **limit points**: if $x_n \in F$ and $x_n \to x$, then $x \in F$.

## Properties

For a collection of sets in any topological space:

| Open sets | Closed sets |
|---|---|
| $\emptyset$ and $X$ are open | $\emptyset$ and $X$ are closed |
| Arbitrary unions of open sets are open | Arbitrary intersections of closed sets are closed |
| Finite intersections of open sets are open | Finite unions of closed sets are closed |

## Neither, Both, or Either

- $[0, 1]$ is closed (not open) in $\mathbb{R}$
- $(0, 1)$ is open (not closed) in $\mathbb{R}$
- $[0, 1)$ is neither open nor closed in $\mathbb{R}$
- $\emptyset$ and $\mathbb{R}$ are both open and closed (**clopen**)

## Closure, Interior, Boundary

For any set $A \subseteq X$:

- **Interior** $A^\circ$: the largest open set contained in $A$
- **Closure** $\overline{A}$: the smallest closed set containing $A$
- **Boundary** $\partial A = \overline{A} \setminus A^\circ$: points on the "edge"

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $B(x, \varepsilon)$ | open ball of radius $\varepsilon$ centred at $x$ |
| Open set | every point has a neighbourhood contained in the set |
| Closed set | complement is open; contains all limit points |
| Limit point | $x$ is a limit point of $A$ if every neighbourhood of $x$ meets $A \setminus \{x\}$ |
| Clopen | simultaneously open and closed |
| $A^\circ$ | interior of $A$ — largest open subset |
| $\overline{A}$ | closure of $A$ — smallest closed superset |
| $\partial A$ | boundary of $A$: $\overline{A} \setminus A^\circ$ |
| $X \setminus F$ | complement of $F$ in $X$ |
| Neighbourhood | an open set containing a given point |
