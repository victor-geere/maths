---
title: Connectivity & Cuts
tag: graph-theory
summary: Measures of how well-connected a graph is — vertex connectivity, edge connectivity, and the cuts that separate a graph into components.
links:
  - graphs-basics
  - paths-cycles-trees
  - bfs-dfs
  - network-flow
---

# Connectivity & Cuts

**Connectivity** measures how robustly a graph stays connected when vertices or edges are removed. A highly connected graph remains intact even after many failures — relevant to network resilience, circuit design, and transportation systems. A **cut** is a set of vertices or edges whose removal disconnects the graph. The **connectivity** $\kappa(G)$ is the minimum number of vertices that must be removed to disconnect $G$ (or reduce it to a single vertex), and Menger's theorem relates this to the maximum number of internally vertex-disjoint paths between any pair. These concepts underpin network flow, Hamiltonian circuit algorithms, and the theory of planar graphs.

## Connected Components

$G$ is **connected** if there is a path between every pair of vertices. Otherwise, the maximal connected subgraphs are its **connected components**.

## Vertex Connectivity $\kappa(G)$

The **vertex connectivity** $\kappa(G)$ is the minimum number of vertices whose removal disconnects $G$ or leaves only one vertex.

- $\kappa(K_n) = n - 1$ (complete graph)
- $\kappa(\text{tree}) = 1$

A graph is **$k$-connected** if $\kappa(G) \geq k$.

## Edge Connectivity $\lambda(G)$

The **edge connectivity** $\lambda(G)$ is the minimum number of edges whose removal disconnects $G$.

$$\kappa(G) \leq \lambda(G) \leq \delta(G)$$

where $\delta(G) = \min_{v} \deg(v)$ is the minimum degree.

## Cuts

A **vertex cut** (separator) $S \subseteq V$ disconnects $G$ when removed.

An **edge cut** (cut set) $F \subseteq E$ disconnects $G$ when removed.

A **cut** $(S, \bar{S})$ partitions $V$ into two non-empty sets; the cut **capacity** is the number (or total weight) of edges crossing from $S$ to $\bar{S}$.

## Menger's Theorem

The maximum number of internally vertex-disjoint paths from $s$ to $t$ equals the minimum size of an $s$–$t$ vertex separator.

**Edge version:** max edge-disjoint $s$–$t$ paths = min $s$–$t$ edge cut.

## Bridge

An **edge** whose removal increases the number of connected components is a **bridge**. A **cut vertex** (articulation point) is a vertex whose removal increases connected components.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\kappa(G)$ | vertex connectivity |
| $\lambda(G)$ | edge connectivity |
| $\delta(G)$ | minimum degree of $G$ |
| $k$-connected | $\kappa(G) \geq k$ |
| Vertex cut | a set of vertices whose removal disconnects $G$ |
| Edge cut | a set of edges whose removal disconnects $G$ |
| Cut $(S, \bar{S})$ | bipartition of $V$; edges crossing it form the cut |
| Bridge | an edge whose removal disconnects the graph |
| Cut vertex / Articulation point | a vertex whose removal disconnects the graph |
| Menger's theorem | max disjoint paths = min separator size |
| Connected component | a maximal connected subgraph |
| $s$–$t$ path | a path from source $s$ to target $t$ |
