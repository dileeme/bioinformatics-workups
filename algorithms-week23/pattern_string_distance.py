def hamming_distance(s, t):
    return sum(1 for a, b in zip(s, t) if a != b)

def min_hamming_distance(pattern, text):
    k = len(pattern)
    return min(hamming_distance(pattern, text[i:i + k]) for i in range(len(text) - k + 1))

def distance_between_pattern_and_strings(pattern, dna):
    return sum(min_hamming_distance(pattern, text) for text in dna)

pattern = "AAA"
dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]

print(distance_between_pattern_and_strings(pattern, dna))
