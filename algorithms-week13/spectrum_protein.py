monoisotopic_mass = {
    "G": 57.02146, "A": 71.03711, "S": 87.03203, "P": 97.05276,
    "V": 99.06841, "T": 101.04768, "C": 103.00919, "L": 113.08406,
    "I": 113.08406, "N": 114.04293, "D": 115.02694, "Q": 128.05858,
    "K": 128.09496, "E": 129.04259, "M": 131.04049, "H": 137.05891,
    "F": 147.06841, "R": 156.10111, "Y": 163.06333, "W": 186.07931
}

def infer_protein(spectrum):
    protein = ""
    for i in range(len(spectrum) - 1):
        diff = spectrum[i + 1] - spectrum[i]
        amino_acid = min(monoisotopic_mass, key=lambda aa: abs(monoisotopic_mass[aa] - diff))
        protein += amino_acid
    return protein

spectrum = [3524.8542, 3710.9335, 3841.974, 3970.0326, 4057.0646]

print(infer_protein(spectrum))
