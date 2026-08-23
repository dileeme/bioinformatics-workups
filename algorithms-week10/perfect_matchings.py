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
    a_count = rna.count("A")
    c_count = rna.count("C")
    return factorial(a_count) * factorial(c_count)

fasta = """
>Rosalind_23
AGCUAGUCAU
"""

sequences = parse_fasta(fasta)
rna = next(iter(sequences.values()))

print(count_perfect_matchings(rna))
