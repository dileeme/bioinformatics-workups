def reverse_complement(dna):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(dna))

def kmer_positions(genome, k):
    positions = {}
    for i in range(len(genome) - k + 1):
        positions.setdefault(genome[i:i + k], []).append(i)
    return positions

def shared_kmers(k, genome1, genome2):
    positions2 = kmer_positions(genome2, k)
    pairs = []
    for x in range(len(genome1) - k + 1):
        kmer = genome1[x:x + k]
        for y in positions2.get(kmer, []):
            pairs.append((x, y))
        rc = reverse_complement(kmer)
        if rc != kmer:
            for y in positions2.get(rc, []):
                pairs.append((x, y))
    return pairs

k = 3
genome1 = "AAACTCATC"
genome2 = "TTTCAAATC"

for x, y in shared_kmers(k, genome1, genome2):
    print(f"({x}, {y})")
