import random

def profile_with_pseudocounts(motifs, k):
    counts = {base: [1] * k for base in "ACGT"}
    for motif in motifs:
        for i, base in enumerate(motif):
            counts[base][i] += 1
    totals = [sum(counts[base][i] for base in "ACGT") for i in range(k)]
    return {base: [counts[base][i] / totals[i] for i in range(k)] for base in "ACGT"}

def profile_most_probable_kmer(text, k, profile):
    best_kmer = text[:k]
    best_prob = -1
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = 1.0
        for j, base in enumerate(kmer):
            prob *= profile[base][j]
        if prob > best_prob:
            best_prob = prob
            best_kmer = kmer
    return best_kmer

def score(motifs, k):
    total = 0
    for i in range(k):
        counts = {"A": 0, "C": 0, "G": 0, "T": 0}
        for motif in motifs:
            counts[motif[i]] += 1
        total += len(motifs) - max(counts.values())
    return total

def randomized_motif_search(dna, k, t):
    motifs = [seq[i:i + k] for seq, i in ((seq, random.randint(0, len(seq) - k)) for seq in dna)]
    best_motifs = motifs
    best_score = score(best_motifs, k)
    while True:
        profile = profile_with_pseudocounts(motifs, k)
        motifs = [profile_most_probable_kmer(seq, k, profile) for seq in dna]
        current_score = score(motifs, k)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs
        else:
            return best_motifs, best_score

def run(dna, k, t, restarts=1000):
    best_motifs = None
    best_score = None
    for _ in range(restarts):
        motifs, motif_score = randomized_motif_search(dna, k, t)
        if best_score is None or motif_score < best_score:
            best_score = motif_score
            best_motifs = motifs
    return best_motifs, best_score

k = 8
t = 5
dna = [
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
    "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
    "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA",
]

best_motifs, best_score = run(dna, k, t)
for motif in best_motifs:
    print(motif)
