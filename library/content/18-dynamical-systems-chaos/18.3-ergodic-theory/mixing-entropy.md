---
title: Mixing & Entropy
tag: dynamical-systems
summary: Mixing is a statistical independence condition on a dynamical system stronger than ergodicity; Kolmogorov–Sinai entropy measures the exponential growth rate of distinguishable orbit segments and classifies systems up to measurable conjugacy.
links:
  - ergodicity
  - birkhoff-ergodic
  - measure-preserving
  - lyapunov-exponents
  - chaos
---

# Mixing & Entropy

**Mixing** and **entropy** are two fundamental invariants in ergodic theory that go beyond ergodicity. A measure-preserving transformation is **mixing** if $\mu(T^{-n}A \cap B) \to \mu(A)\mu(B)$ as $n \to \infty$ — the future and present become statistically independent. **Kolmogorov–Sinai (KS) entropy** $h_{KS}(T)$ measures the average exponential rate at which the system creates new information: how quickly distinct initial conditions become distinguishable. KS entropy is a complete isomorphism invariant for Bernoulli shifts (Ornstein's theorem, 1970): two Bernoulli shifts are measurably isomorphic iff they have the same entropy. For smooth systems, the **Pesin formula** relates KS entropy to Lyapunov exponents: $h_{KS} = \int \sum_{\lambda_i > 0} \lambda_i\,d\mu$ (a deep connection between the ergodic and smooth viewpoints).

## Mixing

$(X,\mu,T)$ is **mixing** if for all $A, B \in \mathcal{B}$:
$$\lim_{n \to \infty} \mu(T^{-n}A \cap B) = \mu(A)\mu(B)$$

**Weak mixing**: $\frac{1}{n}\sum_{k=0}^{n-1} |\mu(T^{-k}A \cap B) - \mu(A)\mu(B)| \to 0$.

Hierarchy: Bernoulli $\Rightarrow$ mixing $\Rightarrow$ weak mixing $\Rightarrow$ ergodic.

## Kolmogorov–Sinai Entropy

For a finite partition $\mathcal{P} = \{P_1,\ldots,P_k\}$ of $X$:
$$h(T, \mathcal{P}) = \lim_{n\to\infty} \frac{1}{n} H\left(\bigvee_{k=0}^{n-1} T^{-k}\mathcal{P}\right)$$
where $H(\mathcal{Q}) = -\sum_i \mu(Q_i)\log\mu(Q_i)$ is the Shannon entropy of partition $\mathcal{Q}$.

The **KS entropy**: $h_{KS}(T) = \sup_{\mathcal{P}} h(T, \mathcal{P})$.

## Pesin's Formula

For a smooth ergodic map preserving $\mu$:
$$h_{KS}(T) = \int \sum_{\lambda_i(x) > 0} \lambda_i(x)\,d\mu(x)$$

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Mixing | $\mu(T^{-n}A \cap B) \to \mu(A)\mu(B)$ |
| Weak mixing | Cesàro average of $|\mu(T^{-n}A\cap B) - \mu(A)\mu(B)|$ goes to 0 |
| KS entropy $h_{KS}(T)$ | supremum over partitions of $h(T,\mathcal{P})$ |
| Partition $\mathcal{P}$ | disjoint measurable sets covering $X$ |
| Shannon entropy $H(\mathcal{P})$ | $-\sum_i \mu(P_i)\log\mu(P_i)$ |
| $\bigvee T^{-k}\mathcal{P}$ | coarsest partition finer than all $T^{-k}\mathcal{P}$ (join) |
| Bernoulli shift entropy | $h = \sum_i p_i \log(1/p_i)$ for distribution $(p_i)$ |
| Ornstein's theorem | Bernoulli shifts isomorphic $\Leftrightarrow$ same KS entropy |
| Pesin's formula | $h_{KS} = \int\sum_{\lambda_i>0}\lambda_i\,d\mu$ |
| Isomorphism invariant | property preserved by measure-theoretic conjugacy |
