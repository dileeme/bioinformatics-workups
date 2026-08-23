def expected_dominant_offspring(counts):
    probs = [1, 1, 1, 0.75, 0.5, 0]
    return sum(c * p * 2 for c, p in zip(counts, probs))

couples = [1, 0, 0, 1, 0, 1]

print(expected_dominant_offspring(couples))
