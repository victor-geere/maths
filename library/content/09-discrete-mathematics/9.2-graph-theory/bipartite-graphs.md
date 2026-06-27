---
title: Bipartite Graphs
tag: graph-theory
summary: Graphs whose vertices split into two independent sets, with edges only between the sets — characterised by containing no odd cycles.
links:
  - graphs-basics
  - paths-cycles-trees
  - graph-colouring
  - network-flow
---

# Bipartite Graphs

A **bipartite graph** is one whose vertex set can be split into two disjoint groups $A$ and $B$ such that every edge connects a vertex in $A$ to a vertex in $B$ — there are no edges within the same group. Bipartite graphs model two-sided matching problems: students and projects, workers and jobs, buyers and goods. The celebrated theorem of König relates maximum matchings to minimum vertex covers, and bipartite graphs are precisely the 2-colourable ones — those with no odd cycles. They appear throughout combinatorics, operations research, and computer science (bipartite matching is solvable in polynomial time).

## Definition

A graph $G = (V, E)$ is **bipartite** with bipartition $(A, B)$ if:

- $V = A \cup B$, $A \cap B = \emptyset$
- Every edge $\{u, v\} \in E$ has $u \in A$ and $v \in B$

## Characterisation

$G$ is bipartite $\iff$ $G$ contains **no odd-length cycles**.

**Proof (sketch):** 2-colour $G$ starting from any vertex using BFS. An odd cycle forces two vertices in the same colour class to be adjacent.

## Complete Bipartite Graph $K_{m,n}$

Every vertex in $A$ ($|A|=m$) is connected to every vertex in $B$ ($|B|=n$).

$$|E(K_{m,n})| = mn$$

## Matchings

A **matching** in $G$ is a set of edges with no shared vertices.

A **perfect matching** covers every vertex.

**Hall's Marriage Theorem:** a bipartite graph $G = (A \cup B, E)$ has a matching that saturates $A$ $\iff$ for every $S \subseteq A$: $|N(S)| \geq |S|$.

## König's Theorem

In a bipartite graph:

$$\text{size of maximum matching} = \text{size of minimum vertex cover}$$

(This fails for non-bipartite graphs.)

## Applications

- **Job assignment:** assign workers (A) to tasks (B) with matching
- **Network flow:** bipartite matching solved via max-flow
- **Coding theory:** parity-check matrices of linear codes are bipartite adjacency matrices

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Bipartite $(A, B)$ | graph with vertex partition $A \cup B$; edges only cross between $A$ and $B$ |
| $K_{m,n}$ | complete bipartite graph with parts of size $m$ and $n$ |
| Matching | set of edges with disjoint vertex sets |
| Perfect matching | matching that covers all vertices |
| $N(S)$ | neighbourhood of $S$: set of all neighbours of vertices in $S$ |
| Hall's theorem | $A$ is saturated $\iff$ $|N(S)| \geq |S|$ for all $S \subseteq A$ |
| Vertex cover | a set of vertices incident to every edge |
| König's theorem | max matching = min vertex cover in bipartite graphs |
| Odd cycle | a cycle of length 3, 5, 7, … |
| 2-colourable | vertices can be coloured with 2 colours so no two adjacent share a colour |
| BFS | Breadth-First Search — used to test bipartiteness |
