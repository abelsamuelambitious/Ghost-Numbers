# Ghost Numbers Verification Suite

This repository provides an optimized computational engine to verify the existence and properties of "Ghost Numbers" (skipped integers in the factorial-power crossover sequence) as defined in the research paper: *'Ghost Numbers: Skipped Integers in the Factorial-Power Crossover'*.

## Overview
The sequence $C(k)$ is defined by the crossover point where $n! > n^k$. This project implements an $O(1)$ amortized linear scan algorithm to identify non-trivial ghost numbers, verifying the structural laws proven in the paper.

## Features
- **$O(1)$ Performance:** Uses logarithmic state tracking to bypass expensive iterative searches.
- **Invariant Verification:** Automatically validates the Theorem 4.2 linear invariant ($g_i = a_i + i + 2$) for every result.
- **Law-Compliant:** Tracks Gap Differences (Theorem 4.1) and milestone convergence ratios (Conjecture 7.1).
- **Live Monitoring:** Includes progress checkpoints for large-scale computation.

## How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone the repository and navigate to the directory:
   ```bash
   git clone [your-repo-link]
   cd [repo-name]
