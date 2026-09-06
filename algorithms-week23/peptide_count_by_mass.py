amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def count_peptides_with_mass(mass):
    counts = [0] * (mass + 1)
    counts[0] = 1
    for m in range(1, mass + 1):
        counts[m] = sum(counts[m - aa] for aa in amino_acid_masses if aa <= m)
    return counts[mass]

mass = 1024

print(count_peptides_with_mass(mass))
