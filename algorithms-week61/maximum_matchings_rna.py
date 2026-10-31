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

def permutations_count(n, k):
    return factorial(n) // factorial(n - k)

def max_matchings(rna):
    a, u = rna.count("A"), rna.count("U")
    g, c = rna.count("G"), rna.count("C")
    au = permutations_count(max(a, u), min(a, u))
    gc = permutations_count(max(g, c), min(g, c))
    return au * gc

fasta = """
>Rosalind_87
AUGCUUC
"""

sequences = parse_fasta(fasta)
rna = list(sequences.values())[0]

print(max_matchings(rna))
