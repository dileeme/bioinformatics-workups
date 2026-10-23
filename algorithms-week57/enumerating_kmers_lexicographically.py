from itertools import product

def ordered_kmers(alphabet, length):
    return ["".join(combo) for combo in product(alphabet, repeat=length)]

alphabet = ["A", "C", "G", "T"]
n = 2

for kmer in ordered_kmers(alphabet, n):
    print(kmer)
