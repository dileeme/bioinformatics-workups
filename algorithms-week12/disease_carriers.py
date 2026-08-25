import math

def carrier_probabilities(aa_frequencies):
    results = []
    for aa_freq in aa_frequencies:
        q = math.sqrt(aa_freq)
        p = 1 - q
        results.append(1 - p ** 2)
    return results

aa_frequencies = [0.1, 0.25, 0.5]

print(" ".join(f"{p:.3f}" for p in carrier_probabilities(aa_frequencies)))
