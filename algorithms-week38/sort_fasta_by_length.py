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

def sort_by_length(sequences):
    return sorted(sequences.items(), key=lambda item: len(item[1]))

fasta = """
>NM_001185097.2
ACGGCGCTGCTATTCGTCATCTAG
>NM_000581.3
CTGCGATTGACCTAGTTAG
>NM_001008541.1
ACGTGCCTAGGCTAGATCCGATCAAGCTAGGT
"""

sequences = parse_fasta(fasta)

for label, seq in sort_by_length(sequences):
    print(f">{label}")
    print(seq)
