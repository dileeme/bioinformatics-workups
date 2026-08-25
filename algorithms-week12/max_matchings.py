import math

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

def max_matchings(rna):
    a = rna.count("A")
    u = rna.count("U")
    g = rna.count("G")
    c = rna.count("C")
    au_pairs = math.perm(max(a, u), min(a, u))
    gc_pairs = math.perm(max(g, c), min(g, c))
    return au_pairs * gc_pairs

fasta = """
>Rosalind_92
AUGCUUC
"""

sequences = parse_fasta(fasta)
rna = list(sequences.values())[0]

print(max_matchings(rna))
