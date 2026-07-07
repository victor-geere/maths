# PSC2-F03 — WP06: the weighted Ihara–Bass identity is proven (G1 audit closed); the honest weighted locus is derived, verified, and is weak

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP06](../workpackages/PSC2-WP06-weighted-locus.md). Code/runs:
`numerics/wp06_bass_certify.py` (exact rational arithmetic + sympy symbolic; `mpmath` dps 40
for the convention-tie only; deterministic) and `numerics/wp06_locus_check.py` (numpy float64;
deterministic — no random draws enter any result). Independent symbolic cross-checks via the
`sympy-verifier` MCP server (list in §A3). Tags per [PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> - a weak locus (fat annulus) still unblocks WP08 — record it even if unimpressive;
> - the measured pole census (parent snapshot: 208 real poles at $n = 7$, $|u| \in [0.19, 4.18]$)
>   is the reality check: the derived locus must contain the measured poles with no fitted
>   constants.
>
> **Deliverable.** A `W-theorem` finding note: identity **proven** (Part A) + locus proposition
> with explicit radii/regions (Part B), symbolically verified at small $n$.
>
> **Falsifier.** None needed for Part A (the $10^{-15}$ agreement makes identity failure
> implausible); Part B's risk is weakness, not falsity. If the locus cannot separate structural
> from arithmetic detachment even in principle, WP08's theorem target is re-scoped to the
> measured census.

## Regression check

N00 targets reproduced: **yes** — §3 graph-lab anchors rebuilt through
`prime_graph_lab.py`'s own builders (rule I0.5): $\mu_1(B) = 3.5419, 5.2810, 7.6871, 10.9663$
at $n = 6, 7, 8, 9$; detached census $4$ (of which $2$ real) at every one of those stages —
all match N00 §3 verbatim. The exact edge lists used in the certification reproduce
`build_bipartite`'s weight matrices exactly (max deviation $0.0$), so the certified graphs
are the F2-verified graphs. The WP's quoted census (208 real poles at $n=7$,
$|u| \in [0.19, 4.18]$) is reproduced to the stated digits (§B, verbatim output). No
$\gamma$-list, no zero data, and no fitted constant appears anywhere in this WP.

---

## Part A — Theorem 1.1 audit closed: the identity is proven

**Theorem A (weighted Ihara–Bass resolvent identity; multigraph form).** Let $G = (V, E)$ be a
finite undirected **loopless multigraph** with edge weights $w_e > 0$, and let $B_w$ act on the
$2|E|$ oriented edges by $(B_w)_{ef} = \sqrt{w_e w_f}$ when $f$ follows $e$ without
backtracking ($h(e) = t(f)$, $f \ne \bar e$), else $0$. Then for all $u \in \mathbb C$,

$$\det(I - u B_w) \;=\; \prod_{e \in E}\big(1 - u^2 w_e^2\big)\;\det M(u),$$

$$M(u)_{xx} = 1 + u^2\!\!\sum_{e:\,x \in e}\frac{w_{e}^2}{1 - u^2 w_{e}^2},\qquad
M(u)_{xy} = -\,u\!\!\sum_{e = \{x,y\}}\frac{w_{e}}{1 - u^2 w_{e}^2}\quad (x \ne y),$$

the sums running over incident/parallel edges (for a simple graph this is exactly
[S05](../sources/PSC2-S05-salvaged-G1.md) Theorem 1.1).

**Proof (explicit block-triangular factorisation — discharges S05 obligation 1).** Write
$\vec E$ for the oriented edges ($|\vec E| = 2|E|$), $\tau$ for the reversal permutation matrix
($\tau^2 = I$; fixed-point free because $G$ is loopless), $W = \mathrm{diag}(w_e)$ on $\vec E$
(so $\tau W = W\tau$, $(W\tau)^\top = W\tau$, $(W\tau)^2 = W^2$), and define
$S, T \in \mathbb{R}^{V \times \vec E}$ by
$S_{v,e} = \sqrt{w_e}\,\delta_{v, h(e)}$, $T_{v,e} = \sqrt{w_e}\,\delta_{v, t(e)}$. Three
entrywise checks:

- **(A1)** $B_w = S^\top T - W\tau$: indeed $(S^\top T)_{ef} = \sqrt{w_ew_f}\,\delta_{h(e),t(f)}$,
  and the backtracking term $f = \bar e$ carries $\sqrt{w_e w_{\bar e}} = w_e = (W\tau)_{e\bar e}$.
- **(A2)** $J(u) := I + uW\tau$ is block-diagonal over the pairs $\{e, \bar e\}$ with blocks
  $\begin{pmatrix}1 & uw_e\\ uw_e & 1\end{pmatrix}$, so $\det J(u) = \prod_{e\in E}(1 - u^2w_e^2)$
  and, when no $u^2w_e^2 = 1$, $J(u)^{-1} = (I - u^2W^2)^{-1}(I - uW\tau)$.
- **(A3)** $I_V - u\,S\,J(u)^{-1}T^\top = M(u)$: expanding with (A2),
  $S(I-u^2W^2)^{-1}T^\top$ has entries $\sum_{e: h(e)=x,\,t(e)=y} w_e/(1-u^2w_e^2)$ (the
  off-diagonal part of $-M/u$, plus loop terms which are absent), while
  $S(I-u^2W^2)^{-1}W\tau\,T^\top$ is **diagonal** with entries
  $\sum_{e: h(e)=x} w_e^2/(1-u^2w_e^2)$ (using $t(\bar e) = h(e)$) — the diagonal part of $M$.

Now factor the $(|V| + 2|E|) \times (|V| + 2|E|)$ matrix
$X(u) = \begin{pmatrix} I_V & uS \\ T^\top & J(u)\end{pmatrix}$ two ways:

$$X(u) = \begin{pmatrix} I_V & 0 \\ T^\top & I\end{pmatrix}
\begin{pmatrix} I_V & uS \\ 0 & I - uB_w^\top\end{pmatrix}
\qquad\text{(by (A1): } J - uT^\top S = I + uW\tau - u(B_w^\top + W\tau)\text{)},$$

$$X(u) = \begin{pmatrix} I_V & uSJ(u)^{-1} \\ 0 & I\end{pmatrix}
\begin{pmatrix} M(u) & 0 \\ T^\top & J(u)\end{pmatrix}
\qquad\text{(by (A3); valid where } J(u) \text{ is invertible)}.$$

Taking determinants: $\det(I - uB_w) = \det(I - uB_w^\top) = \det X(u) =
\prod_e(1-u^2w_e^2)\det M(u)$ for every $u$ outside the finite set $\{u : u^2w_e^2 = 1\}$;
the left side is a polynomial and the right side a rational function, so the identity extends
to all of $\mathbb{C}$ and the right side's apparent singularities are removable.
$\blacksquare$

The kernel-level "Schur complement" step of S05 §2 is thereby replaced by an explicit
factorisation in which every block, every dimension ($|V| + 2|E|$ throughout), and the
determinant multiplicativity are exhibited — obligation 1 discharged in strengthened form.

### A2 — degenerate cases (S05 obligation 2)

- **Degree-1 and degree-0 vertices.** No degree hypothesis appears anywhere in the proof.
  Every stage graph contains degree-1 vertices (prime-power composites *and* large primes
  incident to a single composite — 9 such vertices at $n=6$); they are certified along with
  everything else in §A3, and Part B's Proposition B1 makes their role exact.
- **Multi-edges.** The proof indexes by oriented edges, never by endpoint pairs; the
  multigraph form of $M$ above is the correct statement. Certified symbolically on the double
  edge, where the identity closes as
  $(1-u^2a^2)(1-u^2b^2)\det M(u) = (1-u^2ab)^2$ (check D3).
- **Loops** are excluded: $\tau$ must be fixed-point free. (The sieve graphs are bipartite,
  hence loopless.)
- **Singular $u$ ($u^2w_e^2 = 1$)** is handled by polynomial continuation, as in the proof;
  the exact certification never samples there (pole avoidance is proved in the script: an
  integer sample $v$ equals some $p/k^2$ only if $k = 1$, and those $v = p$ are skipped).
- **$u = 0$**: both sides are $1$. **Disconnected graphs**: all objects are direct sums,
  both sides multiply over components.

### A3 — symbolic certification at $n \le 6$ on the actual stage graphs (S05 obligation 3)

The certification is **exact over $\mathbb{Q}$** — no floating point in the certificate. Three
one-line lemmas rationalise the bipartite stage identity (weights $w_{pm} = k_m(p)\,p^{-1/2}$,
$k_m(p) = v_p(m)$):

- **(L1)** $\mathrm{diag}(\sqrt{w_e})$ conjugates the lab convention $B'$ (entries $w_f$) to
  $B_w$ — same determinant;
- **(L2)** direction grading ($p{\to}m$ states vs $m{\to}p$ states) makes $B'$ block
  anti-diagonal, so $\det(I - uB') = \det(I - u^2 C)$ with
  $C_{(p\to m),(p'\to m')} = [\,\{p',m\} \in E\,][p' \ne p][m' \ne m]\;k_m(p')k_{m'}(p')/p'$
  — **rational** (every closed non-backtracking walk pairs the two $p^{-1/2}$ factors at each
  prime visit);
- **(L3)** conjugating $M(u)$ by $\mathrm{diag}(u\sqrt p \text{ on primes},\,1 \text{ on
  composites})$ gives $\tilde M(v)$, $v = u^2$, with rational entries
  $\tilde M_{xx} = 1 + \sum_e vk^2/(p - vk^2)$, $\tilde M_{pm} = -vkp/(p-vk^2)$,
  $\tilde M_{mp} = -k/(p-vk^2)$ — same determinant.

The identity is then the polynomial identity $F_1 = F_2$ over $\mathbb Q$, where
$F_1(v) = \det(I - vC)\cdot\prod_e(p_e - vk_e^2)$ (computed exactly: characteristic polynomial
of $C$ over $\mathbb Q$) and $F_2(v) = \prod_e(1 - vw_e^2)\det\tilde M(v)\cdot\prod_e(p_e - vk_e^2)$
(computed exactly at $2|E|+1$ integer sample points by fraction-free Bareiss determinants,
then interpolated exactly). Both degrees are $\le 2|E|$ by proof, so agreement at $2|E|+1$
points **is** coefficient-by-coefficient equality; the script compares the two exact
coefficient vectors entry by entry. Result: **equality at every one of the
$7, 21, 41, 101, 219$ coefficients at $n = 2, 3, 4, 5, 6$** (verbatim output below). Since the
certified weights are the exact stage weights, this proves the five stage identities outright,
independently of Theorem A. A dps-40 `mpmath` run ties the certified polynomial back to the
original $\sqrt{\phantom{w}}$-convention matrices (max relative deviation
$1.9\times10^{-40}$), and the full $\sqrt{\phantom{w}}$-convention
identity is verified *symbolically* (sympy, exact surds) on the actual $n = 2$ stage graph
(check D6).

Independent cross-checks through the **sympy-verifier MCP server** (all returned
`equal: true` / `is_zero: true`):
1. the per-edge algebra $g^2 = h(1+h)$ for $g = uw/(1-u^2w^2)$, $h = u^2w^2/(1-u^2w^2)$;
2. the partial-fraction identity $hs - gc = \frac{s-c}{2}\frac{1}{1-uw} +
   \frac{s+c}{2}\frac{1}{1+uw} - s$ (the load-bearing step of Part B);
3. the leaf-cancellation $h - g^2(1-u^2w^2) = 0$ (the load-bearing step of Prop. B1);
4. the full $P_3$ identity $\prod_e(1-u^2w_e^2)\det M(u) = 1$ (tree with a leaf).

### A4 — literature cross-check (S05 obligation 4)

Watanabe–Fukumizu, *Loopy Belief Propagation, Bethe Free Energy and Graph Zeta Function*
(arXiv:1103.0605; the journal form of their NeurIPS 2009 paper), **Corollary 9**: for scalar
weights $u_e$ **independent per orientation**,
$Z_G(u)^{-1} = \det(I + \hat D(u) - \hat A(u))\prod_{[e]}(1 - u_eu_{\bar e})$ with
$\hat D_{ii} = \sum_{e: t(e)=i}\frac{u_eu_{\bar e}}{1-u_eu_{\bar e}}$ and
$\hat A_{i,o(e)} \ni \frac{u_e}{1-u_eu_{\bar e}}$. Our Theorem A is **exactly the
specialisation** $u_e = u_{\bar e} = u\,w_e$ (then $\hat D$, $\hat A$ become the diagonal and
off-diagonal parts of $M(u)$ and the edge factors become $1 - u^2w_e^2$). The general
independent-orientation form was verified symbolically on the triangle with six free scalars
(check D5), so the cross-check does not rest on quoting the paper. The same paper states that
Mizuno–Sato 2004 (and Horton et al. 2008) treat the regime $u_eu_{\bar e} = u^2$
*independent of the edge* — which explains, rather than contradicts, the banked numeric
refutation of the "naive weighted Bass" transplant for our edge-dependent weighting
(max error $\approx 10^{-1}$ vs $10^{-15}$ for the resolvent form; N00 §3).

**Part A verdict: all four S05 §3 obligations discharged. Theorem 1.1 is tagged *proven*.**
A dated correction notice is appended to S05 per convention.

---

## Part B — the honest confinement locus

Throughout, $G$ is loopless with positive weights; "core" means the 2-core $G_2$ (iterated
deletion of degree-$\le 1$ vertices), and $d_x$, $w_{xy}$ are core degrees and weights.

**Proposition B1 (leaf reduction — the honest degree-1 treatment).** Let $x$ have degree 1,
with edge $e_0 = \{x, y\}$, weight $w_0$. Then $M_G(u)_{xx} = \frac{1}{1-u^2w_0^2} \ne 0$, and
Schur elimination of row/column $x$ yields **exactly** $M_{G-x}(u)$: the $(y,y)$ correction
$-M_{yx}M_{xy}/M_{xx} = -(1-u^2w_0^2)\,g_0^2 = -h_0$ cancels edge $e_0$'s diagonal
contribution $h_0$ (MCP check 3), and no other entry involves $e_0$. Hence

$$\det M_G(u) = \frac{\det M_{G-x}(u)}{1 - u^2w_0^2},\qquad
\det(I - uB_G) = \det(I - uB_{G-x}),$$

and by iteration $\det(I - uB_G) = \det(I - uB_{G_2})$ ($= 1$ if $G$ is a forest). In
particular **the non-real zeros of $\det(I - uB_G)$ are exactly the non-real zeros of
$\det M_{G_2}(u)$** (the trivial factors and the poles of $\det M$ are all real). *Proven*;
verified numerically at $n = 4\ldots9$ (nonzero spectra of $B$ and $B_{\mathrm{core}}$ agree
to $\le 4\times10^{-14}$ relative, with 7–64 vertices pruned per stage).

**Proposition B2 (balance identities).** Let $u \notin \mathbb R$ with
$\det M_{G_2}(u) = 0$ and let $\varphi$ be a unit kernel vector. Put, per core edge
$e = \{x,y\}$: $s_e = |\varphi_x|^2 + |\varphi_y|^2$,
$c_e = 2\,\mathrm{Re}(\overline{\varphi_x}\varphi_y)$,
$\alpha_e = \tfrac{s_e - c_e}{2} \ge 0$, $\beta_e = \tfrac{s_e + c_e}{2} \ge 0$
(so $\alpha_e + \beta_e = s_e$, $\sum_e s_e = \bar d := \sum_x d_x|\varphi_x|^2$). Expanding
$\langle\varphi, M(u)\varphi\rangle = 0$ per edge and applying the partial fractions
(MCP check 2) — each diagonal term is a Möbius function of $v = u^2$, split into its two
Herglotz-conjugate parts $\frac{1}{1 \mp uw_e}$ — gives

$$\sum_e\Big[\frac{\alpha_e}{1 - uw_e} + \frac{\beta_e}{1 + uw_e}\Big] = \bar d - 1.$$

Taking the imaginary part (divide by $\mathrm{Im}\,u \neq 0$) and then the real part:

$$(\dagger)\ \ \sum_e \frac{\alpha_e w_e}{|1-uw_e|^2} = \sum_e \frac{\beta_e w_e}{|1+uw_e|^2},
\qquad
(\mathrm R)\ \ \sum_e\Big[\frac{\alpha_e}{|1-uw_e|^2} + \frac{\beta_e}{|1+uw_e|^2}\Big]
= \bar d - 1.$$

*Proven.* (The cross-term of the real part cancels exactly by $(\dagger)$.)

**Theorem B3 (the weighted annulus).** Every non-real zero $u$ of $\det(I - uB_G)$ satisfies,
with $r = |u|$ and all quantities on the 2-core:

$$\exists\,x:\ \sum_{y\sim x}\frac{1}{(1 - rw_{xy})^2} \ge d_x - 1
\qquad\text{and}\qquad
\exists\,x':\ \sum_{y\sim x'}\frac{1}{(1 + rw_{x'y})^2} \le d_{x'} - 1,$$

(where $(1-rw)^2$ means $(rw-1)^2$ when $rw > 1$). Consequently $r_1 \le |u| \le r_2$ with

$$r_1 = \min_x\,\mathrm{root}\Big[\textstyle\sum_{y\sim x}(1+rw_{xy})^{-2} = d_x - 1\Big],
\qquad
r_2 = \max_x\,\mathrm{root}_{\,r > 1/\min_{y}w_{xy}}\Big[\textstyle\sum_{y\sim x}(1-rw_{xy})^{-2} = d_x - 1\Big],$$

both roots unique on monotone tails (each $d_x \ge 2$ on the core makes $r_1 > 0$ and
$r_2 < \infty$). **No fitted constants: both radii are functions of the weight distribution
alone.** *Proof:* $|1 \mp uw| \ge |1 - rw|$ and $\le 1 + rw$ bound the kernels of
$(\mathrm R)$ on both sides; then
$\sum_e s_e f(w_e) = \sum_x |\varphi_x|^2 \sum_{y \sim x} f(w_{xy})$ and
$\bar d - 1 = \sum_x |\varphi_x|^2 (d_x - 1)$ turn the two inequalities into nonnegative
vertex averages, each forcing one vertex to satisfy its condition. $\blacksquare$
*Specialisation check:* for an unweighted $(q+1)$-regular graph,
$r_1 = \sqrt{\tfrac{q+1}{q}} - 1$ and $r_2 = 1 + \sqrt{\tfrac{q+1}{q}}$, containing the
Kotani–Sunada locus $|u| = q^{-1/2}$; the Petersen control reproduces these radii to
$10^{-9}$ and its non-real poles sit exactly on $|u| = 2^{-1/2}$, inside.
($(\dagger)$ is not consumed by the radial bounds — it is banked as the sharpening lever.)

**Proposition B4 (inner bound for all poles; sharp).** Every zero of $\det(I - uB_G)$ has
$|u| \ge 1/\rho(B_w)$, with $\rho(B_w) = \rho(B_{G_2}) \le \max_e \sum_{f: e\to f}\sqrt{w_ew_f}$
(Gershgorin — no degree hypothesis), and by Perron–Frobenius ($B_w \ge 0$) the bound is
**attained by a real pole** at $u = 1/\rho$. *Proven; verified at every stage (Perron equality
to $10^{-6}$).*

**Proposition B5 (real poles, first-power bound).** A real zero with
$|u| < 1/\max_{e \in G_2} w_e$ satisfies
$\exists x: \sum_{y\sim x}(1 + |u|w_{xy})^{-1} \le d_x - 1$, hence $|u| \ge r_1^{\mathbb R}$
(same construction at the first power; $r_1^{\mathbb R} \ge r_1$). *Proven* — for real $u$
the kernel vector is real and $\frac{1}{1 \mp uw} \ge \frac{1}{1 + |u|w}$ termwise on the
stated disk. *Verified at every stage.*

**Definition B6 (intrinsic detachment — what F4/WP08 needed defined).** Relative to the locus:
the **bulk** is the non-real spectrum (provably confined to $[r_1, r_2]$); the **structural
real poles** are the Perron pole $1/\rho$ and its bipartite mirror; a **locus-detached
(graph-Siegel candidate) pole** is a real pole with $|u| < r_1$ — a real pole provably closer
to Perron than any bulk pole can be. "No graph-Siegel zeros" (F4) is then the well-defined
statement: *no real poles other than the Perron pair below the bulk's inner radius*.

### Measured outcome — the pre-registered weakness branch occurred

All containments hold at every stage $n = 4\ldots9$ and the census is reproduced exactly
(208 real poles at $n=7$, $|u| \in [0.1894, 4.1815]$, minimum $=$ the Perron pole $1/\rho$ as
Proposition B4 predicts). But the annulus is **fat**: at $n = 7$,
$[r_1, r_2] = [0.0064, 21.99]$ against measured non-real poles in $[0.2054, 3.86]$, and $r_1$
collapses with $n$ (the $\min_x$ in Theorem B3 is pinned by the highest-degree vertex, $p = 2$,
whose degree grows like the count of even composites). Consequently **locus-detached count
$= 0$ at every stage — even the Perron pole sits above $r_1$** — so this locus cannot separate
structural from arithmetic detachment, and per the pre-registered falsifier **WP08's theorem
target is re-scoped to the measured census**. Two honest addenda, recorded for any future
sharpening: (i) the separation *exists empirically* — at $n=7$ the real Perron pair sits at
$|u| = 0.1894$, the nearest non-real pair at $0.2054$, an $8\%$ gap; a vertex-uniform
(eigenvector-blind) bound of the B3 type cannot see it, but the unconsumed balance identity
$(\dagger)$ and eigenvector-sensitive weighting are available levers. (ii) The detached
non-real pair sits at $|u| = 0.2054$, far **outside** the Ramanujan-type circle
$1/\sqrt{\mu_1} = 0.435$ — the weighted bulk genuinely extends beyond the $\sqrt{\mu_1}$
benchmark, so the measured census criterion ($|\mu| > 1.02\sqrt{\mu_1}$) is a bulk-edge
estimate, not a proven bulk boundary.

---

## Result

`wp06_bass_certify.py` (exact certification; verbatim):

```
== WP06 Part A: exact certification of the weighted Ihara–Bass resolvent identity ==
[D1] P3 tree (leaf degeneracy): RHS == 1: True;  det(I-uB) == 1: True
[D2] leaf reduction det M_G = det M_(G-x) / (1-u^2 w^2): True
[D3] multigraph (double edge), multigraph form of M: True
[D4] g^2 = h(1+h): True;  partial fractions h s - g c: True
[D5] Watanabe–Fukumizu Cor. 9, independent orientation weights, triangle: True
[D6] full sqrt-convention identity on the actual n=2 stage graph: True
[n=2] |P|=2 |C|=2 |E|=3 degree-1 vertices=2 (obligation-2 witnesses present: True) float-tie max|dW|=0.0e+00
       deg L = 3 (<= |E|=3);  F1 == F2: True (7 coefficients compared exactly over Q; 7 sample points)   [0.0s]
[n=2] dps-40 full chain (B' det | S05 sqrt-form RHS | exact L(u^2)): max rel err = 2.3e-41
[n=3] |P|=4 |C|=6 |E|=10 degree-1 vertices=3 (obligation-2 witnesses present: True) float-tie max|dW|=0.0e+00
       deg L = 10 (<= |E|=10);  F1 == F2: True (21 coefficients compared exactly over Q; 21 sample points)   [0.0s]
[n=3] dps-40 full chain (B' det | S05 sqrt-form RHS | exact L(u^2)): max rel err = 6.89e-41
[n=4] |P|=6 |C|=11 |E|=20 degree-1 vertices=5 (obligation-2 witnesses present: True) float-tie max|dW|=0.0e+00
       deg L = 20 (<= |E|=20);  F1 == F2: True (41 coefficients compared exactly over Q; 41 sample points)   [0.0s]
[n=4] dps-40 full chain (B' det | S05 sqrt-form RHS | exact L(u^2)): max rel err = 1.61e-40
[n=5] |P|=11 |C|=25 |E|=50 degree-1 vertices=5 (obligation-2 witnesses present: True) float-tie max|dW|=0.0e+00
       deg L = 50 (<= |E|=50);  F1 == F2: True (101 coefficients compared exactly over Q; 101 sample points)   [1.3s]
[n=5] dps-40 full chain (B' det | S05 sqrt-form RHS | exact L(u^2)): max rel err = 1.84e-40
[n=6] |P|=18 |C|=51 |E|=109 degree-1 vertices=9 (obligation-2 witnesses present: True) float-tie max|dW|=0.0e+00
       deg L = 109 (<= |E|=109);  F1 == F2: True (219 coefficients compared exactly over Q; 219 sample points)   [75.4s]

CERTIFICATION PASS: identity certified coefficient-by-coefficient over Q on all stage graphs n = 2..6, degenerate cases and the Watanabe–Fukumizu general form verified symbolically.
```

`wp06_locus_check.py` (locus verification; verbatim):

```
== WP06 Part B: honest weighted locus — 2-core radii, containment, census ==
[petersen] non-real poles all on |u| = 1/sqrt(2): True;  annulus [0.2247, 2.2247] (expected [0.2247, 2.2247])  contains them: True;  inner(all)=True
[n=4] |V|=17 -> core 10 (pruned 7)  leaf-reduction spectra match: True (worst rel dev 6.04e-15)
       mu1=1.3602  1/rho=0.7352  r1=0.0954  r2=6.3874  r1R=0.2035  1/wmax_core=0.4714
       poles: 10 real, |u| in [0.7352, 1.6849];  16 non-real, |u| in [0.8439, 1.6150]
       checks: inner(all)=True  perron-eq=True  annulus(non-real)=True  real-disk=True
       detached census (sqrt(mu1)*1.02): 2 (2 real)   locus-detached (real, |u| < r1): 0
[n=5] |V|=36 -> core 28 (pruned 8)  leaf-reduction spectra match: True (worst rel dev 6.04e-15)
       mu1=2.3173  1/rho=0.4315  r1=0.0333  r2=10.5233  r1R=0.0685  1/wmax_core=0.3536
       poles: 32 real, |u| in [0.4315, 2.5874];  52 non-real, |u| in [0.4841, 2.5859]
       checks: inner(all)=True  perron-eq=True  annulus(non-real)=True  real-disk=True
       detached census (sqrt(mu1)*1.02): 4 (2 real)   locus-detached (real, |u| < r1): 0
[n=6] |V|=69 -> core 55 (pruned 14)  leaf-reduction spectra match: True (worst rel dev 1.18e-14)
       mu1=3.5419  1/rho=0.2823  r1=0.0141  r2=15.4585  r1R=0.0286  1/wmax_core=0.2828
       poles: 84 real, |u| in [0.2823, 3.2457];  106 non-real, |u| in [0.3032, 3.1440]
       checks: inner(all)=True  perron-eq=True  annulus(non-real)=True  real-disk=True
       detached census (sqrt(mu1)*1.02): 4 (2 real)   locus-detached (real, |u| < r1): 0
       N00 §3 regression (mu1=3.5419, detached 4/2): ok
[n=7] |V|=136 -> core 117 (pruned 19)  leaf-reduction spectra match: True (worst rel dev 1.74e-14)
       mu1=5.2810  1/rho=0.1894  r1=0.0064  r2=21.9945  r1R=0.0129  1/wmax_core=0.2357
       poles: 208 real, |u| in [0.1894, 4.1815];  230 non-real, |u| in [0.2054, 3.8590]
       checks: inner(all)=True  perron-eq=True  annulus(non-real)=True  real-disk=True
       detached census (sqrt(mu1)*1.02): 4 (2 real)   locus-detached (real, |u| < r1): 0
       N00 §3 regression (mu1=5.281, detached 4/2): ok
[n=8] |V|=267 -> core 233 (pruned 34)  leaf-reduction spectra match: True (worst rel dev 4.01e-14)
       mu1=7.6871  1/rho=0.1301  r1=0.0031  r2=31.1985  r1R=0.0062  1/wmax_core=0.2020
       poles: 480 real, |u| in [0.1301, 5.5737];  462 non-real, |u| in [0.1398, 4.5801]
       checks: inner(all)=True  perron-eq=True  annulus(non-real)=True  real-disk=True
       detached census (sqrt(mu1)*1.02): 4 (2 real)   locus-detached (real, |u| < r1): 0
       N00 §3 regression (mu1=7.6871, detached 4/2): ok
[n=9] |V|=534 -> core 470 (pruned 64)  leaf-reduction spectra match: True (worst rel dev 3.78e-14)
       mu1=10.9663  1/rho=0.0912  r1=0.0015  r2=44.3191  r1R=0.0030  1/wmax_core=0.1768
       poles: 1082 real, |u| in [0.0912, 7.3329];  936 non-real, |u| in [0.0978, 5.5480]
       checks: inner(all)=True  perron-eq=True  annulus(non-real)=True  real-disk=True
       detached census (sqrt(mu1)*1.02): 4 (2 real)   locus-detached (real, |u| < r1): 0
       N00 §3 regression (mu1=10.9663, detached 4/2): ok

[census n=7] 208 real poles, |u| in [0.19, 4.18]  (pre-registered: 208, [0.19, 4.18]): reproduced
[teeth] planted outer-violation flagged: True;  planted inner-violation flagged: True

LOCUS VERIFICATION PASS (all containments hold; controls two-sided; census reproduced)
```

The numbers say: the identity is no longer merely $10^{-15}$-verified — it is proven by
explicit factorisation and certified **exactly**, coefficient by coefficient over $\mathbb Q$,
on every stage graph up to $n = 6$, including all degenerate configurations that broke the
quarantined proof. The locus theorems hold with nothing fitted: every pole respects the Perron
inner bound with equality at the Perron pole, every non-real pole lies in the derived annulus,
the checker demonstrably catches planted violations, and the positive control (Petersen)
reproduces the classical radii exactly. The locus is honest but weak — the fat-annulus branch
the WP pre-registered — and it cannot isolate the Perron pair from the bulk, so detachment
remains an empirical (census) notion for WP08.

## Verdict against the pre-registered criteria

**Part A: pass** — deliverable achieved at the "identity **proven**" level; audit closed.
**Part B: pass, in the pre-registered weakness branch** — locus proposition with explicit,
fitted-constant-free radii delivered and verified (weak annulus recorded "even if
unimpressive", per the WP); census containment holds; the locus cannot separate structural
from arithmetic detachment, so per the WP falsifier **WP08's theorem target is re-scoped to
the measured census** (its β-sweep ordering is unaffected).

## Tag

- Theorem A (weighted Ihara–Bass, multigraph form) and its stage instances at $n \le 6$:
  **proven** (explicit factorisation above; exact rational certification; independent
  sympy-verifier checks; Watanabe–Fukumizu cross-check). S05's Theorem 1.1 tag upgrades to
  **proven** (dated notice appended there).
- Propositions B1–B5 and Theorem B3 (leaf reduction, balance identities, annulus, Perron
  inner bound, real-disk bound): **proven**; their numerical instantiations at $n = 4\ldots9$:
  **verified** against pre-registered two-sided controls.
- Definition B6 gives F4/WP08 a well-defined "graph-Siegel" notion; the finding that this
  locus does not separate (locus-detached $= 0$ everywhere): **verified**.
- The empirical separation gap ($0.1894$ vs $0.2054$ at $n=7$) and the $(\dagger)$-based
  sharpening idea: **exploratory**.

**Scope (do-not list compliance).** Everything here concerns the finite weighted divisor
graphs' non-backtracking spectra. The correct-locus rule (I0.3) is respected — the weighted
annulus replaces $|u| = q^{-1/2}$, never $|u| = 1$. Nothing in this note is a statement about
$\zeta$'s zeros; no $\gamma$-data was consumed; RH remains **open**.

## Propagation

Charter ledger updated: **yes** (Weighted Ihara–Bass row → **proven**; T6/WP06 → done; WP08
re-scope note; WP13 unblocked). Source doc correction notice needed: **yes** — appended to
S05 (audit closed, tag upgraded, dated); parent snapshot ledger row updated per README
convention. WP06 status → done. WP08 dated note added (locus exists; census re-scope per this
finding). WP13 gating satisfied (identity proven; per-edge product form now safe to build on).
