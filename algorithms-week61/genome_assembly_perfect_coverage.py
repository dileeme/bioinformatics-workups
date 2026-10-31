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

def assemble_cyclic_genome(reads):
    k = len(reads[0])
    overlap = k - 1
    next_read = {read[:overlap]: read for read in reads}

    genome = reads[0]
    current = reads[0]
    for _ in range(len(reads) - 1):
        current = next_read[current[-overlap:]]
        genome += current[-1]
    return genome[:len(reads)]

fasta = """
>Rosalind_m1
ATTAC
>Rosalind_m2
TACAT
>Rosalind_m3
CATTA
>Rosalind_m4
TTACA
>Rosalind_m5
ACATT
"""

sequences = parse_fasta(fasta)
reads = list(sequences.values())

print(assemble_cyclic_genome(reads))
