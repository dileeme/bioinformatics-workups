monoisotopic_mass = {
    "G": 57.02146, "A": 71.03711, "S": 87.03203, "P": 97.05276,
    "V": 99.06841, "T": 101.04768, "C": 103.00919, "L": 113.08406,
    "I": 113.08406, "N": 114.04293, "D": 115.02694, "Q": 128.05858,
    "K": 128.09496, "E": 129.04259, "M": 131.04049, "H": 137.05891,
    "F": 147.06841, "R": 156.10111, "Y": 163.06333, "W": 186.07931
}

TOLERANCE = 0.001

def infer_peptide_from_spectrum(spectrum):
    nodes = sorted(spectrum)
    n = len(nodes)
    best_prev = [None] * n
    best_amino = [None] * n
    best_len = [1] * n

    for j in range(n):
        for i in range(j):
            gap = nodes[j] - nodes[i]
            for amino_acid, mass in monoisotopic_mass.items():
                if abs(gap - mass) < TOLERANCE and best_len[i] + 1 > best_len[j]:
                    best_len[j] = best_len[i] + 1
                    best_prev[j] = i
                    best_amino[j] = amino_acid
                    break

    end = max(range(n), key=lambda j: best_len[j])
    peptide = []
    j = end
    while best_prev[j] is not None:
        peptide.append(best_amino[j])
        j = best_prev[j]

    return "".join(reversed(peptide))

spectrum = [100.00000, 228.09496, 341.17902, 472.21951, 250.5]

print(infer_peptide_from_spectrum(spectrum))
