---
title: Planar Graphs & Euler's Formula
tag: graph-theory
summary: Graphs that can be drawn in the plane without crossing edges, characterised by Euler's formula V−E+F=2 and Kuratowski's theorem.
links:
  - graphs-basics
  - euler-characteristic
  - graph-colouring
  - connectivity
---

# Planar Graphs & Euler's Formula

A **planar graph** is one that can be drawn in the plane so that no two edges cross. The roads of a city, printed circuit board traces, and many natural networks are planar. Planarity imposes strong constraints on the structure: **Euler's formula** $V - E + F = 2$ relates vertices, edges, and faces of any planar embedding, and it implies that a planar graph on $n$ vertices has at most $3n - 6$ edges — far fewer than the $\binom{n}{2}$ possible. **Kuratowski's theorem** gives the complete characterisation: a graph is planar if and only if it contains no subdivision of $K_5$ or $K_{3,3}$.

## Definition

$G$ is **planar** if it can be drawn in the plane $\mathbb{R}^2$ (or equivalently the sphere $S^2$) with edges as curves that intersect only at their endpoints. Such a drawing is a **planar embedding**.

## Euler's Formula

For any connected planar graph with a planar embedding:

$$V - E + F = 2$$

where $F$ includes the **unbounded outer face**.

## Consequences of Euler's Formula

For simple connected planar graphs with $V \geq 3$:

$$E \leq 3V - 6$$

For triangle-free planar graphs:

$$E \leq 2V - 4$$

**Proof:** Each face is bounded by $\geq 3$ edges; each edge borders 2 faces. So $3F \leq 2E$. Combine with $E = V + F - 2$.

## Kuratowski's Theorem

$G$ is planar $\iff$ it contains no **subdivision** of $K_5$ or $K_{3,3}$.

(A subdivision replaces edges with paths.)

## The Four Colour Theorem

Every planar graph is **4-colourable**: the vertices can be coloured with 4 colours so no two adjacent vertices share a colour. This was proved in 1976 by Appel and Haken — the first major theorem proved with extensive computer assistance.

## Non-Planar Examples

- $K_5$ (5 vertices, 10 edges): $E = 10 > 3(5)-6 = 9$, so not planar by the edge bound.
- $K_{3,3}$ (6 vertices, 9 edges, triangle-free): $E = 9 > 2(6)-4 = 8$, so not planar.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Planar graph | drawable in the plane with no crossing edges |
| Planar embedding | a specific crossing-free drawing |
| $V, E, F$ | vertices, edges, faces (including the outer face) |
| $V - E + F = 2$ | Euler's formula for connected planar graphs |
| Face | a region bounded by edges in a planar embedding |
| Outer face | the unbounded region surrounding the drawing |
| Kuratowski's theorem | planar $\iff$ no subdivision of $K_5$ or $K_{3,3}$ |
| Subdivision | replacing each edge with a path of length $\geq 1$ |
| $K_5$ | complete graph on 5 vertices — the simplest non-planar graph |
| $K_{3,3}$ | complete bipartite graph on $3+3$ vertices — the other obstruction |
| Four Colour Theorem | every planar graph is 4-colourable |
| Triangle-free | contains no $C_3$ (3-cycle) |
