---
title: Fubini's & Tonelli's Theorems
tag: measure-theory
summary: Tonelli's theorem allows iterated integration of non-negative functions; Fubini's theorem extends this to integrable functions, allowing interchange of order of integration in a double integral.
links:
  - lebesgue-integral
  - measure-spaces
  - monotone-convergence
  - dominated-convergence
---

# Fubini's & Tonelli's Theorems

**Fubini's theorem** and **Tonelli's theorem** justify interchanging the order of integration in iterated integrals. For a product measure space $(X \times Y, \mathcal{F} \otimes \mathcal{G}, \mu \otimes \nu)$, these theorems say: under appropriate conditions, $\iint f\,d(\mu\otimes\nu) = \int\!\left(\int f(x,y)\,d\nu(y)\right)d\mu(x) = \int\!\left(\int f(x,y)\,d\mu(x)\right)d\nu(y)$. Tonelli handles non-negative functions (no integrability needed), while Fubini handles integrable functions (possibly signed). Together they are indispensable in multivariable analysis, probability (joint distributions), and PDE theory.

## Product Measure

For $\sigma$-finite $(X,\mathcal{F},\mu)$ and $(Y,\mathcal{G},\nu)$, the **product measure** $\mu \otimes \nu$ on $(X\times Y, \mathcal{F}\otimes\mathcal{G})$ is the unique measure with:
$$\mu\otimes\nu(A\times B) = \mu(A)\cdot\nu(B), \quad A\in\mathcal{F},\ B\in\mathcal{G}$$

## Tonelli's Theorem

If $f: X\times Y \to [0,\infty]$ is measurable, then:
$$\iint f\,d(\mu\otimes\nu) = \int_X\!\left(\int_Y f(x,y)\,d\nu(y)\right)d\mu(x) = \int_Y\!\left(\int_X f(x,y)\,d\mu(x)\right)d\nu(y)$$
(all three equal, possibly $+\infty$).

## Fubini's Theorem

If $f \in L^1(\mu\otimes\nu)$ (i.e., $\iint|f|\,d(\mu\otimes\nu) < \infty$), then:
- For $\mu$-a.e. $x$: $y \mapsto f(x,y)$ is $\nu$-integrable.
- $x \mapsto \int_Y f(x,y)\,d\nu(y)$ is $\mu$-integrable.
- $\iint f\,d(\mu\otimes\nu) = \int_X\int_Y f(x,y)\,d\nu\,d\mu = \int_Y\int_X f(x,y)\,d\mu\,d\nu$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\mu \otimes \nu$ | product measure: $(\mu\otimes\nu)(A\times B) = \mu(A)\nu(B)$ |
| $\mathcal{F}\otimes\mathcal{G}$ | product σ-algebra: $\sigma(\{A\times B\})$ |
| Tonelli's theorem | swap integrals for non-negative $f$; no integrability required |
| Fubini's theorem | swap integrals for $f \in L^1$ |
| $L^1(\mu\otimes\nu)$ | $\iint|f|\,d(\mu\otimes\nu) < \infty$ |
| Iterated integral | $\int_X(\int_Y f(x,y)d\nu)d\mu$ |
| $\sigma$-finite | $X = \bigcup_n X_n$ with $\mu(X_n) < \infty$; required for Fubini |
| Counterexample | without integrability, iterated integrals may differ |
