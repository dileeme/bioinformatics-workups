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

def transition_transversion_ratio(s, t):
    transitions = {"AG", "GA", "CT", "TC"}
    ts, tv = 0, 0
    for a, b in zip(s, t):
        if a != b:
            if a + b in transitions:
                ts += 1
            else:
                tv += 1
    return ts / tv

fasta = """
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT
"""

sequences = parse_fasta(fasta)
labels = list(sequences)
s, t = sequences[labels[0]], sequences[labels[1]]

print(f"{transition_transversion_ratio(s, t):.11f}")
