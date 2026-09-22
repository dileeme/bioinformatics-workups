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

def n_stat(lengths, threshold):
    lengths = sorted(lengths, reverse=True)
    total = sum(lengths)
    target = total * threshold
    running = 0
    for length in lengths:
        running += length
        if running >= target:
            return length
    return 0

fasta = """
>Rosalind_1
GCATCGCA
>Rosalind_2
CTGACCCTGT
>Rosalind_3
TTACGTTAGCC
>Rosalind_4
CTGAACTCGGGTTA
>Rosalind_5
CATTGGGATTCCTTAGATTGGC
>Rosalind_6
ATCTTCGATGCACTGCAAGCTGCAATA
"""

sequences = parse_fasta(fasta)
lengths = [len(seq) for seq in sequences.values()]

n50 = n_stat(lengths, 0.5)
n75 = n_stat(lengths, 0.75)

print(n50)
print(n75)
