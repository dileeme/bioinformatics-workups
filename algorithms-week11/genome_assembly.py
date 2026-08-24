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

def assemble_genome(reads):
    reads = list(reads)
    while len(reads) > 1:
        best = (0, -1, -1, "")
        for i in range(len(reads)):
            for j in range(len(reads)):
                if i == j:
                    continue
                length = overlap_length(reads[i], reads[j])
                if length > best[0]:
                    merged = reads[i] + reads[j][length:]
                    best = (length, i, j, merged)
        _, i, j, merged = best
        reads = [read for k, read in enumerate(reads) if k not in (i, j)]
        reads.append(merged)
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

sequences = parse_fasta(fasta)
reads = list(sequences.values())

print(assemble_genome(reads))
