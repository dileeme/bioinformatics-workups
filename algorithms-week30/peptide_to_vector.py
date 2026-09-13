integer_mass = {"X": 4, "Z": 5}

def peptide_to_vector(peptide):
    total_mass = sum(integer_mass[amino_acid] for amino_acid in peptide)
    vector = [0] * total_mass
    prefix_mass = 0
    for amino_acid in peptide:
        prefix_mass += integer_mass[amino_acid]
        vector[prefix_mass - 1] = 1
    return vector

peptide = "XZZXX"

print(" ".join(str(value) for value in peptide_to_vector(peptide)))
