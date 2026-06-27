---
title: Halting Problem & Undecidability
tag: logic
summary: The halting problem asks whether a given Turing machine halts on a given input; Turing proved it is undecidable — no algorithm can solve it — by a diagonal argument, establishing the existence of inherently unsolvable problems.
links:
  - turing-machines
  - church-turing
  - recursive-functions
  - reducibility-degrees
  - godels-incompleteness
---

# Halting Problem & Undecidability

The **halting problem** is the question: given a description $\langle M \rangle$ of a Turing machine and an input $w$, does $M$ halt on $w$? Turing (1936) proved this problem is **undecidable**: no Turing machine can correctly answer YES/NO for all inputs. The proof is a diagonal argument — a self-referential construction that shows any purported decider leads to a contradiction. This was the first example of a mathematically well-defined problem with no algorithmic solution, establishing that the boundary of computability is fundamental and not merely a technological limitation. The halting problem is the prototypical undecidable problem, and many others are proved undecidable by **reduction** to it.

## Proof of Undecidability

**Theorem**: The language $HALT = \{\langle M, w \rangle : M\text{ halts on }w\}$ is undecidable.

**Proof**: Suppose for contradiction that $H$ decides $HALT$. Build a new machine $D$:
- On input $\langle M \rangle$: run $H$ on $\langle M, \langle M \rangle \rangle$.
  - If $H$ accepts (i.e., $M$ halts on $\langle M \rangle$): loop forever.
  - If $H$ rejects: halt and accept.

Now consider $D$ on input $\langle D \rangle$:
- If $D$ halts on $\langle D \rangle$: then $H$ accepts, so $D$ loops — contradiction.
- If $D$ loops on $\langle D \rangle$: then $H$ rejects, so $D$ halts — contradiction.

So $H$ cannot exist. $\square$

## Rice's Theorem

Any non-trivial semantic property of Turing machines is undecidable. (A property is **trivial** if it holds for all or no machines.)

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| $HALT$ | $\{\langle M,w\rangle : M$ halts on $w\}$ |
| Decidable | recognised by a TM that always halts with YES or NO |
| Undecidable | not decidable |
| Diagonal argument | self-referential proof that no decider $H$ can exist |
| $\langle M \rangle$ | encoding (Gödel number) of machine $M$ |
| Reduction $A \leq_m B$ | instance of $A$ maps to instance of $B$; $B$ decidable $\Rightarrow$ $A$ decidable |
| Rice's theorem | non-trivial semantic TM properties are undecidable |
| Recognisable (RE) | accepted by some TM (may loop on non-instances) |
| Co-RE | complement is RE; $HALT$ is RE but not co-RE |
