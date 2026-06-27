# The Helix Lift & Quaternionic Time — A Phase‑5 Proposal

*Phase‑5 deliverable (see [README](../README.md)). **Status: exploratory /
conjectural.** Unlike the Phase‑1/2 notes, this is a research program, not a
theorem list. The lemmas in §§2,5 are elementary and proved; the quaternionic
positivity and self‑adjointness statements in §4 are **conjectures**, flagged as
such. Quaternion non‑commutativity means "spectrum" and "self‑adjoint" must be
read in the S‑spectrum / slice‑regular sense. Nothing here bears on RH; it only
proposes **where to store** the obstruction that positivity meets.*

---

## 0. Summary

Bochner forces the spectrum $\{\lambda_n\}$ of a circle kernel to be
**nonnegative** for the convolution operator $T_K$ to be positive definite. Two
catalogue objects break this on purpose: the η kernel (alternating signs,
[eta-zeta-transfer.md](eta-zeta-transfer.md) §3) and the zeros↔primes transfer
kernel (its positivity *is* RH). The proposal: when positivity fails, **lift the
unit circle to a helix** so a sign becomes a half‑turn and accumulated negativity
becomes rotation beyond $2\pi$ along an added **time** axis; then identify that
axis with the quaternionic $j$ direction, making $j$ the (conjecturally)
self‑adjoint generator of time.

| | statement | status |
|---|---|---|
| **H1** Cover | the helix $\mathcal H=\{(\cos t,\sin t,t)\}$ is the universal cover of $\mathbb T$; the third axis is the unwrapped winding | proved |
| **H2** Sign = half‑turn | $-a=|a|\,e^{i\pi}$, so each sign flip is a $\pi$ rotation; cumulative flips give a monotone winding $\Rightarrow$ "negatives = rotation past $2\pi$" | proved |
| **H3** η winding | on $s=\tfrac12+ib$ the eta phase $\Theta_n=\pi(n-1)-b\log n\to\infty$; even (negative) $n$ sit on odd half‑turns | proved |
| **H4** $j$ = time | the helix lifts to $e^{jt}=\cos t+j\sin t$; $D_t=-j\partial_t$ is self‑adjoint on the quaternionic module and restores the cone $z^2-(p^2+g^2)\ge0$ | **conjecture** |

---

## 1. The problem positivity leaves open

For a real even kernel $K(\theta)=\sum_n\lambda_n e^{in\theta}$ on
$\mathbb T=\mathbb R/2\pi\mathbb Z$, the convolution operator $T_K$ is
self‑adjoint, and **positive semidefinite iff every $\lambda_n\ge0$** (Bochner;
see [README](../README.md) "The setting"). When some $\lambda_n<0$ the operator is
still self‑adjoint but indefinite, and the circle/RKHS geometry is lost. Rather
than accept a signed spectrum, we re‑encode the sign as geometry on a larger
space.

---

## 2. The helix as the universal cover

> **Lemma H1 (universal cover).** The map $p:\mathbb R\to\mathbb T$,
> $t\mapsto e^{it}$, is the universal covering of the circle, realised
> geometrically as the helix
> $\mathcal H=\{(\cos t,\sin t,t):t\in\mathbb R\}\subset\mathbb C\times\mathbb R_t$.
> The fibre $p^{-1}(e^{i\theta})=\{\theta+2\pi k:k\in\mathbb Z\}$ is indexed by the
> **winding number** $k$; the third coordinate $t$ is the unwrapped phase, which we
> identify with **time**.

*Proof.* $p$ is a surjective local homeomorphism with $\mathbb R$ simply
connected; the deck group is $2\pi\mathbb Z$ acting by translation. The graph map
$t\mapsto(\cos t,\sin t,t)$ is a homeomorphism $\mathbb R\to\mathcal H$ commuting
with $p$ and the projection to the first two coordinates. $\;\blacksquare$

> **Lemma H2 (sign is a half‑turn; negativity is winding).** For $a\in\mathbb R$,
> $a=|a|\,e^{i\pi\,[a<0]}$. Given a sampled real signal $R_0,R_1,\dots$, let
> $f_m=\#\{0\le i<m:\operatorname{sgn}R_{i+1}\ne\operatorname{sgn}R_i\ne0\}$ be the
> cumulative count of sign flips. The **sign‑aware phase**
> $\Phi_m=\omega_m+\pi f_m$ is non‑decreasing, lifts $R_m$ to the helix point of
> radius $|R_m|$ at height $\Phi_m$, and crosses every multiple of $2\pi$ as flips
> accumulate. Hence a run of negative values is literally **rotation beyond
> $2\pi$**, while the radius $|R_m|\ge0$ restores positivity as amplitude.

*Proof.* $a=|a|e^{i\pi}$ when $a<0$ and $a=|a|e^{i0}$ when $a>0$; a sign change is
multiplication by $e^{i\pi}$. $f_m$ is non‑decreasing by construction, so
$\Phi_m=\omega_m+\pi f_m$ is non‑decreasing and unbounded whenever flips are
infinite; the helix point $(|R_m|\cos\Phi_m,|R_m|\sin\Phi_m,\Phi_m)$ projects to
$|R_m|e^{i\Phi_m}$ on $\mathbb T$. $\;\blacksquare$

A one‑parameter family $K_\varepsilon$ (mollifier width, or the cumulative
spectral measure $\int_0^\omega$) sweeps a sheet $\mathcal H\times\{\varepsilon\}$
— the **multi‑dimensional framework over time**.

---

## 3. The sign‑aware lift (constructive definition)

> **Definition H3 (sign‑aware helix lift).** Given a real signal $R(\omega)$ on a
> grid, set
> $$\operatorname{amp}(\omega)=|R(\omega)|,\qquad
> \Phi(\omega)=\omega+\pi\,f(\omega),\qquad
> (x,y,z)=(\operatorname{amp}\cos\Phi,\ \operatorname{amp}\sin\Phi,\ \Phi),$$
> with $f(\omega)$ the cumulative sign‑flip count of $R$ (zeros forward‑filled to
> the previous nonzero sign). This is implemented in
> [prime-zeros.py](../victor/prime-zeros.py) (`sign_aware_helix`).

The naive helix of the original script ($x=R\cos\omega,\ y=R\sin\omega,\ z=\omega$)
folds a negative $R$ onto the *same* height with a flipped radius; Definition H3
instead spends the sign as a genuine $\pi$ of climb, so the lift is single‑valued
and monotone in height.

---

## 4. Quaternionic time: $j$ as the self‑adjoint generator

[spectral-triple.html](../victor/spectral-triple.html) §9 embeds the three real channels of
the explicit formula as a quaternion; here we adopt the sign convention
$$\mathbf K=Z-iP+jG\in\mathbb H\qquad(\text{zeros, primes, Gamma}),$$
so the $i$‑channel carries $-P$ and $\mathbf K$ mirrors the signal $R=Z-P+G$
exactly. (The manuscript writes $+iP$; the cone $z^2-(p^2+g^2)\ge0$ of
Theorem 9.1 is unchanged, depending only on $P^2$.) Promote the helix (time) axis
to the quaternionic $j$:

> **Conjecture H4 ($j$‑time and positivity restoration).**
> 1. The helix lift is the quaternionic exponential $t\mapsto e^{jt}=\cos t+j\sin t$
>    in the $(1,j)$‑plane of $\mathbb H$, so winding past $2\pi$ is motion on the
>    $j$‑circle, *distinguishable* from the spectral phase on the $i$‑circle.
> 2. The generator of time translation is $D_t=-\,j\,\partial_t$, the quaternionic
>    analogue of the self‑adjoint momentum $-i\partial_x$; on the appropriate
>    quaternionic Hilbert module (with the S‑spectrum spectral theorem) $D_t$ is
>    self‑adjoint. "**$j$ is the self‑adjoint operator kernel of time**" = the
>    convolution kernel implementing winding‑shift is built from $j$ and is
>    self‑adjoint.
> 3. An indefinite circle kernel $T_K$ lifts to a helix kernel that acquires a
>    positive $j$/time component (the $G$ channel), restoring the cone
>    $z^2-(p^2+g^2)\ge0$; Bochner's circle case is recovered as **zero winding**.

These are conjectures: the right framework is quaternionic spectral theory
(S‑spectrum, slice‑regular functions), where left/right eigenvalues and a genuine
self‑adjoint spectral theorem require care. Parts of (1)–(2) may be provable as
stated; (3) is the substantive open claim.

---

## 5. Worked micro‑example: the Dirichlet eta function

> **Lemma H3′ (eta phase winds past $2\pi$).** On the critical line $s=\tfrac12+ib$
> the eta term is $(-1)^{n-1}n^{-1/2}e^{-ib\log n}$ with cumulative phase
> $$\Theta_n=\pi(n-1)-b\log n.$$
> Then $\Theta_n\to+\infty$, crossing every $2\pi k$. The **negative** terms are
> the even $n$ (sign $(-1)^{n-1}=-1$), whose half‑turns land on **odd** multiples
> of $\pi$.

*Proof.* $\pi(n-1)$ dominates $b\log n$, so $\Theta_n\to\infty$ monotonically for
large $n$ and passes every level. Parity of $(-1)^{n-1}$ is the parity of $n-1$.
$\;\blacksquare$

Reading this on the helix:

- $\Theta_n\in 2\pi\mathbb Z$ — term is **real and positive** (a full number of
  turns);
- $\Theta_n\in\pi+2\pi\mathbb Z$ — term is **real and negative**: the "real‑valued
  (imaginary‑part) terms" that wound an odd half‑turn past a $2\pi$ multiple;
- the $-b\log n$ drift offsets generic terms off the real axis — **complex‑valued
  offsets around the $2\pi$ multiples.**

So the η kernel — *indefinite* on the circle ([eta-zeta-transfer.md](eta-zeta-transfer.md)
§3) — becomes single‑valued once the winding is restored, and the $j$‑axis carries
exactly the parity the circle folded away.

---

## 6. Numerical experiment

Implemented in [prime-zeros.py](../victor/prime-zeros.py) (Phase‑5 first step). The script:

1. computes the three channels $Z,P,G$ separately and the signal $R=Z-P+G$;
2. builds the **sign‑aware helix** (Definition H3) and reports the total winding
   $\Phi_{\max}/2\pi$ and the number of sign flips;
3. forms the **spectral quaternion** $Z-iP+jG$ (i‑channel $=-P$, mirroring $R$)
   and its **cone indicator**
   $Z^2-(P^2+G^2)$, reporting whether it stays $\ge0$;
4. plots (if `matplotlib` present) the sign‑aware helix coloured by
   $\operatorname{sgn}R$ and the cone indicator vs. $\omega$.

| quantity | meaning | check |
|---|---|---|
| sign flips of $R$ | how many half‑turns the lift adds | matches red segments in the plot |
| $\Phi_{\max}/2\pi$ | total winding (turns) | $> $ naive $\omega_{\max}/2\pi$ when $R$ changes sign |
| $\min(Z^2-P^2-G^2)$ | quaternion cone (Thm 9.1) | $\ge0 \Rightarrow$ in cone with this truncated data |

*(This is an illustration on truncated data — 10 zeros, prime powers $\le100$ — not
a test of RH.)*

---

## 7. Scope and honest limits

- **Proved.** H1–H3 and H3′ are elementary and complete: the helix is the
  universal cover, a sign is a half‑turn, accumulated negativity is winding past
  $2\pi$, and the eta phase realises this concretely.
- **Conjectural.** H4 (parts 2–3 especially): the self‑adjointness of $D_t=-j\partial_t$
  and the cone‑restoration claim are open and require the S‑spectrum framework.
  The eta reading in §5 is illustrative, not a theorem about $\zeta$.
- **No RH claim.** Lifting to the helix **relocates** the positivity obstruction
  into the winding/time channel; it does not remove it. The zeros↔primes case
  stays exactly as hard as RH.
- **Standard / external results used.** Covering‑space theory; Bochner's theorem
  on $\mathbb T$; quaternionic spectral theory (S‑spectrum, slice‑regular
  functions — Colombo–Sabadini–Struppa).
