import itertools

def ordered_kmers(alphabet, n):
    return ["".join(p) for p in itertools.product(alphabet, repeat=n)]

alphabet = ["A", "C", "G", "T"]
n = 2

for kmer in ordered_kmers(alphabet, n):
    print(kmer)
