---
title: Gödel's Incompleteness Theorems
tag: logic
summary: Gödel's first incompleteness theorem shows no consistent, sufficiently strong formal system can prove all true arithmetic statements; the second shows it cannot prove its own consistency.
links:
  - peano-arithmetic
  - consistency-independence
  - completeness-theorem
  - turing-machines
---

# Gödel's Incompleteness Theorems

Gödel's **incompleteness theorems** (1931) are the most profound results in the foundations of mathematics. The **first theorem** states: any consistent formal system $F$ strong enough to express basic arithmetic contains a true sentence $G_F$ that $F$ cannot prove. The **second theorem** states: $F$ cannot prove its own consistency (Con($F$)) unless $F$ is actually inconsistent. These theorems shattered Hilbert's programme of finding a complete, consistent, finitely axiomatisable foundation for all mathematics. The proof uses **Gödel numbering** — encoding syntax as arithmetic — and the **diagonal lemma** to construct a sentence that essentially says "I am not provable in $F$".

## First Incompleteness Theorem

**Theorem**: Let $F$ be a consistent, recursively axiomatisable formal system that interprets Robinson arithmetic $Q$. Then there exists a sentence $G_F$ such that:
- $F \not\vdash G_F$ (not provable)
- $F \not\vdash \neg G_F$ (not refutable)

$G_F$ is true (in the standard model $\mathbb{N}$) but unprovable in $F$.

## Gödel Numbering & Diagonal Lemma

Assign a natural number $\ulcorner \varphi \urcorner$ (Gödel number) to every formula $\varphi$. Arithmetic can then talk about provability: $\mathrm{Prov}_F(n)$ means "the formula with Gödel number $n$ is provable in $F$".

**Diagonal Lemma**: For any formula $\psi(x)$, there is a sentence $\varphi$ with $F \vdash \varphi \leftrightarrow \psi(\ulcorner \varphi \urcorner)$.

Apply with $\psi(x) = \neg\mathrm{Prov}_F(x)$: get $G_F \leftrightarrow \neg\mathrm{Prov}_F(\ulcorner G_F \urcorner)$ — "$G_F$ is not provable".

## Second Incompleteness Theorem

$$F \not\vdash \mathrm{Con}(F)$$
where $\mathrm{Con}(F) = \neg \mathrm{Prov}_F(\ulcorner \bot \urcorner)$ — "F does not prove a contradiction". If $F \vdash \mathrm{Con}(F)$, then $F$ is inconsistent.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $F \vdash \varphi$ | $\varphi$ is provable in $F$ |
| $G_F$ | Gödel sentence: "$G_F$ is not provable in $F$" |
| Consistent | $F \not\vdash \bot$ |
| Recursively axiomatisable | axioms can be listed by a computer program |
| Gödel number $\ulcorner\varphi\urcorner$ | natural number encoding formula $\varphi$ |
| $\mathrm{Prov}_F(n)$ | arithmetic predicate: $n$ is Gödel number of an $F$-theorem |
| Diagonal lemma | self-referential fixed-point construction |
| $\mathrm{Con}(F)$ | "F is consistent": $\neg\mathrm{Prov}_F(\ulcorner\bot\urcorner)$ |
| Robinson arithmetic $Q$ | weak arithmetic; minimum for incompleteness |
| $\omega$-consistency | stronger than consistency; also implies $G_F$ unprovable |
