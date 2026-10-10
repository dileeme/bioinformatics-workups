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

def overlap_edges(sequences, k=3):
    edges = []
    for label1, seq1 in sequences.items():
        for label2, seq2 in sequences.items():
            if label1 != label2 and seq1[-k:] == seq2[:k]:
                edges.append((label1, label2))
    return edges

fasta = """
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
"""

sequences = parse_fasta(fasta)

for label1, label2 in overlap_edges(sequences):
    print(f"{label1} {label2}")
