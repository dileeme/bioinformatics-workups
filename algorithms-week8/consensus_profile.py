def parse_fasta(text):
    sequences = []
    current = ""
    for line in text.strip().splitlines():
        if line.startswith(">"):
            if current:
                sequences.append(current)
            current = ""
        else:
            current += line.strip()
    if current:
        sequences.append(current)
    return sequences

def profile_matrix(sequences):
    length = len(sequences[0])
    counts = {base: [0] * length for base in "ACGT"}
    for seq in sequences:
        for i, base in enumerate(seq):
            counts[base][i] += 1
    return counts

def consensus(counts, length):
    result = []
    for i in range(length):
        best_base = max("ACGT", key=lambda base: counts[base][i])
        result.append(best_base)
    return "".join(result)

fasta = """
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

sequences = parse_fasta(fasta)
counts = profile_matrix(sequences)
print(consensus(counts, len(sequences[0])))
for base in "ACGT":
    print(base + ":", " ".join(str(n) for n in counts[base]))
