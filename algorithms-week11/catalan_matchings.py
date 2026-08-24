import sys

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

complement = {"A": "U", "U": "A", "C": "G", "G": "C"}

def count_noncrossing_matchings(rna):
    sys.setrecursionlimit(10000)
    memo = {}

    def count(i, j):
        if j - i <= 0:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]
        total = 0
        for k in range(i + 1, j + 1, 2):
            if rna[k] == complement[rna[i]]:
                total += count(i + 1, k - 1) * count(k + 1, j)
        memo[(i, j)] = total
        return total

    return count(0, len(rna) - 1)

fasta = """
>Rosalind_57
AUAU
"""

sequences = parse_fasta(fasta)
rna = list(sequences.values())[0]

print(count_noncrossing_matchings(rna))
