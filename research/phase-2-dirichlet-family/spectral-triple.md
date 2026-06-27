# Spectral Triple / RH Framework — Phase 2b

*Full note at [project/spectral-triple.md](../../project/spectral-triple.md).*

*Status: **transfer operator implemented and numerically verified** ([victor/spectral-triple-verify.py](../../victor/spectral-triple-verify.py)). The defining trace identity (Weil explicit formula) is verified to ~40 digits; the positivity ↔ RH step (Conjecture 6.1 = Weil's criterion) remains **conditional**.*

---

## The construction (as implemented)

The spectral transfer operator $T$ couples the **prime numbers** to the **imaginary parts $\gamma$ of the zeta zeros**, on the critical line $\Re s = \sigma = \tfrac12$.

Pick an even test function $\phi$; its autocorrelation $f=\phi\star\tilde\phi$ has $\widehat f=|\widehat\phi|^2\ge0$. The **trace identity of $T$** is the Weil–Guinand explicit formula

$$\underbrace{\sum_\gamma \widehat f(\gamma)}_{\text{ZERO side}}=\underbrace{2\,\widehat f(\tfrac{i}{2})}_{\text{pole}}-\underbrace{2\sum_n\frac{\Lambda(n)}{n^{\sigma}}\,f(\log n)}_{\text{PRIME side},\ \sigma=\tfrac12}+\underbrace{\frac{1}{2\pi}\int_{\mathbb R}\widehat f(r)\,\Re\,\psi\!\bigl(\tfrac14+\tfrac{ir}{2}\bigr)\,dr-f(0)\log\pi}_{\text{archimedean}}.$$

The prime weight $n^{-\sigma}=n^{-1/2}$ **is** "real part $\tfrac12$"; the archimedean shift $\tfrac14=\sigma/2$ is the self-dual point of the functional equation. $T$ is convolution by $K=Z-P+G$, whose signed spectral measure these atoms balance.

## Status

| Result | Status |
|---|---|
| Transfer identity (trace identity of $T$) at $\sigma=\tfrac12$ | **Verified** (~40 digits, exact zeros) |
| Weil positivity functional $W(\phi)\ge0$ from arithmetic side | **Verified** (RH-consistent) |
| Real-part sensitivity: off-line $\beta\ne\tfrac12$ lowers $W$ | **Verified** (closed form, ~1e-44) |
| Conjecture 6.1: $W\ge0\ \Leftrightarrow$ RH (Weil's criterion) | **Conditional** (cite Weil 1952, Bombieri) |
| Raw geometric cone $z^2-(p^2+g^2)\ge0$ | **Refuted as a faithful criterion** (normalization-dependent; goes negative) |
| Zero kernel positive definite (unconditional) | **Holds** ($\gamma_n>0$, Bochner) |
| Effective bound: verification up to $\omega=T$ → no zeros below $T$ | **Open** |
| $T_\varepsilon$ spectrum as $\varepsilon\to0$ | **Open** |

## Numerics (implemented)

[victor/spectral-triple-verify.py](../../victor/spectral-triple-verify.py) — four checks against exact zeros from `mpmath.zetazero`:

1. **Transfer identity** (unconditional): ZERO side $=$ PRIME $+$ archimedean side; worst $|\text{diff}|\sim3\times10^{-41}$ over Gaussian widths $\alpha\in\{0.02,0.05,0.1,0.15\}$.
2. **Weil functional** $W(\phi)$ computed from primes $+\Gamma$ only (never touching the zeros); $W\ge0$ for every tested $\phi$, matching the zero side to $\sim4\times10^{-41}$.
3. **Real-part sensitivity**: $D(\beta)=2e^{-\alpha\gamma^2}\!\bigl(e^{\alpha\delta^2}\cos(2\alpha\gamma\delta)-1\bigr)$, $\delta=\beta-\tfrac12$; $D(\tfrac12)=0$, $D<0$ for $\beta\ne\tfrac12$ — positivity has teeth exactly at $\sigma=\tfrac12$.
4. **Channel/cone tie-in**: `prime-zeros.py` $Z,P,G$ and `quaternion_cone`. The raw indicator goes strongly negative here (dense prime bumps make $P\gg Z$): it is normalization-dependent and **not** a faithful RH criterion — the rigorous positivity is the Weil functional (check 2).

## Open actions

- [x] Implement the transfer operator between primes and zeros at $\sigma=\tfrac12$; verify the trace identity numerically.
- [ ] Restate Conjecture 6.1 as a conditional: the unconditional part is the trace identity (verified); the RH-equivalent part is Weil's positivity criterion. Cite Weil (1952), Bombieri (Clay exposition), Connes (1999) for the spectral interpretation.
- [ ] Survey Bombieri–Lagarias zero-free regions via explicit formulas; add to the open-questions section.
- [ ] Correct §8 of the project note: the raw geometric cone indicator is not $\ge0$ under `prime-zeros.py` normalization; replace the positivity claim with the Weil functional.
