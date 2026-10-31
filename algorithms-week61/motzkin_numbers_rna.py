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

def is_complementary(a, b):
    return {a, b} == {"A", "U"} or {a, b} == {"C", "G"}

def count_secondary_structures(rna, mod=1000000):
    memo = {}

    def count(i, j):
        if i > j:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]
        total = count(i + 1, j)
        for k in range(i + 1, j + 1):
            if is_complementary(rna[i], rna[k]):
                total += count(i + 1, k - 1) * count(k + 1, j)
        total %= mod
        memo[(i, j)] = total
        return total

    return count(0, len(rna) - 1)

fasta = """
>Rosalind_11
AUAU
"""

sequences = parse_fasta(fasta)
rna = list(sequences.values())[0]

print(count_secondary_structures(rna))
