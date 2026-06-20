import math
import sys

def run_beta_analysis(k_limit):
    curr_n = 1
    log_fact = 0.0  # ln(1!) = 0
    
    last_n = 1
    last_skipped_n = 0
    last_base_k = 0
    row_i = 0
    
    max_gap = 0
    milestones = []
    E = math.e
    
    print(f"Starting optimized Beta Ghosts scan up to k={k_limit:,}...")
    
    with open("Beta_Ghosts.txt", "w", encoding="utf-8") as f:
        f.write("===============================================================================================\n")
        f.write("BETA GHOST NUMBERS VERIFICATION DATA SUITE\n")
        f.write("Reference Model: min(n : n! > k^n) | Base-Inversion Threshold Crossover\n")
        f.write("===============================================================================================\n")
        f.write("COLUMN DEFINITIONS & MATHEMATICAL PROPERTIES REPLICATED BELOW:\n")
        f.write("• \u03b2_i (Ghost)     : The i-th non-trivial integer skipped by the minimal threshold function f(k).\n")
        f.write("• Base_k          : The integer base k currently under evaluation during the crossover drop.\n")
        f.write("• Threshold_f(k)  : The upper bound integer matching the current crossover point where n! > k^n.\n")
        f.write("• \u03b2_Gap (n_gap)   : The distance between consecutive Beta ghosts: \u03b2_i - \u03b2_{i-1}.\n")
        f.write("• k_Gap (k_gap)   : The distance between consecutive bases that caused a crossover shift.\n")
        f.write("• Growth_Invar    : Structurally tracks the step-delta behavior across the image space.\n")
        f.write("• m_{j}/m_{j-1}   : The convergence ratio of successive record-gap milestone beta ghosts.\n")
        f.write("                    * Note: Non-milestone rows are left blank to cleanly isolate record-gap transitions.\n")
        f.write("• |e - Ratio|     : The absolute distance between the record-gap milestone ratio and Euler's number e.\n")
        f.write("===============================================================================================\n\n")
        
        f.write(f"{'\u03b2_i (Ghost)':>12} | {'Base_k':>11} | {'Threshold_f':>11} | {'\u03b2_Gap':>7} | {'k_Gap':>7} | {'Invar':>8} | {'m_{j}/m_{j-1}':>13} | {'|e - Ratio|':>12}\n")
        f.write("-" * 115 + "\n")
        
        for k in range(1, k_limit + 1):
            log_k = math.log(k) if k > 0 else 0
            
            # Continuous evaluation condition log(n!) <= n * log(k)
            while log_fact <= (curr_n * log_k):
                curr_n += 1
                log_fact += math.log(curr_n)
            
            # If the threshold jumped by more than 1, we skipped integers (Beta Ghosts)
            if curr_n > last_n + 1:
                k_gap = k - last_base_k if last_base_k != 0 else 0
                
                for skip in range(last_n + 1, curr_n):
                    row_i += 1
                    n_gap = skip - last_skipped_n if last_skipped_n != 0 else 0
                    
                    ratio_str = f"{'':>13}"
                    e_diff_str = f"{'':>12}"
                    
                    if last_skipped_n != 0 and n_gap > max_gap:
                        max_gap = n_gap
                        milestones.append(skip)
                        if len(milestones) >= 2:
                            ratio = milestones[-1] / milestones[-2]
                            abs_e_diff = abs(E - ratio)
                            ratio_str = f"{ratio:>13.6f}"
                            e_diff_str = f"{abs_e_diff:>12.6f}"
                    
                    invar_check = curr_n - skip
                    
                    f.write(f"{skip:>12} | {k:>11} | {curr_n:>11} | {n_gap:>7} | {k_gap:>7} | {invar_check:>8} | {ratio_str} | {e_diff_str}\n")
                    last_skipped_n = skip
                
                last_base_k = k
            
            last_n = curr_n
            
            if k % 100000 == 0:
                print(f"Beta Checkpoint: k = {k:,} | Rows found: {row_i}")

if __name__ == "__main__":
    run_beta_analysis(100000)
