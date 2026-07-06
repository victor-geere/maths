# Phase 7 — The zero side: what a non-Weil equivalence would need (and why the sieve does not supply it)

*New phase (not in the original plan). Asks precisely what the **zero side** of the explicit
formula must provide so that "prime side $=$ zero side" carries information about the location of
the zeros — **without** the equality being furnished by the Weil explicit formula itself.*

*Status: **heuristic / frontier characterisation**. The equivalences it lands on
([prime-side.md](prime-side.md) Cor 5.4, Weil positivity) are **proven** but **RH-equivalent** —
they mark the frontier and are **not** presented as steps toward a proof. RH stays **open**. No
progress toward a proof is claimed here; the phase's job is to locate the gap exactly.*

Back: [phase6.md](phase6.md) · Index: [index.md](index.md).

## 7.1 The question

Phases 1–6 build the **prime side** unconditionally and, in Phase 6, reproduce the Guinand–Weil
balance adelically to $10^{-36}$. But every such reproduction is honest-to-a-fault about the same
thing: it *reproduces* the explicit formula and therefore **decides nothing** about RH, because the
explicit formula $\sum_\rho h(\gamma_\rho)=[\text{arch}]-\mathrm{Tr}(\mathbb W^{1/2}g(\mathbb A)\mathbb W^{1/2})$
holds whether or not the zeros lie on the line.

So the sharp question is:

> Given the constructed prime side of [prime-side.md](prime-side.md), **what must the zero side
> supply** for "zero side $=$ prime side" to constrain the *location* of the zeros — and can the
> sieve furnish it **without** simply invoking the Weil explicit formula (which is what supplies
> that equality classically)?

## 7.2 Two ways to name the zero side

The zero side $Z(h)=\sum_\rho h(\gamma_\rho)$ can be produced in exactly two ways.

- **(W) The Weil route.** *Define* $Z(h)$ to be $[\text{archimedean}]-\mathcal W_{\mathrm{ar}}(g)$
  via [prime-side.md](prime-side.md) Fact 4.1 / Cor 4.2. Then "prove $Z=$ prime side" is a
  tautology — it is the definition. Crucially, the identity is **true off the line as well as on
  it**: it is an equality of two ways of writing the same contour integral, valid for the zeros
  wherever they are. Hence route (W) alone carries **zero** information about $\{\beta_\rho\}$.

- **(I) The intrinsic route.** Take $Z(h)$ as a sum over the *actual* zero set of $\zeta$,
  reached through the meromorphic continuation of $\zeta'/\zeta$ (argument principle / Hadamard
  product) with **no reference to primes**. This is the only route that can *see* where the zeros
  are — because the zeros are, by definition, features of the continued analytic object.

A non-circular equivalence to RH must build $Z$ by route (I) **and** equip that construction with a
structural constraint that pins $\beta_\rho=\tfrac12$. Route (W) can never do this on its own.

## 7.3 The sieve's bridge is $\chi_W$ — and the explicit formula is *one* contour integral of $h\chi_W$

The new connection the sieve provides is not a new theorem; it is already
[prime-side.md](prime-side.md) **Theorem 5.3**. The prime-side **weighted flow character**
$$
\chi_W(z)\;=\;\mathrm{Tr}\big(W e^{izA}\big)\;=\;\sum_{q\in\mathcal Q}\Lambda(q)\,q^{-\frac12+iz}\;=\;-\frac{\zeta'}{\zeta}\Big(\frac12-iz\Big)
$$
is a **trace of the sieve's own data** (von Mangoldt weights on prime powers), holomorphic for
$\mathrm{Im}\,z>\tfrac12$, and its meromorphic continuation has simple poles **exactly at the
zeros**, at $z_\rho=-\gamma_\rho+i(\beta_\rho-\tfrac12)$ (plus $z=\tfrac{i}{2}$ from $\zeta$'s pole
and the trivial-zero poles).

**Observation 7.1 (the two "bridges" are one contour integral). — proven (re-expression of Fact 4.1 via Thm 5.3).**
For admissible even $h$ (Fact 4.1), the Guinand–Weil explicit formula is precisely the residue
calculus of $h(z)\,\chi_W(z)$:

- on the half-plane $\mathrm{Im}\,z>\tfrac12$, $\chi_W$ **is** the convergent prime-power series,
  so pairing $h$ against it there yields the **prime side** $\mathcal W_{\mathrm{ar}}(g)=
  \mathrm{Tr}(\mathbb W^{1/2}g(\mathbb A)\mathbb W^{1/2})$ (Thm 3.4 / Def 3.5);
- continuing the contour **across** $\mathrm{Im}\,z=\tfrac12$ collects the residues at the poles:
  at $z=\tfrac{i}{2}$ the pole term $h(\tfrac{i}{2})+h(-\tfrac{i}{2})$, at the $z_\rho$ the **zero
  side** $-\sum_\rho h(\gamma_\rho)$, at the trivial zeros the $\Gamma$/archimedean term.

Equating the two evaluations of the *same* integral is the explicit formula (Fact 4.1; standard
contour argument, Montgomery–Vaughan Thm 12.13, Iwaniec–Kowalski Thm 5.12).

**One function, $\chi_W$; one operation, the contour shift.** "Connect primes to zeros via the
sieve" (read $\chi_W$'s poles) and "use Weil to prove prime $=$ zero" (shift $\chi_W$'s contour)
are therefore **not two independent facts to be combined** — they are the same analytic
continuation of $\zeta$, done once.

## 7.4 The circularity, stated precisely

Suppose one tried to execute the plan of the question: (a) let the sieve connect primes to zeros,
then (b) use Weil to prove the two sides equal, and read off a new equivalence.

- The sieve delivers $\chi_W$ **only on $\mathrm{Im}\,z>\tfrac12$** (that is where the trace
  converges). The zeros are *not present* there; they are the poles that appear **after**
  continuation.
- The only thing that produces the zeros from $\chi_W$ is analytic continuation across
  $\mathrm{Im}\,z=\tfrac12$ — which is exactly the content of step (b).

So step (a) does not stand on its own before step (b): there is no independent "prime $\to$ zero"
map to which Weil is then applied. Step (b) *is* step (a). The construction closes a loop of unit
length and yields the explicit formula back — true on the line or off it — hence **no constraint on
$\{\beta_\rho\}$**. This is the same trap catalogued in [prime-side.md](prime-side.md) Reading 4.3
("proven equivalent to RH, not a route around it") and in [../flawed/](../flawed/) (the discarded
`barry-keating-hp-*` series, refuted for exactly this class of hidden circularity).

## 7.5 What the zero side must actually supply (and its RH-equivalent cost)

For "$Z=$ prime side" to pin the zeros, the zero side must be built by route (I) **carrying a
structural constraint that forces $\beta_\rho=\tfrac12$**. Equivalently, in the $z$-plane
(Thm 5.3), it must force **every zero-pole $z_\rho$ of $\chi_W$ to be real**. Three known ways to
impose that, all provably **RH-equivalent**:

| Extra structure on the zero side | Forces | Status |
|---|---|---|
| **Self-adjoint $H$** on a *new* Hilbert space with $\sigma(H)=\{\gamma_\rho\}$ and $Z(h)=\mathrm{Tr}\,h(H)$ (Hilbert–Pólya) | spectrum real $\Rightarrow\beta_\rho=\tfrac12$ | **RH-equivalent**; by Prop 3.7 the space is *not* the prime side re-coordinatised — it must be a genuinely new object |
| **Weil positivity** $\sum_\rho h(\gamma_\rho)\ge0$ for $h=\lvert\widehat\phi\rvert^2$-type (Weil 1952) | poles real | **RH-equivalent**; by Cor 4.2 this is a positivity statement *about the prime-side trace* + arch terms |
| **de Branges / Hermite–Biehler** structure function for $\xi$ | zeros on the line | **RH-equivalent** |

The common feature: each supplies a property the *bare* continuation of $\chi_W$ does **not** have.
The explicit formula gives $Z=$ prime side; **self-adjointness/positivity would give $Z\ge0$ with
real support** — and that "$\ge0$ with real support," not the equality, is where RH lives.

**Corollary 7.2 (the equivalence already lives on the prime side, and is RH-equivalent). — proven equivalence, imported.**
By [prime-side.md](prime-side.md) Cor 5.4, RH $\iff$ $\chi_W$ continues holomorphically to
$\{\mathrm{Im}\,z>0\}\setminus\{\tfrac{i}{2}\}$ $\iff$ every zero-pole $z_\rho$ is real. So the
zero-side requirement of §7.5 translates into a **pure prime-side regularity statement** about the
already-constructed $\chi_W$ — but it is a *restatement of* RH, not a reduction of it.

## 7.6 The honest statement

The conditional in the question — *"if the sieve gives a new prime$\to$zero bridge and Weil then
proves equality, state that"* — has an antecedent whose two clauses are the **same** analytic step
(§7.3–7.4). So the honest output is:

> **What is true and provable (Obs 7.1):** the sieve's flow character $\chi_W$ unifies both
> "bridges" into a single object; the explicit formula is the residue theorem for $h\chi_W$.
> **What cannot be asserted:** any equivalence to RH *beyond* the RH-equivalent Cor 5.4 / Weil
> positivity — because the equality "$Z=$ prime side" holds independently of where the zeros are.
> **What the zero side genuinely needs:** an intrinsic (route-I) realisation of $Z$ as a positive
> trace of a self-adjoint operator on a **new** space (Prop 3.7), or an equivalent positivity/de
> Branges structure — the classical Hilbert–Pólya gap, **RH-equivalent and undecided**.

This is consistent with the whole track: Phase 6 reproduces the formula; Phase 7 explains why
reproduction cannot be upgraded to a decision by pairing the sieve with Weil, and names exactly the
missing ingredient. **It reproduces, and locates — it does not decide — RH.**

## 7.7 Task status

| Task | Status |
|---|---|
| State the zero-side question precisely | ✓ (§7.1) |
| Weil route vs intrinsic route | ✓ (§7.2) — route (W) carries no zero-location information |
| Sieve bridge $=$ $\chi_W$; explicit formula $=$ residues of $h\chi_W$ | **proven** (Obs 7.1, re-expressing Fact 4.1 via Thm 5.3) |
| Circularity of "sieve bridge $+$ Weil" | ✓ (§7.4) — the two clauses are one continuation |
| What the zero side must supply | ✓ (§7.5) — self-adjoint / positive / de Branges, all **RH-equivalent** |
| Prime-side translation | **proven equivalence** (Cor 7.2 $=$ Cor 5.4), **RH-equivalent** |
| A self-adjoint $H$ with $\sigma(H)=\{\gamma_\rho\}$ on a new space | **open / undecided** ($=$ RH) — not obtainable from the prime side (Prop 3.7) |

**Bottom line.** The zero side needs an *intrinsic, self-adjoint (or positive) realisation on a new
Hilbert space*; the sieve provides only $\chi_W$, whose zeros are reached by the very continuation
that *is* the Weil explicit formula. Pairing the two is circular and reproduces — does not decide —
RH. The equivalence that survives (Cor 5.4) is **RH-equivalent**, and per the repository
[rigour convention](../CLAUDE.md) is not a step toward a proof.
