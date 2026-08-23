codon_counts = {
    "A": 4, "C": 2, "D": 2, "E": 2, "F": 2, "G": 4, "H": 2, "I": 3,
    "K": 2, "L": 6, "M": 1, "N": 2, "P": 4, "Q": 2, "R": 6, "S": 6,
    "T": 4, "V": 4, "W": 1, "Y": 2,
}

def count_source_rnas(protein, modulus=1_000_000):
    total = 3
    for aa in protein:
        total = (total * codon_counts[aa]) % modulus
    return total

protein = "MA"

print(count_source_rnas(protein))
