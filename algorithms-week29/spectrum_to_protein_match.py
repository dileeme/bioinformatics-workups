from collections import Counter

monoisotopic_mass = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
    "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
    "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
    "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
    "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333,
}

def complete_spectrum(protein):
    prefix_mass = [0.0]
    for acid in protein:
        prefix_mass.append(prefix_mass[-1] + monoisotopic_mass[acid])
    total = prefix_mass[-1]
    masses = []
    for mass in prefix_mass:
        masses.append(mass)
        masses.append(total - mass)
    return masses

def max_multiplicity(spectrum, protein):
    differences = Counter()
    for r in spectrum:
        for s in complete_spectrum(protein):
            differences[round(r - s, 5)] += 1
    return max(differences.values())

def best_matching_protein(proteins, spectrum):
    best_protein = None
    best_multiplicity = -1
    for protein in proteins:
        multiplicity = max_multiplicity(spectrum, protein)
        if multiplicity > best_multiplicity:
            best_multiplicity = multiplicity
            best_protein = protein
    return best_multiplicity, best_protein

proteins = ["GSDMQS", "VWICN", "IASWMQS", "PVSMGAD"]
spectrum = [445.17838, 115.02694, 186.07931, 314.13789, 317.1198, 215.09061]

multiplicity, protein = best_matching_protein(proteins, spectrum)
print(multiplicity)
print(protein)
