integer_mass = {"X": 4, "Z": 5}
mass_to_amino_acid = {mass: amino_acid for amino_acid, mass in integer_mass.items()}

def vector_to_peptide(vector):
    peptide = []
    prefix_mass = 0
    for position, value in enumerate(vector, start=1):
        if value == 1:
            peptide.append(mass_to_amino_acid[position - prefix_mass])
            prefix_mass = position
    return "".join(peptide)

vector = [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]

print(vector_to_peptide(vector))
