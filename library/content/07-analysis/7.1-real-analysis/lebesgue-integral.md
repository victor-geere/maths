---
title: Lebesgue Integral
tag: analysis
summary: An integral defined by partitioning the range of a function rather than its domain, enabling integration of far more functions with superior convergence theorems.
links:
  - lebesgue-measure
  - riemann-integral
  - lp-spaces
---

# Lebesgue Integral

The **Lebesgue integral**, introduced by Henri Lebesgue in 1902, revolutionised integration theory by changing the fundamental approach: instead of partitioning the **domain** (as Riemann does), it partitions the **range**. Intuitively, Lebesgue integration asks "how much of the domain maps into each horizontal strip?" rather than "what is the height of each vertical strip?" This seemingly small shift produces an integral that is defined for a vastly larger class of functions — including all bounded measurable functions, highly oscillatory functions, and limits of sequences — and that obeys three powerful convergence theorems absent from the Riemann theory.

## Construction

For a non-negative measurable function $f : \mathbb{R} \to [0, \infty)$:

**Step 1 — Simple functions:** a **simple function** $\phi = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ (finite combination of indicator functions on measurable sets). Define:

$$\int \phi\,d\lambda = \sum_{i=1}^n a_i\,\lambda(A_i)$$

**Step 2 — Non-negative functions:** approximate $f$ from below by simple functions:

$$\int f\,d\lambda = \sup\left\{\int \phi\,d\lambda : 0 \leq \phi \leq f,\; \phi \text{ simple}\right\}$$

**Step 3 — General functions:** write $f = f^+ - f^-$ where $f^+ = \max(f,0)$, $f^- = \max(-f,0)$, and define $\int f = \int f^+ - \int f^-$ when at least one is finite.

## Lebesgue vs. Riemann

| Property | Riemann | Lebesgue |
|---|---|---|
| Partitions | domain | range |
| Integrable functions | bounded + "few" discontinuities | all measurable bounded functions |
| Convergence theorems | limited | MCT, DCT, Fatou |
| Relation | if $f$ is Riemann integrable, both agree | Lebesgue is strictly more general |

## Three Key Convergence Theorems

**Monotone Convergence Theorem (MCT):** if $0 \leq f_n \nearrow f$ a.e., then $\int f_n \to \int f$.

**Dominated Convergence Theorem (DCT):** if $f_n \to f$ a.e. and $|f_n| \leq g$ with $\int g < \infty$, then $\int f_n \to \int f$.

**Fatou's Lemma:** $\int \liminf_n f_n \leq \liminf_n \int f_n$ (for non-negative $f_n$).

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $\int f\,d\lambda$ | Lebesgue integral of $f$ with respect to Lebesgue measure $\lambda$ |
| Simple function $\phi$ | a finite linear combination of indicator functions of measurable sets |
| $\mathbf{1}_A$ | indicator function: $\mathbf{1}_A(x) = 1$ if $x \in A$, else $0$ |
| $f^+, f^-$ | positive and negative parts of $f$: $f = f^+ - f^-$, both $\geq 0$ |
| Almost everywhere (a.e.) | holds except on a null set |
| MCT | Monotone Convergence Theorem |
| DCT | Dominated Convergence Theorem |
| Fatou's Lemma | $\int \liminf f_n \leq \liminf \int f_n$ |
| $f_n \nearrow f$ | $f_n$ is non-decreasing and converges pointwise to $f$ |
| Dominating function $g$ | $|f_n| \leq g$ for all $n$; controls growth for DCT |
| Measurable function | a function compatible with the measurable set structure |
