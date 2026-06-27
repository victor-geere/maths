---
title: Monotone Convergence Theorem
tag: measure-theory
summary: The monotone convergence theorem states that if fₙ is a non-decreasing sequence of non-negative measurable functions converging pointwise to f, then the integral of f equals the limit of the integrals of fₙ.
links:
  - lebesgue-integral
  - dominated-convergence
  - fatous-lemma
  - measure-spaces
---

# Monotone Convergence Theorem

The **Monotone Convergence Theorem (MCT)** is one of the three fundamental convergence theorems of the Lebesgue integral, and arguably the most important. It states: if $\{f_n\}$ is a sequence of non-negative measurable functions with $f_n \leq f_{n+1}$ everywhere and $f_n \to f$ pointwise, then $\int f\,d\mu = \lim_{n\to\infty}\int f_n\,d\mu$. This justifies exchanging the limit and integral for monotone sequences — something that can fail for the Riemann integral. The MCT is used to prove that the Lebesgue integral of a general non-negative measurable function is well-defined (as a supremum of integrals of simple functions), and it implies Fatou's lemma and the Dominated Convergence Theorem.

## Statement

**Monotone Convergence Theorem**: Let $(X,\mathcal{F},\mu)$ be a measure space and $f_n: X \to [0,\infty]$ measurable with $f_1 \leq f_2 \leq \cdots$ and $f_n \to f$ pointwise. Then:
$$\int_X f\,d\mu = \lim_{n\to\infty}\int_X f_n\,d\mu$$

Note: the limit on the right may be $+\infty$.

## Proof Idea

- By monotonicity, $\int f_n\,d\mu$ is non-decreasing, so $L = \lim\int f_n$ exists in $[0,\infty]$.
- Since $f_n \leq f$, we have $L \leq \int f$.
- For the reverse: for any simple function $0 \leq s \leq f$ and $\alpha \in (0,1)$, the sets $E_n = \{f_n \geq \alpha s\}$ increase to $X$, giving $\int f_n \geq \alpha \int_{E_n} s$, and taking limits gives $L \geq \alpha \int s$. Since $\alpha < 1$ is arbitrary, $L \geq \int s$, and taking sup over simple $s \leq f$ gives $L \geq \int f$.

## Corollaries

- **Linearity of the integral**: $\int (f+g) = \int f + \int g$ for non-negative $f, g$.
- **Series**: $\int \sum_{n=1}^\infty f_n = \sum_{n=1}^\infty \int f_n$ for non-negative $f_n$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| MCT | Monotone Convergence Theorem |
| $f_n \nearrow f$ | $f_n$ increases to $f$ pointwise |
| $\int_X f\,d\mu$ | Lebesgue integral of $f$ |
| Simple function | finite linear combination of indicator functions |
| $\int s\,d\mu = \sum a_i \mu(A_i)$ | integral of simple function $s = \sum a_i \mathbf{1}_{A_i}$ |
| Pointwise limit | $f(x) = \lim_{n} f_n(x)$ for each $x$ |
| Exchange of limit and integral | justified for monotone sequences by MCT |
| Non-negative | $f_n \geq 0$; essential hypothesis |
