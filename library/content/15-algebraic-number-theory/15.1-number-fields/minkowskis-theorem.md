---
title: Minkowski's Theorem
tag: algebraic-number-theory
summary: Every ideal class contains an ideal of norm at most the Minkowski bound M_K, implying the class number h_K is finite and giving an explicit search region.
links:
  - ideal-class-group
  - ring-of-integers
  - number-fields
---

# Minkowski's Theorem

**Minkowski's theorem** provides the key finiteness result in algebraic number theory: the **class number** $h_K$ of any number field $K$ is finite. The proof uses **geometry of numbers** — the study of lattice points in convex bodies — pioneered by Minkowski. The main result states that every ideal class contains a representative ideal $\mathfrak{a}$ with norm $N(\mathfrak{a}) \leq M_K$ (the **Minkowski bound**). Since there are only finitely many ideals of bounded norm in a Dedekind domain, this immediately implies $h_K < \infty$. Moreover, to compute the class group explicitly one only needs to check prime ideals with norm $\leq M_K$ — making the class group effectively computable.

## Minkowski's Bound

For a number field $K$ of degree $n = [K:\mathbb{Q}]$ with $r_1$ real and $r_2$ pairs of complex embeddings:

$$M_K = \frac{n!}{n^n}\left(\frac{4}{\pi}\right)^{r_2}\sqrt{|\text{disc}(K)|}$$

Every ideal class of $\mathcal{O}_K$ contains an integral ideal $\mathfrak{a}$ with:

$$N(\mathfrak{a}) \leq M_K$$

## Geometry of Numbers

**Minkowski's lattice point theorem:** if $S \subseteq \mathbb{R}^n$ is a convex, centrally symmetric set with $\text{vol}(S) > 2^n \cdot \text{covol}(\Lambda)$, then $S$ contains a non-zero lattice point of $\Lambda$.

This is applied to the **Minkowski embedding** $K \hookrightarrow \mathbb{R}^{r_1} \times \mathbb{C}^{r_2} \cong \mathbb{R}^n$: $\alpha \mapsto (\sigma_1(\alpha),\ldots,\sigma_{r_1}(\alpha), \tau_1(\alpha),\ldots,\tau_{r_2}(\alpha))$.

## Finiteness of Class Number

Proof sketch:
1. Every ideal class contains an ideal $\mathfrak{a}$ with $N(\mathfrak{a}) \leq M_K$
2. In $\mathcal{O}_K$, there are only finitely many ideals of norm $\leq M_K$
3. Therefore $|\text{Cl}(K)| \leq \#\{\text{ideals with }N \leq M_K\} < \infty$

## Example: $\mathbb{Q}(\sqrt{-5})$

$n = 2$, $r_1 = 0$, $r_2 = 1$, $|\text{disc}| = 20$.

$$M_K = \frac{2}{4} \cdot \frac{4}{\pi} \cdot \sqrt{20} = \frac{2}{\pi}\sqrt{20} \approx 2.85$$

Check only primes $p \leq 2$: $(2) = \mathfrak{p}_2^2$ in $\mathcal{O}_K$, and $\mathfrak{p}_2$ is not principal → $h_K = 2$.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $M_K$ | Minkowski bound: maximum norm of a representative ideal |
| $n = [K:\mathbb{Q}]$ | degree of the number field |
| $r_1$ | number of real embeddings |
| $r_2$ | number of pairs of complex embeddings |
| $|\text{disc}(K)|$ | absolute value of the discriminant |
| $N(\mathfrak{a})$ | norm of ideal $\mathfrak{a}$: $[\mathcal{O}_K : \mathfrak{a}]$ |
| Geometry of numbers | study of lattice points in convex bodies |
| Minkowski embedding | $K \hookrightarrow \mathbb{R}^{r_1} \times \mathbb{C}^{r_2}$ |
| $\text{covol}(\Lambda)$ | covolume of lattice $\Lambda$: volume of a fundamental domain |
| Centrally symmetric | $S = -S$: if $\mathbf{x} \in S$ then $-\mathbf{x} \in S$ |
