---
title: Continuity in Topology
tag: topology
summary: A function between topological spaces is continuous if the preimage of every open set is open — a purely set-theoretic reformulation of the epsilon-delta definition.
links:
  - topological-spaces
  - open-closed-sets
  - bases-subbases
  - compactness
---

# Continuity in Topology

In calculus, continuity is defined using $\varepsilon$-$\delta$ distances. The topological definition strips away the metric and replaces it with a purely structural condition: a function $f : X \to Y$ is **continuous** if the **preimage** of every open set in $Y$ is open in $X$. This elegant reformulation is equivalent to the $\varepsilon$-$\delta$ definition in metric spaces, but works in any topological space — no distances needed. It captures the intuition that a continuous function doesn't "tear" the space: points that are close in $X$ map to points that are close in $Y$, where "closeness" is encoded by the open sets rather than by a number.

## Definition

A function $f : (X, \tau_X) \to (Y, \tau_Y)$ is **continuous** if:

$$\forall\, V \in \tau_Y,\quad f^{-1}(V) \in \tau_X$$

The preimage of every open set in $Y$ is open in $X$.

## Equivalent Conditions

For $f : X \to Y$, the following are equivalent:
- $f$ is continuous
- Preimage of every closed set is closed
- $f(\overline{A}) \subseteq \overline{f(A)}$ for all $A \subseteq X$
- For every $x \in X$ and every open $V \ni f(x)$, there exists open $U \ni x$ with $f(U) \subseteq V$
- (In metric spaces) $\varepsilon$-$\delta$ definition holds

## Continuity at a Point

$f$ is **continuous at $x$** if for every open $V$ containing $f(x)$, the preimage $f^{-1}(V)$ contains a neighbourhood of $x$.

## Homeomorphism

A **homeomorphism** is a bijective continuous function $f : X \to Y$ whose inverse $f^{-1}$ is also continuous. Homeomorphic spaces are topologically indistinguishable.

**Not every continuous bijection is a homeomorphism:** take $f : [0, 1) \to S^1$ (the unit circle) winding once around. $f$ is continuous but $f^{-1}$ is not.

## Properties Preserved by Continuous Maps

| Property | Preserved by continuous images? |
|---|---|
| Compactness | ✓ (compact $\to$ compact) |
| Connectedness | ✓ (connected $\to$ connected) |
| Second countability | ✓ |
| Hausdorff | ✗ (not always) |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $f : X \to Y$ | a function from space $X$ to space $Y$ |
| $f^{-1}(V)$ | preimage of $V$: the set $\{x \in X : f(x) \in V\}$ |
| Continuous function | $f^{-1}(V)$ is open in $X$ for every open $V$ in $Y$ |
| Homeomorphism | continuous bijection with continuous inverse |
| $\tau_X, \tau_Y$ | topologies on $X$ and $Y$ |
| Neighbourhood of $x$ | an open set containing $x$ |
| $\overline{A}$ | closure of $A$ |
| $f(\overline{A}) \subseteq \overline{f(A)}$ | closure is mapped into closure — a continuity condition |
| $S^1$ | the unit circle in $\mathbb{R}^2$ |
| $[0,1)$ | half-open interval |
| Topological property | one preserved under homeomorphism |
