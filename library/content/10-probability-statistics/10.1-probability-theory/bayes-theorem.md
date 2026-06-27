---
title: Bayes' Theorem
tag: statistics
summary: Updating beliefs in the light of new evidence.
links:
  - conditional-probability
  - normal-distribution
---

## Key Formula

$$P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}$$

## Notes

Bayes' theorem rewrites the [[conditional-probability|conditional probability]] $P(A|B)$ in terms of the reverse conditioning $P(B|A)$ — the key operation for **inference**.

### Terminology

| Term | Symbol | Meaning |
|---|---|---|
| **Prior** | $P(A)$ | Belief about $A$ before seeing $B$ |
| **Likelihood** | $P(B\|A)$ | How probable $B$ is if $A$ is true |
| **Evidence** | $P(B)$ | Normalising constant |
| **Posterior** | $P(A\|B)$ | Updated belief after observing $B$ |

### Law of total probability

$$P(B) = \sum_{i} P(B \mid A_i)\,P(A_i)$$

where $\{A_i\}$ is a partition of the sample space.

### Bayesian inference

Bayes' theorem is iterated: the posterior from one observation becomes the prior for the next.

$$\underbrace{P(A \mid B)}_{\text{new prior}} \propto P(B \mid A)\,P(A)$$

The constant of proportionality is $1/P(B)$.

### Example — medical test

Suppose a disease affects 1% of the population. A test is 95% sensitive (true positive rate) and 95% specific (true negative rate).

$$P(\text{disease} \mid \text{positive}) = \frac{0.95 \times 0.01}{0.95 \times 0.01 + 0.05 \times 0.99} \approx 16\%$$

Despite a positive test, the posterior probability is only ~16% because the base rate is low — the classic **base-rate fallacy**.
