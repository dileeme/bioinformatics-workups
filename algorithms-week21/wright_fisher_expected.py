def expected_allele_counts(population_size, frequencies):
    return [population_size * p for p in frequencies]

population_size = 20
frequencies = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

print(" ".join(f"{count:.3f}" for count in expected_allele_counts(population_size, frequencies)))
