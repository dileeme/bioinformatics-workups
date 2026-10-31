from math import factorial

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

def count_perfect_matchings(rna):
    a = rna.count("A")
    c = rna.count("C")
    return factorial(a) * factorial(c)

fasta = """
>Rosalind_23
AGCUAGUCAU
"""

sequences = parse_fasta(fasta)
rna = list(sequences.values())[0]

print(count_perfect_matchings(rna))
