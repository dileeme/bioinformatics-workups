monoisotopic_mass = {
    "G": 57.02146, "A": 71.03711, "S": 87.03203, "P": 97.05276,
    "V": 99.06841, "T": 101.04768, "C": 103.00919, "L": 113.08406,
    "I": 113.08406, "N": 114.04293, "D": 115.02694, "Q": 128.05858,
    "K": 128.09496, "E": 129.04259, "M": 131.04049, "H": 137.05891,
    "F": 147.06841, "R": 156.10111, "Y": 163.06333, "W": 186.07931,
}

def complete_spectrum(protein):
    masses = [monoisotopic_mass[aa] for aa in protein]
    prefix, suffix = [], []
    total = 0
    for m in masses[:-1]:
        total += m
        prefix.append(total)
    total = 0
    for m in reversed(masses[:-1]):
        total += m
        suffix.append(total)
    return prefix + suffix

def multiplicity(a, b, tolerance=0.001):
    a, b = sorted(a), sorted(b)
    i = j = count = 0
    while i < len(a) and j < len(b):
        if abs(a[i] - b[j]) < tolerance:
            count += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return count

def best_match(proteins, spectrum):
    best_protein, best_count = None, -1
    for protein in proteins:
        count = multiplicity(complete_spectrum(protein), spectrum)
        if count > best_count:
            best_protein, best_count = protein, count
    return best_count, best_protein

proteins = ["PRTEIN", "GSAKLW", "MDVQHC"]
spectrum = complete_spectrum("PRTEIN")

count, protein = best_match(proteins, spectrum)
print(count)
print(protein)
