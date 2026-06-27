---
title: Elliptic Curves
tag: algebraic-geometry
summary: Smooth projective cubic curves with a distinguished point — they carry a natural abelian group structure and are central to number theory and cryptography.
links:
  - plane-curves
  - riemann-roch
  - genus-classification
---

# Elliptic Curves

An **elliptic curve** is a smooth projective curve of genus 1 with a distinguished point $O$. Over a field $k$, it can always be written in **Weierstrass form** $y^2 = x^3 + ax + b$ (with $4a^3 + 27b^2 \neq 0$, ensuring smoothness). The remarkable fact that sets elliptic curves apart from all other algebraic curves is that their points form a **finitely generated abelian group** under a geometrically defined addition law. This group structure makes elliptic curves a crossroads of algebraic geometry, number theory, and cryptography: they are the key tool in Wiles's proof of Fermat's Last Theorem, the Birch and Swinnerton-Dyer conjecture, and elliptic curve cryptography (ECC).

## Weierstrass Form

A **short Weierstrass equation** (characteristic $\neq 2, 3$):

$$E: y^2 = x^3 + ax + b, \quad a,b \in k, \quad 4a^3 + 27b^2 \neq 0$$

The **discriminant** $\Delta = -16(4a^3 + 27b^2) \neq 0$ ensures no singular points.

## The Group Law

Given two points $P, Q$ on $E$, define $P + Q$ geometrically:

1. Draw the line through $P$ and $Q$ (or the tangent at $P$ if $P = Q$)
2. Find the third intersection point $R$ with $E$
3. Reflect $R$ across the $x$-axis to get $P + Q$

The **identity element** $O$ is the point at infinity $[0:1:0]$.

**Negation:** $-P = (x_P, -y_P)$.

## Addition Formulas

For $P = (x_1, y_1)$ and $Q = (x_2, y_2)$ with $P \neq -Q$:

$$\lambda = \begin{cases}\dfrac{y_2 - y_1}{x_2 - x_1} & P \neq Q \\ \dfrac{3x_1^2 + a}{2y_1} & P = Q\end{cases}$$

$$x_3 = \lambda^2 - x_1 - x_2, \quad y_3 = \lambda(x_1 - x_3) - y_1$$

## Mordell's Theorem

Over $\mathbb{Q}$: the group $E(\mathbb{Q})$ of rational points is **finitely generated**:

$$E(\mathbb{Q}) \cong \mathbb{Z}^r \oplus E(\mathbb{Q})_{\text{tors}}$$

where $r \geq 0$ is the **rank** and $E(\mathbb{Q})_{\text{tors}}$ is a finite group.

## Applications

- **Cryptography (ECC):** the discrete logarithm problem on $E(\mathbb{F}_p)$ is hard; used in TLS, Bitcoin
- **Fermat's Last Theorem:** Wiles proved FLT by showing certain elliptic curves are modular
- **Birch–Swinnerton-Dyer conjecture:** relates $r$ to the vanishing of the $L$-function $L(E,s)$ at $s=1$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $E : y^2 = x^3+ax+b$ | short Weierstrass form of an elliptic curve |
| $\Delta = -16(4a^3+27b^2)$ | discriminant; $\Delta \neq 0$ iff $E$ is smooth |
| $O = [0:1:0]$ | the distinguished point at infinity; identity of the group |
| $P + Q$ | addition of points by the chord-and-tangent law |
| $-P = (x_P, -y_P)$ | inverse of point $P$ |
| Rank $r$ | the number of independent infinite-order points in $E(\mathbb{Q})$ |
| $E(\mathbb{Q})_\text{tors}$ | the finite torsion subgroup |
| Mordell's theorem | $E(\mathbb{Q})$ is finitely generated |
| ECC | elliptic curve cryptography |
| $E(\mathbb{F}_p)$ | the group of points over the finite field $\mathbb{F}_p$ |
| $L(E,s)$ | the L-function of $E$; central to BSD conjecture |
