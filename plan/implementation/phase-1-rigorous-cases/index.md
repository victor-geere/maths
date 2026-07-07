# Phase 1 — Easy, Fully Rigorous Cases

**Goal:** one complete proof-note per object, following the template of `project/prime-sine-wave.md`: concrete $L^2$ space, orthonormal system, unconditional convergence/energy theorems, and §6 numerical verification matching to 10 digits.

---

## Status

| Object | Note | Proofs | Numerics |
|---|---|---|---|
| Prime sine wave $\sum_p p^{-s}\sin(p\pi x)$ | [prime-sine-wave.md](prime-sine-wave.md) → `project/prime-sine-wave.md` | **Done** (T1–T4) | **Done** (§6) |
| Fibonacci kernel $K_r(\theta)$ | [fibonacci-kernel.md](fibonacci-kernel.md) → `project/fibonacci-kernel.md` | **Done** (F1–F4) | **Open** (§6) |
| OU process / Mehler kernel | [ou-process.md](ou-process.md) → `project/ou-process.md` | **Done** (O1–O5) | **Open** (§7) |

## Open actions

- [ ] [Phase 1b] Add `fibonacci_kernel` to toolkit; fill §6 of `project/fibonacci-kernel.md`.
- [ ] [Phase 1b] State and prove Lucas transfer multiplier $L_n = F_{n-1}+F_{n+1}$ and its trace identity.
- [ ] [Phase 1c] Add `ou_mehler` to toolkit; fill §7 of `project/ou-process.md` (requires `mpmath`).
- [ ] [Phase 1c] Formalise $L^2(\gamma) \to L^2(\mathbb{T})$ as a bounded intertwining map (Phase 4 prerequisite).
