integer_mass = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103,
    "L": 113, "N": 114, "D": 115, "K": 128, "E": 129, "M": 131,
    "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186
}

def spectrum_graph_edges(spectrum):
    edges = []
    for i in range(len(spectrum)):
        for j in range(i + 1, len(spectrum)):
            diff = spectrum[j] - spectrum[i]
            for amino_acid, mass in integer_mass.items():
                if diff == mass:
                    edges.append((spectrum[i], spectrum[j], amino_acid))
    return edges

spectrum = [57, 71, 154, 185, 301, 332, 415, 429, 486]

for s1, s2, amino_acid in spectrum_graph_edges(spectrum):
    print(f"{s1}->{s2}:{amino_acid}")
