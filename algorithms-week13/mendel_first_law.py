def dominant_phenotype_probability(k, m, n):
    total = k + m + n
    total_pairs = total * (total - 1)
    p_recessive = (
        n * (n - 1)
        + n * m
        + m * (m - 1) / 4
    ) / total_pairs
    return 1 - p_recessive

k, m, n = 2, 2, 2

print(f"{dominant_phenotype_probability(k, m, n):.5f}")
