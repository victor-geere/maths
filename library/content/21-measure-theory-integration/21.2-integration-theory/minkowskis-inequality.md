---
title: Minkowski's Inequality
tag: measure-theory
summary: "Minkowski's inequality states that the Lᵖ-norm satisfies the triangle inequality: ‖f+g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ, making Lᵖ spaces into normed vector spaces (Banach spaces for 1 ≤ p ≤ ∞)."
links:
  - lp-spaces
  - lp-duality
  - lebesgue-integral
  - banach-spaces
---

# Minkowski's Inequality

**Minkowski's inequality** states that the $L^p$-norm satisfies the triangle inequality: $\|f + g\|_p \leq \|f\|_p + \|g\|_p$ for $1 \leq p \leq \infty$. This is the key inequality making $L^p(\mu)$ into a **normed vector space** (and, for $1 \leq p \leq \infty$, a **Banach space** — complete under this norm). For $p = 2$, Minkowski's inequality follows from the Cauchy–Schwarz inequality; for general $p \geq 1$, it is proved using **Hölder's inequality**. The case $p < 1$ fails (the "norm" is not a norm), and $L^p$ for $p < 1$ is only a quasi-Banach space.

## Statement

For $1 \leq p \leq \infty$ and measurable $f, g$:

**$1 \leq p < \infty$**:
$$\|f+g\|_p = \left(\int |f+g|^p\,d\mu\right)^{1/p} \leq \left(\int |f|^p\,d\mu\right)^{1/p} + \left(\int |g|^p\,d\mu\right)^{1/p} = \|f\|_p + \|g\|_p$$

**$p = \infty$**:
$$\|f+g\|_\infty = \mathrm{ess\,sup}|f+g| \leq \mathrm{ess\,sup}|f| + \mathrm{ess\,sup}|g| = \|f\|_\infty + \|g\|_\infty$$

## Proof (via Hölder)

For $p > 1$: write $|f+g|^p \leq (|f|+|g|)|f+g|^{p-1}$ and apply Hölder with exponents $p$ and $p' = p/(p-1)$.

## Hölder's Inequality

**Hölder's inequality** (prerequisite): for $\frac{1}{p} + \frac{1}{q} = 1$:
$$\|fg\|_1 = \int|fg|\,d\mu \leq \|f\|_p \|g\|_q$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\|f\|_p = (\int|f|^p)^{1/p}$ | $L^p$-norm |
| $\|f\|_\infty = \mathrm{ess\,sup}|f|$ | essential supremum norm |
| Minkowski's inequality | triangle inequality for $\|\cdot\|_p$ |
| Hölder's inequality | $\int|fg| \leq \|f\|_p\|g\|_q$, $1/p+1/q=1$ |
| Conjugate exponent $p'$ | $1/p + 1/p' = 1$; $p' = p/(p-1)$ |
| $L^p(\mu)$ | $\{f : \|f\|_p < \infty\}$; Banach space for $p \geq 1$ |
| $p = 2$: Cauchy–Schwarz | special case of Hölder |
| Triangle inequality | $\|f+g\| \leq \|f\| + \|g\|$ |
| Banach space | complete normed vector space |
