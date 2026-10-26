def count_nucleotides(dna):
    return {base: dna.count(base) for base in "ACGT"}

dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

counts = count_nucleotides(dna)
print(counts["A"], counts["C"], counts["G"], counts["T"])
