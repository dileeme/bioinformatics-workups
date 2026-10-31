from math import comb

def sum_combinations(n, m):
    return sum(comb(n, i) for i in range(m, n + 1)) % 1000000

n = 6
m = 3

print(sum_combinations(n, m))
