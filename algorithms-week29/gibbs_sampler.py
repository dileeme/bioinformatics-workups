import random

def profile_with_pseudocounts(motifs, k):
    counts = {base: [1] * k for base in "ACGT"}
    for motif in motifs:
        for i, base in enumerate(motif):
            counts[base][i] += 1
    totals = [sum(counts[base][i] for base in "ACGT") for i in range(k)]
    return {base: [counts[base][i] / totals[i] for i in range(k)] for base in "ACGT"}

def score(motifs, k):
    total = 0
    for i in range(k):
        counts = {"A": 0, "C": 0, "G": 0, "T": 0}
        for motif in motifs:
            counts[motif[i]] += 1
        total += len(motifs) - max(counts.values())
    return total

def profile_randomly_generated_kmer(text, k, profile):
    kmers = [text[i:i + k] for i in range(len(text) - k + 1)]
    weights = []
    for kmer in kmers:
        prob = 1.0
        for j, base in enumerate(kmer):
            prob *= profile[base][j]
        weights.append(prob)
    return random.choices(kmers, weights=weights, k=1)[0]

def gibbs_sampler(dna, k, t, n):
    motifs = [seq[i:i + k] for seq, i in ((seq, random.randint(0, len(seq) - k)) for seq in dna)]
    best_motifs = motifs
    best_score = score(best_motifs, k)
    for _ in range(n):
        i = random.randint(0, t - 1)
        remaining = motifs[:i] + motifs[i + 1:]
        profile = profile_with_pseudocounts(remaining, k)
        motifs = motifs[:i] + [profile_randomly_generated_kmer(dna[i], k, profile)] + motifs[i + 1:]
        current_score = score(motifs, k)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs
    return best_motifs, best_score

def run(dna, k, t, n, restarts=20):
    best_motifs = None
    best_score = None
    for _ in range(restarts):
        motifs, motif_score = gibbs_sampler(dna, k, t, n)
        if best_score is None or motif_score < best_score:
            best_score = motif_score
            best_motifs = motifs
    return best_motifs, best_score

k = 8
t = 5
n = 100
dna = [
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
    "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
    "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA",
]

best_motifs, best_score = run(dna, k, t, n)
for motif in best_motifs:
    print(motif)
