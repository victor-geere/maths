---
title: Graphs, Vertices, Edges
tag: graph-theory
summary: The fundamental objects of graph theory — a vertex set and an edge set encoding pairwise relationships — and the basic vocabulary for describing them.
links:
  - paths-cycles-trees
  - connectivity
  - bipartite-graphs
  - planar-graphs
---

# Graphs, Vertices, Edges

A **graph** is one of the most versatile mathematical structures: a set of **vertices** (nodes) connected by **edges** (links) encoding pairwise relationships. Graphs model an enormous range of real-world systems — road networks, social networks, molecular bonds, web hyperlinks, dependency graphs — and the same abstract structure underlies all of them. Graph theory asks: what can we infer about the structure from local properties? How do we traverse a graph efficiently? What is the minimum number of colours needed to colour vertices so no two adjacent ones match? These questions have profound algorithmic and theoretical answers.

## Definition

A **graph** $G = (V, E)$ consists of:
- A finite set $V$ of **vertices** (or nodes)
- A set $E$ of **edges**, each an unordered pair $\{u, v\}$ with $u, v \in V$

A **directed graph** (digraph) uses ordered pairs $(u, v)$ for edges.

## Basic Vocabulary

| Term | Meaning |
|---|---|
| **Adjacent** | $u$ and $v$ are adjacent if $\{u,v\} \in E$ |
| **Degree** $\deg(v)$ | number of edges incident to $v$ |
| **Neighbour** $N(v)$ | set of vertices adjacent to $v$ |
| **Loop** | edge $\{v, v\}$ from a vertex to itself |
| **Multigraph** | allows multiple edges between the same pair |
| **Simple graph** | no loops, no multiple edges |

## Handshaking Lemma

$$\sum_{v \in V} \deg(v) = 2|E|$$

Every edge contributes 1 to each of its two endpoints' degrees, so the total is $2|E|$.

**Corollary:** the number of odd-degree vertices is always even.

## Special Graphs

| Name | Description |
|---|---|
| $K_n$ (complete) | every pair of vertices is connected; $|E| = \binom{n}{2}$ |
| $P_n$ (path) | $v_1 - v_2 - \cdots - v_n$ |
| $C_n$ (cycle) | $v_1 - v_2 - \cdots - v_n - v_1$ |
| $K_{m,n}$ (complete bipartite) | edges between two parts of sizes $m$ and $n$ |
| Empty graph | $E = \emptyset$ |

## Subgraphs and Induced Subgraphs

$H = (V', E')$ is a **subgraph** of $G$ if $V' \subseteq V$ and $E' \subseteq E$.

The **induced subgraph** on $S \subseteq V$: take $S$ with all edges of $G$ between pairs in $S$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $G = (V, E)$ | graph with vertex set $V$ and edge set $E$ |
| $V$ | vertex set |
| $E$ | edge set |
| $|V|$ | number of vertices (order of $G$) |
| $|E|$ | number of edges (size of $G$) |
| $\deg(v)$ | degree of vertex $v$: number of incident edges |
| Adjacent | connected by an edge |
| $K_n$ | complete graph on $n$ vertices |
| $K_{m,n}$ | complete bipartite graph |
| $C_n$ | cycle graph on $n$ vertices |
| Handshaking lemma | $\sum_v \deg(v) = 2|E|$ |
| Digraph | directed graph: edges are ordered pairs |
| Induced subgraph | subgraph on vertex subset $S$ retaining all edges within $S$ |
