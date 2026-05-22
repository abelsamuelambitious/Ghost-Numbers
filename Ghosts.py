import math
import time
import numpy as np
from numba import njit

@njit
def run_high_speed_analysis(k_limit):
    curr_n = 3
    log_fact = math.log(1.0) + math.log(2.0) + math.log(3.0)
    log_n = math.log(3.0)
    
    last_n = 3
    last_skipped_n = 0
    last_jump_k = 0
    row_i = 0
    max_gap = 0
    
    milestone_count = 0
    m_skips = np.zeros(100, dtype=np.int64)
    m_shift_ks = np.zeros(100, dtype=np.int64)
    m_low_ks = np.zeros(100, dtype=np.int64)
    m_high_ks = np.zeros(100, dtype=np.int64)
    m_g_gaps = np.zeros(100, dtype=np.int64)
    m_a_gaps = np.zeros(100, dtype=np.int64)
    m_laws = np.zeros(100, dtype=np.int64)
    
    for k in range(2, k_limit + 1):
        while log_fact <= k * log_n:
            curr_n += 1
            log_n = math.log(float(curr_n))
            log_fact += log_n
            
        if curr_n > last_n + 1:
            k_gap = k - last_jump_k if last_jump_k != 0 else 0
            lower_k = k - 1
            
            for skip in range(last_n + 1, curr_n):
                row_i += 1
                n_gap = skip - last_skipped_n if last_skipped_n != 0 else 0
                
                if last_skipped_n != 0 and n_gap > max_gap:
                    max_gap = n_gap
                    
                    idx = milestone_count
                    m_skips[idx] = skip
                    m_shift_ks[idx] = lower_k + row_i + 2
                    m_low_ks[idx] = lower_k
                    m_high_ks[idx] = k
                    m_g_gaps[idx] = n_gap
                    m_a_gaps[idx] = k_gap
                    m_laws[idx] = n_gap - k_gap
                    milestone_count += 1
                    
                last_skipped_n = skip
            last_jump_k = k
            
        last_n = curr_n
        
        if k % 10000000 == 0:
            print("Checkpoint: k =", k, "| Rows found:", row_i)
            
    return (m_skips[:milestone_count], m_shift_ks[:milestone_count], 
            m_low_ks[:milestone_count], m_high_ks[:milestone_count], 
            m_g_gaps[:milestone_count], m_a_gaps[:milestone_count], m_laws[:milestone_count])

if __name__ == "__main__":
    TARGET_LIMIT = 1000000000000
    
    start_time = time.time()
    res = run_high_speed_analysis(TARGET_LIMIT)
    skips, shift_ks, low_ks, high_ks, g_gaps, a_gaps, laws = res
    elapsed = time.time() - start_time
    
    print("Execution completed in seconds:", elapsed)
    
    with open("Ghosts.txt", "w", encoding="utf-8") as f:
        f.write("===============================================================================================\n")
        f.write("GHOST NUMBERS SCALE VERIFICATION MATRIX (RECORD-GAP MILESTONES ONLY)\n")
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
        
        f.write(f"{'g_i (Ghost)':>14} | {'a_i + i + 2':>14} | {'Crossover_k':>15} | {'g_Gap':>7} | {'a_Gap':>7} | {'Law_Diff':>8} | {'m_{j}/m_{j-1}':>14} | {'|e - Ratio|':>12}\n")
        f.write("-" * 115 + "\n")
        
        E = math.e
        for idx in range(len(skips)):
            ratio_str = f"{'':>14}"
            e_diff_str = f"{'':>12}"
            
            if idx >= 1:
                ratio = skips[idx] / skips[idx-1]
                abs_e_diff = abs(E - ratio)
                ratio_str = f"{ratio:>14.6f}"
                e_diff_str = f"{abs_e_diff:>12.6f}"
                
            crossover_str = f"{low_ks[idx]}-{high_ks[idx]}"
            f.write(f"{skips[idx]:>14} | {shift_ks[idx]:>14} | {crossover_str:>15} | {g_gaps[idx]:>7} | {a_gaps[idx]:>7} | {laws[idx]:>8} | {ratio_str} | {e_diff_str}\n")
