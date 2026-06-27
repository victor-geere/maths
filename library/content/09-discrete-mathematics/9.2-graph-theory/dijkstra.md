---
title: Shortest Paths (Dijkstra)
tag: algorithms
summary: Dijkstra's algorithm efficiently finds the minimum-weight path from a source vertex to all others in a graph with non-negative edge weights.
links:
  - graphs-basics
  - bfs-dfs
  - spanning-trees
  - big-o-notation
---

# Shortest Paths (Dijkstra)

**Dijkstra's algorithm**, published by Edsger Dijkstra in 1959, solves the **single-source shortest path** problem: given a weighted graph with non-negative edge weights and a source vertex $s$, find the minimum-weight path from $s$ to every other vertex. It works by greedily selecting the unvisited vertex with the smallest tentative distance, updating (relaxing) the distances of its neighbours, and repeating. The greedy approach is correct precisely because all weights are non-negative — a shorter path cannot appear later. Dijkstra's algorithm is the foundation of GPS routing, network packet forwarding (OSPF), and many optimisation problems.

## Algorithm

**Input:** weighted graph $G = (V, E, w)$ with $w(e) \geq 0$, source $s$.

1. Set $d[s] = 0$ and $d[v] = \infty$ for all $v \neq s$.
2. Insert all vertices into a **priority queue** (min-heap) keyed by $d$.
3. Repeat until queue is empty:
   a. Extract vertex $u$ with minimum $d[u]$.
   b. For each neighbour $v$ of $u$: if $d[u] + w(u,v) < d[v]$, set $d[v] \leftarrow d[u] + w(u,v)$ (**relax**) and update the heap.
4. Return $d$.

## Complexity

| Data structure | Complexity |
|---|---|
| Simple array | $O(V^2)$ |
| Binary min-heap | $O((V + E)\log V)$ |
| Fibonacci heap | $O(E + V\log V)$ |

## Correctness

At each step, when a vertex $u$ is extracted from the priority queue, $d[u]$ is already the true shortest-path distance. This follows because all weights are non-negative: any alternative path through later vertices would be at least as long.

## Negative Weights

Dijkstra's algorithm **fails** with negative-weight edges. Use **Bellman–Ford** ($O(VE)$) instead, which also detects negative cycles.

## Example

Graph: $s \xrightarrow{4} a \xrightarrow{1} b$, $s \xrightarrow{2} c \xrightarrow{3} b$.

After running from $s$: $d[c]=2$, $d[a]=4$, $d[b]=5$ (via $s \to c \to b$).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $d[v]$ | tentative (then final) shortest-path distance from $s$ to $v$ |
| $w(u,v)$ | weight of edge $(u,v)$ |
| Relax | update $d[v]$ if a shorter path is found via $u$ |
| Priority queue | data structure supporting extract-min and decrease-key |
| Min-heap | binary tree where each node $\leq$ its children |
| Fibonacci heap | amortised-efficient heap giving $O(1)$ decrease-key |
| $O(V^2)$ | quadratic time; good for dense graphs |
| $O(E \log V)$ | efficient for sparse graphs with a binary heap |
| Bellman–Ford | shortest-path algorithm handling negative edges in $O(VE)$ |
| Negative cycle | a cycle with total negative weight; makes shortest paths undefined |
| OSPF | Open Shortest Path First — a routing protocol using Dijkstra |
