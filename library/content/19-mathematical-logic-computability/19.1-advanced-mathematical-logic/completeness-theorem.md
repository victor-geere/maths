---
title: Completeness Theorem (Gödel)
tag: logic
summary: Gödel's completeness theorem states that a first-order sentence is provable from a theory T if and only if it is true in every model of T, establishing that syntactic provability and semantic truth coincide.
links:
  - structures-models
  - compactness-logic
  - godels-incompleteness
  - proof-strategies
---

# Completeness Theorem (Gödel)

Gödel's **completeness theorem** (1929) is the foundational result of model theory, establishing that first-order logic is **complete**: a sentence $\varphi$ follows semantically from a theory $T$ (is true in every model of $T$) if and only if there is a formal proof of $\varphi$ from $T$. In symbols: $T \models \varphi \iff T \vdash \varphi$. This is not to be confused with Gödel's *incompleteness* theorems (1931), which concern specific theories like Peano arithmetic. The completeness theorem says that first-order logic itself is powerful enough that every semantic consequence can be captured by a proof. Its proof constructs a model from the syntactic data of a consistent theory — the canonical **Henkin construction**.

## Statement

**Gödel's Completeness Theorem**: Let $T$ be a first-order theory and $\varphi$ a sentence. Then:
$$T \models \varphi \iff T \vdash \varphi$$

Equivalently: every consistent first-order theory has a model.

## Henkin Construction

Given a consistent theory $T$:
1. Extend $T$ to a **Henkin theory** $T^*$ by adding witness constants $c_\varphi$ for each existential formula $\exists x\,\varphi(x)$, with axiom $\varphi(c_\varphi)$.
2. Extend to a maximal consistent theory $T^{**}$ (by Zorn's lemma / compactness).
3. Build the **term model**: domain = equivalence classes of closed terms under $t \sim s$ iff $T^{**} \vdash t = s$.
4. Interpret symbols by the terms; verify $T^{**} \models$ every sentence of $T^{**}$.

## Corollary: Compactness

If every finite subset of $T$ has a model then $T$ has a model. (Proof: finite satisfiability implies consistency by completeness; consistency implies a model.)

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $T \models \varphi$ | $\varphi$ is true in every model of $T$ (semantic consequence) |
| $T \vdash \varphi$ | $\varphi$ is provable from $T$ (syntactic derivability) |
| Completeness | $\models$ and $\vdash$ coincide for first-order logic |
| Consistent theory | $T \not\vdash \bot$; has no proof of contradiction |
| Henkin construction | builds a model from a maximal consistent Henkin theory |
| Witness constant $c_\varphi$ | new constant with axiom $\varphi(c_\varphi)$ for $\exists x\,\varphi(x)$ |
| Maximal consistent theory | consistent; adding any new sentence makes it inconsistent |
| Term model | structure whose domain is equivalence classes of terms |
