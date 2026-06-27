---
title: Connectedness
tag: topology
summary: A topological space is connected if it cannot be split into two disjoint non-empty open sets — it is "in one piece".
links:
  - topological-spaces
  - open-closed-sets
  - compactness
  - continuity-topology
---

# Connectedness

**Connectedness** captures the topological notion of being "in one piece." A space is **connected** if it cannot be partitioned into two non-empty open (or equivalently, closed) sets — any attempt to split it leaves the pieces touching. Intuitively, you can travel from any point to any other without leaving the space. **Path-connectedness**, a stronger condition, requires an actual continuous path between any two points. Connectedness is a topological invariant: it is preserved by continuous maps, so homeomorphic spaces are either both connected or both disconnected. The intermediate value theorem — a central theorem in calculus — is really a statement about continuous images of connected sets.

## Definition

A topological space $X$ is **connected** if it cannot be written as a union of two disjoint non-empty open sets:

$$X = U \cup V,\quad U \cap V = \emptyset,\quad U, V \in \tau \implies U = \emptyset \text{ or } V = \emptyset$$

Equivalently: the only **clopen** (simultaneously open and closed) subsets of $X$ are $\emptyset$ and $X$.

## Path-Connectedness

$X$ is **path-connected** if for every $x, y \in X$ there exists a continuous map $\gamma : [0,1] \to X$ with $\gamma(0) = x$ and $\gamma(1) = y$.

$$\text{path-connected} \implies \text{connected}$$

The converse fails: the **topologist's sine curve** $\{(x, \sin(1/x)) : x > 0\} \cup \{(0,y) : y \in [-1,1]\}$ is connected but not path-connected.

## Examples

| Space | Connected? | Path-connected? |
|---|---|---|
| $\mathbb{R}$ | yes | yes |
| $(0,1) \cup (2,3)$ | no | no |
| $S^n$ (sphere, $n \geq 1$) | yes | yes |
| $\mathbb{Q}$ (rationals) | no | no |
| Topologist's sine curve | yes | no |

## Key Theorems

**Continuous image:** if $f : X \to Y$ is continuous and $X$ is connected, then $f(X)$ is connected.

**Intermediate Value Theorem:** $[a,b]$ is connected, so a continuous $f : [a,b] \to \mathbb{R}$ takes every value between $f(a)$ and $f(b)$.

**Connected components:** every space partitions uniquely into maximal connected subsets.

## Local Connectedness

$X$ is **locally connected** at $x$ if every neighbourhood of $x$ contains a connected neighbourhood. Local connectedness does not imply connectedness, nor vice versa.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Connected | cannot be split into two disjoint non-empty open sets |
| Disconnected | can be so split |
| Clopen | simultaneously open and closed |
| Path-connected | any two points joined by a continuous path in the space |
| $\gamma : [0,1] \to X$ | a path from $\gamma(0)$ to $\gamma(1)$ |
| Topologist's sine curve | classic example: connected but not path-connected |
| Connected component | maximal connected subset |
| Intermediate Value Theorem | continuous function on $[a,b]$ takes all intermediate values |
| $S^n$ | the $n$-sphere: the set of unit vectors in $\mathbb{R}^{n+1}$ |
| Local connectedness | every neighbourhood of $x$ contains a connected neighbourhood |
