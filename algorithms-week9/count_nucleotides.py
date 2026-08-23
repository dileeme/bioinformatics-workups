def count_nucleotides(seq):
    return [seq.count(base) for base in "ACGT"]

dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

counts = count_nucleotides(dna)
print(" ".join(str(n) for n in counts))
