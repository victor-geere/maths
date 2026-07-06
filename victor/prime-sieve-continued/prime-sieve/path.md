# path.md — A corrected proof path for the Ihara–Connes program (steps 3 and 4)

*Completes, at the level of a staged research path, the two closing items of
[ihara-connes.html](ihara-connes.html): §3 (make the CCM connection concrete) and §4 (the three
technical hurdles). Every node is tagged per the repository
[rigour convention](../CLAUDE.md): **proven** / **conditional** / **RH-equivalent** /
**heuristic**. The defects of the previous artifacts (empty graph, tautological unfolding,
misstatements M1–M5) are catalogued in [notes.md](notes.md) §2 and are *not* inherited here.*

*Status of this document: a path, not a proof. Its proven content is P1.1, P2.1–P2.4, P3.1–P3.2,
P3.4, and the trace-level identities imported from [../adele/phase6.md](../adele/phase6.md).
RH remains **open**; the path's own Theorem P2.3 explains precisely why the final rung
cannot be anything but the known wall.*

---

## P0. The corrected finite objects

Two stage-$n$ constructions replace the (empty) block graph of the scripts. Both are
sieve-computable: by stage $n$ the composite-generator sieve
([../adele/phase1.md](../adele/phase1.md), Lemma 1) has produced every prime
$\le M_n = 2^{n+1}-1$.

**Definition P0.1 (place-cycle model $X_N$; the Connes-faithful object).**
For each prime $p \le M_n$ take one *directed metric cycle* $c_p$ of length $\ell_p = \log p$
(one complex dimension per prime, holonomy $p^{-s}$ at spectral parameter $s$). Let
$T_n(s) = \bigoplus_{p \le M_n} \big(p^{-s}\big)$ on $\mathbb{C}^{\pi(M_n)}$ and define the
**stage secular determinant**

$$D_n^{\mathrm{cyc}}(s) \;=\; \det\big(I - T_n(s)\big) \;=\; \prod_{p \le M_n}\big(1 - p^{-s}\big).$$

Periodic orbits of the disjoint union are words $\prod_p c_p^{k_p}$ of total length
$\sum_p k_p \log p = \log m$, $m$ an $M_n$-smooth integer: **orbit lengths are logarithms of
integers**, the exact support of the prime side of the explicit formula. — construction
**proven** (elementary); it is the geometric-side skeleton of Connes' trace formula, one place
per cycle, cf. [../adele/phase6.md](../adele/phase6.md) §6.2.

**Definition P0.2 (bipartite divisor graph $B_n$; the coupled object).**
Vertex classes $\mathcal P_n = \{\text{primes } p < 2^n\}$ and
$\mathcal C_n = \{\text{composites } m \in I_n = [2^n, 2^{n+1})\}$; an edge $p \sim m$ iff
$p \mid m$, with weight $w_\beta(p,m) = a_p(m)\,p^{-\beta}$ ($a_p(m)$ the multiplicity,
$\beta$ a calibration exponent, default $\beta = \tfrac12$ per the von Mangoldt normalisation of
[../berry-keating/prime-side.md](../berry-keating/prime-side.md)). This is exactly the
cross-scale coupling that repaired Phase 3 (Def 3.2 there), now read as a graph. **Non-vacuous:
proven** (e.g. every even $m \in I_n$ joins $2$ to its odd part's factors; edge count grows like
$2^n \log\log 2^n$). Its weighted non-backtracking (Hashimoto) operator $B_n^{\mathrm{nb}}$ and
weighted Bass determinant $\det(I - u\,B_n^{\mathrm{nb}})$ are the stage objects
(weighted Ihara determinant: Mizuno–Sato 2004; to be re-verified symbolically —
[implementation.md](implementation.md) I1).

**Remark P0.3 (division of labour).** $X_N$ carries the *exact arithmetic* (its determinant is
the truncated Euler product — nothing more, nothing less). $B_n$ carries *couplings* (composites
tie small primes together). The path's genuine open conjecture (H\*, below) is that a
sieve-computable coupling correction to $X_N$'s determinant — of the kind $B_n$ supplies —
produces stage determinants that keep converging **inside the critical strip**. The bare $X_N$
provably cannot (P1.3).

---

## P1. Hurdle (i) — uniform Fredholm-determinant convergence (statement C1)

**Target C1.** There exist stage determinants $D_n(s)$ (entire, sieve-computable, of the form
archimedean prefactor $\times$ weighted Bass/secular determinant) and a nonvanishing elementary
factor $e(s)$ such that $D_n(s) \to e(s)\,\xi(s)$ **locally uniformly on the open strip**
$\Omega = \{0 < \mathrm{Re}\,s < 1\}$, where $\xi$ is the completed zeta. — **open** (this is
the load-bearing beam of the whole path).

**Lemma P1.1 (determinant continuity; the correct convergence currency). — proven (classical).**
For trace-class $A, B$ on a Hilbert space,
$$\big|\det(I-A) - \det(I-B)\big| \;\le\; \lVert A-B\rVert_{1}\,
\exp\!\big(\lVert A\rVert_{1} + \lVert B\rVert_{1} + 1\big).$$
Hence if $s \mapsto T_n(s)$ are holomorphic trace-class–valued, $T_n(s) \to T(s)$ in
$\lVert\cdot\rVert_1$ uniformly on compacts of a region, then the Fredholm determinants converge
locally uniformly there and the limit is holomorphic. (Simon, *Trace Ideals*, Thm 3.4;
Gohberg–Krein.) This is the precise meaning to give "uniform Fredholm determinant convergence"
in ihara-connes.html §4(i).

**Proposition P1.2 (C1 on $\mathrm{Re}\,s > 1$, place-cycle model). — proven.**
$\lVert T_n(s)\rVert_1 = \sum_{p \le M_n} p^{-\sigma} \le P(\sigma) < \infty$ for
$\sigma = \mathrm{Re}\,s > 1$, and $\lVert T(s) - T_n(s)\rVert_1 = \sum_{p > M_n} p^{-\sigma}
\to 0$ uniformly on compacts of $\{\sigma > 1\}$. By P1.1,
$D_n^{\mathrm{cyc}}(s) \to 1/\zeta(s)$ locally uniformly on $\{\sigma > 1\}$. $\blacksquare$
(The convergence *rate* is the Euler tail $\asymp M_n^{1-\sigma}/((\sigma-1)\log M_n)$ —
measured in [implementation.md](implementation.md) I2; compare the $O(M_n^{-1/2})$ trace rate of
[../adele/phase6.md](../adele/phase6.md) §6.3c.)

**Proposition P1.3 (the bare model dies at the line $\sigma = 1$). — proven.**
For $\sigma \le 1$, $\sum_p p^{-\sigma} = \infty$: $T(s)$ is not trace class, no subsequence of
$T_n(s)$ is $\lVert\cdot\rVert_1$-Cauchy, and indeed $\prod_{p\le M_n}(1-p^{-s})$ diverges (has
no nonzero limit) in the strip. **The strip version of C1 for the uncoupled model is exactly the
analytic-continuation problem**, in agreement with [../adele/phase7.md](../adele/phase7.md):
truncating the Euler product reorganizes the prime side but cannot cross the line by itself.
$\blacksquare$

**Hypothesis H\* (the folder's real conjecture). — open, falsifiable.**
There is a sieve-computable coupling correction — a weighted-graph modification
$D_n(s) = G_\infty^{(n)}(s)\cdot\det(I - u\,B^{\mathrm{nb}}_{w,n})\big|_{u\text{-dictionary}}$
built from $B_n$'s composite couplings, with explicit archimedean prefactor
$G_\infty^{(n)} \to \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)$ — satisfying C1 on $\Omega$.
*Evidence for:* the Gonek–Hughes–Keating hybrid formula (2007) writes $\zeta$ unconditionally
(in controlled ranges) as (truncated Euler product) $\times$ (truncated Hadamard product over
zeros) — precisely the shape "arithmetic factor $\times$ spectral factor", and a spectral factor
is what a *graph determinant* can natively supply, its zeros being honest spectral data.
*Evidence against / caution:* Lemma P3.4 (Turán–Montgomery): for a badly chosen family the
analogue of C1+C2 provably fails; nothing guarantees the sieve couplings are the right ones.
*Proof obligations:* (H\*-a) identify the weight class (calibrate $\beta$, archimedean factor);
(H\*-b) prove local-uniform convergence on $\{\sigma > 1\}$ *with couplings on* (consistency
with P1.2 — couplings must vanish in the limit there); (H\*-c) prove a normal-family/tightness
bound on compacts of $\Omega$ (uniform $\log|D_n|$ upper bound + nonvanishing at one interior
point suffices, Montel + Vitali); (H\*-d) identify the limit on a set with a limit point
(functional-equation symmetry of the stages would do it, and is itself a falsifiable design
constraint: build $B_n$ so that $D_n(s)$ and $D_n(1-s)$ are related exactly — see
[implementation.md](implementation.md) I2.3).

---

## P2. The Hurwitz dictionary — what C1 buys, exactly (this replaces proof-sketch's endgame)

Throughout P2, assume C1 on $\Omega$ (open strip), write $Z = e\,\xi$ for the limit, and recall
$Z \not\equiv 0$.

**Lemma P2.1 (transfer of nonvanishing, limit $\to$ stages). — proven.**
Let $K \subset \Omega$ be compact with $Z$ zero-free on $K$. Then $\exists\, n_0$ such that
$D_n$ is zero-free on $K$ for all $n \ge n_0$.
*Proof.* $\delta := \min_K |Z| > 0$ by compactness and continuity; for $n$ with
$\sup_K|D_n - Z| < \delta/2$, $|D_n| \ge \delta/2 > 0$ on $K$. $\blacksquare$

**Lemma P2.2 (zero capture, stages $\to$ limit). — proven.**
(a) If $z_n \to z^* \in \Omega$ with $D_n(z_n) = 0$, then $Z(z^*) = 0$.
(b) Conversely (Hurwitz), if $Z(z^*) = 0$ with multiplicity $m$, then for every sufficiently
small disc $\overline{B(z^*,r)} \subset \Omega$ there is $n_1$ with: for all $n \ge n_1$, $D_n$
has exactly $m$ zeros (with multiplicity) in $B(z^*, r)$.
*Proof.* (a) $|Z(z^*)| \le |Z(z^*)-Z(z_n)| + |Z(z_n)-D_n(z_n)| \to 0$ by continuity and local
uniform convergence. (b) Choose $r$ with $Z \ne 0$ on $0 < |z - z^*| \le r$; let
$\delta = \min_{|z-z^*|=r}|Z| > 0$; for $n$ with $\sup_{|z-z^*|=r}|D_n - Z| < \delta$, Rouché
gives $D_n$ and $Z$ the same zero count in the disc. $\blacksquare$

**Theorem P2.3 (the endgame, stated honestly). — proven, and it is the wall.**
Assume C1. Define
$$\text{(C2)}:\quad \text{for every compact } K \subset \Omega \setminus
\{\mathrm{Re}\,s = \tfrac12\},\ \exists\, n_0:\ D_n \text{ is zero-free on } K\ \forall n \ge n_0.$$
Then **C2 $\iff$ RH.**
*Proof.* ($\Leftarrow$) RH makes $\xi$ (hence $Z$) zero-free on every such $K$; apply P2.1.
($\Rightarrow$) If RH fails, $\xi$ has a zero $z^*$ off the line inside $\Omega$; take a closed
disc around $z^*$ avoiding the line; P2.2(b) plants zeros of $D_n$ in it for all large $n$,
contradicting C2 on that disc. $\blacksquare$

**Corollary P2.4 (graded ladder: gaps $\iff$ zero-free regions). — proven.**
Assume C1, and let $\Omega' \subset \Omega$ be open. Then $\xi$ is zero-free on $\Omega'$
$\iff$ every compact $K \subset \Omega'$ is eventually zero-free for $(D_n)$. In particular each
*partial* confinement estimate for stage zeros is exactly equivalent to a zero-free region for
$\zeta$, and conversely the classical regions (de la Vallée Poussin 1899, Vinogradov–Korobov
1958) *force* corresponding eventual stage-zero confinement. Same proofs. $\blacksquare$

**Reading (per the rigour convention).** P2.3 says: **given C1, hurdle (iii) at full uniform
strength is not "a step toward RH" — it is RH**, verbatim, in graph coordinates. The program
therefore cannot end anywhere but at the known frontier
([../adele/phase7.md](../adele/phase7.md) §7.5; research-findings §7). What the coordinates
change is the *available toolset* (P3), and — via P2.4 — the existence of **honest intermediate
rungs**: every unconditional partial gap theorem for the stages is a genuine zero-free-region
theorem, no RH needed, no circularity. Note also what P2 does *not* need: hurdle (ii) plays no
role in the function-theoretic route; its correct role is the operator upgrade (P4).

---

## P3. Hurdle (iii) — the spectral-gap program (with the wall marked)

### P3.1 Structural confinement: why graph stages are the right approximants

**Theorem P3.1 (pole confinement; Kotani–Sunada). — proven (classical).**
For a finite connected $(q{+}1)$-regular graph, the nontrivial poles of the Ihara zeta
$\zeta_X(u)^{-1} = (1-u^2)^{r-1}\det(I - uA + qu^2 I)$ solve $qu^2 - \lambda u + 1 = 0$,
$\lambda \in \sigma(A)$ real (self-adjointness!). If $|\lambda| \le 2\sqrt q$ the two roots form
a conjugate pair on $|u| = q^{-1/2}$; if $2\sqrt q < |\lambda| \le q+1$ they are real with
product $1/q$. Hence **all** poles lie on the circle $|u| = q^{-1/2}$ **or** on the real axis;
for irregular graphs the non-real poles lie in the annulus
$q_{\max}^{-1/2} \le |u| \le q_{\min}^{-1/2}$ (Kotani–Sunada 2000). $\blacksquare$

Under the dictionary $u = q^{-s}$: circle $\mapsto \mathrm{Re}\,s = \tfrac12$; positive real $u$
$\mapsto \mathrm{Im}\,s \equiv 0$, negative real $u \mapsto \mathrm{Im}\,s \equiv \pi/\log q$
(mod $2\pi/\log q$). **Finite regular stages cannot have generic complex off-line zeros at all;
the only possible off-line zeros are "real" ones — the graph avatar of Landau–Siegel zeros.**
(The scripts' "poles on $|u|=1$" claim was the empty-graph artifact plus misstatement M1 —
[notes.md](notes.md) §2.)

**Contrast (why family choice is load-bearing):**

**Lemma P3.4 (Turán–Montgomery caution). — proven (classical).**
The partial sums $\zeta_N(s) = \sum_{n \le N} n^{-s}$ have zeros with $\mathrm{Re}\,s > 1$ for
all large $N$ (reaching $\mathrm{Re}\,s = 1 + c\frac{\log\log N}{\log N}$, Montgomery 1983),
although $\zeta$ itself is **proven** zero-free there. So a natural approximating family can
violate the C2-analogue *inside a region where the limit is zero-free*: approximants do not
inherit zero-freeness for free, and Turán's 1948 hope died exactly here. The graph stages'
advantage over $\zeta_N$ is Theorem P3.1: **spectral origin $+$ self-adjointness confine stage
zeros a priori**; partial sums have no such confinement. $\blacksquare$

*Proof obligation W (weighted confinement).* Extend P3.1 to the weighted bipartite
$B^{\mathrm{nb}}_{w,n}$ (weighted Bass formula, Mizuno–Sato 2004): produce the annulus/circle +
real-locus statement with weights $w_\beta$. Finite, checkable, symbolically verifiable at small
$n$ ([implementation.md](implementation.md) I4). — **open, elementary-looking**.

### P3.2 The graph-Siegel dictionary — heuristic, precisely stated

Exceptional eigenvalues $|\lambda| > 2\sqrt q$ (equivalently real $u$-poles off the Ramanujan
circle) are the stage-$n$ objects whose *persistence* as $n \to \infty$ would violate C2 near
the real axis — the locus of Siegel/Landau zeros. Conversely their eventual absence on compacts
is, by P2.4, a real-zero-free statement. The trivial Perron eigenvalue (graph connectivity) is
the stage avatar of the pole of $\zeta$ at $s=1$ — it *should* persist; the Siegel question is
about the *second* real eigenvalue. This dictionary organises route α and is testable now
([implementation.md](implementation.md) I4: track real $u$-poles across $n$; prediction —
Perron survives, all others retreat to the circle). — **heuristic** (the dictionary), with each
side's endpoints **proven** (P3.1; classical Siegel-zero theory).

### P3.3 Three attack routes for the gap, tagged

**Route α (sieve inequalities $\to$ weak gap $\to$ dlVP rung). — open, tractable; milestone M1.**
The proven prototype that "sieve inequality = spectral bound" is the **large sieve**
(Montgomery 1968/1971): $\sum_{q\le Q}\sum^{*}_{a\,(q)}\big|\sum_{n\le N}a_n e(an/q)\big|^2 \le
(N + Q^2)\sum|a_n|^2$ — literally an operator-norm bound for the primes/progressions incidence
structure. For $B_n$: the prime-side coupling matrix has
$(WW^{\mathsf T})_{pq} = \#\{m \in I_n : pq \mid m\}\,(pq)^{-\beta} \approx 2^n (pq)^{-1-\beta}$
— Perron part rank one; the fluctuation part is a bilinear form over divisor counts in a dyadic
block, exactly large-sieve/Brun–Titchmarsh territory. *Target Proposition P3.5:* the weighted
non-backtracking spectral gap of $B_n$ is $\ge c/\log M_n$. *Payoff via P2.4 (once C1/H\* is in
place):* a zero-free region of classical de la Vallée Poussin strength. *Calibration value even
before C1:* if the machinery cannot deliver P3.5 numerically, H\* is likely mis-weighted —
falsification first ([implementation.md](implementation.md) I5). Proof inputs: Brun–Titchmarsh,
Montgomery large sieve, Lemma 2 of [../adele/phase1.md](../adele/phase1.md)
($\widehat{\mu}_n(k) = O_k(1/\log M_n)$ — note the $1/\log$ matches the target gap strength;
this consistency is a good sign the route is correctly calibrated, and a warning that it cannot
give more than dlVP without new input).

**Route β (Bordenave's tangle-free trace method, deterministically). — open.**
Bordenave's proof of Friedman's theorem (random regular graphs are almost-Ramanujan) bounds
$\mathrm{Tr}\,(B^{\mathrm{nb}})^{2k}$ by counting tangle-free non-backtracking paths — a purely
combinatorial sieve over path words. Transplant: for the deterministic $B_n$, the randomness
input is replaced by the sieve's proven equidistribution (Lemma 2). Expected strength: again
$1 - O(1/\log)$ (the equidistribution decay), i.e. the same dlVP rung as route α by a different
engine — a useful independence check. (Bordenave 2020; Bordenave–Collins 2019 for lifts.)

**Route γ (full Ramanujan technologies: interlacing / Lee–Yang). — open; full strength sits at
the wall by P2.3.**
The only known ways to *reach* (not approach) Ramanujan bounds are reality/positivity
technologies: (1) **Deligne's proof of RH over finite fields** behind LPS/Margulis Ramanujan
graphs — an RH powering an RH-analogue; (2) **MSS interlacing families** (Marcus–Spielman–
Srivastava 2015): *bipartite* graphs admit 2-lifts (Bilu–Linial) whose new spectrum stays within
$2\sqrt{\Delta-1}$, proven via real-rootedness of expected characteristic polynomials — note our
corrected stage object $B_n$ **is bipartite**, so the technology is type-correct; (3)
**Lee–Yang/Asano** (statistical mechanics): zeros of partition functions confined to circles,
preserved under Asano contraction/gluing (Lee–Yang 1952; Asano 1970; modern form
Borcea–Brändén 2009). Two crisp open questions, both machine-checkable at small $n$:
- *Q-γ1 (covering structure):* is $B_{n+1}$ (approximately) a lift/covering of $B_n$ in the
  Bilu–Linial sense? The dyadic doubling of the sieve is suggestive; if yes, the MSS machinery
  applies to the actual tower.
- *Q-γ2 (Asano gluing):* does the sieve recursion (composites of $I_{n+1}$ from primes
  $\le 2^{n+1}$) act on the weighted Bass polynomials as an Asano-type product preserving the
  zero-locus annulus? Each instance is a finite polynomial identity —
  [sympy verification](../../../sympy/mcp_server.py) applies
  ([implementation.md](implementation.md) I4.3).

Honesty note: by P2.3, success of route γ *at full uniform strength, together with C1*, would
**be** RH; per the convention, route γ's full rung must be expected to be RH-equivalent-or-harder,
and any partial rung must be stated as the zero-free region it is (P2.4). Reality-of-roots
technology (MSS) is structurally the Hermite–Biehler wall (research-findings N3/§6.2) in
polynomial coordinates — the same wall, new tools.

---

## P4. Hurdle (ii) — the operator upgrade (norm-resolvent convergence), and what it is *for*

Corrected statement (fixes M5, [notes.md](notes.md) §2.3): the useful mode is
**norm-resolvent** convergence — for self-adjoint $H_n \to H$ it gives spectral convergence
without pollution ($\sigma(H_n) \to \sigma(H)$ locally in Hausdorff distance; Reed–Simon
VIII.7). *Strong* resolvent convergence (closed-form.md §5) controls neither pollution nor
gaps and cannot support the intended conclusion.

- **What (ii) is for.** Not needed for P2's function-theoretic route. Its role: upgrade the
  zero set to the **spectrum of a limiting self-adjoint operator on a Hilbert space** — the
  Hilbert–Pólya payoff. If a positive-inner-product limit exists with norm-resolvent
  convergence of the (self-adjoint!) finite stages, C2 follows *automatically* (real spectrum);
  by P2.3 that is RH. So (ii)-with-positivity is **expected RH-equivalent** (unproven claim of
  equivalence avoided; what is proven is the implication chain just stated).
- **Calibration (proven neighbours).** (a) Meyer 2005: an unconditional spectral realization of
  *all* zeros exists on **nuclear non-Hilbert** spaces — positivity is the *entire* remaining
  content (research-findings §7.3). Any (ii)-claim must say where its positivity comes from, or
  it has silently changed category to Meyer's. (b) Connes–Moscovici 2022 (prolate wave
  operator): a concrete self-adjoint operator whose negative spectrum matches the squares of
  the low zeros numerically, with a proven semiclassical counting match — the archimedean fiber
  model of the sought limit; exact spectral identification **open/conjectural**. (c)
  Benjamini–Schramm $\to$ Plancherel/Kesten–McKay: for bounded-degree stages converging locally
  to the $(q{+}1)$-regular tree, spectral measures converge to the tree's Plancherel measure —
  the proven *weak* (measure-level) precursor of (ii) at a single place. Our $B_n$ has
  unbounded degrees (vertex $2$ has degree $\sim 2^{n-1}$), so even BS-convergence requires the
  weighted/rescaled setup — listed as proof obligation, **open**.
- **Krein risk (where (ii) can silently fail).** The natural limiting pairing built from
  sieve weights may become indefinite or degenerate (Krein space), exactly the N1/N2 no-go
  territory of research-findings §3 — self-adjointness at every finite stage does **not**
  guarantee a positive-definite limit inner product. This is the operator-language name of the
  wall, matching [../adele/phase7.md](../adele/phase7.md) §7.5 ("intrinsic route with
  positivity").

---

## P5. Step 3 completed: the CCM connection made concrete (and what is genuinely new here)

The bridge between trace level (done, in-repo) and determinant level (this path):

$$\log\det\big(I - T_n(s)\big) \;=\; -\sum_{k\ge1} \frac{1}{k}\,\mathrm{Tr}\,T_n(s)^k,
\qquad
-\frac{d}{ds}\,\log\det\big(I - T_n(s)\big)\Big|_{\text{cycle model}}
= \sum_{p\le M_n}\sum_{k\ge1} (\log p)\, p^{-ks},$$

whose $n \to \infty$, $s \mapsto \tfrac12 - iz$ reading is exactly the weighted flow character
$\chi_W(z) = -\frac{\zeta'}{\zeta}(\tfrac12 - iz)$ of
[../berry-keating/prime-side.md](../berry-keating/prime-side.md) Thm 5.3. Hence:

| Level | Object | Status in repo |
|---|---|---|
| trace (linear in test $g$) | place-by-place Weil trace $W_\infty - \sum_p W_p$ | **proven + verified to $10^{-36}$** ([../adele/phase6.md](../adele/phase6.md)) |
| character (fixed $s$/$z$) | $\chi_W = $ derivative of $\log$-determinant | **proven** (prime-side.md Thm 5.3); poles = zeros reached only by continuation ([../adele/phase7.md](../adele/phase7.md) Obs 7.1) |
| determinant (uniform in $s$) | C1: $D_n \to e\,\xi$ locally uniformly on the strip | **open** — the precise content this folder adds to the CCM connection |

So "supplying finite approximations to the adele class space" (ihara-connes.html §3) now has an
operational meaning: **the sieve stages already compute Connes' geometric side at trace level;
the Ihara/graph program is the attempt to integrate and uniformise that data into a convergent
spectral determinant (C1), at which point P2 converts spectral-gap statements into zero-location
statements, rung by rung.** The Ramanujan-property reading of RH in CCM coordinates is Theorem
P2.3 — with its honest label attached.

The archimedean place: the prefactor $G_\infty^{(n)} \to \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)$
is imported, not graph-emergent, at this stage of the path; the CCM scaling-site expectation
(archimedean fiber as boundary of the tower, Connes–Consani; prolate operator as its spectral
model, Connes–Moscovici) is recorded as the natural (ii)-side target — **heuristic** here.

---

## P6. Honesty ledger (the whole path in tags)

| Node | Content | Tag |
|---|---|---|
| P0.1 / P0.2 | corrected finite objects (place cycles; bipartite divisor graph), non-vacuity | **proven** |
| P1.1 | determinant-continuity currency | **proven** (classical) |
| P1.2 | C1 on $\mathrm{Re}\,s > 1$ (cycle model) | **proven** |
| P1.3 | bare Euler truncation cannot cross $\sigma = 1$ | **proven** |
| H\* | coupled stage determinants converge in the strip | **open** (the conjecture; falsifiable via I2/I5) |
| P2.1–P2.2 | transfer lemmas | **proven** |
| P2.3 | given C1: C2 $\iff$ RH | **proven equivalence; marks the wall** |
| P2.4 | given C1: partial gaps $\iff$ zero-free regions | **proven** |
| P3.1 | Kotani–Sunada confinement | **proven** (classical) |
| P3.2 | graph-Siegel dictionary | **heuristic** (endpoints proven) |
| P3.4 | Turán–Montgomery caution | **proven** (classical) |
| P3.5 | $c/\log$ gap for $B_n$ from sieve inequalities | **open, tractable** (milestone M1) |
| Q-γ1, Q-γ2 | covering-tower / Asano-gluing structure of the sieve | **open**, machine-checkable |
| Route γ full | uniform Ramanujan for the stages (with C1) | by P2.3 **= RH**; treat as RH-equivalent target, not a step |
| P4 | norm-resolvent + positive limit space | **open**; positivity is the wall (Meyer calibration) |
| P5 | trace→character→determinant ladder; CCM dictionary | trace/character **proven** (imported); determinant **open** (= H\*) |

**Declaration discipline.** Per [CLAUDE.md](../CLAUDE.md): nothing here claims a proof of RH
or progress-toward-proof beyond the tagged proven lemmas; the door stays open strictly at the
stated bar (every link proven, chain terminating at the zeros themselves, adversarial + symbolic
+ numerical verification). The path's designed *first* deliverables are deliberately below the
wall: proof obligation W, Proposition P3.5 (→ dlVP rung), Q-γ1/Q-γ2 answers, and the I-series
falsification experiments of [implementation.md](implementation.md).

---

## References (path-specific; repo-wide list in research-findings.md)

Ihara, *J. Math. Soc. Japan* 18 (1966) · Bass, *Internat. J. Math.* 3 (1992) 717–797 ·
Hashimoto, *Adv. Stud. Pure Math.* 15 (1989) · Kotani–Sunada, *J. Math. Sci. Univ. Tokyo* 7
(2000) 7–25 · Terras, *Zeta Functions of Graphs* (2011) · Lubotzky–Phillips–Sarnak,
*Combinatorica* 8 (1988) · Nilli, *Discrete Math.* 91 (1991) (Alon–Boppana) · Friedman,
*Mem. AMS* 195 (2008) · Bordenave, *Ann. Sci. ÉNS* 53 (2020) 1393–1439 · Bilu–Linial,
*Combinatorica* 26 (2006) · Marcus–Spielman–Srivastava, *Ann. of Math.* 182 (2015) 307–325 ·
Anantharaman–Le Masson, *Duke Math. J.* 164 (2015) 723–765 · Mizuno–Sato, *Linear Algebra
Appl.* 377 (2004) 193–206 · Montgomery, "Zeros of approximations to the zeta function", in
*Studies in Pure Mathematics — To the Memory of Paul Turán* (1983) 497–506 · Turán, *Danske
Vid. Selsk. Mat.-Fys. Medd.* 24 (1948) · Gonek–Hughes–Keating, *Duke Math. J.* 136 (2007)
507–549 · Montgomery, "The analytic principle of the large sieve", *Bull. AMS* 84 (1978) ·
Lee–Yang, *Phys. Rev.* 87 (1952) 410–419 · Asano, *J. Phys. Soc. Japan* 29 (1970) 350–359 ·
Borcea–Brändén, *Invent. Math.* 177 (2009) 541–569 · Kottos–Smilansky, *Ann. Phys.* 274 (1999)
76–124 · Gnutzmann–Smilansky, *Adv. Phys.* 55 (2006) 527–625 · Berry–Keating, *SIAM Rev.* 41
(1999) 236–266 · Connes, *Selecta Math.* 5 (1999) 29–106 · Connes–Consani, *Selecta Math.* 27
(2021) · Connes–Moscovici, *PNAS* 119 (2022) e2123174119 (prolate wave operator) · Meyer,
*Duke Math. J.* 127 (2005) 519–595 · Reed–Simon I, §VIII.7 · Simon, *Trace Ideals and Their
Applications* (2005), Thm 3.4 · de la Vallée Poussin (1899) · Vinogradov (1958); Korobov (1958)
· Gubser–Knapik et al., *Commun. Math. Phys.* 352 (2017) (p-adic AdS/CFT, decorative analogy
only).
