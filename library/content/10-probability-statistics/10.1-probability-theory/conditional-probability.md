---
title: Conditional Probability
tag: statistics
summary: P(A|B) = P(A∩B)/P(B) — restricting the sample space to B.
links:
  - bayes-theorem
---

## Key Formula

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0$$

## Notes

Conditioning on $B$ means we **restrict the sample space** to outcomes where $B$ occurred, then renormalise.

### Multiplication rule

$$P(A \cap B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A)$$

### Independence

Events $A$ and $B$ are **independent** iff:

$$P(A \mid B) = P(A) \iff P(A \cap B) = P(A)\,P(B)$$

Knowing $B$ occurred gives no information about $A$.

**Caution:** independent events are not the same as mutually exclusive events ($A \cap B = \emptyset$).

### Chain rule for probability

$$P(A_1 \cap \cdots \cap A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 \cap A_2)\cdots$$

### Conditional distributions

For continuous random variables, the conditional density of $X$ given $Y = y$:

$$f_{X|Y}(x \mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$$

This naturally leads to [[bayes-theorem|Bayes' theorem]] in continuous form.
