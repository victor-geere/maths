---
title: Bounded Linear Operators
tag: functional-analysis
summary: Linear maps between normed spaces that do not blow up the norm beyond a fixed multiple — the correct notion of continuity in infinite dimensions.
links:
  - banach-spaces
  - hilbert-spaces
  - hahn-banach
  - spectral-theory
---

# Bounded Linear Operators

In finite-dimensional linear algebra, every linear map is automatically continuous. In **infinite dimensions**, this is no longer true: a linear operator may be unbounded, blowing up the norm of some input vectors without limit. A **bounded linear operator** is one that maps bounded sets to bounded sets — equivalently, one that satisfies $\|Tv\| \leq M\|v\|$ for some fixed constant $M$ independent of $v$. Boundedness is exactly the right notion of continuity for linear operators between normed spaces, and the collection of all bounded linear operators from $X$ to $Y$ forms itself a normed space (and a Banach space when $Y$ is complete). These operators are the morphisms of functional analysis.

## Definition

A linear map $T : X \to Y$ between normed spaces is **bounded** if there exists $M \geq 0$ such that:

$$\|Tv\|_Y \leq M\|v\|_X \quad \text{for all } v \in X$$

The **operator norm** is the smallest such constant:

$$\|T\| = \sup_{\|v\|_X = 1} \|Tv\|_Y = \sup_{v \neq 0}\frac{\|Tv\|_Y}{\|v\|_X}$$

## Boundedness = Continuity

For a linear operator, the following are equivalent:
- $T$ is bounded
- $T$ is continuous (at every point)
- $T$ is continuous at $0$

## Space of Bounded Operators

$\mathcal{B}(X, Y) = \{T : X \to Y \mid T \text{ linear, bounded}\}$ is a normed space under $\|\cdot\|$.

When $Y$ is a Banach space, $\mathcal{B}(X, Y)$ is also a Banach space.

$\mathcal{B}(X, X)$ is a Banach algebra under composition.

## Dual Space

The **dual space** $X^* = \mathcal{B}(X, \mathbb{R})$ (or $\mathcal{B}(X, \mathbb{C})$) consists of all bounded linear functionals on $X$.

**Riesz Representation Theorem:** for a Hilbert space $H$, every $\phi \in H^*$ is of the form $\phi(v) = \langle v, u\rangle$ for a unique $u \in H$.

## Key Theorems

| Theorem | Statement |
|---|---|
| Uniform Boundedness | pointwise-bounded family of operators is uniformly bounded |
| Open Mapping | bounded surjective $T : X \to Y$ (Banach) maps open sets to open sets |
| Closed Graph | $T$ with closed graph is bounded |

## Example: Differentiation Operator

$T = \frac{d}{dx}$ on $C^1([0,1])$ with sup-norm: take $f_n(x) = \frac{\sin(n\pi x)}{\sqrt{n}}$.

$\|f_n\|_\infty \to 0$ but $\|f_n'\|_\infty = n\pi/\sqrt{n} = \pi\sqrt{n} \to \infty$.

So $T$ is **unbounded** on this space — an important example.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $T : X \to Y$ | a linear operator from normed space $X$ to $Y$ |
| $\|T\|$ | operator norm — the "size" of $T$ |
| Bounded operator | $\|Tv\| \leq M\|v\|$ for some $M$ and all $v$ |
| $\mathcal{B}(X, Y)$ | space of all bounded linear operators from $X$ to $Y$ |
| Dual space $X^*$ | bounded linear functionals on $X$ |
| Banach algebra | a Banach space with a multiplication satisfying $\|ST\| \leq \|S\|\|T\|$ |
| Uniform Boundedness Principle | (Banach–Steinhaus) pointwise bounded $\Rightarrow$ uniformly bounded |
| Open Mapping theorem | surjective bounded $T$ between Banach spaces is open |
| Closed Graph theorem | closed graph $\Rightarrow$ bounded |
| Riesz Representation | in Hilbert space: $\phi(v) = \langle v, u\rangle$ for unique $u$ |
| Linear functional | a bounded linear map $X \to \mathbb{R}$ (or $\mathbb{C}$) |
