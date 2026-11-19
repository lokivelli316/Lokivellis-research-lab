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

## Additive causal / negative-space matrices

The four primary objects T/O/P/N remain unchanged. The following derived matrices are added for adversarial bookkeeping and are never substitutes for T/O/P/N:

- **C** — causal-stage matrix: correlation, temporal order, propagation, convergence, coupling, receiver trigger, mechanism, causal discrimination, prospective prediction.
- **Q** — confusion / negative-space matrix: TP, FP, FN, TN plus base rates.
- **R** — receiver-susceptibility matrix: receiver class × hidden/local state × history × phase × response.
- **A** — alternative-model matrix: H0/H1/H2/H3/H4/HCC/HS/HA/HB/HC.
- **E** — evidence-state matrix: independent status coordinates rather than one collapsed verdict.

### Q — confusion matrix

| | Event E | No event ¬E |
|---|---:|---:|
| Predicted bulk condition Ψ | TP | FP |
| No predicted bulk condition ¬Ψ | FN | TN |

When data permit, derive sensitivity, specificity, precision, negative predictive value, false-positive rate, false-negative rate, base event rate, likelihood ratios and calibration.

A high TP count without FP/FN/TN is not a successful attack.

### A — alternative-model matrix

Every candidate must be evaluated against:

```text
H0  = ordinary astrophysics + coincidence/systematics
H1  = ordinary 3+1 propagation
H2  = bulk interference + throat coupling
H3  = ordinary + bulk additive
H4  = ordinary × bulk interaction / susceptibility coupling
HCC = common cause
HS  = selection / measurement / cadence / pipeline systematic
HA  = linear bulk interference
HB  = geometric focusing / caustics
HC  = nonlinear buildup + throat discharge/backfire
```

Ordinary and bulk channels may both remain causally real. Never delete one merely to simplify the comparison.

### C — causal-stage matrix

```text
correlation
→ temporal ordering
→ physically allowed propagation
→ convergence / interference
→ coupling
→ receiver susceptibility / trigger
→ explicit mechanism
→ causal discrimination
→ prospective prediction
```

No arrow is automatic and no stage silently promotes into the next.

### R — receiver matrix

For receiver class r:

```text
R_r[Ψ, X_r, history, phase]
P(E_r | Ψ, X_r)
P(E_r | ¬Ψ, X_r)
```

The same candidate bulk condition must be tested across responders and non-responders, including the existing observation axes. Receiver specificity is a prediction only if both positive and negative classes are specified.

### Additional attack operators

15. Positive-twin search: find all other targets satisfying the same frozen criteria.
16. Negative-twin search: matched ordinary controls without the target outcome.
17. Nearest-false-positive search.
18. Nearest-false-negative search.
19. Blind retrieval: score/rank the full population before revealing labels.
20. Base-rate audit and denominator recovery.
21. Hypothesis inversion.
22. Source/receiver role reversal where mathematically meaningful.
23. Common-cause graph attack: A→B, B→A, C→A/C→B, pipeline S→A/S→B.
24. Parallel-channel comparison: 3+1 only / bulk only / additive / interaction.
25. Receiver-susceptibility ablation.
26. History-dependence ablation.
27. Phase-information ablation.
28. Leave-one-target-out analysis.
29. Leave-one-receiver-class-out analysis.
30. Prospective/post-hoc partition with frozen coefficients.
31. Strongest-surviving-alternative comparison.

## Mandatory paired questions

Every positive-looking contraction, correlation, residual, rank or event match must return its paired negative-space answers:

```text
What fits?
Who else fits?
Who fits better?
Who should fit but does not?
Who should not fit but does?
What is the strongest matched counterexample?
What is the strongest false positive?
What is the strongest false negative?
What happens when the condition is inverted?
What happens when labels are hidden?
What common cause survives?
What ordinary explanation survives?
What assumption did the matrix never vary?
What the hell did we not ask that we should have asked already?
```

## Evidence-state matrix

Never collapse these coordinates into one SUPPORT label:

```text
DERIVATION
PROPAGATION
CONVERGENCE / INTERFERENCE
COUPLING
RECEIVER SUSCEPTIBILITY
CORRELATION
TEMPORAL ORDER
MECHANISM
COMMON-CAUSE CLEARANCE
NEGATIVE-CONTROL SURVIVAL
FALSE-POSITIVE CONTROL
FALSE-NEGATIVE CONTROL
BLIND-RANK PERFORMANCE
CAUSAL DISCRIMINATION
PROSPECTIVE STATUS
REPLICATION
```

Allowed states remain explicit: VERIFIED / PARTIALLY VERIFIED / UNKNOWN / UNCONFIGURED / READY / HOLD / BLOCKED / NOT_STARTED / KILLED.

The full matrix, including ugly cells, stays in the record.
