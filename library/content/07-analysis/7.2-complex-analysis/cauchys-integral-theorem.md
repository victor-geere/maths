---
title: Cauchy's Integral Theorem
tag: complex-analysis
summary: The integral of a holomorphic function around any closed contour in a simply connected domain is zero.
links:
  - holomorphic-functions
  - cauchy-riemann
  - laurent-series
  - residue-theorem
---

# Cauchy's Integral Theorem

**Cauchy's Integral Theorem** is the cornerstone of complex analysis. It states that if $f$ is holomorphic on a simply connected domain $D$, then for any closed contour $\gamma$ lying inside $D$, the contour integral of $f$ around $\gamma$ is exactly zero. This vanishing is a direct consequence of the Cauchy–Riemann equations and Green's theorem applied in the complex plane. It implies that holomorphic functions have **path-independent** integrals — two paths between the same endpoints give the same value — and it leads directly to **Cauchy's integral formula**, which expresses the value of a holomorphic function at any interior point as a contour integral of its boundary values.

## Cauchy's Integral Theorem

Let $f$ be holomorphic on a simply connected open domain $D \subseteq \mathbb{C}$, and $\gamma$ a closed rectifiable curve in $D$. Then:

$$\oint_\gamma f(z)\,dz = 0$$

## Cauchy's Integral Formula

For $f$ holomorphic on $D$ and $z_0$ inside a simple closed positively oriented contour $\gamma \subset D$:

$$f(z_0) = \frac{1}{2\pi i}\oint_\gamma \frac{f(z)}{z - z_0}\,dz$$

**Generalisation — derivatives of all orders:**

$$f^{(n)}(z_0) = \frac{n!}{2\pi i}\oint_\gamma \frac{f(z)}{(z - z_0)^{n+1}}\,dz$$

This shows holomorphic functions are **infinitely differentiable**.

## Consequences

- **Morera's Theorem (converse):** if $\int_\gamma f = 0$ for every triangle in $D$, then $f$ is holomorphic.
- **Cauchy's Estimate:** $|f^{(n)}(z_0)| \leq \frac{n! M}{r^n}$ where $M = \max_{|z-z_0|=r}|f(z)|$.
- **Liouville's Theorem:** a bounded entire function is constant (from Cauchy's estimate as $r \to \infty$).
- **Fundamental Theorem of Algebra:** every non-constant complex polynomial has a root (via Liouville).

## Simply Connected Domain

A domain is **simply connected** if it has no "holes" — every closed curve can be continuously shrunk to a point. Cauchy's theorem fails for domains with holes: $\oint_{|z|=1} \frac{1}{z}\,dz = 2\pi i \neq 0$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\oint_\gamma f(z)\,dz$ | contour integral of $f$ along closed curve $\gamma$ |
| Holomorphic | complex-differentiable in a neighbourhood of every point |
| Simply connected | a domain with no holes; every closed loop contracts to a point |
| $z_0$ | a point inside the contour |
| $f^{(n)}(z_0)$ | $n$-th complex derivative of $f$ at $z_0$ |
| $n!$ | $n$ factorial |
| Contour | a piecewise smooth curve in $\mathbb{C}$ |
| Rectifiable curve | a curve of finite length |
| Morera's Theorem | converse of Cauchy: vanishing integrals imply holomorphicity |
| Liouville's Theorem | bounded entire $\Rightarrow$ constant |
| Cauchy's estimate | $|f^{(n)}(z_0)| \leq n!M/r^n$ |
| Fundamental Theorem of Algebra | every degree-$n$ polynomial has exactly $n$ roots in $\mathbb{C}$ |
