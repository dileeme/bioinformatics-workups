def expected_allele_counts(N, probabilities):
    return [2 * N * p for p in probabilities]

N = 4
probabilities = [0.1, 0.2, 0.3]

print(" ".join(f"{count:.1f}" for count in expected_allele_counts(N, probabilities)))
