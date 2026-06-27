---
title: String Diagrams
tag: category-theory
summary: A two-dimensional graphical calculus for morphisms in monoidal categories — where composition flows vertically and tensor product flows horizontally.
links:
  - monoidal-categories
  - natural-transformations
  - adjoint-functors
  - categorical-quantum-mechanics
---

# String Diagrams

**String diagrams** are a powerful graphical notation for morphisms in monoidal categories. Objects are represented as **wires** (strings) and morphisms as **boxes** (nodes); vertical stacking of boxes represents composition while horizontal juxtaposition represents the tensor product. This 2-dimensional calculus, developed by Penrose (1971) and formalised categorically by Joyal and Street, transforms abstract categorical identities into visually intuitive diagrammatic moves. String diagrams are used extensively in quantum computing (to represent quantum gates and circuits), linguistics (Lambek's pregroup grammar), logic (proof nets), and physics (Feynman diagrams and topological field theories), where they make complex compositions transparent.

## Basic Notation

- **Wire labelled $A$**: represents object $A$
- **Box labelled $f$ with input $A$ and output $B$**: represents morphism $f : A \to B$
- **Vertical stacking**: composition $g \circ f$
- **Horizontal juxtaposition**: tensor product $f \otimes g$

Reading direction: top to bottom (inputs at top, outputs at bottom) — though conventions vary.

## Key Rules

| Algebraic identity | Diagrammatic move |
|---|---|
| $g \circ f$ | boxes stacked vertically |
| $f \otimes g$ | boxes placed side by side |
| $\text{id}_A$ | a bare wire labelled $A$ |
| Associativity of $\otimes$ | wires can be moved past each other |
| Naturality of $\sigma$ | boxes slide past crossings |

## Compact Closed Categories

In a **compact closed category** (pivotal/ribbon), each object $A$ has a **dual** $A^*$ with **cup** $\eta : I \to A^* \otimes A$ and **cap** $\varepsilon : A \otimes A^* \to I$ satisfying **snake equations**:

$$(\text{id}_A \otimes \varepsilon) \circ (\eta \otimes \text{id}_A) = \text{id}_A$$

Diagrammatically: a wire bent into a U-shape that can be straightened.

## Applications

| Field | Use of string diagrams |
|---|---|
| Quantum computing | quantum circuits and protocols |
| Linguistics | parsing natural language via categorical grammars |
| Proof theory | proof nets in linear logic |
| Physics | topological quantum field theory |
| Machine learning | tensor network notation |

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| Wire | a string in a diagram representing an object |
| Box / node | represents a morphism |
| Vertical composition | $g \circ f$: boxes stacked top to bottom |
| Horizontal juxtaposition | $f \otimes g$: boxes placed side by side |
| $\text{id}_A$ | a bare wire (no box) |
| Compact closed category | monoidal category where every object has a dual |
| Dual $A^*$ | the object dual to $A$ |
| Cup $\eta : I \to A^* \otimes A$ | unit of the duality |
| Cap $\varepsilon : A \otimes A^* \to I$ | counit of the duality |
| Snake equations | the conditions $(\text{id}\otimes\varepsilon)(\eta\otimes\text{id})=\text{id}$ and analogously |
| Pivotal category | a compact closed category where $A^{**} \cong A$ naturally |
