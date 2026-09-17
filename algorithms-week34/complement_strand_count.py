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

def reverse_complement(dna):
    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement_map[base] for base in reversed(dna))

def count_self_reverse_complements(sequences):
    return sum(1 for seq in sequences if seq == reverse_complement(seq))

fasta = """
>Rosalind_64
ATGCATGC
>Rosalind_78
AGCCTAGT
>Rosalind_29
ACGTACGT
>Rosalind_44
ACGGGCACGT
"""

sequences = parse_fasta(fasta)
print(count_self_reverse_complements(sequences.values()))
