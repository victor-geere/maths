---
title: Area & Co-area Formulas
tag: measure-theory
summary: The area formula generalises the change of variables theorem to Lipschitz maps, counting preimage points; the co-area formula gives the integral of a function as an integral over level sets weighted by the gradient magnitude.
links:
  - rectifiable-sets
  - hausdorff-measure
  - lebesgue-integral
  - currents
---

# Area & Co-area Formulas

The **area formula** and **co-area formula** are the fundamental integral identities of geometric measure theory, generalising the classical change-of-variables theorem to Lipschitz maps and non-smooth functions. The **area formula** for a Lipschitz map $f: \mathbb{R}^m \to \mathbb{R}^n$ ($m \leq n$) counts how many times $f$ covers each point $y$, weighted by the local volume distortion (Jacobian). The **co-area formula** for a Lipschitz function $u: \mathbb{R}^n \to \mathbb{R}^m$ ($m \leq n$) slices the domain by level sets $\{u = t\}$ and expresses the integral of $g|\nabla u|$ as an integral over the values $t$ of $g$ integrated over the level set $\{u = t\}$.

## Area Formula

Let $f: \mathbb{R}^m \to \mathbb{R}^n$ ($m \leq n$) be Lipschitz. For measurable $A \subseteq \mathbb{R}^m$ and $g \geq 0$ measurable:
$$\int_A g(x)\,J_mf(x)\,d\mathcal{L}^m(x) = \int_{\mathbb{R}^n} \sum_{x \in f^{-1}(y)\cap A} g(x)\,d\mathcal{H}^m(y)$$

where $J_mf(x) = \sqrt{\det(Df(x)^T Df(x))}$ is the $m$-dimensional Jacobian.

**Special case** ($g = 1$): $\int_A J_mf\,d\mathcal{L}^m = \int_{\mathbb{R}^n} \#(f^{-1}(y)\cap A)\,d\mathcal{H}^m(y)$.

## Co-area Formula

Let $u: \mathbb{R}^n \to \mathbb{R}^m$ ($m \leq n$) be Lipschitz, $g \geq 0$ measurable:
$$\int_{\mathbb{R}^n} g(x)\,J_mu(x)\,d\mathcal{L}^n(x) = \int_{\mathbb{R}^m} \left(\int_{u^{-1}(t)} g\,d\mathcal{H}^{n-m}\right)d\mathcal{L}^m(t)$$

**Special case** ($m=1$, $g=1$): $\int_{\mathbb{R}^n}|\nabla u|\,d\mathcal{L}^n = \int_{-\infty}^\infty \mathcal{H}^{n-1}(\{u=t\})\,dt$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Lipschitz map $f$ | $|f(x)-f(y)| \leq L|x-y|$ |
| $m$-Jacobian $J_mf$ | $\sqrt{\det(Df^TDf)}$; volume distortion of $f$ |
| Area formula | $\int_A J_mf = \int \#(f^{-1}(y)\cap A)\,d\mathcal{H}^m$ |
| Co-area formula | $\int g|\nabla u| = \int_\mathbb{R}(\int_{\{u=t\}}g\,d\mathcal{H}^{n-1})\,dt$ |
| Level set $\{u = t\}$ | $u^{-1}(t) = \{x : u(x) = t\}$ |
| $\mathcal{H}^{n-1}(\{u=t\})$ | $(n-1)$-dimensional measure of level set |
| $|\nabla u|$ | gradient magnitude; co-area weight |
| Change of variables | area formula generalises this to non-injective Lipschitz maps |
| $\#(f^{-1}(y))$ | number of preimages of $y$ under $f$ |
