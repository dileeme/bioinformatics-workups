import itertools

def hamming_distance(s, t):
    return sum(1 for a, b in zip(s, t) if a != b)

def reverse_complement(dna):
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement_map[base] for base in reversed(dna))

def approximate_count(pattern, text, d):
    k = len(pattern)
    return sum(1 for i in range(len(text) - k + 1) if hamming_distance(pattern, text[i:i + k]) <= d)

def frequent_words_with_mismatches_and_revcomp(text, k, d):
    best_count = -1
    counts = {}
    for bases in itertools.product("ACGT", repeat=k):
        pattern = "".join(bases)
        count = approximate_count(pattern, text, d) + approximate_count(reverse_complement(pattern), text, d)
        counts[pattern] = count
        if count > best_count:
            best_count = count
    return sorted(pattern for pattern, count in counts.items() if count == best_count)

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k, d = 4, 1

print(" ".join(frequent_words_with_mismatches_and_revcomp(text, k, d)))
