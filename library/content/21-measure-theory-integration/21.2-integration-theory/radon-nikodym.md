---
title: Radon–Nikodym Theorem
tag: measure-theory
summary: The Radon–Nikodym theorem states that if ν is absolutely continuous with respect to μ, there exists a measurable function f (the Radon–Nikodym derivative dν/dμ) such that ν(A) = ∫_A f dμ for all measurable A.
links:
  - measure-spaces
  - lebesgue-integral
  - signed-measures
  - lp-spaces
---

# Radon–Nikodym Theorem

The **Radon–Nikodym theorem** is the measure-theoretic generalisation of the fundamental theorem of calculus. It asserts that if a measure $\nu$ is **absolutely continuous** with respect to a $\sigma$-finite measure $\mu$ (written $\nu \ll \mu$: every $\mu$-null set is $\nu$-null), then there exists a non-negative measurable function $f$ — the **Radon–Nikodym derivative** $\frac{d\nu}{d\mu}$ — such that $\nu(A) = \int_A f\,d\mu$ for all measurable $A$. This density $f$ plays the role of a "probability density function" in probability (where $\mu$ is Lebesgue measure and $\nu$ is the distribution of a continuous random variable), and it is the foundation of conditional expectation and the change-of-measure techniques (Girsanov's theorem) in stochastic calculus.

## Absolute Continuity

$\nu \ll \mu$ (**$\nu$ is absolutely continuous w.r.t. $\mu$**) if:
$$\mu(A) = 0 \implies \nu(A) = 0$$

## Radon–Nikodym Theorem

**Theorem**: Let $(X,\mathcal{F})$ be a measurable space with $\sigma$-finite measures $\mu$ and $\nu$. If $\nu \ll \mu$, there exists a unique (up to $\mu$-a.e.) non-negative measurable $f: X \to [0,\infty)$ with:
$$\nu(A) = \int_A f\,d\mu \quad \forall A \in \mathcal{F}$$

$f = \frac{d\nu}{d\mu}$ is the **Radon–Nikodym derivative** (or **density** of $\nu$ w.r.t. $\mu$).

## Lebesgue Decomposition

Any measure $\nu$ decomposes uniquely as $\nu = \nu_{ac} + \nu_s$ where $\nu_{ac} \ll \mu$ and $\nu_s \perp \mu$ (mutually singular: supported on disjoint sets).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\nu \ll \mu$ | absolute continuity: $\mu(A)=0 \Rightarrow \nu(A)=0$ |
| $\frac{d\nu}{d\mu}$ | Radon–Nikodym derivative / density |
| $\nu(A) = \int_A f\,d\mu$ | fundamental formula |
| $\sigma$-finite measure | $X = \bigcup X_n$, $\mu(X_n)<\infty$ |
| Lebesgue decomposition | $\nu = \nu_{ac} + \nu_s$, $\nu_{ac}\ll\mu$, $\nu_s\perp\mu$ |
| $\nu \perp \mu$ | mutually singular: disjoint supports |
| PDF | probability density function; $f = dP/d\lambda$ for prob $P$ |
| Chain rule | $\frac{d\nu}{d\lambda} = \frac{d\nu}{d\mu}\cdot\frac{d\mu}{d\lambda}$ when $\nu\ll\mu\ll\lambda$ |
