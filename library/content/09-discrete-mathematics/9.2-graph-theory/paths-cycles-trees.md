---
title: Paths, Cycles, Trees
tag: graph-theory
summary: Paths traverse vertices without repetition, cycles return to their start, and trees are connected acyclic graphs — three fundamental structural concepts in graph theory.
links:
  - graphs-basics
  - connectivity
  - spanning-trees
---

# Paths, Cycles, Trees

A **path** in a graph is a sequence of distinct vertices connected by edges — a route from one vertex to another. A **cycle** is a closed path, returning to its starting vertex. A **tree** is a connected graph with no cycles: the minimal structure that keeps all vertices linked. These three concepts form the vocabulary for almost all structural questions in graph theory. Trees appear throughout computer science (decision trees, heaps, parse trees), biology (phylogenetic trees), and network design (spanning trees minimise the edges needed to connect everything).

## Paths and Walks

A **walk** of length $k$: a sequence $v_0, e_1, v_1, e_2, v_2, \ldots, e_k, v_k$ where each $e_i = \{v_{i-1}, v_i\}$.

A **path**: a walk with no repeated **vertices**.

A **trail**: a walk with no repeated **edges** (vertices may repeat).

An **Eulerian trail** traverses every edge exactly once; an **Eulerian circuit** returns to the start.

## Cycles

A **cycle** $C = v_0, v_1, \ldots, v_{k-1}, v_0$ visits $k \geq 3$ distinct vertices in order, with $v_0 = v_k$.

**Girth:** the length of the shortest cycle in $G$.

**Hamilton cycle:** a cycle visiting every vertex exactly once.

## Trees

A **tree** is a connected acyclic graph. Equivalent characterisations of a tree on $n$ vertices:

1. Connected with $n-1$ edges
2. Acyclic with $n-1$ edges
3. Connected and acyclic
4. Every pair of vertices has a unique path between them

**Leaf:** a vertex of degree 1.

**Rooted tree:** a tree with one designated vertex as the **root**; induces parent-child structure.

## Spanning Trees

A **spanning tree** of a connected graph $G$ is a subgraph that is a tree and includes all vertices of $G$.

Every connected graph has at least one spanning tree.

## Cayley's Formula

The number of labelled trees on $n$ vertices is $n^{n-2}$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Walk | sequence of vertices/edges; repetition allowed |
| Path | walk with no repeated vertices |
| Trail | walk with no repeated edges |
| Cycle | closed path of length $\geq 3$ |
| Girth | length of the shortest cycle |
| Acyclic | containing no cycles |
| Tree | connected, acyclic graph |
| Leaf | vertex of degree 1 in a tree |
| Root | distinguished vertex in a rooted tree |
| Spanning tree | a tree subgraph including all vertices |
| Eulerian circuit | trail traversing every edge exactly once |
| Hamiltonian cycle | cycle visiting every vertex exactly once |
| Cayley's formula | $n^{n-2}$ labelled trees on $n$ vertices |
| $n-1$ edges | the edge count of any tree on $n$ vertices |
