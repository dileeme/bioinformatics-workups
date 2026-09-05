def find_clumps(genome, k, L, t):
    result = set()
    counts = {}

    for i in range(min(L, len(genome)) - k + 1):
        kmer = genome[i:i + k]
        counts[kmer] = counts.get(kmer, 0) + 1
    for kmer, count in counts.items():
        if count >= t:
            result.add(kmer)

    for start in range(1, len(genome) - L + 1):
        old_kmer = genome[start - 1:start - 1 + k]
        counts[old_kmer] -= 1
        new_kmer = genome[start + L - k:start + L]
        counts[new_kmer] = counts.get(new_kmer, 0) + 1
        if counts[new_kmer] >= t:
            result.add(new_kmer)

    return result

genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
k, L, t = 5, 75, 4

print(" ".join(sorted(find_clumps(genome, k, L, t))))
