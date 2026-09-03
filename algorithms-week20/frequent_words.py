def frequent_words(text, k):
    counts = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        counts[kmer] = counts.get(kmer, 0) + 1
    max_count = max(counts.values())
    return sorted(kmer for kmer, count in counts.items() if count == max_count)

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

print(" ".join(frequent_words(text, k)))
