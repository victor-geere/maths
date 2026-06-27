---
title: Chain Complexes & Homology
tag: homological-algebra
summary: A chain complex is a sequence of modules with composable maps squaring to zero; its homology modules measure the deviation from exactness and are the fundamental invariants computed by derived functors and algebraic topology.
links:
  - modules
  - exact-sequences
  - derived-functors
  - ext-tor
  - singular-homology
---

# Chain Complexes & Homology

A **chain complex** is a sequence of modules $C_\bullet: \cdots \to C_{n+1} \xrightarrow{d_{n+1}} C_n \xrightarrow{d_n} C_{n-1} \to \cdots$ with the fundamental condition $d_n \circ d_{n+1} = 0$ for all $n$ (the boundary of a boundary is zero). The **homology** $H_n(C_\bullet) = \ker(d_n)/\mathrm{im}(d_{n+1})$ measures how close the complex is to being exact: $H_n = 0$ at all degrees iff the complex is exact. Chain complexes and their homology are the algebraic skeleton of algebraic topology (singular homology, de Rham cohomology) and of homological algebra (projective resolutions, derived functors). The category of chain complexes is itself an abelian category, enabling the full machinery of homological algebra to apply to complexes of complexes (spectral sequences).

## Definitions

A **chain complex** $(C_\bullet, d)$ over $R$ consists of:
- $R$-modules $C_n$ for $n \in \mathbb{Z}$
- differentials $d_n: C_n \to C_{n-1}$ with $d_n \circ d_{n+1} = 0$ (equivalently $\mathrm{im}(d_{n+1}) \subseteq \ker(d_n)$)

**Homology**: $H_n(C_\bullet) = \ker(d_n) / \mathrm{im}(d_{n+1})$.

**Cycles** $Z_n = \ker(d_n)$, **Boundaries** $B_n = \mathrm{im}(d_{n+1})$.

## Chain Maps & Homotopy

A **chain map** $f: C_\bullet \to D_\bullet$ is a family of maps $f_n: C_n \to D_n$ commuting with differentials: $d_n^D \circ f_n = f_{n-1} \circ d_n^C$.

A **chain homotopy** between $f, g: C_\bullet \to D_\bullet$ is a family $s_n: C_n \to D_{n+1}$ with $f_n - g_n = d_{n+1}^D s_n + s_{n-1} d_n^C$. Homotopic maps induce the same map on homology.

## Long Exact Sequence

A short exact sequence $0 \to A_\bullet \to B_\bullet \to C_\bullet \to 0$ of chain complexes yields a **long exact sequence in homology**:
$$\cdots \to H_n(A) \to H_n(B) \to H_n(C) \xrightarrow{\delta} H_{n-1}(A) \to \cdots$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Chain complex $(C_\bullet, d)$ | sequence with $d^2 = 0$ |
| Differential $d_n: C_n \to C_{n-1}$ | boundary map |
| $d^2 = 0$ | $d_n \circ d_{n+1} = 0$; fundamental condition |
| Cycles $Z_n = \ker(d_n)$ | closed chains |
| Boundaries $B_n = \mathrm{im}(d_{n+1})$ | exact chains |
| Homology $H_n = Z_n/B_n$ | measure of failure of exactness |
| Cochain complex | complex with $d: C^n \to C^{n+1}$ (arrows reversed); cohomology $H^n$ |
| Chain map $f: C_\bullet \to D_\bullet$ | commutes with differentials |
| Chain homotopy | equivalence relation on chain maps preserving homology |
| Connecting homomorphism $\delta$ | map $H_n(C) \to H_{n-1}(A)$ in long exact sequence |
