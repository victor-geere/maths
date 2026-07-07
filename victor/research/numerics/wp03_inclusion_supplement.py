"""wp03_inclusion_supplement.py — PSC2-WP03 (E2) post-hoc supplement: the n = 12
fine-grid certified floor.

STATUS (disclosed): POST-HOC SUPPLEMENTARY MEASUREMENT, not part of the
pre-registered wp03_inclusion.py run.  That run's mechanical branch rule returned
INDETERMINATE for a disclosed operationalisation artifact: the pre-registered n = 12
grid step h = 5.0 (whose stated role was agreement with n = 10) makes the Lipschitz
floor c_12 = (grid min) - h/2 vacuous by construction (h/2 = 2.5 exceeds any
conceivable floor), and the branch rule's min ran over ALL stages.  This supplement
computes the n = 12 profile on the SAME fine grid as the n <= 10 stages
(lambda = 0(0.5)50), so that c_12 is certified by the identical grid + 1-Lipschitz
argument.  Nothing else changes; the pre-registered verdict stands as reported in
PSC2-F09; this number is filed alongside it, labelled post hoc.

Deterministic (no RNG).  Run:  python wp03_inclusion_supplement.py
"""

import time

import numpy as np

import wp02b_rewindow as w1              # noqa: F401  (dps 35 side effect)
import wp04_certified_enclosures as wp04
import wp03_inclusion as w3

if __name__ == "__main__":
    t0 = time.time()
    print("=" * 78)
    print("WP03 SUPPLEMENT (post hoc, disclosed) — n=12 fine-grid floor, h = 0.5")
    print("=" * 78)
    st = wp04.build_w1_stage(12)
    B, Q, maps, s_pos, dropped = wp04.build_pencil(st)
    h = w3.GRID_H
    lams = np.arange(0.0, w3.WINDOW + h / 2, h)
    rr = np.empty(len(lams))
    for i, la in enumerate(lams):
        rr[i] = w3.r_of_lambda(B, Q, la)
        dd = w3.dist_spec(s_pos, la)
        assert dd <= rr[i] + 1e-6 * (1 + la), "T-a violated (Lemma 1) — code bug"
    bands = [float(np.median(rr[(lams >= lo) & (lams < hi)]))
             for lo, hi in zip(w3.BANDS[:-1], w3.BANDS[1:])]
    amin = lams[int(np.argmin(rr))]
    print(f"  [W1] n=12  dim={B.shape[0]} (dropped {dropped})  grid h={h:.1f} "
          f"({len(lams)} points)   [{time.time() - t0:7.1f}s]")
    print(f"       r_12 on [0,50]:  min={rr.min():7.4f} (argmin lambda={amin:5.1f})  "
          f"certified floor c_12 = min - h/2 ={rr.min() - h / 2:7.4f}")
    print(f"       bands [0,15|15,30|30,50] median = "
          f"{bands[0]:7.4f} {bands[1]:7.4f} {bands[2]:7.4f}")
    print(f"       [n=10 fine-grid comparators: min = 0.9832, floor = 0.7332, "
          f"bands = 2.6623 1.7673 1.4596]")
    ok = rr.min() - h / 2 >= w3.FLOOR_BAR
    print(f"  supplement conclusion: c_12 = {rr.min() - h / 2:.4f} "
          f"{'>=' if ok else '<'} {w3.FLOOR_BAR} — the fine-grid floor is "
          f"{'certified at n=12 as well' if ok else 'NOT certified at n=12'}")
