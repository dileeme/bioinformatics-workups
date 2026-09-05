import itertools

def hamming_distance(s, t):
    return sum(1 for a, b in zip(s, t) if a != b)

def min_hamming_distance(pattern, text):
    k = len(pattern)
    return min(hamming_distance(pattern, text[i:i + k]) for i in range(len(text) - k + 1))

def total_distance(pattern, dna):
    return sum(min_hamming_distance(pattern, text) for text in dna)

def median_string(dna, k):
    best_pattern = None
    best_distance = None
    for bases in itertools.product("ACGT", repeat=k):
        pattern = "".join(bases)
        distance = total_distance(pattern, dna)
        if best_distance is None or distance < best_distance:
            best_distance = distance
            best_pattern = pattern
    return best_pattern

dna = [
    "AAATTGACGCAT",
    "GACGACCACGTT",
    "CGTCAGCGCCTG",
    "GCTGAGCACCGG",
    "AGTACGGGACAG",
]
k = 3

print(median_string(dna, k))
