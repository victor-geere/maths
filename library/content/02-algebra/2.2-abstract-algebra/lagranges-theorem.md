---
title: Lagrange's Theorem
tag: abstract-algebra
summary: The order of a subgroup divides the order of the finite group.
links:
  - subgroups-cosets
  - group-axioms
  - cyclic-groups
---

## Statement

If $G$ is a **finite group** and $H \leq G$, then $|H|$ divides $|G|$. Moreover:

$$|G| = |H| \cdot [G : H]$$

where $[G : H]$ is the index (number of left cosets) of $H$ in $G$.

## Proof Sketch

The left cosets of $H$ partition $G$ into $[G:H]$ disjoint sets, each of size $|H|$. Counting elements gives $|G| = |H| \cdot [G:H]$.

## Corollaries

1. **Order of elements divides group order:** For any $g \in G$, $\text{ord}(g)$ divides $|G|$.
2. **Fermat's Little Theorem:** For $p$ prime and $\gcd(a,p)=1$, $a^{p-1} \equiv 1 \pmod{p}$ (from applying Lagrange to $(\mathbb{Z}/p\mathbb{Z})^*$).
3. **Groups of prime order are cyclic:** If $|G| = p$ (prime), then $G \cong \mathbb{Z}/p\mathbb{Z}$.

## Example

$G = S_3$, $|G| = 6$. Possible subgroup orders: 1, 2, 3, 6.

Indeed, $S_3$ has subgroups of orders 1, 2, 3, and 6 — and no subgroups of order 4 or 5.

## Notes

- The converse of Lagrange's theorem is **false** in general: a divisor of $|G|$ need not correspond to a subgroup. The smallest counterexample is $A_4$ ($|A_4|=12$, no subgroup of order 6).
- Lagrange's theorem is the foundation for much of finite group theory.
