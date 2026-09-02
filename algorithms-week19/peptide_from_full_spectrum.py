monoisotopic_mass = {
    "G": 57.02146, "A": 71.03711, "S": 87.03203, "P": 97.05276,
    "V": 99.06841, "T": 101.04768, "C": 103.00919, "L": 113.08406,
    "I": 113.08406, "N": 114.04293, "D": 115.02694, "Q": 128.05858,
    "K": 128.09496, "E": 129.04259, "M": 131.04049, "H": 137.05891,
    "F": 147.06841, "R": 156.10111, "Y": 163.06333, "W": 186.07931
}

TOLERANCE = 0.001

def infer_peptide(masses):
    k = len(masses) // 2 + 1
    sorted_masses = sorted(masses)
    total_mass = sorted_masses[0] + sorted_masses[-1]
    nodes = sorted(set([0.0, total_mass] + masses))

    path = []

    def search(node_index, remaining):
        if remaining == 0:
            return node_index == len(nodes) - 1
        for j in range(node_index + 1, len(nodes)):
            gap = nodes[j] - nodes[node_index]
            for amino_acid, mass in monoisotopic_mass.items():
                if abs(gap - mass) < TOLERANCE:
                    path.append(amino_acid)
                    if search(j, remaining - 1):
                        return True
                    path.pop()
                    break
        return False

    search(0, k)
    return "".join(path)

masses = [
    97.05276, 253.15387, 354.20155, 483.24414, 669.32345,
    629.29215, 473.19104, 372.14336, 243.10077, 57.02146
]

print(infer_peptide(masses))
