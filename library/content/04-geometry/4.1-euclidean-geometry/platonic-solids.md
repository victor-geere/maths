---
title: Platonic Solids
tag: geometry
summary: The five convex regular polyhedra, each with identical regular polygonal faces meeting at equal angles.
links:
  - eulers-polyhedra
  - volumes-surface-areas
---

# Platonic Solids

A **Platonic solid** is a convex polyhedron in which every face is the same regular polygon and the same number of faces meet at every vertex. Plato associated them with the classical elements (fire, earth, air, water, and the cosmos), but their mathematical significance is that there are **exactly five** of them — a fact proved by Euclid in the *Elements* and resting on the constraint that the angles around each vertex must sum to less than $360°$.

## The Five Platonic Solids

| Solid | Faces | Face shape | Edges | Vertices | $V - E + F$ |
|---|---|---|---|---|---|
| Tetrahedron | 4 | Equilateral triangle | 6 | 4 | 2 |
| Cube (Hexahedron) | 6 | Square | 12 | 8 | 2 |
| Octahedron | 8 | Equilateral triangle | 12 | 6 | 2 |
| Dodecahedron | 12 | Regular pentagon | 30 | 20 | 2 |
| Icosahedron | 20 | Equilateral triangle | 30 | 12 | 2 |

Every Platonic solid satisfies **Euler's formula** $V - E + F = 2$.

## Why Only Five?

At each vertex, the interior angles of the meeting faces must sum to **less than $360°$** (otherwise they lie flat or fold outward). This gives:

- Triangular faces ($60°$ each): at most 5 per vertex → tetrahedron (3), octahedron (4), icosahedron (5)
- Square faces ($90°$ each): at most 3 per vertex → cube (3)
- Pentagonal faces ($108°$ each): at most 3 per vertex → dodecahedron (3)
- Hexagonal faces ($120°$ each): $3 \times 120° = 360°$ — lies flat, so no solid

## Duality

The Platonic solids come in **dual pairs**: swap vertices and face-centres to obtain the dual.

- Tetrahedron ↔ Tetrahedron (self-dual)
- Cube ↔ Octahedron
- Dodecahedron ↔ Icosahedron

## Schläfli Symbol

Each Platonic solid has a Schläfli symbol $\{p, q\}$ denoting $p$-gon faces with $q$ meeting at each vertex:
tetrahedron $\{3,3\}$, cube $\{4,3\}$, octahedron $\{3,4\}$, dodecahedron $\{5,3\}$, icosahedron $\{3,5\}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Polyhedron | a solid bounded by flat polygonal faces |
| Convex | no interior point lies outside the solid's faces extended |
| Regular polygon | a polygon with all sides and angles equal |
| Face | a flat polygonal surface of a polyhedron |
| Edge | a line segment where two faces meet |
| Vertex (pl. vertices) | a corner point where edges meet |
| $V, E, F$ | number of vertices, edges, faces |
| Euler's formula | $V - E + F = 2$ for any convex polyhedron |
| Dual polyhedron | obtained by placing a vertex at each face-centre and connecting adjacent ones |
| Schläfli symbol $\{p,q\}$ | $p$-gon faces, $q$ meeting at each vertex |
| Dihedral angle | the angle between two adjacent faces along their shared edge |
