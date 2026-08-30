def affected_child_probability(carrier_probability):
    return carrier_probability / 4

carrier_probabilities = [0.1, 0.5, 0.8]

results = [affected_child_probability(p) for p in carrier_probabilities]
print(" ".join(f"{value:.3f}" for value in results))
