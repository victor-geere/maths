# PSC2-F01 — the pairing lemma (E1) and the pairing-unification claim (HS5), both proved

*Finding note. Date: 2026-07-06. Work package: [PSC2-WP01](../workpackages/PSC2-WP01-pairing-lemma.md).
Code/run: `numerics/pairing_lemma_check.py` (numpy, seed 20260706; controls only — the proofs
are self-contained). Tags per [PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> None expected for (a) — it is linear algebra once $J V_n = V_n$ is arranged; the real content
> is *constructing* a $J$-invariant basis, which is WP02's N0 builder. If a $J$-invariant basis
> compatible with the sieve inventory cannot be exhibited, that is the reportable obstruction
> (and blocks E1 *by construction*, downgrading the pairing to asymptotic — record and stop).

## Regression check

N00 targets reproduced: **yes** — §4 classical spot-values rerun verbatim (`mpmath` dps 30):
$\gamma_1 = 14.1347251417$, $\gamma_2 = 21.0220396388$, $\gamma_{10} = 49.7738324777$,
$\sin(\pi\gamma_1) = 0.4107272152$, $\sin(\pi\gamma_1)/(\pi\gamma_1) = 0.009249457$ — all
matching [N00 §4](../numerics/PSC2-N00-verification-targets.md). No shared pipeline touched;
the control script is standalone and consumes no arithmetic data (the $\gamma$-values above
appear only in this regression line, not in any proof or control).

## Result

### Part (a) — Lemma E1 (the pairing lemma). — **proven**

**Setting.** $\mathcal H$ a complex Hilbert space; $D$ self-adjoint on
$\mathrm{dom}(D) \subset \mathcal H$; $J$ a **unitary** with $J\,\mathrm{dom}(D) = \mathrm{dom}(D)$
and
$$JDx = -DJx \qquad (x \in \mathrm{dom}(D)),$$
i.e. $JDJ^{-1} = -D$ ([S03 §1](../sources/PSC2-S03-eigenvalue-level.md): $J$ = adelic Fourier
transform composed with inversion, implementing $s \leftrightarrow 1-s$). Let
$V \subset \mathrm{dom}(D)$ be a finite-dimensional subspace with $JV = V$, let $P$ be the
orthogonal projection onto $V$, and let $H := P D P|_V$ (the sieve-Galerkin compression
$H^G_n$ with $V = V_n = \mathrm{ran}\,P_n$).

**Lemma E1.** $H$ is self-adjoint on $V$, $J_V := J|_V$ is a unitary on $V$ with
$J_V H J_V^{-1} = -H$, and consequently
$$\mathrm{spec}(H) = -\mathrm{spec}(H) \text{ as a multiset:}\quad
\dim\ker(H - \lambda) = \dim\ker(H + \lambda) \ \ \forall\lambda,$$
with eigenvectors paired unitarily: $Hu = \lambda u \Rightarrow H(J_V u) = -\lambda\,(J_V u)$.

*Proof.* **(0) Self-adjointness.** For $u, v \in V \subset \mathrm{dom}(D)$:
$\langle Hu, v\rangle = \langle PDu, v\rangle = \langle Du, v\rangle = \langle u, Dv\rangle
= \langle u, Hv\rangle$, using $Pv = v$ and symmetry of $D$ on its domain. So $H = H^*$ on $V$.

**(1) $J$ commutes with $P$.** Since $J$ is unitary and $JV = V$, also
$J^*V = J^{-1}V = V$; hence for $w \in V^\perp$ and any $v \in V$,
$\langle Jw, v\rangle = \langle w, J^*v\rangle = 0$, so $JV^\perp \subseteq V^\perp$.
Writing $x = Px + (I-P)x$: $JPx \in V$ and $J(I-P)x \in V^\perp$, so $PJx = JPx$, i.e.
$[J, P] = 0$.

**(2) The anticommutation descends to the compression.** $J_V$ is unitary on $V$ (as $JV = V$
and $J$ is unitary). For $u \in V \subset \mathrm{dom}(D)$, also $Ju \in V \subset \mathrm{dom}(D)$, and
$$H J_V u = P D J u = -P J D u = -J P D u = -J_V(PDu) = -J_V H u,$$
using the anticommutation on $\mathrm{dom}(D)$, then $[J,P] = 0$, and finally that
$PDu \in V$. Hence $J_V H J_V^{-1} = -H$ on $V$.

**(3) Pairing.** If $Hu = \lambda u$ with $u \neq 0$, then
$H(J_V u) = -J_V H u = -\lambda\,(J_V u)$ and $J_V u \neq 0$. Thus $J_V$ maps
$\ker(H - \lambda)$ into $\ker(H + \lambda)$ and $J_V^{-1}$ maps back, so the two eigenspaces
are unitarily isomorphic and the multiplicities agree. Since $H$ is a finite self-adjoint
matrix, its spectrum is the multiset of its (real) eigenvalues, and
$\mathrm{spec}(H) = -\mathrm{spec}(H)$ with multiplicity. $\blacksquare$

**Corollaries (stage-exact, free consistency checks for WP05).**

- **(C-a) Odd moments vanish.** $\mathrm{tr}(H^{2m+1}) = \mathrm{tr}(J_V H^{2m+1} J_V^{-1})
  = \mathrm{tr}((-H)^{2m+1}) = -\mathrm{tr}(H^{2m+1})$, so $\mathrm{tr}(H^{2m+1}) = 0$ for all
  $m \ge 0$, exactly, at every stage — an exact sum rule usable in E4a/HS2 as a zero-cost
  integrity check.
- **(C-b) Parity of the kernel.** Nonzero eigenvalues pair off, so
  $\dim V \equiv \dim\ker H \pmod 2$; in particular an odd-dimensional stage forces a zero
  mode. (Bookkeeping for HS1/HS2: the stage product and the moments
  $\sigma_n(2m) = \sum_k \lambda_k^{-2m}$ run over *nonzero* eigenvalues; the kernel
  multiplicity must be reported separately by the N0 builder.)
- **(C-c) Chiral block form — the F3 mechanism.** If moreover $J_V^2 = I$, then
  $V = V^+ \oplus V^-$ (the $\pm1$ eigenspaces of $J_V$, projections
  $P^\pm = \tfrac12(I \pm J_V)$), and
  $P^+ H P^+ = \tfrac14(H + J_VH + HJ_V + J_VHJ_V) = \tfrac14(J_VH + HJ_V) = 0 = P^-HP^-$:
  $H$ is purely off-diagonal in the grading,
  $H = \begin{pmatrix} 0 & B \\ B^* & 0 \end{pmatrix}$ — exactly the bipartite/chiral pairing
  mechanism of the divisor-graph stages (F3,
  [S02 §6](../sources/PSC2-S02-determinant-level.md)), and
  $\dim\ker H \ge |\dim V^+ - \dim V^-|$. (Stated conditionally on the involutivity of
  $J|_{V}$; the lemma itself does not need it.)

### Part (b) — Theorem HS5 (the pairing-unification claim). — **proven**

**Setting.** Let $\Lambda \subset \mathbb R \setminus \{0\}$ be a finite multiset (the nonzero
stage spectrum) and define the plain stage product over the whole multiset,
$\Pi_\Lambda(t) := \Xi(0)\prod_{\lambda \in \Lambda}\big(1 - t/\lambda\big)$, and the stage
determinant in $s$-coordinates
$$Z_n(s) := \Pi_\Lambda\big(t(s)\big), \qquad t(s) := -i\big(s - \tfrac12\big)
\ \ (\text{i.e. } s = \tfrac12 + it).$$

**Theorem HS5.** The following are equivalent:

1. $\Lambda = -\Lambda$ as a multiset ($\pm$-paired stage spectrum; positive part
   $0 < \lambda_1 \le \cdots \le \lambda_{d'}$);
2. $\Pi_\Lambda$ is even in $t$;
3. $Z_n(s) = Z_n(1 - s)$ for all $s \in \mathbb C$ (the stage functional equation).

When they hold, $\Pi_\Lambda(t) = \Xi_n(t) := \Xi(0)\prod_{k=1}^{d'}(1 - t^2/\lambda_k^2)$,
and $\Pi_\Lambda$ is **exponential-factor free**: with the genus-1 Weierstrass factor
$E_1(z) = (1-z)e^{z}$,
$$\prod_{\lambda \in \Lambda} E_1(t/\lambda) \;=\; \prod_{k=1}^{d'}\big(1 - t^2/\lambda_k^2\big)
\quad\text{exactly — pairing cancels every convergence factor.}$$

*Proof.* **(1 ⇒ 2)** Grouping each $\lambda_k$ with $-\lambda_k$:
$(1 - t/\lambda_k)(1 + t/\lambda_k) = 1 - t^2/\lambda_k^2$, so
$\Pi_\Lambda(t) = \Xi(0)\prod_k(1 - t^2/\lambda_k^2)$, a polynomial in $t^2$, hence even.

**(2 ⇒ 1)** $\Pi_\Lambda$ is a polynomial whose zero multiset is exactly
$\{\lambda : \lambda \in \Lambda\}$ (zero of $1 - t/\lambda$ at $t = \lambda$, with
multiplicities adding). If $\Pi_\Lambda(-t) = \Pi_\Lambda(t)$, the zero multiset is invariant
under $t \mapsto -t$, i.e. $\Lambda = -\Lambda$.

**(2 ⇔ 3)** The affine map $t(s) = -i(s - \tfrac12)$ satisfies
$t(1-s) = -i(\tfrac12 - s) = +i(s - \tfrac12) = -t(s)$. Hence
$Z_n(1-s) = \Pi_\Lambda(-t(s))$, and $Z_n \equiv Z_n(1 - \cdot)$ iff
$\Pi_\Lambda \equiv \Pi_\Lambda(-\cdot)$ (as $s \mapsto t(s)$ is a bijection of $\mathbb C$).

**(Exponential-factor cancellation)** For each pair,
$E_1(t/\lambda)E_1(-t/\lambda) = (1 - t/\lambda)e^{t/\lambda}(1 + t/\lambda)e^{-t/\lambda}
= 1 - t^2/\lambda^2$: the linear exponential factors cancel *pairwise and exactly*, at every
finite stage. $\blacksquare$

**Remark (infinite paired spectra — the normal form persists).** If $\Lambda = -\Lambda$ is an
infinite paired multiset with $\sum_k \lambda_k^{-2} < \infty$, then
$\prod_k(1 - t^2/\lambda_k^2)$ converges locally uniformly to an even entire function whose
Hadamard factorisation carries **no** factor $e^{a + bt}$ — the classical even Hadamard
product (Titchmarsh, *The Theory of the Riemann Zeta-Function*, §2.12), the same normal form
as the target $\Xi(t) = \Xi(0)\prod_k(1 - t^2/t_k^2)$
([S04 §1](../sources/PSC2-S04-model-pair.md)). So paired stage products live in the target's
normal form at every stage *and* in any $\sum\lambda^{-2}$-summable limit.

**Consequence (recorded, per the WP).** Gate **E1** (spectral pairing, level L4), design law
**C-2** (F6: AFE/functional-equation symmetry by construction, family design) and **H\*-d**
(exact stage FE symmetry $D_n(s) \leftrightarrow D_n(1-s)$, the Vitali identification set,
[S02 §3](../sources/PSC2-S02-determinant-level.md)) are **one constraint read at two levels**:
a stage family has $\pm$-paired spectra iff its stage determinants are even in $t$ iff they
satisfy the stage functional equation. In particular V2 membership (WP12) is correctly defined
*spectrally* — paired spectra, even products — and H\*-d is then automatic, not a separate
obligation. Propagated to [WP12](../workpackages/PSC2-WP12-afe-family.md).

### Numerical controls (harness hygiene, rule I0; not part of the proofs)

`numerics/pairing_lemma_check.py`, numpy, seed 20260706, verbatim:

```
ambient check   max|JDJ^-1 + D|            = 0.000e+00   (exact anticommutation)
E1  positive    J-invariant V, dim 8:  symmetry defect = 1.332e-15
E1  negative    generic V,     dim 8:  symmetry defect = 8.204e-01   (must be O(1))
E1  corollary   odd moments tr H^3, H^5, H^7 = 0.000e+00  0.000e+00  0.000e+00   (exact zeros)
HS5 positive    paired spectrum:   FE defect |Z(s)-Z(1-s)|/scale = 3.444e-17
HS5 negative    1% unpaired:       FE defect |Z(s)-Z(1-s)|/scale = 2.034e-02   (must sit far above machine precision)
HS5 exp-factor  paired:   prod E_1 / plain even product - 1 = 2.220e-16
HS5 exp-factor  unpaired: prod E_1 / plain product      - 1 = 5.724e-04   (residual exp factor, far above machine precision)
```

Every positive instance checks at machine precision and every negative control (generic
non-$J$-invariant subspace; a single 1%-broken pairing) fails by 12–15 orders of magnitude —
the harness can detect its own falsifier. No primes, no zeros, no arithmetic data consumed.

Symbolic cross-check (`sympy-verifier`, `verify_equation`): the two load-bearing identities of
part (b) — $E_1(t/\lambda)E_1(-t/\lambda) = 1 - t^2/\lambda^2$ and $t(1-s) = -t(s)$ for
$t(s) = -i(s - \tfrac12)$ — both return `equal: true`, `simplified_diff: 0`.

The numbers say: a $J$-invariant compression of an anticommuting pair has an exactly symmetric
spectrum with vanishing odd moments, a generic compression does not; a paired spectrum gives a
stage determinant satisfying the functional equation with all Weierstrass exponentials
cancelling, and breaking one pairing by 1% breaks both visibly.

## Verdict against the pre-registered criteria

**Pass**, in the branch the WP predicted: part (a) is linear algebra once $JV_n = V_n$ is
granted, and part (b) is elementary product bookkeeping plus one classical citation. **The
hypothesis $JV_n = V_n$ is assumed here, not constructed** — exhibiting a $J$-invariant basis
compatible with the sieve inventory is WP02's N0 builder, exactly as the falsifier stipulates;
if that construction fails, E1 is blocked *by construction* and the pairing downgrades to
asymptotic (reportable obstruction, routed to WP02).

**Scope (do-not list compliance).** Both results constrain the *shape* of stage objects
(spectral symmetry, evenness, FE normal form), not the *location* of eigenvalues relative to
the $\gamma$'s. That stage zeros sit on $\mathrm{Re}\,s = \tfrac12$ in $s$-coordinates is
carried by self-adjointness and the normalisation (S03 Lemma 1.1) — it is not evidence about
$\zeta$'s zeros, and this finding is not presented as approaching RH. RH remains **open**.

## Tag

**proven** — complete proofs above (part (a) self-contained; part (b) self-contained at finite
stages, classical citation for the infinite-stage remark). The numerical controls are
**verified** at machine precision with negative controls failing as required.

## Propagation

Charter ledger updated: **yes** (E1 + HS5 → proven; T1 marked done). Source doc correction
notice needed: **no** (S03 §6 / S04 §4 state E1/HS5 as targets; status lives in the charter
ledger per PSC2-001 §1). WP12 family definition updated to the spectral form (paired spectra,
even products): **yes**. WP02 unblocked (was: "immediately after WP01"): **yes**.
