---
title: Graph Colouring
tag: algorithms
summary: Assigning colours to vertices (or edges) so that no two adjacent elements share a colour, minimised by the chromatic number.
links:
  - graphs-basics
  - bipartite-graphs
  - planar-graphs
  - ramsey-theory
---

# Graph Colouring

**Graph colouring** asks for the minimum number of colours needed to label vertices so that no two adjacent vertices share the same colour. This minimum is the **chromatic number** $\chi(G)$. The problem models scheduling conflicts (assign time slots to events that cannot overlap), register allocation in compilers, and frequency assignment in wireless networks. Though simple to state, it is NP-complete in general — no efficient algorithm is known for finding the exact chromatic number of an arbitrary graph. The **four colour theorem** proves $\chi(G) \leq 4$ for all planar graphs, and **Brooks' theorem** gives a tight upper bound for all graphs.

## Proper Colouring

A **proper $k$-colouring** of $G$ assigns a colour from $\{1, \ldots, k\}$ to each vertex such that adjacent vertices receive different colours.

The **chromatic number** $\chi(G)$ = minimum $k$ for which a proper $k$-colouring exists.

## Basic Bounds

$$\omega(G) \leq \chi(G) \leq \Delta(G) + 1$$

where $\omega(G)$ = **clique number** (largest complete subgraph) and $\Delta(G)$ = maximum degree.

## Brooks' Theorem

For a connected graph $G$ that is neither complete nor an odd cycle:

$$\chi(G) \leq \Delta(G)$$

## Standard Values

| Graph | $\chi$ |
|---|---|
| Bipartite (non-empty) | 2 |
| Odd cycle $C_{2k+1}$ | 3 |
| $K_n$ | $n$ |
| Planar graph | $\leq 4$ (Four Colour Theorem) |
| Tree | 2 (bipartite) |
| Petersen graph | 3 |

## Greedy Colouring

Colour vertices in any order: assign the smallest colour not used by any already-coloured neighbour.

**Guarantee:** $\chi(G) \leq \Delta(G) + 1$ (achieved by greedy in the worst order).

## Edge Colouring

A **proper edge colouring** assigns colours to edges so no two edges sharing a vertex have the same colour.

**Vizing's Theorem:** $\chi'(G) \in \{\Delta(G), \Delta(G)+1\}$ for any simple graph.

## Chromatic Polynomial

$P(G, k)$ = number of proper $k$-colourings of $G$. It is a polynomial in $k$, and $\chi(G)$ is the smallest positive integer $k$ with $P(G,k) > 0$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\chi(G)$ | chromatic number — minimum colours for a proper colouring |
| $\chi'(G)$ | chromatic index — minimum colours for a proper edge colouring |
| $\omega(G)$ | clique number — size of largest complete subgraph |
| $\Delta(G)$ | maximum degree of any vertex |
| Proper colouring | no two adjacent vertices (or edges) share a colour |
| Clique | a complete subgraph; needs $\omega$ colours |
| Brooks' theorem | $\chi(G) \leq \Delta(G)$ except for $K_n$ and odd cycles |
| Vizing's theorem | $\chi'(G) = \Delta$ or $\Delta+1$ |
| Four Colour Theorem | $\chi(G) \leq 4$ for all planar $G$ |
| Chromatic polynomial $P(G,k)$ | counts proper $k$-colourings |
| NP-complete | no polynomial-time algorithm known; determining $\chi(G)$ is NP-hard |
