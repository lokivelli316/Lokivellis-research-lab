# v0.2 Derivation Ledger

Status: **HOLD — derivation repair in progress.**

## Frozen input

The v0.1 conceptual structure is immutable for this pass. The job is to derive or kill its open mechanisms, not rewrite it around data.

## D1 — Bulk field equation

Target form:

```text
L5 Ψ(X) = J(X)
Ψ_bulk(X,t) = Σ_i A_i G5(X,X_i;t-t_i) exp(i φ_i)
```

Required:
- derive `L5` from the actual SME/capped-cosh background;
- define source normalization and units;
- derive Green function/boundary conditions;
- identify propagating vs trapped/resonant modes;
- derive coherence/decoherence scale.

Kill:
- if independent-source phases necessarily wash out cross terms at all relevant scales and no SME mechanism reconstructs coherence, the coherent-interference branch fails.

## D2 — Mode normalization / A0.5-i

```text
Ψ(x,y) = Σ_n ψ_n(y) φ_n(x)
```

Required:
- normalize continuum / lowest accessible mode from the action;
- derive projection coefficient ζ;
- do not insert 1/(2π) by target-matching.

## D3 — Weyl branch / pressure closure

The old `P=0 ⇒ 1/r²` route is rejected.

Required:
- derive `U(r)` and `P(r)` together;
- test the p=2 branch requiring nonzero dark-pressure closure;
- calculate circular acceleration from the brane metric, not enclosed-density proxy alone.

## D4 — Horizon amplitude / A0.5-ii

Required:
- derive `q_H`;
- compute `q_H ζ`;
- audit the existing internal target discrepancy:
  - `1/(6π)` appears in the Third Cleave amplitude requirement;
  - `1/(3π)` appears in the highest-leverage calculation instruction.
- neither value is promoted before the derivation determines which equation was intended/correct.

## D5 — Throat transfer operator

```text
Φ_brane = C_throat[Ψ_bulk]
```

Required:
- units;
- sign;
- transfer function;
- phase mapping;
- leakage/reflection;
- conservation;
- causal timing;
- CUT state mapping.

## D6 — Fast bulk / slow 3+1 timing

```text
T_bulk = L_bulk / v_bulk
T_3+1 = D_3+1 / c
ΔT = T_3+1 - T_bulk
```

Separate:
- source emission time;
- bulk travel;
- convergence/interference buildup;
- throat delay;
- receiver response;
- photon-to-Earth delay.

## D7 — CUT three-state response

Preserve at minimum:
- `(+,-,+)`
- `(-,+,-)`

Test whether these signs are derived from geometry/state transitions rather than assigned after observation.

## D8 — micro-equivalency → macro response

```text
a_j = -(1+ξ_j) ∇Φ
δ_N = Σ m_j ξ_j / Σ m_j
η_rms ~ σ_ξ / sqrt(N_eff)
```

Required:
- identify the hidden state `X` independently;
- define micro, meso and macro response operators;
- test preconditioning and history dependence;
- keep ordinary equivalence recovery explicit.

## D9 — redshift residual branch

Use residuals only after conventional terms are modeled.

```text
Δln(1+z) = ln(1+z_obs) - ln(1+z_standard)
```

Kill:
- residual vanishes under improved standard modeling;
- residual persists but has no independently predicted dependence on model variables.

## D10 — prospective freeze

No 2026 event correlation may select coefficients.

Only after D1–D9 are resolved enough to produce a frozen mathematical candidate does the observational test unlock.
