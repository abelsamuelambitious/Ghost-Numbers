import math

def f_val(n):
    """Calculates f(n) = log(n!) / log(n)"""
    return math.lgamma(n + 1) / math.log(n)

def eps(n):
    """Calculates the step deficit eps_n = 1 - (f(n) - f(n-1))"""
    return 1 - (f_val(n) - f_val(n - 1))

def generate_theorem_6_1_appendix():
    output_file = "theorem_6_1_appendix.txt"
    with open(output_file, "w") as f_out:
        f_out.write("Ghost (m) | eps_m   | 3-Step Sum (Gap 2 check) | 4-Step Sum (Gap 3 check)\n")
        f_out.write("-" * 65 + "\n")
        
        # 1. Find all ghosts up to slightly past 100
        ghosts = []
        k, n = 1, 3
        C_prev = None
        
        while n <= 150:
            if f_val(n) > k:
                if C_prev is not None and n - C_prev == 2:
                    ghosts.append(C_prev + 1)
                C_prev = n
                k += 1
            else:
                n += 1
                
        # 2. Filter for non-trivial ghosts < 100
        base_case_ghosts = [g for g in ghosts if 2 < g < 100]
        
        # 3. Calculate the required bounding sums
        for m in base_case_ghosts:
            eps_m = eps(m)
            
            # Sum of eps for m, m+1, m+2 (must be > 1 for a gap of 2)
            sum_3_step = eps(m) + eps(m+1) + eps(m+2)
            
            # Sum of eps for m, m+1, m+2, m+3 (must be > 1 for a gap of 3)
            sum_4_step = sum_3_step + eps(m+3)
            
            f_out.write(f"{m:<9d} | {eps_m:.5f} | {sum_3_step:.5f}                  | {sum_4_step:.5f}\n")
            
    print(f"Appendix data successfully written to {output_file}")

if __name__ == "__main__":
    generate_theorem_6_1_appendix()