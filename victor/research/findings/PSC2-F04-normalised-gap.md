# PSC2-F04 — WP07: census to $n = 15$ (stable, no drift) and the uniform normalised-gap theorem (G3 base theorem, proven)

*Finding note. Date: 2026-07-07. Work package:
[PSC2-WP07](../workpackages/PSC2-WP07-normalised-gap.md). Code/run:
`numerics/wp07_gap_census.py` (numpy float64; seed 20260707 used only in the Dobrushin
teeth control — no random draw enters any census value or theorem check). Independent
symbolic checks of the two closed forms used in the proof via the `sympy-verifier` MCP
server (§Proof, Lemma 3). Tags per [PSC2-001](../PSC2-001-conventions.md).*

## Pre-registered criteria (copied verbatim from the WP before the run)

> **Objective.** Prove: $\exists\, c > 0$ with $g_{\mathrm{sym}}(n) \ge c$ for all $n$ — the
> uniform random-walk spectral gap of the bipartite divisor graph $B_n$ (measured stable at
> $\approx 0.54$–$0.57$ for $n = 6\ldots9$).
>
> **Ordering (binding).** 1. Census extension to $n \le 14$ (sparse eigensolvers) **before**
> investing in the proof: drift down kills the conjecture early. 2. Proof attempt: the
> normalised one-mode operator is a doubly-smoothed divisor-correlation form; Perron vector
> explicit to first order; the fluctuation part is a bilinear form over
> $\#\{m \in I_n : pq \mid m\} - 2^n/(pq)$ — Brun–Titchmarsh + Montgomery's large sieve.
>
> **Falsifier.** Census drift; or the bilinear-form estimates capping below a uniform
> constant (record the best $c(n)$ profile either way).

Additional criteria fixed in the script header before any $n \ge 10$ was computed: census
**survives** iff $\min_{4 \le n \le 15} g_{\mathrm{sym}} \ge 0.40$ and the last four stages
are not strictly decreasing; all five theorem-ingredient inequalities (I1–I5 below) must
hold at every computed stage; the Dobrushin teeth controls must behave two-sidedly.

## Regression check

N00 targets reproduced: **yes** — §3 rows $g_{\mathrm{raw}}/g_{\mathrm{sym}} = 0.80627/0.55061,$
$0.78667/0.53722, 0.81016/0.56641, 0.80372/0.56004$ at $n = 6\ldots9$, matched to $2\times10^{-5}$,
with the fast accumulation builder certified against `prime_graph_lab.build_bipartite`'s
one-mode matrix to $10^{-10}$ at those stages (rule I0.5). No $\gamma$-list, no zero data, no
fitted constant anywhere.

## Setting

$P_n = \{p \text{ prime} : p < 2^n\}$, $I_n = [2^n, 2^{n+1})$, $C_n$ = composites in $I_n$.
$W[p,m] = v_p(m)\,p^{-1/2}$ for $p \mid m$; $S = WW^\top$ on $P_n$, i.e.
$S[p,q] = \sum_{m \in C_n} v_p(m)v_q(m)(pq)^{-1/2}$; $d_p = \sum_q S[p,q]$;
$L = D^{-1/2}SD^{-1/2}$. Since $D^{-1}S$ is row-stochastic and similar to $L$, the top
eigenvalue of $L$ is exactly $1$; $g_{\mathrm{sym}}(n) = 1 - \lambda_2(L)$ is the spectral
gap of the reversible chain $P := D^{-1}S$ with stationary law $\pi(q) = d_q/\sum_p d_p$.
Every prime factor of every $m \in C_n$ lies in $P_n$ (if $q \ge 2^n$ divides composite $m$
then $m = qt$, $t \ge 2$, so $m \ge 2^{n+1}$) — the chain is closed on $P_n$.

## Result 1 — the census (deliverable 1; pre-registered verdict: SURVIVES)

```
== WP07 (G3): normalised-gap census n = 4..15 + uniform-gap theorem ingredients ==
   theorem constants: C_d = 45, theta = 2^(-11/2)/C_d^3 = 2.425e-07, proven uniform gap c0 >= theta/2 = 1.212e-07 (n >= 10)
   proof constant A = sum_q q^(-1/2)/(q-1): partial(1e6) = 1.338244, with tail bound <= 1.340244  (proof uses A <= 1.35: True)
[teeth] random reversible: |lam2|=0.0995 <= delta=0.2766: True;   two-block eps=0.001: g_sym=0.00200 < 0.02 (detected): True

    n   |P_n|    g_raw     g_sym     I1>=1     I2<=1     I3>=1     I4>=1     I5<=1
    4      6   0.74243   0.45268     2.750     0.090     4.625   1.318e+06   0.54732
    5     11   0.80297   0.53158     2.125     0.102     5.188   1.644e+06   0.46842
    6     18   0.80627   0.55061     2.312     0.110     5.531   1.800e+06   0.44939  N00: ok
    7     31   0.78667   0.53722     2.094     0.115     5.734   1.795e+06   0.46278  N00: ok
    8     54   0.81016   0.56641     2.047     0.118     5.852   1.966e+06   0.43359  N00: ok
    9     97   0.80372   0.56004     2.008     0.120     5.918   1.989e+06   0.43996  N00: ok
   10    172   0.80588   0.56385     2.035     0.121     5.955   2.040e+06   0.43615
   11    309   0.80480   0.56399     2.014     0.121     5.976   2.067e+06   0.43601
   12    564   0.80389   0.56412     2.005     0.122     5.987   2.088e+06   0.43588
   13   1028   0.80505   0.56576     2.001     0.122     5.993   2.111e+06   0.43424
   14   1900   0.80517   0.56614     2.004     0.122     5.996   2.123e+06   0.43386
   15   3512   0.80472   0.56588     2.003     0.122     5.998   2.130e+06   0.43412

[census] min g_sym over n=4..15: 0.45268 (>= 0.40: True);  last four stages strictly decreasing: False
[census] pre-registered verdict: SURVIVES

WP07 CENSUS + INGREDIENTS PASS
```

The gap does not drift: it **converges** — $g_{\mathrm{sym}}$ is $0.5638, 0.5640, 0.5641,
0.5658, 0.5661, 0.5659$ over $n = 10\ldots15$ (the census exceeded the binding $n \le 14$ by
one stage). The two-block teeth control confirms the metric detects near-disconnection at
$g \approx 2\varepsilon$, so the plateau is not a vacuous artifact of the harness.

## Result 2 — the uniform-gap theorem (deliverable 2)

**Theorem (G3, base form).** For every $n \ge 10$,
$$g_{\mathrm{sym}}(n) \;\ge\; 1 - \sqrt{1 - \theta} \;\ge\; \tfrac{\theta}{2},
\qquad \theta := 2^{-11/2}\,C_d^{-3},\quad C_d := 45,$$
so $g_{\mathrm{sym}}(n) \ge 1.2\times10^{-7}$ for all $n \ge 10$; and $g_{\mathrm{sym}}(n) > 0$
for each $2 \le n \le 9$ (Perron–Frobenius, irreducibility below). Hence
$\inf_{n \ge 2} g_{\mathrm{sym}}(n) > 0$: **the uniform normalised gap exists.** All
constants are explicit and no hypothesis beyond elementary counting is used.

*Proof.*

**Lemma 1 (hub counts).** For every $p \in P_n$: every multiple of $2p$ in $I_n$ is
composite (it is even and $\ge 2^n \ge 4$), and
$N(2p) := \#\{m \in I_n : 2p \mid m\} \ge \max\big(1,\ 2^n/(4p)\big)$. Consequently
$$S[p,2] \;\ge\; (2p)^{-1/2}N(2p) \;\ge\; 2^{-5/2}\,2^n\,p^{-3/2}
\qquad\text{and}\qquad S[2,2] \ge \tfrac12\#\{\text{even } m \in I_n\} = 2^{n-2}.$$
Indeed $I_n$ consists of $2^n$ consecutive integers, and any $2p \le 2^n$ consecutive
integers contain a multiple of $2p$; for $p > 2^{n-1}$, $2p$ itself lies in $I_n$. When
$p \le 2^{n-2}$, $N(2p) \ge 2^n/(2p) - 1 \ge 2^n/(4p)$ (as $2^n/(4p) \ge 1$); when
$p > 2^{n-2}$, $2^n/(4p) < 1 \le N(2p)$. The $p = 2$ case of the first display reads
$S[2,2] \ge 2^{n-4}$, weaker than the second. $\square$

In particular $S[p,2] > 0$ and $S[2,q] > 0$ for all $p, q$, so $P^2 > 0$ entrywise: the
chain is irreducible at every $n \ge 2$, the top eigenvalue of $L$ is simple, and
$g_{\mathrm{sym}}(n) > 0$ for every fixed $n$ — the small-$n$ branch of the theorem.

**Lemma 2 (row-sum upper bound).** For $n \ge 10$ and every $p \in P_n$:
$d_p \le C_d\, 2^n p^{-3/2}$ with $C_d = 45$.

*Proof.* Writing $\sigma(m) = \sum_{q\mid m} v_q(m)q^{-1/2}$ and expanding
$v_p = \sum_{j\ge1}\mathbb 1[p^j \mid \cdot\,]$, $v_q = \sum_{l\ge1}\mathbb 1[q^l \mid \cdot\,]$:
$$d_p = p^{-1/2}\sum_{m \in C_n} v_p(m)\sigma(m)
= p^{-1/2}\sum_{q}\,q^{-1/2}\sum_{j,l\ge1} c(p^j, q^l),$$
$c(a,b) := \#\{m \in C_n: a\mid m,\ b \mid m\} \le 2^n/\mathrm{lcm}(a,b) + 1$, vanishing
unless $\mathrm{lcm}(a,b) < 2^{n+1}$. Split:

*(i) $q \ne p$, main term.* $\sum_{q\ne p}q^{-1/2}\sum_{j,l} 2^n p^{-j}q^{-l}
= 2^n\frac{1}{p-1}\sum_{q \ne p}\frac{q^{-1/2}}{q-1} \le \frac{2A}{p}\,2^n \le \frac{2.7}{p}2^n$,
where $A := \sum_q \frac{q^{-1/2}}{q-1} \le 1.3403 \le 1.35$: the sum over primes
$q \le 10^6$ is $1.338244$ (computed in the run), and the tail is at most
$(1+10^{-6})\sum_{k > 10^6} k^{-3/2} \le (1+10^{-6})\cdot 2\cdot10^{-3}$.

*(ii) $q \ne p$, the $+1$ terms.* These are counted by pairs $(q, l)$ with
$q^l \le X_j := 2^{n+1}p^{-j}$. For $l = 1$: $\sum_{q \le X_j} q^{-1/2} \le 2\sqrt{X_j}$
(integer comparison). For $l \ge 2$: $q \le \sqrt{X_j}$ and $l \le \log_2 X_j$, so the
contribution is $\le 2X_j^{1/4}\log_2 X_j \le 2\cdot2.123\sqrt{X_j}$ (since
$\log_2 X / X^{1/4} \le 4/(e\ln 2) = 2.123$ for $X \ge 1$). Per $j$ this is
$\le 6.25\sqrt{X_j}$, and $\sum_j \sqrt{X_j} = 2^{(n+1)/2}\frac{p^{-1/2}}{1-p^{-1/2}}
\le 3.415\cdot 2^{(n+1)/2} p^{-1/2}$, giving in total
$\le 30.2\cdot 2^{n/2}p^{-1/2} = 30.2\,\frac{2^n}{p}\big(\tfrac{p}{2^n}\big)^{1/2}
\le 30.2\,\frac{2^n}{p}$ (as $p < 2^n$).

*(iii) $q = p$.* $\mathrm{lcm}(p^j, p^l) = p^{\max(j,l)}$ and
$\#\{(j,l): \max = k\} = 2k-1$, so the main part is
$p^{-1/2}\,2^n \sum_{k\ge1}(2k-1)p^{-k} = p^{-1/2}2^n\,\frac{x(1+x)}{(1-x)^2}\Big|_{x=1/p}
\le 6\cdot 2^n p^{-3/2}$ — the closed form $\sum_{k\ge1}(2k-1)x^k = \frac{x(1+x)}{(1-x)^2}$
($|x|<1$) and the bound $\max_{(0,1/2]}\frac{1+x}{(1-x)^2} = 6$ were both verified
independently by the sympy-verifier. The $+1$ part is $\le p^{-1/2}J^2$ with
$J \le (n+1)/\log_2 p$.

Assembling with the outer $p^{-1/2}$:
$$d_p \le (2.7 + 30.2)\,2^n p^{-3/2} \;+\; 6\cdot2^n p^{-2} \;+\; \frac{(n+1)^2}{p(\log_2 p)^2}.$$
Now $6\cdot2^np^{-2} \le 6\cdot2^{-1/2}\,2^np^{-3/2} \le 4.3\cdot2^np^{-3/2}$, and the last
term, against $2^np^{-3/2}$, has ratio $(n+1)^2 p^{1/2}/(2^n(\log_2 p)^2) \le
(n+1)^2 2^{-n/2} \le 3.8$ for $n \ge 10$. Total: $32.9 + 4.3 + 3.8 = 41.0 \le C_d = 45$.
$\square$

**Lemma 3 (Dobrushin).** If a stochastic matrix $K$ satisfies the minorization
$K(p, \cdot) \ge \theta\,\pi(\cdot)$ for all $p$, then every eigenvalue $\lambda \ne 1$
with real eigenfunction satisfies $|\lambda| \le 1 - \theta$.

*Proof.* $\tfrac12\sum_q |K(p,q) - K(p',q)| = 1 - \sum_q \min(K(p,q), K(p',q)) \le 1-\theta$.
If $Kf = \lambda f$ with $f$ nonconstant, pick $p, p'$ attaining
$\mathrm{osc}(f) = f(p) - f(p')> 0$; then
$|\lambda|\,\mathrm{osc}(f) = |\sum_q (K(p,q)-K(p',q))f(q)| \le
\tfrac12\sum_q|K(p,q)-K(p',q)|\cdot\mathrm{osc}(f)$, since replacing $f$ by
$f - \tfrac{\max f + \min f}{2}$ bounds $|f|$ by $\mathrm{osc}(f)/2$ and the difference row
sums to zero. $\square$

**Assembly.** For $n \ge 10$, by Lemmas 1–2:
$$P(p, 2) = \frac{S[p,2]}{d_p} \ge \frac{2^{-5/2}2^np^{-3/2}}{C_d\,2^np^{-3/2}} = \frac{2^{-5/2}}{C_d},
\qquad
P(2, q) = \frac{S[2,q]}{d_2} \ge \frac{2^{-5/2}2^nq^{-3/2}}{C_d\,2^n\,2^{-3/2}} = \frac{q^{-3/2}}{2C_d},$$
$$\pi(q) = \frac{d_q}{\sum_p d_p} \le \frac{C_d\,2^nq^{-3/2}}{S[2,2]} \le \frac{C_d\,2^nq^{-3/2}}{2^{n-2}} = 4C_d\,q^{-3/2}.$$
Hence for all $p, q$:
$$P^2(p,q) \;\ge\; P(p,2)\,P(2,q) \;\ge\; \frac{2^{-5/2}}{C_d}\cdot\frac{q^{-3/2}}{2C_d}
\;\ge\; \frac{2^{-7/2}}{C_d^2}\cdot\frac{\pi(q)}{4C_d} \;=\; \theta\,\pi(q),
\qquad \theta = \frac{2^{-11/2}}{C_d^{3}}.$$
$P$ is reversible, so its spectrum is real with real eigenfunctions; if
$Pf = \lambda f$, $\lambda \ne 1$, then $P^2 f = \lambda^2 f$ with the same nonconstant $f$,
and Lemma 3 applied to the stochastic $P^2$ gives $\lambda^2 \le 1 - \theta$. Therefore
$\lambda_2 \le \sqrt{1-\theta}$ and $g_{\mathrm{sym}} \ge 1 - \sqrt{1-\theta} \ge \theta/2$.
$\blacksquare$

**Numerically:** $\theta = 2.425\times10^{-7}$, proven uniform gap
$c_0 = 1.2\times10^{-7}$ for $n \ge 10$; measured gap $\approx 0.566$. The run verifies
every ingredient at every stage (columns I1–I5 above): the hub lower bound I1 is sharp
within a factor $\approx 2$; the measured row-sum constant is $\approx 5.5$ (I2 ratio
$0.122$ of $C_d = 45$); the Doeblin floor I4 is $\approx 2\times10^6$ below the measured
minorization — the expected price of an eigenvector-blind coupling argument.

**Relation to the WP's suggested route (recorded honestly).** The WP sketched the
sharp-constant route: Perron vector to first order plus a bilinear-form estimate on the
divisor fluctuations $\#\{m: pq \mid m\} - 2^n/(pq)$ via Brun–Titchmarsh/large sieve. The
theorem above settles the *existence* question (the WP's stated objective) by the elementary
hub-minorization route instead — unconditional, all constants explicit, no analytic-number-
theory input. The falsifier branch "bilinear estimates capping below a uniform constant" did
not occur, because no bilinear estimate is needed for existence. Closing the
$c_0 = 10^{-7}$-vs-$0.57$ constant gap is exactly where the WP's machinery belongs, and it
remains **open**, as do the extensions (route α: $c/\log M_n$ for the *non-backtracking* gap
→ P2.4 rung; route β: Bordenave). Per the WP's pricing, no zero-free-region claim is made —
the payoff dictionary activates only if C1/H\* (WP12) lands.

## Verdict against the pre-registered criteria

**Census: SURVIVES** by the mechanical rule (min $0.4527 \ge 0.40$; last four stages not
decreasing — the profile is flat at $0.5638\ldots0.5661$ over $n = 10\ldots15$).
**Proof: the base theorem lands** — $\exists c > 0$ uniform, proven, with explicit
$c = 1.2\times10^{-7}$ for $n \ge 10$ and Perron–Frobenius positivity below. Both
deliverables of the WP are met; neither falsifier branch occurred; the best-$c(n)$ profile
is recorded above either way, as required.

## Tag

- Census $n \le 15$, harness controls, N00 regression: **verified** (two-sided; the teeth
  control detects planted near-disconnection).
- Uniform-gap theorem (Lemmas 1–3 + assembly): **proven** — complete elementary proof above;
  the two closed forms are machine-verified (sympy-verifier: the series identity on $|x|<1$
  and $\max_{(0,1/2]}(1+x)/(1-x)^2 = 6$); the constant $A \le 1.3403$ is a finite computation
  plus an integer-tail bound; all five ingredient inequalities hold empirically at every
  computed stage.
- Sharp constant ($c \approx 0.56$), route α ($c/\log M_n$, non-backtracking), route β:
  **open** (charter H3/H4 extensions; unchanged).

**Scope (do-not list compliance).** This is a statement about the spectral geometry of the
finite sieve divisor graphs — "independently publishable-grade regardless of the zeta
connection", per the WP's own pricing. No claim about zeros, no zero-free region asserted,
no $\gamma$-data consumed. RH remains **open**.

## Propagation

Charter ledger updated: **yes** (T7 → base theorem done, extensions α/β remain; live
conjecture 1 → **proven** in base form; ledger row added). Source doc correction notice
needed: **no** (S02 §7 states G3 as a gate; status lives in the charter ledger per
PSC2-001 §1). WP07 status → base done, extensions open. Parent snapshot ledger annotated
per README convention. Future runs regress against the census table above.
