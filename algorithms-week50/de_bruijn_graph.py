def reverse_complement(dna):
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement_map[base] for base in reversed(dna))

def build_de_bruijn_graph(kmers):
    edges = set()
    for kmer in kmers:
        for strand in (kmer, reverse_complement(kmer)):
            edges.add((strand[:-1], strand[1:]))
    return edges

kmers = ["TGAT", "CATG", "TCAT", "ATGC", "CATC", "CATC"]

for prefix, suffix in build_de_bruijn_graph(kmers):
    print(f"({prefix}, {suffix})")
