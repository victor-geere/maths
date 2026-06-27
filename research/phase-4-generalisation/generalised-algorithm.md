# The Generalised Algorithm — Phase 4

*Status: **not started** (blocked on Phase 1 numerics and $L^2(\gamma)\to L^2(\mathbb{T})$ functor).*

*When ready, this becomes `project/generalised-algorithm.md` following the proof-note template.*

---

## Algorithm statement (skeleton)

**Input:**
- A sequence $(a_n)_{n \ge 0}$ with $a_n \ge 0$.
- A growth class: $a_n = O(n^\alpha)$, $O(\varphi^n)$, etc.
- A symmetry: even extension $a_{-n} = a_n$, or a twist (character, sign).
- A damping rule: geometric $w_n = r^n$, or Gaussian $w_n = e^{-\sigma^2 n^2}$.

**Output (table to fill):**

| Output | Unconditional? | Depends on |
|---|---|---|
| Self-adjoint operator $T_K$ on $L^2(\mathbb{T})$ | Yes, when damped sequence is $\ell^1$ | — |
| Spectrum $\{\lambda_n\} = \{a_n w_n\}$ | Yes | — |
| Positive definiteness | Yes if $a_n \ge 0$ (Bochner) | $a_n \ge 0$ |
| Transfer operator $M: T^{(1)}_r \to T^{(2)}_r$ | Case by case | Existence of closed-form multiplier |
| Explicit formula (trace identity) | Conditional | Analytic continuation of associated $L$-function |
| Positivity criterion | Often conditional | RH or GRH for zeta/L-functions |

## Deliverable outline

```
§0  Abstract inputs and outputs
§1  The recipe (damp → symmetrise → kernel) — condensed from spectral-triple.html §3
§2  Existence and self-adjointness: general theorem
§3  Positive definiteness: Bochner on 𝕋
§4  Transfer operators: definition, boundedness, trace class
§5  Explicit formulas: general trace identity
§6  Positivity criteria: when they are unconditional vs. conditional
§7  Catalogue: one paragraph per object, pointing to its full note
§8  Special case: the spectral-triple recipe recovered
§9  Open problems
```

## Worked cases to cite

| Object | Full note | Status at time of writing |
|---|---|---|
| Prime sine wave | `project/prime-sine-wave.md` | Complete (T1–T4) |
| Fibonacci kernel | `project/fibonacci-kernel.md` | Complete (F1–F4 + numerics) |
| OU process | `project/ou-process.md` | Complete (O1–O5 + numerics) |
| η↔ζ transfer | `project/eta-zeta-transfer.md` | Complete (E1–E4 + numerics) |
| Spectral triple | `project/spectral-triple.md` | Heuristic (Thm 6.1 conditional) |
