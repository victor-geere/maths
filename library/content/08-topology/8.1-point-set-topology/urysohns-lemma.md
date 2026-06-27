---
title: Urysohn's Lemma
tag: topology
summary: In a normal topological space, any two disjoint closed sets can be continuously separated by a real-valued function.
links:
  - separation-axioms
  - topological-spaces
  - continuity-topology
  - tychonoffs-theorem
---

# Urysohn's Lemma

**Urysohn's Lemma** is the fundamental tool for constructing continuous functions on topological spaces. It states that in a **normal** space ($T_4$), whenever two closed sets are disjoint, there always exists a continuous function $f : X \to [0,1]$ that equals $0$ on one closed set and $1$ on the other. This is a non-trivial achievement: on a general topological space, continuous functions can be scarce. The lemma shows that normality is precisely the condition that ensures enough continuous functions exist to separate closed sets. Pavel Urysohn proved it in 1925, and it serves as the key step in proving the Tietze Extension Theorem and the Urysohn Metrisation Theorem.

## Statement

Let $X$ be a **normal** ($T_4$) topological space, and let $A, B \subseteq X$ be disjoint closed sets. Then there exists a continuous function $f : X \to [0, 1]$ such that:

$$f(a) = 0 \;\;\forall\, a \in A \qquad \text{and} \qquad f(b) = 1 \;\;\forall\, b \in B$$

Such a function $f$ is called a **Urysohn function** for the pair $(A, B)$.

## Proof Idea

Use normality to inductively construct a nested family of open sets $U_r$ (indexed by dyadic rationals $r \in [0,1] \cap \mathbb{Q}$) with:

$$A \subseteq U_0, \quad B \subseteq X \setminus U_1, \quad r < s \implies \overline{U_r} \subseteq U_s$$

Define $f(x) = \inf\{r : x \in U_r\}$. One verifies $f$ is continuous and achieves $0$ on $A$, $1$ on $B$.

## Consequences

**Tietze Extension Theorem:** $X$ is normal iff every continuous $f : A \to \mathbb{R}$ on a closed $A \subseteq X$ extends to a continuous $F : X \to \mathbb{R}$.

**Urysohn Metrisation Theorem:** every second-countable normal ($T_4$) Hausdorff space is metrisable (homeomorphic to a metric space).

## Converse

Urysohn's Lemma has a converse: if for every pair of disjoint closed sets a Urysohn function exists, then $X$ is normal. So normality $\iff$ Urysohn functions exist.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Normal space | $T_4$ topological space: disjoint closed sets have disjoint open neighbourhoods |
| $f : X \to [0,1]$ | continuous function with values in the unit interval |
| Urysohn function | a continuous function that is $0$ on $A$ and $1$ on $B$ |
| Dyadic rationals | numbers of the form $p/2^n$ for integers $p, n$ |
| $\overline{U_r}$ | closure of the open set $U_r$ |
| $\inf$ | infimum — greatest lower bound |
| Tietze Extension | continuous functions on closed subsets extend to the whole space in normal spaces |
| Metrisable | admits a metric compatible with the topology |
| Second countable | has a countable basis |
| Hausdorff ($T_2$) | distinct points have disjoint neighbourhoods |
| Nested family | a family of sets indexed so that $r < s \implies U_r \subseteq U_s$ |
