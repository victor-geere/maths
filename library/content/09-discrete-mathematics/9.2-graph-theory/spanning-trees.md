---
title: Minimum Spanning Trees
tag: algorithms
summary: A spanning tree of minimum total edge weight, found greedily by Kruskal's or Prim's algorithm.
links:
  - paths-cycles-trees
  - graphs-basics
  - dijkstra
  - big-o-notation
---

# Minimum Spanning Trees

A **spanning tree** of a connected weighted graph is a subgraph that is a tree (connected, acyclic) and includes all $n$ vertices. Among all spanning trees, the **minimum spanning tree (MST)** has the smallest total edge weight. MSTs arise in network design — finding the cheapest way to connect all cities by roads, or all computers in a network — and also appear in clustering algorithms, image segmentation, and approximation algorithms for the travelling salesman problem. The two classical greedy algorithms (Kruskal's and Prim's) are both provably optimal and run efficiently in practice.

## Definition

For a connected weighted graph $G = (V, E, w)$, an **MST** is a spanning tree $T$ minimising:

$$w(T) = \sum_{e \in T} w(e)$$

## Kruskal's Algorithm

**Greedy by edges:** sort edges by weight, add each edge if it doesn't form a cycle.

1. Sort all edges: $e_1, e_2, \ldots$ with $w(e_1) \leq w(e_2) \leq \cdots$
2. $T \leftarrow \emptyset$
3. For each edge $e_i$: if $T \cup \{e_i\}$ is acyclic, add $e_i$ to $T$.
4. Stop when $|T| = n-1$.

**Complexity:** $O(E \log E)$ (dominated by sorting). Uses **Union-Find** to detect cycles.

## Prim's Algorithm

**Greedy by vertices:** grow the MST one vertex at a time, always adding the cheapest edge crossing the cut.

1. Start with any vertex $s$; mark it visited.
2. Repeat until all vertices visited: add the minimum-weight edge from any visited vertex to any unvisited vertex.

**Complexity:** $O(E \log V)$ with a binary heap; $O(E + V \log V)$ with a Fibonacci heap.

## Cut Property (Correctness)

For any partition of $V$ into $(S, V \setminus S)$, the minimum-weight edge crossing the cut is in **every** MST. Both Kruskal's and Prim's algorithms are correct by this property.

## Uniqueness

If all edge weights are distinct, the MST is **unique**. With ties, multiple MSTs may exist but all have the same total weight.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Spanning tree | acyclic connected subgraph containing all $n$ vertices |
| MST | Minimum Spanning Tree — spanning tree of minimum total weight |
| $w(T)$ | total weight of spanning tree $T$ |
| Kruskal's algorithm | sorts edges and adds cheapest non-cycle-forming edges |
| Prim's algorithm | grows tree by adding cheapest cut edge |
| Cut property | lightest edge crossing a cut belongs to an MST |
| Union-Find | data structure tracking connected components; supports merge and find in near-$O(1)$ |
| $O(E \log E)$ | time for Kruskal; sorting dominates |
| $O(E \log V)$ | time for Prim with binary heap |
| Cycle | adding an edge to a tree creates exactly one cycle |
| Cut $(S, V\setminus S)$ | partition of vertices; crossing edges connect the two parts |
