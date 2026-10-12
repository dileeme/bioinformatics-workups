monoisotopic_mass = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
    "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
    "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
    "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
    "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333,
}

def complete_spectrum(protein):
    n = len(protein)
    prefix = 0.0
    suffix = 0.0
    spectrum = []
    for i in range(n - 1):
        prefix += monoisotopic_mass[protein[i]]
        suffix += monoisotopic_mass[protein[n - 1 - i]]
        spectrum.append(prefix)
        spectrum.append(suffix)
    return spectrum

def max_multiplicity(spectrum, masses):
    counts = {}
    for x in masses:
        for y in spectrum:
            key = round(x - y, 5)
            counts[key] = counts.get(key, 0) + 1
    return max(counts.values()) if counts else 0

def best_match(proteins, masses):
    best_protein, best_score = None, -1
    for protein in proteins:
        score = max_multiplicity(complete_spectrum(protein), masses)
        if score >= best_score:
            best_score, best_protein = score, protein
    return best_score, best_protein

proteins = ["GSDMQS", "VWICN", "IASWMQS", "PVSMGAD"]
masses = [445.17838, 115.02694, 186.07931, 314.13789, 317.1198, 215.09061]

score, protein = best_match(proteins, masses)
print(score)
print(protein)
