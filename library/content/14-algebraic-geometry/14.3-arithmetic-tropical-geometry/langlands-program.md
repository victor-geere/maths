---
title: Langlands Program (Overview)
tag: algebraic-geometry
summary: A vast web of conjectures linking automorphic forms, Galois representations, and L-functions — one of the deepest unifying programs in all of mathematics.
links:
  - etale-cohomology
  - arithmetic-geometry
  - galois-theory
  - elliptic-curves
---

# Langlands Program (Overview)

The **Langlands program** is a vast collection of conjectures and theorems, proposed by Robert Langlands in a letter to André Weil in 1967, that predict deep connections between three seemingly disparate areas: **automorphic forms** (complex-analytic objects on arithmetic quotients), **Galois representations** (group-theoretic objects encoding arithmetic symmetries), and **$L$-functions** (complex functions generalising the Riemann zeta function). The central principle is a **functoriality conjecture**: representations of the absolute Galois group $\text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$ should correspond to automorphic representations of reductive groups. The Langlands program has driven some of the deepest mathematics of the 20th and 21st centuries: the proof of Fermat's Last Theorem by Wiles is a consequence of the Langlands correspondence for $GL_2$, and the geometric Langlands program has deep connections to string theory and mathematical physics.

## The Three Pillars

### 1. Galois Representations

A **Galois representation** is a continuous group homomorphism:

$$\rho : \text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}) \to GL_n(\mathbb{Q}_\ell)$$

These arise naturally from étale cohomology of varieties: $H^i_\text{ét}(X_{\bar{\mathbb{Q}}}, \mathbb{Q}_\ell)$ is a Galois representation.

### 2. Automorphic Forms

An **automorphic form** is a function on $G(\mathbb{A}_\mathbb{Q}) / G(\mathbb{Q})$ (where $\mathbb{A}_\mathbb{Q}$ are the adèles and $G$ is a reductive group) that is smooth, $K$-finite for a maximal compact subgroup $K$, and an eigenfunction of the Hecke operators.

**Classical modular forms** are automorphic forms for $G = GL_2$.

### 3. $L$-Functions

For a Galois representation $\rho$ or automorphic form $\pi$, the **$L$-function** is:

$$L(s, \rho) = \prod_p L_p(s, \rho)$$

a product over primes encoding arithmetic data.

## The Langlands Correspondence

The **Langlands correspondence** predicts a natural bijection:

$$\left\{\begin{array}{c}\text{irreducible } n\text{-dim Galois}\\ \text{representations}\end{array}\right\} \longleftrightarrow \left\{\begin{array}{c}\text{cuspidal automorphic}\\\text{representations of }GL_n\end{array}\right\}$$

matching $L$-functions on both sides.

## Major Achievements

| Result | Significance |
|---|---|
| Langlands–Tunnell theorem | $n=2$, solvable Galois groups |
| Taylor–Wiles method | Modularity for semistable elliptic curves |
| Wiles's proof of FLT | Via modularity of $E_{a,b,c}$ |
| Lafforgue (2002 Fields Medal) | Full Langlands over function fields |
| Geometric Langlands | Reformulation over curves; connects to D-modules |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$ | absolute Galois group of $\mathbb{Q}$ |
| Galois representation | continuous $\rho : \text{Gal}(\bar{\mathbb{Q}}/\mathbb{Q}) \to GL_n(\mathbb{Q}_\ell)$ |
| Automorphic form | generalised modular form on a reductive group |
| $\mathbb{A}_\mathbb{Q}$ | adèle ring: restricted product of $\mathbb{R}$ and all $\mathbb{Q}_p$ |
| $L$-function $L(s,\rho)$ | Euler product encoding arithmetic of $\rho$ |
| Functoriality | the principle that Langlands correspondence respects natural maps between groups |
| Modularity theorem | every elliptic curve over $\mathbb{Q}$ is modular (Wiles, Taylor) |
| Cuspidal automorphic representation | the analytic analogue of an irreducible Galois representation |
| Hecke operators | commuting operators on automorphic forms; eigenvalues are the arithmetic data |
| Geometric Langlands | the function-field analogue; connects to $D$-modules and mirror symmetry |
