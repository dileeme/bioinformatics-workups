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

def shortest_entry(sequences):
    return min(sequences.items(), key=lambda item: len(item[1]))

fasta = """
>JX469983.1
GATCCGTTACGGATCGGCATCGATTACGGCTAGCTAGG
>FJ817486.1
ACGGTTAGCTAGGATCCGATTACGGATCGGCTAGCTAGGACCGGTACGATTCGGATCGAT
>JX069768.1
TTGGCATCGATCGGATCCGATTACGGCTAGCTA
"""

sequences = parse_fasta(fasta)
label, seq = shortest_entry(sequences)

print(f">{label}")
print(seq)
