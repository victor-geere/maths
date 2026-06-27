# Quaternionic Hilbert Module — Phase 5

*Status: **not started**. This is the hardest open item in Phase 5 and the prerequisite for H4.*

Primary reference: F. Colombo, I. Sabadini, D. C. Struppa, *Noncommutative Functional Calculus* (Birkhäuser, 2011) — the S-spectrum and slice-regular function theory.

---

## What needs to be defined

### 1. The module

A right quaternionic Hilbert module $\mathcal{M}$ over $\mathbb{H}$ with:
- An inner product $\langle \cdot, \cdot \rangle_{\mathbb{H}} : \mathcal{M} \times \mathcal{M} \to \mathbb{H}$ satisfying right-$\mathbb{H}$-linearity in the second argument.
- Completeness.
- A distinguished left action of $\mathbb{H}$ (or: clarify if it is a two-sided module — this depends on whether $j$ acts on the left or right).

The helix axis is the quaternionic $j$-direction: the proposal is that the lift $t \mapsto e^{jt} = \cos t + j \sin t$ lives in the $(1,j)$-plane of $\mathbb{H}$.

### 2. The operator $D_t = -j\partial_t$

Formally, $D_t$ is the generator of left-multiplication by $e^{jt}$ along the helix. As a quaternionic analogue of the self-adjoint momentum $-i\partial_x$ on $L^2(\mathbb{R})$:
- Domain: $\mathcal{M}^1 = \{f \in \mathcal{M} : \partial_t f \in \mathcal{M}\}$.
- Symmetry: $\langle D_t f, g \rangle = \langle f, D_t g \rangle$ for $f, g \in \mathcal{M}^1$.

Non-commutativity of $\mathbb{H}$ means left-$j$ and right-$j$ actions differ; the choice of side must be fixed before symmetry can be checked.

### 3. The S-spectrum

For a quaternionic operator $T$, the S-spectrum (Colombo–Sabadini–Struppa, Ch. 4) replaces the classical spectrum: $q \in \sigma_S(T)$ iff $T^2 - 2\,\mathrm{Re}(q)T + |q|^2 I$ is not invertible. This is the right notion of spectrum for slice-regular functional calculus.

## Conjecture H4 (to prove or refute)

$D_t = -j\partial_t$ is self-adjoint on $\mathcal{M}$ in the S-spectrum sense, and for any indefinite circle kernel $K$ with transfer operator $T_K$ (not positive on $L^2(\mathbb{T})$), the lifted operator on $\mathcal{M}$ satisfies:

$$\langle D_t f, f \rangle_{\mathbb{H}} \ge 0 \quad \text{iff} \quad Z^2 - (P^2 + G^2) \ge 0.$$

## Immediate first steps

1. Read Colombo–Sabadini–Struppa Ch. 2 (slice-regular functions) and Ch. 4 (S-spectrum); extract the self-adjointness criterion.
2. Choose the concrete model for $\mathcal{M}$: candidate is $L^2(\mathcal{H}, \mathbb{H})$ with the standard $\mathbb{H}$-valued inner product $\langle f, g \rangle = \int_{\mathcal{H}} \bar f \cdot g \, d\mu$.
3. Verify that $j\partial_t$ is densely defined and symmetric on a core domain (smooth $\mathbb{H}$-valued functions on $\mathcal{H}$ with compact support).
4. Check whether deficiency indices are $(0,0)$ (essentially self-adjoint) or require a self-adjoint extension.
