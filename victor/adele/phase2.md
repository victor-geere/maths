# Phase 2 — Embedding the sieve into the adèle class space

*Implements §3 of [prime-sieve-adele-plan.html](prime-sieve-adele-plan.html).*
*Status: **conceptual / heuristic** — a dictionary, not a theorem.*

Back: [phase1.md](phase1.md) · Index: [index.md](index.md) · Next: [phase3.md](phase3.md).

## 2.1 The space

Let $\mathbb A_\mathbb{Q}$ be the adèles of $\mathbb Q$ and $X = \mathbb A_\mathbb{Q}/\mathbb{Q}^\times$
the adèle class space. Passing to invertibles, the idèle class group
$C_\mathbb{Q} = \mathbb I_\mathbb{Q}/\mathbb{Q}^\times$ sits inside $X$, and the adèlic norm
$|\cdot|_\mathbb{A}:\mathbb I_\mathbb{Q}\to\mathbb R_{>0}$ descends to a proper map
$$
|\cdot| : C_\mathbb{Q}\longrightarrow \mathbb R_{>0}.
$$
The maximal compact $K=\widehat{\mathbb Z}^\times\times\{\pm1\}$ acts trivially on the norm, so a
$K$-invariant function on $X^\times$ is a function of the norm alone. The scaling action
$\alpha_t$ (multiply the archimedean component by $t>0$) has generator $D=-i\,\frac{d}{dt}\big|_{t=1}\pi(\alpha_t)$;
on $K$-invariant / spherical vectors this is the operator Connes' trace formula relates to the
zeros.

**Honest note on §1 of the plan.** The plan writes "the spectrum of $D$ is precisely
$\{\gamma:\zeta(\tfrac12+i\gamma)=0\}$ (Connes 1999)." This overstates Connes' result. Connes
obtains the zeros as an *absorption spectrum* inside a continuous spectrum, conditionally packaged
by the explicit formula — **not** as the honest self-adjoint spectrum of a constructed operator.
The plan itself concedes this two sentences later. Treat §1 as motivation, not as a proven
starting point. (This is the same asymmetry catalogued rigorously in
[prime-side.md](prime-side.md) §0 and Reading 4.3.)

## 2.2 The dictionary: integer $\to$ idèle representative

The sieve lives on integers; the geometry lives on idèles. The bridge:

> An integer $m = \prod_p p^{a_p}$ lifts to the idèle whose finite component at $p$ is
> $p^{a_p}$ and $1$ elsewhere, with archimedean component chosen so that the total norm is
> exactly $m$. Its class in $C_\mathbb{Q}$ is the image of the ideal $(m)$.

This is implemented (as an integer proxy) in [../adeles.py](../adeles.py),
`integer_to_idele_representative`. The dyadic slices $I_n=[2^n,2^{n+1})$ of $\mathbb Z$ become
dyadic slices of the norm on $C_\mathbb{Q}$; the composite generator of Phase 1 distinguishes,
inside each slice, the *prime* idèle classes (norm a prime) from the *composite* ones.

## 2.3 The finite-dimensional Hilbert space

Define $\mathcal H_n\subset L^2(X,\mu_{\mathrm{Tam}})$ spanned by
$\{\xi_p\}_{p\in I_n\cap\mathcal P}$, where $\xi_p$ is the normalised indicator of the fibre above
the prime idèle class of norm $p$. These are $K$-invariant and orthonormal. The scaling
generator restricted to $\mathcal H_n$ is where Phase 3 builds its matrix.

## 2.4 What is and isn't justified

| Claim | Assessment |
|---|---|
| Integers embed as idèle classes via $(m)$ | **standard** (Tate/Connes); fine |
| $K$-invariant functions = functions of the norm | **standard**; fine |
| Dyadic norm-slices $\leftrightarrow I_n$ | **fine** as a bookkeeping device |
| Scaling on a single prime fibre acts by $e^{it\log p}$ | **fine** — this is the origin of $\log p$ |
| "$\mathrm{Spec}(D)$ = zeros" (plan §1) | **overstated** — absorption spectrum only (§2.1) |
| Restricting to $\mathcal H_n$ approximates $D$ | **heuristic** — no convergence proved here |

## 2.5 Open tasks

- **T2.1** Make the intertwiner $L^2(\gamma)\to L^2(\mathbb T)$ / spherical-vector restriction
  precise as a bounded map (this is the same "functor" flagged open in the master
  [plan/project.md](../../plan/project.md), Phase 1c). Until it exists, "$H_n\to D$" in later
  phases is only formal.
- **T2.2** Decide the correct inner product on $\mathcal H_n$: the flat $\ell^2$ of the plan,
  or the $\Lambda$-weighted $\ell^2_\Lambda$ that [prime-side.md](prime-side.md) §2 proves is
  forced by the explicit formula. **Recommendation:** use $\ell^2_\Lambda$ — the flat choice is
  what makes Phase 3's normalisation fail.

Phase 2 introduces no falsifiable numerical claim; its job is to fix notation and to keep the
later phases honest about what "lives on the adèle space" actually means.
