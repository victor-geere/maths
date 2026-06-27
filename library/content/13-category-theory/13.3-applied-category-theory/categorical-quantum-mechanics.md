---
title: Categorical Quantum Mechanics
tag: category-theory
summary: A framework using compact closed categories and string diagrams to reason about quantum processes — separating the mathematical structure from the Hilbert space representation.
links:
  - string-diagrams
  - monoidal-categories
  - hilbert-spaces
---

# Categorical Quantum Mechanics

**Categorical Quantum Mechanics (CQM)** reformulates quantum theory using the language of **compact closed categories** and **string diagrams**, pioneered by Samson Abramsky and Bob Coecke (2004). Rather than working with specific Hilbert spaces, density matrices, and unitary operators, CQM abstracts the structural features — systems compose via tensor products, processes compose sequentially, and every system has a dual enabling teleportation-like protocols. String diagrams then make quantum reasoning visual and compositional: quantum circuits become string diagrams, the no-cloning theorem follows from the structure of the category, and protocols like quantum teleportation are proved by diagram rewriting. This approach has led to new results in quantum information theory and enables automated reasoning about quantum protocols.

## The Category **FHilb**

The fundamental category for CQM is **FHilb**:

- **Objects:** finite-dimensional Hilbert spaces $\mathcal{H}$
- **Morphisms:** linear maps $\mathcal{H} \to \mathcal{K}$
- **Tensor product:** $\mathcal{H} \otimes \mathcal{K}$ (composite system)
- **Unit:** $\mathbb{C}$ (the complex numbers)

**FHilb** is a **compact closed category**: every $\mathcal{H}$ has dual $\mathcal{H}^* = \overline{\mathcal{H}}$ (complex conjugate).

## Key Correspondences

| Physics | Category Theory |
|---|---|
| Quantum system | Object $\mathcal{H}$ |
| Physical process | Morphism $f : \mathcal{H} \to \mathcal{K}$ |
| Composite system | Tensor product $\mathcal{H} \otimes \mathcal{K}$ |
| Sequential processes | Composition $g \circ f$ |
| Quantum state | Morphism $\mathbb{C} \to \mathcal{H}$ |
| Effect / measurement outcome | Morphism $\mathcal{H} \to \mathbb{C}$ |
| Teleportation | Yanking equations (snake diagrams) |

## Frobenius Algebras and Observables

A **quantum observable** corresponds to a **special commutative Frobenius algebra** in **FHilb**: a triple $(\mathcal{H}, \Delta, \epsilon)$ where $\Delta : \mathcal{H} \to \mathcal{H} \otimes \mathcal{H}$ is copying and $\epsilon : \mathcal{H} \to \mathbb{C}$ is deleting.

**No-cloning theorem:** quantum states cannot be perfectly copied — corresponds to the fact that quantum states ($\mathbb{C} \to \mathcal{H}$) are not Frobenius algebra homomorphisms in general.

## ZX-Calculus

The **ZX-calculus** (Coecke–Duncan) is a complete graphical language for qubit quantum computing: two types of spiders (Z and X, green and red) generate all qubit operations, and rewriting rules express quantum circuit identities.

---

## Glossary

| Term / Symbol | Meaning |
|---|---|
| CQM | Categorical Quantum Mechanics |
| **FHilb** | category of finite-dimensional Hilbert spaces and linear maps |
| $\mathcal{H}$ | a Hilbert space (quantum system) |
| $\mathcal{H} \otimes \mathcal{K}$ | tensor product: composite quantum system |
| $\mathcal{H}^*$ | dual Hilbert space (complex conjugate) |
| Compact closed category | every object has a dual with cup and cap morphisms |
| State | morphism $\psi : \mathbb{C} \to \mathcal{H}$; represents a quantum state vector |
| Effect | morphism $e : \mathcal{H} \to \mathbb{C}$; represents a measurement outcome |
| Frobenius algebra | algebraic structure capturing copying and deleting (classical data) |
| No-cloning theorem | quantum states cannot be perfectly copied |
| ZX-calculus | complete graphical calculus for qubit quantum computing |
| Spider | the generators (Z-spider, X-spider) in the ZX-calculus |
