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

def build_profile(motifs, k):
    order = {"A": 0, "C": 1, "G": 2, "T": 3}
    profile = [[0.0] * k for _ in range(4)]
    for j in range(k):
        for motif in motifs:
            profile[order[motif[j]]][j] += 1
        for row in range(4):
            profile[row][j] /= len(motifs)
    return profile

def score_motifs(motifs, k):
    order = {"A": 0, "C": 1, "G": 2, "T": 3}
    score = 0
    for j in range(k):
        counts = [0, 0, 0, 0]
        for motif in motifs:
            counts[order[motif[j]]] += 1
        score += len(motifs) - max(counts)
    return score

def greedy_motif_search(dna, k, t):
    best_motifs = [text[:k] for text in dna]
    best_score = score_motifs(best_motifs, k)

    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i + k]]
        for j in range(1, t):
            profile = build_profile(motifs, k)
            motifs.append(profile_most_probable_kmer(dna[j], k, profile))
        score = score_motifs(motifs, k)
        if score < best_score:
            best_score = score
            best_motifs = motifs

    return best_motifs

dna = [
    "GGCGTTCAGGCA",
    "AAGAATCAGTCA",
    "CAAGGAGTTCGC",
    "CACGTCAATCAC",
    "CAATAATATTCG",
]
k, t = 3, 5

print(" ".join(greedy_motif_search(dna, k, t)))
