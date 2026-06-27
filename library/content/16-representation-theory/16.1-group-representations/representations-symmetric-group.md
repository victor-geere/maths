---
title: Representation Theory of Sₙ
tag: representation-theory
summary: The irreducible complex representations of the symmetric group Sₙ are indexed by partitions of n via Young tableaux, with dimensions given by the hook-length formula.
links:
  - linear-representations
  - characters
  - symmetric-groups
  - induced-representations
  - combinations
---

# Representation Theory of Sₙ

The symmetric group $S_n$ — the group of all permutations of $n$ elements — has a completely explicit and combinatorial representation theory. Its irreducible complex representations are indexed by **partitions** $\lambda \vdash n$ and constructed via the combinatorics of **Young tableaux**. This theory is one of the most beautiful and useful in all of mathematics: it underlies the Schur–Weyl duality that connects representations of $S_n$ and $GL_n$, it controls the representation theory of $GL_n(\mathbb{F}_q)$ via Green's theorem, and it has applications ranging from quantum information to algebraic combinatorics.

## Partitions & Young Diagrams

A **partition** of $n$ is a tuple $\lambda = (\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_k > 0)$ with $\sum \lambda_i = n$, written $\lambda \vdash n$. Its **Young diagram** is an arrangement of $n$ boxes in rows of lengths $\lambda_1, \lambda_2, \ldots$.

For example, $\lambda = (3,2,1) \vdash 6$ gives:
$$\young(\hfil\hfil\hfil,\hfil\hfil,\hfil)$$

## Young Tableaux & Specht Modules

A **standard Young tableau** of shape $\lambda$ is a filling of the diagram with $1, \ldots, n$ increasing along rows and columns. The **Specht module** $S^\lambda$ is the irreducible representation of $S_n$ corresponding to $\lambda$. Every irreducible complex representation of $S_n$ is isomorphic to some $S^\lambda$.

## Hook-Length Formula

The dimension of $S^\lambda$ is given by the **hook-length formula**:
$$\dim S^\lambda = \frac{n!}{\prod_{u \in \lambda} h(u)}$$
where $h(u)$ is the **hook length** at box $u$: the number of boxes directly to the right or below $u$, plus 1.

## Character Formula

The character of $S^\lambda$ on a permutation of cycle type $\mu$ is the **Kostka number** / value given by the Murnaghan–Nakayama rule, computable via a combinatorial algorithm involving rim hook tableaux.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $S_n$ | symmetric group on $n$ elements |
| Partition $\lambda \vdash n$ | $(\lambda_1 \geq \cdots \geq \lambda_k > 0)$ with $\sum \lambda_i = n$ |
| Young diagram | pictorial representation of a partition as rows of boxes |
| Standard Young tableau | filling of Young diagram with $1,\ldots,n$ increasing in rows and columns |
| Specht module $S^\lambda$ | irreducible $S_n$-representation indexed by partition $\lambda$ |
| Hook length $h(u)$ | boxes right of $u$ + boxes below $u$ + 1 |
| Hook-length formula | $\dim S^\lambda = n! / \prod_{u} h(u)$ |
| Cycle type $\mu$ | partition recording lengths of cycles in a permutation |
| Murnaghan–Nakayama rule | algorithm for computing characters of $S_n$ |
| Schur–Weyl duality | link between $S_n$-reps and $GL_n$-reps on $V^{\otimes n}$ |
