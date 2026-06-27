---
title: Network Flow
tag: algorithms
summary: Maximising the flow through a capacitated network from a source to a sink — solved by augmenting-path algorithms and unified with cuts by the max-flow min-cut theorem.
links:
  - graphs-basics
  - bipartite-graphs
  - connectivity
  - big-o-notation
---

# Network Flow

A **flow network** is a directed graph where each edge has a **capacity** — the maximum rate at which material can flow through it — and we seek to maximise the total flow from a **source** $s$ to a **sink** $t$. Network flow models traffic routing, pipeline throughput, airline scheduling, and matching in bipartite graphs. The central result — the **Max-Flow Min-Cut Theorem** — states that the maximum flow equals the minimum capacity of any cut separating $s$ from $t$. This duality is one of the most beautiful theorems in combinatorial optimisation, and the Ford–Fulkerson / Edmonds–Karp algorithms implement it constructively.

## Flow Network

A directed graph $G = (V, E)$ with:
- Capacity function $c : E \to \mathbb{R}_{\geq 0}$
- Source $s \in V$, sink $t \in V$

A **flow** $f : E \to \mathbb{R}_{\geq 0}$ must satisfy:

1. **Capacity constraint:** $0 \leq f(u,v) \leq c(u,v)$ for all edges
2. **Flow conservation:** for all $v \neq s, t$: $\sum_{u}f(u,v) = \sum_{w}f(v,w)$ (flow in = flow out)

The **value** of the flow: $|f| = \sum_v f(s,v)$.

## Max-Flow Min-Cut Theorem

$$\max_f |f| = \min_{\text{cut}(S,T)} \text{cap}(S, T)$$

where $\text{cap}(S,T) = \sum_{u \in S, v \in T, (u,v)\in E} c(u,v)$.

## Ford–Fulkerson Algorithm

1. Start with zero flow.
2. Find an **augmenting path** from $s$ to $t$ in the **residual graph**.
3. Send as much flow as possible along this path.
4. Repeat until no augmenting path exists.

## Residual Graph

$G_f$: for each edge $(u,v)$ with flow $f(u,v)$ and capacity $c(u,v)$:
- Forward residual capacity: $c(u,v) - f(u,v)$
- Backward residual capacity: $f(u,v)$ (can cancel existing flow)

## Edmonds–Karp

Use BFS to find shortest augmenting paths. **Complexity:** $O(VE^2)$.

## Applications via Reduction

- **Bipartite matching:** connect source to all $A$, all $B$ to sink, capacity 1; max flow = max matching
- **Connectivity:** min cut = edge connectivity
- **Circulation with demands:** generalise to supply/demand at nodes

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $c(u,v)$ | capacity of edge $(u,v)$ |
| $f(u,v)$ | flow on edge $(u,v)$ |
| $|f|$ | total flow value (flow out of source) |
| Source $s$ | where flow originates |
| Sink $t$ | where flow terminates |
| Augmenting path | an $s$–$t$ path in the residual graph with positive capacity |
| Residual graph $G_f$ | graph of remaining capacity after applying flow $f$ |
| Cut $(S, T)$ | bipartition of $V$ with $s \in S$, $t \in T$ |
| Cut capacity | $\sum_{u \in S, v \in T} c(u,v)$ |
| Max-flow min-cut | max flow = min cut capacity |
| Ford–Fulkerson | iterative augmenting-path algorithm |
| Edmonds–Karp | Ford–Fulkerson using BFS; $O(VE^2)$ |
