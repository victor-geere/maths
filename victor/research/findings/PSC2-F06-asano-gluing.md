# PSC2-F06 — WP13: the sieve step obeys an exact gluing law (proven), but no Asano-type zero locus survives it — the pre-registered falsifier fired; route γ is closed

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP13](../workpackages/PSC2-WP13-asano-gluing.md). Code/run:
`numerics/wp13_asano_gluing.py` (sympy symbolic + exact rational certification via Bareiss +
numpy float64 census; deterministic — no random draws, no `mpmath` needed). Independent
symbolic cross-checks through the `sympy-verifier` MCP server (six identities, §A4). Tags per
[PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> **Objective.** Using the per-edge product form $\prod_e(1 - u^2w_e^2)\det M(u)$
> ([S05](../sources/PSC2-S05-salvaged-G1.md) §4): test, symbolically at $n \le 6$, whether the
> sieve step $n \to n+1$ (adjoining the composites of $I_{n+1}$, i.e. Schur-complement rank-one
> vertex additions) acts on the stage polynomials as an **Asano-type contraction /
> Schur–Szegő composition preserving a zero locus** (Lee–Yang 1952; Asano 1970;
> Borcea–Brändén 2009). […] the question is whether the linear fractional structure it induces
> belongs to the stability-preserving class, **proved**, not asserted.
>
> **Deliverable.** Either: an identified gluing structure (a lemma, tag **proven**, with the
> preserved locus stated) — which would make route γ2 the first cross-scale structure to
> survive; or a documented failure at small $n$.
>
> **Falsifier (pre-registered; binding).** No identifiable gluing structure at $n \le 6$ ⇒
> **close route γ entirely** (γ1 already closed by X5); the gap program (WP07/WP08) does not
> depend on it.
>
> **Pricing.** Route γ at *full* Ramanujan strength, with C1, is the wall (W3) […] Any partial
> gluing result is stated as the locus-preservation lemma it is.

## Regression check

N00/F03 targets reproduced: **yes.** The stage builds terminate in graphs whose edge weights
reproduce `prime_graph_lab.build_bipartite` exactly (float-tie $0.0$ at every $n = 2\ldots6$,
rule I0.5); $\mu_1 = 1.3602,\ 2.3173,\ 3.5419$ and pole censuses $(10,16), (32,52), (84,106)$
at $n = 4, 5, 6$ match F03's verbatim output; the $n = 3$ chain ends at
$\rho = 15^{-1/6}$, the value forced by the proven cycle formula
$p = (1 - u^6/15)^2$. No $\gamma$-list, no zero data, and no fitted constant appears anywhere.

---

## Part A — the exact gluing structure (proven)

Throughout, $p_G(u) := \det(I - uB_w)$ and $M(u)$ is the vertex matrix of the proven weighted
Ihara–Bass identity ([F03](PSC2-F03-weighted-locus.md) Theorem A). The **atomic sieve step**
is the vertex addition $G \to G+x$: a new vertex $x$ (a composite) attached by $d$ edges of
weights $\omega_i$ to distinct existing vertices $y_i$ (its generator primes; $d = 1$ for
prime powers). The full step $n \to n+1$ is the composition of these over the composites of
the next block, so every cross-scale question reduces to the atomic step.

**Lemma A (gluing law).** With $v_i = u^2\omega_i^2$, $h_i = \frac{v_i}{1-v_i}$,
$g_i = \frac{u\omega_i}{1-v_i}$, $m_{xx} = 1 + \sum_i h_i$:

$$p_{G+x}(u) \;=\; p_G(u)\,\Psi_x(u),\qquad
\Psi_x(u) = \prod_{i=1}^d (1 - v_i)\; m_{xx}\, \det\!\big(I_d + \Gamma(u)\,\Lambda(u)\big),$$

$$\Lambda_{jk} = \delta_{jk}h_j - \frac{g_jg_k}{m_{xx}},\qquad
\Gamma(u) = \big(M_G(u)^{-1}\big)_{N(x)\times N(x)}\ \ (\text{the parent Green block}).$$

*Proof.* In $M_{G+x}(u)$ the new row/column reads $M_{xx} = m_{xx}$,
$M_{xy_i} = M_{y_ix} = -g_i$, and each $y_i$ diagonal gains $h_i$. Schur complement on the
$x$ entry: $\det M_{G+x} = m_{xx}\det(M_G + \Lambda^{\mathrm{full}})$ with
$\Lambda^{\mathrm{full}}$ supported on $N(x)\times N(x)$ as displayed (valid on the open set
$m_{xx} \ne 0$, extended by rationality). Multiply by the edge factors and apply F03 Theorem A
to both $G$ and $G+x$. The $\Gamma$-form follows where $\det M_G \ne 0$; the determinant form
$\det M_{G+x} = m_{xx}\det(M_G + \Lambda^{\mathrm{full}})$ is unconditional. $\blacksquare$

Two corrections of the quarantined X10 picture fall out immediately: the Schur correction is
**diagonal plus rank one** (not rank one), and the Green block is leaf-pruning invariant —
eliminating any degree-1 vertex $\ne y_i$ leaves $\Gamma$ unchanged (B1's Schur step is exact
on the inverse), so the gluing question lives on the 2-core, as F03's Prop. B1 predicted.
(Machine check: full-graph vs protected-core $\Gamma$ agree to $2.2\times10^{-16}$ across all
steps.)

**Lemma B ($d = 2$ transfer quadratic).** For $d = 2$, with $t = u^2\omega_1\omega_2$ and
$\Gamma = \begin{pmatrix}\gamma_{11}&\gamma_{12}\\\gamma_{12}&\gamma_{22}\end{pmatrix}$:

$$\Psi_x(u) \;=\; q\big(t(u)\big),\qquad
q(s) = 1 - 2\gamma_{12}\,s + \big(\gamma_{11}+\gamma_{22}-1-\det\Gamma\big)\,s^2 .$$

*Proof.* Three certified identities: $(1-v_1)(1-v_2)\,m_{xx} = 1 - v_1v_2 = 1 - t^2$; the
cleared correction $(1-t^2)\Lambda = \begin{pmatrix}t^2&-t\\-t&t^2\end{pmatrix}$; and
$\det\!\big((1-t^2)I_2 + t\,\Gamma\begin{pmatrix}t&-1\\-1&t\end{pmatrix}\big) =
(1-t^2)\,q(t)$ (MCP checks 1, 5, 4 of §A4). $\blacksquare$

This is the "linear fractional structure" the WP asked about, correctly derived: the step
depends on the new weights **only through** $t = u^2\omega_1\omega_2$ and on the parent
**only through** the Green block. $d = 1$ gives $\Lambda \equiv 0$, $\Psi \equiv 1$ — F03
Prop. B1 re-derived. More generally:

**Corollary (triviality).** $\Psi_x \equiv 1$ exactly whenever the addition leaves the 2-core
unchanged (leaf; second prime fresh, where $\gamma_{22} = 1, \gamma_{12} = 0$ kills both
coefficients; bridge between tree components). Verified as an equivalence at every one of the
95 vertex additions of the stage builds $n \le 6$ (classification cross-check, zero
mismatches): **the core steps are exactly the steps with $\Psi \ne 1$.**

**Lemma C (multi-affine lift and the GWS reduction).** Give the two new edges free
per-orientation variables $a_i = z_{y_i\to x}$, $b_i = z_{x\to y_i}$ (old edges at
$z_e = uw_e$). Then the lifted polynomial is

$$P_x(a,b)\;=\;p_G(u)\,\Big[\,1 - \gamma_{12}\,(s_1 + s_2) + C\,s_1s_2\,\Big],\qquad
s_1 = a_1b_2,\ s_2 = a_2b_1,\ C = \gamma_{11}+\gamma_{22}-1-\det\Gamma,$$

a **symmetric multi-affine** form in $(s_1, s_2)$; the pairs $(a_1,b_2)$ and $(a_2,b_1)$ are
disjoint, so $(s_1, s_2)$ ranges over the full bidisc $|s_i| \le r_1r_2$ as the four variables
range over $|a_i|, |b_i| \le r_i$. By **Grace–Walsh–Szegő**, nonvanishing of the lift on the
polydisc — the Asano hypothesis — is therefore *equivalent* to nonvanishing of the transfer
quadratic $q(s)$ on the disk $|s| \le r_1r_2$; and the actual sieve step is the diagonal
evaluation $s = t(u)$. The Asano contraction proper of $(s_1,s_2)$ retains only $1 + Cs$ and
is strictly coarser. *Proof:* the $s$-form factorisation is MCP check 6; the exact
identification (including absence of every other monomial, e.g. the backtracking-forbidden
$a_ib_i$ alone) is certified by the 16-corner exact evaluation [S4], which suffices because
each variable occupies a single column of $I - B_z$, making both sides multi-affine.
$\blacksquare$

### A4 — independent MCP cross-checks (`sympy-verifier`, all `equal: true`)

1. $(1-v_1)(1-v_2)(1+h_1+h_2) = 1 - v_1v_2$;
2. $\sigma_3 = 1 - e_2 + 2e_3$ and 3. $\sigma_4 = 1 - e_2 + 2e_3 - 3e_4$ for the star
   polynomial $\sigma_d = \prod(1-v_i)(1+\sum h_i) = 1 + \sum_{m\ge1}(-1)^{m-1}(m-1)e_m$
   (the general-$d$ prefactor);
4. the $t$-form determinant identity of Lemma B;
5. the cleared diagonal $(1-v_1)(1-v_2)\big[h_1m_{xx} - g_1^2\big] = v_1v_2$;
6. the asymmetric $(s_1,s_2)$ factorisation of Lemma C.

**Part A verdict: an identified gluing structure exists and is proven** — symbolically on
explicit graphs (leaf / $d=2$ / $d=3$ / bridge, plus the law against $\det(I-uB)$ on the
oriented-edge space itself), fully symbolically on the actual $n = 3$ stage step
($\Psi_{15}(v) = (1 - v^3/15)^2$, the exact 6-cycle answer), and **certified exactly over
$\mathbb{Q}$ at every one of the 95 vertex additions of the stage builds $n = 2\ldots6$**
(Bareiss determinants at rational sample points; float residuals $\le 8.4\times10^{-15}$
throughout).

---

## Part B — no zero locus survives the composition (the falsifier branch)

The step acts on stage polynomials as *multiplication* by $\Psi_x$. A multiplication operator
preserves nonvanishing on a region $\Omega$ **iff the multiplier is nonvanishing on
$\Omega$** — this is the precise content of "belongs to the stability-preserving class" for
this composition (Borcea–Brändén classify linear preservers; a parent-dependent multiplier
either avoids $\Omega$ or does not). So route γ2 reduces to: *is $\Psi_x$ zero-free on a fixed
region, uniformly along the sieve chain?* The answer is **no**, three ways.

**Obstruction 1 (Perron injection — proven).** At every core step that closes a cycle through
the existing core component, $\rho(B_{G+x}) > \rho(B_G)$ strictly: $B_G$ is a proper principal
submatrix of $B_{G+x}$, the enlarged core block is irreducible (F05's NB-irreducibility lemma),
and Perron–Frobenius gives strict monotonicity; by F03 Prop. B4 the minimal-modulus zero of
$p_{G+x}$ is the **real** point $1/\rho(B_{G+x})$, which is then strictly inside the parent's
zero-free disk and is not a zero of $p_G$ — hence a zero of $\Psi_x$. *Census:* strict at
**45 of 45** same-component core steps, $n = 3\ldots6$ (margin far above the $10^{-10}$
threshold); the two-sided control (disjoint-cycle chain) produces the "radius kept" branch as
designed. Along the chain $1/\rho$ collapses $1.5704 \to 0.2823$ over $n = 3\ldots6$
($0.0912$ by $n = 9$): the multiplier vanishes inside every centered disk eventually.

**Obstruction 2 (factor-zero invasion — proven, small).** The per-edge trivial factors
$1 - u^2w_e^2$ — the multiplicative skeleton any per-edge Asano argument works with — carry
real zeros at $\pm1/w_e$, and $w_{\max} = k\,p^{-1/2}$ grows along stages. Measured: the
innermost factor zero $1/w_{\max}^{\mathrm{core}}$ sits **inside the true zero-free disk** at
$n \le 5$ ($0.4714 < 0.7352$ at $n=4$) and inside the occupied annulus at every stage. The
per-edge product coordinates are not locus-compatible at any stage.

**Obstruction 3 (no Asano-reachable region survives — verified, $n \le 9$).** The diagonal
specialisation $z_e = uw_e$ turns every polydisc/circular-region hypothesis into a modulus
condition on $u$: Asano/GWS-reachable $u$-regions are **radially symmetric** (disks, circles,
annuli, exteriors centered at $0$). Measured on the cumulative stage zero sets $n = 4\ldots9$:
centered disks die (inner radius $0.7352 \to 0.0912$), exteriors die (outer radius
$1.6849 \to 7.3329$), and no stable avoided annulus exists — the largest radial gaps migrate
outward with $n$ and are filled by the next stages (the $n=6$ mid-bulk gap
$0.128$ @ $|u|\approx0.37$ is gone by $n=8$; at $n=9$ all top gaps sit in the transient outer
tail $|u| \approx 6.4$–$7.0$). Circles are contained in this census (a surviving circle would
sit inside a surviving gap). This measurement is consistent with, and explained by,
Obstruction 1.

**The graded chain (what Asano technology does deliver — banked).** Lemma C makes the per-step
Asano hypothesis checkable exactly: *if $p_G \ne 0$ on $|u| \le R$ and $q_u(s) \ne 0$ for
$|s| \le R^2\omega_1\omega_2$ and all $|u| \le R$, then $p_{G+x} \ne 0$ on $|u| \le R$* — a
locus-preservation lemma in the graded (Ruelle product-region) sense, stated as such per the
WP's pricing rule. Chaining the per-step certificates ($d = 2$: the exact GWS root condition;
$d \ge 3$: a norm bound) is **sound at every stage** ($R_{\mathrm{cert}} \le 1/\rho$ verified)
and tracks the true radius at efficiency $0.441, 0.628, 0.679, 0.703$ for $n = 3,4,5,6$ — the
calculus is not vacuous, but what it certifies is a **strictly collapsing disk chain**, never
a preserved locus. (Banked as a possible purely-local lower-bound tool for zero-free radii —
exploratory; shares territory with WP07 route β.)

**Off-center curiosity (exploratory).** The coverage grid finds a stable avoided disk of
radius $0.7227$ at $c = \pm(1.75 - 0.75i)$ and mirrors, flat from $n = 5$ through $n = 9$. It
is outside the Asano-reachable class (not a modulus condition), so it cannot affect the
falsifier; recorded for WP07/WP08's bulk-shape interests only.

---

## Result

`wp13_asano_gluing.py` (verbatim; sections L/T abridged where marked, full log in the run):

```
== WP13: Asano gluing on the per-edge product form — the atomic sieve step ==

== S: symbolic proofs of the gluing lemmas (sympy) ==
[S1] star polynomial sigma_2 = 1 + sum (-1)^(m-1)(m-1) e_m: True
[S1] star polynomial sigma_3 = 1 + sum (-1)^(m-1)(m-1) e_m: True
[S1] star polynomial sigma_4 = 1 + sum (-1)^(m-1)(m-1) e_m: True
[S2] transfer determinant identity: t-form True;  s-form (multi-affine) True
[S3] gluing law p_(G+x) = p_G * Psi, d=1 leaf: True (and Psi == 1)   [0.0s]
[S3] gluing law p_(G+x) = p_G * Psi, d=2: True   [0.3s]
[S3] gluing law p_(G+x) = p_G * Psi, d=3: True   [7.6s]
[S3] gluing law p_(G+x) = p_G * Psi, bridge to fresh vertex: True (and Psi == 1)   [0.1s]
[S3b] Lemma B (d=2 transfer quadratic in Green data): True
[S3c] law vs det(I-uB) on the oriented-edge space at u=1/3: True   [0.0s]
[S3c] law vs det(I-uB) on the oriented-edge space at u=2/7: True   [0.0s]
[S4] multi-affine lift P_x/p_G = 1 - g12(s1+s2) + C s1 s2 (16 corner evaluations, exact): True   [0.0s]
[S5] n=3 anchor: parent forest p == 1: True;  Psi_15(v) == (1 - v^3/15)^2: True   [0.2s]

== G + A: stage build chains — exact gluing certification, census, Asano/GWS chain ==
[n=2] steps=2 (trivial 2, core 0);  exact law over Q at v=['1/7', '3/13']: True;  float law max resid 3.3e-16;  Green core-invariance max dev 0.0e+00;  builder tie 0.0e+00   [0.0s]
[n=3] steps=6 (trivial 5, core 1);  exact law over Q at v=['1/7', '3/13']: True;  float law max resid 6.7e-16;  Green core-invariance max dev 2.2e-19;  builder tie 0.0e+00;  rho == 15^(-1/6): True   [0.0s]
       core steps (m, d): 1/rho before -> after | Asano/GWS R* | outcome
         m=15   d=2:  inf -> 1.5704  |  R*=0.6930  |  zeros appear
       injection census: strict 0, zeros-appear 1, radius-kept 0
       stage end: 1/rho=1.5704;  Asano chain R_cert=0.6930 (ratio 0.441);  spurious factor zeros at 1/wmax_core=0.7071 (inside zero-free disk: True);  soundness R_cert <= 1/rho: True
[n=4] steps=11 (trivial 8, core 3);  exact law over Q at v=['1/7', '3/13']: True;  float law max resid 1.1e-15;  Green core-invariance max dev 8.7e-19;  builder tie 0.0e+00;  F03 tie mu1=1.3602 (exp 1.3602) poles (10, 16) (exp (10, 16)): True   [0.0s]
       core steps (m, d): 1/rho before -> after | Asano/GWS R* | outcome
         m=24   d=2:  inf -> 1.0000  |  R*=0.4620  |  zeros appear
         m=28   d=2:  1.0000 -> 0.9238  |  R*=0.4620  |  injection
         m=30   d=3:  0.9238 -> 0.7352  |  R*=0.4620  |  injection
       injection census: strict 2, zeros-appear 1, radius-kept 0
       stage end: 1/rho=0.7352;  Asano chain R_cert=0.4620 (ratio 0.628);  spurious factor zeros at 1/wmax_core=0.4714 (inside zero-free disk: True);  soundness R_cert <= 1/rho: True
[n=5] steps=25 (trivial 12, core 13);  exact law over Q at v=['1/7', '3/13']: True;  float law max resid 2.4e-15;  Green core-invariance max dev 6.9e-18;  builder tie 0.0e+00;  F03 tie mu1=2.3173 (exp 2.3173) poles (32, 52) (exp (32, 52)): True   [0.4s]
       core steps (m, d): 1/rho before -> after | Asano/GWS R* | outcome
         m=42   d=3:  inf -> 1.0344  |  R*=0.4620  |  zeros appear
         m=44   d=2:  1.0344 -> 0.9778  |  R*=0.4620  |  injection
         [... 10 further strict injections; see run log ...]
         m=63   d=2:  0.4361 -> 0.4315  |  R*=0.2931  |  injection
       injection census: strict 12, zeros-appear 1, radius-kept 0
       stage end: 1/rho=0.4315;  Asano chain R_cert=0.2931 (ratio 0.679);  spurious factor zeros at 1/wmax_core=0.3536 (inside zero-free disk: True);  soundness R_cert <= 1/rho: True
[n=6] steps=51 (trivial 19, core 32);  exact law over Q at v=['1/7']: True;  float law max resid 8.4e-15;  Green core-invariance max dev 2.2e-16;  builder tie 0.0e+00;  F03 tie mu1=3.5419 (exp 3.5419) poles (84, 106) (exp (84, 106)): True   [2.4s]
       core steps (m, d): 1/rho before -> after | Asano/GWS R* | outcome
         m=72   d=2:  inf -> 1.0000  |  R*=0.4620  |  zeros appear
         m=75   d=2:  1.0000 -> 0.8922  |  R*=0.4620  |  injection
         [... 29 further strict injections; see run log ...]
         m=126  d=3:  0.2930 -> 0.2823  |  R*=0.1986  |  injection
       injection census: strict 31, zeros-appear 1, radius-kept 0
       stage end: 1/rho=0.2823;  Asano chain R_cert=0.1986 (ratio 0.703);  spurious factor zeros at 1/wmax_core=0.2828 (inside zero-free disk: False);  soundness R_cert <= 1/rho: True

== L: locus coverage — what region could an Asano chain preserve? ==
[n=4] stage zeros: 26;  min|z|=0.7352  max|z|=1.6849  zeros on imag axis: True
        cumulative radial census: inner disk 0.7352 (-> 0); outer exterior 1.6849 (-> inf); largest avoided annuli (width@radius): 0.148@|u|~0.92, 0.133@|u|~1.06, 0.156@|u|~1.20
[n=6] ... inner disk 0.2823; outer 3.2457; largest avoided annuli: 0.128@|u|~0.37, 0.155@|u|~0.56, 0.159@|u|~2.67
[n=8] ... inner disk 0.1301; outer 5.5737; largest avoided annuli: 0.124@|u|~4.86, 0.150@|u|~5.03, 0.157@|u|~5.26
[n=9] stage zeros: 2018;  min|z|=0.0912  max|z|=7.3329  zeros on imag axis: True
        cumulative radial census: inner disk 0.0912 (-> 0); outer exterior 7.3329 (-> inf); largest avoided annuli (width@radius): 0.137@|u|~6.41, 0.120@|u|~6.54, 0.112@|u|~6.98
        [off-center, not Asano-reachable] largest avoided disk (centers |c|<=2): radius 0.7227 at c=1.75-0.75j

== T: controls — genuine preservation must PASS, planted bump must FLAG ==
[T1] disjoint 4-cycle chain (w=1): all zeros on |u|=1: True;  rho constant after first cycle: True  -> preservation recognised: True
[T2] planted bump (w=1.3 cycle): rho 1.0000 -> 1.3000, min|z|=0.7692 < 1: flagged as injection: True

[verdict] gluing law p_(G+x) = p_G * Psi_x: PROVEN symbolically (S) and certified exactly over Q on every vertex addition of the stage builds n = 2..6 (G): True
[verdict] locus preservation: FAILS. [...]
[verdict] the graded Asano/GWS chain is sound [...] a collapsing disk chain, not a preserved locus.

HARNESS PASS: all symbolic/exact/two-sided checks passed   [13s total]
FALSIFIER (pre-registered, binding): no locus-preserving Asano-type gluing structure at n <= 6 -> route γ closes entirely (γ1 already closed by X5).
```

The numbers say: the atomic sieve step has a clean, fully proven algebraic gluing law — the
honest content that X10's "Asano Compatibility" pretended to have — and that law makes the
Asano question decidable rather than merely testable: the step is multiplication by a
Green-data quadratic, its polydisc/Asano hypothesis is (by Grace–Walsh–Szegő) exactly a root
condition on that quadratic, and the multiplier **provably vanishes inside every centered
candidate region along the chain** (strict Perron injection at all 45 same-component core
steps, inner radius $\to 0$, outer radius $\to \infty$, no stable annulus). Genuine
preservation is recognisable by this harness (the control chain passes), so the failure on the
sieve chain is a property of the object, not of the instrument.

## Verdict against the pre-registered criteria

**Deliverable: both branches, honestly split.** The "identified gluing structure" exists and
is **proven** (Lemmas A–C) — but its preserved locus is empty: the locus-preservation question
the WP actually posed lands in the **documented-failure branch**, established by proof
(Obstruction 1) plus two-sidedly controlled measurement (Obstructions 2–3), not by
failure-to-find. **The pre-registered falsifier fires: route γ is closed entirely** (γ1 by X5,
γ2 by this note). Per the WP's own scoping, the gap program (WP07/WP08) is unaffected, and W3
(route γ at full Ramanujan strength) remains a priced wall — closing the *finite-stage gluing
route to it* changes nothing about its RH-equivalence.

## Tag

- Lemma A (gluing law), Lemma B (transfer quadratic), Lemma C (multi-affine lift + GWS
  reduction), triviality corollary: **proven** (symbolic proofs; exact $\mathbb{Q}$
  certification at all 95 stage vertex additions $n \le 6$; six MCP cross-checks; controls).
- Obstruction 1 (strict Perron injection at same-component core steps; multiplier vanishes in
  the parent zero-free disk): **proven** (PF + F05 NB-irreducibility + F03 B4); census
  **verified** 45/45.
- Obstruction 2 (factor-zero invasion at $n \le 5$; annulus overlap at all stages) and
  Obstruction 3 (no Asano-reachable region survives, $n \le 9$): **verified**.
- Graded-chain efficiency ($0.44 \to 0.70$) as a local lower-bound tool: **exploratory**.
- Off-center avoided disk ($0.72$ at $|c| = 1.9$, stable $n = 5\ldots9$): **exploratory**.
- **Route γ2 / Q-γ2 / gate G6: dead end** (pre-registered falsifier; do not reopen — X13).
- RH: **open**.

**Scope (do-not list compliance).** Everything here concerns finite weighted divisor graphs'
non-backtracking polynomials; nothing is a statement about $\zeta$'s zeros; no $\gamma$-data
was consumed; the correct-locus rule (I0.3) is respected throughout. I0.7 note: the new
harness components are graph-side and $\zeta$-blind — no zeta-facing evidence is produced for
the sine decoy to exercise; the two-sided instrument controls are T1/T2 (genuine-preservation
recognition and a planted violation), per the F03 control pattern.

## Propagation

Charter ledger updated: **yes** (live conjecture 5 closed; H5/WP13 → done, falsifier branch;
status-ledger rows added; ordering update appended). Source doc correction notice needed:
**yes** — dated closure notices appended to S02 (gate G6) and S06 (X-ledger entry X13:
route γ2). WP13 status → done (falsifier branch). README updated (numerics + findings lists).
Parent snapshot reflection per README convention: pending (this project's docs are the source
of truth).
