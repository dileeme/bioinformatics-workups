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

def find_spliced_motif(s, t):
    positions = []
    i = 0
    for char in t:
        while s[i] != char:
            i += 1
        positions.append(i + 1)
        i += 1
    return positions

fasta = """
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA
"""

sequences = parse_fasta(fasta)
s, t = list(sequences.values())

print(" ".join(str(p) for p in find_spliced_motif(s, t)))
