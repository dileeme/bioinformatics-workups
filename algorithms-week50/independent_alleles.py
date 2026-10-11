from math import comb

def prob_at_least_n_aabb(k, n):
    population = 2 ** k
    p = 0.25
    return sum(comb(population, i) * p ** i * (1 - p) ** (population - i) for i in range(n, population + 1))

k, n = 2, 1

print(f"{prob_at_least_n_aabb(k, n):.3f}")
