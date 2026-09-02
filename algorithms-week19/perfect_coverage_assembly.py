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

def assemble_circular_genome(reads):
    k = len(reads[0])
    next_read = {read[:-1]: read for read in reads}

    genome = reads[0]
    while len(genome) < len(reads):
        key = genome[-(k - 1):]
        genome += next_read[key][-1]

    return genome[:len(reads)]

fasta = """
>Rosalind_1
TTC
>Rosalind_2
GAA
>Rosalind_3
GCT
>Rosalind_4
CGA
>Rosalind_5
AAG
>Rosalind_6
AGC
>Rosalind_7
TCG
>Rosalind_8
CTT
"""

sequences = parse_fasta(fasta)
reads = list(sequences.values())

print(assemble_circular_genome(reads))
