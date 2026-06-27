---
title: Breadth-First & Depth-First Search
tag: algorithms
summary: Two fundamental graph traversal strategies — BFS explores level by level finding shortest paths, DFS dives deep first discovering structure like cycles and topological order.
links:
  - graphs-basics
  - paths-cycles-trees
  - connectivity
  - dijkstra
---

# Breadth-First & Depth-First Search

**Breadth-First Search (BFS)** and **Depth-First Search (DFS)** are the two fundamental algorithms for systematically visiting all vertices of a graph. BFS explores the graph **level by level** — first all neighbours of the start vertex, then their neighbours, and so on — naturally finding shortest paths in unweighted graphs. DFS dives **as deep as possible** along each branch before backtracking, revealing the graph's structure through discovery and finishing times: it detects cycles, computes topological orders, identifies connected components, and finds strongly connected components. Together they are the workhorses underlying almost every graph algorithm.

## Breadth-First Search (BFS)

**Algorithm:** uses a **queue** (FIFO).

1. Mark start vertex $s$ visited, enqueue $s$.
2. Dequeue vertex $u$; for each unvisited neighbour $v$: mark $v$ visited, set $\text{dist}[v] = \text{dist}[u]+1$, enqueue $v$.
3. Repeat until queue is empty.

**Output:** shortest-path distances $\text{dist}[v]$ from $s$ to all reachable $v$ (in unweighted graphs).

**Complexity:** $O(V + E)$.

## Depth-First Search (DFS)

**Algorithm:** uses a **stack** (or recursion).

1. Mark start vertex visited.
2. For each unvisited neighbour, recurse into it.
3. Record a **finish time** when backtracking.

**Complexity:** $O(V + E)$.

## Edge Classification (DFS on directed graphs)

| Edge type | Meaning |
|---|---|
| Tree edge | leads to an unvisited vertex |
| Back edge | leads to an ancestor — indicates a **cycle** |
| Forward edge | leads to a descendant (not tree edge) |
| Cross edge | leads to a non-ancestor/descendant |

## Applications

| Algorithm | Uses |
|---|---|
| BFS | shortest paths (unweighted), bipartiteness test, connected components |
| DFS | cycle detection, topological sort, SCCs (Kosaraju/Tarjan), articulation points |

## Topological Sort (DFS-based)

For a **DAG** (directed acyclic graph): output vertices in reverse finishing-time order. Every edge $(u,v)$ then has $u$ before $v$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| BFS | Breadth-First Search — explores layer by layer |
| DFS | Depth-First Search — explores deep before backtracking |
| Queue (FIFO) | First-In-First-Out structure used by BFS |
| Stack (LIFO) | Last-In-First-Out structure used by DFS |
| $\text{dist}[v]$ | shortest-path distance from source $s$ to $v$ |
| Back edge | DFS edge to an ancestor; signals a cycle |
| Finish time | the time step when DFS finishes processing a vertex |
| DAG | Directed Acyclic Graph |
| Topological sort | linear ordering of DAG vertices consistent with edge directions |
| SCC | Strongly Connected Component |
| $O(V + E)$ | linear time in the number of vertices and edges |
