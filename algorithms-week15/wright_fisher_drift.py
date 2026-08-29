from math import comb

def wright_fisher_probability(N, m, g, k):
    alleles = 2 * N
    dist = [0.0] * (alleles + 1)
    dist[g] = 1.0

    for _ in range(m):
        new_dist = [0.0] * (alleles + 1)
        for i, p in enumerate(dist):
            if p == 0.0:
                continue
            freq = i / alleles
            for j in range(alleles + 1):
                new_dist[j] += p * comb(alleles, j) * (freq ** j) * ((1 - freq) ** (alleles - j))
        dist = new_dist

    return dist[k]

N, m, g, k = 4, 3, 3, 5

print(round(wright_fisher_probability(N, m, g, k), 3))
