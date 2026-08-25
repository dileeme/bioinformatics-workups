import math

def sum_combinations(n, m, modulus=1000000):
    return sum(math.comb(n, k) for k in range(m, n + 1)) % modulus

n = 6
m = 3

print(sum_combinations(n, m))
