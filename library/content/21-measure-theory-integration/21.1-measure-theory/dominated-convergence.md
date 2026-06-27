---
title: Dominated Convergence Theorem
tag: measure-theory
summary: The dominated convergence theorem allows interchange of limit and integral when a sequence of measurable functions converges almost everywhere and is uniformly bounded by an integrable dominating function.
links:
  - lebesgue-integral
  - monotone-convergence
  - fatous-lemma
  - measure-spaces
---

# Dominated Convergence Theorem

The **Dominated Convergence Theorem (DCT)** is the workhorse of Lebesgue integration: it gives a widely applicable condition under which $\lim_{n\to\infty}\int f_n = \int \lim_{n\to\infty} f_n$. The condition is that the sequence $\{f_n\}$ is **pointwise a.e. convergent** and **dominated** by an integrable function $g$: $|f_n(x)| \leq g(x)$ a.e. for all $n$, with $\int g < \infty$. The dominating function acts as an integrable "envelope" that prevents the mass of $f_n$ from escaping to infinity or to regions with negligible measure. The DCT vastly extends what the Riemann integral allows: for the Riemann integral, uniform convergence is required, while the DCT only needs pointwise a.e. convergence with a dominating function.

## Statement

**Dominated Convergence Theorem**: Let $f_n, g: X \to \mathbb{R}$ be measurable with:
1. $f_n(x) \to f(x)$ for $\mu$-a.e. $x$
2. $|f_n(x)| \leq g(x)$ a.e. for all $n$
3. $g \in L^1(\mu)$ (i.e., $\int g\,d\mu < \infty$)

Then $f \in L^1(\mu)$ and:
$$\lim_{n\to\infty}\int_X f_n\,d\mu = \int_X f\,d\mu$$

Equivalently: $\|f_n - f\|_{L^1} \to 0$.

## Proof

Apply Fatou's lemma to $g + f_n \geq 0$ and $g - f_n \geq 0$:
- $\int(g+f) \leq \liminf \int(g+f_n)$ gives $\int f \leq \liminf \int f_n$
- $\int(g-f) \leq \liminf \int(g-f_n)$ gives $-\int f \leq -\limsup \int f_n$

Together: $\limsup \int f_n \leq \int f \leq \liminf \int f_n$, so $\lim\int f_n = \int f$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| DCT | Dominated Convergence Theorem |
| Dominating function $g$ | $|f_n| \leq g$ a.e.; ensures uniform integrability |
| $L^1(\mu)$ | integrable functions: $\int|f|\,d\mu < \infty$ |
| A.e. convergence | $f_n(x) \to f(x)$ except on a null set |
| $\|f_n - f\|_{L^1} \to 0$ | convergence in mean |
| Fatou's lemma | $\int\liminf f_n \leq \liminf\int f_n$ for $f_n \geq 0$ |
| Uniform integrability | generalisation of domination; also implies DCT |
| Exchange of limit and integral | justified by DCT under domination |
