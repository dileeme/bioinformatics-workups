monoisotopic_mass = {
    "G": 57.02146, "A": 71.03711, "S": 87.03203, "P": 97.05276,
    "V": 99.06841, "T": 101.04768, "C": 103.00919, "L": 113.08406,
    "I": 113.08406, "N": 114.04293, "D": 115.02694, "Q": 128.05858,
    "K": 128.09496, "E": 129.04259, "M": 131.04049, "H": 137.05891,
    "F": 147.06841, "R": 156.10111, "Y": 163.06333, "W": 186.07931,
}

def infer_protein(spectrum):
    protein = ""
    for i in range(len(spectrum) - 1):
        diff = spectrum[i + 1] - spectrum[i]
        closest = min(monoisotopic_mass, key=lambda aa: abs(monoisotopic_mass[aa] - diff))
        protein += closest
    return protein

spectrum = [0.0, 186.07931, 317.1198, 445.17838, 532.21041, 688.31152, 791.32071]

print(infer_protein(spectrum))
