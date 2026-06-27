# General Dirichlet Series and $L$-functions — Phase 2c

*Status: **core complete**. Deliverable written at
[project/dirichlet-series.md](../../project/dirichlet-series.md); numerics in
`victor/dirichlet-lf-verify.py`. The Hilbert-space core (D1–D3) and the
Gauss-sum transfer operator (D5) are proven and verified; the functional
equation and explicit formula are stated with standard citations and their
kernel-dictionary entries proven. Remaining items are listed under Open actions.*

---

## Status

| Theorem | Statement | Status |
|---|---|---|
| D1 | Domain: $\Psi^{\chi}_s\in H \iff \Re s>\tfrac12$ | **Proved** |
| D2 | Energy: $\lVert\Psi^{\chi}_s\rVert^2=L(2\sigma,\chi_0)=\zeta(2\sigma)\prod_{p\mid q}(1-p^{-2\sigma})$ | **Proved** |
| D3 | Kernel: $\langle\Psi^{\chi_1}_s,\Psi^{\chi_2}_{s'}\rangle=L(s+\overline{s'},\chi_1\bar\chi_2)$ | **Proved** |
| D4 | Parity $\leftrightarrow$ cosine/sine kernel and $\Gamma((s+a)/2)$ factor | **Proved** (kernel side); FE cited |
| D5 | Gauss-sum transfer: $\Psi^{\chi}_s=\tau(\bar\chi)^{-1}\sum_a\bar\chi(a)R_{2\pi a/q}\Psi^{(0)}_s$ | **Proved** |
| Functional equation as kernel symmetry | root number $\leftrightarrow$ transfer normalisation; reflection not internal to $H$ | **Cited + dictionary proved** |
| Explicit formula | Weil form, $\Gamma$-correction $=\psi((s+a)/2)$, prime side $2\Re\chi(n)$ | **Cited** (IK Thm 5.12) |

## Scope (recap)

- General Dirichlet series $\sum a_n n^{-s}$, $a_n\ge0$: the $a_n=\chi_0(n)$ case
  is D2; general non-negative $a_n$ follow the same Parseval pattern with energy
  $\sum a_n^2 n^{-2\sigma}$.
- Dirichlet $L$-functions $L(s,\chi)$: the worked family of the deliverable.
- Higher $L$-functions (automorphic / Artin): out of scope here.

## Key questions — resolution

1. **Kernel / positive definiteness.** $K^{\chi}_r$ is PD iff $\chi=\chi_0$
   (Bochner); every non-principal $\chi$ breaks the positive cone, like $\eta$.
   See deliverable §2.
2. **Functional equation $\leftrightarrow$ kernel symmetry.** Made precise in §4:
   archimedean $\Gamma$-factor $=$ kernel parity (D4); root number $=$ transfer
   normalisation (D5). The full reflection $s\leftrightarrow1-s$ is analytic
   continuation, **not** internal to $H$ — recorded honestly, not overclaimed.
3. **Transfer operator.** D5: a Gauss-sum-weighted sum of $\phi(q)$ rotations;
   $\eta\leftrightarrow\zeta$ is the degenerate $q=2$ instance.
4. **Explicit formula.** §5: Weil form, $\Gamma$-correction is digamma of
   $(s+a)/2$, prime side twisted by $2\Re\chi(n)$.

## Open actions

- [ ] Numerically verify D5 (rotation sum) on a $\theta$-grid for a **complex**
  character — e.g. an order-$4$ character mod $5$ — and tabulate.
- [ ] Promote the §5 transfer correction at $\{k\log p:p\mid q\}$ to a
  measure-level equality, jointly with the Phase 2a $\eta$ task.
- [ ] Imprimitive $\chi$: reduce to the primitive inducing character; track the
  removed Euler factors.

## Prerequisites (status)

- Phases 1b, 1c numerics: still open, but **not** required for the proven core
  D1–D5 (which only use Riesz–Fischer + character theory).
- η↔ζ measure-level equality (Phase 2a): still open; shared with Open action 2.
