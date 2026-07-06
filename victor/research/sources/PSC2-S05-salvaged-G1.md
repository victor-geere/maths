# PSC2-S05 — salvaged G1: the weighted Ihara–Bass resolvent identity

*Source document S05. Salvaged from the quarantined `prime-sieve-continued/flawed/gate-1.md`
(charter dead-end ledger item X10). That document contained three claims; **only the first is
salvaged here.** Status per claim:*

| Claim in gate-1.md | Verdict | Disposition |
|---|---|---|
| Theorem 2.1 (weighted Ihara–Bass resolvent identity) with Schur-complement proof | proof **plausibly correct**; numeric half independently verified to $10^{-15}$ (F2) | **salvaged below**; verification obligations in §3; tag stays *verified numerically / proof under audit* until WP06's audit completes |
| "Weighted Locus Theorem" (annulus $r_1 \le \lvert u\rvert \le r_2$ for non-real zeros) | upper-bound derivation incoherent mid-proof (mislabeled degree quantities, patched estimates); hypothesis "weighted degree $\ge 2$" fails for the actual sieve graph (prime-power composites have degree 1) | **not salvaged** — re-derive honestly in [WP06](../workpackages/PSC2-WP06-weighted-locus.md) |
| "Asano Compatibility" theorem | circular: invokes the locus conclusion for the enlarged graph, then concludes stability from an annulus that *grows* — a non sequitur; no actual Lee–Yang/Asano contraction argument | **not salvaged** — the honest question is [WP13](../workpackages/PSC2-WP13-asano-gluing.md) (Q-γ2) |

---

## 1. Statement

**Theorem 1.1 (weighted Ihara–Bass resolvent identity).** For any finite undirected graph
$G = (V, E)$ with positive edge weights $\{w_e\}_{e \in E}$ and weighted non-backtracking
(Hashimoto) matrix $B_w$ (entries $\sqrt{w_e w_f}$ on allowed transitions $e \to f$),

$$\det(I - u B_w) \;=\; \prod_{e \in E}\big(1 - u^2 w_e^2\big)\;\det M(u),$$

where $M(u)$ is the $|V| \times |V|$ vertex matrix

$$M(u)_{xx} = 1 + u^2\sum_{y \sim x}\frac{w_{xy}^2}{1 - u^2 w_{xy}^2},\qquad
M(u)_{xy} = -\,\frac{u\,w_{xy}}{1 - u^2 w_{xy}^2}\quad (x \ne y,\ x \sim y).$$

*Provenance of the numeric half (F2, run 5 Jul 2026):* validated to $\max$ residual
$5.4 \times 10^{-16}$ on a random symmetric-weighted graph ($v = 8$) and
$1.7 \times 10^{-15}$ on the actual stage-5 bipartite divisor graph ($v = 36$); the naive
weighted Bass form was simultaneously refuted at $10^{-1}$. Classical relatives:
Watanabe–Fukumizu 2009; Coste–Zhu 2021; Mizuno–Sato 2004.

## 2. Proof (salvaged; under audit per §3)

Orient each undirected edge both ways; write $\vec E$ for the $2|E|$ oriented edges, $\bar e$
for the reverse of $e$, $w_e = w_{\bar e} = w_{xy}$. The operator acts by

$$(B_w\psi)(x \to y) = \sum_{\substack{z:\ y \to z\\ z \ne x}}\sqrt{w_{xy}w_{yz}}\;\psi(y \to z),$$

so the kernel equation $(I - uB_w)\psi = 0$ reads componentwise

$$\psi(x \to y) = u\sqrt{w_{xy}}\sum_{\substack{z:\ y \to z\\ z \ne x}}\sqrt{w_{yz}}\,\psi(y \to z). \tag{1}$$

Introduce the outgoing wave $\phi_v = \sum_{z:\ v \to z}\sqrt{w_{vz}}\,\psi(v \to z)$. For a
fixed undirected edge $\{x, y\}$ with weight $w$, the two instances of (1) become

$$\psi(x \to y) = u\sqrt{w}\big(\phi_y - \sqrt{w}\,\psi(y \to x)\big),\qquad
\psi(y \to x) = u\sqrt{w}\big(\phi_x - \sqrt{w}\,\psi(x \to y)\big),$$

a $2 \times 2$ system with block matrix $\begin{pmatrix}1 & uw\\ uw & 1\end{pmatrix}$,
determinant $1 - u^2w^2$. Inverting,

$$\psi(x \to y) = \frac{u\sqrt{w}}{1 - u^2w^2}\big(\phi_y - uw\,\phi_x\big). \tag{2}$$

Substituting (2) into the definition of $\phi_x$ and collecting terms:

$$\phi_x\Big(1 + u^2\sum_{y}\frac{w_{xy}^2}{1 - u^2w_{xy}^2}\Big)
- u\sum_{y}\frac{w_{xy}}{1 - u^2w_{xy}^2}\,\phi_y = 0,$$

which is exactly $M(u)\,\phi = 0$. The change of variables from the edge vector $\psi$ to
(per-edge internal pairs, $\phi$) is block-triangular: each undirected edge's two internal
variables are eliminated through its $2 \times 2$ block of determinant $1 - u^2w_e^2$, and the
Schur complement of those blocks is the map $M(u)$ on $\phi$. Taking determinants,

$$\det(I - uB_w) = \prod_{e \in E}(1 - u^2w_e^2)\,\det M(u). \qquad\blacksquare$$

## 3. Verification obligations (open; owned by WP06)

The proof is short and its mechanism (edge-pair Schur complement) is standard, but it arrived
inside a document whose other two proofs failed audit — so it does not inherit "proven" by
association. Before the tag upgrades to **proven**:

1. **Dimension bookkeeping.** Make the block-triangular change of variables explicit as a
   matrix factorisation ($2|E| = 2|E|$ on both sides; the $\phi$-space has dimension $|V|$,
   so exhibit the exact complement — e.g. the $(2|E| - |V|)$-dimensional internal space — and
   the determinant multiplicativity step, rather than asserting "Schur complement" at the
   level of the kernel computation alone).
2. **Degenerate cases.** Degree-1 vertices (present in the sieve graph: prime-power
   composites), multi-edges if any, and the locus of $u$ with $1 - u^2w_e^2 = 0$ (where the
   elimination is singular — the identity extends by continuity/polynomiality, but say so).
3. **Symbolic certification.** Re-verify coefficient-by-coefficient with the sympy-verifier
   at $n \le 6$ on the actual stage graphs (the F2 numeric validation was floating-point;
   gate-1.md claimed a symbolic check inside `prime_graph_lab.py` — reproduce it
   independently, in this project's tree).
4. **Independent cross-check** against the published weighted Bass identities
   (Mizuno–Sato 2004; Watanabe–Fukumizu 2009) — confirm ours is their specialisation or a
   correct variant.

## 4. What the identity buys once proven

Everything spectral about the weighted stages routes through $\det M(u)$: the trivial factors
$\prod_e(1 - u^2w_e^2)$ contribute only real zeros $u = \pm 1/w_e$, so **the non-real stage
zeros are exactly the non-real zeros of $\det M(u)$**. The diagonal terms
$u^2w^2/(1 - u^2w^2)$ are Möbius functions of $u^2$ (Herglotz-type structure) — the raw
material for the honest confinement locus (WP06) that replaces the quarantined one, and the
per-edge product is the multiplicative structure the Asano question (WP13) acts on.
