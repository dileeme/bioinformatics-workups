def profile_most_probable_kmer(text, k, profile):
    order = {"A": 0, "C": 1, "G": 2, "T": 3}
    best_kmer = text[:k]
    best_prob = -1
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = 1
        for j, base in enumerate(kmer):
            prob *= profile[order[base]][j]
        if prob > best_prob:
            best_prob = prob
            best_kmer = kmer
    return best_kmer

text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
profile = [
    [0.2, 0.2, 0.3, 0.2, 0.3],
    [0.4, 0.3, 0.1, 0.5, 0.1],
    [0.3, 0.3, 0.5, 0.2, 0.4],
    [0.1, 0.2, 0.1, 0.1, 0.2],
]

print(profile_most_probable_kmer(text, k, profile))
