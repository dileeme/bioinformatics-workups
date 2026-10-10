def count_nucleotides(dna):
    return [dna.count(base) for base in "ACGT"]

dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

print(" ".join(str(n) for n in count_nucleotides(dna)))
