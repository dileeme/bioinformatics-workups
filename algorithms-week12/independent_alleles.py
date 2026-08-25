import math

def prob_at_least(k, n):
    population = 2 ** k
    p = 0.25
    total = 0.0
    for i in range(n, population + 1):
        total += math.comb(population, i) * (p ** i) * ((1 - p) ** (population - i))
    return total

k = 2
n = 1

print(round(prob_at_least(k, n), 3))
