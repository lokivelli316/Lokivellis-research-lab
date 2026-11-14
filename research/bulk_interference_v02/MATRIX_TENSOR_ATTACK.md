# Matrix / Tensor Attack Specification

## Four primary objects

- **T** — theory/mechanism tensor
- **O** — observations/receivers tensor
- **P** — propagation/timing tensor
- **N** — null/confounder tensor

## Theory axes

SME routing, bulk modes, throat transfer, CUT phase, PMAE parameter status, micro-equivalency, macro emergence, receiver transfer, redshift residual.

## Observation axes

Sun/heliosphere, main-sequence stars, white dwarfs, pulsars, magnetars, FRBs, AGN/jets, SNe/threshold systems, galaxy redshift residuals.

## Attack operators

1. Tensor contraction across shared dimensions.
2. Lagged cross-correlation.
3. SVD / low-rank residual search.
4. PCA / latent-variable inspection.
5. Partial correlation / nuisance regression.
6. Bayesian model comparison.
7. Time shuffle.
8. Sky-position shuffle.
9. Random-phase scramble.
10. CUT-order permutation.
11. Receiver-class permutation.
12. Channel ablation: bulk off / 3+1 off / throat off / micro layer off.
13. Null replacement with standard astrophysical models.
14. Out-of-sample holdout.

## Nested keystone requirement

A single parameterization must predict at least three independently evaluated families:
- timing;
- phase/sign;
- micro→macro receiver response.

No family may be refit independently and then counted as corroboration.

## Failure rule

A broken lane is a coordinate, not a vote. It spawns a narrower attack. Tool failure is HOLD, not evidence against the theory.
