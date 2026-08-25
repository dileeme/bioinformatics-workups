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

def longest_shared_motif(seqs):
    shortest = min(seqs, key=len)
    others = [s for s in seqs if s is not shortest]
    for length in range(len(shortest), 0, -1):
        for i in range(len(shortest) - length + 1):
            candidate = shortest[i:i + length]
            if all(candidate in s for s in others):
                return candidate
    return ""

fasta = """
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

sequences = parse_fasta(fasta)

print(longest_shared_motif(list(sequences.values())))
