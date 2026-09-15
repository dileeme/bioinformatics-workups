from math import comb, log10

def loss_probability_per_generation(two_n, max_gen, start):
    dist = [0.0] * (two_n + 1)
    dist[start] = 1.0
    losses = []
    for _ in range(max_gen):
        new_dist = [0.0] * (two_n + 1)
        for i, p in enumerate(dist):
            if p == 0.0:
                continue
            freq = i / two_n
            for j in range(two_n + 1):
                new_dist[j] += p * comb(two_n, j) * (freq ** j) * ((1 - freq) ** (two_n - j))
        dist = new_dist
        losses.append(dist[0])
    return losses

def founder_effect_matrix(n, m, starts):
    two_n = 2 * n
    matrix = [loss_probability_per_generation(two_n, m, start) for start in starts]
    return [[log10(matrix[j][i]) for j in range(len(starts))] for i in range(m)]

n = 3
m = 2
starts = [1, 2, 3]

for row in founder_effect_matrix(n, m, starts):
    print(" ".join(f"{v:.4f}" for v in row))
