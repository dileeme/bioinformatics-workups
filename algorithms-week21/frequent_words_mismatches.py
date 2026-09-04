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

def frequent_words_with_mismatches(text, k, d):
    counts = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        for neighbor in neighbors(pattern, d):
            counts[neighbor] = counts.get(neighbor, 0) + 1

    max_count = max(counts.values())
    return sorted(kmer for kmer, count in counts.items() if count == max_count)

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k, d = 4, 1

print(" ".join(frequent_words_with_mismatches(text, k, d)))
