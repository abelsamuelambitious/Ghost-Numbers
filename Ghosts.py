import math
import sys

def run_analysis(k_limit):
    # O(1) Linear scan parameters derived from the paper's core theorem
    curr_n = 3
    log_fact = math.log(1) + math.log(2) + math.log(3)  # ln(3!)
    
    last_n = 3
    last_skipped_n = 0
    last_jump_k = 0
    row_i = 0  # Represents index 'i' of non-trivial ghosts
    
    max_gap = 0
    milestones = []
    E = math.e
    
    print(f"Starting optimized verification scan up to k={k_limit:,}...")
    
    with open("skips.txt", "w", encoding="utf-8") as f:
        # Step 1: Write explanatory markdown-style documentation at the top of the file
        f.write("===============================================================================================\n")
        f.write("GHOST NUMBERS VERIFICATION DATA SUITE\n")
        f.write("Reference Paper: 'Ghost Numbers: Skipped Integers in the Factorial-Power Crossover'\n")
        f.write("===============================================================================================\n")
        f.write("COLUMN DEFINITIONS & MATHEMATICAL THEOREMS REPLICATED BELOW:\n")
        f.write("• g_i (Ghost)     : The i-th non-trivial integer skipped by the crossover sequence C(k).\n")
        f.write("• a_i + i + 2     : The Linear Invariant verification value (Theorem 4.2). Must exactly equal g_i.\n")
        f.write("• Crossover_k     : The exponent interval (a_i to a_i+1) where the sequence C(k) jumps by 2.\n")
        f.write("• g_Gap (n_gap)   : The distance between consecutive ghosts, defined as n_gap = g_i - g_{i-1}.\n")
        f.write("• a_Gap (k_gap)   : The distance between consecutive lower k-values, defined as k_gap = a_i - a_{i-1}.\n")
        f.write("• Law_Diff        : The Gap Difference Law (Theorem 4.1): n_gap - k_gap. Must always equal 1.\n")
        f.write("• m_{j}/m_{j-1}   : The convergence ratio of successive record-gap milestone ghosts (Conjecture 7.1).\n")
        f.write("                    * Note: Non-milestone rows are left blank to cleanly isolate record-gap transitions.\n")
        f.write("• |e - Ratio|     : The absolute distance between the record-gap milestone ratio and Euler's number e.\n")
        f.write("===============================================================================================\n\n")
        
        # Step 2: Write aligned column headers matching the paper's exact notation
        f.write(f"{'g_i (Ghost)':>12} | {'a_i + i + 2':>11} | {'Crossover_k':>11} | {'g_Gap':>7} | {'a_Gap':>7} | {'Law_Diff':>8} | {'m_{j}/m_{j-1}':>13} | {'|e - Ratio|':>12}\n")
        f.write("-" * 115 + "\n")
        
        # Step 3: Core execution loop
        for k in range(2, k_limit + 1):
            # Linearly track exact factorial boundaries without expensive function calls
            while log_fact <= k * math.log(curr_n):
                curr_n += 1
                log_fact += math.log(curr_n)
            
            # Check for a sequence step discontinuity (jump size of 2)
            if curr_n > last_n + 1:
                k_gap = k - last_jump_k if last_jump_k != 0 else 0
                lower_k = k - 1  # This corresponds precisely to a_i in the paper
                
                for skip in range(last_n + 1, curr_n):
                    row_i += 1  
                    n_gap = skip - last_skipped_n if last_skipped_n != 0 else 0
                    
                    # Track record-gap milestones explicitly as defined in Section 5
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
                    
                    # Compute invariants and structural laws
                    shift_k = lower_k + row_i + 2  # Verifies g_i = a_i + i + 2
                    diff = n_gap - k_gap           # Verifies g_i - g_{i-1} = (a_i - a_{i-1}) + 1
                    crossover_str = f"{lower_k}-{k}"
                    
                    # Write beautifully structured outputs matching your exact dataset parameters
                    f.write(f"{skip:>12} | {shift_k:>11} | {crossover_str:>11} | {n_gap:>7} | {k_gap:>7} | {diff:>8} | {ratio_str} | {e_diff_str}\n")
                    last_skipped_n = skip
                
                last_jump_k = k
            
            last_n = curr_n
            
            if k % 100000 == 0:
                print(f"Checkpoint: k = {k:,} | Rows found: {row_i}")

if __name__ == "__main__":
    # Standard testing limit matching your reference structure
    run_analysis(10000)