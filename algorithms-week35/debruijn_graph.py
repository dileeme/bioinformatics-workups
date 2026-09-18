def reverse_complement(dna):
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement_map[base] for base in reversed(dna))

def de_bruijn_graph(reads):
    kmers = set(reads)
    for read in reads:
        kmers.add(reverse_complement(read))

    edges = set()
    for kmer in kmers:
        edges.add((kmer[:-1], kmer[1:]))
    return edges

reads = ["TGAT", "CATG", "TCAT", "ATGC", "CATC", "CATC"]

for prefix, suffix in sorted(de_bruijn_graph(reads)):
    print(f"({prefix}, {suffix})")
