def hamming_distance(s, t):
    return sum(1 for a, b in zip(s, t) if a != b)

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}
    result = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for base in "ACGT":
                result.add(base + text)
        else:
            result.add(pattern[0] + text)
    return result

def approx_occurs(pattern, text, d):
    k = len(pattern)
    return any(hamming_distance(pattern, text[i:i + k]) <= d for i in range(len(text) - k + 1))

def motif_enumeration(dna, k, d):
    candidates = set()
    for i in range(len(dna[0]) - k + 1):
        candidates |= neighbors(dna[0][i:i + k], d)

    motifs = {
        pattern for pattern in candidates
        if all(approx_occurs(pattern, strand, d) for strand in dna)
    }
    return sorted(motifs)

dna = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
k, d = 3, 1

print(" ".join(motif_enumeration(dna, k, d)))
