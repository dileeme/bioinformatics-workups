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

def p_distance(a, b):
    diffs = sum(1 for x, y in zip(a, b) if x != y)
    return diffs / len(a)

def distance_matrix(seqs):
    matrix = []
    for a in seqs:
        row = [p_distance(a, b) for b in seqs]
        matrix.append(row)
    return matrix

fasta = """
>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA
"""

sequences = parse_fasta(fasta)
seqs = list(sequences.values())

for row in distance_matrix(seqs):
    print(" ".join(f"{d:.5f}" for d in row))
