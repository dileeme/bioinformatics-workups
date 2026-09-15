from math import comb

def total_splice_variants(n, m, modulus=1000000):
    return sum(comb(n, k) for k in range(m, n + 1)) % modulus

n, m = 20, 13

print(total_splice_variants(n, m))
