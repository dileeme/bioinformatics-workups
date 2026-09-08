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

def n_statistic(lengths, percent):
    total = sum(lengths)
    threshold = total * percent
    cumulative = 0
    for length in sorted(lengths, reverse=True):
        cumulative += length
        if cumulative >= threshold:
            return length

fasta = """
>Rosalind_1
CAGATTTTCATATTATGCAG
>Rosalind_2
AAAATCTACTTCGCCTGATACGAGTCGGTTATCTTCGGAT
>Rosalind_3
ACTGTATAGT
>Rosalind_4
CCCACCTGGTGATCCTATGCTTGTGAGTACCCAGAAAATA
>Rosalind_5
GCGACGGACCGCGGTGTTAA
"""

sequences = parse_fasta(fasta)
lengths = [len(seq) for seq in sequences.values()]

print(n_statistic(lengths, 0.5))
print(n_statistic(lengths, 0.75))
