# PSC2-F09 — the inclusion theorem (E2): the ambient fixed once (E2a), the inclusion criterion proven (E2b), and the wedge window measured against it — the falsifier branch, quantified

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP03](../workpackages/PSC2-WP03-inclusion-theorem.md). Code/run:
`numerics/wp03_inclusion.py` (deterministic, no seed; stage matrices are the W1 closed
forms of `wp02b_rewindow.py` at `mpmath` dps 35, assembled through the F08 pencil code
path of `wp04_certified_enclosures.py`; `numpy` complex128 eigensolves). Tags per
[PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> - **E2a (the ambient, fixed once).** State rigorously the space on which the target $D$
>   acts (Hilbert $L^2(X)$-with-regularisation vs Meyer nuclear ambient) and record, with
>   tags, what is proven about $\mathrm{spec}(D)$ there — the M4 correction (S06 §2.5)
>   done properly so no later step can equivocate.
> - **E2b (inclusion).** Prove $P_n \to I$ strongly on an explicit core of $D$
>   (Schwartz-type spherical vectors), hence $H^G_n \to D$ in the strong-resolvent sense,
>   hence **spectral inclusion**: every point of $\mathrm{spec}(D)$ is a limit of stage
>   eigenvalues — *no zero is missed*.
> - **Honest payoff statement (binding).** E2 can never certify an eigenvalue *is* near a
>   zero (K2 pollution); it certifies none are missing. Claims are limited accordingly.
> - **Deliverable.** Finding note with the E2a ambient record (every statement tagged) and
>   the E2b theorem, tag target **proven**.
> - **Falsifier / risk.** If the $J$-invariant window of WP02 is incompatible with a
>   common core (domain pathology), document; that constrains the window design, not the
>   theorem's ambition.

Operationalisation, fixed in the script header before the run (the bar itself is the
WP's, unmoved): stage resolution function
$r_n(\lambda) := \min\{\lVert(D-\lambda)v\rVert : v \in V_n,\ \lVert v\rVert = 1\}$
computed exactly from the delivered pencil matrices on the $\lambda$-grid $0(0.5)50$
(stages $n \le 10$; $n = 12$ at spot points); certified continuum floor via the proven
1-Lipschitz bound; probe set $\{5.0,\ 10.586,\ 26.182\}$ fixed from F08's published
$n = 12$ table; must-hold theorem checks (Lemma 1, Theorem 4) at every grid point; two
must-pass controls (prototype finite-place filtration; exhausting Gabor family on the
identical code path); sub-wedge witness probes; mechanical branch rule
(falsifier branch iff certified floors $\ge 0.5$ at every computed stage with no
downward trend; E2b-open iff the grid minimum halves; else indeterminate).

---

## Part I — E2a: the ambient record (every statement tagged)

The E-track's target is fixed, once, as the **archimedean normal form** — the ambient
that F02, F07 and F08 already compute on. Nothing below is new mathematics; the point of
E2a is that it is now *recorded with tags in one place*, so no later step can equivocate
between ambients (the M4 discipline, [S06 §2.5](../sources/PSC2-S06-constraints-and-walls.md)).

**E2a.1 (normal form) — proven (classical).** $\mathcal H = L^2(\mathbb R, du)$,
$D = -i\,d/du$ with $\mathrm{dom}(D) = H^1(\mathbb R)$. $D$ is essentially self-adjoint
on $\mathcal S(\mathbb R)$; the Fourier transform conjugates it to multiplication by
$\tau$; hence $\mathrm{spec}(D) = \mathbb R$, purely absolutely continuous, simple, with
**no eigenvalues**. (Reed–Simon I–II; the statement is S03 Lemma 1.1 in the $u$-picture.)

**E2a.2 (Mellin presentation — why this is "the" ambient) — proven (classical).**
$(Wf)(u) = e^{u/2}f(e^u)$ is unitary $L^2(\mathbb R_+, dx) \to L^2(\mathbb R, du)$ and
carries the dilation generator $D_\infty = -i\left(x\frac{d}{dx} + \tfrac12\right)$ to
$D$. The $\tfrac12$ is the $L^2$-Plancherel normalisation: the critical line is the
unitarity line, $\mathrm{Re}\,\rho = \tfrac12$ is carried by the normalisation and never
produced as output ([S03](../sources/PSC2-S03-eigenvalue-level.md) §1).

**E2a.3 (symmetry) — proven.** $(Jf)(u) = f(-u)$ is unitary with $J = J^* = J^{-1}$ and
$JDJ = -D$; under $W$ it is the inversion $f(x) \mapsto x^{-1}f(1/x)$ — the archimedean
model of the functional-equation symmetry whose general (adelic) form E1/F01 handles.
The W1 stage spaces $V_n$ are finite spans of coherent states, hence
$V_n \subset \mathcal S(\mathbb R) \subset \mathrm{dom}(D)$, $J$-invariant by
construction (F07); **no domain pathology exists** — the WP's named risk, in its literal
"common core" form, does not occur (the actual incompatibility is quantitative, Part III).

**E2a.4 (the M4 separation — one operator concept, four ambients, four tags).**

| Ambient | What is proven about "spectrum vs zeros" there | Tag |
|---|---|---|
| Archimedean model $L^2(\mathbb R, du)$ (this project's working ambient; E2a.1–E2a.3) | $\mathrm{spec}(D) = \mathbb R$, a.c., simple — and carries **no arithmetic whatsoever**; the sieve enters only through the stage spaces $V_n$ (translation lengths, F07) | **proven** |
| Semi-local adelic $X_S$ (Connes 1999) | the trace formula at finitely many places — the L1 anchor ([S00 §6](../sources/PSC2-S00-verified-foundation.md), verified to $10^{-36}$) | **proven** |
| Global Hilbert ambient with $\mathrm{spec} = \{\gamma_\rho\}$ exactly | equivalent to Weil positivity | **RH-equivalent — wall** (K1/W6) |
| Meyer's nuclear non-Hilbert ambient (Duke Math. J. 127 (2005)) | **all** zeros realised unconditionally, with multiplicity; no Hilbert structure, no positivity — positivity is the entire remaining content | **proven (classical, cited)** — the standing category detector |

**E2a.5 (consequences, binding on every later E-step).** (i) On the fixed ambient, E2b's
payoff "every point of $\mathrm{spec}(D)$ is a limit of stage eigenvalues" means exactly
"the stage family asymptotically resolves every real energy" — an approximation-theory
statement with **zero arithmetic content**; the phrase "no zero is missed" is its shadow
only across the wall, and may not be used as more than that (O6, and the WP's honest
payoff clause, now concrete). (ii) The rigorous *global adelic* operator on a Hilbert
ambient (charter H9) is **not** delivered here and cannot be short of the wall; H9 stays
deferred. Any E-track statement that silently upgrades ambient 1 to ambient 3, or drops
to ambient 4 while keeping Hilbert-space language, is a category change and is barred.

## Part II — E2b: the theorems (proofs complete in this note)

Throughout: $D$ self-adjoint on $\mathcal H$, $V_n \subset \mathrm{dom}(D)$
finite-dimensional subspaces, $P_n$ the orthogonal projection onto $V_n$,
$H_n := P_n D P_n|_{V_n}$ (a finite Hermitian matrix; on the W1 family
$\mathrm{spec}(H_n) = \{\pm s_i\}$ exactly, F01/F07).

**Lemma 1 (residual bound) — proven.** For every $0 \ne v \in V_n$ and $\lambda \in \mathbb R$:
$$\mathrm{dist}\big(\lambda,\ \mathrm{spec}(H_n)\big) \;\le\;
\frac{\lVert P_n(D-\lambda)v\rVert}{\lVert v\rVert} \;\le\;
\frac{\lVert (D-\lambda)v\rVert}{\lVert v\rVert}.$$

*Proof.* Expanding $v$ in an eigenbasis of the Hermitian matrix $H_n$,
$\lVert(H_n - \lambda)v\rVert^2 = \sum_i |\lambda_i - \lambda|^2|c_i|^2 \ge
\mathrm{dist}(\lambda, \mathrm{spec}\,H_n)^2 \lVert v\rVert^2$. For $v \in V_n$,
$(H_n - \lambda)v = P_n(D - \lambda)v$, and $\lVert P_n\rVert \le 1$. $\blacksquare$

**Definition (stage resolution function).**
$r_n(\lambda) := \min\{\lVert(D-\lambda)v\rVert : v \in V_n, \lVert v\rVert = 1\}$.
Elementary facts, each **proven**:

- **(a)** $r_n(\lambda)^2$ is the smallest eigenvalue of the whitened
  $\widetilde M(\lambda) = \widetilde Q - 2\lambda\widetilde B + \lambda^2 I$ — the F08
  second-order pencil evaluated at *real* $\lambda$; all matrix elements are the
  delivered dps-35 closed forms. (Gram-orthonormalise; $\lVert(D-\lambda)v\rVert^2 =
  v^*(Q - 2\lambda B + \lambda^2 S)v$.)
- **(b)** $r_n$ is 1-Lipschitz in $\lambda$ (for each unit $v$,
  $\lambda \mapsto \lVert(D-\lambda)v\rVert$ is 1-Lipschitz; a pointwise minimum of
  1-Lipschitz functions is 1-Lipschitz). Hence an exact grid evaluation with step $h$
  certifies the continuum: $\min_{[0,50]} r_n \ge (\text{grid min}) - h/2$.
- **(c)** $\mathrm{dist}(\lambda, \mathrm{spec}\,H_n) \le r_n(\lambda)$ (Lemma 1).
- **(d)** At every F08 pencil root $z$: $r_n(\mathrm{Re}\,z) \le |\mathrm{Im}\,z|$ (the
  F08 quasi-mode identity exhibits a unit $u \in V_n$ with
  $\lVert(D - \mathrm{Re}\,z)u\rVert = |\mathrm{Im}\,z|$) — the F08 radii are pointwise
  upper bounds for $r_n$; the two runs must be, and are, coherent (checked in-run).

**Theorem 2 (the inclusion criterion) — proven.** Let $\mathcal C$ be any core of $D$.

1. **(Graph density $\Rightarrow$ inclusion.)** Suppose *graph-norm stage density*
   holds: for every $\phi \in \mathcal C$ there exist $v_n \in V_n$ with
   $\lVert v_n - \phi\rVert + \lVert D(v_n - \phi)\rVert \to 0$. Then
   $r_n(\lambda) \to 0$ for **every** $\lambda \in \mathrm{spec}(D)$, hence
   $\mathrm{dist}(\lambda, \mathrm{spec}\,H_n) \to 0$: every spectral point of $D$ is a
   limit of stage eigenvalues — the E2b conclusion ("no point of the spectrum missed"),
   quantitatively, with the rate $r_n(\lambda)$.
2. **(Contrapositive, the measurable form.)** If $r_n(\lambda) \not\to 0$ for some
   $\lambda \in \mathrm{spec}(D)$, graph-norm stage density fails for **every** core.

*Proof.* (1) $\mathrm{spec}(D)$ is the approximate point spectrum (Weyl's criterion for
self-adjoint operators; self-contained: for $\lambda \in \mathrm{spec}(D)$ the spectral
projection $E\big((\lambda - \varepsilon, \lambda + \varepsilon)\big) \ne 0$ for every
$\varepsilon > 0$, and any unit $\psi$ in its range has
$\lVert(D - \lambda)\psi\rVert \le \varepsilon$). So given $\varepsilon > 0$ pick a unit
$\psi \in \mathrm{dom}(D)$ with $\lVert(D-\lambda)\psi\rVert \le \varepsilon$. Since
$\mathcal C$ is a core it is graph-dense in $\mathrm{dom}(D)$: pick $\phi \in \mathcal C$
with $\lVert\phi - \psi\rVert + \lVert D(\phi - \psi)\rVert \le \varepsilon/(1+|\lambda|)$;
then $\lVert(D-\lambda)\phi\rVert \le 2\varepsilon$ and
$\lVert\phi\rVert \ge 1 - \varepsilon$. By hypothesis take $v_n \in V_n$ with graph error
$\to 0$; for $n$ large, $\lVert(D-\lambda)v_n\rVert \le 3\varepsilon$ and
$\lVert v_n\rVert \ge 1 - 2\varepsilon$, so
$r_n(\lambda) \le 3\varepsilon/(1 - 2\varepsilon)$ for all $n \ge n(\varepsilon)$.
Diagonalise over $\varepsilon \downarrow 0$ and apply Lemma 1. (2) is the contrapositive
of the implication just proven. $\blacksquare$

**Remark 1 (route correction — K2 hygiene on the WP's own chain).** The WP prescribed
"$P_n \to I$ strongly $\Rightarrow$ $H^G_n \to D$ in the strong-resolvent sense". The
second half of the chain is classical (strong-resolvent convergence $\Rightarrow$
spectral inclusion: Reed–Simon I §VIII.7, Thm VIII.24(b)); the first arrow is **false as
stated**. The core criterion (Reed–Simon I §VIII.7, Thm VIII.25(a); Weidmann GTM 68 §9.3)
requires $H_n\phi \to D\phi$ on a common core, and
$$H_n\phi - D\phi = P_nD(P_n - I)\phi + (P_n - I)D\phi:$$
the second term dies under strong convergence of $P_n$, but the first needs the
**graph-norm** control $\lVert D(I - P_n)\phi\rVert \to 0$ — $L^2$-convergence of
orthogonal projections says nothing about $DP_n\phi$ (high-frequency contamination:
precisely the M5/K2 pollution mechanism). Theorem 2 is the repaired statement, and it is
*stronger than needed*: it obtains inclusion directly from graph-norm **stage density**
(existence of *some* graph-convergent stage sequence — strictly weaker than graph
convergence of the orthogonal projections) without passing through resolvents at all.
For the record, the honest strong-resolvent version is:

**Proposition 2′ (compression s.r.c. under the correct hypotheses) — proven.** If
$P_n \to I$ strongly on $\mathcal H$ *and* $\lVert D(I-P_n)\phi\rVert \to 0$ for every
$\phi$ in a core $\mathcal C$, then $\widehat H_n := P_nDP_n$ (on $\mathcal H$)
$\to D$ in the strong-resolvent sense, and spectral inclusion follows from
Reed–Simon I Thm VIII.24(b). *Proof.* Each $\widehat H_n$ is bounded self-adjoint, so
$\mathcal C$ is a common core; the display above gives
$\widehat H_n\phi \to D\phi$ on $\mathcal C$; apply Thm VIII.25(a). (The extension of
$H_n$ by $0$ on $V_n^\perp$ can only *add* the point $0$ to a stage spectrum — harmless
for inclusion.) $\blacksquare$

**Theorem 3 (the finite-place prototype passes E2b) — proven.** On $\ell^2_\Lambda$ with
$A\,\delta_q = (\log q)\,\delta_q$ and the sieve filtration
$V_n = \mathrm{span}\{\delta_q : q \le M_n\}$
([S00 §5 Prop 6.1(1)](../sources/PSC2-S00-verified-foundation.md)): the finitely
supported vectors are a core, and each lies in $V_n$ for all large $n$ — graph-norm
stage density holds with $v_n = \phi$ eventually, and Proposition 2′'s hypotheses hold
as well ($P_n \to I$ strongly; $A(I-P_n)\phi = 0$ eventually). Hence full spectral inclusion; indeed here
$A_n = P_nAP_n$ is diagonal and $\mathrm{spec}(A_n) = \{\log q : q \le M_n\} \cup \{0\}$
exhausts $\mathrm{spec}(A)$ from below with **no pollution** (S00 Prop 6.1(1)). This is
the pattern the WP's phrase "the finite-place core is explicit" refers to: an
**exhausting** filtration realises the E2b chain verbatim. $\blacksquare$

**Theorem 4 (W1 coarse inclusion, explicit constants) — proven.** Every single coherent
state $\psi_{a,\sigma,\tau} \in V_n$ satisfies (Fourier transform of a Gaussian; the
uncertainty product saturates)
$$\lVert(D - \lambda)\,\psi_{a,\sigma,\tau}\rVert^2 \;=\; \frac{1}{4\sigma^2} + (\tau - \lambda)^2,$$
so with $b_n(\lambda) := \min_{k}\sqrt{\tfrac{1}{4\sigma_k^2} + (\tau_k - \lambda)^2}$
over the stage modes (which include $\pm\tau_k$),
$$\mathrm{dist}(\lambda, \mathrm{spec}\,H_n) \;\le\; r_n(\lambda) \;\le\; b_n(\lambda).$$
The $0$-site ladder ($\sigma_0 = \tfrac{\log 2}{2}$, spacing $4\pi/\log 2$, first rung
$\tau^{(0)}_0 = 2\pi e^{-1} + 2\pi/\log 2 \approx 11.38$, last rung
$> T_n - 4\pi/\log 2$) is present at every stage, so every real $\lambda$ with
$|\lambda| \le T_n - 2\pi/\log 2$ has a mode within $2\pi/\log 2$ of $|\lambda|$ — or
within $\tau^{(0)}_0$ of it when $|\lambda| < \tau^{(0)}_0$ — giving the explicit
uniform bounds
$$\mathrm{dist}(\lambda, \mathrm{spec}\,H_n) \;\le\; \frac{\sqrt{1 + 4\pi^2}}{\log 2} < 9.18
\quad (\tau^{(0)}_0 \le |\lambda| \le T_n - \tfrac{2\pi}{\log 2}),
\qquad \le\; 11.5 \quad (|\lambda| < \tau^{(0)}_0).$$
*Coarse inclusion holds at every stage*: no gap of length $> 18.4$ ever opens in the
covered bulk $|\lambda| \le T_n - 9.1$. (Both inequalities are additionally
machine-checked at every grid point of the run — checks T-a/T-b.) $\blacksquare$

**What Part II delivers.** The E2b *theorem* exists and is proven — as the criterion
(Theorem 2 / Proposition 2′), its verbatim realisation by the finite-place prototype
(Theorem 3), and an unconditional coarse form on W1 with explicit constants
(Theorem 4). What remains is an *instantiation question*: does the W1 family satisfy
graph-norm stage density, so that the strict conclusion ($r_n \to 0$ pointwise) holds?
That is measurable — Part III.

## Part III — the W1 measurement: the falsifier branch, quantified

## Regression check

N00 targets reproduced: **yes** — §4 spot-values ($\gamma_1, \gamma_2, \gamma_{10}$,
$\sin(\pi\gamma_1)$, $\sin(\pi\gamma_1)/(\pi\gamma_1)$; consumed only in the regression
line, per I0.6); §2 legacy $\lVert A'\rVert_{\mathrm{op}} = 9.27, 19.5, 36.3$; §3 graph
stage $\mu_1 = 3.5419$, #detached $= 4$, #detached-real $= 2$. F07 E0b anchors ($n = 4$:
dev $0.118$, dim $44$, tr-ratio $0.9899$; $n = 6$: dev $0.104$, dim $164$, tr-ratio
$0.9959$) reproduced through the F07 code path. F08 pencil anchors at $n = 4$ (min
radius $1.3387$, median $1.7411$) reproduced through the F08 code path, and the
coherence bound $r_4(\mathrm{Re}\,z) \le |\mathrm{Im}\,z|$ verified at every matched F08
root (max of $r_4(\mathrm{Re}\,z) - |\mathrm{Im}\,z|$ over matched roots
$= -7.8 \times 10^{-2} \le 0$: the exact lower envelope sits strictly below the F08
radii, as the quasi-mode identity demands). W1 closed-form self-test (S/D/Q vs
`mpmath.quad`): worst case $3.2 \times 10^{-32}$.

## Result

```
E2 — STAGE RESOLUTION r_n(lambda) AND SPECTRAL GAPS ON [0, 50]  [W1 family]
  [W1] n= 4  M_n=    31  dim=   44 (dropped   0)  grid h=0.5   #eigs in (0,50]= 17
       r_n on [0,50]:  min= 1.0626  certified floor c_n = min - h/2 = 0.8126   bands [0,15|15,30|30,50] median =  2.6666  1.8304  1.5375
       r_n at probes (5.0, 10.586, 26.182)     =   4.6788   1.2918   2.0764
       dist(., spec) at probes                 =   4.3457   1.2403   1.4664
       smallest positive eigenvalue =   9.3457   max gap in (0,50] =  4.0910   max gap in E0b window [  22.84,    60.87] =  3.9893
       sub-wedge probes dist(phi, V_n):  phi_gap = 0.7703   phi_mid = 0.8366   phi_far = 1.0000
  [W1] n= 6  M_n=   127  dim=  164 (dropped   0)  grid h=0.5   #eigs in (0,50]= 17
       r_n on [0,50]:  min= 0.9873  certified floor c_n = min - h/2 = 0.7373   bands [0,15|15,30|30,50] median =  2.6627  1.7752  1.4647
       r_n at probes (5.0, 10.586, 26.182)     =   4.6747   1.2912   1.9888
       dist(., spec) at probes                 =   4.3414   1.2446   1.7141
       smallest positive eigenvalue =   9.3414   max gap in (0,50] =  4.0298   max gap in E0b window [  33.81,   159.35] =  4.3381
       sub-wedge probes dist(phi, V_n):  phi_gap = 0.7699   phi_mid = 0.8354   phi_far = 1.0000
  [W1] n= 8  M_n=   511  dim=  538 (dropped   0)  grid h=0.5   #eigs in (0,50]= 17
       r_n on [0,50]:  min= 0.9837  certified floor c_n = min - h/2 = 0.7337   bands [0,15|15,30|30,50] median =  2.6624  1.7678  1.4600
       r_n at probes (5.0, 10.586, 26.182)     =   4.6743   1.2912   1.9755
       dist(., spec) at probes                 =   4.3410   1.2449   1.7423
       smallest positive eigenvalue =   9.3410   max gap in (0,50] =  4.0235   max gap in E0b window [  49.79,   405.57] =  3.5650
       sub-wedge probes dist(phi, V_n):  phi_gap = 0.7698   phi_mid = 0.8353   phi_far = 1.0000
  [W1] n=10  M_n=  2047  dim= 1626 (dropped   0)  grid h=0.5   #eigs in (0,50]= 17
       r_n on [0,50]:  min= 0.9832  certified floor c_n = min - h/2 = 0.7332   bands [0,15|15,30|30,50] median =  2.6623  1.7673  1.4596
       r_n at probes (5.0, 10.586, 26.182)     =   4.6743   1.2912   1.9744
       dist(., spec) at probes                 =   4.3409   1.2449   1.7441
       smallest positive eigenvalue =   9.3409   max gap in (0,50] =  4.0231   max gap in E0b window [  73.03,  1006.32] =  3.1897
       sub-wedge probes dist(phi, V_n):  phi_gap = 0.7698   phi_mid = 0.8353   phi_far = 1.0000
  [W1] n=12  M_n=  8191  dim= 4876 (dropped   0)  grid h=5.0   #eigs in (0,50]= 17
       r_n on [0,50]:  min= 1.1807  certified floor c_n = min - h/2 =-1.3193   bands [0,15|15,30|30,50] median =  4.6743  1.7617  1.4966
       r_n at probes (5.0, 10.586, 26.182)     =   4.6743   1.2912   1.9743
       dist(., spec) at probes                 =   4.3409   1.2449   1.7439
       smallest positive eigenvalue =   9.3409   max gap in (0,50] =  4.0231   max gap in E0b window [ 108.80,  2550.45] =  3.5600
       sub-wedge probes dist(phi, V_n):  phi_gap = 0.7698   phi_mid = 0.8353   phi_far = 1.0000

  genealogy across stages (rows: quantity at the pre-registered probes):
    quantity                   n= 4      n= 6      n= 8      n=10      n=12
    r_n( 5.000)               4.6788   4.6747   4.6743   4.6743   4.6743
    r_n(10.586)               1.2918   1.2912   1.2912   1.2912   1.2912
    r_n(26.182)               2.0764   1.9888   1.9755   1.9744   1.9743
    dist( 5.000, spec)       4.3457   4.3414   4.3410   4.3409   4.3409
    dist(10.586, spec)       1.2403   1.2446   1.2449   1.2449   1.2449
    dist(26.182, spec)       1.4664   1.7141   1.7423   1.7441   1.7439
    dist(phi_gap, V_n)         0.7703   0.7699   0.7698   0.7698   0.7698
    dist(phi_mid, V_n)         0.8366   0.8354   0.8353   0.8353   0.8353
    dist(phi_far, V_n)         1.0000   1.0000   1.0000   1.0000   1.0000
    grid min of r_n             1.0626   0.9873   0.9837   0.9832   1.1807
    certified floor c_n         0.8126   0.7373   0.7337   0.7332  -1.3193

  eigenvalues in (0, 50] at n=12 vs n=10: counts 17 vs 17, max |shift| (index-matched) = 9.15e-04  (F08 fingerprint: stage growth no longer moves the window)

E2 — CONTROLS (must-pass: prototype filtration, exhausting Gabor family)
  (a) prototype finite-place filtration  A_n = P_n A P_n  on l^2_Lambda:
        n= 4  M_n=    31   r(log 97) = 1.140724
        n= 6  M_n=   127   r(log 97) = 0.000000 (exact: log 97 in spec once M_n >= 97)
        n= 8  M_n=   511   r(log 97) = 0.000000 (exact: log 97 in spec once M_n >= 97)
        n=10  M_n=  2047   r(log 97) = 0.000000 (exact: log 97 in spec once M_n >= 97)
        n=12  M_n=  8191   r(log 97) = 0.000000 (exact: log 97 in spec once M_n >= 97)
      -> PASSES (exhausting filtration: r -> 0, Theorem 3)
  (b) exhausting Gabor family (u = 0, sigma_k = 2^(k-1), ladder pi/sigma):
        k=1  sigma=  1.0  dim=  36 (dropped 0)   r on [0,50]: median = 0.9329   min = 0.5000   max = 1.6431
        k=2  sigma=  2.0  dim=  70 (dropped 0)   r on [0,50]: median = 0.4796   min = 0.2500   max = 0.8215
        k=3  sigma=  4.0  dim= 140 (dropped 0)   r on [0,50]: median = 0.2267   min = 0.1261   max = 0.4108
        k=4  sigma=  8.0  dim= 280 (dropped 0)   r on [0,50]: median = 0.1180   min = 0.0625   max = 0.2054
        k=5  sigma= 16.0  dim= 560 (dropped 0)   r on [0,50]: median = 0.0576   min = 0.0312   max = 0.1027
      counting shape (report-only): N(50)/N(25) = 255/127 = 2.01 — linear, the E0-killed shape (F02): completeness on the
      window is bought at the counting law the density gate forbids.
      -> PASSES (metric is demonstrably passable: median 0.933 -> 0.480 -> 0.227 -> 0.118 -> 0.058)

VERDICT (mechanical application of the pre-registered rule)
  harness valid:            True  (prototype passes: True; Gabor exhausting family passes: True)
  theorem checks T-a/T-b/T-c: PASSED at every grid point (asserted)
  certified floors c_n on [0,50]: 0.8126  0.7373  0.7337  0.7332  -1.3193   [bar 0.5]
  grid-min trend m_last/m_first = 1.111   [falsifier branch iff >= 0.75; E2b-open iff <= 0.5]
  sub-wedge witness (phi_far >= 0.5 at every stage): True
  E2b on W1, fixed windows:  INDETERMINATE — report profiles as measured;
     no branch claimed; the bar does not move post hoc.
```

**The mechanical verdict, and its disclosed cause (two-sided reporting, I0.4).** The
branch rule as pre-registered returned **INDETERMINATE** — reported verbatim above —
and the cause is an operationalisation artifact, visible in the table: the $n = 12$
grid step was pre-registered at $h = 5.0$ (its stated role: "agreement with $n = 10$,
F08-fingerprint"), so its Lipschitz floor $c_{12} = (\text{grid min}) - h/2$ is
**vacuous by construction** ($h/2 = 2.5$ exceeds any conceivable floor), and the branch
rule's minimum ran over all stages including that vacuous entry. The substance is
unambiguous: floors are *certified* $\ge 0.73$ at all four fine-grid stages, and every
$n = 12$ sampled value agrees with $n = 10$ to $\le 9.2 \times 10^{-4}$. A post-hoc
supplement (`wp03_inclusion_supplement.py`, labelled as such — the pre-registered
verdict stands as printed) recomputes $n = 12$ on the identical fine grid:

```
WP03 SUPPLEMENT (post hoc, disclosed) — n=12 fine-grid floor, h = 0.5
  [W1] n=12  dim=4876 (dropped 0)  grid h=0.5 (101 points)
       r_12 on [0,50]:  min= 0.9831 (argmin lambda= 48.0)  certified floor c_12 = min - h/2 = 0.7331
       bands [0,15|15,30|30,50] median =  2.6623  1.7672  1.4595
       [n=10 fine-grid comparators: min = 0.9832, floor = 0.7332, bands = 2.6623 1.7673 1.4596]
  supplement conclusion: c_12 = 0.7331 >= 0.5 — the fine-grid floor is certified at n=12 as well
```

With the supplement, the certified floors are $0.8126,\ 0.7373,\ 0.7337,\ 0.7332,\
0.7331$ across **all five** stages — every value the pre-registered rule intended to
test clears its $0.5$ bar, and the $n = 12$ fine-grid profile matches $n = 10$ to
$10^{-4}$ in minimum, argmin and every band median. The INDETERMINATE above stands as
the mechanical verdict of record; the supplement removes the only ambiguity it left.

The numbers say: **(i)** the resolution function $r_n$ on the E4b window $[0,50]$ is
bounded below by a **certified** floor $c_n \ge 0.73$ at every fine-grid stage
($0.8126,\ 0.7373,\ 0.7337,\ 0.7332$ at $n = 4,6,8,10$; grid minima
$1.063 \to 0.983$, *converging upward-stable from above*, not decreasing toward $0$),
and the profile is stage-stable to $10^{-4}$ by $n = 10$ — the graph-norm stage-density
hypothesis of Theorem 2 *fails* on fixed windows for the W1 family, at every computed
stage, by a certified margin; **(ii)** the stage spectra on $(0, 50]$ are 17 points at
every stage, index-stable to $9.2 \times 10^{-4}$ between $n = 10$ and $12$, with a
permanent low-energy hole (smallest positive eigenvalue $9.3409$, stable across all five
stages — no spectrum in $(-9.34, 9.34)$, ever) and a stable largest in-window gap
$\approx 4.02$ (between the 3rd and 4th positive eigenvalues, midpoint
$\lambda \approx 16.8$); at the probes, $\mathrm{dist}(10.586, \mathrm{spec})$ sits at
$1.245$ and $\mathrm{dist}(26.182, \mathrm{spec})$ *increases* $1.466 \to 1.744$ — the
strict E2b *conclusion* (stage eigenvalues asymptotically dense in $\mathbb R$) is
failing exactly where the hypothesis fails; **(iii)** the deep sub-wedge unit vector
$\varphi_{\mathrm{far}}$ has $\mathrm{dist}(\varphi_{\mathrm{far}}, V_n) = 1.0000$ (to
four digits) at every stage — $P_n \to I$ fails outright at the computed stages, not
merely in graph norm; **(iv)** both must-pass controls behave: the finite-place
prototype drives its resolution to exactly $0$ from $n = 6$ on (Theorem 3 realised
numerically), and the exhausting Gabor family drives the same $r$-metric on the same
code path monotonically $0.933 \to 0.058$ — while exhibiting the *linear* counting
shape ($N(50)/N(25) = 2.01$) that E0 kills (F02). Completeness on a fixed window and
the convex $T\log T$ counting shape pulled against each other in every measured family.

## Verdict against the pre-registered criteria

**E2a: delivered** (Part I; every statement tagged; the M4 separation recorded once, in
one table). **E2b: the theorem is delivered and proven** (Theorems 2–4, Proposition 2′).
For the W1 instantiation, the script's mechanical branch rule returned **INDETERMINATE**
(reported verbatim; cause disclosed above — the vacuous-by-construction $n = 12$
coarse-grid Lipschitz margin inside the rule's minimum); the *WP-level* verdict, read
against the WP's own falsifier text, is the **falsifier branch, quantified**:

1. The WP's falsifier anticipated "the $J$-invariant window … incompatible with a common
   core (domain pathology)". The incompatibility is real but **not** a domain pathology
   ($V_n \subset \mathcal S$, all forms finite — E2a.3): it is the *quantitative* failure
   of graph-norm stage density on fixed windows — certified floors
   $r_n \ge c_n \ge 0.7331$ on $[0, 50]$ at all five stages ($n = 12$ via the labelled
   post-hoc fine-grid supplement; its profile matches $n = 10$ to $10^{-4}$)
   (Theorem 2(2) then kills the hypothesis for every core, at the computed stages), and
   $P_n \to I$ itself failing at the sub-wedge witness
   ($\mathrm{dist}(\varphi_{\mathrm{far}}, V_n) = 1.0000$, all stages). Per the WP's own
   text, **this constrains the window design, not the theorem's ambition**: the wedge's
   aperture at energy $\lambda$ is fixed ($u \le 1 + \log\frac{\lambda}{2\pi}$), so on a
   fixed window the family converges to a fixed-aperture limit — the same structural
   fingerprint F08 measured as the radii floor $\approx 1.72$, seen here as its exact
   lower envelope ($r_n$ grid minima $\to 0.983$; the F08 coherence check confirms
   $r_n \le$ radii pointwise).
2. **What survives unconditionally for W1**: coarse inclusion with explicit constants
   (Theorem 4 — no gap of length $> 18.4$ in the covered bulk, at any stage), and the
   moving-window picture (report-only, stated exactly as measured): the maximal spectral
   gap inside the derived E0b window stays $O(4)$ in absolute terms
   ($3.99,\ 4.34,\ 3.57,\ 3.19,\ 3.56$ across stages) while the window top grows
   $61 \to 2550$ — i.e. *relative to the window scale* the worst hole shrinks
   $6.6\% \to 0.14\%$, consistent with the derived counting law's mean spacing
   $2\pi/\log(T/2\pi) \to 0$: resolution improves *with energy*, not with stage at fixed
   energy. A strict inclusion theorem for W1 in that moving sense (or a proof of the
   fixed-window floor as $n \to \infty$, currently **verified (extrapolation)** via the
   F08 tail fingerprint) would each be a new WP with its own pre-registration.
3. **The design trade-off, named** (tag: **heuristic**, precise statement only): a
   fixed-support family whose counting law is the convex
   $R(T) = \frac{T}{2\pi}\log\frac{T}{2\pi}$ has phase-space aperture
   $U(\lambda) = 1 + \log\frac{\lambda}{2\pi}$ at energy $\lambda$, and pays
   $r_\infty(\lambda) \gtrsim c/U(\lambda) > 0$ at every fixed $\lambda$; the exhausting
   Gabor control shows the converse side (an E2-complete family with the E0-killed
   linear shape). Conjectured **aperture trade-off** — an E2-counterpart of F02's no-go
   lemma; proving it (for a precise family class) is a legitimate new-WP target. The
   pre-registered escalation for the E-track is unchanged and now doubly motivated: the
   genuinely quadratic **prolate pencil** (Connes–Moscovici; F02 redesign note, WP02b
   falsifier branch), whose window grows with the stage rather than sitting at fixed
   aperture.
4. **Consequence for WP05 (binding, additive to F08's).** E4b on $[0, 50]$ operates
   against (a) the certified-enclosure radii floor $\approx 1.72$ (F08), (b) the
   certified quasi-mode floor $r_n \ge 0.73$ on $[0,50]$, grid minima $\approx 0.98$
   (this note — no trial vector in $V_n$ localises better, at any computed stage), and
   (c) the permanent low-energy hole: no stage eigenvalue below $9.34$, while
   $\gamma_1 = 14.13\ldots$ sits inside the resolved band. WP05's design must state in
   advance its displacement-resolution budget against (a)–(b) and its handling of the
   hole (c); if the budget is unmeetable, the escalation is the prolate pencil, already
   pre-registered.

## Tag

- E2a ambient record (normal form, Mellin presentation, symmetry, M4 separation):
  **proven** (classical, cited; assembled once, binding).
- Lemma 1, Theorem 2, Proposition 2′ (inclusion criterion; corrected named-theorem
  route): **proven** (complete proofs above).
- Theorem 3 (finite-place prototype realises E2b): **proven** (S00 Prop 6.1(1) + three
  lines; control (a) verifies it numerically).
- Theorem 4 (W1 coarse inclusion, explicit constants $9.18/11.5/18.4$): **proven**
  (complete proof above; the single-state residual identity
  $\lVert(D-\lambda)\psi\rVert^2 = \tfrac{1}{4\sigma^2} + (\tau-\lambda)^2$
  cross-checked symbolically via the `sympy-verifier` MCP server, and both inequalities
  machine-checked at every grid point of the run).
- Certified floors $r_n(\lambda) \ge c_n \ge 0.73$ on $[0,50]$ at the fine-grid stages
  $n = 4, 6, 8, 10$ (grid + 1-Lipschitz; exact closed-form matrices; deterministic run,
  regression anchors reproduced first), and the spectral-gap/hole measurements:
  **verified**. The mechanical branch rule's INDETERMINATE (vacuous $n = 12$ coarse-grid
  margin): reported verbatim, cause disclosed; the $n = 12$ fine-grid floor is filed via
  the post-hoc supplement (labelled as such): $c_{12} = 0.7331$, profile matching
  $n = 10$ to $10^{-4}$ — floors certified at all five stages.
- The $n \to \infty$ persistence of the floor (the strict-sense non-inclusion limit):
  **verified (extrapolation)** — stage-stable profiles + the F08 tail fingerprint; a
  proof (tail-coupling stability lemma) is stated as an open target, not claimed.
- The aperture trade-off as a general law: **heuristic** (measured on two families +
  one prototype; conjecture stated precisely, unproven).
- Any statement connecting any of this to zeros: **none made** (E2a.5; O6).

**Scope (do-not list compliance).** No $\gamma$-list outside the N00 regression line, no
unfolding, no fitted parameter. Per E2a.5, spectral inclusion on this ambient is an
approximation statement about the W1 family and $\mathbb R$; it neither finds nor misses
any zero. No spectral conclusion is drawn from strong-resolvent convergence alone
(S06 do-not list) — indeed Part II shows the program's own planned s.r.c. route needed
repair, and the repaired criterion is what was measured. Nothing here bears on the truth
of RH, which remains **open**.

## Propagation

Charter ledger updated: **yes** (T3 row → done, falsifier branch quantified; §4
ordering update appended — WP05 next, with the resolution/hole budget binding; §6
ledger rows added for E2a/E2b). WP03 status → done (this note). WP05 status note
updated (E4b budget constraints (a)–(c) recorded). README numerics/findings lists
updated. Source doc correction notice needed: **no** (S03 states E2 as a gate; the
run-time status lives in the charter ledger per PSC2-001 §1); S03's E2 wording is
superseded in the precise form by Part II Remark 1, recorded here per the audit-trail
convention (sources are never edited). N00 unchanged (anchors for future runs live in
this note's Result block, per F03–F08 precedent).
