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

def permutations(n, k):
    return factorial(n) // factorial(n - k)

def count_maximum_matchings(rna):
    a_count = rna.count("A")
    u_count = rna.count("U")
    c_count = rna.count("C")
    g_count = rna.count("G")

    au = permutations(max(a_count, u_count), min(a_count, u_count))
    cg = permutations(max(c_count, g_count), min(c_count, g_count))

    return au * cg

fasta = """
>Rosalind_92
AUGCUUC
"""

sequences = parse_fasta(fasta)
rna = next(iter(sequences.values()))

print(count_maximum_matchings(rna))
