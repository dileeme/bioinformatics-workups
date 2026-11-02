def reverse_complement(seq):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(seq))

def assemble_genome(reads):
    read_len = len(reads[0])
    for k in range(read_len, 1, -1):
        kmers = set()
        for read in reads:
            for seq in (read, reverse_complement(read)):
                for i in range(len(seq) - k + 1):
                    kmers.add(seq[i:i + k])

        out_edge = {}
        in_count = {}
        consistent = True
        for kmer in kmers:
            prefix, suffix = kmer[:-1], kmer[1:]
            if prefix in out_edge and out_edge[prefix] != suffix:
                consistent = False
                break
            out_edge[prefix] = suffix
            in_count[suffix] = in_count.get(suffix, 0) + 1

        if not consistent or any(count != 1 for count in in_count.values()):
            continue
        if set(out_edge.keys()) != set(in_count.keys()):
            continue

        start = next(iter(out_edge))
        cycle = [start]
        node = out_edge[start]
        while node != start:
            cycle.append(node)
            node = out_edge[node]

        return "".join(n[0] for n in cycle)

    return None

reads = [
    "GAAACT", "AAACTT", "CAAGTT", "ACTTGT", "AACAAG", "CAACAA",
    "TGTTGG", "GCCAAC", "GGCCAA", "GGGCCA", "GGCCCA", "GCCCAG",
    "CCCAGT", "CCAGTG", "TCACTG", "AGTGAA", "GTGAAA", "TGAAAC",
]

print(assemble_genome(reads))
