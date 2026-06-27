---
title: The Exponential Map
tag: representation-theory
summary: The exponential map sends a Lie algebra element X to a Lie group element exp(X), linearising the group near the identity and providing the bridge between infinitesimal and global symmetry.
links:
  - lie-groups
  - lie-algebras
  - root-systems
---

# The Exponential Map

The **exponential map** $\exp: \mathfrak{g} \to G$ is the fundamental bridge between a Lie algebra $\mathfrak{g}$ and its Lie group $G$. For a matrix group, it is literally the matrix exponential $e^X = \sum_{n=0}^\infty X^n/n!$. In general, $\exp(tX)$ is the unique one-parameter subgroup of $G$ with tangent vector $X$ at the identity. The exponential map is a local diffeomorphism near $0 \in \mathfrak{g}$, so the Lie algebra completely determines the local (and, for simply connected groups, the global) structure of $G$. It turns integration of the Lie bracket into multiplication in the group via the Baker–Campbell–Hausdorff formula.

## Matrix Exponential

For $X \in M_n(k)$:
$$e^X = \sum_{n=0}^\infty \frac{X^n}{n!} = I + X + \frac{X^2}{2!} + \frac{X^3}{3!} + \cdots$$

This series converges absolutely for all $X$, giving $e^X \in GL_n(k)$.

## Properties

- $e^0 = I$
- $\frac{d}{dt}e^{tX}\big|_{t=0} = X$
- $e^{(s+t)X} = e^{sX}e^{tX}$ — one-parameter subgroup
- $\det(e^X) = e^{\mathrm{tr}(X)}$ — so $e^{\mathfrak{sl}_n} \subseteq SL_n$
- If $XY = YX$: $e^{X+Y} = e^X e^Y$
- In general: $e^X e^Y \neq e^{X+Y}$ (the BCH formula corrects this)

## Baker–Campbell–Hausdorff Formula

$$\log(e^X e^Y) = X + Y + \frac{1}{2}[X,Y] + \frac{1}{12}([X,[X,Y]] - [Y,[X,Y]]) + \cdots$$

This expresses the group multiplication purely in terms of the Lie bracket, showing that $\mathfrak{g}$ determines the local group law.

## Surjectivity

For compact connected Lie groups (e.g., $SU(n)$, $SO(n)$), the exponential map is **surjective**: every group element is $e^X$ for some $X \in \mathfrak{g}$. For non-compact groups this may fail.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\exp(X) = e^X$ | exponential map: $\sum_{n\geq 0} X^n/n!$ |
| One-parameter subgroup | smooth homomorphism $\mathbb{R} \to G$; $t \mapsto \exp(tX)$ |
| $\mathrm{tr}(X)$ | trace of matrix $X$ |
| $\det(e^X) = e^{\mathrm{tr}X}$ | key identity relating exp to determinant |
| Baker–Campbell–Hausdorff (BCH) | formula for $\log(e^Xe^Y)$ in terms of brackets |
| Local diffeomorphism | bijective smooth map with smooth inverse near a point |
| Simply connected | every loop in $G$ is contractible; $\pi_1(G) = 0$ |
| $\mathfrak{sl}_n$ | traceless matrices; its exponential lies in $SL_n$ |
| Surjectivity of $\exp$ | every element of compact connected $G$ is $e^X$ |
