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
    return sum(x != y for x, y in zip(a, b)) / len(a)

def distance_matrix(strings):
    return [[p_distance(a, b) for b in strings] for a in strings]

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
strings = list(sequences.values())

for row in distance_matrix(strings):
    print(" ".join(f"{d:.5f}" for d in row))
