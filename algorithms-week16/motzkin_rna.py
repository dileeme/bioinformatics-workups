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
    return {a, b} in ({"A", "U"}, {"C", "G"})

def count_secondary_structures(seq, modulus=1000000):
    n = len(seq)
    memo = {}

    def solve(i, j):
        if j - i <= 1:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]
        total = solve(i + 1, j)
        for k in range(i + 1, j):
            if is_complementary(seq[i], seq[k]):
                total += solve(i + 1, k) * solve(k + 1, j)
        total %= modulus
        memo[(i, j)] = total
        return total

    return solve(0, n)

fasta = """
>Rosalind_57
AUAU
"""

sequences = parse_fasta(fasta)
seq = next(iter(sequences.values()))

print(count_secondary_structures(seq))
