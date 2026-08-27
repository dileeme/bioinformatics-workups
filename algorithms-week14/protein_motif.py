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

def find_glycosylation_motif(protein):
    positions = []
    for i in range(len(protein) - 3):
        n, x, s_or_t, p = protein[i:i + 4]
        if n == "N" and x != "P" and s_or_t in "ST" and p != "P":
            positions.append(i + 1)
    return positions

fasta = """
>Protein_1
KVNATFTNVCAMNNKNQSMLVGSNSANHTGSVLNCTPYTVSGNNSTGVA
>Protein_2
MVKAQNNSTQPNNVSPKAMLNTTGSATNSSMNSTNQSTVLNVTFANNTT
>Protein_3
GGNNTSAPLICNGTPMLASYNETKVKCHGKA
"""

sequences = parse_fasta(fasta)

for label, protein in sequences.items():
    positions = find_glycosylation_motif(protein)
    if positions:
        print(label)
        print(" ".join(str(p) for p in positions))
