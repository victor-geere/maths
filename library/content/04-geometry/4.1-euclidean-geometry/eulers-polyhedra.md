---
title: Euler's Formula for Polyhedra (V−E+F=2)
tag: geometry
summary: For any convex polyhedron, the number of vertices minus edges plus faces always equals 2.
links:
  - platonic-solids
  - volumes-surface-areas
---

# Euler's Formula for Polyhedra (V−E+F=2)

Euler's polyhedron formula states that for any **convex polyhedron**, the counts of its vertices, edges, and faces are not independent: they are always locked together by the equation $V - E + F = 2$. First noticed by Descartes and proved by Euler in 1752, this is one of the earliest results in what would become **topology** — the study of properties preserved under continuous deformations. The number $2$ is the **Euler characteristic** of the sphere.

## Statement

For any convex polyhedron with $V$ vertices, $E$ edges, and $F$ faces:

$$V - E + F = 2$$

## Verification on Platonic Solids

| Solid | $V$ | $E$ | $F$ | $V-E+F$ |
|---|---|---|---|---|
| Tetrahedron | 4 | 6 | 4 | **2** |
| Cube | 8 | 12 | 6 | **2** |
| Octahedron | 6 | 12 | 8 | **2** |
| Dodecahedron | 20 | 30 | 12 | **2** |
| Icosahedron | 12 | 30 | 20 | **2** |

## Proof (Network / Graph Approach)

1. **Flatten:** project the polyhedron onto a plane (keeping one face as the outer region).
2. You have a planar graph with $V$ vertices, $E$ edges, $F - 1$ bounded faces (the outer face counts as one).
3. **Spanning tree:** choose a spanning tree of the graph ($V - 1$ edges, no cycles). It spans all $V$ vertices using $V - 1$ edges.
4. Each of the remaining $E - (V-1)$ edges adds exactly one new face. Since we start with 1 face:

$$F = 1 + (E - V + 1) \implies V - E + F = 2 \quad \square$$

## Generalisation: Euler Characteristic

For surfaces of genus $g$ (a torus has genus 1):

$$V - E + F = 2 - 2g$$

- Sphere ($g = 0$): $\chi = 2$
- Torus ($g = 1$): $\chi = 0$
- Double torus ($g = 2$): $\chi = -2$

## Consequence: Classification of Regular Polyhedra

Euler's formula, together with the constraint that $p$-gon faces ($p \geq 3$) meet in groups of $q \geq 3$, yields exactly **five** solutions — the Platonic solids.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $V$ | number of vertices |
| $E$ | number of edges |
| $F$ | number of faces |
| $\chi$ (chi) | Euler characteristic ($\chi = V - E + F$) |
| Convex polyhedron | solid where any line segment between two interior points stays inside |
| Genus $g$ | number of "handles" on a surface (torus has $g=1$) |
| Planar graph | a graph that can be drawn in the plane with no edge crossings |
| Spanning tree | a subgraph connecting all vertices with no cycles, using $V-1$ edges |
| Euler characteristic | topological invariant $V - E + F = 2 - 2g$ |
| Topology | branch of mathematics studying properties preserved under continuous deformations |
