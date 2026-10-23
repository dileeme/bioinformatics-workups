def reverse_complement(dna):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(dna))

dna = "AAAACCCGGT"

print(reverse_complement(dna))
