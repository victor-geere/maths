# PSC2-F05 — WP08: the edge-purity (anti-Siegel) theorem is proven for every stage and every $\beta$; the $\beta$-sweep fires the pre-registered falsifier — "exactly 4 detached" is a finite-window artifact, while the real-detached census is the Perron pair alone at every point measured

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP08](../workpackages/PSC2-WP08-anti-siegel.md). Code/run:
`numerics/wp08_beta_sweep.py` (numpy float64; seed 20260708 used only in the rewired-null
control — no random draw enters any census value or theorem check; the $n=12$ anchor point
uses scipy's sparse LM eigensolver and is skipped with a notice if scipy is absent).
Tags per [PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> **Objective.** Upgrade F4 from measurement to theorem: relative to WP06's locus, the
> detached spectrum of $B_w$ consists exactly of the structural part (Perron + bipartite
> mirror + one conjugate pair) — **no arithmetic exceptionals**. Measured: exactly 4 detached
> at every stage $n = 6\ldots9$, $\beta = \tfrac12$.
>
> **Ordering (binding).** 1. **$\beta$-sweep first** ($\beta \in [0.3, 0.7]$, numerically):
> check the finding is not a $\beta = \tfrac12$ accident. 2. Proof: community-detection
> technology (Krzakala et al.; Bordenave–Lelarge–Massoulié) […] Proof input: divisor-count
> concentration (shared with WP07).
>
> **Falsifier (two-sided, pre-registered).** A $\beta$ at which a fifth eigenvalue detaches
> **persistently** across stages — a genuine discovery either way; document per the
> two-sided rule (I0.4), do not suppress.

Per the gating update recorded in the WP after [F03](PSC2-F03-weighted-locus.md) (locus
weak, locus-detached count $0$), the theorem target was already re-scoped to the **measured
census** ($|\mu| > 1.02\sqrt{\mu_1}$). Additional mechanical criteria were fixed in the
script header before any $(n,\beta)$ with $\beta \ne \tfrac12$ or $n \ge 10$ was computed:
grid $\beta \in \{0.30, 0.35, \ldots, 0.70\}$ × $n = 4\ldots10$ plus a coarse $n = 11$ row;
survives iff every point with $n \ge 5$ shows exactly 4 detached $= 2$ real $+$ 2 purely
imaginary; "persistent fifth" $= {\ge}6$ detached at $\ge 3$ consecutive stages at one
$\beta$; ingredient checks E1–E6; two-sided controls (classical $K_{a,b}$ closed form,
weakly-coupled-copies teeth, interpretive nulls).

## Regression check

N00 targets reproduced: **yes** — lab-$B$ census at $\beta = \tfrac12$ rebuilt through
`prime_graph_lab`'s own builders (rule I0.5): $\mu_1 = 3.5419, 5.2810, 7.6871, 10.9663$ at
$n = 6\ldots9$ with detached census $4$ (of which $2$ real), matching N00 §3 verbatim; the
half-dimensional $C$-method (below) agrees with the lab-$B$ nonzero $|\mathrm{spec}|$ to
$1.8\times10^{-14}$ across $n = 5\ldots7$, $\beta \in \{0.3, 0.5, 0.7\}$. No $\gamma$-list,
no zero data, no fitted constant anywhere (the census constant $1.02$ is inherited
unchanged from the N00 §3 definition). *Harness note:* the first run's predicted $K_{a,b}$
multiset omitted the $\pm1$ family of multiplicity $(a-1)(b-1)$; the closed form was
corrected against direct diagonalization (census counts were unaffected by the bug; the
correction is flagged in the script header).

## Setting

$P_n = \{p < 2^n\}$, $I_n = [2^n, 2^{n+1})$, $C_n$ = composites in $I_n$; bipartite graph
$G_n$ on $P_n \cup C_n$ with edges $\{p, m\}$ for $p \mid m$ and weights
$w_{pm} = v_p(m)\,p^{-\beta} > 0$. $B_w$ is the weighted non-backtracking operator on the
$2|E|$ directed edges (lab convention; spectrum-equivalent to the
$\sqrt{\vphantom{w}}$-convention by diagonal conjugation, F03 L1). Direction grading (F03
L2) makes $B_w$ block anti-diagonal, $B_w = \begin{pmatrix}0 & X\\ Y & 0\end{pmatrix}$, and
one Schur step gives

$$\det(I - uB_w) \;=\; \det(I - u^2 C), \qquad C := XY,\qquad
C_{(p\to m),(p'\to m')} = w_{p'm}\,w_{p'm'}\,[\,p' \mid m\,][\,p' \ne p\,][\,m' \ne m\,],$$

on the $|E|$ states $(p \to m)$. So $\mathrm{spec}(B_w)\setminus\{0\} =
\pm\sqrt{\mathrm{spec}(C)\setminus\{0\}}$ with matching multiplicities, and the whole sweep
runs on $C$ at half dimension; by leaf reduction (F03 Prop B1, proven) $C$ is built on the
2-core. Note $\mathrm{Tr}\,C = 0$ identically (the diagonal is excluded by $p' \ne p$): the
eigenvalues of $C$ sum to zero, so negative real-part mass at least equal to $\rho(C)$ is
always present — the mirror sector is never empty. Census (N00 §3,
unchanged): $\mu$ detached iff $|\mu| > 1.02\sqrt{\mu_1}$, i.e. $|\nu| > 1.02^2\mu_1$ for
$\nu = \mu^2 \in \mathrm{spec}(C)$, $\mu_1 = \sqrt{\rho(C)}$.

## Result 1 — the edge-purity theorem (G4 at the spectral edge; proven)

**Lemma 1 (grading).** As displayed above: $\det(I - uB_w) = \det(I - u^2C)$; in particular
$\mathrm{spec}(B_w) = -\mathrm{spec}(B_w)$, and a simple eigenvalue $\nu \ne 0$ of $C$
yields the pair of simple eigenvalues $\pm\sqrt\nu$ of $B_w$. *Proven* (F03 L2 plus the
one-line Schur factorisation $\det\begin{psmallmatrix}I & -uX\\ -uY & I\end{psmallmatrix}
= \det(I - u^2XY)$; certified exactly on the stage graphs in F03 §A3).

**Lemma 2 (leaf reduction; F03 Prop B1, proven).** The nonzero spectra of $B_w$ on $G_n$
and on its 2-core $H_n$ coincide.

**Lemma 3 (structure of the core — the divisor-count input shared with WP07).** For every
$n \ge 4$:
(a) $G_n$ is connected;
(b) $H_n$ is nonempty, connected, has minimum degree $\ge 2$, contains
$K_{2,t_6}$ with $t_6 = \#\{m \in I_n : 6 \mid m\} \ge 3$ (vertices $2$, $3$ and the
multiples of $6$), and is not a cycle;
(c) $H_n$ contains a $4$-cycle and a $6$-cycle — equivalently, closed $C$-walks of the
coprime lengths $2$ and $3$.

*Proof.* (a) Every composite $m \in I_n$ has all prime factors in $P_n$ (a prime factor
$q \ge 2^n$ of a composite $m$ forces $m \ge 2q \ge 2^{n+1}$), so $m$ is adjacent to some
$p \in P_n$. Every $p \in P_n$ is adjacent to a multiple of $2p$ in $I_n$ — F04 Lemma 1
(hub counts): $2^n$ consecutive integers contain a multiple of $2p$ when $2p \le 2^n$, and
$2p$ itself lies in $I_n$ when $p > 2^{n-1}$ — and every such multiple is even, $\ge 2^n
\ge 4$, hence composite and adjacent to $2$. So every vertex connects to the vertex $2$.
(b) $I_n$ contains $\ge \lfloor 2^n/6\rfloor \ge 2$ multiples of $6$ ($n \ge 4$), and
$\ge 3$ for $n \ge 5$ (at $n = 4$ explicitly $\{18, 24, 30\}$, $t_6 = 3$); each is even and
$\ge 16$, hence composite, adjacent to both $2$ and $3$: this is $K_{2,t_6} \subseteq G_n$.
Iterated leaf-pruning never deletes a vertex of a subgraph of minimum degree $\ge 2$ (by
induction each such vertex keeps degree $\ge 2$ among survivors), so $K_{2,t_6} \subseteq
H_n$ and $\deg_{H_n}(2) \ge t_6 \ge 3$; a cycle has all degrees $2$, so $H_n$ is not a
cycle. Deleting a vertex of degree $\le 1$ from a connected graph leaves it connected;
iterating from the connected $G_n$ keeps $H_n$ connected.
(c) $4$-cycle: two distinct multiples $m_1 \ne m_2$ of $6$ give $2\,m_1\,3\,m_2$. $6$-cycle
for $n \ge 5$: pick $m_1$ a multiple of $6$ with $5 \nmid m_1$ (count
$\ge (2^n/6 - 1) - (2^n/30 + 1) = 2^{n+1}/15 - 2 > 0$), $m_2$ an odd multiple of $15$ (the
admissible $k$ with $15k \in I_n$ fill an interval of length $2^n/15 \ge 2$, which contains
an odd integer), $m_3$ any multiple of $10$ in $I_n$; then $m_2$ is odd while $m_1, m_3$
are even, $5 \nmid m_1$ but $5 \mid m_3$, so the three are pairwise distinct, all
composite, and $2\,m_1\,3\,m_2\,5\,m_3$ is a $6$-cycle. At $n = 4$ take $(18, 30, 20)$.
Cycles have minimum degree $2$, hence lie in $H_n$; traversing a $2k$-cycle is a closed
non-backtracking walk of length $2k$, i.e. a closed $C$-walk of length $k$. $\square$

**Lemma 4 (non-backtracking irreducibility; classical).** For a finite connected graph with
minimum degree $\ge 2$ that is not a cycle, the directed-edge (Hashimoto) graph is strongly
connected. *(Classical: Kotani–Sunada 2000, "Zeta functions of finite graphs", J. Math.
Sci. Univ. Tokyo 7, 7–25; Terras 2011, "Zeta Functions of Graphs: A Stroll through the
Garden", CUP — the irreducibility of the edge matrix underlying the graph prime number
theorem. Additionally machine-verified on the actual stage cores at every computed stage
$n = 4\ldots11$ by explicit two-sided reachability on the $C$-state graph — ingredient E4
below — so the computed instances do not rest on the citation.)*

**Theorem (edge purity — no exceptional eigenvalue at the spectral edge).** For every stage
$n \ge 4$ and every $\beta \in \mathbb{R}$, let $\rho = \rho(B_w) > 0$. Then:
(a) $\mathrm{spec}(B_w) = -\mathrm{spec}(B_w)$;
(b) the peripheral spectrum of $B_w$ is exactly $\{\rho, -\rho\}$, both simple: every other
eigenvalue $\mu$ satisfies $|\mu| < \rho$ strictly;
(c) for every census radius $R \in (0, \rho)$, the detached set
$D_R = \{\mu \in \mathrm{spec}(B_w) : |\mu| > R\}$ is invariant under $\mu \mapsto -\mu$
and $\mu \mapsto \bar\mu$, has even cardinality, contains $\{\pm\rho\}$, and its real
members pair as $\{x, -x\}$; if $|D_R| = 4$ with exactly two real members, then
$D_R = \{\pm\rho, \pm i\tau\}$ with $\tau \in (R, \rho)$ and $-\tau^2$ a simple negative
eigenvalue of $C$ — the non-real members are forced to be **purely imaginary**.

*Proof.* (a) is Lemma 1 (the characteristic polynomial is even in $u$). (b) By Lemma 2 pass
to the core. $C \ge 0$ entrywise with support the two-step non-backtracking adjacency,
which is independent of $\beta$ (weights $v_p(m)p^{-\beta}$ are positive for every real
$\beta$). By Lemmas 3(a,b) and 4 the Hashimoto graph of $H_n$ is strongly connected; any
directed path between two states of the same direction class has even length, so the
$C$-state graph is strongly connected, i.e. $C$ is irreducible. The period of an
irreducible nonnegative matrix is the gcd of its closed-walk lengths; Lemma 3(c) provides
closed $C$-walks of lengths $2$ and $3$, so $C$ is aperiodic, hence **primitive**.
Perron–Frobenius for primitive matrices (Horn–Johnson, *Matrix Analysis*, §8.5):
$\rho_C = \rho(C) > 0$ is a simple eigenvalue and every other eigenvalue $\nu$ of $C$ has
$|\nu| < \rho_C$. By Lemma 1 the eigenvalues $\pm\sqrt{\rho_C}$ of $B_w$ are simple of
modulus $\rho = \sqrt{\rho_C}$, and every other eigenvalue has modulus
$\sqrt{|\nu|} < \rho$. (c) Closure under negation is (a); under conjugation because $B_w$
is real. Members of $D_R$ are nonzero, so they pair as $\{\mu, -\mu\}$: even cardinality,
real members in pairs $\{x, -x\}$. If $|D_R| = 4$ with two real members, the reals are
$\{\pm\rho\}$ (contained in $D_R$ since $R < \rho$); the remaining pair $\{\mu, -\mu\}$ is
conjugation-closed with $\mu$ non-real, forcing $\bar\mu = -\mu$, i.e. $\mu = i\tau$; then
$-\tau^2 \in \mathrm{spec}(C)$ is negative, simple because a double $-\tau^2$ would put
four members $\pm i\tau$ (with multiplicity) besides $\pm\rho$ in $D_R$; and $\tau < \rho$
by (b). $\blacksquare$

**Why (b) has content — the degenerate comparator.** Edge purity is *not* automatic for
weighted bipartite hub graphs: for the pure hub $K_{2,b}$ every cycle is a $4$-cycle, every
closed $C$-walk has even length, $C$ has period $2$, and the NB spectrum (control below,
verified against the closed form $\{\pm\sqrt{b-1}\} \cup \{\pm i\sqrt{b-1}\} \cup
\{\pm i\}^{b-1} \cup \{\pm 1\}^{b-1}$) has the imaginary pair $\pm i\sqrt{b-1}$ **at the
Perron modulus** — a maximal "exceptional degeneracy" at the edge. The stage graphs escape
precisely through Lemma 3(c): the coexistence of multiples of $6$, $10$ and $15$ inside the
octave $I_n$ — an arithmetic fact about $I_n$, and exactly the divisor-count input the WP
predicted would be consumed. In the graph-Siegel dictionary (heuristic, per the WP's
pricing): *no eigenvalue, real or not, can be degenerate with the Perron pair at any stage
or any damping* — the finite-stage analogue of "no exceptional zero at the edge of the
critical strip", proven unconditionally.

## Result 2 — the $\beta$-sweep: the pre-registered falsifier fired

Verbatim output (controls, ingredients, sweep, verdicts, diagnostics):

```
== WP08 (G4): beta-sweep of the detached census + edge-purity theorem ingredients ==
[control] unweighted K_{a,b} vs closed-form NB spectrum {+-sqrt((a-1)(b-1)), +-i sqrt(b-1) x(a-1), +-i sqrt(a-1) x(b-1), +-1 x(a-1)(b-1)}:
   K_2,5: |spectrum| matches closed form: True;  census 4 (2 real) (expected 4 (2 real))  [imaginary pair AT Perron modulus - period-4 comparator]
   K_2,12: |spectrum| matches closed form: True;  census 4 (2 real) (expected 4 (2 real))  [imaginary pair AT Perron modulus - period-4 comparator]
   K_3,8: |spectrum| matches closed form: True;  census 6 (2 real) (expected 6 (2 real))
[teeth] two weakly coupled copies of stage n=6: detached = 8 (4 real, 4 imaginary) >= 6: True  (expected 8)
[regress] lab-B census at beta=1/2 vs N00 par.3 (must be mu1 match to 1e-3, 4/2):
   n=6: mu1=3.5419 (N00 3.5419);  detached 4 (2 real);  |Re| of non-real detached = 4.0e-17: ok
   n=7: mu1=5.2810 (N00 5.281);  detached 4 (2 real);  |Re| of non-real detached = 1.2e-16: ok
   n=8: mu1=7.6871 (N00 7.6871);  detached 4 (2 real);  |Re| of non-real detached = 1.8e-15: ok
   n=9: mu1=10.9663 (N00 10.9663);  detached 4 (2 real);  |Re| of non-real detached = 2.7e-17: ok
[regress] C-method vs lab-B nonzero |spec| (rel 1e-8), n=5..7 x beta={0.3,0.5,0.7}:
   worst relative deviation: 1.79e-14  (< 1e-8: True)

-- theorem ingredients E1-E5 per stage (beta-independent) --
   n= 4: connected=True  core|P|,|C|=(4, 6) (pruned 7) deg>=2+hub=True (t6=3)  witnesses=True (triple (18, 30, 20))  strong-conn=True  TrC=0,TrC^2>0,TrC^3>0=True
   n= 5: connected=True  core|P|,|C|=(8, 20) (pruned 8) deg>=2+hub=True (t6=5)  witnesses=True (triple (36, 45, 40))  strong-conn=True  TrC=0,TrC^2>0,TrC^3>0=True
   n= 6: connected=True  core|P|,|C|=(13, 42) (pruned 14) deg>=2+hub=True (t6=11)  witnesses=True (triple (66, 75, 70))  strong-conn=True  TrC=0,TrC^2>0,TrC^3>0=True
   n= 7: connected=True  core|P|,|C|=(23, 94) (pruned 19) deg>=2+hub=True (t6=21)  witnesses=True (triple (132, 135, 130))  strong-conn=True  TrC=0,TrC^2>0,TrC^3>0=True
   n= 8: connected=True  core|P|,|C|=(39, 194) (pruned 34) deg>=2+hub=True (t6=43)  witnesses=True (triple (258, 270, 260))  strong-conn=True  TrC=0,TrC^2>0,TrC^3>0=True
   n= 9: connected=True  core|P|,|C|=(68, 402) (pruned 64) deg>=2+hub=True (t6=85)  witnesses=True (triple (516, 525, 520))  strong-conn=True  TrC=0,TrC^2>0,TrC^3>0=True
   n=10: connected=True  core|P|,|C|=(123, 833) (pruned 103) deg>=2+hub=True (t6=171)  witnesses=True (triple (1026, 1035, 1030))  strong-conn=True  TrC=0,TrC^2>0,TrC^3>0=True
   n=11: connected=True  core|P|,|C|=(218, 1693) (pruned 191) deg>=2+hub=True (t6=341)  witnesses=True (triple (2052, 2055, 2050))  strong-conn=True  TrC=0,TrC^2>0,TrC^3>0=True

-- census sweep --
    n  beta   nE    mu1      det  real  imag  cplx   m_det   m_bulk   |nu2|/rho  tau/mu1  edge-gap
    4  0.30    13   1.6628    2     2     0     0    1.264    0.977    0.5965   0.7724   0.4031
    4  0.35    13   1.5808    4     2     2     0    1.011    0.915    0.6723   0.8200   0.3277
    4  0.40    13   1.5032    4     2     2     0    1.012    0.887    0.7084   0.8417   0.2916
    4  0.45    13   1.4297    4     2     2     0    1.006    0.866    0.7360   0.8579   0.2640
    4  0.50    13   1.3602    2     2     0     0    1.143    0.996    0.7589   0.8712   0.2411
    4  0.55    13   1.2943    2     2     0     0    1.115    0.984    0.7788   0.8825   0.2212
    4  0.60    13   1.2319    2     2     0     0    1.088    0.971    0.7964   0.8924   0.2036
    4  0.65    13   1.1727    2     2     0     0    1.062    0.957    0.8122   0.9012   0.1878
    4  0.70    13   1.1167    2     2     0     0    1.036    0.942    0.8264   0.9091   0.1736
    5  0.30    42   2.8465    4     2     2     0    1.407    0.888    0.7232   0.8504   0.2768
    5  0.35    42   2.7023    4     2     2     0    1.390    0.872    0.7435   0.8623   0.2565
    5  0.40    42   2.5663    4     2     2     0    1.371    0.855    0.7620   0.8729   0.2380
    5  0.45    42   2.4382    4     2     2     0    1.351    0.839    0.7790   0.8826   0.2210
    5  0.50    42   2.3173    4     2     2     0    1.330    0.823    0.7946   0.8914   0.2054
    5  0.55    42   2.2032    4     2     2     0    1.309    0.807    0.8090   0.8994   0.1910
    5  0.60    42   2.0953    4     2     2     0    1.287    0.791    0.8223   0.9068   0.1777
    5  0.65    42   1.9934    4     2     2     0    1.265    0.776    0.8346   0.9136   0.1654
    5  0.70    42   1.8969    4     2     2     0    1.242    0.760    0.8461   0.9198   0.1539
    6  0.30    95   4.3432    4     2     2     0    1.852    0.899    0.8217   0.9065   0.1783
    6  0.35    95   4.1245    4     2     2     0    1.819    0.867    0.8345   0.9135   0.1655
    6  0.40    95   3.9187    4     2     2     0    1.785    0.848    0.8463   0.9199   0.1537
    6  0.45    95   3.7248    4     2     2     0    1.752    0.831    0.8572   0.9258   0.1428
    6  0.50    95   3.5419    4     2     2     0    1.718    0.815    0.8673   0.9313   0.1327
    6  0.55    95   3.3693    4     2     2     0    1.685    0.799    0.8766   0.9363   0.1234
    6  0.60    95   3.2062    4     2     2     0    1.652    0.783    0.8852   0.9409   0.1148
    6  0.65    95   3.0519    4     2     2     0    1.619    0.768    0.8933   0.9451   0.1067
    6  0.70    95   2.9060    4     2     2     0    1.586    0.752    0.9007   0.9491   0.0993
    7  0.30   219   6.4957    4     2     2     0    2.240    0.978    0.8039   0.8966   0.1961
    7  0.35   219   6.1635    4     2     2     0    2.199    0.944    0.8166   0.9037   0.1834
    7  0.40   219   5.8513    4     2     2     0    2.158    0.912    0.8284   0.9102   0.1716
    7  0.45   219   5.5576    4     2     2     0    2.118    0.880    0.8394   0.9162   0.1606
    7  0.50   219   5.2810    4     2     2     0    2.077    0.849    0.8498   0.9218   0.1502
    7  0.55   219   5.0202    4     2     2     0    2.036    0.820    0.8595   0.9271   0.1405
    7  0.60   219   4.7740    4     2     2     0    1.996    0.791    0.8686   0.9320   0.1314
    7  0.65   219   4.5415    4     2     2     0    1.957    0.763    0.8771   0.9365   0.1229
    7  0.70   219   4.3218    4     2     2     0    1.917    0.739    0.8851   0.9408   0.1149
    8  0.30   471   9.4526    8     2     2     4    1.005    0.826    0.8225   0.9069   0.1775  <-- DEVIATION
    8  0.35   471   8.9693    4     2     2     0    2.682    0.970    0.8344   0.9135   0.1656
    8  0.40   471   8.5155    4     2     2     0    2.631    0.937    0.8455   0.9195   0.1545
    8  0.45   471   8.0888    4     2     2     0    2.580    0.904    0.8559   0.9251   0.1441
    8  0.50   471   7.6871    4     2     2     0    2.529    0.872    0.8655   0.9303   0.1345
    8  0.55   471   7.3085    4     2     2     0    2.479    0.842    0.8746   0.9352   0.1254
    8  0.60   471   6.9512    4     2     2     0    2.429    0.812    0.8830   0.9397   0.1170
    8  0.65   471   6.6139    4     2     2     0    2.380    0.784    0.8908   0.9438   0.1092
    8  0.70   471   6.2950    4     2     2     0    2.331    0.756    0.8982   0.9477   0.1018
    9  0.30  1009  13.4906    8     2     2     4    1.035    0.813    0.8280   0.9100   0.1720  <-- DEVIATION
    9  0.35  1009  12.7989    4     2     2     0    3.214    0.998    0.8397   0.9164   0.1603
    9  0.40  1009  12.1500    4     2     2     0    3.152    0.964    0.8506   0.9223   0.1494
    9  0.45  1009  11.5401    4     2     2     0    3.090    0.930    0.8608   0.9278   0.1392
    9  0.50  1009  10.9663    4     2     2     0    3.029    0.897    0.8702   0.9328   0.1298
    9  0.55  1009  10.4257    4     2     2     0    2.968    0.866    0.8790   0.9375   0.1210
    9  0.60  1009   9.9157    4     2     2     0    2.908    0.835    0.8872   0.9419   0.1128
    9  0.65  1009   9.4343    4     2     2     0    2.849    0.806    0.8948   0.9460   0.1052
    9  0.70  1009   8.9793    4     2     2     0    2.790    0.778    0.9020   0.9497   0.0980
   10  0.30  2147  19.2807    6     2     4     0    1.242    0.922    0.8243   0.9079   0.1757  <-- DEVIATION
   10  0.35  2147  18.2895    6     2     4     0    1.128    0.945    0.8361   0.9144   0.1639  <-- DEVIATION
   10  0.40  2147  17.3600    4     2     2     0    3.760    0.996    0.8472   0.9204   0.1528
   10  0.45  2147  16.4868    4     2     2     0    3.686    0.961    0.8574   0.9260   0.1426
   10  0.50  2147  15.6655    4     2     2     0    3.613    0.927    0.8670   0.9311   0.1330
   10  0.55  2147  14.8919    4     2     2     0    3.541    0.894    0.8760   0.9359   0.1240
   10  0.60  2147  14.1625    4     2     2     0    3.470    0.862    0.8843   0.9404   0.1157
   10  0.65  2147  13.4739    4     2     2     0    3.399    0.832    0.8921   0.9445   0.1079
   10  0.70  2147  12.8233    4     2     2     0    3.329    0.802    0.8994   0.9484   0.1006
   11  0.30  4501  27.3752    6     2     4     0    1.663    0.844    0.8264   0.9091   0.1736  <-- DEVIATION
   11  0.50  4501  22.2395    6     2     4     0    1.307    0.705    0.8689   0.9322   0.1311  <-- DEVIATION
   11  0.70  4501  18.2043    4     2     2     0    3.971    0.985    0.9010   0.9492   0.0990
[nulls] interpretive controls at n=8, beta=0.5 (recorded, not pass/fail):
   k==1 weights, true divisor support:   detached 4 (2 real, 2 imag)  tau/mu1=0.880
   rewired support (seed 1), w=p^-b:      detached 4 (2 real, 2 imag)  tau/mu1=0.878
   rewired support (seed 2), w=p^-b:      detached 4 (2 real, 2 imag)  tau/mu1=0.903
   rewired support (seed 3), w=p^-b:      detached 4 (2 real, 2 imag)  tau/mu1=0.910

[verdict] deviating grid points (n >= 5): [(8, 0.3, 8, 2, 2, 4), (9, 0.3, 8, 2, 2, 4), (10, 0.3, 6, 2, 4, 0), (10, 0.35, 6, 2, 4, 0), (11, 0.3, 6, 2, 4, 0), (11, 0.5, 6, 2, 4, 0)]
[verdict] persistent-fifth betas: [0.3];  fifth-watch: max bulk |mu|/threshold over sweep = 0.998
[verdict] pre-registered census verdict: PERSISTENT FIFTH (falsifier branch)

-- post-falsifier diagnostics (addendum; criteria above unchanged) --
   [D1 n= 8 beta=0.30] R+3.014  R-2.734  C 1.005  C 1.005  R+0.826  R-0.815  C 0.789  C 0.789  R+0.751  R-0.735  R+0.677  R-0.673
   [D1 n= 9 beta=0.35] R+3.507  R-3.214  C 0.998  C 0.998  C 0.777  C 0.777  R+0.763  R-0.751  R+0.694  R-0.694  R+0.673  R-0.657
   [D1 n=10 beta=0.30] R+4.305  R-3.908  R-1.242  R-0.922  C 0.832  C 0.832  R+0.717  R-0.708  R+0.677  R-0.672  C 0.655  C 0.655
   [D1 n=10 beta=0.50] R+3.880  R-3.613  C 0.927  C 0.927  C 0.694  C 0.694  R+0.665  R-0.657  R+0.628  R-0.623  R+0.606  R-0.601
   [D1 n=11 beta=0.50] R+4.623  R-4.310  R-1.307  C 0.705  C 0.705  R-0.690  R+0.606  R-0.604  R+0.594  R-0.594  R+0.583  R-0.548
   [D1 n=11 beta=0.70] R+4.183  R-3.971  R-0.985  R-0.682  C 0.589  C 0.589  R+0.560  R-0.558  R-0.549  R+0.549  R+0.539  R-0.508
   [D2 n=10 beta=0.50] rho=245.4; most negative nu: [-212.8   -7.    -6.3];  isolated hub strengths: (2,3): t=171 h=205.1  (2,5): t=102 h=78.7  (3,5): t=68 h=32.8  (2,7): t=73 h=43.9
   [D2 n=11 beta=0.50] rho=494.6; most negative nu: [-429.8  -39.6  -11. ];  isolated hub strengths: (2,3): t=341 h=413.7  (2,5): t=205 h=159.6  (3,5): t=137 h=65.1  (2,7): t=146 h=89.3
   [D2 n=10 beta=0.30] rho=371.7; most negative nu: [-306.4  -31.   -17. ];  isolated hub strengths: (2,3): t=171 h=293.5  (2,5): t=102 h=124.7  (3,5): t=68 h=56.4  (2,7): t=73 h=74.5
   [D3 n=12 beta=0.5] nE=9397  mu1=31.5263  detached 6 (2 real, 4 imag);  top ladder: R+5.505  R-5.135  R-1.636  C 0.710  C 0.710  R-0.585  R+0.556  R-0.553
```

(Ladder legend: entries are $\sqrt{|\nu|}\,/\,1.02\sqrt{\mu_1}$ — the census-threshold
ratio of the corresponding $B$-eigenvalue pair — for the top 12 $|\nu|$; `R+`/`R-` = real
positive/negative $\nu$ (a real/imaginary $B$-pair), `C` = non-real $\nu$ (a genuinely
complex $B$-quadruple member).)

**What fired.** At $\beta = 0.30$ the count is ${\ge}6$ at four consecutive stages
$n = 8, 9, 10, 11$ — the mechanical "persistent fifth" rule triggers. Beyond the
pre-registered rule, the anchor $\beta = \tfrac12$ itself deviates from $n = 11$ on:
$6 = 2$ real $+ 4$ imaginary at $n = 11$, confirmed and *strengthened* at the $n = 12$
anchor point ($6$ detached, third pair at $1.636\times$ threshold). **The F4/N00 census
"exactly 4 detached, stable" was a finite-window artifact of $n \le 10$, $\beta \ge 0.4$**
(and, at $\beta=\tfrac12$, of $n \le 10$): the anchors themselves reproduce verbatim — what
fails is only their extrapolation to a stable law.

## Result 3 — what the fifth eigenvalue is (diagnostics)

- **It is isolated structure, not bulk leakage.** At $(n, \beta) = (11, \tfrac12)$ the
  third detached object sits at $1.307\times$ threshold with the next spectral mass at
  $0.705$ — an $85\%$ gap to the cloud; at $n = 12$ it has grown to $1.636$ vs $0.710$. The
  census circle $1.02\sqrt{\mu_1}$ (already flagged by F03 addendum (ii) as a bulk-edge
  *estimate*) is being crossed by discrete structural objects; the `m_bulk` column of the
  count-4 rows mostly tracks the *next member of the same discrete family* hovering under
  the circle (e.g. $0.998$ at $(9, 0.35)$), not the continuous bulk.
- **Entry mechanism: complex-pair collision.** The second family enters as a genuinely
  complex $\nu$-quadruple ($(8\ldots9, 0.30)$ at ratio $\approx 1.0$; $(10, \tfrac12)$ at
  $0.927$), then collides onto the negative real axis (a real-matrix eigenvalue collision)
  and splits into two negative reals — two imaginary $B$-pairs — of which the larger grows:
  $0.927 \to 1.307 \to 1.636$ at the anchor over $n = 10, 11, 12$. Every settled detached
  object is an **imaginary pair**; the complex quadruples are the transient.
- **The leading imaginary pair is the $(2,3)$-hub mirror.** The isolated weighted sub-hub
  on $\{2, 3\} \cup \{6\mathbb{Z} \cap I_n\}$ (a weighted $K_{2,t_6}$, whose two-prime
  alternation forces spectrum $\pm h$) predicts the full graph's most negative eigenvalue
  within $4$–$5\%$ at every sampled point: $h = 205.1$ vs $\nu_2 = -212.8$ $(10, \tfrac12)$;
  $413.7$ vs $-429.8$ $(11, \tfrac12)$; $293.5$ vs $-306.4$ $(10, 0.30)$. The identification
  of the *second* imaginary pair is open — the isolated $(2,5)$-hub overestimates it by
  $\approx 4\times$ ($159.6$ vs $39.6$ at $(11, \tfrac12)$): embedding dilution is not
  negligible there, so "the family enumerates prime-pair hubs" stays **heuristic**.
- **The interpretive nulls say the first imaginary pair is generic, not arithmetic:**
  $k \equiv 1$ weights and all three degree-preserving rewired supports show the same
  $4 = 2 + 2$ census with $\tau/\mu_1 \approx 0.88$–$0.91$ at $(8, \tfrac12)$ — the pair is
  a hub-profile phenomenon of the weighted degree sequence, present with or without the
  divisor structure.
- **The real-detached census is exactly $2$ — everywhere.** All $66$ grid points, the
  $n = 12$ anchor, and all null/teeth controls (up to copy-doubling) show real detached
  $= \{\pm\mu_1\}$ only. On the would-be Landau–Siegel side (a second *positive*
  $\nu$ = a second real $B$-pair), the margin **improves with $n$**: the second-largest
  positive ratio falls $0.826, 0.763, 0.717, 0.665, 0.606, 0.556$ along the D1/D3 ladders
  (at the anchor: $0.665 \to 0.606 \to 0.556$ over $n = 10, 11, 12$). All census growth
  lives in the negative-$\nu$ (imaginary, bipartite-mirror) sector.
- **The proven edge gap is measured comfortably open:** peripheral gap
  $1 - |\nu_2|/\rho \approx 0.13$ at $\beta = \tfrac12$, stable in $n$ (no
  edge-degeneracy trend), $\approx 0.10$ at $\beta = 0.7$.

## Verdict against the pre-registered criteria

**Census: FALSIFIER BRANCH — "persistent fifth"** by the mechanical rule at $\beta = 0.30$
($n = 8\ldots11$), with the anchor $\beta = \tfrac12$ crossing at $n = 11$ and $n = 12$
confirming growth. Documented two-sidedly per I0.4; nothing suppressed. The count-level
census claim ("exactly 4, stable") is **dead as an $n$-uniform statement**.
**Theorem: lands** at the edge-purity strength for every $n \ge 4$ and every $\beta$ — the
honest proven core of "no arithmetic exceptionals": nothing shares the peripheral circle
with the Perron pair, and any count-4 census is forced into the structural shape
Perron $+$ mirror $+$ imaginary pair. The WP's step-2 technology
(Krzakala/Bordenave–Lelarge–Massoulié) was **not** needed for this and was **not** consumed
by the falsifier: a Bordenave-type proven bulk bound is exactly what the discovery makes
valuable, with the corrected target below.

## Corrected statement of G4 (replaces "exactly 4"; the surviving claims)

1. *(proven)* Edge purity: peripheral spectrum $= \{\pm\rho\}$, simple, for all $n \ge 4$,
   all $\beta$; detached sets are $\pm$/conjugation-closed with even real part; count-4
   censuses have the structural form.
2. *(verified)* **No graph-Siegel avatar in census form:** real detached $= \{\pm\mu_1\}$
   exactly, at every sweep point and the $n = 12$ anchor, with the second-positive margin
   falling in $n$ ($0.83 \to 0.56$).
3. *(verified)* The non-real detached census is a **growing hierarchy of imaginary pairs**
   (transiently complex quadruples at entry), crossing the $1.02\sqrt{\mu_1}$ circle at a
   $\beta$-dependent stage $n^*(\beta)$: $n^* \le 8$ at $\beta = 0.30$, $n^* = 10$ at
   $0.35$, $n^* = 11$ at $\tfrac12$, $n^* > 11$ at $0.70$ (poised at $0.985$).
4. *(heuristic)* The hierarchy enumerates prime-pair hub blocks, led by the $(2,3)$-hub
   mirror (within $5\%$); the graph-Siegel dictionary (exceptional real poles ↔
   Landau–Siegel) remains heuristic per the WP's pricing, now with the sharpened reading
   that all detached growth is confined to the antisymmetric (imaginary) sector.

The remaining honest theorem target on this axis (open; charter): a proven bulk/real-sector
bound — e.g. Bordenave's tangle-free method with equidistribution replacing randomness
(shared engine with WP07 route β) — establishing (2) as a theorem: *no second positive
detached eigenvalue of $C$ for all $n$*.

## Tag

- Edge-purity theorem (Lemmas 1–3 + theorem + corollary (c)): **proven** — Lemmas 1–2
  imported proven from F03; Lemma 3 proved above from elementary counting (F04 Lemma 1
  input); Lemma 4 classical with citation *and* machine-verified on every computed stage
  $n = 4\ldots11$ (ingredient E4), so the computed instances are citation-independent.
- $\beta$-sweep census, ladders, hub comparison, $n = 12$ anchor, controls and nulls:
  **verified** (two-sided; the teeth control shows the census detects a planted fifth; the
  $K_{a,b}$ control pins the machinery to a closed form and exhibits the period-4
  degenerate comparator).
- "Exactly 4 detached at every stage" (F4 reading; live conjecture 2 in count form):
  **refuted** as an $n$-uniform law (pre-registered falsifier branch; correction notice to
  S02 §6 appended).
- Hub-block dictionary and graph-Siegel dictionary: **heuristic** (unchanged pricing).

**Scope (do-not list compliance).** Everything here concerns the finite weighted divisor
graphs' non-backtracking spectra. No claim about $\zeta$'s zeros; no $\gamma$-data
consumed; the Siegel language is a dictionary, not an assertion of arithmetic consequence.
RH remains **open**.

## Propagation

Charter ledger updated: **yes** (T8/WP08 → done, discovery branch; live conjecture 2
restated in the corrected form; ledger rows added; ordering note appended). Source doc
correction notice needed: **yes** — appended to S02 §6 (F4 row: stability fails at
$n \ge 11$ ($\beta = \tfrac12$) and $\beta \le 0.35$; the no-real-exceptionals half
survives and strengthens), dated, per the audit-trail convention. WP08 status → **done**
(dated note in the WP header). Parent snapshot ledger/conjecture rows annotated per README
convention. Future runs regress against the sweep table above (including the six DEVIATION
rows — they are data, not defects).
