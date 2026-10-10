from math import comb

def prob_dominant_offspring(k, m, n):
    total = k + m + n
    pairs = comb(total, 2)
    recessive_weight = comb(n, 2) + n * m * 0.5 + comb(m, 2) * 0.25
    return 1 - recessive_weight / pairs

k, m, n = 2, 2, 2

print(f"{prob_dominant_offspring(k, m, n):.5f}")
