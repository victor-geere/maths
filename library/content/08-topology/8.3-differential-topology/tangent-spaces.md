---
title: Tangent Spaces
tag: differential-topology
summary: The linearisation of a smooth manifold at a point — a vector space that captures all the directions in which you can move.
links:
  - smooth-manifolds
  - differential-forms
  - jacobian
  - grad-div-curl
---

# Tangent Spaces

The **tangent space** $T_pM$ at a point $p$ on a smooth manifold $M$ is the vector space of all directions in which one can move away from $p$ within $M$. It is the best linear approximation to $M$ near $p$: a curved surface gets replaced locally by its tangent plane. Tangent spaces are the scaffolding on which all differential calculus on manifolds is built — vectors, derivatives of maps (the differential), vector fields, and differential forms all live in or are built from tangent spaces. Assembling all tangent spaces together gives the **tangent bundle** $TM$, which is itself a smooth manifold of dimension $2n$.

## Definition (via Curves)

A tangent vector at $p \in M$ is an equivalence class of smooth curves $\gamma : (-\varepsilon, \varepsilon) \to M$ with $\gamma(0) = p$, where $\gamma_1 \sim \gamma_2$ if they have the same velocity in every chart:

$$\frac{d}{dt}\!\left.(\varphi \circ \gamma_1)\right|_{t=0} = \frac{d}{dt}\!\left.(\varphi \circ \gamma_2)\right|_{t=0}$$

## Definition (via Derivations)

Equivalently, $T_pM$ consists of **derivations** at $p$: linear maps $v : C^\infty(M) \to \mathbb{R}$ satisfying the Leibniz rule:

$$v(fg) = v(f)\,g(p) + f(p)\,v(g)$$

## Basis in Coordinates

In a chart $\varphi = (x^1, \ldots, x^n)$, the tangent space has basis:

$$\left\{\frac{\partial}{\partial x^1}\bigg|_p, \ldots, \frac{\partial}{\partial x^n}\bigg|_p\right\}$$

Any tangent vector is $v = \sum_i v^i \frac{\partial}{\partial x^i}\big|_p$.

## The Differential (Pushforward)

For a smooth map $f : M \to N$, the **differential** at $p$:

$$df_p : T_pM \to T_{f(p)}N$$

is the linear map sending $[\gamma] \mapsto [f \circ \gamma]$. In coordinates, it is the Jacobian matrix $J_f$.

## Tangent Bundle

$$TM = \bigsqcup_{p \in M} T_pM$$

is the disjoint union of all tangent spaces. It is a smooth manifold of dimension $2n$. A **vector field** on $M$ is a smooth section of $TM$: a smooth assignment $p \mapsto X_p \in T_pM$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $T_pM$ | tangent space at $p$ — all tangent vectors at $p$ |
| Tangent vector | an equivalence class of curves through $p$, or a derivation |
| $\gamma : (-\varepsilon, \varepsilon) \to M$ | a smooth curve through $p = \gamma(0)$ |
| Derivation | a linear map $v : C^\infty(M) \to \mathbb{R}$ satisfying the Leibniz rule |
| $\partial/\partial x^i|_p$ | the $i$-th basis tangent vector in a chart |
| $df_p$ | differential (pushforward) of $f$ at $p$ |
| Jacobian matrix | the matrix of $df_p$ in coordinates |
| $TM$ | tangent bundle — collection of all tangent spaces |
| Vector field | smooth section of $TM$; assigns a tangent vector to every point |
| Section of $TM$ | a smooth map $s : M \to TM$ with $\pi \circ s = \text{id}_M$ |
| Leibniz rule | product rule for derivations: $v(fg) = v(f)g(p) + f(p)v(g)$ |
