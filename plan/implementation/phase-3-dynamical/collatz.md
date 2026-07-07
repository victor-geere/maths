# Collatz Orbit Statistics — Phase 3b

*Status: **feasibility not yet assessed**. Write this memo before committing to a full spectral note.*

---

## Feasibility memo (to be written)

Answer the following questions before beginning:

### 1. Which sequence?

Options:
- **Stopping times** $T(n)$ = number of steps to reach 1.
- **Total stopping times** (steps to reach a value below $n$).
- **Orbit-length distribution** as $n \to \infty$.
- **Ergodic measure** on the $2$-adic integers (Terras, Lagarias).

Recommendation: start with stopping-time statistics and their generating function (if it exists).

### 2. Does geometric damping suffice?

The sequence must satisfy $\sum a_n r^n < \infty$ for some $r < 1$. Check:
- Growth rate of $T(n)$: conjectured $\sim C \log n$, so $e^{-\varepsilon T(n)}$ decays fast enough.
- Whether the sequence is *deterministic* or must be treated probabilistically.

### 3. Is a spectral note tractable?

A full note requires:
- A Hilbert space where $\{a_n\}$ lives as an operator spectrum.
- A closed-form or convergent kernel (no closed form is known for Collatz).
- Positive definiteness of the kernel (requires $a_n \ge 0$, which stopping times satisfy).

If no kernel closed form exists, the deliverable is a convergent series definition and a decay estimate — still useful as a catalogue entry.

### 4. Transfer operator connection

Collatz dynamics are naturally described by a Ruelle–Mayer transfer operator on $p$-adic or dyadic spaces (Lagarias 1985). Assess whether this operator's spectrum connects to the spectral-recipe framework.

## References to consult

- J. C. Lagarias, *The 3x+1 Problem and its Generalizations*, 1985.
- A. Kontorovich, J. C. Lagarias, *Stochastic models for the 3x+1 and 5x+1 problems*, 2010.
- R. Terras, *A stopping time problem on the positive integers*, 1976.
