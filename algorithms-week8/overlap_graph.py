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

def overlap_graph(sequences, k=3):
    edges = []
    for label_a, seq_a in sequences.items():
        for label_b, seq_b in sequences.items():
            if label_a != label_b and seq_a[-k:] == seq_b[:k]:
                edges.append((label_a, label_b))
    return edges

fasta = """
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
AAATCTA
>Rosalind_0442
AAATCTA
>Rosalind_5013
GGGTGGG
"""

sequences = parse_fasta(fasta)
for a, b in overlap_graph(sequences, k=3):
    print(a, b)
