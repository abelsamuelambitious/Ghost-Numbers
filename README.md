# Ghost Numbers Verification Suite

This repository contains the computational verification engines accompanying the research paper: 
**"Ghost Numbers: Skipped Integers in the Factorial-Power Crossover"** (2026).

## Overview
This suite provides computational proofs and high-performance verification data for the structural crossover boundaries between factorial growth and power sequences. The framework is split into two distinct classes of latent integers:

* **Alpha Ghosts ($\alpha_i$):** Non-trivial integers skipped by the fixed-exponent crossover function $C_\alpha(k) = \min\{n : n! > n^k\}$. 
* **Beta Ghosts ($\beta_i$):** Non-trivial integers skipped by the base-inversion threshold function $C_\beta(k) = \min\{n : n! > k^n\}$, which scale asymptotically with Euler's number ($e$).

This suite provides empirical validation for the finite base cases, gap difference laws, and limiting distribution densities where analytic continuous limits do not apply.

## Repository Structure
* `scripts/Alpha_Ghosts.py`: High-performance engine evaluating the fixed-exponent crossover. Validates the Linear Invariant Property and tracks record-gap milestone transitions.
* `scripts/Beta_Ghosts.py`: Drift-free engine evaluating the base-inversion threshold using un-accumulated log-gamma validation. Tracks step-delta bounds ($\Delta f(k) \in \{2, 3\}$) and milestone convergence ratios.
* `scripts/verify_theorem_6_1.py`: Validation script computing fractional drift step deficits ($\varepsilon_m$) for all non-trivial ghost numbers under $100$.

## Pre-computed Datasets (Zenodo)
If you do not want to execute the computation loops locally for large limits ($k \ge 100,000$), the fully generated data suites (`Alpha_Ghosts.txt` and `Beta_Ghosts.txt`) are hosted on Zenodo. 

* **Download Alpha Ghosts Dataset:** [Zenodo Link Pending]
* **Download Beta Ghosts Dataset:** [Zenodo Link Pending]

## Getting Started

### Prerequisites
* Python 3.8 or higher
* Standard library modules (`math`, `sys`)

### Running the Verification Scripts

To execute the core Alpha Ghost generation loop (Fixed Exponent):
```bash
python scripts/Alpha_Ghosts.py
