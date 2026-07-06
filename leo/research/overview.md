# Intensional and Extensional Equality of Recursive Functions: Formalization, SAT-Based Refutation, and k-Induction Proofs

**Grok (xAI)**  
**July 6, 2026**

## Abstract

We examine two intensionally distinct yet extensionally equivalent recursive definitions of the triangular number function: the direct accumulation \( f(n) = f(n-1) + n \) with \( f(0) = 0 \), and the auxiliary-square formulation \( r(n) = g(n) - r(n-1) \) with \( g(n) = g(n-1) + 2n - 1 \). Both compute \( \frac{n(n+1)}{2} \). 

We provide a rigorous formalization of this distinction between symbolic (intensional) and input–output (extensional) equality. We then reduce the problem of detecting whether a third, differently defined recursive function \( h \) is inequivalent to a family of Boolean satisfiability (SAT) instances via bounded unrolling and bit-blasting. Finally, we explore **k-induction** as a powerful automated technique to prove full equivalence when it holds, encoding both base cases and inductive steps as SMT queries.

Concrete examples, including a shifted triangular-number function that diverges at \( n=1 \), illustrate the methodology. The work unifies classical mathematical proof, modern satisfiability solving, and automated induction into a coherent framework for reasoning about recursive functions.

## 1. Introduction

Functions in mathematics and computer science can be presented in multiple ways. Two definitions may appear completely different—using distinct recursive structures, auxiliary variables, or computational strategies—yet produce identical results for every input. This phenomenon raises fundamental questions about the nature of equality: when are two functions “the same”?

We begin with a concrete pair of recursive definitions over the natural numbers (including zero). The first is the classic accumulation that directly builds triangular numbers. The second uses an auxiliary function that computes perfect squares and then applies a subtraction-based recurrence. Although their defining equations differ profoundly, both compute exactly the same values. A third function \( h \), defined by yet another recurrence, raises the practical question: how can we rigorously determine whether it is equivalent to the first two, and if not, what function it actually computes?

The paper makes three contributions that together provide a complete methodological toolkit:

1. A precise mathematical formalization of the original statement distinguishing intensional and extensional equality.
2. A reduction of the problem of detecting inequivalence with a third function \( h \) to Boolean Satisfiability (SAT) via bounded model checking.
3. An exploration of **k-induction** as an automated technique for proving full equivalence when it holds.

## 2. Background: The Functions and Their Equivalence

Let \( \mathbb{N}_0 = \{0, 1, 2, \dots\} \).

### Function \( f \)

\[
f(0) = 0, \quad f(n) = f(n-1) + n \quad (n \geq 1)
\]

### Functions \( g \) and \( r \)

\[
\begin{align*}
g(0) &= 0, \quad g(n) &= g(n-1) + 2n - 1 \quad (n \geq 1) \\
r(0) &= 0, \quad r(n) &= g(n) - r(n-1) \quad (n \geq 1)
\end{align*}
\]

Both functions compute the \( n \)-th triangular number:

\[
f(n) = r(n) = \frac{n(n+1)}{2}
\]

This can be shown by induction or by deriving the closed form.

## 3. Formalization of Intensional vs. Extensional Equality

Two total functions \( f, r : \mathbb{N}_0 \to \mathbb{N}_0 \) are **intensionally distinct** if their defining recursive equations differ syntactically. They are **extensionally equal** (\( f = r \)) if and only if

\[
\forall n \in \mathbb{N}_0.\quad f(n) = r(n)
\]

The original statement asserts that \( f \) and \( r \) are intensionally distinct yet extensionally equal.

For a third function \( h \) given by any other recursive specification, the central questions are:

- How can we determine whether \( \forall n.\ h(n) = f(n) \)?
- If not, what function does \( h \) actually compute?

## 4. Reduction to Boolean Satisfiability

The full universal statement cannot be decided by a single finite SAT instance. However, **refuting equivalence** (finding a concrete counterexample) reduces to SAT.

### Bounded Counterexample Search

For chosen bounds \( N \) and bit-width \( b \), construct CNF formula \( \phi(N, b) \):

- Bit-vector variables for \( f(m) \) and \( h(m) \) (\( m = 0 \dots N \)).
- Encode base cases and recursive steps as arithmetic circuits in CNF.
- Add difference assertion: at least one \( m \leq N \) where \( f(m) \neq h(m) \).

**Interpretation**:

- **SAT** → Counterexample exists (not equivalent).
- **UNSAT** → No difference up to \( N \) (increase \( N \)).

This is Bounded Model Checking applied to functional equivalence.

### Concrete Example

Consider \( h(0) = 0 \), \( h(n) = h(n-1) + (n + 1) \).

Using \( N=5 \), \( b=16 \), the SAT instance is satisfiable. Values:

| n | f(n) | h(n) | Differ? |
|---|------|------|---------|
| 0 | 0    | 0    | No      |
| 1 | 1    | 2    | **Yes** |
| 2 | 3    | 5    | Yes     |
| 3 | 6    | 9    | Yes     |
| 4 | 10   | 14   | Yes     |
| 5 | 15   | 20   | Yes     |

Counterexample at \( n=1 \). In fact, \( h(n) = \frac{(n+1)(n+2)}{2} - 1 \).

## 5. k-Induction for Equivalence Proofs

**k-Induction** generalizes classical induction:

- **Base**: Prove \( P(0) \land \dots \land P(k-1) \).
- **Step**: Prove \( \forall n \geq k-1.\ (P(n-k+1) \land \dots \land P(n)) \implies P(n+1) \).

If both hold, \( P(n) \) is true for all \( n \).

### Application

Let \( P(n) \equiv h(n) = f(n) \). Strengthen with invariants for auxiliaries (e.g., \( g(n) = n^2 \)).

Encode base and inductive step as bounded SMT queries (same unrolling technology as SAT refutation). If both UNSAT for their negations, full equivalence is proved.

For simple cases like \( f = r \), \( k=1 \) suffices and matches classical induction.

## 6. Comparison of Methods

- **Classical Induction**: Manual or in proof assistants. Excellent for obvious invariants.
- **Bounded SAT**: Fast refutation.
- **k-Induction**: Automated proofs using SMT. Bridges the two.

**Recommended Workflow**: SAT search for counterexamples → k-induction for proofs → classical methods for closed forms.

## 7. Discussion and Implications

**Edge Cases**:
- Bit-width overflow.
- Need for property strengthening.
- Complex control flow.
- Non-linear recurrences.

The approach supports program verification, compiler correctness, and equivalence checking. It demonstrates the power of combining mathematical insight with automated reasoning tools.

## Conclusion

We have provided a unified toolkit for reasoning about recursive function equivalence: formalization of intensional/extensional equality, SAT-based refutation of inequivalence, and k-induction for automated proofs. These methods are complementary and highly practical.

---

*This Markdown version was derived from the corresponding HTML research paper. All mathematical notation uses standard LaTeX delimiters compatible with Markdown renderers supporting KaTeX/MathJax.*