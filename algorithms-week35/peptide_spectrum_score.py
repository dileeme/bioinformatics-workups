integer_mass = {"X": 4, "Z": 5}

def peptide_to_vector(peptide):
    total_mass = sum(integer_mass[amino_acid] for amino_acid in peptide)
    vector = [0] * total_mass
    prefix_mass = 0
    for amino_acid in peptide:
        prefix_mass += integer_mass[amino_acid]
        vector[prefix_mass - 1] = 1
    return vector

def score_peptide(peptide, spectral_vector):
    peptide_vector = peptide_to_vector(peptide)
    return sum(s for s, p in zip(spectral_vector, peptide_vector) if p == 1)

peptide = "XZZXX"
spectral_vector = [((i * 7) % 9) - 4 for i in range(1, 23)]

print(score_peptide(peptide, spectral_vector))
