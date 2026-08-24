from itertools import product

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

def kmer_composition(dna, k=4):
    kmers = ["".join(bases) for bases in product("ACGT", repeat=k)]
    counts = {kmer: 0 for kmer in kmers}
    for i in range(len(dna) - k + 1):
        counts[dna[i:i + k]] += 1
    return [counts[kmer] for kmer in kmers]

fasta = """
>Rosalind_6431
CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGGCCCTGACTACCGAACGTAATGGGATGACTCATTAAATAGAGACACGGCC
"""

sequences = parse_fasta(fasta)
dna = list(sequences.values())[0]

print(" ".join(str(c) for c in kmer_composition(dna)))
