def parse_fasta(text):
    sequences = {}
    label = None
    for line in text.strip().splitlines():
        if line.startswith(">"):
            label = line[1:].strip()
            sequences[label] = ""
        else:
            sequences[label] += line.strip()
    return sequences

def overlap_length(a, b):
    max_len = min(len(a), len(b))
    for length in range(max_len, 0, -1):
        if a[-length:] == b[:length]:
            return length
    return 0

def shortest_superstring(reads):
    reads = list(reads)
    while len(reads) > 1:
        best_overlap, best_i, best_j, best_merged = -1, -1, -1, None
        for i in range(len(reads)):
            for j in range(len(reads)):
                if i == j:
                    continue
                ov = overlap_length(reads[i], reads[j])
                if ov > best_overlap:
                    best_overlap = ov
                    best_i, best_j = i, j
                    best_merged = reads[i] + reads[j][ov:]
        reads = [best_merged] + [r for k, r in enumerate(reads) if k != best_i and k != best_j]
    return reads[0]

fasta = """
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
"""

reads = list(parse_fasta(fasta).values())

print(shortest_superstring(reads))
