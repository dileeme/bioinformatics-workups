from itertools import product

def enumerate_kmers(symbols, n):
    return ["".join(combo) for combo in product(symbols, repeat=n)]

symbols = ["A", "C", "G", "T"]
n = 2

for kmer in enumerate_kmers(symbols, n):
    print(kmer)
