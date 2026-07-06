# A Prime Sieve on the Adèle Class Space — Implementation Index

*Working notes turning the research program of
[prime-sieve-adele-plan.html](prime-sieve-adele-plan.html) into staged, testable tasks.*

*Started 4 July 2026.*

The plan proposes to **construct** a Hilbert–Pólya operator directly: build a finite,
self-adjoint "Sieving Laplacian" $H_n$ from the composite-generator sieve on the dyadic
block $I_n = [2^n, 2^{n+1}-1]$, and argue its spectrum converges — after affine rescaling —
to the imaginary parts of the nontrivial zeros of $\zeta$.

These notes break that program into five phases, one file each, and — per the repository
[rigour convention](../CLAUDE.md) — tag every claim **proven** / **conditional** /
**heuristic**. Where a phase is numerically testable, a runnable check lives in
[sieve_operator.py](sieve_operator.py); the tables quoted in the phase notes are its verbatim
output (`python adele/sieve_operator.py`).

## Phases

| # | File | Plan §§ | Core object | Status |
|---|---|---|---|---|
| 1 | [phase1.md](phase1.md) | §2 | Composite-generator sieve; equidistribution $\widehat\mu_n(k)=O_k(1/\log M_n)$ | **proven** (numerics confirm) |
| 2 | [phase2.md](phase2.md) | §3 | Embedding integers $\to$ idèle classes in $X=\mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times$ | conceptual / heuristic |
| 3 | [phase3.md](phase3.md) | §4 | Sieving Laplacian: Def 4.1 vacuous, **corrected** to $H_n'=D_n'+\varepsilon_n A'$ (Def 3.2, $A'\ne0$, $\varepsilon_n=c/\lVert A'\rVert$) | **corrected** — non-vacuous; its role is the *trace*, not eigenvalues |
| 4 | [phase4.md](phase4.md) | §5–6, §8 | Conj 5.1 (eigenvalues→zeros) **restated** as trace convergence (Thm 4.1/4.2) | **corrected** — non-vacuous trace statement, **proven** |
| 5 | [phase5.md](phase5.md) | §7 | Hecke / Langlands enrichment on $\mathrm{GL}_1$ | exploratory |
| 6 | [phase6.md](phase6.md) | — (new) | **The fix:** sieve *in* adèle space — Connes trace formula, place by place | **proven** + verified to $10^{-36}$ |
| 7 | [phase7.md](phase7.md) | — (new) | **The zero side:** what a non-Weil equivalence needs; why "sieve bridge $+$ Weil" is circular | frontier — Cor 5.4 **proven** but **RH-equivalent** |

## Critical review (read before implementing)

The program is worth staging. Two problems were found by *running* the construction, not by
reading it — and **both have since been corrected**, non-vacuously, below. Diagnosis and
correction are recorded together, honestly, per the [repository rule](../CLAUDE.md) against
asserting a framework implies RH unless it is provably tied to the zeros.

**(A) Definition 4.1 was vacuous as written — the coupling matrix is identically zero.**
The plan takes the operator basis to be $V_n = \{\text{primes } p \in I_n\}$ and builds the
off-diagonal $A_{p,q}=\sum_{m\in W_n} a_p(m)a_q(m)/\mathrm{rad}(m)$ from composites $m\in I_n$.
But a composite $m\in[2^n,2^{n+1})$ **cannot** have two distinct prime factors $p,q$ that are
both $\ge 2^n$: their product alone would be $pq \ge 2^{2n} \gg 2^{n+1}$. Hence *no* composite
in $I_n$ contributes an off-diagonal term, $A\equiv 0$, and $H_n = D_n = \mathrm{diag}(\log p)$
exactly. The claimed "level repulsion that shifts $\log p$ to the zeros" never occurs. This is
confirmed numerically: `||A||_op = 0.0000` for every $n$ tested, and the spectrum is completely
insensitive to $\varepsilon$ (`mean|shift| = 0.000000` for $C\in\{0,\dots,10\}$). See
[phase3.md](phase3.md). **Corrected (Def 3.2):** take the basis to be the primes $p<2^n$ that the
composites in $I_n$ are actually built from; then $A'\ne0$ genuinely (norms below), and with the
consistent scaling $\varepsilon_n=c/\lVert A'\rVert$ the operator is non-vacuous and well defined.

**(B) Even corrected, the spectrum has the wrong density to be the zeros — so the *target* is restated to the trace.**
The corrected operator has a genuinely nonzero coupling ($\lVert A'\rVert_{\mathrm{op}}
= 9.3, 19.5, 36.3, 64.7$ for $n=8,10,12,14$ — which is exactly why $\varepsilon_n=c/\lVert
A'\rVert$, not $1/\log M_n$, is the forced scaling). But a deeper obstruction remains, independent
of any scaling: the diagonal spectrum $\{\log p\}$ has **exponential**
counting density $N_A(T)\sim e^T/T$, whereas the zeros have **logarithmic** density
$N(T)\sim\frac{T}{2\pi}\log\frac{T}{2\pi}$. The companion note
[prime-side.md](prime-side.md) (Prop 3.7) *proves* no unitary conjugation or affine rescaling
can reconcile these. Our unfolding experiment confirms it: the best affine fit of $\mathrm{Spec}
(H_{14})$ to the first 1612 zeros has RMS residual $14.7$ — as large as $\gamma_1$ itself.

**What this means for the program.** The explicit formula pairs the two spectra through a
*Fourier transform*, not a bijection (prime-side.md §4). So the honest target is not "the
eigenvalues of $H_n$ are the zeros" but "the *trace* reproduces the prime side of the
Guinand–Weil formula." That trace identity **is** already established unconditionally in
[prime-side.md](prime-side.md) (Theorem 3.4, Corollary 4.2). The value this program can still add
is *constructive*: producing that trace stage-by-stage from the sieve with a controlled error
(prime-side.md Prop 6.1).

**The fix — [phase6.md](phase6.md).** Producing that trace does **not** work as a finite matrix:
$\mathrm{Tr}\,g(H_n')$ of the repaired operator *diverges* with the matrix dimension
($16.7\to 632.6$ as $n:8\to14$) and never approaches the arithmetic side (constant $0.603035$),
because the explicit-formula trace is a sum of **local distributions, one per place of
$\mathbb Q$**, not a sum over a spectrum. Phase 6 therefore does the sieve *in* the adèle class
space $X=\mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times$ à la Connes: each prime is a place contributing a
$p$-adic principal-value term $W_p(g)=2\sum_k \frac{\log p}{p^{k/2}}g(k\log p)$, the sieve
enumerates the places, and the assembled geometric side balances the zero side to $10^{-36}$ with
a proven $O(M_n^{-1/2})$ truncation rate ([adele_trace.py](adele_trace.py)).

**Bottom line.** Phase 1 is solid and proven. Phase 2 is a reasonable conceptual dictionary.
Phase 3 is **corrected**: the vacuous Def 4.1 becomes the non-vacuous, correctly-normalised
$H_n'=D_n'+\varepsilon_n A'$ (Def 3.2, $\varepsilon_n=c/\lVert A'\rVert$), whose role is the trace,
not eigenvalues ([phase3.md](phase3.md)). Phase 4 is **corrected**: Conjecture 5.1's refuted
eigenvalue→zero claim is restated as the **proven** trace-convergence statement (Thm 4.1/4.2,
[phase4.md](phase4.md)). Phase 5's Phase 3–4 gate is now cleared. **Phase 6 is the working
construction**: the sieve, in adèle space, produces the correct trace at the correct rate — what
the program was really after. It reproduces, does not decide, RH. **Phase 7** explains why that
ceiling is structural, not incidental: the sieve's only bridge to the zeros is the flow character
$\chi_W$, whose zeros are reached by the same analytic continuation that *is* the Weil explicit
formula — so "sieve bridge $+$ Weil" is circular. What the zero side genuinely needs — an intrinsic
self-adjoint / positive realisation on a *new* Hilbert space — is RH-equivalent and undecided
([phase7.md](phase7.md)).

## Reproducing the numbers

```bash
cd victor
source .venv/bin/activate            # numpy + mpmath
python adele/sieve_operator.py       # Phases 1,3,4: sieve, H_n, repair, repaired trace
python adele/adele_trace.py          # Phase 6: adelic place-by-place Weil trace + balance
```

## Related documents in this folder

- [prime-side.md](prime-side.md) — the rigorous, unconditional "prime side" package (space,
  kernel, flow, generator, weights, trace identity, boundary law). The gold-standard the phase
  notes are measured against.
- [prime-kernel.html](prime-kernel.html) — the three RKHS ingredients.
- [prime-sieve-adele.html](prime-sieve-adele.html) / [prime-sieve-adele-plan.html](prime-sieve-adele-plan.html)
  — the source program these notes implement.
