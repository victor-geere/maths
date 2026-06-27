---
title: Measure-Preserving Transformations
tag: dynamical-systems
summary: A measure-preserving transformation is one that leaves a probability measure invariant; these are the objects of ergodic theory, which studies the long-term statistical behaviour of dynamical systems.
links:
  - ergodicity
  - birkhoff-ergodic
  - mixing-entropy
  - lebesgue-measure
  - haar-measure
---

# Measure-Preserving Transformations

A **measure-preserving transformation** is a measurable map $T: (X, \mathcal{B}, \mu) \to (X, \mathcal{B}, \mu)$ on a probability space satisfying $\mu(T^{-1}A) = \mu(A)$ for all measurable sets $A$. These are the fundamental objects of **ergodic theory**, which studies the long-term statistical behaviour of dynamical systems. The condition $T_* \mu = \mu$ means that $\mu$ is an **invariant measure** for $T$: it represents an equilibrium distribution that is preserved by the dynamics. Examples include: irrational rotations of the circle (ergodic, not mixing), Bernoulli shifts (mixing, hence ergodic), and Hamiltonian flows preserving Liouville measure. Poincaré's recurrence theorem follows immediately: almost every point returns arbitrarily close to its starting position.

## Definition

A **measure-preserving system** (MPS) is a quadruple $(X, \mathcal{B}, \mu, T)$ where:
- $(X, \mathcal{B}, \mu)$ is a probability space ($\mu(X) = 1$)
- $T: X \to X$ is measurable
- $\mu(T^{-1}A) = \mu(A)$ for all $A \in \mathcal{B}$

## Examples

| System | Invariant measure |
|---|---|
| Rotation $T_{\alpha}: x \mapsto x + \alpha \pmod 1$ | Lebesgue measure on $[0,1)$ |
| Doubling map $x \mapsto 2x \pmod 1$ | Lebesgue measure |
| Bernoulli shift on $\{0,1\}^\mathbb{Z}$ | $\prod (1/2, 1/2)$ |
| Hamiltonian flow | Liouville measure $dp\,dq$ |

## Poincaré Recurrence Theorem

If $\mu(A) > 0$, then $\mu$-almost every point $x \in A$ returns to $A$ infinitely often: $T^n(x) \in A$ for infinitely many $n$.

## Invariant Functions

$f: X \to \mathbb{R}$ is **$T$-invariant** if $f \circ T = f$ a.e. Ergodicity is the condition that the only invariant functions are constants a.e.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $(X,\mathcal{B},\mu)$ | probability space: $\mu(X) = 1$ |
| Measure-preserving | $\mu(T^{-1}A) = \mu(A)$ for all $A \in \mathcal{B}$ |
| Invariant measure | $T_*\mu = \mu$; probability measure preserved by $T$ |
| $T^{-1}A = \{x : Tx \in A\}$ | preimage |
| Poincaré recurrence | a.e. point in $A$ returns to $A$ infinitely often |
| Bernoulli shift | shift on $\{0,1,\ldots,k-1\}^\mathbb{Z}$ with product measure |
| Rotation $T_\alpha$ | $x \mapsto x + \alpha \pmod 1$; irrational $\alpha$ gives ergodic system |
| Liouville measure | $\prod dp_i \, dq_i$; preserved by Hamiltonian flows |
| Invariant function | $f \circ T = f$ a.e. |
